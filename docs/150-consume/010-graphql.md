---
layout: cluedin
title: GraphQL
parent: Consume
nav_order: 3
has_children: true
permalink: consume/graphql
tags: ["consume","graphql"]
last_modified: 2021-10-08
---

CluedIn provides GraphQL as its way to pull and query data from it. The CluedIn GraphQL endpoint uses a combination of the different datastores to service the result of the query in question. 

You might find that a particular GraphQL query uses the Search, Graph and Blob Datastore to render the results. This is due to the query optimiser of CluedIn that determines the right datastore to serve the different parts of your query. This also allows immense flexibility with querying the data. An example would be that if we wanted to find all entities that are of a specific business domain and have a particular value for a property then you will find that the Search Store will service both these parts of the query and hence CluedIn will only ask it to service the query. If you then ask it to run this query, but return the full history of the records then CluedIn will run the search against the Search Store, but then using the results from the Search it will then ask the Blob Store to fetch the full object history out if it. Likewise, if you asked it to also return the records that are connected to these results of type Person, then it will most likely ask the Graph Store to fulfil that part of the query. 

![image](../assets/images/consume/simple-graphql-example.png)

The GraphQL endpoint has many different operations, including the ability to:

* Lookup entities by Id
* Lookup entities using a Full Text search
* Lookup entities using property value matches. 
* Lookup Metrics of Data

All value lookups are case sensitive by default and hence if you were to use our GraphQL search point to lookup organisation.industry:Banking then if you had a value in an entity that was “banking” (note the lower case “b”) then you would not match this data. Although this behaviour can be changed, there is a better way to handle this. One of the main ideas behind CluedIn is that we are going to give downstream consumers a standard representation of the data and hence “banking” and “Banking” are different variations of essentially the same value. We would rather that you use CluedIn Clean to normalise these values and standardise as a business on the way that you will represent values for downstream consumers. It is perfectly fine to not propagate these changes back to the sources using the Mesh API, but downstream consumers should receive a standardised representation of values. 

If you decide that you would like to enabled case incentive values, you will need to extend the inbuilt ElasticEntity model within CluedIn and add in your own properties with their respective analysers to achieve that. 

# Examples
To help you get upskilled on our GraphQL implementation, here are some examples for you to play with.

## Get an entity by Id

Obtain an example id by searching for your admin user:

![search for admin](../assets/images/consume/01-by-id-01.png)

~~~
{
  entity(id:"c2d38278-6886-532d-8405-98e97298298f")
  {
    name
  }
}
~~~

![image](../assets/images/consume/01-by-id-02.png)

## Get entities by search

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

![image](../assets/images/consume/02-by-search.png)

## Get entities by particular vocabulary keys

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


![image](../assets/images/consume/03-by-vocab-key.png)

## Get entities by a combination of vocabulary keys

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

![image](../assets/images/consume/04-by-vocab-key-combo.png)

## Get all entities that have a value for a certain property

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

![image](../assets/images/consume/05-certain-prop.png)

or just find out how many records match

~~~
{
  search(query: "properties.user.firstName:A*")
  {
    totalResults
  }
}
~~~

![image](../assets/images/consume/05-certain-prop-num-match.png)

## Change what properties come back in the results, 4 records at a time

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

![image](../assets/images/consume/06-what-props-pagesize4.png)

## Change what metadata comes out of the properties

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

![image](../assets/images/consume/07-what-metadata.png)

## Explore Edges

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

![image](../assets/images/consume/8.png)
