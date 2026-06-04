"""Core test runner: executes endpoints with a bearer token and grades results."""

from __future__ import annotations

import dataclasses
import json
import time
from typing import Optional

import requests

from .catalog import Endpoint, substitute

# Result statuses.
PASS = "PASS"          # expected status / GraphQL data returned
FAIL = "FAIL"          # unexpected status or GraphQL errors
FORBIDDEN = "FORBIDDEN"  # 403 — endpoint & token are fine, role/RACI denies
AUTH = "AUTH"          # 401 — token rejected/expired
SKIP = "SKIP"          # missing context placeholder or destructive & not opted-in
ERROR = "ERROR"        # connection/transport error


@dataclasses.dataclass
class TestResult:
    endpoint: Endpoint
    status: str
    http_status: Optional[int] = None
    elapsed_ms: Optional[float] = None
    detail: str = ""
    url: str = ""


class ApiTester:
    def __init__(
        self,
        api_url: str,
        token: str,
        *,
        public_api_url: Optional[str] = None,
        session: Optional[requests.Session] = None,
        verify: bool = True,
        timeout: float = 30,
        context: Optional[dict] = None,
    ):
        self.api_url = api_url.rstrip("/")
        # Per-endpoint base resolution. Hosted instances serve Server.WebApi under
        # /api and PublicApi.WebApi under /public, so they can differ.
        self.bases = {
            "server": self.api_url,
            "public": (public_api_url or api_url).rstrip("/"),
        }
        self.token = token
        self.session = session or requests.Session()
        self.verify = verify
        self.timeout = timeout
        self.context = dict(context or {})

    def _headers(self, json_body: bool) -> dict:
        headers = {"Authorization": f"Bearer {self.token}", "Accept": "application/json"}
        if json_body:
            headers["Content-Type"] = "application/json"
        return headers

    def run_one(self, ep: Endpoint) -> TestResult:
        missing = ep.required_placeholders - set(self.context)
        if missing:
            return TestResult(
                ep, SKIP, detail=f"needs context: {', '.join(sorted(missing))} "
                f"(pass via --context {next(iter(sorted(missing)))}=<value>)"
            )

        path = substitute(ep.path, self.context).lstrip("/")
        base = self.bases.get(ep.base, self.bases["server"])
        url = f"{base}/{path}"
        params = substitute(ep.params, self.context) if ep.params else None

        start = time.perf_counter()
        try:
            if ep.graphql_query:
                query = substitute(ep.graphql_query, self.context)
                resp = self.session.post(
                    url, headers=self._headers(True), json={"query": query},
                    params=params, verify=self.verify, timeout=self.timeout,
                )
            elif ep.method.upper() in ("POST", "PUT", "PATCH"):
                body = substitute(ep.body, self.context)
                resp = self.session.request(
                    ep.method.upper(), url, headers=self._headers(True),
                    params=params, json=body, verify=self.verify, timeout=self.timeout,
                )
            else:
                resp = self.session.request(
                    ep.method.upper(), url, headers=self._headers(False),
                    params=params, verify=self.verify, timeout=self.timeout,
                )
        except requests.RequestException as exc:
            elapsed = (time.perf_counter() - start) * 1000
            return TestResult(ep, ERROR, None, elapsed, f"{type(exc).__name__}: {exc}", url)

        elapsed = (time.perf_counter() - start) * 1000
        code = resp.status_code

        if code == 401:
            return TestResult(ep, AUTH, code, elapsed, "401 Unauthorized (token rejected/expired)", url)
        if code == 403:
            return TestResult(ep, FORBIDDEN, code, elapsed, "403 Forbidden (role/RACI lacks access)", url)

        if ep.graphql_query:
            return self._grade_graphql(ep, resp, code, elapsed, url)

        if code in ep.pass_status:
            return TestResult(ep, PASS, code, elapsed, "", url)
        return TestResult(ep, FAIL, code, elapsed, f"HTTP {code}: {resp.text[:200]}", url)

    @staticmethod
    def _grade_graphql(ep, resp, code, elapsed, url) -> TestResult:
        if not resp.ok:
            return TestResult(ep, FAIL, code, elapsed, f"HTTP {code}: {resp.text[:200]}", url)
        try:
            body = resp.json()
        except ValueError:
            return TestResult(ep, FAIL, code, elapsed, "non-JSON GraphQL response", url)
        errors = body.get("errors")
        if errors:
            return TestResult(ep, FAIL, code, elapsed, f"GraphQL errors: {json.dumps(errors)[:300]}", url)
        if "data" in body:
            return TestResult(ep, PASS, code, elapsed, "GraphQL data returned", url)
        return TestResult(ep, FAIL, code, elapsed, "GraphQL response had no 'data'", url)

    def run(self, endpoints: list[Endpoint], *, include_destructive: bool = False) -> list[TestResult]:
        results = []
        for ep in sorted(endpoints, key=lambda e: e.sort_key()):
            if ep.destructive and not include_destructive:
                results.append(TestResult(ep, SKIP, detail="destructive (enable with --include-mutations)"))
                continue
            results.append(self.run_one(ep))
        return results
