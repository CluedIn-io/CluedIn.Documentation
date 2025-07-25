---
layout: cluedin
title: Deduplicate data
parent: Getting started
permalink: /getting-started/data-deduplication
nav_order: 40
tags: ["getting-started"]
---
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

Deduplication process helps you find and merge duplicate records based on a set of rules that you define. This process involves [creating a deduplication project](#create-deduplication-project), [configuring the matching rules](#configure-matching-rule) for identifying duplicates, and [fixing duplicates](#fix-duplicates).

<div class="videoFrame">
<iframe src="https://player.vimeo.com/video/850839188?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen title="Getting started with data deduplication in CluedIn"></iframe>
</div>

In this guide, you will learn how to deduplicate the data that you have ingested into CluedIn.

**Before you start:** Make sure you have completed all steps in the [Ingest data guide](/getting-started/data-ingestion).

**Context:** This guide focuses on identifying duplicates based on the same first name and last name.

## Create deduplication project

As a first step, you need to create a deduplication project that allows you to check for duplicates that belong to a certain business domain.

**To create a deduplication project**

1. On the navigation pane, go to **Management**. Then, select **Deduplication**.

1. Select **Create Deduplication Project**.

1. On the **Create Deduplication Project** pane, do the following:

    1. Enter the name of the deduplication project.

    1. Select the business domain that you want to use as a filter for all records.

        ![dedup-2.png]({{ "/assets/images/getting-started/deduplication/dedup-2.png" | relative_url }})

    1. In the lower-right corner, select **Create**.

    You created the deduplication project. Now, you can proceed to define the rules for checking duplicates within the selected business domain.

## Configure matching rule

When creating a matching rule, you need to specify certain criteria. CluedIn uses these criteria to check for matching values among records belonging to the selected business domain.

**To configure a matching rule**

1. Go to the **Matching Rules** tab and select **Add Matching Rule**.

    The **Add Matching Rule** pane opens on the right side of the page.

1. On the **Matching Rule Name** tab, enter the name of the matching rule, and then select **Next**.

    ![dedup-4.png]({{ "/assets/images/getting-started/deduplication/dedup-4.png" | relative_url }})

1. On the **Matching Criteria** tab, do the following:

    1. Enter the name of the matching criteria.

    1. Select the vocabulary key. All values associated with this vocabulary key will be checked for duplicates.

    1. In the **Matching Function** dropdown list, select the method for detecting duplicates.

        ![dedup-5.png]({{ "/assets/images/getting-started/deduplication/dedup-5.png" | relative_url }})
    
    1. In the lower-right corner, select **Next**.

1. On the **Preview** tab, review the defined matching criteria.

    ![dedup-6.png]({{ "/assets/images/getting-started/deduplication/dedup-6.png" | relative_url }})

    If you want to add more matching criteria to the rule, select **Add Matching Criteria**.

1. After you have added the needed matching criteria, in the lower-right corner of the **Preview** tab, select **Add Rule**.

    The status of the deduplication project becomes **Ready to generate**.

1. In the upper-right corner, select **Generate Results**. Then, confirm that you want to generate the results for the deduplication project.

    The process of generating results may take some time. After the process is completed, you will receive a notification. If duplicates are detected, the results will be displayed on the page. The results are organized into groups containing records that match your criteria. For example, on the following screenshot, the group consists of two duplicates. The name of the group corresponds to the value of the vocabulary key from the matching rule. 

    ![dedup-8.png]({{ "/assets/images/getting-started/deduplication/dedup-8.png" | relative_url }})

    Now, you can proceed to fix the duplicates.

## Fix duplicates

The process of fixing duplicates involves reviewing the values from duplicate records and selecting which values you want to merge into the deduplicated record.

**To fix duplicates**

1. Select the name of the group.

    The **Fix Conflicts** tab opens. Here, you can view the details of the duplicate records. In the **Conflicting** section, you can find the properties that have different values in the duplicate records. In the **Matching** section, you can find the properties that have the same values in the duplicate records.

1. In the **Conflicting** section, select the values that you want to merge into the deduplicated record.

    ![dedup-9.png]({{ "/assets/images/getting-started/deduplication/dedup-9.png" | relative_url }})

1. In the upper-right corner of the page, select **Next**.

    The **Preview Merge** tab opens. Here, you can view the values that will be merged into the deduplicated record.

    ![dedup-10.png]({{ "/assets/images/getting-started/deduplication/dedup-10.png" | relative_url }})

1. In the upper-right corner of the page, select **Approve**. Then, confirm that you want to approve your selection of values for the group.

1. Select the checkbox next to the group name. Then, select **Merge**.

    ![dedup-11.png]({{ "/assets/images/getting-started/deduplication/dedup-11.png" | relative_url }})

1. Confirm that you want to merge the records from the group:

    1. Review the group that will be merged and select **Next**.

    1. Select an option to handle the data merging process if more recent data becomes available for the golden record. Then, select **Confirm**.

        ![dedup-12.png]({{ "/assets/images/getting-started/deduplication/dedup-12.png" | relative_url }})

    The process of merging data may take some time. After the process is completed, you will receive a notification. As a result, the duplicate records have been merged into one record.

{:.important}
All changes to golden records in CluedIn are tracked. You can search for the needed golden record and on the **Topology** pane, you can view the visual representation of the records that were merged through the deduplication process.

## Results & next steps

After you identified and merged duplicates, the count of golden records decreased. By following the steps outlined in this guide, you can conduct additional checks for duplicates in your data using various matching functions.

The next item on the list of common data management tasks is data streaming. Now that your data has been cleaned and deduplicated, you can send it to a Microsoft SQL Server database. Learn how to send data from CluedIn to external systems in the [Stream data guide](/getting-started/data-streaming).
