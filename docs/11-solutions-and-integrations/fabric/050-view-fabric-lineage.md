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

In this article, you will learn how to follow data from Microsoft Fabric into CluedIn and back out to Fabric again.

CluedIn shows this lineage on a **Fabric lineage** tab. The tab draws a graph from left to right, in the direction the data moves. It can contain:

- The Fabric items that CluedIn reads from or writes to, such as a lakehouse or a mirrored database.
- The CluedIn ingestion endpoints that read from Fabric, and the streams that export their records.
- The Fabric items around them that Fabric itself reports, such as the pipeline that loads a lakehouse or the reports built on a mirrored database.
- Other parts of CluedIn that use a Fabric item in the graph: the Global Data Model, when it is synced to a Fabric Ontology, and rules and deduplication, when they run as Spark jobs in a Fabric lakehouse.

Microsoft Fabric does not accept lineage from other systems. CluedIn's lineage is therefore shown in CluedIn, not in the lineage view of your Fabric workspace.

## Where the Fabric lineage tab appears

| Where | When it appears | What the graph shows |
| --- | --- | --- |
| Ingestion endpoint | The endpoint was onboarded from Microsoft Fabric. | The Fabric table the endpoint reads, the Fabric items upstream of it, the streams that export the endpoint's records, and the Fabric items those streams write to. |
| Stream | The stream's export target is the [OneLake connector](/publish/export-targets/onelake-connector) or the [Open Mirroring connector](/publish/export-targets/openmirroring-connector). | The ingestion endpoints whose records the stream exports and the Fabric tables they read, the Fabric item the stream writes to, and the Fabric items downstream of it. |
| OneLake Catalog | You open an item in the OneLake Catalog explorer. | The Fabric items upstream and downstream of the item, the ingestion endpoints that read from it, and the streams that export to it. |

## How CluedIn links ingestion endpoints to streams

An ingestion endpoint feeds a stream when the stream exports golden records that contain data from the endpoint. CluedIn checks this against the golden records themselves, so the lineage shows where data has actually gone, not only where it could go. An endpoint with no processed records yet is not linked to any stream.

A golden record knows which data source its data came from, but not which ingestion endpoint of that data source. If a data source has several ingestion endpoints, they are all shown feeding the same streams, and the number of records is shown only when the data source has a single endpoint.

## View the lineage of an ingestion endpoint

**To view the lineage of an ingestion endpoint onboarded from Microsoft Fabric**

1. Open the ingestion endpoint.

1. Select the **Fabric lineage** tab.

    The graph starts at the Fabric table the endpoint reads. It continues to every stream that exports the endpoint's records, with the number of records on each edge, and on to the Fabric item each stream writes to.

    ![Fabric lineage tab of an ingestion endpoint, linking the Sales Lakehouse to the contacts endpoint, and the endpoint to three streams and the Fabric items they write to]({{ "/assets/images/microsoft-integration/fabric/fabric-lineage-ingestion-endpoint.png" | relative_url }})

## View the lineage of a stream

**To view the lineage of a stream that exports to Microsoft Fabric**

1. Open the stream.

1. Select the **Fabric lineage** tab.

    The graph starts at the Fabric tables of the ingestion endpoints that feed the stream. It continues through the stream to the Fabric item that the export target writes to.

    ![Fabric lineage tab of a stream, linking the Sales Lakehouse to the contacts endpoint, the endpoint to the stream, and the stream to the CluedInMirror mirrored database]({{ "/assets/images/microsoft-integration/fabric/fabric-lineage-stream.png" | relative_url }})

## View the lineage of a OneLake Catalog item

**To view the lineage of an item in the OneLake Catalog**

1. Open the OneLake Catalog explorer and select an item.

1. In the item pane, select the **Fabric lineage** tab.

    The graph shows the Fabric items upstream and downstream of the item, the ingestion endpoints that read from it, and the streams whose export target names this item's workspace and item.

## Figures in the graph

The cards and edges show figures that help you check that data is arriving and up to date:

| Figure | Where it comes from |
| --- | --- |
| Records on an edge from an ingestion endpoint to a stream | The golden records the stream exports that contain data from the endpoint. |
| Mirroring status, rows in Fabric, and last mirrored time | Fabric's mirroring status of the table, for a stream on the Open Mirroring connector. |
| Last synced, and last sync failed | The ingestion endpoint's Microsoft Fabric sync schedule. |
| Status and last exported | The stream. |
| Last synced, and business domains synced | The Global Data Model's Ontology sync. |

### Count the rows of a Fabric table

A Fabric card lists the tables CluedIn reads or writes. Select **Count rows in** a table to count its rows in Fabric. CluedIn counts the rows only when you ask, because the count runs a query on your Fabric capacity.

You can count rows in a lakehouse or a mirrored database. If the capacity of the workspace is paused, CluedIn tells you instead of resuming it, because a running capacity is billed.

### Open an item in Fabric

Select **Open in Fabric** on a Fabric card to open the item in the Fabric portal. Lakehouses, reports, and semantic models open on their own page. Other items open their workspace.

## When part of the lineage is missing

CluedIn reads the Fabric part of the lineage with the service principal of the connection or export target. If Fabric does not return it, the tab shows a warning that explains why, and still shows the rest of the lineage. Common reasons:

- The tenant ID, client ID, or client secret of the connection or export target is wrong.
- The service principal does not have access to the workspace. Add it as at least a **Viewer** on the workspace.
- The Fabric item was renamed or deleted. Export targets find their Fabric item by its workspace name and item name.
- The Fabric connection that the ingestion endpoint was onboarded from was deleted.

CluedIn reads the surrounding Fabric items with Fabric's item relations API, which is in beta. If the API is not available in your tenant, the warning says so, and the graph shows only the items that CluedIn reads from or writes to.
