---
layout: cluedin
nav_order: 3
parent: Data engineering playbook
grand_parent: Playbooks
permalink: /playbooks/data-engineering-playbook/customization-in-cluedin
title: Customization in CluedIn
last_modified: 2025-02-03
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article, you will learn about custom solutions that can be implemented in CluedIn. While this article focuses on the most common customization options, do not hesitate to reach out to CluedIn support if your use case requires other solutions.

## Custom rule actions

In CluedIn, there are three types of rules: data part rules, survivorship rules, and golden record rules. For a detailed explanation, see [Rule types](/management/rules/rule-types). Regardless of the type of rule, the rule structure is the same. A rule is an object that allows you to transform the data and modify the data processing logic. Every rule consists of several building blocks.

![customization-in-cluedin-rules.png](../../assets/images/playbooks/customization-in-cluedin-rules.png)

- **Filters** – conditions that define which golden records are affected by the rule.

- **Actions** – modifications applied to golden records that match the rule's filters and conditions. Each action contains additional settings allowing you to define the modifications to be executed on the data.

    Let's take the **Set Value** action as an example. The purpose of this action is to modify the value of a specific vocabulary key in golden records that match the rule's filters and conditions. To configure this action, you need to provide the name of the vocabulary key (**Field Name**) as well as select the desired value for that vocabulary key (**Value**).

- **Conditions** – additional criteria on top of the filters to define which golden records are affected by the specific action.

CluedIn offers a variety of [actions](/management/rules/rules-reference) for each rule type to cover the most common data transformation tasks. However, if you need a custom action for your use case, reach out to CluedIn support. Our in-house Data Engineers will help you implement a custom solution.

**Example of custom rule action**

One of the examples of custom rule actions if the **Enrich** action. It provides a flexible way to enrich data in CluedIn with external data sources.

The **Enrich** action requires an API that accepts a list of vocabulary keys and returns a list of properties. The returned properties are saved with a specified vocabulary prefix. The API can be implemented as an Azure Function, a REST API, or any other service that can be accessed via HTTP.
The API is also responsible for getting the data from the external source, processing it, and returning the properties to CluedIn.

The **Enrich** action takes the following parameters:

- **URL** – the URL of the enriching API.

- **Payload** – comma-separated list of vocabulary keys to send to the API.

- **Vocabulary Prefix** – the vocabulary prefix used to save properties returned by the API.

When the **Enrich** action is invoked, it sends the payload to the API (HTTP POST) and saves the returned properties with the specified vocabulary prefix. If you would like to implement the **Enrich** action, reach out to CluedIn support.

## Custom connectors for a stream

CluedIn offers a variety of [connectors](/consume/export-targets/connector-reference) to cater for different export systems. Among them are OneLake, SQL Server, Azure Data Lake, and many others. If you cannot find the needed connector in the list and require a custom solution, reach out to CluedIn support and our Data Engineers will help you implement a custom solution.

**Example of custom connector**

One of the examples of custom connectors is **Kafka**. It provides an efficient way to export golden records from CluedIn to Kafka.

The Kafka connector requires the following parameters:

- **Bootstrap Servers** – Kafka server address.

- **SASL Username** – the username or the key.

- **SASL Password** – the secret or the password.

When you start the stream with the Kafka connector, CluedIn first checks if the connection can be established. Then, CluedIn checks for the streaming mode—event mode or synchronized—that is used in the particular export target configuration. Finally, every time a golden record is modified in CluedIn, the corresponding event is sent to Kafka. If you use Kafka in your operations and would like to send golden records from CluedIn to Kafka topic, reach out to CluedIn support.