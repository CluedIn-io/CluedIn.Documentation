---
title: Sync deduplication projects to Purview
url: https://documentation.cluedin.net/solutions/purview/sync-deduplication-projects-to-purview
content_type: how-to
section: Solutions & integrations > Microsoft Purview
---

# Sync deduplication projects to Purview

> how-to: Steps to accomplish one task.

In this article, you will learn how to sync CluedIn deduplication projects to Purview assets.

## Preparation in CluedIn

1. In CluedIn, go to **Administration** > **Settings**, and then scroll down to find the **Purview** section.

1. Turn on the toggle in **Sync Deduplications to Purview**.

    ![Sync Deduplications to Purview setting turned on, with the description Create Asset and Lineage for Deduplications](https://documentation.cluedin.net/assets/images/microsoft-integration/purview/sync-dedup-projects.png)

1. Select **Save**.

1. Make sure you have an existing deduplication project.

    ![Account Deduplication Project on the Matching Rules tab, with the Account Name Rule matching on account.name](https://documentation.cluedin.net/assets/images/microsoft-integration/purview/sync-dedup-projects-existing.png)

## Feature demonstration

Once you enable synchronization of deduplication projects to Purview, you will receive a notification when the project is synced.

![CluedIn notification saying the Account Deduplication Project was synced to Purview](https://documentation.cluedin.net/assets/images/microsoft-integration/purview/sync-dedup-projects-notification.png)

**To find the asset in Purview**

1. In the [Microsoft Purview portal](https://purview.microsoft.com/), navigate to **Data Map** > **Domains**.

1. In your default domain, select the collection that stores the assets from CluedIn.

1. Select the assets card.

1. In the list of assets, find and select the asset with the same name as the deduplication project in CluedIn.

1. On the asset details page, go to **Lineage**. Here, you can view a visual representation of how deduplication projects are applied to the data set within the CluedIn processing pipeline.

    The following screenshot shows the application of a deduplication project within the CluedIn processing pipeline. The deduplication project is executed on processed entities, resulting in generating clues. The clues generated from the deduplication project are then sent back to the beginning of the processing pipeline.

    ![Purview lineage: processed entities flow into golden record, deduplication and clean branches; the highlighted deduplication step produces a Deduplication asset and generates clues](https://documentation.cluedin.net/assets/images/microsoft-integration/purview/sync-dedup-projects-lineage.png)

Up: [Microsoft Purview](https://documentation.cluedin.net/solutions/purview.md)
