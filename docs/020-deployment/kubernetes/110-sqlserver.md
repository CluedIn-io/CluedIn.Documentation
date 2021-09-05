---
layout: default
nav_order: 11
parent: Kubernetes
grand_parent: Deployment
permalink: /deployment/kubernetes/sql
title: SQL Server
tags: ["deployment", "kubernetes", "sqlserver"]
---
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

### Inside a pod

If using SQLServer as a deployment inside the cluster (instead of for example SQLAzure) two secrets will get created. One will contain the password for the SQLServer (which will be a randomly generated password), the other will contain the connection strings that will be consumed by various deployments.

### Custom SQL server (Sql Azure)

If you are using your own SQL installation, like SQL Azure, you will need to:

1. Install the database definitions (DACPACs) to your SQL instance. This can be done from the command line using [`SqlPackage.exe`](https://docs.microsoft.com/en-us/sql/tools/sqlpackage?view=sql-server-2017#publish-parameters-properties-and-sqlcmd-variables). 

2. Create a secret with the *connection strings* for each database. The secret should have the following keys:
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

3. You should then pass the name of the secret in the `values.yaml` override file:
```yaml
sqlserver:
    connectionsSecretName: my-connection-string-secret
```