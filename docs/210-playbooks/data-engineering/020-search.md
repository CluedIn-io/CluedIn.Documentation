---
layout: cluedin
title: Query data using GraphQL and Python SDK
parent: Data engineering playbook
grand_parent: Playbooks
permalink: /playbooks/data-engineering-playbook/search
nav_order: 020
tags: ["python"]
last_modified: 2025-01-14
summary: "How to query data using GraphQL and the CluedIn Python SDK."
---


## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

## GraphQL Search API

CluedIn provides a powerful GraphQL API that is very helpful in almost every interaction with CluedIn
(one of a few exceptions is Ingestion Endpoints that are not GraphQL).
You can read about CluedIn GraphQL in a separate article: [documentation.cluedin.net/consume/graphql](https://documentation.cluedin.net/consume/graphql).

When you open the Consume section in your CluedIn instance,
you will find a GraphQL playground where you can run GraphQL queries.

In our example, we have some `/Duck` entities
(from the [DuckTales](https://en.wikipedia.org/wiki/DuckTales)).
To find them, I can run a query like this:

### Simple GraphQL search query

```graphql
{
  search(query:"+entityType:/Duck")
  {
    entries {
      id
      name
      entityType
    }
  }
}
```

The query will return me the top 20 of the `/Duck` entities.
The `query` parameter tells the API to filter the response by a given business domain (previously entity type).
You can also specify the entity properties you want to get in the payload: `id`, `name`, and `entityType`.

### GraphQL search query with variables and cursor

We can sophisticate the query a little so that it will take parameters from the GraphQL variables:

```graphql
query ($query: String, $pageSize: Int) {
  search(
    query: $query
    pageSize: $pageSize
    sort: FIELDS
    sortFields: {field: "id", direction: ASCENDING}
  ) {
    cursor
    entries {
      id
      name
      entityType
    }
  }
}
```

Variables:

```json
{
  "query": "+entityType:/Duck",
  "pageSize": 10000
}
```

Here are a few things to notice in this query:
- `query ($query: String, $pageSize: Int)` - we defined a query with parameters. We can also give this query a name: `query searchEntities($query: String, $pageSize: Int)`
- `sort: FIELDS sortFields: {field: "id", direction: ASCENDING}` - it's important to sort by a unique field to get predictable results when you page data.
- `cursor` - we ask CluedIn to return a special value that we can pass to our next query to get the next page of results.
- `"pageSize": 10000` - By default, the page size is 20, so if you have millions of entities, you will get only the first `20`. Setting the page size to its maximum value (`10000`) will decrease the number of requests you send to CluedIn API, but there are situations when you only want to get a few entities from the top, and a query with a smaller page size will be faster.

![GraphQL](/assets/images/python-sdk/gql.png)

## CluedIn Python SDK

### Installation and initialization

You can use any programming language to send a GraphQL request to CluedIn and get the data back. Let's explore how you can do it in Python.

First of all, you will need to install the latest version of CluedIn Python SDK:

```python
%pip install cluedin
```

Let's import it then together with Pandas (we will use Pandas to load data in DataFrames):

```python
import pandas as pd
import cluedin
```

You need an API token; you can copy or create a new one by going to "API Tokens" under "Administration" in CluedIn.

Now, in our example, CluedIn is installed at `https://foobar.contoso.com/`,
so we need to initialize a Context for our CluedIn instance by providing `org_name` (`foobar`), `domain` (`contoso.com`), and the `access_token` (the one you copied from CluedIn UI):


```python
ctx = cluedin.Context.from_dict({
    'domain': 'contoso.com',
    'org_name': 'foobar',
    'access_token': '{paste_your_token_here}'
})
```

### Running a GraphQL query

We can now run GraphQL queries from Python code:

```python
query = """
query searchEntities($query: String, $pageSize: Int) {
  search(
    query: $query
    pageSize: $pageSize
    sort: FIELDS,
    sortFields: {field: "id", direction: ASCENDING}
  ) {
    cursor
    entries {
      id
      name
      entityType
    }
  }
}
"""

variables = {
    'query': '+entityType:/Duck',
    'pageSize': 3
}

cluedin.gql.gql(ctx, query=query, variables=variables)
```

The result is top three entities (because we use the page size = 3 for demo purpose),
and we also get a cursor that we can use to get the next page:

```python
{'data': {'search': {'cursor': 'ewAiAFAAYQBnAGUAIgA6ADEALAAiAFAAYQBnAGUAUwBpAHoAZQAiADoAMwAsACIAQwBvAG0AcABvAHMAaQB0AGUAQQBmAHQAZQByACIAOgB7AH0ALAAiAFMAZQBhAHIAYwBoAEEAZgB0AGUAcgAiADoAWwAiADYAMwA1ADMAOAAzAGEAOQAtADkAYwA3ADUALQA1AGQANgAxAC0AOABmADIAYgAtAGYAZQA0ADkANgBmAGQAOAAyAGIAZQA3ACIALAAiADYAMwA1ADMAOAAzAGEAOQAtADkAYwA3ADUALQA1AGQANgAxAC0AOABmADIAYgAtAGYAZQA0ADkANgBmAGQAOAAyAGIAZQA3ACIAXQB9AA==',
   'entries': [{'id': '145afb55-4e78-5dad-b208-633b5b6d19cf',
     'name': 'Donald Duck',
     'entityType': '/Duck'},
    {'id': '17bad60e-6782-5ae5-84bf-7efe05e78e58',
     'name': 'Jake McDuck',
     'entityType': '/Duck'},
    {'id': '635383a9-9c75-5d61-8f2b-fe496fd82be7',
     'name': 'Dewey Duck',
     'entityType': '/Duck'}]}}}
```

### Getting the next page

We can change our code to pass the cursor as a parameter:

```python
query = """
query searchEntities($cursor: PagingCursor, $query: String, $pageSize: Int) {
  search(
    query: $query
    cursor: $cursor
    pageSize: $pageSize
    sort: FIELDS,
    sortFields: {field: "id", direction: ASCENDING}
  ) {
    cursor
    entries {
      id
      name
      entityType
    }
  }
}
"""

variables = {
    'query': '+entityType:/Duck',
    'pageSize': 3
    'cursor': 'ewAiAFAAYQBnAGUAIgA6ADEALAAiAFAAYQBnAGUAUwBpAHoAZQAiADoAMwAsACIAQwBvAG0AcABvAHMAaQB0AGUAQQBmAHQAZQByACIAOgB7AH0ALAAiAFMAZQBhAHIAYwBoAEEAZgB0AGUAcgAiADoAWwAiADYAMwA1ADMAOAAzAGEAOQAtADkAYwA3ADUALQA1AGQANgAxAC0AOABmADIAYgAtAGYAZQA0ADkANgBmAGQAOAAyAGIAZQA3ACIALAAiADYAMwA1ADMAOAAzAGEAOQAtADkAYwA3ADUALQA1AGQANgAxAC0AOABmADIAYgAtAGYAZQA0ADkANgBmAGQAOAAyAGIAZQA3ACIAXQB9AA=='
}

cluedin.gql.gql(ctx, query=query, variables=variables)
```

The result is the next three entities:

```python
{'data': {'search': {'cursor': 'ewAiAFAAYQBnAGUAIgA6ADIALAAiAFAAYQBnAGUAUwBpAHoAZQAiADoAMwAsACIAQwBvAG0AcABvAHMAaQB0AGUAQQBmAHQAZQByACIAOgB7AH0ALAAiAFMAZQBhAHIAYwBoAEEAZgB0AGUAcgAiADoAWwAiADkAMwBiADkAMgA4ADMANQAtADkANgBmADIALQA1ADYAYQA5AC0AOQA4AGMAMAAtAGMAOAA0ADgAMgAzADYANQAyADEAYQA5ACIALAAiADkAMwBiADkAMgA4ADMANQAtADkANgBmADIALQA1ADYAYQA5AC0AOQA4AGMAMAAtAGMAOAA0ADgAMgAzADYANQAyADEAYQA5ACIAXQB9AA==',
   'entries': [{'id': '6ae43a44-81b4-5fd7-9c7b-47cb24d407ea',
     'name': 'Angus McDuck',
     'entityType': '/Duck'},
    {'id': '9353b703-13d8-59a1-886c-f40b95283c06',
     'name': 'Hortense McDuck',
     'entityType': '/Duck'},
    {'id': '93b92835-96f2-56a9-98c0-c848236521a9',
     'name': 'Matilda McDuck',
     'entityType': '/Duck'}]}}}
```

### Using a generator

But what if you want to avoid manually passing a new cursor to every new call?
You can just use the `cluedin.gql.entries` method, and it will return you
a [Generator](https://wiki.python.org/moin/Generators)
that you can convert to a list or just iterate as you wish:

```python
...

# this is where you need a smaller page size
# if you don't want to iterate to the end
variables = {
    'query': '+entityType:/Duck',
    'pageSize': 2
}

generator = cluedin.gql.entries(ctx, query=query, variables=variables)
print(next(generator))
print(next(generator))
```

Result:


```python
{'id': '145afb55-4e78-5dad-b208-633b5b6d19cf', 'name': 'Donald Duck', 'entityType': '/Duck'}
{'id': '17bad60e-6782-5ae5-84bf-7efe05e78e58', 'name': 'Jake McDuck', 'entityType': '/Duck'}
```

### Using automatic pagination

You can also load all entities in a DataFrame, in this case,
it makes sense using the maximum page size (`10000`) to reduce the number of calls to the server:

```python
query = """
query searchEntities($cursor: PagingCursor, $query: String, $pageSize: Int) {
  search(
    query: $query
    cursor: $cursor
    pageSize: $pageSize
    sort: FIELDS,
    sortFields: {field: "id", direction: ASCENDING}
  ) {
    cursor
    entries {
      id
      name
      entityType
    }
  }
}
"""

variables = {
    'query': '+entityType:/Duck',
    'pageSize': 10_000
}

print(pd.DataFrame(cluedin.gql.entries(ctx, query=query, variables=variables)))
```

Result:

```text
                                      id             name entityType
0   145afb55-4e78-5dad-b208-633b5b6d19cf      Donald Duck      /Duck
1   17bad60e-6782-5ae5-84bf-7efe05e78e58      Jake McDuck      /Duck
2   635383a9-9c75-5d61-8f2b-fe496fd82be7       Dewey Duck      /Duck
3   6ae43a44-81b4-5fd7-9c7b-47cb24d407ea     Angus McDuck      /Duck
4   9353b703-13d8-59a1-886c-f40b95283c06  Hortense McDuck      /Duck
5   93b92835-96f2-56a9-98c0-c848236521a9   Matilda McDuck      /Duck
6   a388a77d-7d43-51d1-87b2-efb4f854b5ad    Fergus McDuck      /Duck
7   b2fb05cb-e806-5088-955b-2ff3f9261236   Scrooge McDuck      /Duck
8   b8fc5baf-b679-5e26-abb5-50ca77467992        Huey Duck      /Duck
9   cd8fe1dd-5637-5037-931e-f8bf1a15c0b4       Della Duck      /Duck
10  f5bf5d66-5698-515a-800e-9d778d916dcd       Louie Duck      /Duck
```

### Using the search method

Starting from CluedIn Python SDK 2.5.0,
you can shrink the code above to one line and get almost the same result.
The difference is that it will also return you all codes and properties of entities,
and you don't have to copy and paste the same GraphQL query every time you want to query some data:

```python
# this will return all the queried entities with all properties and codes
print(pd.DataFrame(cluedin.gql.search(ctx, '+entityType:/Duck')))
```

### Using the search method with a subset of data

Finally, if you only want a subset of data, you can use the `itertools.islice`,
but then remember to set a smaller `page_size` to not query more data than you need:

```python
from itertools import islice

# gets a generaror that queries entities from the server by three
gen = cluedin.gql.search(ctx, '+entityType:/Duck', page_size=3)

# wrap in an iterator that stops after three iterations
iter = islice(gen, 3)

# convert to DataFrame
df = pd.DataFrame(iter)

print(df)
```

Or simply:
    
```python
pd.DataFrame(itertools.islice(cluedin.gql.search(ctx, '+entityType:/Duck', 3), 3))
```

## GraphQL Actions

You can add GraphQL [Actions](/consume/graphql/graphql-actions) when running GraphQL queries in the Python SDK. Actions are a way to run commands in bulk, such as processing, enriching, or deleting entities.

For example, if you take the previous GraphQL query and add an `actions` field to it, you can delete, enrich or process entities entities in bulk. Here is an example of bulk enrichment:

```graphql
query searchEntities($cursor: PagingCursor, $query: String, $pageSize: Int) {
  search(
    query: $query
    cursor: $cursor
    pageSize: $pageSize
    sort: FIELDS,
    sortFields: {field: "id", direction: ASCENDING}
  ) {
    cursor
    entries {
      id
      name
      entityType
      actions {
        enrich
      }
    }
  }
}
```

And here is another example of how to use Actions in the Python SDK to delete entities (please note that this is a destructive operation and should be used with caution): [delete_entities.py](https://gist.github.com/romaklimenko/8092c9161a2bde7d981dd34a5c58888b).

Here is a list of available actions you can use:

- `deleteEntity` - deletes an entity.
- `postProcess` - reprocesses an entity.
- `enrichEntity` - enriches an entity.
