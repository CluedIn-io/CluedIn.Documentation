---
layout: cluedin
nav_order: 40
parent: Features
grand_parent: Power Apps Integration
permalink: /microsoft-integration/powerapps/features/create-batch-approval-workflow
title: Create a batch approval workflow process
tags: ["integration", "microsoft", "powerautomate", "approval", "workflow"]
last_modified: 2023-05-17
---

This feature enables you to automate the creation of the workflow for the batch approval process. If we process the data (regardless of the source) and the system identifies that the EntityType used has been tagged for the Approval Process, the data will be halted and the approval process will start and wait for the User/s approval before we continue the data processing.

**Prerequisites**

- Dataverse Connection
- Approval Connection

Please refer to this [Setup Connections](../020-setup-connections.md) link.

### Settings

- To enable this feature, you have to Navigate to **Management** > **Entity Types**, select the Entity Type you want to sync and turn on the switch for **Enable for Batch Approval Workflow** in the settings.
    
    ![Create workflow for Batch Approval](../images/batch-approval-entitytypes-page-setting.png)

### Dataverse - Approval Queue Table

- A new table will be created in Dataverse upon Enabling this feature. This table will serve as a storage of the Cluedin Data or information on the data waiting for approval.
- The **CluedIn Approval Queue ID** is the Id of the Data that we are trying to approve in this process. _(A page to show this data in CluedIn is coming soon)_.
    ![Approval Queue Table](../images/approval-queue-table.png)

### Workflow

- The content of the approval workflow will be composed of events such as condition, Approval, variables and HTTP. A 60-second cycle will occur to check if there is data in **Approval Queue** table. Once we recieve a response in the Approval Process, we send the Approval details together with the CluedIn Approval Queue IDs to the CluedIn API via HTTP event.

    ![Batch Approval Workflow](../images/batch-approval-workflow.png)

### Notifications
- Once the Automation has been done, you can expect a notification for creating the Approval Queue Table/Columns and the creation of the Batch Approval Workflow.

![Batch Approval Workflow notification](../images/batch-approval-workflow-notification.png)
