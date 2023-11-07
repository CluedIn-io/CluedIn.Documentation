---
layout: default
title: What are Integrations
parent: Integration
nav_order: 070
has_children: false
permalink: /integration/introduction
tags: ["integration"]
last_modified: 2022-01-12
---


## Introduction

The first thing you need to do when CluedIn is running, is to feed it with Data. You need to choose which data you want to add to CluedIn. Data is pushed into CluedIn via integrations. You have two options

- [Installing an existing integration](./install-integrations)
- Building a custom integration

![Diagram](../assets/images/integration/intro-integrate.png)

There are two main types of integrations:

### Providers

These integrations allow you to add data into CluedIn. They can connect to cloud tools, databases, file systems, etc. extract the data you want to send to CluedIn and assemble it in a format CluedIn will understand.

There are many *providers* available in our [GitHub](https://github.com/CluedIn-io), but alternatively you can also [build your own](./build-integration) to cater for your specific requirements. In order to do this though, you will require some C# coding experience.

Some of the most common *providers* are the following:
* [Crawlers](https://github.com/CluedIn-io?q=crawl&type=public)
* [Connectors](https://github.com/CluedIn-io?q=connect&type=public)

### Enrichers

Their mission is to add extra information to improve data that is already in CluedIn. Data in CluedIn is structured in entities; these are similar to records. They can contain information about a person, a company, a task, etc. An enricher will use the existing information CluedIn to then query other external systems to try to find out more information about that entity, i.e. *enrich* it.

We have a list of available *enrichers* in our [GitHub](https://github.com/CluedIn-io?q=enricher&type=public), but you can also [build your own](./build-enricher), as long as you have some C# coding experience. 
