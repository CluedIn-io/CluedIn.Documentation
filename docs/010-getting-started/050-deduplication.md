---
layout: default
title: Deduplicate data
parent: Getting Started
permalink: /getting-started/data-deduplication
nav_order: 50
tags: ["getting-started"]
---
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

Deduplication process helps you find and merge duplicate records based on a set of rules that you define. CluedIn will automatically identify the changes and update the stream with deduplicated records.

<div style="padding:56.25% 0 0 0;position:relative;">
<iframe src="https://player.vimeo.com/video/850839188?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen style="position:absolute;top:0;left:0;width:100%;height:100%;" title="Getting started with data deduplication in CluedIn"></iframe>
</div>

In this article, you will learn how to deduplicate the data that you have ingested into CluedIn and streamed to a Microsoft SQL Server database.

Deduplicating the data in CluedIn involves [creating a deduplication project](/Documentation/Getting-started/Deduplicate-data#create-deduplication-project), [configuring the matching rules](/Documentation/Getting-started/Deduplicate-data#configure-matching-rule) for identifying duplicates, and [fixing duplicates](/Documentation/Getting-started/Deduplicate-data#fix-duplicates).

**Prerequisites**

Before proceeding with the data deduplication process, ensure that you have completed the following tasks:

1. Ingested some data into CluedIn. For more information, see [Ingest data](/Documentation/Getting-started/Ingest-data).

1. Created a stream that keeps the data synchronized between CluedIn and the Microsoft SQL Server database. For more information, see [Stream data](/Documentation/Getting-started/Stream-data).

# Create deduplication project

As a first step, you need to create a deduplication project that allows you to check for duplicates that belong to a certain entity type.

**To create a deduplication project**

1. On the navigation pane, select **Management**. Then, select **Deduplication**.

1. On the **Actions** dashboard, select **Deduplication**.

    ![dedup-1.png](/.attachments/dedup-1-7dfb8b82-cc5e-41e1-9969-1dbe3cbfa456.png)

1. Select **Create Deduplication Project**.

1. On the **Create Deduplication Project** pane, do the following:

    1. Enter the name of the deduplication project.

    1. Select the entity type that you want to use as a filter for all records.

        ![dedup-2.png](/.attachments/dedup-2-b68f10a9-ae70-48c6-a307-ce4f307df6e6.png)

    1. In the lower-right corner, select **Create**.

        You created the deduplication project.

        ![dedup-3.png](/.attachments/dedup-3-bc125a51-f874-49af-a9d0-c49aea38bbb1.png)
    
        Now, you can proceed to define the rules for checking duplicates within the selected entity type.

# Configure matching rule

When creating a matching rule, you need to specify certain criteria that CluedIn uses to check for matching values among records that belong to the selected entity type.

**To configure a matching rule**

1. Go to the **Matching Rules** tab and select **Add Matching Rule**.

    The **Add Matching Rule** pane opens on the right side of the page.

1. On the **Matching Rule Name** tab, enter the name of the matching rule, and then select **Next**.

    ![dedup-4.png](/.attachments/dedup-4-1294d92b-9f47-4a33-a341-3dc7e1c7b98b.png)

1. On the **Matching Criteria** tab, do the following:

    1. Enter the name of the matching criteria.

    1. Select the vocabulary key. All values associated with this vocabulary key will be checked for duplicates.

    1. In the **Matching Function** dropdown list, select the method for detecting duplicates.

        ![dedup-5.png](/.attachments/dedup-5-9f45c436-0c33-429e-9821-925edff4365a.png)
    1. In the lower-right corner, select **Next**.

1. On the **Preview** tab, review the defined matching criteria.

    ![dedup-6.png](/.attachments/dedup-6-c5851686-18e2-4a26-97a5-ae09ccd5876e.png)

    If you want to add more matching criteria to the rule, select **Add Matching Criteria**.

    After you have added the needed matching criteria, in the lower-right corner of the **Preview** tab, select **Add Rule**.

    The status of the deduplication project becomes **Ready to generate**.

    ![dedup-7.png](/.attachments/dedup-7-d633647c-ce30-424a-9c45-4b7f5cde623b.png)

1. In the upper-right corner, select **Generate Results**. Then, confirm that you want to generate the results for the deduplication project.

    **Note:** The process of generating results may take some time.

    After the process is completed, you will receive a notification. If duplicates are detected, the results will be displayed on the page. The results are organized into groups containing records that match your criteria. For example, on the following screenshot, the group consists of two duplicates. The name of the group corresponds to the value of the vocabulary key from the matching rule. 

    ![dedup-8.png](/.attachments/dedup-8-6919fb78-f3b9-49aa-936d-462e62f16384.png)

    Now, you can proceed to fix the duplicates.

# Fix duplicates

The process of fixing duplicates involves reviewing the values from duplicate records and selecting which values you want to merge into the deduplicated record.

**To fix duplicates**

1. Select the name of the group.

    The **Fix Conflicts** tab opens. Here, you can view the details of the duplicate records. In the **Conflicting** section, you can find the properties that have different values in the duplicate records. In the **Matching** section, you can find the properties that have the same values in the duplicate records.

1. In the **Conflicting** section, select the values that you want to merge into the deduplicated record.

    ![dedup-9.png](/.attachments/dedup-9-f98a5052-4d6c-4971-9ddb-bd1010568ea1.png)

1. In the upper-right corner of the page, select **Next**.

    The **Preview Merge** tab opens. Here, you can view the values that will be merged into the deduplicated record.

    ![dedup-10.png](/.attachments/dedup-10-d537fd94-3ec4-45bd-a7b5-7d834becc306.png)

1. In the upper-right corner of the page, select **Approve**. Then, confirm that you want to approve your selection of values for the group.

1. Select the checkbox next to the group name. Then, select **Merge**.

    ![dedup-11.png](/.attachments/dedup-11-5c96bb34-3b30-4949-bb98-1288404b351f.png)

1. Confirm that you want to merge the records from the group:

    1. Review the group that will be merged and select **Next**.

    1. Select an option to handle the data merging process if more recent data becomes available for the entity. Then, select **Confirm**.

        ![dedup-12.png](/.attachments/dedup-12-09ec331a-2a78-4ce4-8ea5-116d5750c42d.png)

        **Note:** The process of merging data may take some time.

    After the process is completed, you will receive a notification. As a result, the duplicate records have been merged into one record.

    You fixed the duplicate records.

**Note:** All changes to the data records in CluedIn are tracked. You can search for the needed data record and on the **History** pane, you can view all actions associated with the record.

![dedup-13.png](/.attachments/dedup-13-23f52175-2d72-4732-8eaf-b50cb409db3c.png)

# Results

You have performed data deduplication in CluedIn.

# Next steps

_[TBD]_
