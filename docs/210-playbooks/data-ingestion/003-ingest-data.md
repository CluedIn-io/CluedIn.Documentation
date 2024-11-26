---
layout: cluedin
nav_order: 3
parent: Data ingestion playbook
grand_parent: Playbooks
permalink: /playbooks/data-ingestion-playbook/ingest-data
title: Ingest data
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

| Audience | Time to read |
|--|--|
| Data Engineer, Data Analyst | 3 min |

**You are here in the data journey**

![data-ingestion-you-are-here.png](../../assets/images/playbooks/data-ingestion-you-are-here.png)

**Before you start**

- Make sure you have conducted the [data impact workshop](/playbooks/data-ingestion-playbook/data-impact-workshop) to understand what sources you want to use first.

- Make sure you are familiar with the available tools for data ingestion and have [picked the right tool](/playbooks/data-ingestion-playbook/pick-the-right-tool) for your use case.

Now that you have prepared a list of sources and selected a tool for data ingestion, you can start the actual data ingestion process. This process consists of three steps—ingest, map, and process. In this article, we'll focus on the first step to get your data into CluedIn.

![ingest-data-intro.png](../../assets/images/playbooks/ingest-data-intro.png)

While ingesting your data, remember one of our project  principles—[start small](/playbooks/how-to-approach-your-cluedin-project). The idea is to **focus on one end-to-end data flow**, and not to load 10 million records at once as this will become a burden in the development phase of your project.

## Data ingestion instructions

In the following table, you'll find links to video trainings and documentation for each data ingestion tool. Follow the steps for your tool of choice to get your data into CluedIn.

| Tool | Link to documentation |
|--|--|
| File | [Link](/integration/file) to training video and documentation. |
| Endpoint | [Link](/integration/endpoint) to training video and documentation. |
| Database | [Link](/integration/database) to documentation. |
| Azure Data Factory | [Link](/microsoft-integration/adf-integration) to training video. |
| Microsoft Fabric/Azure Databricks | [Link](/microsoft-integration/fabric/connect-fabric-to-cluedin) to documentation. |
| Microsoft Purview | [Link](/microsoft-integration/purview) to documentation. |
| Crawler | [Link](/integration/crawling) to documentation. |

**Data ingestion limitations**

The current public [release](/release-notes) of CluedIn does not support nested data and will flatten nested objects. Depending on the structure of your nested data, the current flattening approach might be suitable. However, in some cases, you might need to process the nested object in a separate data set. We are currently working on the support of nested objects in the future.

## Structure of ingested data

When the data is ingested into CluedIn, it will be represented in the following structure.

![structure-of-ingested-data.png](../../assets/images/playbooks/structure-of-ingested-data.png)

- **Group** – this is a folder to organize your sources in a logical form.

- **Data source** – this is an object that contains the necessary information on how to connect to the source (if applicable), as well as the users and roles that have permissions to the source. Think of it like a database in SQL Server.

- **Data set** – this is the actual data obtained from the source. The data set contains unprocessed records, mapping information, quarantine capabilities, and rules applied to your raw records. Think of it like a table in a SQL Server database.

## Data ingestion results

If you followed our instructions, you should see the result similar to the following.

![ingested-data-sample-1.png](../../assets/images/playbooks/ingested-data-sample-1.png)

**Data source containing data sets**

![ingested-data-sample-2.png](../../assets/images/playbooks/ingested-data-sample-2.png)

**Data set containing raw records on the Preview tab**

The main goal of data ingestion is to have some records on the **Preview** tab.

![ingested-data-sample-3.png](../../assets/images/playbooks/ingested-data-sample-3.png)

## Next step

Ensure that the required records are available on the **Preview** tab of the data set. Once the necessary data is ingested, you can start the [mapping process](/playbooks/data-ingestion-playbook/concept-of-mapping). 