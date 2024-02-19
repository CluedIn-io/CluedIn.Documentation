---
layout: cluedin
nav_order: 2
parent: GraphQL
grand_parent: Consume
permalink: /consume/graphql/graphql-actions
title: GraphQL actions
tags: ["consume","graphql"]
---

CluedIn supports GraphQL actions so that you can run commands in bulk from our GraphQL endpoint. You will need to be in the Admin role to even see these commands as they allow you to run operations in bulk.  


Split Entities in Bulk.

```json


{
  search(query: "user.firstName:Tim", pageSize: 4) {
    entries {
      name
      actions {
          splitEntity
      }
    }
  }
}
```

Delete Entities in Bulk.

```json


{
  search(query: "user.firstName:Tim", pageSize: 4) {
    entries {
      name
      actions {
          deleteEntity
      }
    }
  }
}
```

Run Post Processing

```json
{
  search(query: "user.firstName:Tim", pageSize: 4) {
    entries {
      name
      actions {
          postProcess
      }
    }
  }
}
```

Run Entity Metrics Processing

```json
{
  search(query: "user.firstName:Tim", pageSize: 4) {
    entries {
      name
      actions {
          processEntityMetrics
      }
    }
  }
}
```

Run Edge Processing

```json
{
  search(query: "user.firstName:Tim", pageSize: 4) {
    entries {
      name
      actions {
          processEdges
      }
    }
  }
}
```


Run Enrichment

```json
{
  search(query: "user.firstName:Tim", pageSize: 4) {
    entries {
      name
      actions {
          enrich
      }
    }
  }
}
```
