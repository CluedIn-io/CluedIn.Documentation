---
layout: default
nav_order: 010
parent: Integration
permalink: /integration/define-data-to-ingest
title: Define data to ingest
tags: ["integration"]
last_modified: 2023-11-07
---

In this article, you will explore various methods available for ingesting the data into CluedIn.

You can ingest the data into CluedIn using the following methods:

- **File** – you can upload files in CSV, JSON, XLS, and XLSX formats. You can upload up to 5 files at once, and the total file size should not exceed 1 GB.

- **Ingestion point** – you can push a JSON array to an HTTP endpoint created by CluedIn.

- **Database** – you can set up a connection with your database and add the needed database tables to CluedIn.

- **Connector** (also referred to as a provider or crawler) – you can configure a software component to enable seamless interaction and data exchange between different software applications or systems and CluedIn. Currently, the ability to use connectors in CluedIn is different than using the above-mentioned options.

- **Out-of-the-box integration** – CluedIn supports out-of-the-box integration, but it is not covered in this section.

**Important!** Regardless of the data ingestion method you choose, the processing is the same across all sources.