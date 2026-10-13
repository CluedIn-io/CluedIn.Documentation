---
title: Tutorial: stream data
url: https://documentation.cluedin.net/publish/streams/tutorial-stream-data
content_type: tutorial
section: Publish & consume > Streams
---

# Tutorial: stream data

> tutorial: Guided end-to-end learning.

Streaming data from CluedIn involves setting up an export target and creating a stream.

In this guide, you will learn how to stream your records from CluedIn to a Microsoft SQL Server database.

**Before you start:** Make sure you have completed all steps in the [Ingest data guide](https://documentation.cluedin.net/ingest/tutorial-ingest-data.md).

## Set up an export target

An export target is a place where you can send the data out of CluedIn after it has been processed. In the following procedure, we are going to establish a connection with a Microsoft SQL Server database to use it as an export target.

**To set up an export target**

1. On the navigation pane, go to **Consume** > **Export Targets**.

1. Select **Add Export Target**.

1. On the **Choose Target** tab, find and select **Sql Server Connector**. Then, select **Next**.

    ![The Add Export Target dialog on the Choose Target tab, with a search for sql server returning the Sql Server Connector](https://documentation.cluedin.net/assets/images/getting-started/data-streaming/add-export-target-1.png)

1. On the **Configure** tab, enter the database connection details such as **Name**, **Host**, **Database Name**, **Username**, and **Password**. Optionally, you may add **Port Number**, **Schema**, and **Connection pool size**.

    ![The Configure tab of the Add Export Target dialog with Name, Host, Database Name, Username, and Password filled in](https://documentation.cluedin.net/assets/images/getting-started/data-streaming/add-export-target-2.png)

1. Select **Test Connection**. After you receive a notification that the connection is successful, select **Add**.

    The export target is added.

    ![The Export Targets list showing the new SQL Server target with Synchronized and Event stream modes, Active status, and Healthy health](https://documentation.cluedin.net/assets/images/getting-started/data-streaming/add-export-target-3.png)

    Now, you can create a stream.

## Create a stream

A stream is a trigger that starts the process of sending the data to the export target. In the following procedure, we are going to configure the stream and define the records that will be streamed to a Microsoft SQL Server database.

**To create a stream**

1. On the navigation pane, go to **Consume** > **Streams**. 

1. Select **Create Stream**.

1. Enter the **Stream Name**, and then select **Create**. 

    The stream details page opens.

1. On the **Configuration** tab, in the **Filters** section, select **Add First Filter**, and then specify what data you want to share.

    ![The stream Filters section with one rule: Property, Business domain, Equals, with the value TrainingContact](https://documentation.cluedin.net/assets/images/getting-started/data-streaming/create-stream-2.png)

    The fields for configuring a filter appear one by one. After you complete the previous field, the next field appears.

1. Select **Save**. To view the records that match stream filters, go to the **Preview Condition** tab.

1. Go to the **Export Target Configuration** tab.

1. On the **Choose Connector** tab, select the Sql Server connector, and then select **Next**.

    ![The Export Target Configuration tab of the Training stream on the Choose connector step, with the SQL Server export target selected](https://documentation.cluedin.net/assets/images/getting-started/data-streaming/create-stream-4.png)  

1. On the **Connector Properties** tab, do the following:

    1. Enter the **Target Name**. This will be the name of the table in the database.

    1. Select the **Streaming Mode**. Two streaming modes are available:

        - **Synchronized stream** – the database and CluedIn contain the same data that is synchronized. For example, if you edit the record in CluedIn, the record is also edited in the database. 

        - **Event log stream** – every time you make a change in CluedIn, a new record is added to the database instead of replacing the existing record.

        ![Connector properties with Target name set to Training and Streaming Mode set to Synchronized stream](https://documentation.cluedin.net/assets/images/getting-started/data-streaming/create-stream-5.png)  

1. On the **Properties to Export** tab, click **Auto-select**. All vocabulary keys associated with the records in the strem filter will be displayed on the page.

    ![The Properties to export section after Auto-select, listing trainingcontact vocabulary keys such as email, firstName, id, jobTitle, and lastName](https://documentation.cluedin.net/assets/images/getting-started/data-streaming/create-stream-6.png)  

1. Select **Save**. To view the data that will be sent to the database, go to the **Data** tab.

1. Start the stream by selecting the play button. Then, confirm that you want to start the stream.

    ![The Training stream details page with the Start button highlighted next to Pause, Stop, and Edit](https://documentation.cluedin.net/assets/images/getting-started/data-streaming/create-stream-9.png)

    The **Streaming** and **Exporting** labels appear under the stream name, indicatig that the stream is active.

    ![The Training stream header showing the Streaming and Exporting labels under the stream name](https://documentation.cluedin.net/assets/images/getting-started/data-streaming/create-stream-10.png)

    On the **Monitoring** tab, you can view different data performance metrics.

1. Go to the database and open the table.

    ![A SQL query on the dbo.Training table in the export database, with results showing streamed records and trainingcontact columns](https://documentation.cluedin.net/assets/images/getting-started/data-streaming/create-stream-11.png)  

    The records have been sent to the database.

## Results & next steps

After completing all steps outlined in this guide, you learned how to configure the connection to a Microsoft SQL Server database and how to send data from CluedIn to the database. If you make any changes to the records in CluedIn, they will be automatically updated in the database. For example, if you fix the job title values in CluedIn, they will be automatically corrected in the database.

Next, learn how to create rules for automating data transformation and capturing data quality issues in the [Create rules guide](https://documentation.cluedin.net/govern/rules/tutorial-create-rules.md).

Up: [Streams](https://documentation.cluedin.net/publish/streams.md)
