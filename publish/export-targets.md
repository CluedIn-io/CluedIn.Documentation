---
title: Export targets
url: https://documentation.cluedin.net/publish/export-targets
content_type: landing
section: Publish & consume
---

# Export targets

Export targets are used for connecting with an integration point (also referred to as target), enabling CluedIn to send records to it using a [stream](https://documentation.cluedin.net/publish/streams.md). Examples of integration points include the following:

- Business intelligence tools

- Data warehouse dimension tables

- Machine learning platforms

- Custom applications

- Databases

Here are two examples of how to build a new Export Target:

- [SQL Server](https://github.com/CluedIn-io/CluedIn.Connector.SqlServer)

- [Snowflake](https://github.com/CluedIn-io/CluedIn.Connector.Snowflake)

See the full list of public implementations of CluedIn Export Targets [here](https://github.com/CluedIn-io?q=connector).

In this article, you will learn how to configure and manage an export target that can receive records sent from CluedIn.

## Configure an export target

You can configure a predefined export target provided with CluedIn (such as SQL Server Connector or Azure Event Hub Connector). You can also write a custom connector using the CluedIn NuGet package; however, it requires C# knowledge and the actual external service.

**To configure an export target**

1. On the navigation pane, go to **Consume** > **Export Targets**. Then, select **Add Export Target**.

    The **Add Export Target** pane opens, where you can select and configure the needed export target.

1. On the **Choose Target** tab, select the external system you want to establish a connection with. Then, select **Next**.

1. On the **Configure** tab, enter the connection details. The list of fields that you need to complete depends on the selected export target. For example, for the Microsoft SQL Server export target, you need to provide the **Name**, **Host**, **Database Name**, **Username**, and **Password**.

1. Test the connection to make sure it works, and then select **Add**.

    ![Animation: selecting Add Export Target, choosing a target on the Choose Target tab, entering connection details on the Configure tab, testing the connection, and adding it](https://documentation.cluedin.net/assets/images/consume/export-targets/export-target-configuration.gif)

    You configured the export target. Now, it can be attached to the stream. The user who added the export target is the owner of the export target.

## Manage an export target

On the export target details page, you can do the following:

- Test the connection to the export target.

    ![Export target details page with Test connection, the Active toggle, and the Synchronized and Healthy status labels](https://documentation.cluedin.net/assets/images/consume/export-targets/export-targets-1.png)

- View the streaming modes supported by the export target:

    - **Synchronized** – the records in the export target mirror the records in CluedIn.

    - **Event** – the records in the export target are written as events (for example, Create, Insert, Update, Delete) each time an action occurs in CluedIn.

- Activate and deactivate the export target. When activating or deactivating the export target, you can view the streams linked to it as well as start, pause, or stop the needed streams.

    ![Deactivate Export Target dialog listing linked streams with start, pause and stop controls, and the Deactivate button](https://documentation.cluedin.net/assets/images/consume/export-targets/export-targets-2.png)

- Review the export target health checks.

    Health checks for the export target run every 60 seconds. If, for example, somebody has changed the password for the user connecting to the export target, the health check status would change to **Unhealthy**, letting you know that you need to check on the export target. After the issue is fixed, the status will go back to **Healthy** again. The **Partially Healthy** status indicates that some pods are reporting healthy and others are reporting unhealthy (for example, if there is a network issue where one pod is struggling to connect but the other pods can still connect).

    If the export target is **Unhealthy**, you cannot select it in the export target configuration for a stream. Additionally, if you have already configured the stream and the export target becomes **Unhealthy**, you cannot start such stream.

- Edit the connection details.

## In this section

- [Connector reference](https://documentation.cluedin.net/publish/export-targets/connector-reference.md) (reference): In this article, you will find reference information about built-in connectors in CluedIn.
- [Amazon S3 connector](https://documentation.cluedin.net/publish/export-targets/amazon-s3-connector.md) (reference): This article outlines how to configure the Amazon S3 connector to publish data from CluedIn to an Amazon Simple Storage Service (Amazon S3) bucket.
- [Azure Data Lake connector](https://documentation.cluedin.net/publish/export-targets/adl-connector.md) (reference): This article outlines how to configure the Azure Data Lake connector to publish data from CluedIn to Azure Data Lake Storage Gen2.
- [Azure Dedicated SQL Pool connector](https://documentation.cluedin.net/publish/export-targets/azure-dedicated-sql-pool-connector.md) (reference): This article outlines how to configure the Azure Dedicated SQL Pool connector to push data from CluedIn to Microsoft’s Dedicated SQL Pool, which is a part of Azure Synapse Analytics platform.
- [Azure Event Hub connector](https://documentation.cluedin.net/publish/export-targets/azure-event-hub-connector.md) (reference): This article outlines how to configure the Azure Event Hub connector to publish data from CluedIn to Azure Event Hubs.
- [Azure Service Bus connector](https://documentation.cluedin.net/publish/export-targets/azure-service-bus-connector.md) (reference): This article outlines how to configure the Azure Service Bus connector to publish data from CluedIn to Service Bus.
- [Dataverse connector](https://documentation.cluedin.net/publish/export-targets/dataverse-connector-v2.md) (reference): This article outlines how to configure the Dataverse connector to publish data from CluedIn to Microsoft Dataverse.
- [Dataverse connector (legacy)](https://documentation.cluedin.net/publish/export-targets/dataverse-connector.md) (reference): This article outlines how to configure the Dataverse connector to publish data from CluedIn to Microsoft Dataverse.
- [HTTP connector](https://documentation.cluedin.net/publish/export-targets/http-connector.md) (reference): This article outlines how to configure the HTTP connector to publish data from CluedIn to an external HTTP endpoint.
- [OneLake connector](https://documentation.cluedin.net/publish/export-targets/onelake-connector.md) (reference): This article outlines how to configure the OneLake connector to push data from CluedIn to Microsoft’s OneLake.
- [Open Mirroring connector](https://documentation.cluedin.net/publish/export-targets/openmirroring-connector.md) (reference): This article outlines how to configure the Open Mirroring connector to push data from CluedIn to Microsoft’s Fabric.
- [Snowflake connector](https://documentation.cluedin.net/publish/export-targets/snowflake-connector.md) (reference): This article explains how to find the Snowflake connection details, configure key-pair authentication, and add a Snowflake export target in CluedIn.
- [SQL Server connector](https://documentation.cluedin.net/publish/export-targets/sql-server-connector.md) (reference): This article outlines how to configure the SQL Server connector to publish data from CluedIn to SQL databases.
- [Create a service principal](https://documentation.cluedin.net/publish/export-targets/create-service-principal.md) (how-to): This article outlines how to register an application and create a service principal.
- [File name patterns](https://documentation.cluedin.net/publish/export-targets/file-name-patterns.md) (reference): In this article, you will learn about the file name patterns that you can use in the export target configuration to customize the output file names.

Up: [Publish & consume](https://documentation.cluedin.net/publish.md)
