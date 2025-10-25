---
layout: cluedin
title: GraphQL
parent: Consume
nav_order: 3
has_children: true
permalink: /consume/graphql
tags: ["consume","graphql"]
last_modified: 2021-10-08
---
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

CluedIn provides GraphQL as a flexible way to pull and query data. The CluedIn GraphQL endpoint integrates multiple datastores to service each query efficiently, using an internal query optimizer to determine which datastore should handle which part of the request.

## How it works

Depending on the query, CluedIn may interact with one or more of the following datastores:

- Search store – For full-text searches and property-based lookups.

- Graph store – For exploring relationships and connected records.

- Blob store – For retrieving complete record histories and raw data.

The query optimizer automatically selects the best datastore combination for each query.

Consider the following example:

- A query that finds all entities in a specific business domain with a certain property value is handled entirely by the Search store.

- If the query also requests the full history of those records, CluedIn first retrieves the results from the Search store, and then asks the Blob store for historical data.

- If the query expands to include related records (for example, entities of the Person type connected to the results), CluedIn adds the Graph store to process that part of the query.

![image]({{ "/assets/images/consume/simple-graphql-example-2.png" | relative_url }})

## Supported operations

The CluedIn GraphQL endpoint supports a wide range of operations, including:

* Get entities by ID.

* Get entities using a full-text search.

* Get entities by property value.

* Get data metrics.

## Case sensitivity in lookups

By default, all value lookups are case-sensitive. For example, `organisation.industry:Banking` will not match entities where the value is "banking" (lowercase “b”).

While you can modify this behavior, CluedIn encourages using CluedIn Clean to normalize and standardize data values. This ensures that downstream consumers receive consistent data (for example, "Banking" vs "banking") without requiring schema or query adjustments.

You can standardize capitalization and formatting conventions without pushing changes back to the original source systems through the Mesh API.

## Enabling case-insensitive lookups

If you need to enable case-insensitive searches, extend the built-in ElasticEntity model within CluedIn and add custom properties with their respective analyzers to support case-insensitive matching.

## Examples of using GraphQL

To help you get familiar with CluedIn’s GraphQL implementation, the following examples illustrate common queries you can experiment with.

### Get an entity by ID

You can retrieve a specific entity using its unique ID. To begin, you will need to obtain an example ID by searching for your admin user.

![search for admin]({{ "/assets/images/consume/01-by-id-01-2.png" | relative_url }})

~~~
{
  entity(id:"c2d38278-6886-532d-8405-98e97298298f")
  {
    name
  }
}
~~~

![image]({{ "/assets/images/consume/01-by-id-02-2.png" | relative_url }})

### Get entities by search

~~~
{
  search(query:"Test")
  {
    entries
    {
      name
    }
  }
}
~~~

![image]({{ "/assets/images/consume/02-by-search-2.png" | relative_url }})

### Get entities by vocabulary keys

~~~
{
  search(query:"properties.user.firstName:Alix")
  {
    entries
    {
      name
    }
  }
}
~~~


![image]({{ "/assets/images/consume/03-by-vocab-key-2.png" | relative_url }})

### Get entities by a combination of vocabulary keys

~~~
{
  search(query: "+properties.user.firstName:Alix +properties.user.lastName:Freke")
  {
    entries
    {
      name
    }
  }
}
~~~

![image]({{ "/assets/images/consume/04-by-vocab-key-combo-2.png" | relative_url }})

### Get all entities that have a value for a certain property

~~~
{
  search(query: "properties.user.firstName:A*")
  {
    totalResults
    entries
    {
      name
    }
  }
}
~~~

![image]({{ "/assets/images/consume/05-certain-prop-2.png" | relative_url }})

Alternatively, find out how many records match.

~~~
{
  search(query: "properties.user.firstName:A*")
  {
    totalResults
  }
}
~~~

![image]({{ "/assets/images/consume/05-certain-prop-num-match-2.png" | relative_url }})

### Change what properties come back in the results, 4 records at a time

~~~
{
  search(query: "properties.user.firstName:A*", pageSize:4)
  {
    totalResults
    entries
    {
      name
      createdDate
      displayName
      properties
    }
  }
}
~~~

![image]({{ "/assets/images/consume/06-what-props-pagesize4-2.png" | relative_url }})

### Change what metadata comes out of the properties

~~~
{
  search(query: "properties.user.firstName:A*", pageSize:4)
  {
    totalResults
    entries
    {
      name
      properties(propertyNames:["user.lastName", "user.gender"])
    }
  }
}
~~~

![image]({{ "/assets/images/consume/07-what-metadata-2.png" | relative_url }})

### Explore edges

~~~
{
  search(query: "user.firstName:*", pageSize: 4) {
    entries {
      name
      edges {
        outgoingOfType(entityType: "/Organization", edgeType: "/PartOf") {
          entries {
            name
          }
        }
      }
    }
  }
}
~~~

![image]({{ "/assets/images/consume/8-2.png" | relative_url }})
