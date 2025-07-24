---
layout: cluedin
nav_order: 2
parent: Data engineering playbook
grand_parent: Playbooks
permalink: playbooks/data-engineering-playbook/extending-cluedin-with-microsoft-integrations
title: Extending CluedIn with Microsoft integrations
last_modified: 2025-01-16
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article, you will find an overview of various Microsoft integrations, enabling you to leverage the ones you need to enhance your data management capabilities in CluedIn.

## Power Platform integration

[Microsoft Power Platform](https://learn.microsoft.com/en-us/power-platform/) is a suite of low-code/no-code tools designed to empower users to create custom business applications, automate workflows, analyze data, and build websites. Several of its key components—[Power Apps](https://learn.microsoft.com/en-us/power-apps/), [Power Automate](https://learn.microsoft.com/en-us/power-automate/), and [Dataverse](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/)—can be integrated with CluedIn.

The **most common use case** of Power Platform integration involves using a Power Apps form for data input and a Power Automate workflow for approving the data input. Once the input is approved, it is written to the Dataverse table. The Dataverse table is then synchronized with CluedIn and the updated data is sent to the ingestion endpoint. Once the data is in CluedIn, it undergoes processing and becomes a data part of an existing [golden record](/key-terms-and-features/golden-records), which is then sent to the Dataverse export target by stream.

![ms-integration-power-platform.png](../../assets/images/playbooks/ms-integration-power-platform.png)

The above use case is specific for data changes in the source system. In addition to this, CluedIn offers in-app [Workflow](/workflow) module for streamlining and tracking approvals and notifications for specific activities happening in CluedIn. For example, you can set up a workflow to notify the owners of a vocabulary key when other users make changes. The owners will receive an approval request in Outlook or the Approvals app in Teams, where they can approve or reject the changes. The changes will be applied only if at least one of the owners approves them.

To sum up, if you want to implement a process for approving and syncing data entry changes from Dataverse to CluedIn, consider using [Power Platform integration](/microsoft-integration/powerapps).

## Purview integration

[Microsoft Purview](https://learn.microsoft.com/en-us/purview/) is a comprehensive set of solutions that can help your organization govern, protect, and manage data, wherever it lives. If you provide Purview with a source of data (for example, a blob storage or a SQL table), it will **scan it and build the data map**. This map helps you understand what data you have, where it is located, and how it is being used. Additionally, Purview can classify the data, apply labels for sensitivity, and ensure compliance with data governance policies. Purview also captures **data lineage**, which tracks the lifecycle of data from its origin through its various transformations and movements across the data estate.

With Purview integration, CluedIn can take the assets from Purview and turn them into ready-for-insight data, which is then exported to the needed target system. What is more, you can configure synchronization between Purview glossaries and CluedIn vocabularies. Once the data is exported, Purview can scan it to automatically pick up on the mastered data coming out of CluedIn.

![ms-integration-purview.png](../../assets/images/playbooks/ms-integration-purview.png)

For more information about Purview integration, see:

- [Microsoft Purview integration](/microsoft-integration/purview)

- [Microsoft training](https://learn.microsoft.com/en-us/training/modules/building-end-to-end-data-governance-master-data-stack-with-microsoft-purview-cluedin/) on how build an end-to-end data governance and master data management stack with Microsoft Purview and CluedIn

## Copilot integration

CluedIn Copilot is an AI assistant that leverages [Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-services/openai/) to help you interact within the CluedIn platform using natural language commands. For example, you can prompt Copilot to tag golden records based on specific criteria or analyze and describe a specific dataset. While Copilot can simplify data management tasks, keep in mind that the results of Copilot actions should be carefully reviewed.

Consider enabling Copilot when you have a clear understanding of your business use case and when you know which actions can be delegated to Copilot. It is important to understand how to perform a specific task in CluedIn and then evaluate if it can be handled by Copilot.

For more information about Copilot skills in CluedIn, see Work with [Copilot integration](/microsoft-integration/copilot-integration).

## Fabric integration

[Microsoft Fabric](https://learn.microsoft.com/en-us/fabric/) is an end-to-end analytics and data platform designed for enterprises that require a unified solution. It encompasses data movement, processing, ingestion, transformation, real-time event routing, and report building. By integrating Fabric with CluedIn, you can achieve seamless data integration, enhanced data quality, and robust data management capabilities. In addition to this, CluedIn offers [OneLake connector](/consume/export-targets/onelake-connector) to export golden records to the centralized storage in OneLake.

![ms-integration-fabric.png](../../assets/images/playbooks/ms-integration-fabric.png)
 
{:.important}
If you use Fabric, Databricks, Snowflake, Synapse, or any other Python-based data platform, you can easily integrate with CluedIn using Python SDK as described in our instructions [here](/microsoft-integration/fabric).

## Event Hubs integration

[Azure Event Hubs](https://learn.microsoft.com/en-us/azure/event-hubs/) is a native data-streaming service in the cloud that can stream millions of events per second, with low latency, from any source to any destination. By integrating Azure Event Hubs and CluedIn, you can enable the transmission of important events from CluedIn to your event hub. For example, adding or updating a data source, adding a business domain, creating a deduplication project, and more. You can then connect your event hub to Fabric and **build reports or alerts for different events**. This way you can get valuable insights about the activities in CluedIn, such as the number of deduplication or clean projects that were created last week. For more information, see [Event Hub integration](/microsoft-integration/event-hub-integration).

In addition to this, CluedIn offers the [Azure Event Hub connector](/consume/export-targets/azure-event-hub-connector). You can configure it and use it in a stream to **export golden records** to a specific event hub.

## Azure Data Factory integration

[Azure Data Factory](https://learn.microsoft.com/en-us/azure/data-factory/) is Azure's cloud ETL service for data integration and data transformation. With over 90 [built-in connectors](https://learn.microsoft.com/en-us/azure/data-factory/connector-overview), Azure Data Factory enables you to acquire data from a wide range of sources such as relational databases, big data and NoSQL systems, data lakes and storages, and many more. By integrating Azure Data Factory with CluedIn, you can build automated data flows and leverage CluedIn’s core capabilities in data quality and enrichment to ensure that the data is clean, reliable, and ready for insights.

![ms-integration-adf.png](../../assets/images/playbooks/ms-integration-adf.png)

For more information, see:

- [Azure Data Factory integration](/microsoft-integration/adf-integration)

- [Configure Azure Data Factory with private link](/microsoft-integration/adf-integration/private-link)