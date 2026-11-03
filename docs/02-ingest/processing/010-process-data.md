---
layout: cluedin
title: Process data
parent: Processing
grand_parent: Ingest
nav_order: 10
permalink: /ingest/processing/process-data
content_type: how-to
redirect_from: ["/integration/process-data"]
source_path: docs/040-integration/data-sources/190-process-data.md
tags: ["integration", "processing"]
last_modified: 2024-10-31
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

Process a data set to turn its records into standalone golden records, or to use them to enhance existing golden records. Process a data set after you have [created](/ingest/mapping/create-mapping) and [reviewed](/ingest/mapping/review-mapping) its mapping; until then, the records exist only in the data set.

Depending on the type of data source, there are three processing options:

- For file, ingestion endpoint, and database: [Manual processing](#manual-processing)

- For ingestion endpoint only: [Auto-submission](#auto-submission)

- For ingestion endpoint only: [Bridge mode](#bridge-mode)

## Prerequisites

- A data set with a mapping. See [Create mapping](/ingest/mapping/create-mapping).

- Access to the **Data Sources** module. The claims it needs are listed in [Data sources](/ingest/data-sources).

- For auto-submission and bridge mode: a data set created from an [ingestion endpoint](/ingest/data-sources/endpoint).

- Recommended: check the **Logs** tab of the data set for errors before processing. See [Logs](/ingest/troubleshooting/logs).

## How processing decides what to process

- You can process the data set as many times as you want. In CluedIn, once a record has been processed, it won't undergo processing again. When the processing is started, CluedIn checks for identical records. If identical records are found, they won't be processed again.

- If you change the primary identifier for the previously processed records, CluedIn will treat these records as new and process them.

- Records with identical primary identifiers, or identical identifiers, are merged. The confirmation pane of manual processing shows whether the selected identifier fields contain duplicates in the current data set. See [Identifiers](/ingest/mapping/review-mapping#identifiers).

- Records that fail the conditions in [property](/ingest/mapping/property-rules) or [pre-process](/ingest/mapping/preprocess-rules) rules go to [quarantine](/ingest/troubleshooting/quarantine) instead of becoming golden records. So do records from an [endpoint](/ingest/data-sources/endpoint) with [schema protection](/ingest/data-sources/endpoint#schema-protection) enabled that contain fields outside of the defined mapping.

- If [source record approval](/ingest/processing/approval) is configured for the data source, and the data set is processed by a user who is not its owner or receives data in auto-submission mode, records that meet the approval conditions are sent for approval before they are processed.

- Fields that the mapping ignores are not processed and do not appear in the resulting golden records.

## Manual processing

Manual processing is available for the data coming from a file, an ingestion endpoint, or a database. With manual processing, the original data that was initially sent to CluedIn remains in the temporary storage on the **Preview** tab. After the data has been processed, the resulting golden records appear on the **Data** tab.

**To process the data**

1. On the navigation pane, go to **Integrations** > **Data Sources**. Then, find and open the data set that you need to process.

1. Go to the **Process** tab, and then select **Process**.

    The confirmation pane opens, where you can do the following:

    - View the number of records that will be processed.

    - Delete the records that are currently in quarantine. This option is useful if you have already processed the data set before and there are some records in quarantine.

    - View the result of the primary identifier status check along with the field that was selected for producing the primary identifier.

    - View the result of the identifier status check along with the field that was selected for producing additional identifier.

        {:.important}
        If any status check shows duplicates, the records containing duplicates will be merged to maintain data integrity and consistency. To learn more about unique identifiers, see [Identifiers](/ingest/mapping/review-mapping#codes).

1. In the lower-right corner, select **Confirm**.

    ![Animation: on the Process tab, selecting Process opens the confirmation pane; after Confirm, a processing log shows Success 20]({{ "/assets/images/integration/data-sources/process-data.gif" | relative_url }})

## Auto-submission

Auto-submission is available for the data coming from an ingestion endpoint. When auto-submission is enabled, data received from the ingestion endpoint is processed automatically. With auto-submission, the original data that was initially sent to CluedIn remains in the temporary storage on the **Preview** tab. After the data has been processed, the resulting golden records appear on the **Data** tab.

**To enable auto-submission**

1. On the navigation pane, go to **Integrations** > **Data Sources**. Then, find and open the data set for which you want to enable auto-submission.

1. Go to the **Process** tab, and then turn on the toggle next to **Auto-submission**.

1. Confirm that you want to enable automatic processing of records once they are received by CluedIn.

    ![Animation: turning on the Auto submission toggle on the Process tab, confirming, and a notification that auto-submission has been saved]({{ "/assets/images/integration/data-sources/auto-submission-1.gif" | relative_url }})

If you no longer want the records to be processed automatically, turn off the toggle next to **Auto-submission**.

## Bridge mode

Bridge mode is available for the data coming from an ingestion endpoint. When bridge-mode is enabled, all your JSON records will be transformed into golden records directly, without being stored in the temporary storage on the **Preview** tab. However, you can rely on data set logs and ingestion receipts for debugging purposes.

Bridge mode allows you to use less storage and memory, resulting in increased performance. Use this mode when your mapping will not change over time, and you want to use the ingestion endpoint only as a mapper.

**To switch to bridge mode**

1. On the navigation pane, go to **Integrations** > **Data Sources**. Then, find and open the data set that you want to switch to bridge mode.

1. Go to the **Process** tab. Open the three dots menu, and then select **Switch to bridge mode**.

1. Confirm that you want to switch to bridge mode by entering _BRIDGE_. Then, select **Confirm bridge mode**.

    ![Animation: choosing Switch to bridge mode in the Process tab menu, typing BRIDGE, and the data set showing the Bridge Mode label]({{ "/assets/images/integration/data-sources/bridge-mode-1.gif" | relative_url }})

If you no longer want your ingestion endpoint to operate in bridge mode, you can switch it back to the default mode. After switching back to the default mode, the **Preview** tab will appear. However, it will not contain records received while bridge mode was enabled.

**To switch back to default mode**

1. On the navigation pane, go to **Integrations** > **Data Sources**. Then, find and open the data set that you want to switch back to default mode.

1. Go to the **Process** tab. Open the three dots menu, and then select **Switch to default mode**.

1. Confirm that you want to switch back to default mode by entering _DEFAULT_. Then, select **Confirm default mode**.

    ![Animation: choosing Switch to default mode in the Process tab menu, typing DEFAULT, confirming, and the Preview tab returning]({{ "/assets/images/integration/data-sources/default-mode-1.gif" | relative_url }})

## Processing logs

Every time the records are processed, a new processing log appears on the **Process** tab of the data set. If the number of processing logs is growing, consider removing older logs. You can also configure the retention settings to automatically remove processing logs after a specific period.

### Remove processing logs

Removing processing logs frees up disk space without impacting the processed records. However, once removed, processing logs cannot be recovered.

**To remove processing logs**

1. Near the upper-right corner of the processing logs table, open the three dots menu, and then select **Purge processing logs**.

1. Select the statuses of the processing logs that you want to remove.

1. Confirm that you want to remove processing logs by entering _DELETE_. Then, select **Purge**.

    ![Animation: choosing Purge processing logs, keeping the Finished, Aborted and Cancelled statuses selected, typing DELETE, and selecting Purge]({{ "/assets/images/integration/data-sources/purge-logs-1.gif" | relative_url }})

    After processing logs are removed, the **Process** tab will display information about the user who removed them and the time of removal.

### Configure retention settings

Retention settings allow you to automatically delete processing logs after a specified period.

**To configure retention settings**

1. Near the upper-right corner of the processing logs table, open the three dots menu, and then select **Retention settings**.

1. Select the checkbox to enable retention.

1. Select a period to specify which processing logs should be removed. For example, selecting **2 months old** means that all processing logs created 2 months ago will be removed. Thus, when a processing log turns 2 months old, it will be automatically removed.

1. Select **Save**.

    ![Animation: opening Retention settings from the Process tab menu, enabling retention, choosing 2 months old, and saving]({{ "/assets/images/integration/data-sources/retention-settings-1.gif" | relative_url }})

1. If you want to change the retention period, repeat step 1. Then, select another period and save your changes.

1. If you want to remove the retention settings, repeat step 1. Then, clear the checkbox to disable retention and save your changes.

## Verify the result

Processing runs in the background. Selecting **Confirm**, or new data arriving with auto-submission enabled, sends a request for processing; the records then move through the processing queues shown on the **Monitoring** tab.

- **On the Process tab**, a new [processing log](#processing-logs) appears in the table, with the **Source**, the **Total** number of records, the **Stats**, and when it was **Created**. While the records are being processed, the **Stats** column shows a progress indicator and a **Cancel** button is available. When processing has finished, the **Stats** column shows **Success** with the number of records and a check mark.

- **On the Data tab**, records that were processed successfully are displayed.

- **On the Quarantine tab**, records that did not meet the conditions described in [How processing decides what to process](#how-processing-decides-what-to-process) are listed. See [Quarantine](/ingest/troubleshooting/quarantine).

- **On the Monitoring tab**, the queue message counts return to 0 when there is nothing left to process. See [Monitoring](/ingest/troubleshooting/monitoring).

- **As a notification**, once all processing across the organization has finished, CluedIn proactively surfaces a "Duplicates found" notification if any deduplication project has unresolved duplicate groups, and a "Data quality issues found" notification if any data quality metric is below its configured threshold. See [Deduplication](/master/deduplication) and [Data quality dashboard](/govern/data-quality-dashboard) to review and act on what was found.

## What this changes

- **Golden records.** Processed records become new golden records, or are added as data parts to existing golden records. Records with identical primary identifiers are merged.

- **Source data.** With manual processing and auto-submission, the original data that was initially sent to CluedIn remains in the temporary storage on the **Preview** tab. In bridge mode, records are not stored there.

- **Undoing processing.** To take the processed records out of CluedIn again, [remove the records](/ingest/processing/remove-records) created from the data set. This removes golden records that consist only of those records, and removes the corresponding data parts from golden records that also have data from other sources.

- **Processing logs.** Removing processing logs frees up disk space without impacting the processed records, but removed logs cannot be recovered. For an ingestion endpoint, the receipts associated with those submissions become orphaned.

## If something goes wrong

- **Processing takes a long time.** Go to the **Monitoring** tab and check the number of messages in the queues. Depending on the type of message queue with a high message count, you can perform specific troubleshooting actions. For further details, see [Monitoring](/ingest/troubleshooting/monitoring).

- **A submission is in the Error state.** On the **Process** tab, select **Retry** for that submission. See [Monitoring](/ingest/troubleshooting/monitoring#ingestion-anomalies).

- **Records are in quarantine.** Open the **Quarantine** tab to see which rule sent each record there, then fix and process the records, or reject them. See [Quarantine](/ingest/troubleshooting/quarantine).

- **Some records were not processed again.** Records that were processed before are skipped. See [How processing decides what to process](#how-processing-decides-what-to-process).

- **More records were merged than expected.** The field used for the primary identifier or an identifier contains duplicate values. Check the identifier status in the confirmation pane before you confirm, and see [Review mapping](/ingest/mapping/review-mapping#identifiers).
