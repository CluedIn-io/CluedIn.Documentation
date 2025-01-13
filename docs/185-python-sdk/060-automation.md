---
layout: cluedin
title: Automation
parent: Python SDK
permalink: /python-sdk/automation
nav_order: 060
has_children: false
tags: ["python"]
last_modified: 2025-01-12
summary: "How to automate tasks using the CluedIn Python SDK."
---
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

CluedIn, as a Master Data Management system, encourages users to work with data using a UI and low-code approach.
You can do a full data cycle from ingesting data into CluedIn to data modeling,
transformation, cleaning, enriching, deduplication, and export without writing a single line of code.

However, there are situations when automation and basic scripting can save the day.
Moreover, in the same way as we can free business users from dealing with IT and code,
we can free them from repetitive actions in UI when, for example, you implement a CI/CD pipeline between your development, staging, and production instances.

In this article, we will implement basic automation without knowing too much about it beforehand.
Let's start with the fact that CluedIn UI communicates with the server via GraphQL API.

## Two GraphQL API endpoints

CluedIn provides two GraphQL API endpoints:

- `/api/api/graphql` - the endpoint used to query data.
- `/graphql` - the endpoint for UI interactions.

## Authentication

CluedIn uses [JWT token](https://jwt.io/introduction)-based authorization.

There are two kinds of tokens in CluedIn: API Tokens and Access Tokens. 

API Tokens are used to extract or ingest data from and into CluedIn. You can create or copy an API Token from [Administration -> API Tokens](https://documentation.cluedin.net/integration/endpoint#send-data). 

The Access Tokens are generated when you log in to CluedIn as a user.

You need an API Token to use the `/api/api/graphql` endpoint.

The `/graphql` endpoint only accepts Access Tokens, so you must log in with your email and password to obtain one.

## Exploring GraphQL API

In this article, we explore a use case of automating the actions you usually do in UI with the help of CluedIn GraphQL API and [CluedIn Python SDK](https://pypi.org/project/cluedin/).

Let's use a simple example: You want to automate Vocabulary creation. You can do it from the CluedIn UI, but you would prefer an automated approach to synchronize Vocabularies from another place.

The first thing you can do is create a test Vocabulary in a browser and see how the API calls look. You can do it with the [Network](https://developer.chrome.com/docs/devtools/network) tab or with the help of [GraphQL Network Inspector](https://chromewebstore.google.com/detail/graphql-network-inspector/ndlbedplllcgconngcnfmkadhokfaaln) (better).

Let's try both approaches. First, I go to UI and create a test CluedIn Vocabulary while I have my Network tab opened:

![Network tab](/assets/images/python-sdk/network-tab.png)

Now, when I inspect GraphQL queries, I can see the `createVocabulary` mutation call:

![GraphQL Inspector](/assets/images/python-sdk/network-tab-create-vocabulary.png)

Finding the right call is even easier with GraphQL Network Inspector:

![GraphQL Inspector](/assets/images/python-sdk/graphql-inspector-create-vocabulary.png)

No matter how we found it, now we can copy the GraphQL query:

```graphql
mutation createVocabulary($vocabulary: InputVocabulary) {
  management {
    id
    createVocabulary(vocabulary: $vocabulary) {
      ...Vocabulary
      __typename
    }
    __typename
  }
}

fragment Vocabulary on Vocabulary {
  vocabularyId
  vocabularyName
  keyPrefix
  isCluedInCore
  entityTypeConfiguration {
    icon
    entityType
    displayName
    __typename
  }
  isDynamic
  isProvider
  isActive
  grouping
  createdAt
  providerId
  description
  connector {
    id
    name
    about
    icon
    __typename
  }
  __typename
}
```

And the variables:

```json
{
  "vocabulary": {
    "vocabularyName": "Test",
    "entityTypeConfiguration": {
      "new": false,
      "icon": "Profile",
      "entityType": "/IMDb/Name",
      "displayName": "IMDb Name"
    },
    "providerId": "",
    "keyPrefix": "test",
    "description": ""
  }
}
```

## Python SDK

Now, we can use the CluedIn Python SDK to create a Vocabulary.

First of all, I create a file with my CluedIn credentials. You can also provide them via environment variables:

```json
{
  "domain": "172.167.52.102.sslip.io",
  "org_name": "foobar",
  "user_email": "admin@foobar.com",
  "user_password": "mysecretpassword"
}
```

Then, I install the CluedIn Python SDK:

```bash
%pip install cluedin
```

Next, I need to "log in" to CluedIn to get the Access Token:

```python
import cluedin

ctx = cluedin.Context.from_json_file('cluedin.json')
ctx.get_token()
```

The `ctx` object now contains the Access Token, and I can use it to create a Vocabulary:

```python
def create_vocabulary(ctx, name, prefix):
  query = """
mutation createVocabulary($vocabulary: InputVocabulary) {
  management {
    id
    createVocabulary(vocabulary: $vocabulary) {
      ...Vocabulary
    }
  }
}
fragment Vocabulary on Vocabulary {
  vocabularyId
  vocabularyName
  keyPrefix
  entityTypeConfiguration {
    icon
    entityType
    displayName
  }
  providerId
  description
}
"""

  variables = {
    "vocabulary": {
      "vocabularyName": name,
      "entityTypeConfiguration": {
        "new": False,
        "icon": "Profile",
        "entityType": "/IMDb/Name",
        "displayName": "IMDb Name"
      },
      "providerId": "",
      "keyPrefix": prefix,
      "description": ""
    }
  }

  return cluedin.gql.org_gql(ctx, query, variables)
```

Let's test it:

```python
print(create_vocabulary(ctx, 'Foo Bar', 'foo.bar'))
```

Output:

```json
{
  "data": {
    "management": {
      "id": "management",
      "createVocabulary": {
        "vocabularyId": "e4528e92-f4ad-406a-aeab-756acc20fd01",
        "vocabularyName": "Foo Bar",
        "keyPrefix": "foo.bar",
        "entityTypeConfiguration": {
          "icon": "Profile",
          "entityType": "/IMDb/Name",
          "displayName": "IMDb Name"
        },
        "providerId": null,
        "description": ""
      }
    }
  }
}
```

Check the UI:

![New Vocabulary](/assets/images/python-sdk/new-vocabulary.png)

Here are a couple more of examples used on real projects:

- Create missing Vocabularies and keys for a given Entity: [https://gist.github.com/romaklimenko/a203c3ef63b4106304e62f6f816d7e25](https://gist.github.com/romaklimenko/a203c3ef63b4106304e62f6f816d7e25)
- Explore a CluedIn Entity's Data Parts to troubleshoot overmerging: [https://gist.github.com/romaklimenko/d5a07dde12e8f215d69131de47976d7d](https://gist.github.com/romaklimenko/d5a07dde12e8f215d69131de47976d7d)
