---
layout: cluedin
nav_order: 3
parent: Export targets
grand_parent: Consume
permalink: /consume/export-targets/onelake-connector
title: OneLake connector
last_modified: 2024-10-28
---

This article outlines how to configure the OneLake connector to push data from CluedIn to Microsoft’s OneLake.

**Prerequisites:** Make sure you use a [service principal](/consume/export-targets/create-service-principal) to authenticate and access OneLake.

**To configure OneLake connector**

1. On the navigation pane, go to **Consume** > **Export Targets**. Then, select **Add Export Target**.

1. On the **Choose Target** tab, select **OneLake Connector**. Then, select **Next**.

    ![onelake-connector-1.png](../../assets/images/consume/export-targets/onelake-connector-1.png)

1. On the **Configure** tab, enter the connection details:

    1. **Name** – user-friendly name of the export target that will be displayed on the **Export Target** page in CluedIn.

    1. **WorkspaceName** – name of the workspace where you want to store the data from CluedIn.

        To find the workspace, sign in to [Microsoft Fabric](https://app.fabric.microsoft.com/home?experience=data-warehouse), and then select **Workspaces** from the left-hand menu. In the list of workspaces, find the needed workspace and select it.

        ![onelake-workspace.png](../../assets/images/consume/export-targets/onelake-workspace.png)

    1. **ItemName** – name of the data item within the workspace where you want to store the data from CluedIn.

        ![onelake-item-name.png](../../assets/images/consume/export-targets/onelake-item-name.png)

    1. **ItemType** – type of the data item within the workspace where you want to store the data from CluedIn (for example, Lakehouse).

        ![onelake-item-type.png](../../assets/images/consume/export-targets/onelake-item-type.png)

    1. **ItemFolder** – directory within a data item where you want to store the data from CluedIn (for example, Files/FirstLevel/SecondLevel).

        ![onelake-item-folder.png](../../assets/images/consume/export-targets/onelake-item-folder.png)

    1. **ClientID** – unique identifier assigned to the OneLake app when it was registered in the Microsoft identity platform. You can find this value in the **Overview** section of app registration.

        ![onelake-client-id.png](../../assets/images/consume/export-targets/onelake-client-id.png)

    1. **ClientSecret** – confidential string used by your OneLake app to authenticate itself to the Microsoft identity platform. You can find this value in the **Certificates & secrets** section of app registration.

        ![onelake-client-secret.png](../../assets/images/consume/export-targets/onelake-client-secret.png)

    1. **TenantID** – unique identifier for your Microsoft Entra tenant. You can find this value in the **Overview** section of app registration.

        ![onelake-tenant-id.png](../../assets/images/consume/export-targets/onelake-tenant-id.png)

    1. **Enable Stream Cache (Sync mode only)** – when stream cache is enabled, CluedIn caches the golden records at intervals, and then writes out accumulated data to one file (JSON, Parquet, or CSV). When stream cache is not enabled, CluedIn streams out golden records one by one, each in a separate file. Stream cache is available only for the synchronized stream mode.

    1. **Output Format** – file format for the exported data. You can choose between JSON, Parquet, and CSV. However, Parquet and CSV formats are available only if you enabled stream cache. If stream cache is not enabled, you can only choose JSON.

    1. **Schedule** – schedule for sending the data from CluedIn to the export target. You can choose between hourly, daily, and weekly intervals.

1. Test the connection to make sure it works, and then select **Add**.

    ![onelake-connector-2.png](../../assets/images/consume/export-targets/onelake-connector-2.png)

    Now, you can select the OneLake connector in a stream and start exporting golden records.