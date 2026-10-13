---
title: Purview configuration guide
url: https://documentation.cluedin.net/solutions/purview/configuration-guide
content_type: how-to
section: Solutions & integrations > Microsoft Purview
---

# Purview configuration guide

> how-to: Steps to accomplish one task.

In this guide, you will learn how to configure Purview integration in CluedIn.

> **Important:** Make sure that you have completed all of the actions described in [Purview pre-configuration guide](https://documentation.cluedin.net/solutions/purview/pre-configuration-guide.md).

## Basic Purview configuration

Basic Purview configuration is required to establish connection between your CluedIn instance and your Microsoft Purview portal.

**To configure Purview in CluedIn**

1. In CluedIn, go to **Administration** > **Azure Integration** > **Purview**.

1. In **Base URL**, enter the base URL for HTTP calls to Purview API. To find the base URL, go to your Microsoft Purview account, select **JSON View**, and then copy the value of **catalog**. The base URL value can be in one of following formats:

    - `https://xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxxx-api.purview-service.microsoft.com/` – for tenant-level Purview account.

    - `https://[purview-account-name].purview.azure.com/)` – for a separate Purview account.

    ![Resource JSON pane of a Microsoft Purview account with the catalog endpoint URL highlighted under endpoints](https://documentation.cluedin.net/assets/images/microsoft-integration/purview/purview-resorce-json.png)

1. In **Client ID**, enter a unique identifier assigned to an application when you registered it in Microsoft Entra ID. This is the application that you created during the pre-configuration stage in [Register an application and create a service principal](https://documentation.cluedin.net/solutions/purview/pre-configuration-guide.md#register-an-application-and-create-a-service-principal). You can find this value on the application overview page, in **Application (client) ID**.

1. In **Tenant ID**, enter a unique identifier for your Microsoft Entra ID tenant in which your application is registered. This is the application that you created during the pre-configuration stage in [Register an application and create a service principal](https://documentation.cluedin.net/solutions/purview/pre-configuration-guide.md#register-an-application-and-create-a-service-principal). You can find this value on the application overview page, in **Directory (tenant) ID**.

1. In **Client Secret**, enter a string value that your application uses to prove its identity when requesting a token. This is the client secret that you created during the pre-configuration stage in [Register an application and create a service principal](https://documentation.cluedin.net/solutions/purview/pre-configuration-guide.md#register-an-application-and-create-a-service-principal).

1. In **Collection Name**, enter the ID of the collection in Purview for storing golden records from CluedIn. You can find the collection ID in the URL as described in [Create a new collection](https://documentation.cluedin.net/solutions/purview/pre-configuration-guide.md#create-a-new-collection).

    ![Purview settings in CluedIn with Base Url, Client ID, Client Secret, Tenant ID and Collection name filled in](https://documentation.cluedin.net/assets/images/microsoft-integration/purview/basic-purview-configuration.png)

1. Select **Save**.

## Purview integration features configuration

Once you have completed basic Purview configuration, you can enable and configure various Purview integration features:

- [Sync data sources](https://documentation.cluedin.net/solutions/purview/sync-data-sources.md)

- [Azure Data Factory (ADF) pipeline automation](https://documentation.cluedin.net/solutions/purview/data-factory-pipeline-automation.md)

- [Sync manual data entry to Purview](https://documentation.cluedin.net/solutions/purview/sync-manual-data-entry-to-purview.md)

- [Sync processing rules to Purview](https://documentation.cluedin.net/solutions/purview/sync-processing-rules-to-purview.md)

- [Sync clean projects to Purview](https://documentation.cluedin.net/solutions/purview/sync-clean-projects-to-purview.md)

- [Sync deduplication projects to Purview](https://documentation.cluedin.net/solutions/purview/sync-deduplication-projects-to-purview.md)

- [Sync streams to Purview](https://documentation.cluedin.net/solutions/purview/sync-streams-to-purview.md)

- [Sync Purview glossaries to CluedIn glossaries](https://documentation.cluedin.net/solutions/purview/sync-purview-glossaries-to-cluedin-glossaries.md)

- [Sync Purview glossaries to CluedIn vocabularies](https://documentation.cluedin.net/solutions/purview/sync-purview-glossaries-to-cluedin-vocabularies.md)

- [Sync data products](https://documentation.cluedin.net/solutions/purview/sync-data-products.md)

Up: [Microsoft Purview](https://documentation.cluedin.net/solutions/purview.md)
