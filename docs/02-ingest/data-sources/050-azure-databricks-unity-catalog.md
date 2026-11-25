---
layout: cluedin
title: Azure Databricks Unity Catalog
parent: Data sources
grand_parent: Ingest
nav_order: 50
permalink: /ingest/data-sources/azure-databricks-unity-catalog
content_type: how-to
tags: ["integration", "azure", "databricks", "unity catalog"]
last_modified: 2026-11-24
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article, you will learn how to connect CluedIn to an Azure Databricks workspace and ingest tables governed by Unity Catalog.

CluedIn reads Unity Catalog through the public Azure Databricks REST APIs. It can browse every kind of securable Unity Catalog exposes. It reads table rows through a Databricks SQL warehouse, so Unity Catalog permissions, row filters and column masks apply to everything CluedIn ingests. Each table you onboard becomes its own [ingestion endpoint](/ingest/data-sources/endpoint). You can keep it in sync with the table on a schedule.

| What you can do | Supported Unity Catalog objects |
|--|--|
| Browse | Catalogs (including Delta Sharing catalogs and Lakehouse Federation foreign catalogs), schemas, tables, views, materialized views, streaming tables, foreign tables, volumes, functions and registered models |
| Inspect | Column names, types, nullability and comments, primary key, table type and format, storage location, owner, created/updated details, table properties, and upstream/downstream table lineage |
| Preview and ingest | Tables, views, materialized views, streaming tables and foreign tables |

Volumes, functions and registered models are shown when you browse, so the list matches Catalog Explorer, but you can't ingest them as records.

## Prerequisites

- An Azure Databricks workspace with Unity Catalog enabled, which means a metastore is assigned to the workspace.
- An identity for CluedIn to use. You can use any one of the following:
    - **Microsoft Entra ID service principal** (recommended). This is an app registration with a client secret. Add it to the workspace under **Settings** > **Identity and access** > **Service principals**, using its application (client) ID.
    - **Databricks service principal with an OAuth secret**. This is a Databricks-managed service principal; CluedIn authenticates with OAuth machine-to-machine. Create the secret on the service principal's **Secrets** tab.
    - **Personal access token**. This is convenient for trying the integration out, but the token belongs to a user and expires.
- Unity Catalog privileges for that identity on the data you want to ingest:
    - `USE CATALOG` on the catalog.
    - `USE SCHEMA` on the schema.
    - `SELECT` on the tables and views.

    For example:

    ```sql
    GRANT USE CATALOG ON CATALOG main TO `cluedin-ingest`;
    GRANT USE SCHEMA, SELECT ON SCHEMA main.sales TO `cluedin-ingest`;
    ```

- **CAN USE** permission on a SQL warehouse. CluedIn needs a warehouse to preview and ingest rows, but not to browse. A serverless SQL warehouse is recommended because it starts in seconds. CluedIn starts a stopped warehouse automatically when it needs one.
- Optional, to record lineage in Unity Catalog: the `CREATE EXTERNAL METADATA` privilege on the metastore, for example ``GRANT CREATE EXTERNAL METADATA ON METASTORE TO `cluedin-ingest`;``. Without it, syncs still work; only the lineage step is skipped. See [Record lineage in Unity Catalog](#record-lineage-in-unity-catalog).
- Network access from CluedIn to the workspace URL. If the workspace uses IP access lists or Private Link, allow CluedIn's outbound addresses.

## Connect to Azure Databricks

1. In **Ingest** > **Sources**, select **Import** > **From Azure Databricks (Unity Catalog)**.

    ![The Import menu with the From Azure Databricks (Unity Catalog) option]({{ "/assets/images/integration/data-sources/azure-databricks/import-menu.png" | relative_url }})

1. On the **Configure** tab, enter the **Name** of the data source, choose its **Group**, and then select **Next**.

1. On the **Connect** tab, choose **Connect to a new Azure Databricks workspace**. To reuse a connection you created before, choose **Use an existing connection** instead.

1. Enter a **Name** for the connection and the **Workspace URL**. The workspace URL is the URL you open the workspace with, for example `https://adb-1234567890123456.7.azuredatabricks.net`. You can find it on the workspace's **Overview** page in the Azure portal.

1. Choose the **Authentication** type, and then enter its credentials:

    | Authentication | Fields |
    |--|--|
    | Microsoft Entra ID service principal | Tenant ID, Client ID, Client secret |
    | Databricks service principal (OAuth secret) | Client ID (the service principal's application ID), Client secret (the OAuth secret) |
    | Personal access token | Access token |

1. Select **Test connection**. CluedIn checks each prerequisite in turn and reports the metastore it reached and how many catalogs it can see. It also lists the SQL warehouses the connection can use, so you can choose a default warehouse.

    ![A successful connection test, showing the metastore name and number of catalogs]({{ "/assets/images/integration/data-sources/azure-databricks/connect-test-success.png" | relative_url }})

1. Select **Connect**. CluedIn validates the connection again and saves it. Secrets are stored encrypted and are never shown again.

## Browse and select tables

On the **Browse** tab, open a catalog, and then a schema. Each object shows its type and, for tables, its format. Select the tables and views to ingest. You can select several, including from different schemas.

![Browsing the main.sales schema with two tables selected]({{ "/assets/images/integration/data-sources/azure-databricks/browse.png" | relative_url }})

## Preview tables

On the **Preview** tab, each selected table shows the following:

- **Columns**: name, type, nullability, primary key and comment.
- **Lineage**: the upstream and downstream tables Unity Catalog has recorded.
- **Sample rows**: read through the SQL warehouse.

![The preview of main.sales.customers, showing columns, lineage and sample rows]({{ "/assets/images/integration/data-sources/azure-databricks/preview.png" | relative_url }})

If a preview isn't available, the reason is shown instead. For example, the identity might lack `SELECT` on the table, or no SQL warehouse is selected.

## Onboard and keep tables in sync

1. On the **Map** tab, review the tables to onboard. Each table becomes its own ingestion endpoint, named after the table.

1. To pull the table's rows automatically, select **Keep the ingestion endpoints in sync with Azure Databricks**, and choose how often (every 15 minutes, hourly or daily).

    ![The Map tab with sync enabled every 15 minutes]({{ "/assets/images/integration/data-sources/azure-databricks/map-sync.png" | relative_url }})

1. Select **Add**.

Each sync run reads the next batch of rows (500 by default) and submits it to the ingestion endpoint. When it reaches the end of the table, it starts again from the beginning. CluedIn creates and manages the API token used to submit the rows, so you don't need to create one.

On the ingestion endpoint's page, you can see when the sync last ran and any error from that run. Select **Run now** to sync without waiting for the schedule. If an endpoint was onboarded without sync, you can turn it on from the same page.

![The customers ingestion endpoint showing its Azure Databricks sync status and Run now]({{ "/assets/images/integration/data-sources/azure-databricks/endpoint-sync-status.png" | relative_url }})

After the rows arrive, [map](/ingest/mapping/create-mapping) and [process](/ingest/processing/process-data) them as for any other ingestion endpoint.

## Record lineage in Unity Catalog

After a sync first delivers rows, CluedIn records in Unity Catalog lineage that the table feeds the ingestion endpoint. In Catalog Explorer, the table's **Lineage** tab then shows a downstream node for the endpoint. Its column-level lineage maps each table column to the endpoint column of the same name.

- The endpoint appears as an external metadata object named `cluedin_<organization>_<table>_<data set id>`. Its entity type is **CluedIn ingestion endpoint**. Its URL opens the endpoint in CluedIn, and its properties record the organization, data set id and sync schedule.
- It's recorded once. If you point the sync at a different table, the next run moves the lineage to the new table. If you delete the sync, the lineage is removed.
- This uses Unity Catalog external lineage, which is in Public Preview. It needs the `CREATE EXTERNAL METADATA` privilege listed under [Prerequisites](#prerequisites).
- If lineage can't be recorded, the sync still succeeds. The reason is shown on the endpoint's page under **Azure Databricks sync**, and CluedIn tries again on the next run, so once you grant the privilege, select **Run now**.
- Only data coming into CluedIn is recorded. Data CluedIn sends out through export targets isn't added to Unity Catalog lineage.

## Verify the result

- The data source opens with one ingestion endpoint per table, and CluedIn shows a notification such as **2 Azure Databricks tables added**.
- With sync on, each endpoint's page shows **Azure Databricks sync** and **Last run**. A run that succeeded has no error. Rows appear on the endpoint's **Preview** tab once the first run has finished. Saving the schedule only registers it; the first run happens on the next scheduled time, or straight away if you select **Run now**.

## What this changes

- Connecting saves the connection, with its secrets encrypted. Nothing is read from Databricks except metadata.
- Onboarding creates the data source, its ingestion endpoints and, if sync is on, a sync schedule and a CluedIn API token for each endpoint.
- Sync only **reads** table data from Azure Databricks; it never writes to your tables. The one thing it writes is the lineage metadata described in [Record lineage in Unity Catalog](#record-lineage-in-unity-catalog). The rows it submits are processed like any other ingestion endpoint data, so golden records change only when you process them.
- Deleting a connection doesn't delete the endpoints or the data already ingested.

## Manage connections

To see your Azure Databricks connections, go to **Azure Integration** > **Azure Databricks connections**, or open `/admin/inbound/datasourceset/databricks-connections`. From there you can do the following:

- Test a connection.
- Rename a connection or change its default SQL warehouse.
- Rotate a connection's credentials. Changing the workspace URL, the authentication type or the credentials requires re-entering the secret, and the connection is validated again before it's saved.
- Delete a connection. Delete or repoint any syncs that use it first.

![The Azure Databricks connections page]({{ "/assets/images/integration/data-sources/azure-databricks/connections.png" | relative_url }})

To automate any of this, use the `api/databricks` endpoints in the [REST API](/api). Reading needs at least the Informed level of the **Integration** > **Data Source Groups** claim, and creating or changing anything needs at least Consulted.

## If something goes wrong

If a connection test fails, CluedIn tells you which prerequisite is missing and how to fix it. Save and sync failures use the same messages.

![A failed connection test explaining that the personal access token was rejected]({{ "/assets/images/integration/data-sources/azure-databricks/connect-test-error.png" | relative_url }})

| Message says | What to do |
|--|--|
| ...is not a valid Azure Databricks workspace URL | Use the `https://` workspace URL from the Azure portal. |
| Could not reach the Azure Databricks workspace | Check the URL, and that the workspace's IP access lists or Private Link settings allow CluedIn. |
| The client secret is invalid / has expired | Copy the secret's **Value** (not its **Secret ID**), or create a new secret. |
| No app registration with client ID ... exists in tenant ... | Check the client (application) ID and the directory (tenant) ID. |
| Make sure the service principal has been added to this workspace | Add the service principal to the workspace, using its application ID. |
| The personal access token was rejected | Generate a new token under **Settings** > **Developer** > **Access tokens**. |
| ...isn't attached to a Unity Catalog metastore | An account admin must assign a metastore to the workspace in the Databricks account console. |
| ...can't see any Unity Catalog catalogs | Grant the identity `USE CATALOG` on at least one catalog. |
| Lineage couldn't be recorded in Unity Catalog: grant the connection's identity CREATE EXTERNAL METADATA | Grant `CREATE EXTERNAL METADATA` on the metastore, then select **Run now**. The sync itself isn't affected. |
| Lineage couldn't be recorded: external lineage (Public Preview) isn't available | The workspace doesn't offer external lineage yet. Syncs still work. |
| No SQL warehouses are available to this connection | Create a SQL warehouse and grant the identity **CAN USE** on it. You can still browse without one. |
| The table could not be found, or this connection's identity lacks... | Check the table still exists, and grant `USE CATALOG`, `USE SCHEMA` and `SELECT`. |
| The SQL warehouse ... did not finish the query | The warehouse was probably still starting. Select **Run now** again, or use a serverless warehouse. |
| Submitting rows to the Ingestion Endpoint failed | The sync read the rows but CluedIn refused them. The same rows are retried on the next run. |
