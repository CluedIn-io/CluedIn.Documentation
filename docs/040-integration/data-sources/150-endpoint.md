---
layout: cluedin
nav_order: 030
parent: Data sources
grand_parent: Integration
permalink: /integration/endpoint
title: Endpoint
tags: ["integration"]
last_modified: 2024-10-31
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article, you will learn how to ingest data into CluedIn using an endpoint. This method is a default solution to push your data easily into CluedIn, especially if you are using tools like Azure Data Factory, Databricks, or Apache NiFi.

<div class="videoFrame">
<iframe src="https://player.vimeo.com/video/896475765?h=8f20829bc2&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" title="Using an endpoint for data ingestion"></iframe>
</div>

The process of ingesting data using an endpoint involves two steps:

1. [Adding an ingestion point](#add-ingestion-point)

1. [Sending data in HTTP POST request](#send-data)

{:.important}
Before loading data into CluedIn, ensure that it does not contain unsupported characters. Refer to our knowledge base [article](/kb/supported-characters) for information about supported and unsupported characters.

## Overview of data ingestion using an endpoint

When you need to push a large set of records into CluedIn, we recommend that you start by pushing a small, representative subset of your data. As with files, this approach allows you to verify the accuracy of mapping and relations before pushing a large set of records. Once the golden records generated from this subset align with your expectations, you can safely remove those records from the system, while keeping the mapping configuration intact. After that you can push a large set of records and use the existing mapping to generate golden records in an efficient way.

After you send an HTTP POST request, CluedIn checks if it is correct based on the built-in logic and limitations. If your JSON is completely invalid, CluedIn won't start ingesting the data, and you'll receive a response with the status "400 Bad Request". The response body will include an array of errors that provide context for fixing them. Once you correct the request, you can try sending it again.

![endpoint-error.png](../../assets/images/integration/data-sources/endpoint-error.png)

If your JSON contains issues, such as spaces or dots in property names, CluedIn tries to fix them and store the data. These issues are treated as warnings and they are recorded on the **Logs** tab of the data set. You'll receive a response with the status "200 OK", which means that the data has been successfully sent to CluedIn. However, the response body will include an array of warnings explaining how the issues were fixed. 

![endpoint-warning.png](../../assets/images/integration/data-sources/endpoint-warning.png)

Once CluedIn receives the data, it initially stores it in a temporary storage, accessible through the **Preview** tab. To turn the received data into golden records, you need to map it to the semantic model and then process it.

(For advanced users) To ensure the creation of the expected golden records, you can generate a sample clue and verify its accuracy before processing. This step helps confirm that the resulting golden record aligns with your expectations. For more information, see [Clue](/key-terms-and-features/clue-reference).

## Processing options for data received via an endpoint

CluedIn provides the following processing options for turning your data into golden records:

- **Manual processing** - when CluedIn receives the data from the endpoint, you are required to process the data manually. You can view the received data in the temporary storage at any time, and you can process the data set as many times as you need. In CluedIn, once a record has been processed, it won't undergo processing again. When you trigger processing, CluedIn will check for identical records. If identical records are found, they won't be processed again. However, if you change the origin code for the previously processed records, CluedIn will treat these record as new and process them.

- **Automatic processing** - when CluedIn receives the data from the endpoint, this data is processed automatically. You can view the received data in the temporary storage at any time.

- **Bridge mode** – all your JSON records will be transformed into golden records directly, without being stored in the temporary storage. However, you can rely on rely on data set logs for debugging purposes.

    Bridge mode allows you to use less storage and memory, resulting in increased performance. Use this mode when your mapping will not change over time and you want to use the ingestion endpoint only as a mapper.

{:.important}
When you send the data to CluedIn via ingestion point, a separate data set is created. If you want to send more data, add a new ingestion point instead of reusing the existing one.

## Add ingestion point

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

## Send data

In this section, Postman is used as a tool to demonstrate how to send an HTTP POST request to CluedIn.

**Prerequisites**

To be accepted by CluedIn, your HTTP POST request should meet the following prerequisites:

- The request's header must contain Authorization key with the value set to _Bearer <API token>_. It is very important to include the word _Bearer_ followed by a space before pasting the API token. You can find the API token in CluedIn in **Administration** > **API Tokens**.

    ![ingest-data-6.png](../../assets/images/integration/data-sources/ingest-data-6.png)

- The request's body should contain **raw data in JSON format**.

    ![ingest-data-2.png](../../assets/images/integration/data-sources/ingest-data-2.png)

- The **content-type** in the request's header should be set to **application/json**.

    ![ingest-data-3.png](../../assets/images/integration/data-sources/ingest-data-3.png)
 
**To send data to CluedIn**

1. In CluedIn, open the data set that was created in the [previous procedure](#add-ingestion-point), and then select **View instructions**.

    On the **Ingestion point instructions** pane, find and copy the POST URL that you can use to send data to CluedIn.

    ![ingest-data-4.png](../../assets/images/integration/data-sources/ingest-data-4.png)

1. In Postman, paste the URL that you copied to the URL input field of your request. Then, send the request.

    The data has been sent to CluedIn. You can now view it on the [Preview](/integration/additional-operations-on-records/preview) tab of the data set. The next steps involve [creating a mapping](/integration/create-mapping) and [processing the data](/integration/process-data).