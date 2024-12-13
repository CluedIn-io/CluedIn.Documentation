---
layout: cluedin
nav_order: 020
parent: Data sources
grand_parent: Integration
permalink: /integration/file
title: File
tags: ["integration"]
last_modified: 2024-01-15
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article, you will learn how to ingest data from files into CluedIn.

<div class="videoFrame">
<iframe src="https://player.vimeo.com/video/896471681?h=297bcecaf9&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" title="Using files for data ingestion"></iframe>
</div>

You can upload files in CSV, JSON, XLS, XLSX, and Parquet formats. You can upload up to 5 files at once, and the total file size should not exceed 1 GB. Note that uploading Parquet files is a beta feature. To be able to upload Parquet files, go to **Administration** > **Feature Flags**, and enable the **Parquet file support** feature.

{:.important}
The maximum number of columns accepted for data ingestion is 490.<br>Before loading data into CluedIn, ensure that it does not contain unsupported characters. Refer to our knowledge base [article](/kb/supported-characters) for information about supported and unsupported characters.

## Overview of the data ingestion process for files

When you need to upload a large set of records to CluedIn, we recommend that you start by uploading a small, representative subset of your data in CSV or JSON format. This approach allows you to verify the accuracy of mapping and relations before dealing with a large set of records. Once the golden records generated from this subset align with your expectations, you can safely remove those records from the system, while keeping the mapping configuration intact. After that you can upload a large set of records and use the existing mapping to generate golden records in an efficient way.

CluedIn **file uploader** accommodates structured data, so you can upload the files in CSV, JSON, or basic Excel formats. After you upload a JSON or XLS/XLSX file, we recommend that you download an example file provided by the system. This example serves as a reference to confirm the expected data format. If your file deviates from this format, adjust it according to the example to ensure a smooth data ingestion process.

The **data ingestion process for files** consists of three stages: uploading, parsing, and loading. When your file adheres to the required data format and each stage executes without interruption, the entire process runs seamlessly. However, to efficiently address issues that might arise during the data ingestion process, get acquainted with the potential reasons for failure at each stage:

- If the upload fails, the recovery of the file is not possible. Such a situation may arise if the file upload was initiated but the browser tab was closed while the upload was in progress. To resolve this, remove the data source and upload the file again.

- If the parsing fails—for example, due to the file being corrupted or having invalid data format—you will see a corresponding error message from the parser. To resolve this, remove the data source, fix the file and make sure it conforms to the required data format, and upload the file again.

- If the loading fails, you will see an error message with the number of chunks that could not be loaded. To resolve this, retry to load the data or remove the data source altogether and upload the file again.

## Upload a file

Follow our step-by-step instruction to upload a file.

**To upload a file**

1. On CluedIn home page, in the **Integrations** section, select **Import from files**.

1. In the **Add files** section, either drag the file or choose it from your computer.

1. Specify the **Group** where the data source will be stored. You can choose the existing group or create a new group. If you upload several files, they will be stored as separate data sources within a group.

1. In the lower-right corner, select **Upload**.

    The data has been ingested to CluedIn, and you can view it on the [Preview](/integration/additional-operations-on-records/preview) tab of the data set. Next, check the [logs](/integration/additional-operations-on-records/logs) to make sure all your records are valid. To turn your data into golden records, [create a mapping](/integration/create-mapping) and [process the data](/integration/process-data).