---
layout: cluedin
nav_order: 5
parent: CluedIn upgrade guide
grand_parent: Upgrade
permalink: /paas-operations/upgrade/guide/resolve-common-upgrade-issues
title: Resolve common upgrade issues
tags: ["deployment", "ama", "marketplace", "azure", "aks", "kubernetes", "upgrade"]
last_modified: 2025-09-22
headerIcon: "paas"

---
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

Even with careful preparation, upgrades may sometimes encounter issues. This section describes the most common issues you might face during or after the [CluedIn upgrade process](/paas-operations/upgrade/guide) and provides guidance on how to resolve them quickly.

## Scenario 1: CrashLoopBackOff state 
A pod is in a **CrashLoopBackOff** state, the container keeps starting, failing, and restarting in a loop. 

In this case, when you run `kubectl get pods –n cluedin`, you will see similar output showing a high number of restarts and the **CrashLoopBackOff** status. 

```
NAME                              READY STATUS           RESTARTS AGE
----                              ----- ------           -------- ---
cluedin-ui-7d9f8d7c9d-abc12       0/1   CrashLoopBackOff 9        5m
```

To troubleshoot this, it is important to review the logs of the previous container instance, not the current one that is restarting. The previous logs usually contain the exact error message that caused the crash. These logs often appear near the last few lines of the output. 

To check previous logs from before a pod crashed, add the `–p` (stands for previous) flag at the end of the `kubectl logs` command:
 
```
kubectl logs <pod name> -n cluedin –p 
```

**Example**
Running the above command:

**Returns**

```powershell
2025-09-25 09:35:09.212+0000 INFO  Starting Neo4j.
2025-09-25 09:35:09.522+0000 INFO  Setting max memory usage to 1.5GiB
2025-09-25 09:35:11.785+0000 INFO  Performing database recovery...
2025-09-25 09:35:14.120+0000 INFO  Recovery complete.
2025-09-25 09:35:14.785+0000 INFO  Starting Bolt connector on 0.0.0.0:7687
2025-09-25 09:35:15.333+0000 ERROR OutOfMemoryError: Java heap space
2025-09-25 09:35:15.335+0000 INFO  Neo4j shutting down due to fatal error
```

The error indicates that the Neo4j container was terminated due to insufficient memory (OutOfMemoryError: Java heap space).
This typically occurs when either:

  - The container’s memory limit is set too low for the workload, or
  - Neo4j’s internal memory settings (heap, page cache, etc.) are too aggressive for the available resources.

**Resolution**
Increase the memory limit assigned to the Neo4j StatefulSet.

------

## Scenario 2: Pod not ready
A pod can be in the **Running** state but still marked as **Not Ready** if it is failing its readiness probes. This situation occurs when [Kubernetes](/paas-operations/upgrade/guide/required-tools#kubernetes) has successfully started the pod, but the application inside is not yet prepared to handle traffic. In other words, the container is alive, but it cannot serve requests.

In this case, when you run `kubectl get pods –n cluedin`, you will see similar output: 

```powershell
NAME                              READY STATUS   RESTARTS AGE
----                              ----- ------   -------- ---
cluedin-ui-7d9f8d7c9d-abc12       0/1   Running  0        5m
```

To investigate whether a pod is failing due to a readiness probe, do the following:

1. Describe the pod and review the events section at the bottom of the output.

    You may see warnings similar to the following:

    ```powershell
    Warning  Unhealthy  2m (x4 over 4m)  kubelet  Readiness probe failed: {{reason}}
    ```

    If you find repeated **Readiness probe failed** events, this confirms that the pod is starting but failing to pass the readiness check. For example, a pod might be running but remain **Not Ready** until it successfully connects to its database. In this case, the readiness probe will continue to fail until the dependency becomes available.

    Example:
    ```
    kubectl logs <pod-name> -n cluedin 
    ```

    Returns the following:
    ```powershell
    2025-09-19T10:25:12Z INFO Starting CluedIn ... 
    2025-09-19T10:25:15Z WARN Waiting for database connection... 
    2025-09-19T10:25:30Z ERROR Timeout connecting to SQL at db-service:4133 
    ```

1. Examine the container logs, which may provide additional details on why the application is not ready to serve traffic.

1. Resolve the issue. In this example, the issue must be resolved by fixing the connectivity between the pod and the database.

    Common causes include:

    - A misconfigured connection string (for example, wrong host, port, username, or password).

    - The database may be under resource pressure (for example, CPU or memory exhaustion), which can prevent it from accepting new connections.

    Addressing these problems will allow the pod to pass its readiness probe and become ready to serve traffic.

------

## Scenario 3: Pod running and ready, but application exhibits unexpected behaviour

In some cases, a pod may be in the **Running** state and marked as **Ready**, but the application inside still shows unexpected or faulty behaviour. This indicates that the pod has passed its liveness and readiness probes, but the underlying issue lies within the application itself.

1. To begin diagnosing the issue, run the following command:

    ```
    kubectl get pods –n cluedin 
    ```
    The output will be similar to the following:

    ```powershell
    NAME                              READY STATUS   RESTARTS AGE
    ----                              ----- ------   -------- ---
    cluedin-ui-7d9f8d7c9d-abc12       1/1   Running  0        5m
    ``` 

    This usually means that the problem is not with [Kubernetes](/paas-operations/upgrade/guide/required-tools#kubernetes) itself, but with the application inside the pod, or with network access between the user and the pod. 
 
1. Even if a pod appears healthy, the application inside might be failing silently. To check for hidden errors, review the pod logs by running the following command: 

    ```
    kubectl logs <pod name> -n cluedin 
    ```

    If you want to read the log in a more convenient way, you can download it to a file and open it with any file reader. 

    ``` 
    kubectl logs <pod name> -n cluedin  >  <podname>.log 
    ```

**Example**
Given we have a pod with the name `cluedin-gql-97cb77cd6-d5rcz`.

```powershell
kubectl logs cluedin-gql-97cb77cd6-d5rcz -n cluedin 
```

**Returns**

```powershell
14:48:32.145Z ERROR CluedIn.UI.GQL/CluedIn.UI.GQL: 500: Internal Server Error
err: {
"message": "500: Internal Server Error",
"locations": [
{
"line": 109,
"column": 7
}
],
"path": [
"inbound",
"dataSource",
connectorConfiguration
],
"extensions": {
"code": "INTERNAL_SERVER_ERROR",
"response": {
"url": "http://cluedin-server:9000/api/v1/configuration/providers?id=FA871776-60CA-49A6-8433-42BEE288400E",
"status": 500,
"statusText": "Internal Server Error",
"body": "{\"type\":\"https://tools.ietf.org/html/rfc7231#section-6.6.1\",\"title\":\"An error occurred while processing your request.\",\"status\":500,\"detail\":\"Our job server is down and not accepting new providers for now\",\"traceId\":\"00-cc0351878f70a5edc267cdca4409b4b9-129d08969588f435-00\"}"
}
}
}
```

In this example, the issue may be related to a failed connection to our job server (Redis).

Commonly caused by the `cluedin-server` starting before Redis, preventing it from establishing a proper connection during boot.

**Resolution**
Restart the deployment `cluedin-server` to ensure it reconnects to Redis correctly at startup:

```
kubectl rollout restart deployment cluedin-server -n cluedin
```

## Scenario 4: Pod pending due to init container issues

A pod can contain one or more application containers, and may also include one or more init containers.

- Init containers run sequentially before the main application containers start. Each must complete successfully before any main container in the pod can begin running.

- If an init container fails or cannot complete, the main container responsible for serving traffic may remain stuck in the **Pending** state. This means that the pod never progresses to running the main workload.

To verify whether a pod is unable to start because of a failing init container, describe the pod with the following command:

```
kubectl describe pod <pod-name> -n cluedin
```

The output will be similar to the following:

```powershell
Name:           cluedin-ui-879c4db6b-8jzks 
Namespace:      cluedin 
Status:         Pending 
Controlled By:  ReplicaSet/cluedin-ui-879c4db6b 
 
Init Containers: 
  wait-cluedin-gql: 
    Image:      cluedinprod.azurecr.io/groundnuty/k8s-wait-for:v1.3 
    State:      Terminated 
      Reason:   Error 
      Exit Code: 1 
    Restart Count: 3 
    Args: 
      service 
      cluedin-gql 
      -n 
      cluedin 
Containers: 
  ui: 
    Image:      cluedinprod.azurecr.io/cluedin/ui:2024.12.02 
    State:      Waiting 
      Reason:   PodInitializing 

Events: 
  Type      Reason     Age   From     Message 
  ----      ------     ----  ----     ------- 
  Warning   Failed     5m    kubelet  Init container "wait-cluedin-gql" failed 
```

In the example above:

- The main container named `ui` is in the `Waiting` state. This usually means it is waiting for the init containers to complete successfully.

- The events show that the init container `wait-cluedin-gql` has failed. In such cases, the pod cannot progress to running the main container until the init container issue is resolved.

Sometimes, an init container may run indefinitely without explicitly failing. In both scenarios, it is useful to inspect the init container logs for more details. You can view the logs of a specific init container by adding the `-c <init-container-name>` flag to the `kubectl logs` command:

```
kubectl logs <pod-name> -n cluedin -c <init-container-name>
```

This will help you understand why the init container is failing or stuck, and therefore why the main container cannot proceed.