---
layout: cluedin
nav_order: 2
parent: GraphQL
grand_parent: Consume
permalink: {{ site.baseurl }}/consume/graphql/graphql-actions
title: GraphQL actions
tags: ["consume","graphql"]
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

CluedIn supports GraphQL actions so that you can run commands in bulk from our GraphQL endpoint. You will need to be in the Admin role to even see these commands as they allow you to run operations in bulk.  

## Split entities in bulk

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

## Delete entities in bulk

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

## Run post-processing

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

## Run entity metrics processing

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

## Run edge processing

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

## Run enrichment

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

## Search with filter

```json
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

In `-properties.customer.addressZipCode:*`, the `-properties` means where value does not exist; and if it is `+properties`, it would mean where value exists. Note that the filter uses [Lucene](https://lucene.apache.org/core/2_9_4/queryparsersyntax.html) syntax. Also, you can test the filter query directly in the search bar.

![gql-search-with-filter.png](../../assets/images/consume/gql-search-with-filter.png)