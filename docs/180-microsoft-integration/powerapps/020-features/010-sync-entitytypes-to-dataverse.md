---
layout: cluedin
nav_order: 10
parent: Features
grand_parent: PowerApps Integration
permalink: /microsoft-integration/powerapps/features/sync-entitytypes
title: Sync entity types to Dataverse tables
tags: ["integration", "microsoft", "powerapps", "dataverse"]
last_modified: 2023-05-17
---

This feature allows you to sync CluedIn entity types, vocabularies, and vocabulary keys with Dataverse table and columns.

**To sync CluedIn entity types with Dataverse table**

1. On the navigation pane, go to **Administration** > **Settings**, and then find the **PowerApps** section.

1. In **Sync CluedIn Entity Types to Dataverse Table**, turn on the toggle, and then enter the entity type that you want to sync. If you want to sync multiple entity types, separate them with a comma (for example, _/_Type1,/Type2,/Type3_).

    ![Sync Entity Types to Dataverse Tables](../images/sync-cluedin-entitytypes-setting.png)

    All the vocabulary keys below will be created as columns in the Dataverse table.

    ![Sync Entity Types to Dataverse Tables](../images/entity-type-dog-details.png)

    Once the synchronization has been successfully completed, you'll receive two notifications: **Dataverse Table Created** and **Dataverse Column Created/Updated**.

    ![Sync Entity Types to Dataverse Tables Notification](../images/sync-cluedin-entitytypes-notification.png)

1. Verify the table and columns created in Dataverse.

    ![Sync Entity Types to Dataverse Tables](../images/dataverse-dog-table-details.png)