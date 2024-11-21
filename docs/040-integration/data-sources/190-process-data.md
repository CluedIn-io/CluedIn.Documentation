---
layout: cluedin
nav_order: 070
parent: Data sources
grand_parent: Integration
permalink: /integration/process-data
title: Process data
tags: ["integration", "processing"]
last_modified: 2024-08-15
---

In this article, you will learn about the processing of data that you ingested into CluedIn. The goal of processing is to turn your records into standalone golden records or to use them to enhance existing golden records.

Depending on the type of data source, there are three processing options:

- For file, endpoint, and database: Manual processing

- For endpoint only: Auto-submission

- For endpoint only: Bridge mode

You can process the data set as many times as you want. In CluedIn, once a record has been processed, it won’t undergo processing again. When the processing is started, CluedIn checks for identical records. If identical records are found, they won’t be processed again. However, if you change the origin code for the previously processed records, CluedIn will treat these records as new and process them.

After the processing is completed, the [processing log](#processing-logs) appears in the table. Any records that fail to meet specific conditions outlined in [property](/Documentation/Data-sources/Additional-operations/Property-rules) or [pre-process](/Documentation/Data-sources/Additional-operations/Pre%2Dprocess-rules) rules will be sent to quarantine. To learn more about managing these records, see [Quarantine](/Documentation/Data-sources/Additional-operations/Quarantine). Records that were processed successfully are displayed on the **Data** tab.

If the processing takes a long time, go to the **Monitoring** tab and check the number of messages in the queues. Depending on the type of message queue with a high message count, you can perform specific troubleshooting actions. For further details, see [Monitoring](/Documentation/Data-sources/Additional-operations/Monitoring).

## Manual processing

Manual processing is available for the data coming from a file, an endpoint, or a database. With manual processing, the original data that was initially sent to CluedIn remains in the temporary storage on the **Preview** tab. After the data has been processed, the resulting golden records appear on the **Data** tab.

**To process the data**

1. On the navigation pane, go to **Integrations** > **Data Sources**. Then, find and open the data set that you need to process.

1. Go to the **Process** tab, and then select **Process**.

    The confirmation pane opens, where you can do the following:

    - View the number of records that will be processed.

    - Delete the records that are currently in quarantine. This option is relevant if you have already processed the data set before and there are some records in quarantine.

    - View the result of the origin entity code status check along with the field that was selected for producing the entity origin code.

    - View the result of the code status check along with the field that was selected for producing the entity code.

    {:.important}
    The records containing duplicates will be merged to maintain data integrity and consistency. To learn more about unique identifiers, see [Codes](/integration/review-mapping#codes).

1. In the lower-right corner, select **Confirm**.

    ![process-data.gif](../../assets/images/integration/data-sources/process-data.gif)
    
## Auto-submission

Auto-submission is available for the data coming from an endpoint. When auto-submission is enabled, data received from the endpoint is processed automatically. With auto-submission, the original data that was initially sent to CluedIn remains in the temporary storage on the **Preview** tab. After the data has been processed, the resulting golden records appear on the **Data** tab.

**To enable auto-submission**

1. On the navigation pane, go to **Integrations** > **Data Sources**. Then, find and open the data set for which you want to enable auto-submission.

1. Go to the **Process** tab, and then turn on the toggle next to **Auto-submission**.

1. Confirm that you want to enable automatic processing of records once they are received by CluedIn.

    ![auto-submission.gif](../../assets/images/integration/data-sources/auto-submission.gif)

If you no longer want the records to be processed automatically, turn off the toggle next to **Auto-submission**.

## Bridge mode

Bridge mode is available for the data coming from an endpoint. When bridge-mode is enabled, all your JSON records will be transformed into golden records directly, without being stored in the temporary storage on the **Preview** tab. However, you can rely on data set logs and ingestion receipts for debugging purposes.

Bridge mode allows you to use less storage and memory, resulting in increased performance. Use this mode when your mapping will not change over time, and you want to use the ingestion endpoint only as a mapper.

**To switch to bridge mode**

1. On the navigation pane, go to **Integrations** > **Data Sources**. Then, find and open the data set that you want to switch to bridge mode.

1. Go to the **Process** tab. Open the three dots menu, and then select **Switch to bridge mode**.

1. Confirm that you want to switch to bridge mode by entering _BRIDGE_. Then, select **Confirm bridge mode**.

    ![enable-bridge-mode.gif](../../assets/images/integration/data-sources/enable-bridge-mode.gif)

If you no longer want your endpoint to operate in bridge mode, you can switch it back to the default mode. After switching back to the default mode, the **Preview** tab will appear. However, it will not contain records received while bridge mode was enabled.

**To switch back to default mode**

1. On the navigation pane, go to **Integrations** > **Data Sources**. Then, find and open the data set that you want to switch back to default mode.

1. Go to the **Process** tab. Open the three dots menu, and then select **Switch to default mode**.

1. Confirm that you want to switch back to default mode by entering _DEFAULT_. Then, select **Confirm default mode**.

    ![disable-bridge-mode.gif](../../assets/images/integration/data-sources/disable-bridge-mode.gif)

## Processing logs

Every time the records are processed, a new processing log appears on the **Process** tab of the data set. If the number of processing logs is growing, consider removing older logs. You can also configure the retention settings to automatically remove processing logs after a specific period.

### Remove processing logs

Removing processing logs frees up disk space without impacting the processed records. However, once removed, processing logs cannot be recovered.

**To remove processing logs**

1. Near the upper-right corner of the processing logs table, open the three dots menu, and then select **Purge processing logs**.

1. Select the statuses of the processing logs that you want to remove.

1. Confirm that you want to remove processing logs by entering _DELETE_. Then, select **Purge**.

    ![remove-processing-logs.gif](../../assets/images/integration/data-sources/remove-processing-logs.gif)

    After processing logs are removed, the **Process** tab will display information about the user who removed them and the time of removal.

### Configure retention settings

Retention settings allow you to automatically delete processing logs after a specified period.

**To configure retention settings**

1. Near the upper-right corner of the processing logs table, open the three dots menu, and then select **Retention settings**.

1. Select the checkbox to enable retention.

1. Select a period to specify which processing logs should be removed. For example, selecting **2 months old** means that all processing logs created 2 months ago will be removed. Thus, when a processing log turns 2 months old, it will be automatically removed.

1. Select **Save**.

    ![retention-settings.gif](../../assets/images/integration/data-sources/retention-settings.gif)

1. If you want to change the retention period, repeat step 1. Then, select another period and save your changes.

1. If you want to remove the retention settings, repeat step 1. Then, clear the checkbox to disable retention and save your changes.