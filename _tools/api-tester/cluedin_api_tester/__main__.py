"""CLI entry point.

Example:
    python -m cluedin_api_tester \
        --url https://app.example.cluedin.com \
        --client-id mycompany \
        --username admin@mycompany.com \
        --password '***' \
        --only graphql,high \
        --markdown run.md
"""

from __future__ import annotations

import argparse
import getpass
import os
import sys
from pathlib import Path
from urllib.parse import urlparse

import requests

from . import report
from .auth import AuthError, get_access_token
from .catalog import load_catalog
from .tester import ApiTester

_DEFAULT_CATALOG = Path(__file__).resolve().parent.parent / "endpoints.yaml"


def _parse_context(pairs: list[str]) -> dict:
    ctx = {}
    for pair in pairs or []:
        if "=" not in pair:
            raise SystemExit(f"--context expects key=value, got: {pair!r}")
        key, value = pair.split("=", 1)
        ctx[key.strip()] = value
    return ctx


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="cluedin_api_tester",
        description="Acquire a CluedIn bearer token and smoke-test REST endpoints "
        "(GraphQL-backed endpoints first).",
    )
    p.add_argument("--url", required=True,
                   help="Base URL of the CluedIn instance (used for both auth and API "
                        "unless --auth-url/--api-url are given).")
    p.add_argument("--auth-url", help="Override base URL for the auth server. Hosted instances "
                                      "serve auth under '/auth' (e.g. https://<host>/auth); the tool "
                                      "also auto-probes that path during discovery.")
    p.add_argument("--api-url", help="Base URL for the Server.WebApi REST API "
                                     "(Search/Rules/Glossary etc.). Hosted: https://<host> "
                                     "(routes already include the /api prefix).")
    p.add_argument("--public-api-url", help="Base URL for PublicApi.WebApi (public GraphQL, Clue, "
                                            "enrichment). Hosted: https://<host>/public. "
                                            "Defaults to --api-url if omitted.")
    p.add_argument("--token-endpoint", help="Explicit token endpoint URL (skips discovery).")

    p.add_argument("--client-id", required=True, help="OAuth client_id (the organization subdomain).")
    p.add_argument("--username", required=True)
    p.add_argument("--password", help="If omitted, read from $CLUEDIN_PASSWORD or prompt securely.")
    p.add_argument("--client-secret", help="Only if the client is confidential (usually not needed).")
    p.add_argument("--scope", help="Optional OAuth scope, e.g. 'openid profile ServerApiForUI'.")

    p.add_argument("--catalog", default=str(_DEFAULT_CATALOG),
                   help=f"Endpoint catalog YAML (default: {_DEFAULT_CATALOG.name}).")
    p.add_argument("--only", help="Comma-separated priorities and/or categories to include "
                                  "(e.g. 'graphql,high' or 'Search,Glossary').")
    p.add_argument("--context", action="append", metavar="KEY=VALUE",
                   help="Provide values for {placeholder} params, e.g. --context entity_id=<guid>. Repeatable.")
    p.add_argument("--include-mutations", action="store_true",
                   help="Also run endpoints flagged destructive (POST/PUT/DELETE writes). Off by default.")

    p.add_argument("--insecure", action="store_true", help="Disable TLS verification (self-signed dev certs).")
    p.add_argument("--timeout", type=float, default=30)
    p.add_argument("-v", "--verbose", action="store_true",
                   help="Print each token-endpoint discovery/attempt (useful for 405/auth debugging).")
    p.add_argument("--json", dest="json_out", help="Write a JSON report to this path.")
    p.add_argument("--markdown", dest="md_out", help="Write a Markdown report to this path.")
    p.add_argument("--list", action="store_true", help="List the endpoints that would run, then exit.")
    return p


def _auth_prefix_from_token_endpoint(token_endpoint: str) -> str:
    """Return the proxy path prefix in front of /connect/token (e.g. 'auth'), or ''.

    A non-empty prefix means the deployment is reverse-proxied with path prefixes,
    so the Server.WebApi / PublicApi.WebApi bases also need their prefixes (/api, /public).
    """
    path = urlparse(token_endpoint).path  # e.g. /auth/connect/token
    for suffix in ("/connect/token", "/token"):
        if path.endswith(suffix):
            return path[: -len(suffix)].strip("/")
    return ""


def _filter_catalog(endpoints, only: str | None):
    if not only:
        return endpoints
    wanted = {w.strip().lower() for w in only.split(",") if w.strip()}
    return [e for e in endpoints if e.priority.lower() in wanted or e.category.lower() in wanted]


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)

    auth_url = args.auth_url or args.url
    verify = not args.insecure
    if args.insecure:
        requests.packages.urllib3.disable_warnings()  # type: ignore[attr-defined]

    catalog = load_catalog(args.catalog)
    catalog = _filter_catalog(catalog, args.only)
    if not catalog:
        print("No endpoints matched the --only filter.", file=sys.stderr)
        return 2

    if args.list:
        for ep in sorted(catalog, key=lambda e: e.sort_key()):
            flag = " [graphql]" if ep.uses_graphql else ""
            dest = " [destructive]" if ep.destructive else ""
            print(f"{ep.priority:<7} {ep.method:<6} {ep.path}{flag}{dest}")
        return 0

    password = args.password or os.environ.get("CLUEDIN_PASSWORD") or getpass.getpass("CluedIn password: ")

    session = requests.Session()
    log = (lambda msg: print(f"  [auth] {msg}", file=sys.stderr)) if args.verbose else None
    try:
        token = get_access_token(
            auth_url, args.client_id, args.username, password,
            scope=args.scope, client_secret=args.client_secret,
            token_endpoint=args.token_endpoint, session=session,
            verify=verify, timeout=args.timeout, log=log,
        )
    except AuthError as exc:
        print(f"\nAUTH FAILED:\n{exc}\n", file=sys.stderr)
        return 1

    print(f"Token acquired from {token.token_endpoint} "
          f"(expires_in={token.expires_in}, scope={token.scope or 'n/a'})")

    # Resolve API bases. If the deployment is reverse-proxied (the token endpoint
    # sits under a path prefix such as /auth), the Server.WebApi and PublicApi.WebApi
    # backends are also prefixed (/api and /public) and the gateway strips that
    # segment before routing — while the controllers' own routes still start with
    # 'api/'. So the bases must include those prefixes. Derive them unless overridden.
    host = args.url.rstrip("/")
    proxy_prefix = _auth_prefix_from_token_endpoint(token.token_endpoint)
    hosted = bool(proxy_prefix)

    if args.api_url:
        api_url = args.api_url
    elif hosted:
        api_url = f"{host}/api"
    else:
        api_url = args.url

    if args.public_api_url:
        public_api_url = args.public_api_url
    elif hosted:
        public_api_url = f"{host}/public"
    else:
        public_api_url = None  # ApiTester falls back to api_url

    if hosted and not (args.api_url and args.public_api_url):
        print(f"Detected reverse-proxied deployment (auth under '/{proxy_prefix}'). "
              f"Using api_url={api_url}  public_api_url={public_api_url or api_url}  "
              f"(override with --api-url / --public-api-url).")

    tester = ApiTester(
        api_url, token.access_token, public_api_url=public_api_url,
        session=session, verify=verify,
        timeout=args.timeout, context=_parse_context(args.context),
    )
    results = tester.run(catalog, include_destructive=args.include_mutations)

    report.print_console(results)

    meta = {
        "api_url": api_url,
        "public_api_url": public_api_url or api_url,
        "auth_url": auth_url,
        "token_endpoint": token.token_endpoint,
        "client_id": args.client_id,
        "username": args.username,
        "catalog": str(args.catalog),
    }
    if args.json_out:
        report.write_json(results, args.json_out, meta)
        print(f"JSON report written to {args.json_out}")
    if args.md_out:
        report.write_markdown(results, args.md_out, meta)
        print(f"Markdown report written to {args.md_out}")

    counts = report.summarize(results)
    # Non-zero exit if anything outright failed or auth was rejected.
    return 1 if (counts.get("FAIL", 0) or counts.get("AUTH", 0) or counts.get("ERROR", 0)) else 0


if __name__ == "__main__":
    raise SystemExit(main())
