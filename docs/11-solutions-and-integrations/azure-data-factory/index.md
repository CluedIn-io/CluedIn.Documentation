---
layout: cluedin
title: Azure Data Factory
parent: Solutions & integrations
nav_order: 50
has_children: true
permalink: /solutions/azure-data-factory
content_type: landing
summary: Using Data Factory pipelines to move data into and out of CluedIn.
redirect_from: ["/microsoft-integration/adf-integration"]
source_path: docs/180-microsoft-integration/070-adf.md
---

With over 90 built-in connectors, Azure Data Factory (ADF) enables you to acquire data from a wide range of sources such as relational databases, big data and NoSQL systems, data lakes and storages, and many more. These connectors empower ADF to extract, transform, and load data from diverse systems for seamless integration and analytics.

With ADF integration, you can leverage CluedIn’s core capabilities in data quality and enrichment to ensure that the data is clean, reliable, and ready for insights.

<div class="videoFrame">
<iframe src="https://player.vimeo.com/video/1001520869?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write" title="Connect CluedIn to Azure Data Factory"></iframe>
</div>

For successful integration between ADF and CluedIn, you need to meet a couple of prerequisites:

- Your CluedIn instance must be accessible by ADF. For this, you might need to configure a private link as described [here](/solutions/azure-data-factory/private-link).

- You need to create an ingestion endpoint in CluedIn where the data from ADF will be sent. For more information, see [Endpoint](/ingest/data-sources/endpoint).

- You need to create an API token in CluedIn that will be used to authenticate your post requests.

- You need to have a source dataset in ADF ready to be sent to CluedIn.