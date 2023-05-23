---
layout: default
nav_order: 20
parent: Features
grand_parent: PowerApps Integration
permalink: /microsoft-integration/powerapps/features/sync-dataverse
title: Sync Dataverse Table to Cluedin Entity Types/Vocabularies
tags: ["integration", "microsoft", "powerapps", "dataverse"]
last_modified: 2023-05-17
---

This feature will allow you to Synchronize the Dataverse Table and columns into CluedIn Entity Type, Vocabulary, and Vocabulary Keys
![Sync Dataverse Table to Cluedin Entity Types/Vocabularies](../images/sync-dataverse-table-setting.png)
In the textbox above, you need to specify and provide which Dataverse table to sync. The value should be the **logical name** of the table. For multiple values, it should be separated by a comma _(logical_name1_,logical_name2,..)_
- There are ways to identify or get the logical name of the table
  1. Go to table Properties => look for the logical name value
  2. Tools => Copy the logical name
  3. In the Table List view, the logical name is right after the table name
![Identifying Logical Name](../images/dataverse-logical-name.png)
- Once the synchronization has been successfully executed, three success notifications will be displayed to the user. Creation of the Entity Type, Creation of Vocabulary, and Creation of Vocabulary Keys.
![Sync Dataverse Table Notification](../images/sync-dataverse-table-notification.png)
- Verifying Entity Type, Vocabulary, and Vocabulary Keys created.
![Create New EntityType and Vocab](../images/created-new-entitytype-and-vocab.png)