---
title: Azure Event Hub connector
url: https://documentation.cluedin.net/publish/export-targets/azure-event-hub-connector
content_type: reference
section: Publish & consume > Export targets
---

# Azure Event Hub connector

> reference: Facts, options, APIs.

This article outlines how to configure the Azure Event Hub connector to publish data from CluedIn to Azure Event Hubs.

**Prerequisites:** Make sure you have an existing Event Hubs namespace with a specific event hub where you want to store the data from CluedIn. In addition, the event hub must have a policy with **Manage**, **Send**, and **Listen** access.

**To configure Azure Event Hub connector**

1. On the navigation pane, go to **Consume** > **Export Targets**. Then, select **Add Export Target**.

1. On the **Choose Target** tab, select **Azure Event Hub Connector**. Then, select **Next**.

    ![The Add Export Target dialog on the Choose Target tab, with Azure Event Hub Connector selected](https://documentation.cluedin.net/assets/images/consume/export-targets/event-hub-choose-target.png)

1. On the **Configure** tab, enter the connection details:

    1. **Name** – user-friendly name of the export target that will be displayed on the **Export Target** page in CluedIn.

    1. **Connection String** – connection string to the event hub within a namespace where you want to store the data from CluedIn. To find this value, select the needed event hub. Then, select **Shared access policies** on the left menu under **Settings**. Finally, select the policy, and then select the **Copy** button next to the **Connection string-primary key** field. For more information, see [Microsoft documentation](https://learn.microsoft.com/en-us/azure/event-hubs/event-hubs-get-connection-string#connection-string-for-a-specific-event-hub-in-a-namespace).

        ![Azure portal Shared access policies page for an event hub, with the SAS policy pane open and Connection string-primary key highlighted](https://documentation.cluedin.net/assets/images/consume/export-targets/event-hub-connection-string.png)

    1. **Name** – name of the event hub in the Event Hubs namespace where you want to store the data from CluedIn.

       ![Azure portal Event Hubs namespace page listing event hubs, with the event hub name qaeventhub3 highlighted](https://documentation.cluedin.net/assets/images/consume/export-targets/event-hub-name.png)

1. Test the connection to make sure it works, and then select **Add**.

    ![The Configure tab of the Azure Event Hub connector with Name, Connection String and Event Hub Name filled in, and the Test connection and Add buttons](https://documentation.cluedin.net/assets/images/consume/export-targets/event-hub-configure.png)

    Now, you can select the Azure Event Hub connector in a stream and start exporting golden records.

## Batch events

The Azure Event Hub connector supports **batching events** before they are sent to Azure Event Hubs.

Batching can reduce the number of individual send operations and can improve throughput when a stream is publishing a high volume of records.

Batching is configured **on the stream that uses the Azure Event Hub export target**, rather than on the export target itself. This means that different streams using the same Azure Event Hub connector can use different batching settings.

To configure batching:

1. Go to **Consume** > **Streams** and open the stream that uses the Azure Event Hub export target.

1. Open the **Export Target Configuration** for the stream.

1. Configure the batching options available for the Azure Event Hub connector.

1. Save the stream configuration.

When batching is enabled, CluedIn groups multiple events and sends them to Azure Event Hubs together instead of sending every event as an individual operation.

> **Important:** Batching settings are specific to each stream. Changing the batching configuration on one stream does not change the configuration of other streams that use the same Azure Event Hub export target.

Up: [Export targets](https://documentation.cluedin.net/publish/export-targets.md)
