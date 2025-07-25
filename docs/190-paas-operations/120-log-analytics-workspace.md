---
layout: cluedin
title: Review logs in Log Analytics workspace
parent: PaaS operations
permalink: paas-operations/review-logs-in-log-analytics-workspace
nav_order: 12
headerIcon: "paas"
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article, you will learn how to review logs from all CluedIn services in your Log Analytics workspace.

## Retrieve logs

1. In the [Azure portal](https://portal.azure.com/), go to your Log Analytics workspace.

    ![log-analytics-workspace.png]({{ "/assets/images/paas-operations/log-analytics-workspace.png" | relative_url }})

1. On the left navigation pane of the Log Analytics workspace, select **Logs**. Then, close the **Queries hub** pop-up window. This will open the query editor where you can run queries to retrieve logs.

1. Run the following query in the Log Analytics workspace. Replace `{name of service}` with the appropriate service name from the [mapping reference table](#service-name-to-pod-name-mapping).

    ```
    KubePodInventory
    | where ServiceName == {name of service}
    | distinct ContainerID
    | join( 
        ContainerLog 
        | project ContainerID, LogEntry, TimeGenerated
    ) on ContainerID
    | order by TimeGenerated asc
    | project  TimeGenerated, LogEntry
    ```

    This query retrieves logs for the specified service, orders them chronologically, and displays the log entries along with their timestamps.

## Example of retrieving logs for cluedin-server pod

If you want to retrieve logs for the cluedin-server pod, do the following:

1. Identify the corresponding service name from the [mapping reference table](#service-name-to-pod-name-mapping): `cluedin-clean-auth`.

1. Run the following query in the Log Analytics workspace:

    ```
    KubePodInventory
    | where ServiceName == "cluedin-clean-auth"
    | distinct ContainerID
    | join( 
        ContainerLog 
        | project ContainerID, LogEntry, TimeGenerated
    ) on ContainerID
    | order by TimeGenerated asc
    | project  TimeGenerated, LogEntry
    ```

    ![query-example.png]({{ "/assets/images/paas-operations/query-example.png" | relative_url }})

    This query will return logs related to the cluedin-server pod.

    ![logs-example.png]({{ "/assets/images/paas-operations/logs-example.png" | relative_url }})

## Service name to pod name mapping

| Service name | Pod name |
|--------------|----------|
|cluedin-haproxy-ingress| cluedin-haproxy-ingress |
|cluedin-libpostal| cluedin-libpostal |
|cluedin-clean-auth|cluedin-server|
|cluedin-server-processing|cluedin-server-processing|
|cluedin-datasource|cluedin-datasource|
|cluedin-datasource-processing|cluedin-datasource-processing|
|cluedin-datasource-submitter|cluedin-datasource-submitter|
|cluedin-gql|cluedin-gql|
|cluedin-elasticsearch|cluedin-elasticsearch|
|cluedin-rabbitmq|cluedin-rabbitmq|
|cluedin-controller|cluedin-controller|
|cluedin-neo4j|cluedin-neo4j|
|cluedin-sqlserver|cluedin-sqlserver|
|cluedin-openrefine|cluedin-openrefine|
