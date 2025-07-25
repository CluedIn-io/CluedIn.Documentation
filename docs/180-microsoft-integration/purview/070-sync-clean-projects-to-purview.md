---
layout: cluedin
nav_order: 7
parent: Microsoft Purview Integration
grand_parent: Microsoft Integration
permalink: microsoft-integration/purview/sync-clean-projects-to-purview
title: Sync clean projects to Purview
last_modified: 2025-04-30
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article, you will learn how to sync CluedIn clean projects to Purview assets.

## Preparation in CluedIn

1. In CluedIn, go to **Administration** > **Settings**, and then scroll down to find the **Purview** section.
    
1. Turn on the toggle in **Sync Clean Projects to Purview**.

    ![sync-clean-projects.png]({{ "/assets/images/microsoft-integration/purview/sync-clean-projects.png" | relative_url }})

1. Select **Save**.

1. Make sure you have an existing clean project.

    ![sync-clean-projects-existing.png]({{ "/assets/images/microsoft-integration/purview/sync-clean-projects-existing.png" | relative_url }})

## Feature demonstration

Once you enable synchronization of rules to Purview, you will receive a notification when the rule is synced.

![sync-clean-projects-notification.png]({{ "/assets/images/microsoft-integration/purview/sync-clean-projects-notification.png" | relative_url }})

**To find the asset in Purview**

1. In the [Microsoft Purview portal](https://purview.microsoft.com/), navigate to **Data Map** > **Domains**.

1. In your default domain, select the collection that stores the assets from CluedIn.

1. Select the assets card.

1. In the list of assets, find and select the asset with the same name as the clean project in CluedIn.

1. On the asset details page, go to **Lineage**. Here, you can view a visual representation of how clean projects are applied to the data set within the CluedIn processing pipeline.

    The following screenshot shows the application of a clean project within the CluedIn processing pipeline. The clean project is executed on processed entities, resulting in generating clues. The clues generated from the clean project are then sent back to the beginning of the processing pipeline.

    ![sync-clean-projects-lineage-1.png]({{ "/assets/images/microsoft-integration/purview/sync-clean-projects-lineage-1.png" | relative_url }})