---
layout: default
nav_order: 1
parent: Streams
grand_parent: Consume
permalink: /consume/streams/create-a-stream
title: Create a stream
tags: ["consume", "streams"]
last_modified: 2024-01-16
---
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

In this section, you will learn how to set up a live stream of golden records from CluedIn to a specific external target (for example, a Microsoft SQL Server database).

**Prerequisite:** Make sure you have added and configured the connection to the export target where you want to send the records from CluedIn. For more information, see [Export targets](/consume/export-targets).

## Create a stream

The first step to send the records from CluedIn to an export target is to create a stream and define what golden records you want to share.

**To create a stream**

1. On the navigation pane, go to **Consume** > **Streams**.

1. Select **Create Stream**. Enter the name of the stream, and then select **Create**.

    The stream details page opens, where you can configure the stream and the export target for the stream, as well as view all stream-related data.

1. In the **Filters** section, select **Add First Filter**, and then specify which records you want to send to the export target. For more information on how to set up a filer, see [Filters](/key-terms-and-features/filters).

    **Note:** If you want to view the records matching the filter, select **Preview Condition**.

1. If you want to modify the records before sending them to the export target—for example, mask certain values—you can do it in the **Actions** section. Select **Add Action**, and then configure the action that will be performed on the records matching the stream's filter. For more information about the available actions, see [Actions in data part rules](/management/rules/rules-reference#actions-in-data-part-rules). You can add multiple actions.

    **Important:** The changes applied by the actions do not affect the records stored in CluedIn, only the records that will be sent to the export target.

    ![streams-2.png](../../assets/images/consume/streams/streams-2.png)

1. (Optional) In the **Description** section, enter the details about the stream.

1. In the upper-right corner of the stream details page, select **Save**.

    You created the stream. Next, configure the export target for the stream and select which properties from the golden records will be shared.

## Configure an export target

You can configure the export target for the stream on the **Export Target Configuration** tab of the stream details page.

**To configure the export target for the stream:**

1. On the **Choose connector** tab, select the connection to an external system where the records will be sent. Then, near the upper-right corner, select **Next**.

    ![streams-3.png](../../assets/images/consume/streams/streams-3.png)

    The **Properties to export** tab opens, where you can provide other configuration details and select which properties from a record you want to send to the target.

1. In the **Target name** field, enter the name of the container that will receive the records sent from CluedIn. For example, in SQL databases this container is a table and in Elasticsearch databases it is the index.

1. In the **Streaming mode** section, select the option for sending the records to the export target:

    - Synchronized stream – select this option if you want the records in the export target to mirror the records in CluedIn.

    - Event log stream – select this option if you want to send data as events (for example, Create, Insert, Update, Delete) each time an action occurs in CluedIn.

1. In the **Export edges** section, select whether you want to send the linked data together with the golden records:

    - Outgoing – turn on this toggle if you want to send the data for which the stream's records are the target.

    - Incoming – turn on this toggle if you want to send the data for which the stream's records are the source.

1. In the **Properties to export** section, select which properties of the golden records you need to send to the export target.

    By default, certain properties of the golden records will be sent to the export target. These default properties depend on the export target (for example, for SQL Server Connector the default properties include Id, PersistVersion, PersistHash, OriginEntityCode, EntityType, Timestamp). However, you can send other properties as well. To do that, select **Add Property** > **Add Entity Property**, and then select the needed properties. In a similar way, you can add the vocabulary keys.

    If you want to send all vocabulary keys associated with the records matching the stream's filters, select **Auto-select**. All vocabulary keys will be displayed in the table. If you don't want to send a particular vocabulary key, select the checkbox next to it, and then select **Remove Property**.

    ![streams-4.png](../../assets/images/consume/streams/streams-4.png)

1. Near the upper-right corner, select **Save**.

    You configured the export target for the stream and defined what properties will be sent to the export target. Now, you're ready to [start](/consume/streams/manage-streams#) streaming records to the external system.

