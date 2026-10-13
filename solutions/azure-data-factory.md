---
title: Azure Data Factory
url: https://documentation.cluedin.net/solutions/azure-data-factory
content_type: landing
section: Solutions & integrations
---

# Azure Data Factory

With over 90 built-in connectors, Azure Data Factory (ADF) enables you to acquire data from a wide range of sources such as relational databases, big data and NoSQL systems, data lakes and storages, and many more. These connectors empower ADF to extract, transform, and load data from diverse systems for seamless integration and analytics.

With ADF integration, you can leverage CluedIn’s core capabilities in data quality and enrichment to ensure that the data is clean, reliable, and ready for insights.

For successful integration between ADF and CluedIn, you need to meet a couple of prerequisites:

- Your CluedIn instance must be accessible by ADF. For this, you might need to configure a private link as described [here](https://documentation.cluedin.net/solutions/azure-data-factory/private-link.md).

- You need to create an ingestion endpoint in CluedIn where the data from ADF will be sent. For more information, see [Endpoint](https://documentation.cluedin.net/ingest/data-sources/endpoint.md).

- You need to create an API token in CluedIn that will be used to authenticate your post requests.

- You need to have a source dataset in ADF ready to be sent to CluedIn.

## In this section

- [Configure ADF with private link](https://documentation.cluedin.net/solutions/azure-data-factory/private-link.md) (how-to): In this article, you will learn how to configure a private link service between Azure Data Factory (ADF) and CluedIn.
- [Configure ADF pipeline with Copy data activity](https://documentation.cluedin.net/solutions/azure-data-factory/copy-data.md) (how-to): This guide provides step-by-step instructions for configuring an Azure Data Factory (ADF) Copy data activity to send data to CluedIn using a private endpoint.
- [Configure ADF pipeline with Data flow activity](https://documentation.cluedin.net/solutions/azure-data-factory/data-flow-activity.md) (how-to): This guide provides step-by-step instructions for configuring an Azure Data Factory (ADF) Data flow activity to send data to CluedIn.

Up: [Solutions & integrations](https://documentation.cluedin.net/solutions.md)
