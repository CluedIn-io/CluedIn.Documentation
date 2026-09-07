---
layout: cluedin
title: GraphQL actions
parent: GraphQL
grand_parent: Publish & consume
nav_order: 20
permalink: /publish/graphql/graphql-actions
content_type: how-to
redirect_from: ["/consume/graphql/graphql-actions"]
source_path: docs/150-consume/graphql/050-graphql-actions.md
tags: ["consume","graphql"]
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

CluedIn supports GraphQL actions, which allow you to perform bulk operations directly from the GraphQL endpoint. These actions are restricted to [Admin users](/administer/users-and-roles/roles) for security reasons, as they can modify or process large volumes of data at once.

## Split entities in bulk

The following query splits multiple records that match a given search filter.

```
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

## Delete entities in bulk
You can delete multiple records at once by specifying a search query.

```
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

## Run post-processing
Trigger post-processing jobs in bulk for matching records.

```
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

## Run entity metrics processing
Process data quality metrics for a batch of records.

```
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

## Run edge processing
Rebuild or recalculate relationships ([edges](/model/relationships/edges)) between records.

```
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

## Run enrichment
Re-run enrichment for a specific set of records to pull in updated or missing data:

```
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

## Search with filters
You can refine search results using filters with [Lucene syntax](https://lucene.apache.org/core/2_9_4/queryparsersyntax.html).

The following example retrieves all Customer records where the `addressCountry` property equals CHN or JPN, and where `addressZipCode` is missing.

```
{
  search(
    query:"entityType:/Customer",
    filter: "(properties.customer.addressCountry:CHN OR JPN) AND -properties.customer.addressZipCode:*"    
  )
   {
    totalResults
    entries {
      id
      name
      properties
    }
  }
}
```

In the filter expression:

- `-properties.customer.addressZipCode:*` means the properties where the value does not exist.

- `+properties.customer.addressZipCode:*` means the properties where the value exists.

Filters use Lucene syntax, and you can test your filter expressions directly in the CluedIn search bar.

![gql-search-with-filter.png]({{ "/assets/images/consume/gql-search-with-filter.png" | relative_url }})