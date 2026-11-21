---
layout: cluedin
title: View Microsoft Fabric lineage
parent: Microsoft Fabric
grand_parent: Solutions & integrations
nav_order: 50
permalink: /solutions/fabric/view-fabric-lineage
content_type: how-to
---

## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

In this article, you will learn how to see which Microsoft Fabric items CluedIn reads data from and writes data to.

CluedIn shows this lineage on a **Fabric lineage** tab. The tab draws a graph from left to right, in the direction the data moves. It contains:

- The Fabric items that CluedIn reads from or writes to, such as a lakehouse or a mirrored database.
- The CluedIn ingestion endpoints and streams that read from or write to those items.
- The Fabric items around them that Fabric itself reports, such as the pipeline that loads a lakehouse or the reports built on a mirrored database.

Microsoft Fabric does not accept lineage from other systems. CluedIn's lineage is therefore shown in CluedIn, not in the lineage view of your Fabric workspace.

## Where the Fabric lineage tab appears

| Where | When it appears | What the graph shows |
| --- | --- | --- |
| Ingestion endpoint | The endpoint was onboarded from Microsoft Fabric. | The Fabric table the endpoint reads from, and the Fabric items upstream of it. |
| Stream | The stream's export target is the [OneLake connector](/publish/export-targets/onelake-connector) or the [Open Mirroring connector](/publish/export-targets/openmirroring-connector). | The Fabric item the stream writes to, and the Fabric items downstream of it. |
| OneLake Catalog | You open an item in the OneLake Catalog explorer. | The Fabric items upstream and downstream of the item, and the CluedIn streams that export to it. |

## View the lineage of an ingestion endpoint

**To view the lineage of an ingestion endpoint onboarded from Microsoft Fabric**

1. Open the ingestion endpoint.

1. Select the **Fabric lineage** tab.

    The graph links the Fabric item to the ingestion endpoint. The edge label shows the table that CluedIn reads.

    ![Fabric lineage tab of an ingestion endpoint, linking the Sales Lakehouse Fabric item to the customers ingestion endpoint]({{ "/assets/images/microsoft-integration/fabric/fabric-lineage-ingestion-endpoint.png" | relative_url }})

## View the lineage of a stream

**To view the lineage of a stream that exports to Microsoft Fabric**

1. Open the stream.

1. Select the **Fabric lineage** tab.

    The graph links the stream to the Fabric item that the export target writes to. The edge label shows the table that the stream writes.

    ![Fabric lineage tab of a stream, linking the stream to the CluedInMirror mirrored database]({{ "/assets/images/microsoft-integration/fabric/fabric-lineage-stream.png" | relative_url }})

## View the lineage of a OneLake Catalog item

**To view the lineage of an item in the OneLake Catalog**

1. Open the OneLake Catalog explorer and select an item.

1. In the item pane, select the **Fabric lineage** tab.

    The graph shows the Fabric items upstream and downstream of the item. It also shows the CluedIn streams whose export target names this item's workspace and item.

## When part of the lineage is missing

CluedIn reads the Fabric part of the lineage with the service principal of the connection or export target. If Fabric does not return it, the tab shows a warning that explains why, and still shows the CluedIn side of the lineage. Common reasons:

- The tenant ID, client ID, or client secret of the connection or export target is wrong.
- The service principal does not have access to the workspace. Add it as at least a **Viewer** on the workspace.
- The Fabric item was renamed or deleted. Export targets find their Fabric item by its workspace name and item name.
- The Fabric connection that the ingestion endpoint was onboarded from was deleted.

CluedIn reads the surrounding Fabric items with Fabric's item relations API, which is in beta. If the API is not available in your tenant, the warning says so, and the graph shows only the items that CluedIn reads from or writes to.
