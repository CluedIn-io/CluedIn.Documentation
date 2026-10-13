---
title: Azure Service Bus connector
url: https://documentation.cluedin.net/publish/export-targets/azure-service-bus-connector
content_type: reference
section: Publish & consume > Export targets
---

# Azure Service Bus connector

> reference: Facts, options, APIs.

This article outlines how to configure the Azure Service Bus connector to publish data from CluedIn to Service Bus.

**Prerequisites:** Make sure you have an existing Service Bus namespace with a specific queue where you want to store the data from CluedIn. The namespace must have the **RootManageSharedAccessKey** policy with **Manage**, **Send**, and **Listen** access. In addition, the queue must have a policy with **Manage**, **Send**, and **Listen** access.

**To configure Azure Service Bus connector**

1. On the navigation pane, go to **Consume** > **Export Targets**. Then, select **Add Export Target**.

1. On the **Choose Target** tab, select **Azure Service Bus Connector**. Then, select **Next**.

    ![The Add Export Target dialog on the Choose Target tab, with Azure Service Bus Connector selected](https://documentation.cluedin.net/assets/images/consume/export-targets/service-bus-choose-target.png)

1. On the **Configure** tab, enter the connection details:

    1. **Name** – user-friendly name of the export target that will be displayed on the **Export Target** page in CluedIn.

    1. **Connection String** – connection string to the Service Bus namespace or to the specific queue where you want to store the data from CluedIn.

         To get the connection string to the Service Bus namespace, follow [this instruction](https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-dotnet-get-started-with-queues?tabs=connection-string#get-the-connection-string) from Microsoft. The following image shows an example of connection string for the namespace.

        ![Azure portal Shared access policies for a Service Bus namespace, with the Primary Connection String of RootManageSharedAccessKey highlighted](https://documentation.cluedin.net/assets/images/consume/export-targets/service-bus-connection-string.png)

        Alternatively, you can use the connection string to the specific queue.

    1. **Queue Name** – name of the queue in the Service Bus namespace where you want to store the data from CluedIn. 

        If you provided the connection string to the namespace in step 2b, you can leave the **Queue Name** field empty. When configuring the export target for the stream, you'll need to provide the name of the queue as the **Target name**.

        If you provided the connection string to the queue in step 2b, you can leave the **Queue Name** field empty since the connection string contains the queue name.

       ![Azure portal Queues page of a Service Bus namespace, with the queue name queuetest highlighted](https://documentation.cluedin.net/assets/images/consume/export-targets/service-bus-queue-name.png)

1. Test the connection to make sure it works, and then select **Add**.

    ![Configure tab with Name, Connection String and Queue Name filled in, and the Test connection and Add buttons](https://documentation.cluedin.net/assets/images/consume/export-targets/service-bus-configure.png)

    Now, you can select the Azure Service Bus connector in a stream and start exporting golden records.

Up: [Export targets](https://documentation.cluedin.net/publish/export-targets.md)
