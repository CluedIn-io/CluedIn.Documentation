---
category: Get Started
title: Monitoring the application
hideMenu: true
---

## Logging 

CluedIn uses structured logging. You can configure any sink, but only 3 have been tested with the application.
1. Console: this sink is enabled by default.

1. [Seq](https://datalust.co/seq): To enable it, you just need to add the `seq` image you want to use:
    ```yaml
    seq:
        image: datalust/seq
    ```
    
    You can access it using port-forwarding or you could enable an ingress route:
    ```yaml
    seq:
        public_endpoint: /seq
    ```
    By default the seq endpoint is protected with an [Oauth2 proxy](/docs/0-gettingStarted/oauth2.html).
1. [Azure Application Insights](https://docs.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview)
    All you need to do is add the key for the Application Insights instance you want to use:
    ```yaml
    logging:
        appInsightsKey: 'your-app-instance-key-guid'
    ```
    By default it will send full telemetry of the frontend application, and all the logs from the CluedIn server will be sent as trace information.

## Admin UIs
It is sometimes useful, for example for debugging purposes, to be able to log in to some of the tools / dependencies that CluedIn uses. The easiest way is to set up a proxy using a machine that has ```kubectl``` configured to access the cluster.

In the following statements the ```<name-of-release>``` is how you named your helm deployment. You can see the list of releases using ```helm list```.

You can proxy several ports at the same time if you want to use several tools simultaneously. The ```port-forward``` instruction used to set up the proxy, will just remain running. The proxy will be available whilst you don't terminate the ```port-forward``` instruction.

### Neo4j
Graph database used to store the relationships between entities. 

```powershell
kubectl port-forward $(kubectl get pod -o name -l 'release=<name-of-release>,app=neo4j') 7474 7687
```

Then point your browser to ```localhost:7474```

### RabbitMq
Messaging bus.

```powershell
kubectl port-forward $(kubectl get pod -o name -l 'release=<name-of-release>,app=rabbitmq') 15672
```
Then point your browser to ```localhost:15672```

##### Redis
Cache and key-value pair storage.

```powershell
kubectl port-forward $(kubectl get pod -o name -l 'release=<name-of-release>,app=redis') 6379
```
Redis has no default frontend. But you could stand one up in your computer using docker. 

```powershell
docker run --rm -p 8081:8081 -e REDIS_HOSTS=local:host.docker.internal:6379 rediscommander/redis-commander
```
Then point your browser to ```localhost:8081```

### ElasticSearch
Search index.

```powershell
kubectl port-forward $(kubectl get pod -o name -l 'release=<name-of-release>,app=elasticsearch') 9200
```
Then point your browser to ```localhost:9200/_plugin/inquisitor/#/```

### SqlServer
Well-known relational Database. You can retrieve the password by executing this command in a bash shell:
```bash
kubectl get secret <release-name>-cluedin-sql-password -o jsonpath="{.data.SA_PASSWORD}" | base64 --decode
```

Or using Powershell:
```powershell
[System.Text.Encoding]::ASCII.GetString([System.Convert]::FromBase64String($(kubectl get secret <release-name>-cluedin-sql-password -o jsonpath="{.data.SA_PASSWORD}")))
```

The port can be exposed locally using regular Kubernetes port-forwarding:

```powershell
kubectl port-forward $(kubectl get pod -o name -l 'release=<name-of-release>,app=sqlserver') 1433
```
You can then use Visual Studio, or the MSSQL Management Studio to connect to the database on localhost. If there is already a SQLServer instance in your machine, there will be a port clash. See note below to map to a different local port.

*Note*: You can map the port to a different local port if there is a conflict with existing open ports in your machine using the syntax ```kubectl port-forward <pod> <local-port>:<remote-port>```
