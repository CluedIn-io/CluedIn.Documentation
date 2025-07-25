---
layout: cluedin
nav_order: 8
parent: Microsoft Purview Integration
grand_parent: Microsoft Integration
permalink: microsoft-integration/purview/sync-deduplication-projects-to-purview
title: Sync deduplication projects to Purview
last_modified: 2025-04-30
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article, you will learn how to sync CluedIn deduplication projects to Purview assets.

## Preparation in CluedIn

1. In CluedIn, go to **Administration** > **Settings**, and then scroll down to find the **Purview** section.
    
1. Turn on the toggle in **Sync Deduplications to Purview**.

    ![sync-dedup-projects.png]({{ "/assets/images/microsoft-integration/purview/sync-dedup-projects.png" | relative_url }})

1. Select **Save**.

1. Make sure you have an existing deduplication project.

    ![sync-dedup-projects-existing.png]({{ "/assets/images/microsoft-integration/purview/sync-dedup-projects-existing.png" | relative_url }})

## Feature demonstration

Once you enable synchronization of deduplication projects to Purview, you will receive a notification when the project is synced.

![sync-dedup-projects-notification.png]({{ "/assets/images/microsoft-integration/purview/sync-dedup-projects-notification.png" | relative_url }})

**To find the asset in Purview**

1. In the [Microsoft Purview portal](https://purview.microsoft.com/), navigate to **Data Map** > **Domains**.

1. In your default domain, select the collection that stores the assets from CluedIn.

1. Select the assets card.

1. In the list of assets, find and select the asset with the same name as the deduplication project in CluedIn.

1. On the asset details page, go to **Lineage**. Here, you can view a visual representation of how deduplication projects are applied to the data set within the CluedIn processing pipeline.

    The following screenshot shows the application of a deduplication project within the CluedIn processing pipeline. The deduplication project is executed on processed entities, resulting in generating clues. The clues generated from the deduplication project are then sent back to the beginning of the processing pipeline.

    ![sync-dedup-projects-lineage.png]({{ "/assets/images/microsoft-integration/purview/sync-dedup-projects-lineage.png" | relative_url }})