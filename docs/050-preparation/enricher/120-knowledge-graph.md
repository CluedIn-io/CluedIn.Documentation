---
layout: cluedin
nav_order: 12
parent: Enricher
grand_parent: Preparation
permalink: preparation/enricher/knowledge-graph
title: Knowledge Graph
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

This article outlines how to configure the Knowledge Graph enricher. The purpose of this enricher is to provide a description of an organization. More details can be found in [Properties from Knowledge Graph enricher](#properties-from-knowledge-graph-enricher).

The Knowledge Graph enricher supports the following endpoint:

- `https://kgsearch.googleapis.com?query={nameOrUri}&key={apiKey}&limit=10&indent=true`, where `{nameOrUri}` is the name or website of the organization and `{apiKey}` is your API key for accessing Google’s Knowledge Graph database.

## Add Knowledge Graph enricher

To use the Knowledge Graph enricher, you must provide the API key. To get the API key, follow the instructions [here](https://cloud.google.com/docs/authentication/api-keys#create). The enricher uses the organization name or website to retrieve information from Google’s Knowledge Graph database.

**To add Knowledge Graph enricher**

1. On the navigation pane, go to **Preparation** > **Enrich**. Then, select **Add Enricher**.

1. On the **Choose Enricher** tab, select **Knowledge Graph**, and then select **Next**.

    ![knowledge-graph-enricher-1.png]({{ "/assets/images/preparation/enricher/knowledge-graph-enricher-1.png" | relative_url }})

1. On the **Configure** tab, provide the following details:

    - **API Key** – enter the API key for accessing Google’s Knowledge Graph database.

    - **Accepted Business Domain** – enter the business domain to define which golden records will be enriched using the Knowledge Graph enricher.

    - **Organization Name Vocabulary Key** – enter the vocabulary key that contains the names of organizations that will be used for searching the Knowledge Graph database.

    - **Website Vocabulary Key** – enter the vocabulary key that contains the websites of organizations that will be used for searching the Knowledge Graph database.

        ![knowledge-graph-enricher-2.png]({{ "/assets/images/preparation/enricher/knowledge-graph-enricher-2.png" | relative_url }})

1. Select **Test Connection** to make sure the enricher is properly configured, and then select **Add**.

    The Knowledge Graph enricher is added and has an active status. This means that it will enrich golden records based on the configuration details during processing or when you trigger external enrichment.

After the Knowledge Graph enricher is added, you can modify its details:

- **Settings** – add a user-friendly display name, select the description for data coming from the enricher, and define the source quality for determining the winning values.

- **Authentication** – modify the details you provided to configure the enricher.

## Properties from Knowledge Graph enricher

You can find the properties added to golden records from the Knowledge Graph enricher on the **Properties** page.

![knowledge-graph-enricher-4.png]({{ "/assets/images/preparation/enricher/knowledge-graph-enricher-4.png" | relative_url }})

For a more detailed information about the changes made to a golden record by the Knowledge Graph enricher, check the corresponding data part on the **History** page.

![knowledge-graph-enricher-3.png]({{ "/assets/images/preparation/enricher/knowledge-graph-enricher-5.png" | relative_url }})

The following table lists the properties that can be added to golden records by the Knowledge Graph enricher.

| Display name | Vocabulary key |
|--|--|
| Description | knowledgeGraph.organization.description |
| Description Body | knowledgeGraph.organization.detailedDescriptionBody |
| Detailed Description License | knowledgeGraph.organization.detailedDescriptionLicense |
| Detailed Description Url | knowledgeGraph.organization.detailedDescriptionUrl |
| Url | knowledgeGraph.organization.url |