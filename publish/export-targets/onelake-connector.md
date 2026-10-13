---
title: OneLake connector
url: https://documentation.cluedin.net/publish/export-targets/onelake-connector
content_type: reference
section: Publish & consume > Export targets
---

# OneLake connector

> reference: Facts, options, APIs.

This article outlines how to configure the OneLake connector to push data from CluedIn to Microsoft’s OneLake.

**Prerequisites**

- Make sure you have a [service principal](https://documentation.cluedin.net/publish/export-targets/create-service-principal.md) to authenticate and access OneLake.

- In PowerBI/Fabric, enable the following settings:

    - **Service principals can use Fabric APIs**

        ![Fabric tenant setting Service principals can use Fabric APIs, set to Enabled and applied to the entire organization](https://documentation.cluedin.net/assets/images/consume/export-targets/onelake-fabric-settings-api.png)

    - **Users can access data stored in OneLake with apps external to Fabric**

        ![OneLake setting Users can access data stored in OneLake with apps external to Fabric, set to Enabled](https://documentation.cluedin.net/assets/images/consume/export-targets/onelake-fabric-settings-data-access.png)

- In the workspace that you want to use in OneLake connector, give at least Contributor access to the OneLake service principal. To do that, in the workspace, select **Manage access**.

    ![Fabric workspace toolbar with Manage access highlighted](https://documentation.cluedin.net/assets/images/consume/export-targets/onelake-workspace-manage-access.png)

    Then, add the OneLake service principal and assign it the Contributor role to the workspace.

    ![Manage access pane of the workspace with the OneLake service principal listed and assigned the Contributor role](https://documentation.cluedin.net/assets/images/consume/export-targets/onelake-workspace-manage-access-contributor.png)

**To configure OneLake connector**

1. On the navigation pane, go to **Consume** > **Export Targets**. Then, select **Add Export Target**.

1. On the **Choose Target** tab, select **OneLake Connector**. Then, select **Next**.

    ![Choose Target tab of the Add Export Target pane with OneLake Connector selected](https://documentation.cluedin.net/assets/images/consume/export-targets/onelake-connector-1.png)

1. On the **Configure** tab, enter the connection details:

    1. **Name** – user-friendly name of the export target that will be displayed on the **Export Target** page in CluedIn.

    1. **WorkspaceName** – name of the workspace where you want to store the data from CluedIn.

        To find the workspace, sign in to [Microsoft Fabric](https://app.fabric.microsoft.com/home?experience=data-warehouse), and then select **Workspaces** from the left-hand menu. In the list of workspaces, find the needed workspace and select it.

        ![Microsoft Fabric Workspaces menu with the CluedInLakehouse workspace highlighted](https://documentation.cluedin.net/assets/images/consume/export-targets/onelake-workspace.png)

    1. **ItemName** – name of the data item within the workspace where you want to store the data from CluedIn.

        ![Workspace item list with the CluedInLakehouse item name highlighted](https://documentation.cluedin.net/assets/images/consume/export-targets/onelake-item-name.png)

    1. **ItemType** – type of the data item within the workspace where you want to store the data from CluedIn (for example, Lakehouse).

        ![Workspace item list with the item type Lakehouse highlighted](https://documentation.cluedin.net/assets/images/consume/export-targets/onelake-item-type.png)

    1. **ItemFolder** – directory within a data item where you want to store the data from CluedIn (for example, Files/FirstLevel/SecondLevel).

        ![Lakehouse Explorer with the Files/FirstLevel/SecondLevel folder path highlighted](https://documentation.cluedin.net/assets/images/consume/export-targets/onelake-item-folder.png)

    1. **ClientID** – unique identifier assigned to the OneLake app when it was registered in the Microsoft identity platform. You can find this value in the **Overview** section of app registration.

        ![OneLake app registration Overview page in the Azure portal with the Application (client) ID highlighted](https://documentation.cluedin.net/assets/images/consume/export-targets/onelake-client-id.png)

    1. **ClientSecret** – confidential string used by your OneLake app to authenticate itself to the Microsoft identity platform. You can find this value in the **Certificates & secrets** section of app registration.

        ![Client secrets tab of the app registration with the secret Value highlighted](https://documentation.cluedin.net/assets/images/consume/export-targets/onelake-client-secret.png)

    1. **TenantID** – unique identifier for your Microsoft Entra tenant. You can find this value in the **Overview** section of app registration.

        ![OneLake app registration Overview page in the Azure portal with the Directory (tenant) ID highlighted](https://documentation.cluedin.net/assets/images/consume/export-targets/onelake-tenant-id.png)

    1. **Enable Stream Cache (Sync mode only)** – when stream cache is enabled, CluedIn caches the golden records at intervals, and then writes out accumulated data to one file (JSON, Parquet, or CSV). When stream cache is not enabled, CluedIn streams out golden records one by one, each in a separate JSON file. Stream cache is available only for the synchronized stream mode.

        ![Configure tab with Name, Workspace Name, Item Name, Item Type, Item Folder, client and tenant details, and Enable Stream Cache turned on](https://documentation.cluedin.net/assets/images/consume/export-targets/onelake-connector-configure-1.png)

    1. **Output Format** – file format for the exported data. You can choose between JSON, Parquet, and CSV. However, Parquet and CSV formats are available only if you enabled stream cache. If stream cache is not enabled, JSON is the default format.

    1. **Export Schedule** – schedule for sending the files from CluedIn to the export target. The files will be exported based on Coordinated Universal Time (UTC), which has an offset of 00:00. You can choose between the following options:

        - **Hourly** – files will be exported every hour (for example, at 1:00 AM, at 2:00 AM, and so on).

        - **Daily** – files will be exported every day at 12:00 AM.

        - **Weekly** – files will be exported every Monday at 12:00 AM.

        - **Custom Cron** – you can create a specific schedule for exporting files by entering the cron expression in the **Custom Cron** field. For example, the cron expression `0 18 * * *` means that the files will be exported every day at 6:00 PM.

    1. (Optional) **File Name Pattern** – a file name pattern for the export file. For more information, see [File name patterns](https://documentation.cluedin.net/publish/export-targets/file-name-patterns.md).

        For example, in the `{ContainerName}.{OutputFormat}` pattern, `{ContainerName}` is the **Target Name** in the [stream](https://documentation.cluedin.net/publish/streams/create-a-stream.md#configure-an-export-target), and `{OutputFormat}` is the output format that you select in step 3j. In this case, every time the scheduled export occurs, it will generate the same file name, replacing the previously exported file.

        If you do not specify the file name pattern, CluedIn will use the default file name pattern: `{StreamId:N}_{DataTime:yyyyMMddHHmmss}.{OutputFormat}`.

1. Test the connection to make sure it works, and then select **Add**.

    ![Lower part of the Configure tab with Output Format Parquet, a daily Export Schedule, a File Name Pattern, and the Test connection and Add buttons](https://documentation.cluedin.net/assets/images/consume/export-targets/onelake-connector-configure-2.png)

    Now, you can select the OneLake connector in a stream and start exporting golden records.

Up: [Export targets](https://documentation.cluedin.net/publish/export-targets.md)
