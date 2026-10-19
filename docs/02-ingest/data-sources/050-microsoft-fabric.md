---
layout: cluedin
title: Microsoft Fabric
parent: Data sources
grand_parent: Ingest
nav_order: 50
permalink: /ingest/data-sources/microsoft-fabric
content_type: how-to
tags: ["integration", "data sources", "microsoft fabric"]
last_modified: 2026-10-19
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article, you will learn how to connect CluedIn to Microsoft Fabric and ingest Fabric tables - including Delta tables, Shortcuts, and tables from Mirrored Databases - as CluedIn ingestion endpoints.

The process involves three steps:

1. [Connect to Microsoft Fabric](#connect-to-microsoft-fabric)
1. [Browse and preview Fabric tables](#browse-and-preview-fabric-tables)
1. [Onboard a Fabric table](#onboard-a-fabric-table)

## Prerequisites

- A Microsoft Entra ID app registration (service principal) with a client secret, added as a member or contributor on the Microsoft Fabric workspace(s) you want to browse.
- The Tenant ID and Client ID of that app registration.

## Connect to Microsoft Fabric

**To connect to Microsoft Fabric**

1. On the CluedIn home page, in the **Ingest** section, go to **Sources**, and then select **Import** > **From Microsoft Fabric**.

1. On the **Configure** tab, enter a **Name** for the data source and the **Group** it belongs to, and then select **Next**.

1. On the **Connect** tab, do one of the following:

    - To reuse a connection you created earlier, select **Use an existing connection**, and then choose it from the list.
    - To create a new connection, select **Connect to a new Microsoft Fabric tenant**, and then enter the **Tenant ID**, **Client ID**, and **Client secret** of your Microsoft Entra ID app registration. Optionally, give the connection a **Name** so you can recognize it later.

1. Select **Connect**.

    CluedIn verifies the credentials against Microsoft Fabric before saving the connection. If the credentials are invalid, or the app registration doesn't have access to any workspace, an error message explains what to fix. Once connected, the connection is saved for your organization and can be reused without re-entering the client secret.

## Browse and preview Fabric tables

**To browse and preview Fabric tables**

1. On the **Browse** tab, select a workspace, and then a Lakehouse or Mirrored Database, to see its tables.

    Tables created as Shortcuts are labeled **Shortcut**, and Delta tables show their storage format. Browsing into a Mirrored Database's own tables isn't supported yet; use the Lakehouse that Microsoft Fabric creates automatically for it instead.

1. Select the checkbox next to the table you want to ingest, and then select **Next**.

1. On the **Map** tab, review the preview of the table's data.

    If a preview isn't available - for example, because the Lakehouse doesn't have a SQL analytics endpoint yet, or the service principal doesn't have data access permissions - an explanation is shown instead, and you can still continue onboarding without it.

## Onboard a Fabric table

The **Map** tab also pre-fills the ingestion endpoint's fields from the Fabric table's columns, the same as [creating an ingestion endpoint](/ingest/data-sources/endpoint) manually.

**To onboard a Fabric table**

1. On the **Map** tab, enter a name for the ingestion endpoint, and choose whether to map it to a new entity type or an existing data set.

1. Select **Add**.

    The table is added to CluedIn as an ingestion endpoint. Next, [create mapping](/ingest/mapping/create-mapping) and [process data](/ingest/processing/process-data).

{: .important }
Onboarding a Fabric table creates an ingestion endpoint; it doesn't continuously sync data from Fabric. To get Fabric rows into CluedIn, push them to the endpoint - for example using the [Fabric notebook approach](/solutions/fabric/connect-fabric-to-cluedin) - or your own pipeline.
