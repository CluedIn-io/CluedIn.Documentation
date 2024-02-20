---
layout: cluedin
nav_order: 10
parent: Features
grand_parent: PowerApps Integration
permalink: /microsoft-integration/powerapps/features/sync-entitytypes
title: Sync Entity Types to Dataverse Tables
tags: ["integration", "microsoft", "powerapps", "dataverse"]
last_modified: 2023-05-17
---

This feature will allow you to Synchronize the CluedIn Entity Types, Vocabs, and Vocabulary Keys into the Dataverse table and column.
![Sync Entity Types to Dataverse Tables](../images/sync-cluedin-entitytypes-setting.png)
In the textbox above, you must specify which EntityTypes to sync. For multiple values, it should be separated by a comma _(/_Type1,/Type2,..)_ 
- All the Vocabulary keys below will be created as columns in Dataverse
![Sync Entity Types to Dataverse Tables](../images/entity-type-dog-details.png)
- Once the synchronization has been successfully executed, two success notifications will be displayed to the user. Creation of the table and Create/Update of the Columns.
![Sync Entity Types to Dataverse Tables Notification](../images/sync-cluedin-entitytypes-notification.png)
- Verifying the table and columns created in Dataverse
![Sync Entity Types to Dataverse Tables](../images/dataverse-dog-table-details.png)