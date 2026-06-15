"""Reporting: console summary, JSON, and Markdown."""

from __future__ import annotations

import dataclasses
import json
from collections import Counter
from pathlib import Path

from .tester import AUTH, ERROR, FAIL, FORBIDDEN, PASS, SKIP, TestResult

_ORDER = [PASS, FORBIDDEN, FAIL, AUTH, ERROR, SKIP]


def summarize(results: list[TestResult]) -> Counter:
    return Counter(r.status for r in results)


def print_console(results: list[TestResult]) -> None:
    print()
    print(f"{'STATUS':<10} {'PRIO':<7} {'METHOD':<6} {'PATH':<46} {'HTTP':<5} {'ms':>7}  DETAIL")
    print("-" * 110)
    for r in results:
        ms = f"{r.elapsed_ms:7.0f}" if r.elapsed_ms is not None else "      -"
        http = str(r.http_status) if r.http_status is not None else "-"
        path = (r.endpoint.path or "")[:46]
        detail = r.detail[:48]
        gql = "*" if r.endpoint.uses_graphql else " "
        print(
            f"{r.status:<10} {r.endpoint.priority:<6}{gql} {r.endpoint.method:<6} "
            f"{path:<46} {http:<5} {ms}  {detail}"
        )

    counts = summarize(results)
    print("-" * 110)
    summary = "  ".join(f"{status}={counts.get(status, 0)}" for status in _ORDER)
    print(f"TOTAL={len(results)}   {summary}")
    print("(* = GraphQL-backed endpoint, reported first)")
    print()


def _result_to_dict(r: TestResult) -> dict:
    ep = r.endpoint
    return {
        "name": ep.name,
        "category": ep.category,
        "priority": ep.priority,
        "uses_graphql": ep.uses_graphql,
        "method": ep.method,
        "path": ep.path,
        "status": r.status,
        "http_status": r.http_status,
        "elapsed_ms": round(r.elapsed_ms, 1) if r.elapsed_ms is not None else None,
        "url": r.url,
        "detail": r.detail,
    }


def write_json(results: list[TestResult], path: str | Path, meta: dict) -> None:
    payload = {"meta": meta, "summary": dict(summarize(results)), "results": [_result_to_dict(r) for r in results]}
    Path(path).write_text(json.dumps(payload, indent=2), encoding="utf-8")


def write_markdown(results: list[TestResult], path: str | Path, meta: dict) -> None:
    counts = summarize(results)
    lines = ["# CluedIn REST API test run", ""]
    lines.append(f"- Base API URL: `{meta.get('api_url')}`")
    lines.append(f"- Token endpoint: `{meta.get('token_endpoint')}`")
    lines.append(f"- Client / user: `{meta.get('client_id')}` / `{meta.get('username')}`")
    lines.append(f"- Catalog: `{meta.get('catalog')}`")
    lines.append("")
    lines.append("**Summary:** " + "  ".join(f"`{s}={counts.get(s, 0)}`" for s in _ORDER) + f"  (total {len(results)})")
    lines.append("")
    lines.append("| Status | Prio | GQL | Method | Path | HTTP | ms | Detail |")
    lines.append("|---|---|---|---|---|---|---|---|")
    for r in results:
        ms = f"{r.elapsed_ms:.0f}" if r.elapsed_ms is not None else "-"
        http = r.http_status if r.http_status is not None else "-"
        gql = "yes" if r.endpoint.uses_graphql else ""
        detail = r.detail.replace("|", "\\|")[:80]
        lines.append(
            f"| {r.status} | {r.endpoint.priority} | {gql} | {r.endpoint.method} | "
            f"`{r.endpoint.path}` | {http} | {ms} | {detail} |"
        )
    Path(path).write_text("\n".join(lines) + "\n", encoding="utf-8")
