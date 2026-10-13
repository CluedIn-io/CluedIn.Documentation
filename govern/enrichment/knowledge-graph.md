---
title: Knowledge Graph
url: https://documentation.cluedin.net/govern/enrichment/knowledge-graph
content_type: reference
section: Govern & improve > Enrichment
---

# Knowledge Graph

> reference: Facts, options, APIs.

This article outlines how to configure the Knowledge Graph enricher. The purpose of this enricher is to provide a description of an organization. More details can be found in [Properties from Knowledge Graph enricher](#properties-from-knowledge-graph-enricher).

The Knowledge Graph enricher supports the following endpoint:

- `https://kgsearch.googleapis.com?query={nameOrUri}&key={apiKey}&limit=10&indent=true`, where `{nameOrUri}` is the name or website of the organization and `{apiKey}` is your API key for accessing Google’s Knowledge Graph database.

## Add Knowledge Graph enricher

To use the Knowledge Graph enricher, you must provide the API key. To get the API key, follow the instructions [here](https://cloud.google.com/docs/authentication/api-keys#create). The enricher uses the organization name or website to retrieve information from Google’s Knowledge Graph database.

**To add Knowledge Graph enricher**

1. On the navigation pane, go to **Preparation** > **Enrich**. Then, select **Add Enricher**.

1. On the **Choose Enricher** tab, select **Knowledge Graph**, and then select **Next**.

    ![Choose enricher tab of the Add Enricher pane with Knowledge Graph selected](https://documentation.cluedin.net/assets/images/preparation/enricher/knowledge-graph-enricher-1.png)

1. On the **Configure** tab, provide the following details:

    - **API Key** – enter the API key for accessing Google’s Knowledge Graph database.

    - **Accepted Business Domain** – enter the business domain to define which golden records will be enriched using the Knowledge Graph enricher.

    - **Organization Name Vocabulary Key** – enter the vocabulary key that contains the names of organizations that will be used for searching the Knowledge Graph database.

    - **Website Vocabulary Key** – enter the vocabulary key that contains the websites of organizations that will be used for searching the Knowledge Graph database.

        ![Configure tab with API Key, Accepted Business Domain set to Organization, and the organization name and website vocabulary keys filled in](https://documentation.cluedin.net/assets/images/preparation/enricher/knowledge-graph-enricher-2.png)

1. Select **Test Connection** to make sure the enricher is properly configured, and then select **Add**.

    The Knowledge Graph enricher is added and has an active status. This means that it will enrich golden records based on the configuration details during processing or when you trigger external enrichment.

After the Knowledge Graph enricher is added, you can modify its details:

- **Settings** – add a user-friendly display name, select the description for data coming from the enricher, and define the source quality for determining the winning values.

- **Authentication** – modify the details you provided to configure the enricher.

## Properties from Knowledge Graph enricher

You can find the properties added to golden records from the Knowledge Graph enricher on the **Properties** page.

![Properties page of a golden record listing properties whose Source is Knowledge Graph, such as description and URL](https://documentation.cluedin.net/assets/images/preparation/enricher/knowledge-graph-enricher-4.png)

For a more detailed information about the changes made to a golden record by the Knowledge Graph enricher, check the corresponding data part on the **History** page.

![History page of a golden record with the Knowledge Graph data part highlighted above the file data source record](https://documentation.cluedin.net/assets/images/preparation/enricher/knowledge-graph-enricher-5.png)

The following table lists the properties that can be added to golden records by the Knowledge Graph enricher.

| Display name | Vocabulary key |
|--|--|
| Description | knowledgeGraph.organization.description |
| Description Body | knowledgeGraph.organization.detailedDescriptionBody |
| Detailed Description License | knowledgeGraph.organization.detailedDescriptionLicense |
| Detailed Description Url | knowledgeGraph.organization.detailedDescriptionUrl |
| Url | knowledgeGraph.organization.url |

Up: [Enrichment](https://documentation.cluedin.net/govern/enrichment.md)
