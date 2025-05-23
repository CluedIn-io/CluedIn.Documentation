---
layout: cluedin
nav_order: 040
parent: Data sources
grand_parent: Ingestion
permalink: /integration/database
title: Database
tags: ["integration"]
last_modified: 2024-01-15
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article, you will learn how to ingest data from a database into CluedIn.

You can ingest the database tables to CluedIn if you have the **read permission** to these database tables. The process of ingesting data from the database involves two steps:

1. [Adding connection to the database](#add-connection-to-database)

2. [Ingesting the database tables](#ingest-database-tables)

{:.important}
The maximum number of columns accepted for data ingestion is 490.<br>Before loading data into CluedIn, ensure that it does not contain unsupported characters. Refer to our knowledge base [article](/kb/supported-characters) for information about supported and unsupported characters.

**Prerequisites**

To be able to ingest the data from a database, go to **Administration** > **Feature Flags** and make sure that the **Import databases in Data Source module** feature is enabled.

## Add connection to database

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

## Ingest database tables

With an established connection to the database, you can choose which database tables you want to ingest into CluedIn.

**To ingest database tables**   

1. Open the data source, and then select **Add new table**.

    The **Add data table** pane opens, where you can view all tables existing in the database.

1. Select the checkboxes next to the tables you want to ingest into CluedIn. Then, in the lower-right corner, select **Add**.

    The tables are added to CluedIn. Each table is added as a separate data set. Next, [create mapping](/integration/create-mapping) and [process data](/integration/process-data).