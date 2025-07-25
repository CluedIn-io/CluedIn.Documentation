---
layout: cluedin
title: Ingest data
parent: Getting started
permalink: getting-started/data-ingestion
nav_order: 20
tags: ["getting-started"]
---
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

Ingesting data to CluedIn involves three basic steps: importing, mapping, and processing data. As a result, your records will become searchable and ready to be cleaned, deduplicated, and streamed.

<div class="videoFrame">
<iframe src="https://player.vimeo.com/video/843840937?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen title="Getting started with data ingestion in CluedIn"></iframe>
</div>

In this guide, you will learn how to import a file into CluedIn, create a mapping, process the data, and search for golden records.

**File for practice:** <a href="../../../assets/other/training-data.csv" download>training-data.csv</a>

## Import file

The easiest way to add data to CluedIn is to import a file. In the following procedure, we will import a CSV file containing 500 records.

A CSV (comma-separated values) file format allows data to be saved in a tabular format, making it compatible with most spreadsheet programs such as Excel. So, if you are using Excel for your data analysis or management tasks, importing a CSV file is a convenient option.

**To import a file**

1. On the navigation pane, go to **Ingestion**, and then in the **Files** section, select **Add**.

    ![files-add.png]({{ "/assets/images/getting-started/data-ingestion/files-add.png" | relative_url }})

1. In the **Add Files** section, add the file. You may drag the file or select the file from the computer.

1. In the **Group** section, leave the default **Create new group** option selected, and then enter the name of the group.

    A group indicates a department or domain within your company that is associated with the data. Think of a group as a folder where you can store files related to similar types of data.

    ![import-a-file-2.png]({{ "/assets/images/getting-started/data-ingestion/import-a-file-2.png" | relative_url }})

1. Select **Upload**.

## View imported data

After you uploaded the file, you can view the data from the file as a table with columns and rows.

**To view imported data**

1. On the navigation pane, go to **Ingestion** > **Sources**.

1. Find and expand the group that you created in the previous procedure.

1. Expand the element contained in the group. This element is called a data source; think of a data source as a database.

1. Select the element contained in the data source. This element is called a data set; think of a data set as a table in the database.

    ![view-imported-data-1.png]({{ "/assets/images/getting-started/data-ingestion/view-imported-data-1.png" | relative_url }})

    The data set details page opens, where you can view imported data.

The data is parsed and stored in CluedIn, but it is not yet been processed.

**What does it mean if the data is not processed?**

Unprocessed data is not available for any data management tasks. What is more, if you try to search for data, the results won't return any records. This is because the data is not yet visible for CluedIn. To make the data available for use within CluedIn, you need to create a mapping and process the data.

## Create mapping

Mapping is the process of creating a semantic layer for your data so that CluedIn understands it. This process involves the mapping of original fields to standard fields as well as assigning appropriate data types.

**To create a mapping**

1. On the data set details page, select the **Missing Mapping** label.

    ![create-mapping-1.png]({{ "/assets/images/getting-started/data-ingestion/create-mapping-1.png" | relative_url }})

    Alternatively, go to the **Map** tab.

1. In the middle of the page, select **Map Data**.

1. In **Mapping Type**, leave the default **Auto Mapping** option selected.

    ![create-mapping-2.png]({{ "/assets/images/getting-started/data-ingestion/create-mapping-2.png" | relative_url }})

1. Select **Next**.

1. In **Business Domain**, enter the name of a new business domain and select **Create**. A business domain is a specific business object within the organization. A well-named business domain is global and should not be changed (for example, Person, Organization, Car) across sources.

    The **Business Domain Identifier** is created automatically; it is a string that represents the business domain in code (for example, in clues).

1. In **Icon**, select the visual representation of the business domain.

    ![create-mapping-3.png]({{ "/assets/images/getting-started/data-ingestion/create-mapping-3.png" | relative_url }})

1. In **Vocabulary**, enter the name of a new vocabulary and select **Create**. A vocabulary is a structured framework for creating a unified view of your data. The purpose of vocabulary is to translate your original fields to the language CluedIn understands.

    The **Key prefix** is created automatically; it is added before the original field names to establish consistent and well-organized standard fields.

    ![create-mapping-4.png]({{ "/assets/images/getting-started/data-ingestion/create-mapping-4.png" | relative_url }})

1. In **Primary Identifier**, review the field that was selected automatically for generating a unique identifier for each record.

    ![create-mapping-5.png]({{ "/assets/images/getting-started/data-ingestion/create-mapping-5.png" | relative_url }})

1. In **Preview**, review the mapping of original fields to standard fields. You can edit the names of standard fields that come after the key prefix, and you can change the data type if needed.

    ![create-mapping-6.png]({{ "/assets/images/getting-started/data-ingestion/create-mapping-6.png" | relative_url }})

 1. Select **Create Mapping**.

    As a result of the mapping process, you can view how the fields from the file are linked to the standard fields in CluedIn.

    ![create-mapping-7.png]({{ "/assets/images/getting-started/data-ingestion/create-mapping-7.png" | relative_url }})

## Process data

Processing turns your data into golden records that can be cleaned, deduplicated, and streamed.

**To process data**

1. On the data set details page, select the **Not Processed** label.

    ![process-data-1.png]({{ "/assets/images/getting-started/data-ingestion/process-data-1.png" | relative_url }})

    Alternatively, go to the **Process** tab.

1. Select **Process**.

1. Review information about records that will be processed. Pay attention to the **Primary Identifier Status** section. If there are duplicates, they will be merged during processing.

    ![process-data-2.png]({{ "/assets/images/getting-started/data-ingestion/process-data-2.png" | relative_url }})

1. Select **Confirm**.

    After the records are processed, you can view the resulting golden records on the **Data** tab.

## Search for data

After the data has been processed, you can search for any property and view all golden records where it is used. In the following procedure, we will use the email address as an input to search for data.

**To search for data**

1. On the **Preview** tab of the data set, copy any email address.

1. Paste the email address in the search field, and then select the search icon.

    ![search-for-data-1.png]({{ "/assets/images/getting-started/data-ingestion/search-for-data-1.png" | relative_url }})

1. On the search results page, select the name of the record.

1. On the golden record details page, go to the **Properties** tab. Here, you can view all the properties of the golden record.

    ![search-for-data-2.png]({{ "/assets/images/getting-started/data-ingestion/search-for-data-2.png" | relative_url }})

## Results & next steps

In this guide, you learned how to import data into CluedIn using a file, create auto-mapping, process the data, and perform data searches. After completing all steps outlined here with our practice file, you now have 500 golden records in the system. With these golden records, you can perform various data management tasks.

In the following guides, you'll find detailed instructions about common data management tasks. If you find errors in your golden records, such as misspelled job titles or emails, you can fix them using the clean functionality. To learn how to do it, go to the next guide, [Clean data](/getting-started/manual-data-cleaning).