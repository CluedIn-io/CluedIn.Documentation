---
layout: default
nav_order: 12
parent: Kubernetes
grand_parent: Deployment
permalink: /deployment/kubernetes/monitoring
title: Monitoring
tags: ["deployment", "kubernetes", "monitoring"]
---
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}
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
    By default the seq endpoint is protected with an [OAuth2 proxy](./oauth).
1. [Azure Application Insights](https://docs.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview)
    All you need to do is add the key for the Application Insights instance you want to use:
    ```yaml
    logging:
        appInsightsKey: 'your-app-instance-key-guid'
    ```
    By default it will send full telemetry of the frontend application, and all the logs from the CluedIn server will be sent as trace information.
### Log Levels
By default your CluedIn server containers are configured to log at a Production level. The Production log level gives you the ability to gain high level information regarding the server and the tasks it is undertaking. The production logging level will output the following log entry types

    -	**INF**   informational messages 
    -	**WRN** system warnings
    -	**ERR**  system errors 
    -	**FTL**  Fatal system logs

    The verbosity of the log messages your system generates can be adjusted buy changing the required value of ASPNETCORE_ENVIRONMENT variable to one of the following values
        -	Production
        -	Development or debug
        -	verbose or trace

    When the value of ASPNETCORE_ENVIRONMENT is changed to development or debug you will see log messages of the DBG type in addition to the 4 default types. In the event a more granular level of detail is required setting ASPNETCORE_ENVIRONMENT to the value of trace or verbose will enabled messages of type VRB in addition to DBG and the four production types 

    <table>
    <colgroup>
    <col width="30%" />
    <col width="70%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th>Logging Level</th>
    <th>Message Types</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td markdown="span">Production</td>
    <td markdown="span"> INF,WARN,ERR,FTL </td>
    </tr>
    <tr>
    <td markdown="span">Development/Debug</td>
    <td markdown="span">DBG</td>
    </tr>
    <tr>
    <td markdown="span">Trace/Verbose</td>
    <td markdown="span">VRB</td>
    </tr>
    </tbody>
    </table>



    #### Logging Format & Examples

    CluedIn by default will provide logs to the console  in the format shown below  

    **Log Format**

    ```[#{ThreadId:000} {Timestamp:HH:mm:ss} {Level:u3}][{SourceContext}] {Message:lj}{NewLine}{Exception}```

    Example of an information message created by thread 001 at 11:38 of the type information 
    ```[#001 11:38:53 INF] Operating System:             Unix 5.15.0.58```
        
    The following is an example log  of development/debug logging
    ```[#001 10:36:35 DBG] [ComponentHost] : Starting Metrics```

    The following is an example log  of verbose/ trace logs 
    ```[#015 10:42:11 VRB][CluedIn.Core.ExecutionContext] Operation GetByEntityCode (/Organization#CluedIn xxxxx-XXXX-xxxx-xxxx) : 5475```

    **Applying your Log Level** 

    **Config Map**

    The following commands show the process for getting the current cluedin-server config map,  editing the configuration and applying the configuration to your kubernates cluster . 

    {: .highlight }
    > **Note**
    >Note In the example below uses a target namespace called cluedin you might need to amend this to fit your implementation 

    **Get current configuration**

    The following command will download the current cluedin-server config map into a local file called cluedin-server.yaml. This can be edited by any text editor vi,nano,vscode etc
    ~~~~
    kubectl get configmap cluedin-server -o yaml > cluedin-server.yaml --namespace cluedin
    ~~~~

    **Edit the configuration** 

    Using a text editor of your choice open the file you created in the previous step.  edit the value after  the ASPNETCORE_ENVIRONMENT:  to your required log levels using one of the six values shown in the previous table. 
    ```example ASPNETCORE_ENVIRONMENT: debug``` 


    **Config Snipet**
~~~~
    apiVersion: v1
    Data:
      ASPNETCORE_ENVIRONMENT: debug
~~~~
    **Applying the configuration**

    The following command will apply the newly amended values from the local cluedin-server.yaml we created in the previous step to your kubernates cluedin-server config map 
    ~~~~
    kubectl apply -f cluedin-server.yaml --namespace cluedin
    ~~~~

    **Enabling & verifying** 

    Once the values have been applied they will not be active until the pod has been restarted as these values are applied during the pod start up process. Once the required pod has been restarted you should see any additional log types in your logging target or the pod logs   



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

### Redis
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

Or using PowerShell:
```powershell
[System.Text.Encoding]::ASCII.GetString([System.Convert]::FromBase64String($(kubectl get secret <release-name>-cluedin-sql-password -o jsonpath="{.data.SA_PASSWORD}")))
```

The port can be exposed locally using regular Kubernetes port-forwarding:

```powershell
kubectl port-forward $(kubectl get pod -o name -l 'release=<name-of-release>,app=sqlserver') 1433
```
You can then use Visual Studio, or the MSSQL Management Studio to connect to the database on localhost. If there is already a SQLServer instance in your machine, there will be a port clash. See note below to map to a different local port.

*Note*: You can map the port to a different local port if there is a conflict with existing open ports in your machine using the syntax ```kubectl port-forward <pod> <local-port>:<remote-port>```
