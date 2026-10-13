---
title: File
url: https://documentation.cluedin.net/ingest/data-sources/file
content_type: how-to
section: Ingest > Data sources
---

# File

> how-to: Steps to accomplish one task.

Upload one or more files to CluedIn to create a data set for each file. Use a file when your data is an export you can upload by hand; to push records to CluedIn over HTTP, use an [ingestion endpoint](https://documentation.cluedin.net/ingest/data-sources/endpoint.md), and to read tables directly from a database, use a [database](https://documentation.cluedin.net/ingest/data-sources/database.md). Uploading a file does not create golden records yet: that takes [mapping](https://documentation.cluedin.net/ingest/mapping/create-mapping.md) and [processing](https://documentation.cluedin.net/ingest/processing/process-data.md).

## Prerequisites

- Access to the **Data Sources** module. The claims it needs are listed in [Data sources](https://documentation.cluedin.net/ingest/data-sources.md): at least Consulted for all **Integration** claims, and at least Informed for **Data Catalog**, **Annotation** and **Export Targets**.

- To upload Parquet files: go to **Administration** > **Feature Flags**, and enable the **Parquet file support** feature. Uploading Parquet files is a beta feature.

- A file that meets the limits in [Inputs](#inputs) and contains only supported characters.

> **Important:** The maximum number of columns accepted for data ingestion is 490.<br>Before loading data into CluedIn, ensure that it does not contain unsupported characters. Refer to our knowledge base [article](https://documentation.cluedin.net/model/data-catalog/supported-characters.md) for information about supported and unsupported characters.

## Inputs

| Field | Required | What it accepts | Example |
|--|--|--|--|
| **Add files** | Yes | Files in CSV, JSON, XLS, XLSX, or Parquet format. Up to 5 files at once, with a total size of no more than 1 GB, and no more than 490 columns. | `customers.csv` |
| **Group** | Chosen in step 3 of the procedure | An existing group, or the name of a new group. Every file in one upload goes into this group as a separate data source. | `CRM exports` |

## Overview of the data ingestion process for files

When you need to upload a large set of records to CluedIn, we recommend that you start by uploading a small, representative subset of your data in CSV or JSON format. This approach allows you to verify the accuracy of mapping and relations before dealing with a large set of records. Once the golden records generated from this subset align with your expectations, you can safely remove those records from the system, while keeping the mapping configuration intact. After that you can upload a large set of records and use the existing mapping to generate golden records in an efficient way.

CluedIn **file uploader** accommodates structured data, so you can upload the files in CSV, JSON, or basic Excel formats. After you upload a JSON or XLS/XLSX file, we recommend that you download an example file provided by the system. This example serves as a reference to confirm the expected data format. If your file deviates from this format, adjust it according to the example to ensure a smooth data ingestion process.

The **data ingestion process for files** consists of three stages: uploading, parsing, and loading. When your file adheres to the required data format and each stage executes without interruption, the entire process runs seamlessly. Each stage can fail for a different reason; see [If something goes wrong](#if-something-goes-wrong).

## Upload a file

Follow our step-by-step instruction to upload a file.

**To upload a file**

1. On CluedIn home page, in the **Integrations** section, select **Import from files**.

1. In the **Add files** section, either drag the file or choose it from your computer.

1. Specify the **Group** where the data source will be stored. You can choose the existing group or create a new group. If you upload several files, they will be stored as separate data sources within a group.

1. In the lower-right corner, select **Upload**.

    Keep the browser tab open until the upload has finished. If the tab is closed while the upload is in progress, the file cannot be recovered.

    The data has been ingested to CluedIn, and you can view it on the [Preview](https://documentation.cluedin.net/ingest/processing/preview.md) tab of the data set. Next, check the [logs](https://documentation.cluedin.net/ingest/troubleshooting/logs.md) to make sure all your records are valid. To turn your data into golden records, [create a mapping](https://documentation.cluedin.net/ingest/mapping/create-mapping.md) and [process the data](https://documentation.cluedin.net/ingest/processing/process-data.md).

## Verify the result

- On the navigation pane, go to **Integrations** > **Data Sources**. The group you chose contains one data source for each uploaded file.

- Open the data set. The **Preview** tab shows the original, raw records from the file. The data set has not been processed yet, so it shows the **Not Processed** status next to its name.

- On the **Logs** tab, check for entries with the **Error** level. A record with an error is not saved in CluedIn. Warnings mean the record was stored but some values, such as property names, were changed. See [Logs](https://documentation.cluedin.net/ingest/troubleshooting/logs.md).

- On the **Monitoring** tab, the **Total** section shows the total number of records and original columns, so you can compare them with your file. See [Monitoring](https://documentation.cluedin.net/ingest/troubleshooting/monitoring.md).

## What this changes

- Uploading creates a data source in the group you chose, and a data set holding the file's records in temporary storage, shown on the **Preview** tab.

- No golden records are created or changed. Records become golden records, or enhance existing ones, only after you [create a mapping](https://documentation.cluedin.net/ingest/mapping/create-mapping.md) and [process the data](https://documentation.cluedin.net/ingest/processing/process-data.md).

- To undo an upload, remove the data source.

## If something goes wrong

- **The upload fails.** The file cannot be recovered. This happens, for example, if the browser tab was closed while the upload was in progress. Remove the data source and upload the file again.

- **Parsing fails.** You see an error message from the parser, for example because the file is corrupted or its data format is invalid. Remove the data source, fix the file so that it conforms to the required data format, and upload the file again. For JSON and XLS/XLSX files, compare your file with the example file that CluedIn provides.

- **Loading fails.** You see an error message with the number of chunks that could not be loaded. Retry loading the data (on the **Preview** tab, select **Retry**), or remove the data source and upload the file again. The **Loading Failures** queue on the **Monitoring** tab counts records that could not be fully loaded; see [Monitoring](https://documentation.cluedin.net/ingest/troubleshooting/monitoring.md#common-monitoring-elements).

- **The Logs tab shows errors.** Each validation message explains what is wrong with the record, for example a record with too many columns or a property with unsupported characters. See [Logs](https://documentation.cluedin.net/ingest/troubleshooting/logs.md).

Up: [Data sources](https://documentation.cluedin.net/ingest/data-sources.md)
