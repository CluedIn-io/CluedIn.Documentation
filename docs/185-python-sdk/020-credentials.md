---
layout: cluedin
title: Context and Credentials
parent: Python SDK
permalink: /python-sdk/credentials
nav_order: 020
has_children: false
tags: ["python"]
last_modified: 2025-01-13
summary: "How to get CluedIn API context and credentials."
---
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

To connect to your CluedIn instance via API or CluedIn Python SDK, you need two things:
URL of your CluedIn instance
API (access) token - a JWT token that gives you access to API

CluedIn Python SDK uses the `Context` object to keep the information it needs to connect to CluedIn API.

## Import CluedIn Python SDK module

In the code examples below, we assume that you imported CluedIn module in your code:

```python
import cluedin
```

## Create a Context from API token

If you already have the API token, CluedIn Python SDK can build the Context for you:

```python
# assuming your API token is in the CLUEDIN_TOKEN variable
ctx = cluedin.Context.from_jwt(CLUEDIN_TOKEN)
```

Now, you can use the `ctx` Context variable to call CluedIn APIs.

## Create a Context from an object

You can also create a Context from a Python `dict`:

```python
# assumming you log in to https://foobar.contoso.com
# "foobar" is org_name, and "contoso.com" is the domain
context = {
    "domain": "contoso.com",
    "org_name": "foobar", 
    "access_token": CLUEDIN_TOKEN
}

ctx = cluedin.Context.from_dict(context)
```

## Create a Context from a file

Or from a file:

```python
# cluedin.json
# {
#     "domain": "contoso.com",
#     "org_name": "foobar", 
#     "access_token": CLUEDIN_TOKEN
# }

ctx = cluedin.Context.from_json_file("cluedin.json")
```

## Getting the API token from email and password

The API token lets you use some of CluedIn APIs like data ingestion endpoints and search, but to have full access to APIs (assuming you have the necessary permissions), you need to use the token that CluedIn gives you when you log in with your email and password. With the CluedIn Python SDK, you can set your email and password in the Context, and then call the `get_token` method to get the token:

```python
ctx = cluedin.Context.from_dict({
    "domain": "contoso.com",
    "org_name": "foobar", 
    "user_email": "joe@contoso.com",
    "user_password": "yourStrong(!)Password"
})

ctx.get_token() # after this line, `ctx.access_token` will be set
```
