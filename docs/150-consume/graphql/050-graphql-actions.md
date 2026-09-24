---
layout: cluedin
nav_order: 2
parent: GraphQL
grand_parent: Consume
permalink: /consume/graphql/graphql-actions
title: GraphQL actions
tags: ["consume","graphql"]
last_modified: 2026-09-24
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

CluedIn supports GraphQL actions, which allow you to perform bulk operations directly from the GraphQL endpoint. These actions are restricted to [Admin users](/administration/roles) for security reasons, as they can modify or process large volumes of data at once.

## Run actions across all matching records with executeEntityActions

Use the `executeEntityActions` GraphQL function when you want to run an action across **all records that match a query** without manually paging through the search results yourself.

With the standard `search` pattern, your query returns a page of records and you perform an action against the records in that page. If the result set is larger than the page size, the client normally needs to request the next page and continue until all matching records have been processed.

`executeEntityActions` handles this traversal for you. CluedIn automatically scrolls through the matching records and applies the selected action across the complete result set.

This is useful for large bulk operations where you want CluedIn to manage record traversal rather than implementing pagination logic in your client.

### Syntax

The basic pattern is:

```graphql
{
  executeEntityActions(query: "entityType:/Customer") {
    actions {
      processEntityMetrics
    }
  }
}
```

In this example:

- `query` defines which records should be targeted.
- `executeEntityActions` finds all matching records.
- CluedIn automatically scrolls through the result set.
- `processEntityMetrics` is executed for each matching record.

You do not need to specify a page number or repeatedly call the query to process subsequent pages.

### Available actions

The actions exposed by `executeEntityActions` can include operations such as:

- `deduplicateEntity`
- `deleteEntity`
- `enrichEntity`
- `processEntityEdges`
- `processEntityMetrics`
- `processOutgoingStreams`
- `reprocessEntity`
- `splitEntity`

The exact list available in GraphQL introspection can depend on the CluedIn version and enabled functionality.

### Example: reprocess all Customer records

```graphql
{
  executeEntityActions(query: "entityType:/Customer") {
    actions {
      reprocessEntity
    }
  }
}
```

CluedIn finds all Customer records and reprocesses them without requiring the caller to manage pagination.

### Example: process outgoing streams

```graphql
{
  executeEntityActions(query: "entityType:/Product") {
    actions {
      processOutgoingStreams
    }
  }
}
```

This can be useful when you want matching Product records to be evaluated for outgoing stream processing in bulk.

### Example: target a filtered subset

You can use the same Lucene-style query syntax that is available elsewhere in CluedIn.

For example:

```graphql
{
  executeEntityActions(
    query: "entityType:/Customer AND properties.customer.country:Australia"
  ) {
    actions {
      enrichEntity
    }
  }
}
```

This applies the enrichment action to all matching Customer records from Australia, while CluedIn handles scrolling through the complete result set.

### Why use executeEntityActions

Use `executeEntityActions` instead of manually paging through `search` results when:

- The action should run against every record that matches a query.
- The result set can contain many records.
- You do not need to inspect each page in the client before running the action.
- You want CluedIn to manage scrolling and pagination internally.

This reduces client-side orchestration and avoids having to track page numbers, page sizes, or continuation logic for the bulk action.

{:.important}
`executeEntityActions` can apply an operation to a large number of records. Test the query carefully before running destructive or expensive actions such as deletion, deduplication, enrichment, splitting, or reprocessing.

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
Rebuild or recalculate relationships ([edges](/key-terms-and-features/edges)) between records.

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