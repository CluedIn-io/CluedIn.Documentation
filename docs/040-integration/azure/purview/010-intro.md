---
layout: default
title: Introduction
parent: Microsoft Purview
grand_parent: Microsoft Azure Integrations
permalink: /integration/azure-integrations/purview/introduction
nav_order: 010
has_children: false
tags: ["integration", "azure", "purview"]
---

# Overview
CluedIn integrates with your Microsoft Purview instance to synchronize your assets, glossaries, and lineage of your data journey in CluedIn.

| Integration Feature | Description
| ---- | ------ |
| Polling Data Source | Update properties and metrics on existing "Cluedin Dataset" Purview entities
| Synchronize CluedIn Vocabularies to Purview Glossary Terms | Create Purview Glossary Terms from CluedIn Vocabularies
| Synchronize Data Sources | Create and update "Cluedin Ingest Process", "Cluedin Dataset", "Cluedin Map Process", and "Cluedin Entity" entities on Purview lineages that link Purview assets to CluedIn Data Sets and their matching CluedIn Entity Types
| Synchronize Purview Glossaries Terms To CluedIn Glossary Terms | Create CluedIn glossary terms from Purview glossary terms
| Synchronize Purview Glossary Terms To CluedIn Vocabularies | Create Purview glossary terms from CluedIn vocabulary
| Synchronize Streams | Create and update "Cluedin Entity", "Cluedin Stream Process", and "Cluedin Organization Provider" entities on Purview lineages that link CluedIn streams and connectors
| Synchronize Crawlers And Enrichers | Create and update "Cluedin Organization Provider", "Cluedin Crawl Process", "Cluedin Enrich Process", "Cluedin Ingest Process", "Cluedin Dataset", "Cluedin Map Process", and "Cluedin Entity" entities on Purview lineages that link Purview assets to CluedIn Data Sets and matching CluedIn Entity Types |

# Assumptions
Assumptions of what the customers have with their Microsoft Azure setup:
- Customers owns only one Purview resource.
- When ingesting data from ADF, the ADF pipeline should only does a one-to-one mapping from targeted file on Azure to API endpoint.

# Concepts

## Sync CluedIn Data Sources

When this feature is enabled, CluedIn fetches all Microsoft Purview asset entities from Purview to create Data Source Groups and their respective Data Sources. The Data Source Groups can be viewed under the Integrations pillar on the Data Sources page. The CluedIn purview integration components create purview assets under a single root collection.

CluedIn creates a lineage when one or more Data Sets are created within a Data Source associated with a Purview asset entity. An "Ingest Data" process displays data flow from the Microsoft Purview asset entity to a newly created or updated Microsoft Purview Data Set entity. The Microsoft Purview Data Set entity represents the CluedIn Data Set with its populated column names.

Data Sets in CluedIn with a mapping of at least one property to a CluedIn Entity Type results in both the CluedIn Entity and a "Map to Entity" process being created in Purview. The "Map to Entity" process connects the CluedIn Dataset to the CluedIn Entity Type under the assets lineage tab.

![Example of a Data Set lineage](./media/dataset_lineage.png)
Example of a Data Set lineage

Background processes in CluedIn detect changes in CluedIn Data Sets and their respective mapping. These changes synchronized with the existing Microsoft Purview Data Set assets.

## Sync Streams

A background processing CluedIn synchronizes streams and their respective export connector as assets in Purview. These assets show outbound lineage from CluedIn Entity Types to the export target.

## Monitor Events

CluedIn updates Microsoft Purview entities when specific actions are carried out by a user in CluedIn.
The supported actions are as follows:

- Adding or removing a CluedIn Data Source or Enrichers
- Adding, updating, reprocessing or removing a CluedIn Stream
- Adding, updating or removing a CluedIn Export Target

## Sync Microsoft Purview Glossaries to CluedIn Vocabularies

This synchronization feature allows the import of Microsoft Purview Glossaries as CluedIn vocabularies. If there are matching CluedIn vocabularies, they will be updated; otherwise, new CluedIn vocabularies are created for the incoming Microsoft Purview glossaries.

## Azure Data Factory pipeline Automation

This job will automatically create your ADF pipeline and execution to ingest data from Purview Asset source to CluedIn Ingestion Endpoint (CluedIn ADF Copy Data Automation).

![CluedIn ADF Copy Data Automation Dataset](./media/adf_copy.png)
