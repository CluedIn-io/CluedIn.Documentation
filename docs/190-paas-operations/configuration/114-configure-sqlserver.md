---
layout: cluedin
nav_order: 16
parent: Configuration
grand_parent: PaaS operations
permalink: deployment/kubernetes/sql
title: SQL Server
tags: ["deployment", "kubernetes", "sqlserver"]
headerIcon: "paas"
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

{:.important}
To run SQL Server in production environment, you should have a valid Microsoft SQL Server license. Learn more about licensing [here](https://www.microsoft.com/en-us/sql-server/sql-server-2022-pricing).

## Inside the cluster

By default, SQL Server is deployed within the cluster. This is currently the recommended approach. However, it is possible to deploy to Azure SQL instead. When deployed inside the cluster, two secrets will get created. One will contain the password for the SQL Server (which will be a randomly generated password), the other will contain the connection strings that will be consumed by various deployments.

## Custom SQL server (Azure SQL)

If you are using your own SQL installation, like Azure SQL, you will need to do the following:

1. Install the database definitions (DACPACs) to your SQL instance. This can be done from the command line using [`SqlPackage.exe`](https://docs.microsoft.com/en-us/sql/tools/sqlpackage?view=sql-server-2017#publish-parameters-properties-and-sqlcmd-variables). 

1. Create a secret with the **connection strings** for each database. The secret should have the following keys:
    ```yaml
    apiVersion: v1
    kind: Secret
    metadata:
      name: my-connection-string-secret
    type: Opaque
    data:
      AuthenticationStore: <connection-string>
      BlobStorage: <connection-string>
      ConfigurationStore: <connection-string>
      CluedInEntities: <connection-string>
      TokenStore: <connection-string>
      Training: <connection-string>
      ExternalSearch: <connection-string>
      ML-Logging: <connection-string>
      Metrics: <connection-string>
    ```

1. Pass the name of the secret in the `values.yaml` override file:
    ```yaml
    application:
      sqlserver:
        connectionsSecretName: my-connection-string-secret
    ```