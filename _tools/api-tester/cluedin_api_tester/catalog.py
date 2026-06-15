"""Endpoint catalog model and loader.

The catalog is a YAML file (``endpoints.yaml``) describing which REST endpoints
to exercise. GraphQL endpoints are flagged ``priority: graphql`` so they run and
report first — GraphQL is CluedIn's primary query mechanism.
"""

from __future__ import annotations

import dataclasses
import re
from pathlib import Path
from typing import Any, Optional

import yaml

_PLACEHOLDER = re.compile(r"\{(\w+)\}")

# Lower number == higher priority (runs/reports first).
_PRIORITY_ORDER = {"graphql": 0, "high": 1, "normal": 2, "low": 3}

_FIELDS = {
    "name",
    "category",
    "method",
    "path",
    "base",
    "priority",
    "uses_graphql",
    "destructive",
    "params",
    "body",
    "graphql_query",
    "pass_status",
    "note",
}


@dataclasses.dataclass
class Endpoint:
    name: str
    category: str
    method: str = "GET"
    path: str = ""
    base: str = "server"  # which base URL to use: "server" (Server.WebApi) or "public" (PublicApi.WebApi)
    priority: str = "normal"
    uses_graphql: bool = False
    destructive: bool = False
    params: dict = dataclasses.field(default_factory=dict)
    body: Any = None
    graphql_query: Optional[str] = None
    pass_status: list = dataclasses.field(default_factory=lambda: [200, 204])
    note: str = ""

    @property
    def required_placeholders(self) -> set:
        """Names of ``{placeholder}`` tokens that must be supplied via context."""
        found: set = set()
        blobs = [self.path, repr(self.params), repr(self.body or ""), self.graphql_query or ""]
        for blob in blobs:
            found.update(_PLACEHOLDER.findall(blob))
        return found

    def sort_key(self):
        return (_PRIORITY_ORDER.get(self.priority, 2), self.category, self.name)


def load_catalog(path: str | Path) -> list[Endpoint]:
    data = yaml.safe_load(Path(path).read_text(encoding="utf-8")) or {}
    endpoints = []
    for raw in data.get("endpoints", []):
        clean = {k: v for k, v in raw.items() if k in _FIELDS}
        endpoints.append(Endpoint(**clean))
    return endpoints


def substitute(obj: Any, context: dict) -> Any:
    """Recursively replace ``{key}`` placeholders using ``context``."""
    if isinstance(obj, str):
        return _PLACEHOLDER.sub(lambda m: str(context.get(m.group(1), m.group(0))), obj)
    if isinstance(obj, dict):
        return {k: substitute(v, context) for k, v in obj.items()}
    if isinstance(obj, list):
        return [substitute(v, context) for v in obj]
    return obj
