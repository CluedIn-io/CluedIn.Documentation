---
layout: cluedin
title: Work with glossary
parent: Getting started
permalink: /getting-started/glossary
nav_order: 80
tags: ["getting-started"]
---
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

Glossary can help you in documenting groups of records that meet specific criteria, simplifying the process of cleaning and streaming these groups of records.

<div class="videoFrame">
<iframe src="https://player.vimeo.com/video/853694351?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture"
title="Getting started with Glossary in CluedIn"></iframe>
</div>

In this article, you will learn how to work with the glossary in CluedIn. Glossary consists of terms that are grouped into categories. Each term contains a list of records that correspond to your conditions.

Working with the glossary in CluedIn includes creating categories and creating terms within those categories. You can have multiple terms under one category.

**Prerequisites**

Before proceeding with the glossary, ensure that you have completed the following tasks:

1. Ingested some data into CluedIn. For more information, see [Ingest data](/getting-started/data-ingestion).

1. Created a stream that keeps the data synchronized between CluedIn and the Microsoft SQL Server database. For more information, see [Stream data](/getting-started/data-streaming).

# Create category

Category refers to a logical grouping of terms. For example, you can have a category named **Customer**, which would contain customer records organized by regions. Each region is a separate term within the category. In other words, a category acts as a folder for terms.

**To create a category**

1. On the navigation pane, go to **Management** > **Glossary**.

1. Depending on whether or not you have created categories before, do one of the following:

    - If you haven't created any categories before, then in the middle of the page, select **Create Category**.

    - If you already created some categories, then, in the upper-left corner, select **Create** > **Create Category**. 

1. Enter the category name. Then, in the lower-right corner, select **Create**.

    ![create-category-1.png](../../assets/images/getting-started/glossary/create-category-1.png)

    You created the category. Now, you can create a term in the category.

# Create term

Term refers to the list of records that meet specific conditions. For example, within the **Customer** category, you can have a term named **North America** encompassing customer records where the **BusinessRegion** vocabulary key is set to **North America**. 

**To create a term**

1. Select **Create Term**.

1. On the **Create Term** pane, do the following:

    1. Enter the term name.

    1. In the **Category** section, leave the **Choose an existing Category** checkbox selected.

    1. Select the category that you created.

        ![create-term-1.png](../../assets/images/getting-started/glossary/create-term-1.png)

    1. In the lower-left corner, select **Create**.

        You created the term. Now, proceed to define the records that will be included in this term.

1. In the upper-right corner of the term details page, select **Edit**.

1. On the **Configuration** tab, in the **Conditions** section, select **Add first rule**, and then specify which records will be included in the term:

    1. Select the type of property (**Property** or **Vocabulary**).

    1. Depending on the type of property that you selected, do one of the following:

        For **Property**, find and select the needed property.

        For **Vocabulary**, find and select the needed vocabulary key.

    1. Select the operation.

    1. Select the value of the property.

        ![create-term-2.png](../../assets/images/getting-started/glossary/create-term-2.png)

        **Note:** The fields for configuring a filter appear one by one. After you complete the previous field, the next field appears.

1. (Optional) Specify additional details about the term:

    1. In the **Certification Level** dropdown list, select the quality level of the records.

    1. Enter the **Short Description** and **Long Description** of the term.

        ![create-term-3.png](../../assets/images/getting-started/glossary/create-term-3.png)

1. In the upper-right corner of the term details page, select **Save**.

1. Go to the **Matches** tab to view the records that meet the condition that you set up.

    By default, all records are displayed in the following columns: **Name**, **Entity Type**, and **Description**. To add more columns to the table, see step 3 of [Find data](/getting-started/manual-data-cleaning#find-data).

1. Activate the term by turning on the toggle next to the term status.

    ![create-term-4.png](../../assets/images/getting-started/glossary/create-term-4.png)

    You created the term and defined the records that are included in this term.

Now, you can clean the glossary term and stream it to a Microsoft SQL Server database. As an example, [update the configuration of the stream](#update-stream-configuration) that you created in the [Stream data](/getting-started/data-streaming) guide.

# Manage glossary

You can do the following actions with the terms in the glossary:

- Endorse the term when you are confident that the records are of good quality, signaling to other users that the term is reliable for their use. To do that, in the upper-right corner of the term page, select **Endorse**.

    ![manage-glossary-1.png](../../assets/images/getting-started/glossary/manage-glossary-1.png)

- Rate the term, enabling other users to view that it is reliable for their use.

    ![manage-glossary-2.png](../../assets/images/getting-started/glossary/manage-glossary-2.png)

# Update stream configuration

Streaming the glossary terms to the database is more convenient than streaming specific records based on filters. You only need to specify the name of the glossary term, rather than setting filters for properties or vocabulary values.

**To update the stream**

1. On the navigation pane, go to **Consume** > **Streams**.

1. Open the needed stream.

1. On the **Configuration** page, in the **Filters** section, delete the existing filter.

1. Select **Add First Filter**, and then specify the glossary term that you created:

    1. In the **Select Property Type** dropdown list, select **Glossary**.

    1. In the **All Glossary** dropdown list, select the glossary term that you created.

    1. In the **Choose Operation** dropdown list, select **Is True**.

        ![update-stream-configuration-1.png](../../assets/images/getting-started/glossary/update-stream-configuration-1.png)

1. In the upper-right corner select **Save**. Then, confirm that you want to save your changes.

    The stream is updated with the new filter. As a result, the database table now contains the records from the glossary  term.

    If you update the glossary term, the records will be automatically updated in the database.

# Results

You created a glossary term in CluedIn.

# Next steps

- [Add relations between golden records](/getting-started/relations)