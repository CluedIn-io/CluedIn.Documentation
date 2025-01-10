---
layout: cluedin
nav_order: 9
parent: Export targets
grand_parent: Consume
permalink: /consume/export-targets/sql-server-connector
title: SQL Server connector
last_modified: 2025-01-10
---

This article outlines how to configure the SQL Server connector to publish data from CluedIn to SQL databases.

**To configure SQL Server connector**

1. On the navigation pane, go to **Consume** > **Export Targets**. Then, select **Add Export Target**.

1. On the **Choose Target** tab, select **SQL Server Connector**. Then, select **Next**.

    ![sql-server-connector-choose-target.png](../../assets/images/consume/export-targets/sql-server-connector-choose-target.png)

1. On the **Configure** tab, enter the connection details:

    1. **Name** – user-friendly name of the export target that will be displayed on the **Export Target** page in CluedIn.

    1. **Host** – server where your database is located.

    1. **Database Name** – name of a particular database where you want to store the data from CluedIn.

    1. **Username** – username that you use to access the database.

    1. **Password** – password associated with the username that grants access to the database.

    1. (Optional) **Port Number** – network port on which your database server is listening for connections.

    1. (Optional) **Schema** – container within a database where you want to store the data from CluedIn.

    1. (Optional) **Connection Pool Size** – number of database connections that are maintained in a pool for reuse.

1. Test the connection to make sure it works, and then select **Add**.

    ![sql-server-connector-configure.png](../../assets/images/consume/export-targets/sql-server-connector-configure.png)

    Now, you can select the SQL Server connector in a stream and start exporting golden records.