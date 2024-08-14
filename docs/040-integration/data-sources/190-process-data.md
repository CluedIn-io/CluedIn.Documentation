---
layout: cluedin
nav_order: 070
parent: Data sources
grand_parent: Integration
permalink: /integration/process-data
title: Process data
tags: ["integration", "processing"]
last_modified: 2023-11-07
---

In this article, you will learn about the processing of data that you ingested into CluedIn. The goal of processing is to turn your data into golden records that can be cleaned, deduplicated, and streamed.

The processing of data is the same regardless of the source of data (file, ingestion point, or database.)

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
    
    After the processing is completed, review the statistics. Any records that fail to meet specific conditions outlined in [property](/integration/additional-operations-on-records/property-rules) or [pre-process](/integration/additional-operations-on-records/preprocess-rules) rules will be sent to quarantine. To learn more about managing these records, see [Quarantine](/integration/additional-operations-on-records/quarantine).

If the processing takes a long time, go to the **Monitoring** tab and check the number of messages in the queues. Depending on the type of message queue with a high message count, you can perform specific troubleshooting actions. For further details, see [Monitoring](/integration/additional-operations-on-records/monitoring).