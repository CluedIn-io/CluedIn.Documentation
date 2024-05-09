---
layout: cluedin
nav_order: 5
parent: Configuration
grand_parent: PaaS operations
permalink: /paas-operations/configuration/configure-logging
title: Logging
tags: ["deployment", "ama", "marketplace", "azure"]
last_modified: 2023-06-20
headerIcon: "paas"
---
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

In this article, you will get an overview of the logging options and learn how to configure the logging level that you need.

## Overview of logging

CluedIn uses structured logging. You can configure any sink, but only 3 sinks have been tested with the application: console, Seq, and Azure Application Insights.

**Console**

This sink is enabled by default.

**Seq**

By default, the Seq endpoint is protected with an OAuth2 proxy. To enable [Seq](https://datalust.co/seq), add the `seq` image that you want to use.

```yaml
seq:
  image: datalust/seq
```
You can access Seq using port-forwarding. Alternatively, you can enable an ingress route.

```yaml
seq:
  public_endpoint: /seq
```

**Azure Application Insights**

Add the key to the [Application Insights](https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview?tabs=net) instance that you want to use.


```yaml
logging:
  appInsightsKey: 'your-app-instance-key-guid'
```

By default, Azure Application Insights sends full telemetry of the front-end application. All the logs from the CluedIn server are sent as trace information.

### Log levels
By default, your CluedIn server containers are configured to log at the production level. The production-level log provides high-level information about the server and the tasks it is performing.

The production-level log can include log message types as described in the following table.


| Log message type | Description |
|----|----|
| INF | Informational messages |
| WRN | System warnings |
| ERR | System errors |
| FTL | Fatal system logs |

You can adjust the verbosity of the log messages that your system generates. To do that, change the value of the ASPNETCORE_ENVIRONMENT variable to one of the following values:

- **Production**
- **Development** or **debug**
- **Verbose** or **trace**

If you change the value of ASPNETCORE_ENVIRONMENT to **development** or **debug**, you will see log messages of the DBG type in addition to the four default types (INF, WRN, ERR, FTL).

If you need a more granular level of detail, set the value of ASPNETCORE_ENVIRONMENT to **verbose** or **trace**. As a result, the VRB type will be added in addition to DBG and the four default types.

### Log format and examples

By default, CluedIn provides logs to the console in the following format:  
`[#{ThreadId:000} {Timestamp:HH:mm:ss} {Level:u3}][{SourceContext}] {Message:lj}{NewLine}{Exception}`

Examples of log messages are provided in the following table.

| Log message type | Example |
|----|----|
| Information log message created by thread 001 at 11:38 | `[#001 11:38:53 INF] Operating System:             Unix 5.15.0.58` |
| Development/debug log message | `[#001 10:36:35 DBG] [ComponentHost] : Starting Metrics` |
| Verbose/trace log message | `[#015 10:42:11 VRB][CluedIn.Core.ExecutionContext] Operation GetByEntityCode (/Organization#CluedIn xxxxx-XXXX-xxxx-xxxx) : 5475` |

## Apply your log level
   
The following procedure shows how to get the current cluedin-server config map, edit the configuration, and apply the configuration to your Kubernetes cluster.

{:.important}
The example below uses a target namespace called **cluedin**. You may need to change the namespace to fit your implementation.

**To apply your log level**

1. Get the current configuration by running the following command:

    ```
    kubectl get configmap cluedin-server -o yaml > cluedin-server.yaml --namespace cluedin
    ```

    This command downloads the current cluedin-server config map into a local **cluedin-server.yaml** file.

2. Open the downloaded file in the text editor of your choice.

3. Change the value of ASPNETCORE_ENVIRONMENT to your required log level. You can use one of the following values: **production**, **development**, **debug**, **verbose**, or **trace**.
```yaml
apiVersion: v1
  Data:
    ASPNETCORE_ENVIRONMENT: debug
```

4. Apply the changed values from the local **cluedin-server.yaml** file to your Kubernetes cluedin-server config map by running the following command:

    ```
    kubectl apply -f cluedin-server.yaml --namespace cluedin
    ```

After you apply the values, they won’t become active until the pod is restarted. This is because the values are applied during the pod startup process. After the required pod is restarted, you should see additional log types in your logging target or in the pod logs. 

## Admin UIs

For debugging purposes, it is helpful to be able to log in to some of the tools/dependencies used by CluedIn. The easiest way to do this is to set up a proxy using a machine that has `kubectl` configured to access the cluster. You can use the following tools:

- [Neo4J](#neo4j)
- [RabbitMQ](#rabbitmq)
- [Redis](#redis)
- [ElasticSearch](#elasticsearch)
- [SQL Server](#sql-server)

In the following statements, `<name-of-release>` is how you named your Helm deployment. You can see the list of releases using `helm list`.

If you want to use several tools simultaneously, you can proxy several ports at the same time. The `port-forward` command used to set up the proxy will remain running. The proxy will be available until you stop the `port-forward` command.

### Neo4j
Neo4J is a graph database used to store the relationships between entities.

**To connect to Neo4j via port forwarding**

1. Run the following command:  
`kubectl port-forward $(kubectl get pod -o name -l 'release=<name-of-release>,app=neo4j') 7474 7687`

2. Point your browser to `localhost:7474`

### RabbitMQ
RabbitMQ is a messaging bus.

**To connect to RabbitMQ via port forwarding**

1. Run the following command:  
 `kubectl port-forward $(kubectl get pod -o name -l 'release=<name-of-release>,app=rabbitmq') 15672`

2. Point your browser to `localhost:15672`

### Redis
Redis is a storage of cache and key-value pairs.

**To connect to Redis via port forwarding**

1. Run the following command:
 ```
 powershell kubectl port-forward $(kubectl get pod -o name -l 'release=<name-of-release>,app=redis') 6379
 ```
2. Set up the front end for Redis on your computer using Docker. To do that, run the following command:
```
 docker run --rm -p 8081:8081 -e REDIS_HOSTS=local:host.docker.internal:6379 rediscommander/redis-commander
```
3. Point your browser to `localhost:8081`

### ElasticSearch
ElasticSearch is a search index.

**To connect to ElasticSearch via port forwarding**

1. Run the following command:
 ```
 kubectl port-forward $(kubectl get pod -o name -l 'release=<name-of-release>,app=elasticsearch') 9200
 ```
2. Point your browser to `localhost:9200/_plugin/inquisitor/#/`

### SQL Server

SQL Server is relational database.

**To connect to SQL Server via port forwarding**

1. Depending on the tool that you use, retrieve the password by doing one of the following actions:
    - If you are using bash shell, run the following command:
        `kubectl get secret <release-name>-cluedin-sql-password -o jsonpath="{.data.SA_PASSWORD}" | base64 --decode`

    - If you are using PowerShell, run the following command:
        `[System.Text.Encoding]::ASCII.GetString([System.Convert]::FromBase64String($(kubectl get secret <release-name>-cluedin-sql-password -o jsonpath="{.data.SA_PASSWORD}")))`

2. To expose the port locally using regular Kubernetes port-forwarding, run the following command:  
`kubectl port-forward $(kubectl get pod -o name -l 'release=<name-of-release>,app=sqlserver') 1433`

Then, you can use either Visual Studio or the MS SQL Management Studio to connect to the database on localhost. If there is already a SQL Server instance on your machine, there will be a port clash. If there is a conflict with the existing open ports on your machine, you can map the port to a different local port. To do that, use the following syntax:  
`kubectl port-forward <pod> <local-port>:<remote-port>`