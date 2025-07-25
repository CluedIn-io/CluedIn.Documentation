---
layout: cluedin
nav_order: 3
parent: Microsoft Purview Integration
grand_parent: Microsoft Integration
permalink: microsoft-integration/purview/sync-data-sources
title: Sync data sources
last_modified: 2025-04-30
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article, you will learn how to sync data sources between Purview and CluedIn. When this feature is enabled, CluedIn fetches all assets from Purview and creates data source groups and their respective data sources in CluedIn. Note that this feature only syncs asset metadata, not the data itself. To sync the data, use the [Azure Data Factory pipeline feature](/microsoft-integration/purview/adf-pipeline-automation). Additionally, this feature enables syncing data sources from CluedIn to Purview.

## Preparation

To sync data sources between Purview and CluedIn, complete 2 preparation steps:

1. [Prepare data sources in Purview](#preparation-in-purview) – create a glossary and a glossary term, and then associate this term with the data sources that you want to sync.

1. [Configure settings in CluedIn](#preparation-in--cluedin) – enable the sync data sources feature in Purview settings and provide the glossary term to identify the data sources for syncing. 

### Preparation in Purview

1. In the [Microsoft Purview portal](https://purview.microsoft.com), navigate to **Unified Catalog** > **Catalog management** > **Classic types**.

1. Select **New glossary**.

    ![sync-data-sources-create-glossary.png]({{ "/assets/images/microsoft-integration/purview/sync-data-sources-create-glossary.png" | relative_url }})

1. Enter the **Name** of the glossary.

1. Select the default **Domain** that contains the collections you created in [Create a new collection](/microsoft-integration/purview/pre-configuration-guide#create-a-new-collection).

    ![sync-data-sources-new-glossary.png]({{ "/assets/images/microsoft-integration/purview/sync-data-sources-new-glossary.png" | relative_url }})

1. Find and select the **Data Steward** and the **Expert** who will manage the glossary.

1. Select **Create**.

    The new glossary is created. Next, add a term to the glossary.

    ![sync-data-sources-glossary-created.png]({{ "/assets/images/microsoft-integration/purview/sync-data-sources-glossary-created.png" | relative_url }})

1. To add a term to the glossary:

    1. On the terms card, select **View terms**.

    1. Select **New term**.

    1. Select the **System default** term template and select **Continue**.

    1. Enter the **Name** of the term and select **Create**.

    The new term is added to the glossary. Next, add the term to the asset that you want to sync with CluedIn.

    ![sync-data-sources-term-created.png]({{ "/assets/images/microsoft-integration/purview/sync-data-sources-term-created.png" | relative_url }})

1. To add the term to the asset that you want to sync with CluedIn:

    1. Navigate to **Data Map** > **Domains**. In your default domain, select the collection that stores the assets from Azure Data Lake Storage.

    1. Select the assets card.

    1. Find and select the asset that you want to sync with CluedIn.

    1. On the asset details page, select **Edit**.

    1. In **Glossary terms**, find and select the term you created in step 7.

        ![sync-data-sources-add-term-to-asset.png]({{ "/assets/images/microsoft-integration/purview/sync-data-sources-add-term-to-asset.png" | relative_url }})

    1. Select **Save**.

    The term is added to the asset that you want to sync with CluedIn. On the term details page, you can find the assets associated with the term.

    ![sync-data-sources-term-with-assets-associated.png]({{ "/assets/images/microsoft-integration/purview/sync-data-sources-term-with-assets-associated.png" | relative_url }})

    Once you have prepared the data sources that you want to sync, configure the appropriate settings in CluedIn.

### Preparation in  CluedIn

1. In CluedIn, go to **Administration** > **Settings**, and then scroll down to find the **Purview** section.

1. Turn on the toggle in **Sync CluedIn Data Sources**.

1. In **Sync CluedIn Data Sources Keywords**, enter the name of the term that is associated with assets you want to sync. If you want to sync all assets, enter an asterisk (*).

    ![sync-data-sources-cluedin-settings.png]({{ "/assets/images/microsoft-integration/purview/sync-data-sources-cluedin-settings.png" | relative_url }})

1. Select **Save**.

    Once you save the changes, synchronization begins.

## Feature demonstration

This section describes the two methods of data source synchronization: from Purview to CluedIn and from CluedIn to Purview.

### Sync data sources from Purview to CluedIn

When the synchronization is completed, you will receive a notification.

![sync-data-sources-notification.png]({{ "/assets/images/microsoft-integration/purview/sync-data-sources-notification.png" | relative_url }})

After synchronization, you can view the data source groups in **Integrations** > **Data Sources**. Each Purview asset is created in CluedIn as a separate data source group.

![sync-data-sources-data-sources.png]({{ "/assets/images/microsoft-integration/purview/sync-data-sources-data-sources.png" | relative_url }})

As a result of synchronization, asset metadata is now available in CluedIn. Synchronization runs every minute, so new assets will be automatically synced with CluedIn.

### Sync data sources from CluedIn to Purview

Once you create the mapping and process the data set from the data source synced from Purview, you will receive a notification when the data set is synced back to Purview.

![sync-data-sources-data-set-synced-notification.png]({{ "/assets/images/microsoft-integration/purview/sync-data-sources-data-set-synced-notification.png" | relative_url }})

**To find the asset in Purview**

1. In the [Microsoft Purview portal](https://purview.microsoft.com/) , navigate to **Data Map** > **Domains**.
    
1. In your default domain, select the collection that stores the assets from CluedIn.
    
1. Select the assets card.
    
1. In the list of assets, find and select the asset with the same name as the data set in CluedIn.

1. On the asset details page, go to **Lineage**. Here, you can view a visual representation of how a data set moves in the CluedIn processing pipeline.

    The following screenshot shows the initial data set that has been ingested into CluedIn. The data set is then mapped to standard fields, resulting in clues. Finally, the mapped records (clues) are sent to the processing pipeline.

    ![sync-data-sources-lineage-1.png]({{ "/assets/images/microsoft-integration/purview/sync-data-sources-lineage-1.png" | relative_url }})

    The following screenshot shows the continuation of the lineage from the previous screenshot. As a result of processing, the data set produced golden records of the Account entity type.
 
    ![sync-data-sources-lineage-2.png]({{ "/assets/images/microsoft-integration/purview/sync-data-sources-lineage-2.png" | relative_url }})