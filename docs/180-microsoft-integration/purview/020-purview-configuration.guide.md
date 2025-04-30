---
layout: cluedin
nav_order: 20
parent: Microsoft Purview Integration
grand_parent: Microsoft Integration
permalink: /microsoft-integration/purview/configuration-guide
title: Purview configuration guide
last_modified: 2025-04-30
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this guide, you will learn how to configure Purview integration in CluedIn.

{:.important}
Make sure that you have completed all of the actions described in [Purview pre-configuration guide](/microsoft-integration/purview/pre-configuration-guide).

## Basic Purview configuration

Basic Purview configuration is required to establish connection between your CluedIn instance and your Microsoft Purview portal.

**To configure Purview in CluedIn**

1. In CluedIn, go to **Administration** > **Settings**, and then scroll down to find the **Purview** section.

1. In **Base URL**, enter the base URL for HTTP calls to Purview API. To find the base URL, go to your Microsoft Purview account, select **JSON View**, and then copy the value of **catalog**. The base URL value can be in one of following formats:

    - `https://xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxxx-api.purview-service.microsoft.com/` – for tenant-level Purview account.

    - `https://[purview-account-name].purview.azure.com/)` – for a separate Purview account.

    ![purview-resorce-json.png](../../assets/images/microsoft-integration/purview/purview-resorce-json.png)

1. In **Client ID**, enter a unique identifier assigned to an application when you registered it in Microsoft Entra ID. This is the application that you created during the pre-configuration stage in [Register an application and create a service principal](/microsoft-integration/purview/pre-configuration-guide#register-an-application-and-create-a-service-principal). You can find this value on the application overview page, in **Application (client) ID**.

1. In **Tenant ID**, enter a unique identifier for your Microsoft Entra ID tenant in which your application is registered. This is the application that you created during the pre-configuration stage in [Register an application and create a service principal](/microsoft-integration/purview/pre-configuration-guide#register-an-application-and-create-a-service-principal). You can find this value on the application overview page, in **Directory (tenant) ID**.

1. In **Client Secret**, enter a string value that your application uses to prove its identity when requesting a token. This is the client secret that you created during the pre-configuration stage in [Register an application and create a service principal](/microsoft-integration/purview/pre-configuration-guide#register-an-application-and-create-a-service-principal).

1. In **Collection Name**, enter the ID of the collection in Purview for storing golden records from CluedIn. You can find the collection ID in the URL as described in [Create a new collection](/microsoft-integration/purview/pre-configuration-guide#create-a-new-collection).

    ![basic-purview-configuration.png](../../assets/images/microsoft-integration/purview/basic-purview-configuration.png)

1. Select **Save**.

## Purview integration features configuration

Once you have completed basic Purview configuration, you can enable and configure various Purview integration features:

- [Sync data sources - Overview](https://dev.azure.com/CluedIn-io/CluedIn/_wiki/wikis/CluedIn.wiki/2434/Sync-data-sources)

- [Azure Data Factory pipeline automation - Overview](https://dev.azure.com/CluedIn-io/CluedIn/_wiki/wikis/CluedIn.wiki/2454/Azure-Data-Factory-pipeline-automation)

- [Sync manual data entry to Purview - Overview](https://dev.azure.com/CluedIn-io/CluedIn/_wiki/wikis/CluedIn.wiki/4044/Sync-manual-data-entry-to-Purview)

- [Sync processing rules to Purview - Overview](https://dev.azure.com/CluedIn-io/CluedIn/_wiki/wikis/CluedIn.wiki/4045/Sync-processing-rules-to-Purview)

- [Sync clean projects to Purview - Overview](https://dev.azure.com/CluedIn-io/CluedIn/_wiki/wikis/CluedIn.wiki/4047/Sync-clean-projects-to-Purview)

- [Sync deduplication projects to Purview - Overview](https://dev.azure.com/CluedIn-io/CluedIn/_wiki/wikis/CluedIn.wiki/4051/Sync-deduplication-projects-to-Purview)

- [Sync streams to Purview - Overview](https://dev.azure.com/CluedIn-io/CluedIn/_wiki/wikis/CluedIn.wiki/4053/Sync-streams-to-Purview)

- [Sync Purview glossaries to CluedIn glossaries - Overview](https://dev.azure.com/CluedIn-io/CluedIn/_wiki/wikis/CluedIn.wiki/2451/Sync-Purview-glossaries-to-CluedIn-glossaries)

- [Sync Purview glossaries to CluedIn vocabularies - Overview](https://dev.azure.com/CluedIn-io/CluedIn/_wiki/wikis/CluedIn.wiki/2444/Sync-Purview-glossaries-to-CluedIn-vocabularies)

- [Sync data products - Overview](https://dev.azure.com/CluedIn-io/CluedIn/_wiki/wikis/CluedIn.wiki/2453/Sync-data-products)