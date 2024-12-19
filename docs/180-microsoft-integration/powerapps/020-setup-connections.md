---
layout: cluedin
nav_order: 20
parent: Power Apps Integration
grand_parent: Microsoft Integration
permalink: /microsoft-integration/powerapps/setup-credentials
title: Credentials and application setup
tags: ["integration", "microsoft", "powerapps", "dataverse"]
last_modified: 2023-05-17
---

## Connections Setup

To be able to automate the workflow creation, some **Connection** need to be manually created and shared with the Application User.


### Create Connection
1. In Power Apps, on the left navigation pane, select **Connections**.

1. Select **New connection**.

1. In the list that appears, find and select Connection you want to create. In this sample, we are selecting the **Approvals**.

1. Select **Create**.

    ![Create Approval Connection Id](./images/create-approval-connection-id.png)

### Getting the Connection Id
- Open the Approvals connection that you've just created, and then copy the connection ID in the URL field.

    ![Create Approval Connection Id](./images/create-approval-connection-id2.png)

### Share Connection with Application User
- We need to grant access to the Application User too. On the top section of the page, Click the **Share** button. Find and Select the App User, grant **Can use** or **Can edit** permission and click **Save**

    ![Share Approval Connection](./images/share-approval-connection.png)

### Other Connections need to be created

1. Dataverse

    ![Dataverse Connection](./images/create-dataverse-connection-id.png)

### Organization Settings for Connection Id

1. In **Approval Connection Id**, enter the Approval connection ID. This connection ID will allow you to create the approval workflow.

    ![Approval Connection Id Setting](./images/approvals-connection-id-setting.png)

1. In **Dataverse Connection Id**, enter the Dataverse connection ID. This connection ID will allow you to access the Power Apps table in the Power Automate workflow.

    ![Dataverse Connection Id Setting](./images/dataverse-connection-id-setting.png)

