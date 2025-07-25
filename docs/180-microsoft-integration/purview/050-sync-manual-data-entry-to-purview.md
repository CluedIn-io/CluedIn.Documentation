---
layout: cluedin
nav_order: 5
parent: Microsoft Purview Integration
grand_parent: Microsoft Integration
permalink: /microsoft-integration/purview/sync-manual-data-entry-to-purview
title: Sync manual data entry to Purview
last_modified: 2025-04-30
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article, you will learn how to sync CluedIn manual data entry projects to Purview assets.

## Preparation in CluedIn

1. In CluedIn, go to **Administration** > **Settings**, and then scroll down to find the **Purview** section.
    
1. Turn on the toggle in **Sync Manual Data Entry to Purview**.

    ![sync-manual-data-entry.png]({{ "/assets/images/microsoft-integration/purview/sync-manual-data-entry.png" | relative_url }})

1. Select **Save**.

1. Make sure you have an existing manual data entry project that contains some processed data.

    ![sync-manual-data-entry-existing-project.png]({{ "/assets/images/microsoft-integration/purview/sync-manual-data-entry-existing-project.png" | relative_url }})

## Feature demonstration

Once you enable synchronization of manual data entry projects to Purview, you will receive a notification when the project is synced.

![sync-manual-data-entry-notification.png]({{ "/assets/images/microsoft-integration/purview/sync-manual-data-entry-notification.png" | relative_url }})

**To find the asset in Purview**

1. In the [Microsoft Purview portal](https://purview.microsoft.com/), navigate to **Data Map** > **Domains**.

1. In your default domain, select the collection that stores the assets from CluedIn.

1. Select the assets card.

1. In the list of assets, find and select the asset with the same name as the manual data entry project.

1. On the asset details page, go to **Lineage**. Here, you can view a visual representation of how a manual data entry project moves in the CluedIn processing pipeline.

    ![sync-manual-data-entry-lineage.png]({{ "/assets/images/microsoft-integration/purview/sync-manual-data-entry-lineage.png" | relative_url }})