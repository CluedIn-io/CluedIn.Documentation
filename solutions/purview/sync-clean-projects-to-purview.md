---
title: Sync clean projects to Purview
url: https://documentation.cluedin.net/solutions/purview/sync-clean-projects-to-purview
content_type: how-to
section: Solutions & integrations > Microsoft Purview
---

# Sync clean projects to Purview

> how-to: Steps to accomplish one task.

In this article, you will learn how to sync CluedIn clean projects to Purview assets.

## Preparation in CluedIn

1. In CluedIn, go to **Administration** > **Settings**, and then scroll down to find the **Purview** section.

1. Turn on the toggle in **Sync Clean Projects to Purview**.

    ![The Sync Clean Projects to Purview setting with its toggle set to Enabled](https://documentation.cluedin.net/assets/images/microsoft-integration/purview/sync-clean-projects.png)

1. Select **Save**.

1. Make sure you have an existing clean project.

    ![An existing clean project named Account Clean Project in CluedIn, with status Ready for clean](https://documentation.cluedin.net/assets/images/microsoft-integration/purview/sync-clean-projects-existing.png)

## Feature demonstration

Once you enable synchronization of rules to Purview, you will receive a notification when the rule is synced.

![A CluedIn notification: Clean Project Account Clean Project synced to Purview](https://documentation.cluedin.net/assets/images/microsoft-integration/purview/sync-clean-projects-notification.png)

**To find the asset in Purview**

1. In the [Microsoft Purview portal](https://purview.microsoft.com/), navigate to **Data Map** > **Domains**.

1. In your default domain, select the collection that stores the assets from CluedIn.

1. Select the assets card.

1. In the list of assets, find and select the asset with the same name as the clean project in CluedIn.

1. On the asset details page, go to **Lineage**. Here, you can view a visual representation of how clean projects are applied to the data set within the CluedIn processing pipeline.

    The following screenshot shows the application of a clean project within the CluedIn processing pipeline. The clean project is executed on processed entities, resulting in generating clues. The clues generated from the clean project are then sent back to the beginning of the processing pipeline.

    ![Purview lineage: Process Entities produces Processed Entities, which feed Golden Record (Account) and Clean; Clean produces Clean Projects, then Generate Clue loops back to the start of the pipeline](https://documentation.cluedin.net/assets/images/microsoft-integration/purview/sync-clean-projects-lineage-1.png)

Up: [Microsoft Purview](https://documentation.cluedin.net/solutions/purview.md)
