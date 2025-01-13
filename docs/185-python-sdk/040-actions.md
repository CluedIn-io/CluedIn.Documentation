---
layout: cluedin
title: GraphQL Actions
parent: Python SDK
permalink: /python-sdk/actions
nav_order: 040
has_children: false
tags: ["python"]
last_modified: 2025-01-13
summary: "How to use GraphQL Actions in the Python SDK"
---

You can add GraphQL [Actions](/consume/graphql/graphql-actions) when running GraphQL queries in the Python SDK. Actions are a way to run commands in bulk, such as processing, enriching, or deleting entities.

Here is an example of how to use Actions in the Python SDK to delete entities (please note that this is a destructive operation and should be used with caution):

```python
#!/usr/bin/env python3

import argparse
import time
from datetime import timedelta

import cluedin


def main(context_file: str, query_string: str) -> None:
    """
    Executes a GraphQL query against CluedIn using the supplied query string.

    :param context_file: The CluedIn Context file.
    :param query_string: The query parameter to filter entities.
    """

    ctx = cluedin.Context.from_json_file(context_file)
    ctx.get_token()

    gql_query = """
    query searchEntities($cursor: PagingCursor, $query: String, $pageSize: Int) {
        search(query: $query, sort: FIELDS, cursor: $cursor, pageSize: $pageSize
            sortFields: {field: "id", direction: ASCENDING}
        ) {
            totalResults cursor
            entries { id name entityType
                actions { deleteEntity } } } }"""

    variables = { "query": query_string, "pageSize": 10_000 }

    start_time = time.time()
    iteration_start = start_time

    for i, entity in enumerate(
        cluedin.gql.entries(context=ctx, query=gql_query, variables=variables)
    ):
        print(i + 1, entity["id"], entity["name"], entity["entityType"])

        if i % 10_000 == 0 and i > 0:
            time_from_start = timedelta(seconds=time.time() - start_time)
            time_from_iteration_start = timedelta(
                seconds=time.time() - iteration_start)
            iteration_start = time.time()

            print(
                f"{time_from_start} {time_from_iteration_start}: "
                f"{i} entities queued for deletion"
            )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Query and list entities from CluedIn."
    )
    parser.add_argument(
        "context",
        type=str,
        help="The JSON file representing CluedIn context " +
        "(https://documentation.cluedin.net/python-sdk/credentials#create-a-context-from-a-file)."
    )
    parser.add_argument(
        "query",
        type=str,
        help="The query parameter used to filter entities (e.g. +entityType:/Contact)."
    )
    args = parser.parse_args()
    main(args.context, args.query)
```

This script queries CluedIn for entities that match the query string and then deletes them. The script uses the `searchEntities` query to find entities and then uses the `deleteEntity` action to delete them.

Run the script with the following command:

```powershell
python .\delete_entities.py ".cluedin/demo.json" "+entityType:/Duck"
```
