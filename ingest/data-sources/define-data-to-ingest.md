---
title: Define data to ingest
url: https://documentation.cluedin.net/ingest/data-sources/define-data-to-ingest
content_type: concept
section: Ingest > Data sources
---

# Define data to ingest

> concept: Explains how something works.

In this article, you will explore various methods available for ingesting the data into CluedIn.

You can ingest the data into CluedIn using the following methods:

- **File** – you can upload files in CSV, JSON, XLS, XLSX, and Parquet formats. You can upload up to 5 files at once, and the total file size should not exceed 1 GB.

- **Ingestion endpoint** – you can push a JSON array to an HTTP endpoint created by CluedIn.

- **Database** – you can set up a connection with your database and add the needed database tables to CluedIn.

- **Connector** (also referred to as a provider or crawler) – you can configure a software component to enable seamless interaction and data exchange between different software applications or systems and CluedIn. Currently, the ability to use connectors in CluedIn is different than using the above-mentioned options.

- **Out-of-the-box integration** – CluedIn supports out-of-the-box integration, but it is not covered in this section.

> **Important:** Regardless of the data ingestion method you choose, the [processing](https://documentation.cluedin.net/ingest/processing/process-data.md) of data is the same across all sources.

Up: [Data sources](https://documentation.cluedin.net/ingest/data-sources.md)
