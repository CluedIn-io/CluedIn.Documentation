---
layout: cluedin
title: Azure SQL migration
parent: PaaS operations
permalink: /paas-operations/azure-sql-migration
nav_order: 15
headerIcon: "paas"
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

This document outlines the process of provisioning Azure SQL infrastructure and migrating data from an existing in-cluster SQL database to Azure SQL.

The process is split into two parts:

1. Azure SQL Server Creation
1. Migrating Existing SQL to Azure SQL

## Overview
This migration is designed to run entirely within the AKS cluster, leveraging an in-cluster job that:

Connects to both the existing in-cluster SQL instance and the target Azure SQL Database

Exports the data from the in-cluster SQL as a BACPAC file

Uploads the BACPAC file to an Azure Storage Account

Imports the BACPAC into the Azure SQL database

This approach ensures secure, seamless, and auditable data migration without requiring any manual data export/import actions outside of the cluster.

![azure-sql-migration.png]({{ "/assets/images/paas-operations/azure-sql-migration.png" | relative_url }})

![sql-migration-blocks.png]({{ "/assets/images/paas-operations/sql-migration-blocks.png" | relative_url }})

## Azure SQL Server Creation

**Pre-requisites**:

Ensure the current instance is upgraded with 4.6.0 (Egret)

Ensure the following Azure role assignments:

- Contributor
- Network Contributor
- Private DNS Zone Contributor

Get the Bicep template from `Global Ops` 

1. Prepare Input Parameters: 

    - Update the Vnet & subnet IDs
    - Update the Azure SQL username & password
    - Change the specs if you want to choose different from default

1. Run Bicep Template:

    It Deploys the following components:
    - Azure SQL Server
    - Elastic Pool (optional)
    - CluedIn Databases
    - Private endpoint
    - Private DNS zone

1. Validation Checklist:

- SQL server successfully provisioned
- Private endpoint connected and DNS resolving
- SQL server reachable via Azure Data Studio or sqlcmd from within the VNet

## Migrating Existing SQL to Azure SQL

**Pre-requisites**
1. Scale Down Data Processing:
    ```bash
    kubectl scale deploy cluedin-server cluedin-server-processing cluedin-datasource-processing cluedin-datasource-submitter cluedin-gql cluedin-ui -n cluedin --replicas=0 --timeout 5m
    ```
1. Patch Persistent Volume:

    Ensure in-cluster SQL disk isn't deleted on PV release:
    ```bash
    kubectl patch pv <pv-name> -p '{"spec":{"persistentVolumeReclaimPolicy":"Retain"}}'
    ```
1. Check the existing in-cluster SQL DB size to estimate migration time:
    ```bash
    kubectl exec -it <cluedin-sql-pod-name> -n cluedin -- /opt/mssql-tools/bin/sqlcmd \
      -S localhost -U sa -P <SA_PASSWORD> \
      -Q "SET NOCOUNT ON;
      CREATE TABLE #Space (DBName SYSNAME, DataSize NVARCHAR(50), LogSize NVARCHAR(50));
      EXEC sp_MSforeachdb 'USE [?];
      INSERT INTO #Space
      SELECT DB_NAME(), (SELECT SUM(size)*8/1024 FROM sys.database_files WHERE type_desc=''ROWS''), (SELECT SUM(size)*8/1024 FROM sys.database_files WHERE type_desc=''LOG'');';
      SELECT DBName AS [Database], DataSize AS [Data(MB)], LogSize AS [Log(MB)] FROM #Space;
      DROP TABLE #Space;"
    ```
  If any DB is larger than 30GB, consider increasing the individual DB storage size on Azure SQL. All the DBs are created with 32GB by default.

**Migration Steps**

1. Get the migration script & update SQL Secrets:

    Edit your Kubernetes YAML to include the new Azure SQL host, username, and password. And update the in-cluster SQL secret

1. Apply Migration Manifest:
    ```bash
    kubectl apply -f cluedin-sql-migration.yaml -n cluedin
    ```

1. This job will:
    - Connect to the in-cluster SQL
    - Export DB to BACPAC
    - Upload BACPAC to Azure Storage
    - Import BACPAC into Azure SQL

1. Monitor Job Logs:
    ```bash
    kubectl logs job/<sql-migration-job-name> -n cluedin
    ```

1. Verify Data in Azure SQL:
  - Connect using Azure Data Studio or sqlcmd
  - Validate that table counts and data match the original in-cluster database

## Helm Upgrade (Post-Migration)

1. Backup Existing in-cluster SQL Secret:
    ```bash
    kubectl get secret cluedin-sqlserver-secret -n cluedin -o yaml > sql-secret-backup.yaml
    ```
1. Update Helm Values:

    Backup the current helm values and rename it to new values.yaml and insert the Azure SQL connection values into the new values.yaml.
    ```yaml
    application:
      sqlserver:
        host: <AZURE_SQL_SERVER>.database.windows.net
        isExternal: true
        connectionOptions:
          timeout: 15
          encrypt: true
          extraParameters: "Max Pool Size=200;Pooling=True;"
        users:
          sa:
            username: <AZURE_SQL_ADMIN_USERNAME>
            passwordSecretName: cluedin-sqlserver-secret
      cluedincontroller:
        hosts:
          sqlserver:
            host: <AZURE_SQL_SERVER>.database.windows.net
            connectionOptions:
              encrypt: true
              extraParameters: Max Pool Size=200;Pooling=True;
              timeout: 15
              isExternal: true
            users:
              sa:
                passwordSecretName: cluedin-sqlserver-secret
                username: <AZURE_SQL_ADMIN_USERNAME>
    infrastructure:
      mssql:
        enabled: false
    platform:
      extraSecrets:
        cluedin-sqlserver-secret:
          sapassword: <Azure_SQL_ADMIN_PASSWORD>
    ```
    **note:** If keyvault is used, update the keyvault secret `cluedin-mssql-sa-password` with new Azure SQL password 

1. Scale down the in-cluster SQL deployment and remove the sql secret cluedin-sqlserver-secret

1. Run Helm Upgrade:
    ```bash
    helm upgrade -i cluedin-platform -n cluedin cluedin-platform/cluedin-platform --version 2.6.x --values values.yaml --set application.system.runDatabaseJobsOnUpgrade=true
    ```
1. Post-Deployment Checks:
    - All pods should be in Running state
    - UI should be accessible
    - Run sanity tests