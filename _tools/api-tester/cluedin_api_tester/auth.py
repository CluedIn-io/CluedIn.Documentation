"""Token acquisition for CluedIn (IdentityServer resource-owner-password grant).

The recipe is derived from the CluedIn codebase:

* ``CluedInResourceOwnerPasswordValidator`` — ``client_id`` is the organization's
  ``ApplicationSubDomain`` (the org subdomain), and the org must be Active.
* ``ClientDataStore`` — organization clients are *public*
  (``RequireClientSecret = false``) and allow the ``password`` grant.
* ``test/integration/.../WebApiTestBase.cs`` — posts
  ``grant_type=password&username=..&password=..&client_id=..`` (form-urlencoded)
  to the auth server's token endpoint, then sends ``Authorization: Bearer <token>``.

Hosted topology (IMPORTANT): when ``Proxy.Enabled=true`` (the default for hosted
deployments), IdentityServer is reverse-proxied under a path prefix
(``Proxy.AuthPrefix``, default ``auth``) — see ``AuthenticationServer/Startup.cs``
(``ctx.Request.PathBase = "/auth"``). So the public token endpoint is
``https://<host>/auth/connect/token``, NOT ``https://<host>/connect/token``.
POSTing to the un-prefixed path hits the proxy/SPA and returns a **405 HTML page**.

Token-endpoint resolution order (each tried until one yields an ``access_token``):
  1. an explicit ``--token-endpoint`` if supplied;
  2. OpenID discovery at ``<auth-url>[/auth]/.well-known/openid-configuration``;
  3. fallbacks: ``.../connect/token``, ``.../auth/connect/token``,
     ``.../token``, ``.../auth/token``.
"""

from __future__ import annotations

import dataclasses
from typing import Callable, Optional

import requests


class AuthError(RuntimeError):
    """Raised when no token could be obtained from any candidate endpoint."""


@dataclasses.dataclass
class TokenResult:
    access_token: str
    token_endpoint: str
    expires_in: Optional[int] = None
    token_type: str = "Bearer"
    scope: Optional[str] = None
    raw: dict = dataclasses.field(default_factory=dict)


def _dedupe(seq):
    seen = set()
    out = []
    for item in seq:
        if item and item not in seen:
            seen.add(item)
            out.append(item)
    return out


def _looks_like_html(resp: requests.Response) -> bool:
    ctype = resp.headers.get("Content-Type", "").lower()
    if "html" in ctype:
        return True
    head = resp.text[:200].lstrip().lower()
    return head.startswith("<!doctype html") or head.startswith("<html")


def _discovery_urls(auth_url: str) -> list[str]:
    base = auth_url.rstrip("/")
    return _dedupe([
        f"{base}/.well-known/openid-configuration",
        f"{base}/auth/.well-known/openid-configuration",
    ])


def _token_candidates(auth_url: str) -> list[str]:
    base = auth_url.rstrip("/")
    return _dedupe([
        f"{base}/connect/token",
        f"{base}/auth/connect/token",
        f"{base}/token",
        f"{base}/auth/token",
    ])


def discover_token_endpoint(
    session: requests.Session,
    auth_url: str,
    *,
    verify: bool = True,
    timeout: float = 15,
    log: Optional[Callable[[str], None]] = None,
) -> Optional[str]:
    """Best-effort OpenID-Connect discovery of the token endpoint.

    Tries both the root and the ``/auth``-prefixed metadata URLs (hosted proxy).
    """
    for url in _discovery_urls(auth_url):
        try:
            resp = session.get(url, verify=verify, timeout=timeout)
        except requests.RequestException as exc:
            if log:
                log(f"discovery {url} -> connection error: {exc}")
            continue
        if resp.ok and not _looks_like_html(resp):
            try:
                endpoint = resp.json().get("token_endpoint")
            except ValueError:
                endpoint = None
            if endpoint:
                if log:
                    log(f"discovery {url} -> token_endpoint={endpoint}")
                return endpoint
        if log:
            log(f"discovery {url} -> HTTP {resp.status_code} (no usable metadata)")
    return None


def get_access_token(
    auth_url: str,
    client_id: str,
    username: str,
    password: str,
    *,
    scope: Optional[str] = None,
    client_secret: Optional[str] = None,
    token_endpoint: Optional[str] = None,
    session: Optional[requests.Session] = None,
    verify: bool = True,
    timeout: float = 30,
    log: Optional[Callable[[str], None]] = None,
) -> TokenResult:
    """Acquire a bearer token using the resource-owner-password grant.

    Returns a :class:`TokenResult`. Raises :class:`AuthError` if every candidate
    endpoint fails (with collected, actionable error details).
    """
    session = session or requests.Session()

    if token_endpoint:
        candidates = [token_endpoint]
    else:
        discovered = discover_token_endpoint(
            session, auth_url, verify=verify, timeout=timeout, log=log
        )
        candidates = _dedupe([discovered, *_token_candidates(auth_url)])

    form = {
        "grant_type": "password",
        "client_id": client_id,
        "username": username,
        "password": password,
    }
    if client_secret:
        form["client_secret"] = client_secret
    if scope:
        form["scope"] = scope

    errors = []
    saw_405_or_html = False
    for endpoint in candidates:
        try:
            resp = session.post(
                endpoint,
                data=form,  # requests sets application/x-www-form-urlencoded
                headers={"Accept": "application/json"},
                verify=verify,
                timeout=timeout,
            )
        except requests.RequestException as exc:
            errors.append(f"{endpoint} -> connection error: {exc}")
            if log:
                log(errors[-1])
            continue

        if resp.ok:
            try:
                data = resp.json()
            except ValueError:
                errors.append(f"{endpoint} -> HTTP 200 but non-JSON (likely an HTML/SPA page)")
                saw_405_or_html = True
                if log:
                    log(errors[-1])
                continue
            token = data.get("access_token")
            if token:
                if log:
                    log(f"{endpoint} -> token acquired")
                return TokenResult(
                    access_token=token,
                    token_endpoint=endpoint,
                    expires_in=data.get("expires_in"),
                    token_type=data.get("token_type", "Bearer"),
                    scope=data.get("scope"),
                    raw=data,
                )
            # 400 with error/error_description = real OAuth error (bad creds/client).
            err = data.get("error_description") or data.get("error") or list(data)
            errors.append(f"{endpoint} -> 200 but no access_token ({err})")
            if log:
                log(errors[-1])
            continue

        # Non-2xx
        is_html = _looks_like_html(resp)
        if resp.status_code == 405 or is_html:
            saw_405_or_html = True
            kind = "405 Method Not Allowed" if resp.status_code == 405 else f"HTTP {resp.status_code}"
            tail = " (HTML page — proxy/SPA, not the token endpoint)" if is_html else ""
            errors.append(f"{endpoint} -> {kind}{tail}")
        else:
            # 400/401 here is usually a genuine OAuth error worth surfacing verbatim.
            try:
                payload = resp.json()
                detail = payload.get("error_description") or payload.get("error") or resp.text[:200]
            except ValueError:
                detail = resp.text[:200]
            errors.append(f"{endpoint} -> HTTP {resp.status_code}: {detail}")
        if log:
            log(errors[-1])

    hint = ""
    if saw_405_or_html:
        hint = (
            "\n\nHint: a 405 / HTML response means the POST hit a reverse proxy or SPA, "
            "not IdentityServer. Hosted CluedIn serves auth under an '/auth' prefix — "
            "pass  --auth-url https://<host>/auth  (or set --token-endpoint explicitly)."
        )
    raise AuthError(
        "Failed to acquire an access token. Attempts:\n  - " + "\n  - ".join(errors) + hint
    )
