---
layout: default
nav_order: 3
parent: Local
grand_parent: Installation
permalink: /deployment/local/step-3
title: Add extension packages
tags: ["deployment", "local"]
last_modified: 2023-06-30
---
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

In this article, you will learn how to add the **SQL Server Connector** extension package to CluedIn. This is our most commonly used package, and it allows you to stream data towards database instances.

# Overview of extension packages

To extend CluedIn with additional features—such as enrichers, export targets, and vocabularies—you can restore extension packages for the environment. Packages are made available through NuGet feeds. NuGet feeds are a convenient way to distribute and manage packages for your local development environment. These feeds can be hosted publicly, privately, or even on your local machine.

To facilitate local development, a preconfigured environment includes a specific folder called **packages/local NuGet**. This folder serves as a designated location where you can place locally built NuGet packages that need to be included in the CluedIn environment. The easiest way to integrate your locally built packages into CluedIn is to build your extension packages directly to this folder.

CluedIn has many built-in extension packages. To learn more about these extension packages, reach out your CluedIn contact.

# Add SQL Server Connector to CluedIn

The following image presents an overview of the steps involved in adding SQL Server Connector to CluedIn.

![add-sql-server-connector.png](../../assets/images/local-install/add-sql-server-connector.png)

In the procedure, we'll use following input variables:

- `202304` – name of the environment
- `2023.04` – version of CluedIn.
- `CluedIn.Connector.SqlServer` – name of the extension package.

**To add SQL Server Connector to CluedIn**

1. Add a reference for the package by running the following command:

    ```pwsh .\cluedin.ps1 packages 202304 -Add CluedIn.Connector.SqlServer```

    You will get an output similar to the following.    
 
    ![add-package.png](../../assets/images/local-install/add-package.png)

    **Note:** You can also specify a version for your package using `-version`. You can also use floating versions (for example, `1.0.0-*`) for the latest pre-release.

1. Restore the package by running the following command:

    ```pwsh .\cluedin.ps1 packages 202304 -Restore```

    You will get an output similar to the following.

    ![restore-package.png](../../assets/images/local-install/restore-package.png)

1. Stop the CluedIn server by running the following command:

    ```pwsh .\cluedin.ps1 stop 202304```

    You will get an output similar to the following.

    ![stop-cluedin-server.png](../../assets/images/local-install/stop-cluedin-server.png)

1. Start the CluedIn server by running the following command:

    ```pwsh .\cluedin.ps1 up 202304```

    You will get an output similar to the following.

    ![start-cluedin-server.png](../../assets/images/local-install/start-cluedin-server.png)

    **Note:** Starting the CluedIn server takes some time. When CluedIn starts up, it takes all extension assets from the disk and to copy them into the container.

1.  After you start CluedIn, make sure the package was included. In Docker Desktop, select the CluedIn server and look for the similar section in logs.

    ![sql-connector-logs.png](../../assets/images/local-install/sql-connector-logs.png)

1. In browser, open the CluedIn application and check if the SQL Connector is there. To do that, go to **Consume** > **Export Targets** > **Add Export Target**.

    ![sql-connector-app.png](../../assets/images/local-install/sql-connector-app.png)

    **Note:** The SQL Server Connector may take a few minutes to appear in the application.

# Results

You have added the SQL Server Connector extension package. Now you are ready to stream data to a SQL Database.

# Next steps

- Learn more about CluedIn functionality in our [Getting started guide](/getting-started).

- Learn how to [install CluedIn from the Azure Marketplace](/deployment/azure-marketplace).