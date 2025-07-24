---
layout: cluedin
title: CluedIn Magic
parent: Data engineering playbook
grand_parent: Playbooks
permalink: playbooks/data-engineering-playbook/magic
nav_order: 060
tags: ["python"]
last_modified: 2025-01-15
summary: "CluedIn IPython Magic simplifies working with CluedIn in Jupyter notebooks."
---

## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

[IPython](https://ipython.org/),
the command shell behind [Jupyter](https://jupyter.org/) notebooks,
provides an awesome feature called [magics](https://ipython.readthedocs.io/en/stable/interactive/python-ipython-diff.html#magics).
In short, you can skip writing Python code and use more like command line syntax.

This approach can simplify many repeating tasks, including work with [CluedIn Python SDK](https://pypi.org/project/cluedin/).

In this article, I want to introduce you
to [CluedIn Magic](https://pypi.org/project/cluedin-magic/) - the package that lets you work with
CluedIn API with minimal code.

CluedIn Magic depends on CluedIn Python SDK, so you only need to install one package to get them both:

```shell
%pip install cluedin-magic
```

When working with products like Microsoft Fabric, Synapse Analytics, Databricks, etc.,
I usually pre-install packages in an environment so you don't have to run the above line.

Now, we can load CluedIn Magic by calling the `%load_ext` magic:

```shell
%load_ext cluedin_magic
```

After this, you can call `%cluedin` magic. If you do it without parameters or with wrong parameters, it will give you a brief help:

```
Available commands: get-context, search
Usage:
%cluedin get-context --jwt <jwt>
%cluedin search --context <context> --query <query> [--limit <limit>]
```

## Get CluedIn context

When you work with CluedIn API, you need a context—a domain, organization name,
email, password, or API token. What if I tell you that you just need the API token,
and then CluedIn Magic will automagically resolve the rest? Let's try it!

At first, you only need an API token &mdash; you can get one from
[Administration -> API Tokens](https://documentation.cluedin.net/integration/endpoint#send-data) in CluedIn.

In the example below, I store it in an environment variable and then can get into a variable:


```shell
access_token = %env ACCESS_TOKEN
```

```shell
ctx = %cluedin get-context --jwt $access_token
```

Now, just give it to CluedIn Magic and it will give you a working CluedIn context:

```shell
ctx = %cluedin get-context --jwt eyJhbGci...5Odvpr1g
```

You can use this context now with CluedIn Python SDK or CluedIn Magic.

## Search

Say you want to load all `/Infrastructure/User` entities &mdash;
provide a context and a query, and get a pandas DataFrame with your data:

```shell
%cluedin search --context ctx --query +entityType:/Infrastructure/User
```

<img src="/assets/images/python-sdk/notebook.png" alt="notebook" />

You can get a sample by providing a limit if you have millions of entities.
In the next example, I get ten entities out of all entities in the system:

```shell
%cluedin search --context ctx --query * --limit 10
```

In the next example, I get ten records of type
`/IMDb/Name` where `imdb.name.birthYear` vocabulary key property does not equal `\\N`:

```shell
%cluedin search --context ctx --query +entityType:/IMDb/Name -properties.imdb.name.birthYear:"\\\\N" --limit 10
```

You can also save the results in a variable and use it as a usual pandas DataFrame:

```shell
pd = %cluedin search --context ctx --query +entityType:/IMDb/Name +properties.imdb.name.birthYear:1981
pd.head()
```
