---
layout: default
title: Setup credentials and permissions
parent: Microsoft Purview
grand_parent: Microsoft Azure Integrations
permalink: /integration/azure-integrations/purview/setup
nav_order: 020
has_children: false
tags: ["integration", "azure", "purview"]
---

# Setup Microsoft Purview
Purview integration is enabled via CluedIn's settings page. When the fields are left empty or blank, no synchronization is performed with Microsoft Purview.

## Credentials
1. Enter [Microsoft Purview credentials](https://docs.microsoft.com/en-us/azure/purview/create-catalog-portal#open-the-microsoft-purview-governance-portal) in CluedIn's Settings
   i. Visit CluedIn web application
   ii. Navigate to Administration > Settings
   iii. Scroll down to Organization Settings section and enter Purview credentials into the respective textboxes for the following details :
      ![Input Microsoft Purview credentials](./Media/settings.png)
      - Base URL
      - Client ID
      - Client Secret
      - Tenant ID

2. On the same Organization Settings page, navigate to "Purview: Collection Name" setting and enter the target collection path of your Purview instance. Ex. root_collection/collection1/targetcollection
     
3. Select one or more synchronization features
   ![Optional settings](./Media/settings_optional.png)
   - Synchronize Data Sources
   - Synchronize Crawlers And Enrichers
   - Synchronize Streams
   - Synchronize Purview Glossary Terms To CluedIn Vocabularies
   - Synchronize CluedIn Vocabularies to Purview Glossary Terms
   - Synchronize Purview Glossaries Terms To CluedIn Glossary Terms
   - Polling Data Sources

## Minimum Permission Requirements

The following table lists the Purview roles[^permissions] CluedIn requires per integration feature. Roles assignments can be found under the "Role assignments" tab of each collection in purview.

| Integration Feature | Role | Collection Level |
| ---- | ------ | ------- |
| Polling Data Sources | Data Curator | Target Collection[^target-collection] |
| Synchronize CluedIn Vocabularies to Purview Glossary Terms | Data Curator | Target Collection[^target-collection] |
| Synchronize Data Sources | Data Curator | Target Collection[^target-collection] |
| Synchronize Data Sources | Data Reader | Root Collection[^root-collection] |
| Synchronize Purview Glossaries Terms To CluedIn Glossary Terms | Data Reader | Root Collection[^root-collection] |
| Synchronize Purview Glossary Terms To CluedIn Vocabularies | Data Reader | Root Collection[^root-collection] |
| Synchronize Streams | Data Curator | Target Collection[^target-collection] |
| Synchronize Streams | Data Reader | Root Collection[^root-collection] |
| Synchronize Crawlers And Enrichers | Data Curator | Target Collection[^target-collection] |

# Setup Azure Data Factory
## Credentials

1. Enter [Microsoft ADF Credentials](https://learn.microsoft.com/en-us/azure/data-factory/quickstart-create-data-factory) in CluedIn's Settings
   i. Visit CluedIn web application
   ii. Navigate to Administration > Settings
   iii. Scroll down to Organization Settings section and enter ADF credentials into the respective textboxes for the following details :
      ![Input Microsoft Azure Data Factory credentials](./Media/adf_settings.png)
      - Base URL (format: https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.DataFactory/factories/{factoryName}/)
      - Client ID
      - Client Secret
      - Tenant ID

2. Enabled the Automation button.
![Input Microsoft Azure Data Factory credentials](./Media/adf_settings2.png)
- Provide Term Name pattern to filter the asset that you want to automate.

## ADF Automation Coverage
- Azure SQL Server
- Azure Data Lake gen 2
- Azure File (in progress)

[^permissions]: [Microsoft Purview Catalog Permissions](https://learn.microsoft.com/en-us/azure/purview/catalog-permissions)
[^root-collection]: "Root Collection" refers to the top most collection of your Microsoft Purview instance.
[^target-collection]: "Target Collection" refers to the "Collection Name" specified in CluedIn's organization settings.