# CluedIn REST API tester

A small Python tool that authenticates to a CluedIn instance and smoke-tests its
REST endpoints. It takes **url + client_id + username + password**, obtains an
OAuth **bearer token**, and uses that token to call a catalog of endpoints —
**GraphQL-backed endpoints first**, because GraphQL is CluedIn's primary query
mechanism.

## Why GraphQL is prioritised

Of all 173 controllers, only two actually *execute* GraphQL — and they **are** the
GraphQL endpoints:

| Controller | Route | Notes |
|---|---|---|
| `PublicApiGraphQLController` | `POST api/v1/graphql` | Public GraphQL API |
| `Consume/GraphQLController`  | `POST api/graphql`    | Internal / UI GraphQL |

Both run `CluedInGraphQLExecuter.ExecuteAsync(...)` against one shared schema
(`Core.GraphQL/CluedInQuery.cs`) exposing `me`, `entity`, `latest`, `upcoming`,
and `search`. Other controllers only *import* GraphQL types for serialization;
they don't run queries. These two are tagged `priority: graphql` in the catalog
and run/report first.

## How auth works (derived from the codebase)

- `client_id` is the **organization subdomain** (`ApplicationSubDomain`);
  organization clients are **public** (`RequireClientSecret = false`) and allow the
  `password` grant (`CluedInResourceOwnerPasswordValidator`, `ClientDataStore`).
- The token request is form-urlencoded:
  `grant_type=password&username=..&password=..&client_id=..`
- The token endpoint is resolved via OpenID discovery
  (`<auth-url>/.well-known/openid-configuration`), falling back to
  `<auth-url>/connect/token` then `<auth-url>/token`.
- API calls send `Authorization: Bearer <access_token>`.
- In **local dev** the auth server and API are on different ports
  (`9001` auth, `9000` API) — use `--auth-url`/`--api-url`. In hosted instances
  they're usually the same host, so a single `--url` is enough.

## Install

```bash
cd _tools/api-tester
python -m venv .venv && . .venv/Scripts/activate    # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Usage

```bash
# Hosted instance (auth + API same host)
python -m cluedin_api_tester \
  --url https://app.example.cluedin.com \
  --client-id mycompany \
  --username admin@mycompany.com \
  --password '***'

# Local dev (separate ports), GraphQL + priority areas only, self-signed certs
python -m cluedin_api_tester \
  --auth-url http://localhost:9001 \
  --api-url  http://localhost:9000 \
  --client-id consoleApp \
  --username Tim \
  --password jerrong \
  --only graphql,high \
  --insecure \
  --markdown run.md --json run.json
```

The password may also be supplied via the `CLUEDIN_PASSWORD` environment variable,
or entered at a secure prompt if omitted.

### Useful flags

| Flag | Purpose |
|---|---|
| `--only graphql,high` | Run only chosen priorities/categories (e.g. `graphql`, `high`, `Search`, `Glossary`). |
| `--context entity_id=<guid>` | Fill `{placeholder}` params; parameterized endpoints SKIP without them. Repeatable. |
| `--include-mutations` | Also run endpoints flagged `destructive` (writes). **Off by default.** |
| `--list` | Print the endpoints that would run (with priority/flags) and exit. |
| `--token-endpoint <url>` | Skip discovery and post directly to this token URL. |
| `--insecure` | Disable TLS verification (local self-signed certs). |
| `--json` / `--markdown` | Write machine- and human-readable reports. |

## Result statuses

| Status | Meaning |
|---|---|
| `PASS` | Expected HTTP status, or GraphQL returned `data` with no `errors`. |
| `FORBIDDEN` | `403` — token is valid but the user's role/RACI lacks access (endpoint exists). |
| `FAIL` | Unexpected status, or GraphQL `errors`. |
| `AUTH` | `401` — token rejected/expired. |
| `SKIP` | Missing `{context}` value, or a destructive endpoint without `--include-mutations`. |
| `ERROR` | Connection/transport failure. |

Exit code is non-zero if any `FAIL`, `AUTH`, or `ERROR` occurred (CI-friendly).

## Troubleshooting

### `405 Method Not Allowed` / an HTML page when getting the token

This means the POST hit a reverse proxy or SPA, **not** IdentityServer — almost
always a base-URL/prefix issue, not bad credentials. Hosted CluedIn proxies each
backend under a path prefix (from `SystemConfigurationEx`):

The gateway **strips the prefix** before routing to the backend, but each backend's
controller routes already start with `api/`. So the public base URL must *include*
the prefix:

| Backend | Public base | Example full URL |
|---|---|---|
| AuthenticationServer (IdentityServer) | `https://<host>/auth` | `POST https://<host>/auth/connect/token` |
| Server.WebApi (Search/Rules/Glossary…) | `https://<host>/api` | `GET https://<host>/api/api/v1/rules` |
| PublicApi.WebApi (public GraphQL, Clue, enrichment) | `https://<host>/public` | `POST https://<host>/public/api/v1/graphql` |

> The Server.WebApi example looks like it has “`api`” twice — that's correct. The
> gateway eats the first `/api`, leaving `/api/v1/rules`, which is the controller's
> real route. (For `/public`, the prefix differs from the route, so it reads
> naturally.) Omitting the prefix makes the gateway strip `/api/v1/rules` down to
> `/v1/rules` (→ 404) or `/search` down to a single segment that the API's greedy
> `GET /{id}` route answers with **400 "Cannot retrieve entity info with an invalid
> GUID"** — the tell-tale sign you're missing the prefix.

**You usually don't need to set any of this.** Once the token endpoint is found under
`/auth`, the tool infers a reverse-proxied deployment and automatically uses
`https://<host>/api` and `https://<host>/public` as the bases. So this just works:

```bash
python -m cluedin_api_tester -v \
  --url https://<host> \
  --client-id <org-subdomain> --username <you> --password '***'
```

You'll see a line like:
`Detected reverse-proxied deployment (auth under '/auth'). Using api_url=.../api  public_api_url=.../public`.

Override only if your instance uses non-default prefixes:

```bash
python -m cluedin_api_tester \
  --url https://<host> \
  --api-url https://<host>/<your-api-prefix> \
  --public-api-url https://<host>/<your-public-prefix> \
  --client-id <org-subdomain> --username <you> --password '***'
```

### Token works but specific API calls return 404 / 400 "invalid GUID"

You're missing or mismatching a service prefix. Server.WebApi endpoints use
`base: server` (→ `--api-url`, default `https://<host>/api`); public
GraphQL/Clue/enrichment endpoints use `base: public` (→ `--public-api-url`, default
`https://<host>/public`). A **400 "Cannot retrieve entity info with an invalid GUID"**
on endpoints like `api/search`/`api/streams` specifically means the `/api` prefix was
dropped and the request hit the API's catch-all `GET /{id}` route — set
`--api-url https://<host>/api`.

### `400` with `invalid_grant` / `invalid_client`

That *is* a genuine auth error (the tool surfaces `error_description` verbatim):
check the `client_id` is the **organization subdomain**, the org is Active, and the
user/password are valid.

## Extending the catalog

Edit [`endpoints.yaml`](endpoints.yaml). Each entry maps to one request. Use
`priority: graphql|high|normal`, `params:` for query strings, `body:` for POST/PUT
JSON, `graphql_query:` for GraphQL, and `{placeholder}` tokens resolved from
`--context`. Mark any writing call `destructive: true` so it's opt-in only.

> **Note on parameter names:** a few GET endpoints (e.g. `api/search`) take query
> parameters whose exact names vary by version. The catalog uses best-effort
> defaults; if an endpoint returns `400`, adjust its `params:` in the YAML. The
> GraphQL introspection calls are version-proof and are the most reliable signal.
