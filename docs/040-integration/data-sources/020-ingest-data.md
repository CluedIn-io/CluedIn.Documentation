---
layout: default
nav_order: 2
parent: Integration
permalink: /integration/ingest-data
title: Ingest data
tags: ["integration"]
last_modified: 2023-11-07
---
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

In this article, you will learn how to ingest the data into CluedIn from files, from an ingestion point, and from a database.

## Files

You can ingest data from CSV, JSON, XLS, and XLSX files. 

**To ingest data from files**

1. On CluedIn home page, in the **Integrations** section, select **Import from files**.

1. In the **Add files** section, either drag the file or choose it from your computer. You can upload up to 5 files at once, and the total file size should not exceed 1 GB.

1. Specify the **Group** where the data source will be stored. You can choose the existing group or create a new group. If you upload several files, they will be stored as separate data sources within a group.

1. In the lower-right corner, select **Upload**.

    The data has been sent to CluedIn. You can now view it on the [Preview](#preview) tab of the data set. The next steps involve [creating a mapping](/Documentation/Integrations/Create-mapping) and [processing the data](/Documentation/Integrations/Process-data).

## Ingestion point

You can ingest a JSON array to an HTTP endpoint created by CluedIn. The process of ingesting data from an ingestion point involves two steps:

1. [Adding an ingestion point](#add-ingestion-point)

1. [Sending data in HTTP POST request](#send-data)

### Add ingestion point

An ingestion point is a channel through which CluedIn can receive data from external sources.

**To add an ingestion point**

1. On CluedIn home page, in the **Integrations** section, select **Import from ingestion point**.

    The **Import from ingestion point** pane opens, where you can choose the group for storing the data source and define preliminary mapping configuration.

1. On the **Configure** tab,  do the following:

    1. Enter the **Name** of the data source.

    1. Specify the **Group** where the data source will be stored. You can choose the existing group or create a new group.

    1. In the lower-right corner, select **Next**.

1. On **Add ingestion point** tab, do the following:

    1. Enter the **Endpoint name** that will be used as the name of the data set.

    1. Select the **Mapping configuration** option:

        - **New mapping** – you can create a new mapping for the data set. If you choose this option, you need to select the existing entity type or create a new one. If you create a new entity type, select an icon to visually represent the entity type.

        - **Existing mapping** – you can reuse the mapping from the data set that has the same structure. If you choose this option, you need to indicate the data set with the required mapping configuration. To do that, choose the following items one by one: a data source group, a data source, and a data set.

    1. In the lower-right corner, select **Add**.

    The ingestion point is added to CluedIn. It has a label **No data sent**, which indicates that CluedIn has not received data for this ingestion point.

    ![ingest-data-1.png](../../assets/images/integration/data-sources/ingest-data-1.png)

    Now, you can send data to CluedIn by creating HTTP POST requests.

### Send data

In this section, Postman is used as a tool to demonstrate how to send an HTTP POST request to CluedIn.

**Prerequisites**

To be accepted by CluedIn, your HTTP POST request should meet the following prerequisites:

- The request's authorization type should be set to **Bearer Token** and the value should be a valid API token from CluedIn. You can find the API token in CluedIn in **Administration** > **API Tokens**.

- The request's body should contain **raw data in JSON format**.

    ![ingest-data-2.png](../../assets/images/integration/data-sources/ingest-data-2.png)

- The **content-type** in the request's header should be set to **application/json**.

    ![ingest-data-3.png](../../assets/images/integration/data-sources/ingest-data-3.png)
 
**To send data to CluedIn**

1. In CluedIn, open the data set that was created in the [previous procedure](#add-an-ingestion-point), and then select **View instructions**.

    On the **Ingestion point instructions** pane, find and copy the POST URL that you can use to send data to CluedIn.

    ![ingest-data-4.png](../../assets/images/integration/data-sources/ingest-data-4.png)

1. In Postman, paste the URL that you copied to the URL input field of your request. Then, send the request.

    The data has been sent to CluedIn. You can now view it on the [Preview](#preview) tab of the data set. The next steps involve [creating a mapping](/Documentation/Integrations/Create-mapping) and [processing the data](/Documentation/Integrations/Process-data).

## Database

You can ingest the database tables to CluedIn if you have the **read permission** to these database tables. The process of ingesting data from the database involves two steps:

1. [Adding connection to the database](#add-connection-to-database)

2. [Ingesting the database tables](#import-database-tables)

**Prerequisites**

To be able to ingest the data from a database, go to **Administration** > **Feature Flags** and make sure that the **Import databases in Data Source module** feature is enabled.

### Add connection to database

To be able to access the database tables in CluedIn, first establish a connection to the database.

**To add a connection to the database**

1. On CluedIn home page, in the **Integrations** section, select **Import from database**.

    The **Import from database** pane opens, where you can provide the database connection details and choose the group for storing the data source.

1. On the **Connection string** tab, do the following:

    1. Choose the **SQL database technology** to query the data (Microsoft SQL Server, MySQL, or Postgres).

    1. Enter the database connection details such as **Host**, **Database name**, **Username**, and **Password**. Optionally, you may add **Port number**.

    1. In the lower-right corner, select **Test connection**. After you receive a notification that the connection is successful, select **Next**.

1. On the **Configure** tab, do the following:

    1. Enter the **Name** of the data source.

    1. Specify the **Group** where the data source will be stored. You can choose the existing group or create a new group.

    1. In the lower-right corner, select **Add**.

    The database connection is added to CluedIn.

    ![ingest-data-5.png](../../assets/images/integration/data-sources/ingest-data-5.png)

    Now, you can add database tables to CluedIn.

### Ingest database tables

With an established connection to the database, you can choose which database tables you want to ingest into CluedIn.

**To ingest database tables**   

1. Open the data source, and then select **Add new table**.

    The **Add data table** pane opens, where you can view all tables existing in the database.

1. Select the checkboxes next to the tables you want to ingest into CluedIn. Then, in the lower-right corner, select **Add**.

    The tables are added to CluedIn. Each table is added as a separate data set. Next, [create mapping](/Documentation/Integrations/Create-mapping) and [process data](/Documentation/Integrations/Process-data).

## Preview

After you ingest the data, it is displayed on the **Preview** tab as a table.

If you want to focus on specific columns and hide the others, select **Column Options**, and then clear the checkboxes next to the columns that you want to hide from the table.

After you create the mapping for the data set, each column header will contain the vocabulary key to which the original field is mapped. You can view the number of duplicates in each field.

**To view duplicates**

- In the column header, select the vertical ellipsis button, and then select **View duplicates**.

    The **Duplicates Preview** pane opens, where you can view the following information:

    - Number of duplicates in the data set.

    - Which values are duplicates.

    - Occurrences of duplicates – for each duplicate value, the pane displays how many times it occurs within the data set.