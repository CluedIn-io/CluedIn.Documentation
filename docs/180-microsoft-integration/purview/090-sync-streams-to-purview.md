---
layout: cluedin
nav_order: 9
parent: Microsoft Purview Integration
grand_parent: Microsoft Integration
permalink: microsoft-integration/purview/sync-streams-to-purview
title: Sync streams to Purview
last_modified: 2025-04-30
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article, you will learn how to sync CluedIn streams to Purview assets.

## Preparation in CluedIn

1. In CluedIn, go to **Administration** > **Settings**, and then scroll down to find the **Purview** section.
    
1. Turn on the toggle in **Sync CluedIn Streams**.

    ![sync-streams.png](../../assets/images/microsoft-integration/purview/sync-streams.png)

1. Select **Save**.

1. Make sure you have a configured stream in place.

## Feature demonstration

Once you enable synchronization of deduplication projects to Purview, you will receive a notification when the project is synced.

![sync-streams-notification.png](../../assets/images/microsoft-integration/purview/sync-streams-notification.png)

**To find the asset in Purview**

1. In the [Microsoft Purview portal](https://purview.microsoft.com/), navigate to **Data Map** > **Domains**.

1. In your default domain, select the collection that stores the assets from CluedIn.

1. Select the assets card.

1. In the list of assets, find and select the asset with the same name as the stream in CluedIn.

1. On the asset details page, go to **Lineage**. Here, you can view a visual representation of how streams are applied to the data set within the CluedIn processing pipeline.

    The following screenshot shows the application of a stream within the CluedIn processing pipeline. The stream is executed on processed entities.

    ![sync-streams-lineage.png](../../assets/images/microsoft-integration/purview/sync-streams-lineage.png)