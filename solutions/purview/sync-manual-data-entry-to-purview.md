---
title: Sync manual data entry to Purview
url: https://documentation.cluedin.net/solutions/purview/sync-manual-data-entry-to-purview
content_type: how-to
section: Solutions & integrations > Microsoft Purview
---

# Sync manual data entry to Purview

> how-to: Steps to accomplish one task.

In this article, you will learn how to sync CluedIn manual data entry projects to Purview assets.

## Preparation in CluedIn

1. In CluedIn, go to **Administration** > **Settings**, and then scroll down to find the **Purview** section.

1. Turn on the toggle in **Sync Manual Data Entry to Purview**.

    ![The Sync Manual Data Entry to Purview setting with its toggle set to Enabled](https://documentation.cluedin.net/assets/images/microsoft-integration/purview/sync-manual-data-entry.png)

1. Select **Save**.

1. Make sure you have an existing manual data entry project that contains some processed data.

    ![The Configuration tab of the manual data entry project Account MDE, with the Account entity type and vocabulary](https://documentation.cluedin.net/assets/images/microsoft-integration/purview/sync-manual-data-entry-existing-project.png)

## Feature demonstration

Once you enable synchronization of manual data entry projects to Purview, you will receive a notification when the project is synced.

![A CluedIn notification saying the manual data entry project Account MDE was synced to Purview](https://documentation.cluedin.net/assets/images/microsoft-integration/purview/sync-manual-data-entry-notification.png)

**To find the asset in Purview**

1. In the [Microsoft Purview portal](https://purview.microsoft.com/), navigate to **Data Map** > **Domains**.

1. In your default domain, select the collection that stores the assets from CluedIn.

1. Select the assets card.

1. In the list of assets, find and select the asset with the same name as the manual data entry project.

1. On the asset details page, go to **Lineage**. Here, you can view a visual representation of how a manual data entry project moves in the CluedIn processing pipeline.

    ![Purview lineage: the Account MDE project and an Account.csv source each flow through Generate Clue into the CluedIn Processing Pipeline, then on to processing rules](https://documentation.cluedin.net/assets/images/microsoft-integration/purview/sync-manual-data-entry-lineage.png)

Up: [Microsoft Purview](https://documentation.cluedin.net/solutions/purview.md)
