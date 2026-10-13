---
title: Extension packages
url: https://documentation.cluedin.net/operate/local/step-3
content_type: how-to
section: Deploy & operate > Local deployment
---

# Extension packages

> how-to: Steps to accomplish one task.

In this article, you will learn how to add the **SQL Server Connector** extension package to CluedIn. This is our most commonly used package, and it allows you to stream data towards database instances.

## Overview of extension packages

To extend CluedIn with additional features—such as enrichers, export targets, and vocabularies—you can restore extension packages for the environment. Packages are made available through NuGet feeds. NuGet feeds are a convenient way to distribute and manage packages for your local development environment. These feeds can be hosted publicly, privately, or even on your local machine.

To facilitate local development, a preconfigured environment includes a specific folder called **packages/local NuGet**. This folder serves as a designated location where you can place locally built NuGet packages that need to be included in the CluedIn environment. The easiest way to integrate your locally built packages into CluedIn is to build your extension packages directly to this folder.

CluedIn has many built-in extension packages. To learn more, reach out to your CluedIn contact.

## Add SQL Server Connector to CluedIn

The following image presents an overview of the steps involved in adding SQL Server Connector to CluedIn.

![Diagram of adding SQL Server Connector in five steps: 1 add a reference for the extension package, 2 restore the package, 3 restart the CluedIn server, 4 check the server logs, 5 check the connector in CluedIn](https://documentation.cluedin.net/assets/images/deployment/local-sql-server-connector.gif)

In the procedure, we'll use the following input variables:

- `202401` – name of the environment

- `CluedIn.Connector.SqlServer` – name of the extension package.

**To add SQL Server Connector to CluedIn**

1. Add a reference to the package by running the following command:

    ```
    pwsh .\cluedin.ps1 packages 202401 -Add CluedIn.Connector.SqlServer
    ```

    You will get an output similar to the following.    

    ![Terminal output of pwsh .\cluedin.ps1 packages 202401 -Add CluedIn.Connector.SqlServer, confirming Added package CluedIn.Connector.SqlServer](https://documentation.cluedin.net/assets/images/local-install/add-package.png)

    You can also specify a version for your package (`-version`) and use floating versions (for example, `1.0.0-*`) for the latest pre-release.

1. Restore the package by running the following command:

    ```
    pwsh .\cluedin.ps1 packages 202401 -Restore
    ```

    You will get an output similar to the following.

    ![Terminal output of pwsh .\cluedin.ps1 packages 202401 -Restore, with the installer image layers downloading](https://documentation.cluedin.net/assets/images/local-install/restore-package.png)

1. Stop the CluedIn server by running the following command:

    ```
    pwsh .\cluedin.ps1 stop 202401
    ```

    You will get an output similar to the following.

    ![Terminal output of pwsh .\cluedin.ps1 stop 202401, with all 20 CluedIn containers Stopped](https://documentation.cluedin.net/assets/images/local-install/stop-cluedin-server.png)

1. Start the CluedIn server by running the following command:

    ```
    pwsh .\cluedin.ps1 up 202401
    ```

    You will get an output similar to the following.

    ![Terminal output of pwsh .\cluedin.ps1 up 202401, with all 20 CluedIn containers Running](https://documentation.cluedin.net/assets/images/local-install/start-cluedin-server.png)

    Starting the CluedIn server takes some time. When CluedIn starts up, it takes all extension assets from the disk and copies them into the container.

1.  After you start CluedIn, make sure the package was included. In Docker Desktop, select the CluedIn server and look for the similar section in logs.

    ![Docker Desktop logs of the CluedIn server container, highlighting CluedIn.Connector.SqlServer.dll being copied and Installing component extensions COMPLETE](https://documentation.cluedin.net/assets/images/local-install/sql-connector-logs.png)

1. In browser, open the CluedIn application and check if the SQL Connector is there. To do that, go to **Consume** > **Export Targets** > **Add Export Target**.

    ![The Add Export Target dialog on the Choose Target tab, with a search for Sql Server returning Sql Server Connector](https://documentation.cluedin.net/assets/images/local-install/sql-connector-app.png)

    The SQL Server Connector may take a few minutes to appear in the application.

## Results

You have added the SQL Server Connector extension package. Now, you are ready to stream data to Microsoft SQL Server databases.

## Next steps

- Learn more about CluedIn functionality in our [Getting started guide](https://documentation.cluedin.net/get-started/quickstart.md).

- Learn how to [install CluedIn from the Azure Marketplace](https://documentation.cluedin.net/operate/deployment-options/azure-marketplace.md).

Up: [Local deployment](https://documentation.cluedin.net/operate/local.md)
