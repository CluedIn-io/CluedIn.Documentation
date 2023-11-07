---
layout: default
nav_order: 050
parent: Integration
permalink: /integration/process-data
title: Process data
tags: ["integration", "processing"]
last_modified: 2023-11-07
---

In this article, you will learn about the processing of data that you ingested into CluedIn. The goal of processing is to turn your data into records that can be searchable, cleaned, deduplicated, and streamed. These records can be merged or used to enhance the existing golden records.

The processing of data is the same regardless of the source of data (file, ingestion point, or database.)

**To process the data**

1. On the navigation pane, go to **Integrations** > **Data Sources**. Then, find and open the data set that you need to process.

1. Go to the **Process** tab, and then select **Process**.

    The confirmation pane opens, where you can view the number of records that will be processed.

    **Note:** The records containing duplicates will be merged to maintain data integrity and consistency. To learn more about unique identifiers, see [Codes](/integration/review-mapping#codes).

1. In the lower-right corner, select **Confirm**.

    After the processing is completed, review the statistics. Any records that fail to meet specific conditions outlined in [property](/integration/additional-operations-on-records/property-rules) or [pre-process](/integration/additional-operations-on-records/preprocess-rules) rules will be sent to quarantine. To learn more about managing these records, see [Quarantine](/integration/additional-operations-on-records/quarantine).

If the processing takes a long time, go to the **Monitoring** tab and check the number of messages in the queues. Depending on the type of message queue with a high message count, you can perform specific troubleshooting actions. For further details, see [Monitoring](/integration/additional-operations-on-records/monitoring).