---
layout: cluedin
nav_order: 30
parent: Power Apps Integration
grand_parent: Microsoft Integration
permalink: /microsoft-integration/powerapps/features
title: Features
tags: ["integration", "microsoft", "powerapps", "dataverse"]
last_modified: 2023-05-17
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

## Sync business domains to Dataverse tables

This feature allows you to sync CluedIn business domains, vocabularies, and vocabulary keys with Dataverse table and columns.

**To sync CluedIn business domains with Dataverse table**

1. On the navigation pane, go to **Administration** > **Settings**, and then find the **PowerApps** section.

1. In **Sync CluedIn Business Domains to Dataverse Table**, turn on the toggle, and then enter the business domain that you want to sync. If you want to sync multiple business domains, separate them with a comma (for example, _/_Type1,/Type2,/Type3_).

    ![Sync Entity Types to Dataverse Tables](../../../assets/images/microsoft-integration/power-apps-backup/sync-cluedin-entitytypes-setting.png)

    Another way to enable this feature is to navigate to **Management** > **Business Domains** and select the business domain you want to sync. Then, select **Edit** and turn on the toggle for **Sync CluedIn Business Domains to Dataverse Table**. Finally, save changes.

    ![Sync Entity Types to Dataverse Tables](../../../assets/images/microsoft-integration/power-apps-backup/sync-cluedin-entitytypes-page-setting.png)

    All the vocabulary keys below will be created as columns in the Dataverse table.

    ![Sync Entity Types to Dataverse Tables](../../../assets/images/microsoft-integration/power-apps-backup/entity-type-dog-details.png)

    Once the synchronization has been completed, you'll receive two notifications: **Dataverse Table Created** and **Dataverse Column Created/Updated**.

    ![Sync Entity Types to Dataverse Tables Notification](../../../assets/images/microsoft-integration/power-apps-backup/sync-cluedin-entitytypes-notification.png)

1. Verify the table and columns created in Dataverse.

    ![Sync Entity Types to Dataverse Tables](../../../assets/images/microsoft-integration/power-apps-backup/dataverse-dog-table-details.png)

## Sync Dataverse table to Cluedin business domains/vocabularies

This feature allows you to sync Dataverse table and columns into CluedIn business domains, vocabulary, and vocabulary keys.

**Prerequisites**

You'll need to provide the logical name of the Dataverse table. There are the following ways to identify or get the logical name of the table:

1. Go to table **Properties**, and then copy the value from the **Logical name** field.

1. Go to **Tools**, and then select **Copy logical name**.

1. In the table list view, the logical name is right after the table name.

    ![Identifying Logical Name](../../../assets/images/microsoft-integration/power-apps-backup/dataverse-logical-name.png)

**To sync Dataverse table and columns into CluedIn business domains and vocabulary**

1. On the navigation pane, go to **Administration** > **Settings**, and then find the **PowerApps** section.

1. In **Sync Dataverse Table/Columns to CluedIn Business Domains and Vocabulary**, turn on the toggle, and then enter the Dataverse table name. The value should be the **logical name** of the table. If you want to sync multiple tables, separate them with a comma (for example, _logical_name1_,logical_name2,logical_name3_).

    ![sync-dataverse-table.png](../../../assets/images/microsoft-integration/power-apps/sync-dataverse-table.png)

    Once the synchronization has been successfully completed, you'll receive three notifications: **Entity Type Created**, **Vocabulary Created**, and **Vocabulary Keys Created**.
    
    ![Sync Dataverse Table Notification](../../../assets/images/microsoft-integration/power-apps-backup/sync-dataverse-table-notification.png)

1. Verify the business domain, vocabulary, and vocabulary keys created in CluedIn.

    ![Create New EntityType and Vocab](../../../assets/images/microsoft-integration/power-apps-backup/created-new-entitytype-and-vocab.png)

## Create ingestion endpoint workflow

This feature allows you to automate the creation of workflow that will send the data from Dataverse to CluedIn via ingestion endpoint.

**Prerequisites**

- Dataverse connection.

**To automate the workflow creation**

1. In CluedIn, on the navigation pane, go to **Administration** > **Settings**, and then find the **PowerApps** section.

1. In **Create workflow to Ingest Data to CluedIn**, turn on the toggle.

    ![Create workflow to Ingest Data to CluedIn](../../../assets/images/microsoft-integration/power-apps-backup/create-workflow-to-ingest-data-setting-3.png)

**Ingestion endpoint**

As part of workflow automation, the ingestion endpoint will be created as well. From our sample above, you can expect two ingestion endpoints to be created, one for each of the **cluedin_dog** and **crc12_customer** tables.
    
![Power Automate Workflow Ingestion Endpoint](../../../assets/images/microsoft-integration/power-apps-backup/power-automate-workflow-ingestion-endpoint.png)

**Workflow**

The creation of workflow will depend on the values of **Sync Business Domains** and **Sync Dataverse Tables**. Once the execution of the job is done, from the sample values above, you can expect two workflows to be created, one for each of the **cluedin_dog** and **crc12_customer** tables.

![Power Automate Workflows](../../../assets/images/microsoft-integration/power-apps-backup/power-automate-workflows.png)

You can expect to see a notification when the creation is successful.

![Power Automate Workflow Notification](../../../assets/images/microsoft-integration/power-apps-backup/power-automate-workflow-notification.png)

The content of the workflow will be composed of a Dataverse event named _When a row is added, modified or delete_ (but mainly focused on _Added and Modified_) and an HTTP event that pushes the data into CluedIn ingestion endpoint. On the following screenshot, the token has been edited to show the full content of HTTP event.

![Power Automate Workflow Content](../../../assets/images/microsoft-integration/power-apps-backup/power-automate-workflow-content.png)

**Auto mapping and processing**
    
As we already know the structure of the table/vocabulary that we are working on, the system will automate the data mapping and processing. By navigating to the data set page, you can notice that the **Map**, **Prepare**, and **Process** tabs are now available as we already automated the creation of the data mapping into our vocabularies.

![Auto Mapping](../../../assets/images/microsoft-integration/power-apps-backup/ingestion-endpoint-automapping-01.png)

On the **Map** tab, you can find the the full view of all columns mapped to our vocabulary, including edges (relationships) and identifiers, if there are any.

![Auto Mapping](../../../assets/images/microsoft-integration/power-apps-backup/ingestion-endpoint-automapping-02.png)

On the **Preview** tab, you can find the data received from Dataverse.

![Ingestion Endpoint Preview](../../../assets/images/microsoft-integration/power-apps-backup/ingestion-endpoint-preview.png)

Once the data is received, you can expect to see it processed because we have also enabled the **Auto submission** property of the ingestion endpoint.

![Auto Processing](../../../assets/images/microsoft-integration/power-apps-backup/ingestion-endpoint-auto-submission.png)

## Create a batch approval workflow process

This feature enables you to automate the creation of the workflow for the batch approval process. If you process the data (regardless of the source) and the system identifies that the business domain used has been tagged for the approval process, the data will be halted, and the approval process will start and wait for the user's approval to continue the data processing.

**Prerequisites**

- Dataverse connection
- Approval connection

**To enable the batch approval workflow**

1. In CluedIn, on the navigation pane, go to **Management** > **Business Domains**, and then select the business domain that you want to sync.

1. Select **Edit** and then turn on the toggle for **Enable for Batch Approval Workflow**.

1. Select **Save**.
    
    ![Create workflow for Batch Approval](../../../assets/images/microsoft-integration/power-apps-backup/batch-approval-entitytypes-page-setting.png)

    After enabling this feature, a new table (Approval Queue Table) will be created in Dataverse.

**Approval Queue table in Dataverse**

This table will serve as a storage of the CluedIn data or information on the data waiting for approval.

The **CluedIn Approval Queue ID** is the ID of the data that we are trying to approve in this process.

![Approval Queue Table](../../../assets/images/microsoft-integration/power-apps-backup/approval-queue-table.png)

**Workflow**

The content of the approval workflow will be composed of events such as condition, approval, variables, and HTTP. A 60-second cycle will occur to check if there is data in the **Approval Queue** table. Once we receive a response in the Approval Process, we send the Approval details together with the CluedIn Approval Queue IDs to the CluedIn API via an HTTP event.

![Batch Approval Workflow](../../../assets/images/microsoft-integration/power-apps-backup/batch-approval-workflow.png)

**Notifications**

Once the automation has been done, you can expect a notification for creating the Approval Queue Table/Columns and the creation of the Batch Approval Workflow.

![Batch Approval Workflow notification](../../../assets/images/microsoft-integration/power-apps-backup/batch-approval-workflow-notification-3.png)

## Create streams

This feature allows you to automate the creation of export targets and streams.

**To automate the creation of export targets and streams**

1. On the navigation pane, go to **Administration** > **Settings**, and then find the **PowerApps** section.

1. In **Create CluedIn Stream**, turn on the toggle.

    ![Create CluedIn Streams](../../../assets/images/microsoft-integration/power-apps-backup/create-stream-setting.png)

**Export targets**

Export target will be created automatically using the same credentials from Organization Settings.

![CluedIn Export Target](../../../assets/images/microsoft-integration/power-apps-backup/create-export-target-2.png)

**Streams**

The creation of a stream will depend on the values of **Sync Business Domains** and **Sync Dataverse Tables**.

Once the execution of the job is done, from the sample values above, two streams should have been created, one for each of the **cluedin_dog** and **crc12_customer** tables.

![CluedIn Streams](../../../assets/images/microsoft-integration/power-apps-backup/cluedin-stream.png)

Each stream will have a certain configuration filtered by business domain.

![CluedIn Stream Configuration](../../../assets/images/microsoft-integration/power-apps-backup/cluedin-stream-configuration.png)

It will automatically assign the same export target that was created from the Dataverse connector. Incoming and outgoing edges are set to be exported. All the properties associated with it have been automatically added too.

![CluedIn Stream Export Target Configuration](../../../assets/images/microsoft-integration/power-apps-backup/cluedin-stream-export-target-configuration.png)

**Notifications**

Two notifications can be expected in this job: **Stream created** and **Stream mapping updated**.

![CluedIn Streams Notifications](../../../assets/images/microsoft-integration/power-apps-backup/cluedin-stream-notification.png)
