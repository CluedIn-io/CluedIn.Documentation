---
layout: cluedin
nav_order: 20
parent: Power Apps Integration
grand_parent: Microsoft Integration
permalink: /microsoft-integration/powerapps/configuration-guide
title: Power Apps configuration guide
tags: ["integration", "microsoft", "powerapps", "dataverse"]
last_modified: 2025-03-13
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this guide, you will learn how to configure Power Apps integration in CluedIn.

Make sure that you have completed all of the actions described in [Power Apps pre-configuration guide](/microsoft-integration/powerapps/pre-configuration-guide).

## Basic Power Apps configuration

Basic Power Apps configuration is required to establish connection between your CluedIn instance and your Power Apps environment.

**To configure Power Apps in CluedIn**

1. In CluedIn, go to **Administration** > **Settings**, and then scroll down to find the **Power Apps** section.

1. In **Base URL**, enter the root address used to access resources within your Power Apps environment. You can find this value in your [Power Apps](https://make.powerapps.com/) environment: in the upper-right corner of the Power Apps page, select the settings icon, and then select **Developer Resources**. Copy the value in **Web API endpoint** and paste it to the **URL** field in CluedIn. You do not need to copy the version of the API (`/api/data/v9.2`).

    ![dev-resources-base-url.png](../../assets/images/microsoft-integration/power-apps/dev-resources-base-url.png)

1. In **Tenant Id**, enter a unique identifier for your Microsoft Entra ID tenant in which your application is registered. This is the application that you created during the pre-configuration stage in [Register a new application](/microsoft-integration/powerapps/pre-configuration-guide#register-a-new-application). You can find this value in **Directory (tenant) ID**.

1. In **Client Id**, enter a unique identifier assigned to an application when you registered it in Microsoft Entra ID. This is the application that you created during the pre-configuration stage in [Register a new application](/microsoft-integration/powerapps/pre-configuration-guide#register-a-new-application). You can find this value in **Application (client) ID**.

1. In **Client Secret**, enter a string value that your application uses to prove its identity when requesting a token. This is the client secret that you created during the pre-configuration stage in [Create a client secret](/microsoft-integration/powerapps/pre-configuration-guide#create-a-client-secret)

1. In **Environment Id**, enter a unique identifier assigned to you Power Apps environment. This is the environment ID that you found during the pre-configuration stage in [Find your environment ID](/microsoft-integration/powerapps/pre-configuration-guide#find-your-environment-id)

    ![cluedin-power-apps.png](../../assets/images/microsoft-integration/power-apps/cluedin-power-apps.png)

1. In the upper-right corner, select **Save**.

    Proceed to the next section to configure Power Apps integration features that you want to use.

## Features of Power Apps integration

Power Apps integration offers a variety of features for syncing data between CluedIn and Dataverse.

**To configure specific features of Power Apps integration**

1. If you want to sync multiple CluedIn business domains to Dataverse tables, specify the **Parallel Execution Count**. This is the number of business domains that can be simultaneously synced with Dataverse. Be default, this number is 5.

1. If you want to sync CluedIn business domains to Dataverse tables:

    1. Turn on the toggle next to **Sync CluedIn Business Domains to Dataverse Table**.

    1. Enter the business domains that you want to sync. If you want to sync multiple business domains, separate them with a comma (for example, _/Type1,/Type2,/Type3_). 

        ![sync-entity-types.png](../../assets/images/microsoft-integration/power-apps/sync-entity-types.png)

        Each business domain will be synced into a separate Dataverse table. For more information, see [Sync business domains to Dataverse tables](/microsoft-integration/powerapps/features/sync-entitytypes).

1. If you want to sync Dataverse tables and columns to CluedIn business domains and vocabulary keys:

    1. Turn on the toggle next to **Sync Dataverse Table/Columns to CluedIn Business Domains and Vocabulary**.

    1. Enter the name of the Dataverse table that you want to sync. This should be the logical name of the Dataverse table. If you want to sync multiple tables, separate them with a comma (for example, _logical_name1,logical_name2,logical_name3_).

        ![sync-dataverse-table.png](../../assets/images/microsoft-integration/power-apps/sync-dataverse-table.png)

        Each table will be synced into a separate CluedIn business domain and vocabulary associated with that business domain. The columns from the table will be synced into the vocabulary keys of the vocabulary associated with the business domain. For more information, see [Sync Dataverse tables to CluedIn business domains and vocabularies](/microsoft-integration/powerapps/features/sync-dataverse).

1. If you want to automate the ingestion of data from Dataverse to CluedIn:

    1. Turn on the toggle next to **Create workflow to Ingest Data to CluedIn**.

    1. If you want to allow specific users to view the workflow in Power Apps, add the email addresses of those users in **Workflow Access Users List**.

    1. Enter the **Dataverse Connection ID**. This is the ID that you found during the pre-configuration stage in [Create a connection](/microsoft-integration/powerapps/pre-configuration-guide#create-a-dataverse-connection).

        ![ingestion-workflow.png](../../assets/images/microsoft-integration/power-apps/ingestion-workflow.png)

        For more information, see [Create ingestion endpoint workflow](/microsoft-integration/powerapps/features/create-workflow).

1. If you want to create a stream to export golden records from CluedIn to a Dataverse table:

    1. Make sure you have the [Dataverse export target](/consume/export-targets/dataverse-connector) installed in your CluedIn instance. It should be available in the list of export targets (**Consume** > **Export Targets** > **Add Export Target**). You do not need to configure the Dataverse export target because it will be configured automatically.

    1. Make sure you have enabled **Sync CluedIn Business Domains to Dataverse Table** for business domains of golden records that you want to export to a Dataverse table. 

    1. Turn on the toggle next to **Create CluedIn Stream**.

        ![create-stream.png](../../assets/images/microsoft-integration/power-apps/create-stream.png)

        For more information, see [Create streams](/microsoft-integration/powerapps/features/create-streams).

1. In the upper-right corner, select **Save**.

## Next steps

Explore different [features](/microsoft-integration/powerapps/features) that are available as part of Power Apps integration in CluedIn.