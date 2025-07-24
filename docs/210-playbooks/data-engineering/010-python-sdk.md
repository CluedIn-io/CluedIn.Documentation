---
layout: cluedin
nav_order: 010
parent: Data engineering playbook
grand_parent: Playbooks
permalink: {{ site.baseurl }}/playbooks/data-engineering-playbook/python-sdk
tags: ["python"]
last_modified: 2025-01-14
title: CluedIn Python SDK
summary: "CluedIn Python SDK provides powerful REST and GraphQL APIs to interact with your CluedIn instance programmatically."
---

## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

CluedIn provides powerful REST and GraphQL APIs. To simplify programmatic interaction, we offer the [CluedIn Python SDK](https://pypi.org/project/cluedin/) — a Python package that handles authentication, automation, data import and export, data transformation, and data exploration.

You can use CluedIn Python SDK in many environments, from your local laptop to cloud services like:

- [Microsoft Fabric](https://www.microsoft.com/en-us/microsoft-fabric)
- [Azure Synapse Analytics](https://azure.microsoft.com/en-us/products/synapse-analytics)
- [Databricks](https://www.databricks.com/)
- [Snowflake](https://www.snowflake.com/)
- [Azure Functions](https://azure.microsoft.com/en-us/products/functions)
- [Jupyter Notebook](https://jupyter.org/)
- [Google Colab](https://colab.research.google.com/)
- [Airflow](https://airflow.apache.org/)
- [dbt](https://www.getdbt.com/)
- [Kaggle](https://www.kaggle.com/)

The above list is non-exhaustive. You can use CluedIn Python SDK in any environment where you can run Python code.

Some of the scenarios where CluedIn Python SDK will be helpful are:
- Querying data from your CluedIn instance.
- Exporting and saving the data to CSV, Parquet, Excel, JSON, or many other file formats.
- Reading and writing configuration of your CluedIn instance.
- Ingesting data in CluedIn.
- Automating repetitive actions to reduce manual work in UI.

## Getting started

[CluedIn Python SDK](https://pypi.org/project/cluedin/) supports Python from version 3.7 and above.

### Local environment

When you run Python scripts or notebooks on your local machine, we recommend using virtualenv or venv to ensure your local environment has the right version of Python and installed modules.

To install CluedIn Python SDK, run the following command in your shell:

```shell
pip install cluedin
```

### Cloud environments and notebooks

To install CluedIn Python SDK in a notebook, use `%pip` instead of `pip` and run the following command in your notebook's cell:

```shell
%pip install cluedin
```

Alternatively, when you use notebooks in tools like Microsoft Fabric, Databricks, etc., there is usually a way to configure the notebook's environment. For example, here's how to install a module in Microsoft Fabric: [https://learn.microsoft.com/en-us/fabric/data-engineering/create-and-use-environment](https://learn.microsoft.com/en-us/fabric/data-engineering/create-and-use-environment).

In all cases, after you install the `cluedin` package, you can import it in your Python code:

```python
import cluedin
```

## Authentication

To connect to your CluedIn instance via API or CluedIn Python SDK, you need two things:
URL of your CluedIn instance
API (access) token - a JWT token that gives you access to API

CluedIn Python SDK uses the `Context` object to keep the information it needs to connect to CluedIn API.

## Import CluedIn Python SDK module

In the code examples below, we assume that you imported CluedIn module in your code:

```python
import cluedin
```

## Creating a Context

### From API token

If you already have the API token, CluedIn Python SDK can build the Context for you:

```python
# assuming your API token is in the CLUEDIN_TOKEN variable
ctx = cluedin.Context.from_jwt(CLUEDIN_TOKEN)
```

Now, you can use the `ctx` Context variable to call CluedIn APIs.

### From an object

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

### From a file

```python
# cluedin.json
# {
#     "domain": "contoso.com",
#     "org_name": "foobar", 
#     "access_token": CLUEDIN_TOKEN
# }

ctx = cluedin.Context.from_json_file("cluedin.json")
```

### Getting API token from email and password

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
