---
layout: cluedin
nav_order: 6
parent: Microsoft Purview Integration
grand_parent: Microsoft Integration
permalink: microsoft-integration/purview/sync-processing-rules-to-purview
title: Sync processing rules to Purview
last_modified: 2025-04-30
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article, you will learn how to sync CluedIn rules (data part rules, survivorship rules, golden records rules) to Purview assets.

## Preparation in CluedIn

1. In CluedIn, go to **Administration** > **Settings**, and then scroll down to find the **Purview** section.
    
1. Turn on the toggle in **Sync Processing Rules to Purview**.

    ![sync-rules.png](../../assets/images/microsoft-integration/purview/sync-rules.png)

1. Select **Save**.

1. Make sure you have existing rules of any type.

## Feature demonstration

Once you enable synchronization of rules to Purview, you will receive a notification when the rule is synced.

![sync-rules-notification.png](../../assets/images/microsoft-integration/purview/sync-rules-notification.png)

**To find the asset in Purview**

1. In the [Microsoft Purview portal](https://purview.microsoft.com/), navigate to **Data Map** > **Domains**.

1. In your default domain, select the collection that stores the assets from CluedIn.

1. Select the assets card.

1. In the list of assets, find and select the asset with the same name as the data set in CluedIn.

1. On the asset details page, go to **Lineage**. Here, you can view a visual representation of how rules are applied to the data set within the CluedIn processing pipeline.

    The following screenshot shows the application of a data part rule, a survivorship rule, and a golden record rule within the CluedIn processing pipeline.

    ![sync-rules-lineage.png](../../assets/images/microsoft-integration/purview/sync-rules-lineage.png)
