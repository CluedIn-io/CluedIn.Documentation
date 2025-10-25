---
layout: cluedin
title: About integrations
parent: Crawlers
grand_parent: Ingestion
nav_order: 010
has_children: false
permalink: /integration/introduction
tags: ["integration"]
last_modified: 2022-01-12
---

## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

When CluedIn is running, the first step is to feed it with data. You decide which data to add, and this is done through integrations. You have two options:

- [Install an existing integration](./install-integrations)
- Build a custom integration

{:.important}
When you install CluedIn, you get access to out-of-the-box integrations. Contact us if you need help configuring or enabling them. We can also implement custom integrations on request.

## Types of integrations

There are two main types of integrations:

- Providers

- Enrichers

## Providers

Providers allow you to add data into CluedIn:

- They can connect to cloud tools, databases, file systems, and so on.

- They extract the data you want and format it so CluedIn can understand it.

There are many providers available in our [GitHub repository](https://github.com/CluedIn-io). You can also [build your own providers](./build-integration), but this requires C# coding experience.

Common provider types include:
* [Crawlers](https://github.com/CluedIn-io?q=crawl&type=public)
* [Connectors](https://github.com/CluedIn-io?q=connect&type=public)

## Enrichers

Enrichers add extra information to data that is already in CluedIn:

- Data in CluedIn is structured as entities (similar to records) – for example, a person, a company, or a task.

- An enricher uses the existing information in CluedIn to query external systems for additional details about that entity.

We have a list of available enrichers in our [GitHub repository](https://github.com/CluedIn-io?q=enricher&type=public). You can also [build your own enrichers](/preparation/enricher/build-custom-enricher) if you have some C# coding experience.
