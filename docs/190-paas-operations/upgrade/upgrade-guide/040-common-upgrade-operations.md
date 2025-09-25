---
layout: cluedin
nav_order: 4
parent: CluedIn upgrade guide
grand_parent: Upgrade
permalink: /paas-operations/upgrade/guide/common-upgrade-operations
title: Common upgrade operations
tags: ["deployment", "ama", "marketplace", "azure", "aks", "kubernetes", "upgrade"]
last_modified: 2025-09-22
headerIcon: "paas"

---
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

This section outlines common CluedIn activities you may need to carry out during the [CluedIn upgrade process](/paas-operations/upgrade/guide). It is designed to provide practical steps and references that help you keep your CluedIn environment running smoothly.

## Check CluedIn UI 

A successful load of the CluedIn UI is a strong indication that your installation is functioning correctly. 

To access the UI, use the URL that was configured during installation (please obtain this from your administrator). This URL may be either public or private: 

  - Public URL – Accessible from any network without restrictions. 
  - Private URL – Requires that you are connected to the correct internal or VPN network. Ensure you have the necessary access before attempting to open the UI. 

**Do You Have a Login?**
There are two main methods for granting users access to CluedIn. The user has been provided access via one of the following:  

- **SSO (Single Sign-On)** – Your administrator must grant you access through your organization’s SSO provider.  
- **Invitation Email** – Your CluedIn administrator will send you an email invite to join.

**Checking the UI**
Log into CluedIn, the home dashboard should appear almost instantly. Click through the left hand menu, all pages should appear almost instantly. Perform a search in the top menu, click on any of the entities in the results and browse through the entity tabs. All tabs should respond quickly.

{:.important}
If any page takes longer than 5 seconds to load, it may indicate a performance issue or that the upgrade has not fully completed.

------------

## Check CluedIn Pods 
Monitoring the state of pods is a routine task in Kubernetes, and it becomes especially critical during installation and upgrade processes. Verifying that pods are running and healthy ensures the CluedIn platform is functioning correctly and that any new deployments are stable. 

**Prerequisites**
Before checking the pods, make sure you are already connected to the target Kubernetes cluster via a valid **kubeconfig** file. Without this connection, you won’t be able to query the cluster. 

**Checking Pod States** 
To view the status of all CluedIn pods, run the following command: 

```powershell
kubectl get pods -n cluedin 
```

The command returns a list of all pods in the CluedIn namespace (-n cluedin) along with their current state (e.g., Running, Pending, CrashLoopBackOff, Completed, Succeeded, Failed). This provides quick visibility into whether services are healthy or require troubleshooting. Ideally, all pods should be in a Running or Completed state.

**All Pods in Running or Completed state** 
All pods in **Running** or **Completed** state indicate that your CluedIn installation is healthy and the infrastructure is actively running.

If all pods are **Green/Running** but the application still has issues, check the pod logs. See the **Checking CluedIn Logs** section for details.

**Pods in Pending state**
If some pods remain in a **Pending** state, allow a few minutes for them to transition to **Running**.  
- If a pod is still pending after **5 minutes**, review the logs to identify the cause. 

**Pods in CrashLoopBackOff state**
When a pod is in a CrashLoopBackOff state, it means Kubernetes is repeatedly trying to start the pod, but the container inside it keeps failing and crashing. After each crash, Kubernetes waits a little longer before attempting to restart it again (the “backoff” part).

Common Causes
  - **Configuration errors** – such as incorrect environment variables, secrets, or config maps. *Note: CluedIn config maps are complex. If changes have been made to the recommended configurations, revert them to the default settings.*  
  - **Application errors** – the application may crash on startup due to bugs, missing dependencies, or incompatible versions.  
  - **Resource limits (most common)** – the container may not have sufficient CPU or memory and is killed by the system.  
  - **Permission or connectivity issues** – for example, firewall changes or Azure policies may block the pod from starting.  

More detail on a pod not starting or in a crash loop state can be found by running this command:

```powershell
kubectl describe pod <pod-name> -n cluedin 
```

------------

## Check CluedIn logs
All CluedIn pods generate logs that provide detailed information about what the system is doing.These logs help you:  
  - Confirm that services are running smoothly.  
  - Diagnose issues when problems occur.  
  - Gain visibility into the internal behavior of the system.  

Reviewing pod logs is an essential step in troubleshooting errors or verifying that your installation is functioning correctly.

To check logs of pod, run below command: 

```powershell
kubectl logs <pod name> -n cluedin 
```

Pod logs are especially useful for troubleshooting in the following scenarios:  

  - **CrashLoopBackOff** – when a pod repeatedly fails to start.  
  - **Running but Not Ready** – when readiness probes fail even though the pod is running.  
  - **Running and Ready, but Application Misbehaving** – when the pod looks healthy but the application itself is not functioning correctly.  
  - **Init Containers Delayed or Failing** – when initialization steps take too long or do not complete successfully.  


NOTE: Logs stored in kubernetes pod are limited to the default 10MB of size, if it grow more than that, older log will no longer be visible by using kubectl logs. If you have log analytic configured to collect pod logs, it is advisable to use that to read pod logs. 

------

## Check CluedIn queues
This guide explains how to identify and troubleshoot issues with CluedIn queues, which are powered by a messaging system called RabbitMQ.

**What are RabbitMQ Queues?**
RabbitMQ is a message broker – it allows different parts of CluedIn to communicate by passing messages between them.

  - Think of a queue as a waiting line for messages.
  - One service in CluedIn places messages onto the queue.
  - Another service takes messages off the queue and processes them.

This setup helps CluedIn handle large volumes of data reliably and asynchronously.

**Why Are Queues Important?**

If queues stop working correctly, CluedIn may not be able to move data between services efficiently. Common symptoms include:

  - Queues growing indefinitely (messages are piling up but not being processed).
  - Queues stuck (no new messages are being consumed).

Services that depend on these messages may experience failures or degraded performance.

By checking the queues, you can quickly determine if CluedIn’s internal messaging system is healthy, or if a backlog or failure might be affecting the platform.

**Accesing rabbitmq**
Run this command to get access the rabbitmq credentials. 
 
```powershell
kubectl get secret cluedin-rabbitmq -n cluedin -o jsonpath="{.data.rabbitmq-password}" | base64 --decode 
```

RabbitMQ includes a built-in management UI. To access it, you first need to open a port forward to the RabbitMQ pod:

```powershell
#kubectl port-forward service/cluedin-rabbitmq 15672:15672 -n cluedin 
```
Returns
```powershell
Forwarding from 127.0.0.1:15672 -> 15672 
Handling connection for 15672 
Handling connection for 15672 
Handling connection for 15672 
Handling connection for 15672 
Handling connection for 15672 
Handling connection for 15672 
```

This makes the RabbitMQ dashboard available at http://localhost:15672.

When logging in to the RabbitMQ UI:
  - Username: cluedin
  - Password: Retrieve the password from your stored CluedIn credentials.

**Checking queues**  
Upon logging in, the system typically directs the user to the Overview tab. This dashboard provides a high-level summary of RabbitMQ, including the total number of messages currently in the system and key metrics related to queue activity.

The queues can be sorted by total messages to quickly identify the largest queues within RabbitMQ.

![rabbitmq-queues.png]({{ "/assets/images/upgrade/rabbitmq-queues.png" | relative_url }})

Message rates can also be reviewed to determine whether queues are processing messages as expected:
  - Incoming – Indicates that messages are being published to the queue by a producer. These messages remain in the queue until they are consumed.
  - Deliver/Get – Indicates that messages from the queue are being consumed by a consumer.

![rabbitmq-rates.png]({{ "/assets/images/upgrade/rabbitmq-rates.png" | relative_url }})

If a large number of Incoming messages are observed but no corresponding Deliver/Get activity is recorded, it may indicate that no consumers are currently available to process those messages.

The number of consumers attached to a queue can be viewed by clicking the +/– icon on the right-hand side to enable the Consumers column.

![rabbitmq-consumers.png]({{ "/assets/images/upgrade/rabbitmq-consumers.png" | relative_url }})

In the example above, the queue RemoteEvents_cluedin-server-processing is connected to a single consumer, with messages being delivered at a rate of 224/s. This indicates that the queue is functioning as expected and is in a healthy state.