---
title: Plan the ingestion
url: https://documentation.cluedin.net/playbooks/data-ingestion/plan-the-ingestion
content_type: concept
section: Playbooks > Data ingestion playbook
---

# Plan the ingestion

> concept: Explains how something works.

| Audience | Time to read |
|--|--|
| Data Engineer, Data Analyst | 3 min |

**You are here in the data journey**

![Diagram of the data journey: 1. Essential requirements, then 2. Data discovery workshop, then the data quality virtuous circle of data ingestion, transformation, automation, export and release to production, with You are here on Data ingestion](https://documentation.cluedin.net/assets/images/playbooks/data-ingestion-you-are-here.png)

**Before you start**

- Make sure you have conducted the [data impact workshop](https://documentation.cluedin.net/playbooks/data-ingestion/data-impact-workshop.md) to understand what sources you want to use first.

- Make sure you are familiar with the available tools for data ingestion and have [picked the right tool](https://documentation.cluedin.net/playbooks/data-ingestion/pick-the-right-tool.md) for your use case.

Now that you have prepared a list of sources and selected a tool for data ingestion, you can start the actual data ingestion process. This process consists of three steps—ingest, map, and process. In this article, we'll focus on the first step to get your data into CluedIn.

![Data ingestion steps in order: Data impact workshop, Pick the right tool, Ingest, Map, Process, with Ingest highlighted as the current step](https://documentation.cluedin.net/assets/images/playbooks/ingest-data-intro.png)

While ingesting your data, remember one of our project  principles—[start small](https://documentation.cluedin.net/playbooks/project-delivery/how-to-approach-your-cluedin-project.md). The idea is to **focus on one end-to-end data flow**, and not to load 10 million records at once as this will become a burden in the development phase of your project.

## Data ingestion instructions

In the following table, you'll find links to video trainings and documentation for each data ingestion tool. Follow the steps for your tool of choice to get your data into CluedIn.

| Tool | Link to documentation |
|--|--|
| File | [Link](https://documentation.cluedin.net/ingest/data-sources/file.md) to training video and documentation. |
| Endpoint | [Link](https://documentation.cluedin.net/ingest/data-sources/endpoint.md) to training video and documentation. |
| Database | [Link](https://documentation.cluedin.net/ingest/data-sources/database.md) to documentation. |
| Azure Data Factory | [Link](https://documentation.cluedin.net/solutions/azure-data-factory.md) to training video. |
| Microsoft Fabric/Azure Databricks | [Link](https://documentation.cluedin.net/solutions/fabric/connect-fabric-to-cluedin.md) to documentation. |
| Microsoft Purview | [Link](https://documentation.cluedin.net/solutions/purview.md) to documentation. |
| Crawler | [Link](https://documentation.cluedin.net/ingest/connectors/crawling.md) to documentation. |

**Data ingestion limitations**

The current public [release](https://documentation.cluedin.net/release-notes.md) of CluedIn does not support nested data and will flatten nested objects. Depending on the structure of your nested data, the current flattening approach might be suitable. However, in some cases, you might need to process the nested object in a separate data set. We are currently working on the support of nested objects in the future.

## Structure of ingested data

When the data is ingested into CluedIn, it will be represented in the following structure.

![Hierarchy diagram: a Group (folder for logical grouping of sources) contains a Data source (configuration and permissions), which contains a Data set (records, mapping, quarantine, pre-process rules)](https://documentation.cluedin.net/assets/images/playbooks/structure-of-ingested-data.png)

- **Group** – this is a folder to organize your sources in a logical form.

- **Data source** – this is an object that contains the necessary information on how to connect to the source (if applicable), as well as the users and roles that have permissions to the source. Think of it like a database in SQL Server.

- **Data set** – this is the actual data obtained from the source. The data set contains unprocessed records, mapping information, quarantine capabilities, and rules applied to your raw records. Think of it like a table in a SQL Server database.

## Data ingestion results

If you followed our instructions, you should see the result similar to the following.

![The Data Sources page with the Training group expanded to show the hr-contact.csv data source and its hr-contact.csv data set](https://documentation.cluedin.net/assets/images/playbooks/ingested-data-sample-1.png)

**Data source containing data sets**

![The hr-contact.csv data source on the Data Sets tab, listing one data set of 10 rows](https://documentation.cluedin.net/assets/images/playbooks/ingested-data-sample-2.png)

**Data set containing raw records on the Preview tab**

The main goal of data ingestion is to have some records on the **Preview** tab.

![The hr-contact.csv data set on the Preview tab, showing raw employee records with id, first_name, last_name, email, full_name and job_title columns](https://documentation.cluedin.net/assets/images/playbooks/ingested-data-sample-3.png)

## Next step

Ensure that the required records are available on the **Preview** tab of the data set. Once the necessary data is ingested, you can start the [mapping process](https://documentation.cluedin.net/playbooks/data-ingestion/plan-the-mapping.md).

Up: [Data ingestion playbook](https://documentation.cluedin.net/playbooks/data-ingestion.md)
