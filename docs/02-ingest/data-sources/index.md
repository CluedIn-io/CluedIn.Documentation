---
layout: cluedin
title: Data sources
parent: Ingest
nav_order: 20
has_children: true
permalink: /ingest/data-sources
content_type: landing
summary: A data source is where records come from.
list_children: false
redirect_from: ["/integration/data sources"]
source_path: docs/040-integration/190-data-sources.md
tags: ["integration", "data sources"]
last_modified: 2023-11-07
---

In this section, you will learn how to get your data from external sources into CluedIn.

All data you ingest into CluedIn is stored in **Integrations** > **Data Sources**. One of the main purposes of the **Data Sources** module is to provide you with the tools to create a semantic layer for your data so that CluedIn can understand it.

![integrations-1.gif]({{ "/assets/images/integration/integrations-1.gif" | relative_url }})

Each step is explained in detail in a separate article in this section:

1. [Define data to ingest](/ingest/data-sources/define-data-to-ingest) – explore all the ways you can ingest data into CluedIn and choose the one that works best for your needs.

1. Ingest data from [a file](/ingest/data-sources/file), [an endpoint](/ingest/data-sources/endpoint), or [a database](/ingest/data-sources/database) - find step-by-step instructions for ingesting data into CluedIn.

1. [Create mapping](/ingest/mapping/create-mapping) - create a semantic layer for your data and [review the mapping details](/ingest/mapping/review-mapping) to ensure that your records are produced and merged in the most effective way.

1. [Process data](/ingest/processing/process-data) - turn your data into golden records, making it searchable and ready to be cleaned, deduplicated, and streamed.

In addition to these fundamental steps, we encourage you to explore [additional operations on records](/ingest) to discover tools for normalizing and improving the quality of data.

To ingest, map, and process the data, you need to have access to different modules in CluedIn. The following table contains a list of claims required to work with the **Data Sources** module.

| Section | Claim | Access level |
|--|--|--|
| Integration | All claims | at least Consulted |
| Management | Data Catalog | at least Informed |
| Management | Annotation | at least Informed |
| Consume | Export Targets | at least Informed |