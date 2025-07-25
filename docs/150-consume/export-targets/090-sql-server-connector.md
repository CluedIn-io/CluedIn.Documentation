---
layout: cluedin
nav_order: 9
parent: Export targets
grand_parent: Consume
permalink: /consume/export-targets/sql-server-connector
title: SQL Server connector
last_modified: 2025-04-03
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

This article outlines how to configure the SQL Server connector to publish data from CluedIn to SQL databases.

**Prerequisites:** The authentication method for the SQL Server must be **SQL Server Authentication** (not Windows Authentication). If you do not use SQL Server Authentication, you need to enable it as described [here](#sql-server-authentication).

## Configure SQL Server connector

1. On the navigation pane, go to **Consume** > **Export Targets**. Then, select **Add Export Target**.

1. On the **Choose Target** tab, select **SQL Server Connector**. Then, select **Next**.

    ![sql-server-connector-choose-target.png]({{ "/assets/images/consume/export-targets/sql-server-connector-choose-target.png" | relative_url }})

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

    ![sql-server-connector-configure.png]({{ "/assets/images/consume/export-targets/sql-server-connector-configure.png" | relative_url }})

    Now, you can select the SQL Server connector in a stream and start exporting golden records.

## SQL Server Authentication

When integrating with CluedIn, you typically need to use SQL Server Authentication (not Windows Authentication) to allow the platform to connect to your SQL Server. This is because CluedIn generally requires a consistent, non-interactive authentication method to securely access your database.   

- **Windows Authentication** is generally tied to the local user context of the machine you're using, and it requires a session with specific privileges. This can create issues when trying to connect from an external service like CluedIn, especially when the service doesn't have access to your machine’s Windows authentication context.

- **SQL Server Authentication** is independent of the Windows environment and uses a specific SQL Server login and password that can be configured to have the appropriate access to your SQL database. This makes it easier to set up and more compatible with external systems.

**To configure SQL Server Authentication**

1. Ensure that your SQL Server is configured to accept **SQL Server Authentication**. This is a setting you can enable in the SQL Server Management Studio (SSMS) under the server properties.

1. To enable SQL Server Authentication:

    1. Open **SQL Server Management Studio (SSMS)**.

    1. Right-click on the server instance and select **Properties**.

    1. In the **Server Properties** window, go to the **Security** tab.

    1. Choose **SQL Server and Windows Authentication mode**.

    1. Restart SQL Server after making this change.

1. Create a dedicated SQL Server login (with a username and password) that CluedIn can use to connect. You can do this via SSMS:

    1. Under the **Security** node in SSMS, go to **Logins**.

    1. Right-click on **Logins** and select **New Login**.

    1. Choose **SQL Server authentication** and set the password.

    1. Assign the appropriate roles or permissions for the login to access the necessary databases.

    Once you’ve set up SQL Server Authentication and created a login for CluedIn, you can provide the login credentials (username and password) to connect CluedIn to your SQL Server instance.