---
layout: cluedin
nav_order: 3
parent: Data engineering playbook
grand_parent: Playbooks
permalink: /playbooks/data-engineering-playbook/customization-in-cluedin
title: Customization in CluedIn
last_modified: 2025-02-05
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article, you will learn about customizations that can be implemented in CluedIn. While this article focuses on the most common customization options, do not hesitate to reach out to CluedIn Customer Success Team if your use case requires other solutions.

![customization-options.png](../../assets/images/playbooks/customization-options.png)

## Customization of data ingestion

CluedIn offers multiple [options](https://documentation.cluedin.net/playbooks/data-ingestion-playbook/pick-the-right-tool) for getting your data into the platform. However, you can further customize the data ingestion process if your use case requires it.

![customization-options-ingestion-without-validation.png](../../assets/images/playbooks/customization-options-ingestion-without-validation.png)

There are two ways to customize data ingestion in CluedIn:

- **Customization via advanced mapping** – if you want to customize the CluedIn mapping experience, you can write JavaScript code at any time. This can be useful for implementing complex conditional mapping, as the UI mapping may become too complex for such tasks. For more information, see [Advanced mapping code](/integration/additional-operations-on-records/advanced-mapping-code).

- **Customization via crawler written in C#** – if the existing options for ingesting data into CluedIn do not meet your needs—for example, if neither Azure Data Factory, Microsoft Fabric, nor CluedIn have a specific connector—you can use a custom crawler. This can be useful if you use a legacy system that works on-premises or a very custom system. You can get acquainted with the example of crawler template [here](https://github.com/CluedIn-io/CluedIn.Connector.SqlServer).

## Customization of rules

In CluedIn, there are three [types of rules](/management/rules/rule-types): data part rules, survivorship rules, and golden record rules. Regardless of the type of rule, the rule structure is the same. Essentially, a rule is an object that allows you to transform the data and modify the data processing logic. 

CluedIn offers a variety of [actions](/management/rules/rules-reference) for each rule type to cover the most common data transformation tasks. However, if out-of-the-box actions are not enough, and you need something non-standard, you can write custom rule actions.

![customization-options-rules.png](../../assets/images/playbooks/customization-options-rules.png)

There are three ways to customize rule actions in CluedIn:

- **Custom action in data part rules written in C#** – if the [list of actions in data part rules](/management/rules/rules-reference#actions-in-data-part-rules) does not contain the action you need, you can reach out to CluedIn Customer Success Team to get help with preparing custom rule action for your use case.

- **Custom action in survivorship rules written in C#** – if the [list of actions in survivorship rules](/management/rules/rules-reference#actions-in-survivorship-rules) does not contain the action you need, you can reach out to CluedIn Customer Success Team to get help with preparing custom rule action for your use case.

- **Custom action in golden record rules written in C#** – if the [list of actions in golden record rules](/management/rules/rules-reference#actions-in-golden-record-rules) does not contain the action you need, you can reach out to CluedIn Customer Success Team to get help with preparing custom rule action for your use case.

After the custom rule action is ready, it will appear in the list of actions for the specific rule type, allowing you to select it while creating a rule.

**Example of custom data part rule action**

One of the examples of custom rule actions if the **Enrich** action. It provides a flexible way to enrich data in CluedIn with external data sources. The **Enrich** action requires an API that accepts a list of vocabulary keys and returns a list of properties. The returned properties are saved with a specified vocabulary prefix. The API can be implemented as an Azure Function, a REST API, or any other service that can be accessed via HTTP. The API is also responsible for getting the data from the external source, processing it, and returning the properties to CluedIn.

The **Enrich** action takes the following parameters:

- **URL** – the URL of the enriching API.

- **Payload** – comma-separated list of vocabulary keys to send to the API.

- **Vocabulary Prefix** – the vocabulary prefix used to save properties returned by the API.

When the **Enrich** action is invoked, it sends the payload to the API (HTTP POST) and saves the returned properties with the specified vocabulary prefix. If you would like to implement the **Enrich** action, reach out to CluedIn Customer Success Team.

## Customization of enrichers

CluedIn offers a variety of [enrichers](/preparation/enricher/enricher-reference) to help you enhance your golden records with information from external sources. However, if the out-of-the-box list of enrichers is not sufficient, we can create a custom enricher in C# for your specific system. For example, an enricher that calls an internal API to enrich your data.

![customization-options-enricher.png](../../assets/images/playbooks/customization-options-enricher.png)

## Customization of export targets for a stream

CluedIn offers a variety of [export targets](/consume/export-targets/connector-reference) to cater for different export systems. Among them are OneLake, SQL Server, Azure Data Lake, and many others. If you cannot find the needed connector in the list and require a custom solution, reach out to CluedIn and our Data Engineers will help you implement a custom solution.

![customization-options-stream.png](../../assets/images/playbooks/customization-options-stream.png)

**Example of custom export target**

One of the examples of custom export targets is **Kafka**. It provides an efficient way to export golden records from CluedIn to Kafka. The Kafka connector requires the following parameters:

- **Bootstrap Servers** – Kafka server address.

- **SASL Username** – the username or the key.

- **SASL Password** – the secret or the password.

When you start the stream with the Kafka connector, CluedIn first checks if the connection can be established. Then, CluedIn checks for the streaming mode—event mode or synchronized—that is used in the particular export target configuration. Finally, every time a golden record is modified in CluedIn, the corresponding event is sent to Kafka. If you use Kafka in your operations and would like to send golden records from CluedIn to Kafka topic, reach out to CluedIn support.

## Customizations using Microsoft Fabric (or Azure Databricks)

If all of the above customization options are not sufficient for you, consider opting for customizations using Microsoft Fabric (or Azure Databricks).

![customization-options-fabric.png](../../assets/images/playbooks/customization-options-fabric.png)

You can run your own scripts using [CluedIn Python SDK](/playbooks/data-engineering-playbook/python-sdk) to perform such tasks as:

- Ingestion

- Enrichment

- Custom export

- Custom reporting

Regardless of the customization you need, get in touch with our Customer Success Team. We have implemented many customizations, so we might already have what you are looking for.