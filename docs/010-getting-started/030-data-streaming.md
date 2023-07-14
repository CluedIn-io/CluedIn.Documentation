---
layout: default
title: Stream data
parent: Getting Started
permalink: /getting-started/data-streaming
nav_order: 20
tags: ["getting-started"]
---
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

Streaming data from CluedIn involves setting up an export target and creating a stream.

In this article, you will learn how to stream your records from CluedIn to a Microsoft SQL Server database.

# Set up export target

An export target is a place where you can send the data out of CluedIn after it has been processed. In the following procedure, we are going to establish a connection with a Microsoft SQL Server database to use it as an export target.

**To set up an export target**

1. On the navigation pane, select **Consume**. Then, select **Export Targets**.

1. Select **Add Export Target**.

1. On the **Add Export Target** pane, do the following:

    1. On the **Choose Target** tab, find and select **Sql Server Connector**. Then, in the lower-right corner, select **Next**.

        ![add-export-target-1.png](/.attachments/add-export-target-1-32210507-75b9-4dd2-ba38-f2e8f19d97f1.png)

    1. On the **Configure** tab, enter the database connection details such as **Host**, **Database Name**, **Username**, and **Password**. Optionally, you may add **Port Number** and **Schema**.

        ![add-export-target-2.png](/.attachments/add-export-target-2-dc764dbc-8612-45fa-b11b-11f933a64983.png)

    1. In the lower-right corner, select **Test Connection**. After you receive a notification that the connection is successful, select **Add**.

        The export target is added.

        ![add-export-target-3.png](/.attachments/add-export-target-3-b278e900-9666-4e3c-b7ab-0d493a739968.png)

Now, you can create a stream.

# Create stream

A stream is a trigger that starts the process of sending the data to the export target. In the following procedure, we are going to configure the stream and define the data records that will be streamed to a Microsoft SQL Server database.

**To create a stream**

1. On the navigation pane, select **Consume**. Then, select **Streams**. 

1. Select **Create Stream**.

1. On the **Create Stream** pane, enter the **Stream Name**, and then select **Create**.

    ![create-stream-1.png](/.attachments/create-stream-1-186a5bb2-71f0-45e8-bad1-2351f9950bf9.png)    

    The stream details page opens.

1. On the **Configuration** tab, in the **Filters** section, select **Add First Filter**, and then specify what data you want to share:

    1. Select the property type (**Property**). 

    1. Select the property (**Entity Type**).

    1. Select the operation (**Equals**).

    1. Select the value of the entity type.

        **Note:** The fields for configuring a filter appear one by one. After you complete the previous field, the next field appears.

        ![create-stream-2.png](/.attachments/create-stream-2-73460fb4-fcd9-4494-86e8-29b929a89a41.png)

1. In the upper-right corner of the stream details page, select **Save**. Then, confirm that you want to save changes.

    On the **Preview Condition** tab, you can view all the data that will be streamed to the database.

    ![create-stream-3.png](/.attachments/create-stream-3-337c00aa-a57d-4491-846c-c095a326672b.png)

1. Go to the **Export Target Configuration** tab, and then specify the target where the data will be sent:

    1. On the **Choose connector** tab, select **Sql Server Connector**. Then, select **Next**.

        ![create-stream-4.png](/.attachments/create-stream-4-3346c0e1-f7f3-4dfb-af30-65ba6e46ec2f.png)

    1. On the **Properties to export** tab, enter the **Target name**.

        The target name that you enter will be the name of the table in the database.

    1. Select the **Streaming mode**.

        Two streaming modes are available:

        - **Synchronized stream** – the database and CluedIn contain the same data that is synchronized. For example, if you edit the record in CluedIn, the record is also edited in the database. 

        - **Event log stream** – every time you make a change in CluedIn, a new record is added to the database instead of replacing the existing record.

        ![create-stream-5.png](/.attachments/create-stream-5-bb1e74a5-24f2-4216-a49d-f39f6061500e.png)
  
    1. In the **Properties to export** section, select **Add Property** > **Add Vocabulary Property**.

        ![create-stream-6.png](/.attachments/create-stream-6-a297e9bc-3ede-4270-b9a9-70544c5efa50.png)

    1. In the search field, enter the name of the vocabulary, and start the search. In the search results, select the needed vocabulary keys that will be added as columns in the database table. Then, select **Add Vocabulary Columns**.

        ![create-stream-7.png](/.attachments/create-stream-7-8b6b3dcd-adf8-40c4-b394-091389d230f2.png)

    1. In the lower-right corner, select **Add Vocabulary Columns**.

    1. Select **Save**.

1. Go to the **Data** tab and review the data that will be shared with the export target.

    ![create-stream-8.png](/.attachments/create-stream-8-784a53d8-2659-49fd-8e41-1f3603e03f79.png)

    Currently, the stream is inactive.

1. Start the stream by turning on the toggle next to the stream status. Then, confirm that you want to activate the stream.

    The **Inactive Stream** label disappears, and the stream status is changed to **Active**.

    ![create-stream-9.png](/.attachments/create-stream-9-4b88e12d-d316-493f-8c71-870f5473ebf6.png)

    **Note:** On the **Monitoring** tab, you can view different data performance metrics.

1. Go to the database and open the table.

    ![create-stream-11.png](/.attachments/create-stream-11-23e0426e-f3ab-44a8-bace-1e43b071a13b.png) 

    The records have been streamed to the target database.

# Results

You have streamed your records from CluedIn to a Microsoft SQL Server database.

# Next steps

- Clean data (add link)