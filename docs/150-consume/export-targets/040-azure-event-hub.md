---
layout: cluedin
nav_order: 4
parent: Export targets
grand_parent: Consume
permalink: consume/export-targets/azure-event-hub-connector
title: Azure Event Hub connector
last_modified: 2025-01-08
---

This article outlines how to configure the Azure Event Hub connector to publish data from CluedIn to Azure Event Hubs.

**Prerequisites:** Make sure you have an existing Event Hubs namespace with a specific event hub where you want to store the data from CluedIn. In addition, the event hub must have a policy with **Manage**, **Send**, and **Listen** access.

**To configure Azure Event Hub connector**

1. On the navigation pane, go to **Consume** > **Export Targets**. Then, select **Add Export Target**.

1. On the **Choose Target** tab, select **Azure Event Hub Connector**. Then, select **Next**.

    ![event-hub-choose-target.png]({{ "/assets/images/consume/export-targets/event-hub-choose-target.png" | relative_url }})

1. On the **Configure** tab, enter the connection details:

    1. **Name** – user-friendly name of the export target that will be displayed on the **Export Target** page in CluedIn.

    1. **Connection String** – connection string to the event hub within a namespace where you want to store the data from CluedIn. To find this value, select the needed event hub. Then, select **Shared access policies** on the left menu under **Settings**. Finally, select the policy, and then select the **Copy** button next to the **Connection string-primary key** field. For more information, see [Microsoft documentation](https://learn.microsoft.com/en-us/azure/event-hubs/event-hubs-get-connection-string#connection-string-for-a-specific-event-hub-in-a-namespace).

        ![event-hub-connection-string.png]({{ "/assets/images/consume/export-targets/event-hub-connection-string.png" | relative_url }})

    1. **Name** – name of the event hub in the Event Hubs namespace where you want to store the data from CluedIn.

       ![event-hub-name.png]({{ "/assets/images/consume/export-targets/event-hub-name.png" | relative_url }})

1. Test the connection to make sure it works, and then select **Add**.

    ![event-hub-configure.png]({{ "/assets/images/consume/export-targets/event-hub-configure.png" | relative_url }})

    Now, you can select the Azure Event Hub connector in a stream and start exporting golden records.