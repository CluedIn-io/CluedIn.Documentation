---
layout: cluedin
nav_order: 010
parent: Data engineering playbook
grand_parent: Playbooks
permalink: /playbooks/data-engineering-playbook/python-sdk
tags: ["python"]
last_modified: 2026-09-03
title: CluedIn Python SDK
summary: "CluedIn Python SDK provides powerful REST and GraphQL APIs to interact with your CluedIn instance programmatically."
---

## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

CluedIn provides powerful REST and GraphQL APIs. To simplify programmatic interaction, we offer the [CluedIn Python SDK](https://pypi.org/project/cluedin/) — a Python package that handles authentication, automation, data import and export, data transformation, and data exploration.

You can use CluedIn Python SDK in many environments, from your local laptop to cloud services like:

- [Microsoft Fabric](https://www.microsoft.com/en-us/microsoft-fabric)
- [Azure Synapse Analytics](https://azure.microsoft.com/en-us/products/synapse-analytics)
- [Databricks](https://www.databricks.com/)
- [Snowflake](https://www.snowflake.com/)
- [Azure Functions](https://azure.microsoft.com/en-us/products/functions)
- [Jupyter Notebook](https://jupyter.org/)
- [Google Colab](https://colab.research.google.com/)
- [Airflow](https://airflow.apache.org/)
- [dbt](https://www.getdbt.com/)
- [Kaggle](https://www.kaggle.com/)

The above list is non-exhaustive. You can use CluedIn Python SDK in any environment where you can run Python code.

Some of the scenarios where CluedIn Python SDK will be helpful are:
- Querying data from your CluedIn instance.
- Exporting and saving the data to CSV, Parquet, Excel, JSON, or many other file formats.
- Reading and writing configuration of your CluedIn instance.
- Ingesting data in CluedIn.
- Automating repetitive actions to reduce manual work in UI.

## Getting started

[CluedIn Python SDK](https://pypi.org/project/cluedin/) requires Python 3.10 or later (`>=3.10,<4.0`).

### Local environment

When you run Python scripts or notebooks on your local machine, we recommend using virtualenv or venv to ensure your local environment has the right version of Python and installed modules.

To install CluedIn Python SDK, run the following command in your shell:

```shell
pip install cluedin
```

### Cloud environments and notebooks

1. To install CluedIn Python SDK in a notebook, use `%pip` instead of `pip` and run the following command in your notebook's cell:

    ```shell
    %pip install cluedin
    ```

    Alternatively, when you use notebooks in tools like Microsoft Fabric, Databricks, etc., there is usually a way to configure the notebook's environment. For example, here's how to install a module in Microsoft Fabric: [https://learn.microsoft.com/en-us/fabric/data-engineering/create-and-use-environment](https://learn.microsoft.com/en-us/fabric/data-engineering/create-and-use-environment).

1. In all cases, after you install the `cluedin` package, you can import it in your Python code:

    ```python
    import cluedin
    ```

## Authentication

To connect to your CluedIn instance via API or CluedIn Python SDK, you need the following:

- URL of your CluedIn instance.

- API (access) token – a JWT token that gives you access to API.

CluedIn Python SDK uses the `Context` object to keep the information it needs to connect to CluedIn API.

### Context settings

You rarely need to set every value. In most cases, you provide `domain`, `org_name`, and either an `access_token` or a `user_email`/`user_password` pair – the SDK derives all the URLs from them.

| Setting | Default | Description |
|---|---|---|
| `domain` | – | Everything in the host name after the organization name. For `https://foobar.contoso.com`, the domain is `contoso.com`. |
| `org_name` | – | Organization name. It is also the OAuth `client_id` used when signing in. |
| `user_email` | – | Email address used to sign in. Required for `get_token`. |
| `user_password` | – | Password used to sign in. Required for `get_token`. |
| `access_token` | – | JWT access token. Set it directly if you already have one, or let `get_token` populate it. |
| `protocol` | `https` | Protocol used to build the URLs below. Keep it as `https`. |
| `org_url` | `{protocol}://{org_name}.{domain}` | Base URL of the organization. Every URL below is derived from it. |
| `auth_url` | `{org_url}/auth` | Authentication endpoint. The token is requested from `{auth_url}/connect/token`. |
| `api_url` | `{org_url}/api/api` | REST API endpoint, used by helpers such as `cluedin.vocab` and `cluedin.entity`. |
| `gql_api_url` | `{api_url}/graphql` | GraphQL endpoint used by `cluedin.gql.gql`, `cluedin.gql.entries`, and `cluedin.gql.search`. |
| `gql_org_url` | `{org_url}/graphql` | Organization-level GraphQL endpoint, used only by `cluedin.gql.org_gql`. |
| `public_api_url` | `{org_url}/public/api` | Public API endpoint used by `cluedin.public`. |
| `verify_tls` | `True` | Whether to validate the server's TLS certificate. |

{: .important }
Note that `gql_api_url` ends in `/api/api/graphql`, not `/graphql`. `{org_url}/graphql` is a different endpoint (`gql_org_url`) that serves only the organization-level schema, and posting a normal `search` query to it returns `400 Bad Request`.

## Import CluedIn Python SDK module

In the code examples below, we assume that you imported CluedIn module in your code:

```python
import cluedin
```

## Creating a Context

### From API token

If you already have the API token, CluedIn Python SDK can build the Context for you:

```python
# assuming your API token is in the CLUEDIN_TOKEN variable
ctx = cluedin.Context.from_jwt(CLUEDIN_TOKEN)
```

Now, you can use the `ctx` Context variable to call CluedIn APIs.

### From an object

You can also create a Context from a Python `dict`:

```python
# assumming you log in to https://foobar.contoso.com
# "foobar" is org_name, and "contoso.com" is the domain
context = {
    "domain": "contoso.com",
    "org_name": "foobar", 
    "access_token": CLUEDIN_TOKEN
}

ctx = cluedin.Context.from_dict(context)
```

### From a file

```python
# cluedin.json
# {
#     "domain": "contoso.com",
#     "org_name": "foobar", 
#     "access_token": CLUEDIN_TOKEN
# }

ctx = cluedin.Context.from_json_file("cluedin.json")
```

### Getting API token from email and password

The API token lets you use some of CluedIn APIs like data ingestion endpoints and search, but to have full access to APIs (assuming you have the necessary permissions), you need to use the token that CluedIn gives you when you log in with your email and password. With the CluedIn Python SDK, you can set your email and password in the Context, and then call the `get_token` method to get the token:

```python
ctx = cluedin.Context.from_dict({
    "domain": "contoso.com",
    "org_name": "foobar", 
    "user_email": "joe@contoso.com",
    "user_password": "yourStrong(!)Password"
})

ctx.get_token() # after this line, `ctx.access_token` will be set
```

## Connecting to CluedIn SaaS

CluedIn SaaS (multi-tenant) instances follow a fixed host naming pattern. The same server answers on two host names, and it matters which one you use:

- `https://<org>.<region>.saas.cluedin.com` – the **UI** host for a single organization. This is the address you open in a browser.
- `https://app.<region>.saas.cluedin.com` – the **API** host, shared by every organization in that region. This is the host in the `iss` (issuer) claim of your token.

`<region>` is the region code of your instance, for example `weu` for West Europe. Both host names are covered by the same wildcard certificate, so TLS verification works against either one.

The URL patterns that matter when you configure the SDK are:

| Endpoint | URL pattern |
|---|---|
| Token | `https://app.<region>.saas.cluedin.com/auth/connect/token` |
| GraphQL | `https://app.<region>.saas.cluedin.com/api/api/graphql` |

### Configuration example

The following configuration works against a SaaS instance as-is. Change only the region, organization name, and credentials:

```json
{
    "domain": "weu.saas.cluedin.com",
    "org_name": "presales",
    "user_email": "joe@cluedin.com",
    "user_password": "yourStrong(!)Password",
    "verify_tls": true
}
```

Save it as `cluedin.json` and load it:

```python
import cluedin

ctx = cluedin.Context.from_json_file("cluedin.json")
ctx.get_token()

# GraphQL
query = 'query { search(query: "*", pageSize: 1) { totalResults } }'
result = cluedin.gql.gql(ctx, query)

# REST
vocab_keys = cluedin.vocab.get_vocab_keys(ctx)
```

Because `domain` is everything after the organization name, `weu.saas.cluedin.com` plus an `org_name` of `presales` gives an `org_url` of `https://presales.weu.saas.cluedin.com`, and the SDK derives the token and GraphQL URLs from there. You do not need to set `api_url` or `gql_api_url` for SaaS.

{: .warning }
Do not set `"api_url": "app"`. A snippet with that value circulates in older notebooks, but `api_url` is a full base URL, not a host prefix, so setting it to `app` makes every REST call fail with `MissingSchema: Invalid URL 'app/entity/schema': No scheme supplied`. Likewise, setting `"gql_api_url": "https://app.<region>.saas.cluedin.com/graphql"` returns `400 Bad Request`, because the API GraphQL endpoint is at `/api/api/graphql`.

### Pinning requests to the API host

If you want every call to go to the shared `app.` host instead of the per-organization host – for example, when only the `app.` host is allowed through a firewall – set `org_url` and leave the rest to the SDK:

```json
{
    "domain": "weu.saas.cluedin.com",
    "org_name": "presales",
    "org_url": "https://app.weu.saas.cluedin.com",
    "user_email": "joe@cluedin.com",
    "user_password": "yourStrong(!)Password"
}
```

Keep `org_name` set to your organization even when you pin `org_url`, because `org_name` is sent as the OAuth `client_id`.

## Booleans in configuration

`verify_tls` is the one setting where it is easy to write something that is silently wrong, because Python and JSON spell booleans differently.

{: .warning }
In a Python `dict`, booleans are `True` and `False` – capitalized. Writing `"verify_tls": false` in Python code raises `NameError: name 'false' is not defined`. In a `.json` file, it is the opposite: booleans are lowercase `true` and `false`, and `True` is invalid JSON.

Correct in Python:

```python
ctx = cluedin.Context.from_dict({
    "domain": "weu.saas.cluedin.com",
    "org_name": "presales",
    "user_email": "joe@cluedin.com",
    "user_password": "yourStrong(!)Password",
    "verify_tls": False  # Python: False, not false
})
```

Correct in `cluedin.json`:

```json
{
    "domain": "weu.saas.cluedin.com",
    "org_name": "presales",
    "user_email": "joe@cluedin.com",
    "user_password": "yourStrong(!)Password",
    "verify_tls": false
}
```

{: .important }
`Context.from_dict` treats any value that is not the string `true` (case-insensitive) as `False`. This means `"verify_tls": 1` and `"verify_tls": "yes"` both **disable** certificate validation instead of enabling it. Use only the boolean literals `True`/`False` in Python and `true`/`false` in JSON.

When should you set `verify_tls` to `False`? Only when the certificate cannot be validated – a self-signed certificate on a development or on-premises instance, or a corporate proxy that intercepts TLS. CluedIn SaaS presents a valid certificate, so leave `verify_tls` at its default of `True` there. Turning verification off also makes `urllib3` print an `InsecureRequestWarning` on every call.

## Troubleshooting authentication

Most connection problems surface as an exception from `ctx.get_token()`. The message tells you which part of the configuration is wrong.

### invalid_username_or_password

```
requests.exceptions.HTTPError: 400 Client Error: Bad Request
{"error":"invalid_grant","error_description":"invalid_username_or_password"}
```

The `user_email` or `user_password` is wrong. CluedIn returns the same error for both, so it does not reveal which one failed.

To diagnose:

1. Open `https://<org>.<region>.saas.cluedin.com` in a browser and sign in with the same credentials. If sign-in fails there, the credentials are the problem.
1. Check that the password reached Python unchanged. Passwords containing `!`, `$`, or backslashes are frequently mangled by shell interpolation or by an `.env` file. Print `len(ctx.user_password)` and compare it with the expected length.
1. If your account signs in through an external identity provider (such as Microsoft Entra ID), the username and password grant does not apply. Get a token from the browser session instead and use `cluedin.Context.from_jwt`.

### Client not found for client id

```
requests.exceptions.HTTPError: 500 Server Error: Internal Server Error
Client not found for client id <value>
```

The `org_name` does not match an organization on that instance. It must be the organization name exactly as it appears in the host name – for `https://presales.weu.saas.cluedin.com`, `org_name` is `presales`.

### ConnectionError or NameResolutionError

```
requests.exceptions.ConnectionError: HTTPSConnectionPool(host='presales.weu.saas.cluedin.invalid', port=443):
Max retries exceeded with url: /auth/connect/token (Caused by NameResolutionError(...))
```

The host name built from `domain` and `org_name` does not exist. The host name in the error message is the fastest way to see what the SDK actually assembled.

To diagnose:

1. Print the Context – `print(ctx)` shows every derived URL, with the password and token masked:

    ```
    Context:
        Domain: weu.saas.cluedin.com
        Organization Name: presales
        Organization URL: https://presales.weu.saas.cluedin.com
        Authentication URL: https://presales.weu.saas.cluedin.com/auth
        API URL: https://presales.weu.saas.cluedin.com/api/api
        GQL API URL: https://presales.weu.saas.cluedin.com/api/api/graphql
        Verify TLS: True
    ```

1. Compare the Organization URL with the URL you use in the browser. They must match.
1. Check that you did not put the whole URL into `domain`. `domain` is only the part **after** the organization name, without a protocol – `weu.saas.cluedin.com`, not `https://presales.weu.saas.cluedin.com`.

### ConnectTimeout

A timeout on port 80 means `protocol` was set to `http`. Remove the setting, or set it to `https`.

A timeout on port 443 usually means the instance is not reachable from where your code runs – check VPN, firewall rules, and outbound proxy configuration for notebook environments such as Fabric or Databricks.

### SSLCertVerificationError

```
requests.exceptions.SSLError: ... certificate verify failed: unable to get local issuer certificate
```

The certificate chain cannot be validated. On a development or on-premises instance with a self-signed certificate, set `verify_tls` to `False` (`false` in JSON). On SaaS, this error normally points to a TLS-intercepting corporate proxy – install its root certificate rather than disabling verification.

### 400 Bad Request from a GraphQL call

Authentication succeeded but the query fails. Check `ctx.gql_api_url`: it must end in `/api/api/graphql`. If it ends in just `/graphql`, you have either set `gql_api_url` explicitly or set `api_url` to something that is not a full base URL. Remove both settings and let the SDK derive them.

### 401 Unauthorized from any call

The token is missing or expired. `Context` does not refresh tokens automatically, so call `ctx.get_token()` again in long-running jobs.
