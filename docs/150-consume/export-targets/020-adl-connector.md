---
layout: cluedin
nav_order: 2
parent: Export targets
grand_parent: Consume
permalink: /consume/export-targets/adl-connector
title: Azure Data Lake connector
last_modified: 2024-10-28
---

This article outlines how to configure the Azure Data Lake connector to publish data from CluedIn to Azure Data Lake Storage Gen2.

**Prerequisites:** Make sure you use a service principal to authenticate and access Azure Data Lake.

**To configure Azure Data Lake connector**

1. On the navigation pane, go to **Consume** > **Export Targets**. Then, select **Add Export Target**.

1. On the **Choose Target** tab, select **Azure Data Lake Connector**. Then, select **Next**.

    ![adl-connector-1.png](../../assets/images/consume/export-targets/adl-connector-1.png)

1. On the **Configure** tab, enter the connection details:

    1. **Name** – user-friendly name of the export target that will be displayed on the **Export Target** page in CluedIn.

    1. **AccountName** – name of the Azure Data Lake storage account where you want to store the data from CluedIn.

        ![adl-account-name.png](../../assets/images/consume/export-targets/adl-account-name.png)

    1. **AccountKey** – access key for authenticating requests to the Azure Data Lake storage account.

        ![adl-account-key.png](../../assets/images/consume/export-targets/adl-account-key.png)

    1. **FileSystemName** – name of a container in Azure Data Lake.

        ![adl-file-system-name.png](../../assets/images/consume/export-targets/adl-file-system-name.png)

    1. **DirectoryName** – name of a directory inside the container in Azure Data Lake.

        ![adl-directory-name.png](../../assets/images/consume/export-targets/adl-directory-name.png)

    1. **Enable Stream Cache (Sync mode only)** – when stream cache is enabled, CluedIn caches the golden records at intervals, and then writes out accumulated data to one file (JSON, Parquet, or CSV). When stream cache is not enabled, CluedIn streams out golden records one by one, each in a separate file. Stream cache is available only for the synchronized stream mode.

    1. **Output Format** – file format for the exported data. You can choose between JSON, Parquet, and CSV. However, Parquet and CSV formats are available only if you enabled stream cache. If stream cache is not enabled, you can only choose JSON.

    1. **Schedule** – schedule for sending the data from CluedIn to the export target. You can choose between hourly, daily, and weekly intervals.

1. Test the connection to make sure it works, and then select **Add**.

    ![adl-connector-2.png](../../assets/images/consume/export-targets/adl-connector-2.png)

    Now, you can select the Azure Data Lake connector in a stream and start exporting golden records.