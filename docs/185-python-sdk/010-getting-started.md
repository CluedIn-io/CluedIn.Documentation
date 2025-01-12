---
layout: cluedin
title: Getting Started
parent: Python SDK
permalink: /python-sdk/getting-started
nav_order: 010
has_children: false
tags: ["python"]
last_modified: 2025-01-12
summary: "Learn how to install CluedIn Python SDK in your local environment or cloud services."
---
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

[CluedIn Python SDK](https://pypi.org/project/cluedin/) supports Python from version 3.7 and above.

## Local environment

When you run Python scripts or notebooks on your local machine, we recommend using virtualenv or venv to ensure your local environment has the right version of Python and installed modules.

To install CluedIn Python SDK, run the following command in your shell:

```shell
pip install cluedin
```

## Cloud environments and notebooks

To install CluedIn Python SDK in a notebook, use `%pip` instead of `pip` and run the following command in your notebook's cell:

```shell
%pip install cluedin
```

Alternatively, when you use notebooks in tools like Microsoft Fabric, Databricks, etc., there is usually a way to configure the notebook's environment. For example, here's how to install a module in Microsoft Fabric: [https://learn.microsoft.com/en-us/fabric/data-engineering/create-and-use-environment](https://learn.microsoft.com/en-us/fabric/data-engineering/create-and-use-environment).

In all cases, after you install the `cluedin` package, you can import it in your Python code:

```python
import cluedin
```

