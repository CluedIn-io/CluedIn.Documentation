---
layout: cluedin
nav_order: 1
parent: Upgrade
grand_parent: PaaS operations
permalink: /paas-operations/upgrade/guide
title: CluedIn Upgrade Guide
tags: ["deployment", "ama", "marketplace", "azure", "aks", "kubernetes", "upgrade"]
last_modified: 2025-09-22
headerIcon: "paas"
---
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

## Planning Your Upgrade

This guide provides instructions for upgrading CluedIn after the initial installation. 
Regular upgrades are recommended to ensure you benefit from the latest features, improvements, and fixes. 

### Versioning Scheme 

CluedIn releases version numbers follow the format: 

**`{year}.{month}.{patch}`** 

Example: 
**`2025.05.02`** 

### Prerequisites 

Before starting an upgrade, make sure you have the following in place: 

  1. Access to the live CluedIn application 
  1. Access to the kubeconfig file this must be provided by your azure administrator 
  1. A machine or VM with the following tools installed: 

      - Kubectl 1.30 (min) 
      - Helm 3.x.x 
      - Visual Studio Code (optional) 
      - Lens (or FreeLens) (optional) 

### Preparation & Communication 

Before performing an upgrade, complete the following steps to ensure a smooth process and minimize risks: 

  1. Schedule Downtime 
    Plan the upgrade during a period when the application is not in use. The application will be unavailable throughout the upgrade process. 

  1. Perform a Full Backup 
    Back up all persistent disks and user values. This step is critical in case a rollback is required. 

  1. Allocate Sufficient Time 
    Allow enough time to run the full upgrade and to manage potential disaster recovery scenarios if needed. 

  1. Inform Stakeholders 
    Keep all relevant stakeholders informed before, during, and after the upgrade: 

      - Before the upgrade: Provide advance notice of the planned upgrade window, expected downtime, and potential business impact. 
      - During the upgrade: Share progress updates if the process takes longer than anticipated or if issues arise. 
      - After the upgrade: Confirm completion, communicate any changes that may affect users, and provide guidance on reporting unexpected issues. 

### Review Upgrade Documentation 

CluedIn publishes upgrade documentation with each new release. Please ensure you read the documentation in full before beginning the upgrade process. While many upgrades share common steps, not all are identical, and some may include specialized procedures. 

Pay particular attention to any infrastructure-related changes, as these may require additional preparation or configuration. 

## Preparing your Environment 
### Access to CluedIn Application

Before starting an upgrade, it’s best practice to open the CluedIn UI and confirm that all services are running as expected. If you don’t have direct access, make sure someone who does is available and ready to assist throughout the upgrade process.

[CluedIn UI – Link]

#### Connecting Helm and Kubectl to the CluedIn AKS Cluster

Helm and kubectl are command-line tools used to manage Kubernetes clusters. To connect them to the CluedIn Azure Kubernetes Service (AKS) cluster, you will need a valid kubeconfig file.

#### Obtaining the kubeconfig

- The kubeconfig file must be securely provided by your Azure administrator.  
- Treat this file as sensitive information—it contains access credentials and cluster details.  
- Store it in a secure location and **never** check it into source control.

#### Setting up your environment

Once you have the kubeconfig file, configure your environment to point to it. For example, in PowerShell:

```powershell
$env:KUBECONFIG="path-to-file"
```

This ensures that both kubectl and helm commands will use the correct cluster context. 

**Access Modes** 
**Public Cluster** 

  - Description: A Kubernetes cluster with a public endpoint can be accessed from anywhere on the internet. 
  - Considerations: 

    - This setup is less common due to security risks. 
    - Ensure your personal or organizational firewalls allow outbound access. 
    - Always use role-based access control (RBAC) and strong authentication. 

**Private Cluster** 

  - Description: In a private AKS cluster, the API server is only accessible within the virtual network (VNet). 
  - Requirements: 

    - Your Azure administrator must peer your virtual machine (VM) or workstation to the cluster's VNet. 
    - Once peered, you can securely connect to the cluster without exposing it to the public internet. 

------------

### Cluster Management with Kubectl 

Kubectl lets you communicate directly with the Kubernetes API server defined in your **kubeconfig** file. This means you can: 

  - Inspect cluster resources (pods, services, deployments, nodes). 
  - Apply configuration files (kubectl apply -f deployment.yaml). 
  - Scale applications up or down. 
  - Restart, delete, or debug workloads. 

Without kubectl, you wouldn’t have a straightforward way to manage or query what’s running inside your AKS cluster. 

To check kubectl is installed correctly, run the following command in PowerShell: 
 
```powershell
kubectl version --client 
```
  - If installed, you’ll see the client version details (e.g., Client Version: v1.30.0). 
  - If not, you’ll get a “command not found” error. In this case, contact your system administrator to install and configure it properly. 

To check that kubectl is correctly connected to your cluster run the following command in powershell: 

```powershell
kubectl get pods --namespace cluedin 
```
 
You should see a list of pods. 

If not then your kubeconfig is not configured correctly or network access is not configured correctly. [See admin] 

------------

### Helm Configuration 

We use Helm to upgrade because it makes updating applications simple, consistent, and reversible - allowing you to apply changes with one command while keeping version history for easy rollbacks. 

To check helm is installed correctly run the following command in PowerShell: 
 
```powershell
helm version 
```

  - You should see a client version (e.g., v3.x.x). 
  - If you see “command not found,” Helm isn’t installed or not in your PATH. In this case, contact your system administrator to install and configure it properly. 

Check you are connected to the cluster 

```powershell
helm config current-context 
```

  - You should see the cluster name (eg. aks-cluedin-eastus). 
  - If you see an error like “current-context is not set”. Contact your system administrator to ensure the kubeconfig is configured correctly. 

**Verifying the CluedIn Helm Repository** 

CluedIn publishes its latest Helm charts to a dedicated Helm repository. To check if it’s configured, run: 

```powershell
helm repo list 
```

  - If CluedIn appears in the list, you’re ready to use it. 
  - If not, add it with: 

```powershell
Helm repo add https://cluedin-io.github.io/Charts 
Helm repo list 
```
 
**Updating Charts Before an Upgrade** 

Before performing any upgrade, always fetch the latest CluedIn charts: 

```powershell
Helm repo update 
```

This ensures you’re deploying the most up-to-date configurations and fixes. 

-----------

### Lens 

**Lens** and **Open Lens** are powerful, free tools designed for monitoring and managing Kubernetes clusters. They provide a user-friendly graphical interface that simplifies many everyday Kubernetes tasks. By reducing the need to recall and execute long or complex command-line instructions, these tools can significantly improve productivity and save valuable time. 

**Why Use Lens?** 

  - Ease of Use: Offers an intuitive dashboard for viewing and managing cluster resources. 
  - Productivity Boost: Eliminates the need to memorize kubectl commands for common tasks. 
  - Logs Built In: The Free Lens version includes built-in log viewing, which makes it especially useful for troubleshooting. 

**Connecting to Your Cluster** 

Lens connects to Kubernetes using your kubeconfig file. You can add clusters in two main ways: 

  1. Drop-in method: Place your kubeconfig into the system’s .kube folder (commonly located at ~/.kube/config). 
  1. UI method: Import or configure your cluster directly through the Lens graphical interface. 

**Key Capabilities** 
Once connected, you can quickly and easily: 
  - View and manage pods, services, deployments, and namespaces. 
  - Monitor resource usage such as CPU and memory. 
  - Access and search through logs directly from the UI. 
  - Inspect and edit Kubernetes objects without leaving the dashboard. 

{:.important}
**Recommendation** 
We recommend using **Free Lens**, since it includes built-in log access and provides a more complete out-of-the-box experience. For teams working regularly with Kubernetes, Lens can become an indispensable daily tool for monitoring and troubleshooting clusters. 

## Performing the Upgrade 

With the previous steps completed, you are now ready to begin the upgrade process. Please note that upgrade steps may vary depending on the release. The follow steps are part of the typical process: 

  1. Get current values 
  1. Setup new values 
  1. System Pre-Checks
  1. Run the helm (Basic)
  1. Complete the upgrade 
  1. Validate the upgrade 

-----------

### Get Current Helm User Values  

The Helm user values file is a YAML file which defines the configuration values to be apply when upgrading a Kubernetes cluster. The user value file will look something like this: 

  ```yaml
    global: 
      image: 
        tag: "2024.12.02" 
      strategy: 
        type: Recreate 

    application: 
      cluedin: 
        image: 
          tag: "2024.12.02" 
        components: 
          packages: 
          - name: "CluedIn.Connector.AzureEventHub" 
            version: "4.0.1" 
          - name: "CluedIn.Connector.Dataverse" 
            version: "4.4.0" 
          - name: "CluedIn.Connector.Http" 
            version: "4.0.0" 
  ```

{:.important}
We recommend using the following format for naming your user values files: 
values-<environment>-<release-version>.yml 

  - <environment> = the target environment (e.g., dev, staging, prod). 
  - <release-version> = the release identifier, written as a hyphen-separated date or version number. 

Example: 
For release 2024.12.02 on the dev environment, the file should be named: 
 
```
values-dev-2024-12-02.yml 
```

To get your helm user values run the following command in powershell (substitute your environment and release number): 
 
```powershell
helm get values cluedin-platform -n cluedin -o yaml > ./ values-<environment>-<release-version>.yml 
```

  - The YAML file will be created in your working directory. Open it in your preferred IDE (we typically use Visual Studio Code). 
  - The file should resemble the provided example. If it appears empty, this usually means you are not connected to the cluster correctly. In that case, revisit the earlier steps to confirm your connection. 

-----------

### Prepare New User Values 

The required values for the target release are published in the CluedIn documentation. Before proceeding, carefully confirm that your current release is compatible with the target release. Once verified, duplicate the values file created in the previous step and rename it to match the target release. 

Example: 
To go to release 2025.05.00 on the dev environment, the file should be named: 
 
```
values-dev-2025-05-00.yml 
```

Carefully review your existing values file against the new release values. Replace any outdated entries with the updated ones, and add any values that are newly introduced. In most cases, you will be updating image tags and package versions, but additional configuration keys may also be required. Be especially mindful of YAML indentation, as incorrect spacing will cause errors during deployment. 

An IDE such as Visual Studio Code will highlight any formatting or indentation issues as you edit the YAML file. Once everything looks correct, save the file. 

Based on the earlier example, your YAML file should now look like this: 
 
  ```yaml
    global: 
      image: 
        tag: "2025.05.00" 
      strategy: 
        type: Recreate 
  
    application: 
      cluedin: 
        components: 
          packages: 
          - name: "CluedIn.Connector.AzureEventHub" 
            version: "4.5.0" 
          - name: "CluedIn.Connector.Dataverse" 
            version: "4.5.0" 
          - name: "CluedIn.Connector.Http" 
            version: "4.5.0" 
  ```

-----------

### System Pre-checks
Before starting an upgrade, ensure the following checks are completed:

  - Verify that the UI is running correctly.
  - Confirm that all pods are in a healthy (green) state.
  - Review the server logs and ensure they are free of errors.

If any issues are detected, it is recommended to resolve them before proceeding with the upgrade. In some cases, the upgrade itself may address certain problems, but when uncertain, seek advice from CluedIn Support.

**Check CluedIn Workload**
Determine whether CluedIn is currently processing a high volume of data. If the system is under heavy load, it is generally advisable to allow all data to finish processing before performing the upgrade.

Any data still in the queues should remain forward-compatible, but minimizing workload reduces risk during the upgrade process.

Check the internal CluedIn queues and confirm their status before proceeding.

### Helm Upgrade (Basic) 

During a Helm upgrade, the UI will be temporarily unavailable. Please notify all users in advance so they are aware of the downtime. 

A standard CluedIn upgrade typically results in 20–30 minutes of downtime. If the upgrade includes data migrations or additional updates, the outage may take longer. 

**Verify the Current CluedIn Helm Chart Version** 
Run the following command to list all Helm releases in the cluedin namespace: 

```powershell
helm list -a -n cluedin 
```

The output will display the currently installed chart version. For example: 

```powershell
cluedin-platform-2.5.1 
```

This indicates that the current Helm chart version in use is **2.5.1**. 
 
**Prepare the Helm Command** 
The exact Helm command for the current update will be provided in the target documentation. In general, the command follows this structure: 

```powershell
# ${CustomValues} refers to the values file you have amended with the above changes. Please type the full path here. 

helm upgrade cluedin-platform -n cluedin cluedin/cluedin-platform \ 
    --version {CluedInChartVersion} \ 
    --values ${CustomValues} \ 
    --set application.system.runDatabaseJobsOnUpgrade=true \ 
    --set application.system.runNugetFullRestore=true \ 
    --wait \ 
    --timeout 10m0s 
```

**Parameter details:** 
  - {CluedInChartVersion} – The target chart version specified in the documentation. 
  - ${CustomValues} – The full path to the user values file you created in the previous step. 
  - runDatabaseJobsOnUpgrade=true – Ensures the database is refreshed during the upgrade. 
  - runNugetFullRestore=true – Ensures all packages are fully restored. 
  - --timeout 10m0s – A best practice is to allow a 10-minute timeout. If the upgrade fails due to a timeout, please follow the documented mitigation steps. 

**Run the Helm Command** 
When you are ready, execute the Helm command in PowerShell. 

The PowerShell prompt will remain active for several minutes—this is expected. Please be patient while the process runs. 

During the upgrade, the Helm release status will progress through the following states: 

 - Active → Pending Upgrade → Upgrading 

Allow the process to complete without interruption. 

**Helm Command Completed**
After about **10 minutes**, the Helm command in PowerShell should complete and display a confirmation message. This indicates that the Helm command executed successfully. 

However, while the Helm upgrade itself will be finished, some pods may still be starting up. It can take an additional **10–15** minutes for all pods to become fully healthy (green). 

You can monitor progress by checking: 

  - CluedIn pods 
  - CluedIn server logs 

When checking the server logs, look for the following message: 

```
Application started
``` 

This indicates a successful startup, finally check the CluedIn UI and ensure everything is running smoothly.

## Common Operations
This guide outlines common CluedIn activities you may need to carry out during installation, upgrades, or when troubleshooting performance issues. It is designed to provide practical steps and references that help you keep your CluedIn environment running smoothly.

### Verifying CluedIn UI 

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

### Checking CluedIn Pods 
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

### Checking CluedIn Logs
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

### Checking CluedIn Queues
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

------

### Scenario 1: CrashLoopBackOff state 
A pod is in a CrashLoopBackOff state, the container keeps starting, failing, and restarting in a loop. 

The symptom for this is when you run kubectl get pods –n cluedin, you will see output like below, where high number of restarts and CrashLoopBackOff status. 

```powershell
kubectl get pods –n cluedin 
```
**returns**
```
NAME                              READY STATUS           RESTARTS AGE
----                              ----- ------           -------- ---
cluedin-ui-7d9f8d7c9d-abc12       0/1   CrashLoopBackOff 9        5m
```

To troubleshoot this, it’s important to check the logs of the previous container instance, not the current one that is restarting. 

The previous logs usually contain the exact error message that caused the container to crash. These logs often appear near the last few lines of output. 

To check previous logs before pods is crashed, simply add –p at the end of kubectl logs command, which stand for previous 
 
```powershell
kubectl logs <pod name> -n cluedin –p 
```

--Give an example error
--Give an example resolution

------

### Scenario 2: Pod Not Ready
A pod can be in the Running state but still marked as Not Ready if it is failing its readiness probes.

This situation occurs when Kubernetes has successfully started the pod, but the application inside is not yet prepared to handle traffic. In other words, the container is alive, but it cannot serve requests.

```powershell
kubectl get pods –n cluedin 
```
**Returns**
```powershell
NAME                              READY STATUS   RESTARTS AGE
----                              ----- ------   -------- ---
cluedin-ui-7d9f8d7c9d-abc12       0/1   Running  0        5m
```

To investigate whether a pod is failing due to a readiness probe, the first step is to describe the pod and review the events section at the bottom of the output.

You may see warnings similar to the following:

```powershell
Warning  Unhealthy  2m (x4 over 4m)  kubelet  Readiness probe failed: {{reason}}
```

If you find repeated Readiness probe failed events, this confirms that the pod is starting but failing to pass the readiness check. The next step is to examine the container logs, which may provide additional details on why the application is not ready to serve traffic.

For example, a pod might be running but remain Not Ready until it successfully connects to its database. In this case, the readiness probe will continue to fail until the dependency becomes available.
 
**Example**
```powershell
kubectl logs <pod-name> -n cluedin 
```
**Returns**
```powershell
2025-09-19T10:25:12Z INFO Starting CluedIn ... 
2025-09-19T10:25:15Z WARN Waiting for database connection... 
2025-09-19T10:25:30Z ERROR Timeout connecting to SQL at db-service:4133 
```

**Resolution**
In this example, the issue must be resolved by fixing the connectivity between the pod and the database.

Common causes include:
  - A misconfigured connection string (e.g., wrong host, port, username, or password).
  - The database being under resource pressure, such as CPU or memory exhaustion, preventing it from accepting new connections.

Addressing these problems will allow the pod to pass its readiness probe and become ready to serve traffic.

------

### Scenario 3: Pod Running and Ready, but Application Exhibits Unexpected Behaviour

In some cases, a pod may be in the Running state and marked as Ready, yet the application inside still shows unexpected or faulty behaviour. This indicates that the pod has passed its liveness and readiness probes, but the underlying issue lies within the application itself.

To begin diagnosing, run:
 
```powershell
kubectl get pods –n cluedin 
```
**Returns**
```powershell
NAME                              READY STATUS   RESTARTS AGE
----                              ----- ------   -------- ---
cluedin-ui-7d9f8d7c9d-abc12       1/1   Running  0        5m
``` 

This usually means the problem isn't with Kubernetes itself, but with the application inside the pod, or with network access between the user and the pod. 
 
Even if the pod looks healthy, the application inside might be failing silently. 
 To check for hidden errors, look at the pod logs with below command  

```powershell
kubectl logs <pod name> -n cluedin 
```

If you want to read the log in a more convenient way, it might be useful to download it to a file and open it with any file reader. 

```powershell 
kubectl logs <pod name> -n cluedin  >  <podname>.log 
```

--Give an example error
--Give an example resolution

### Scenario 3: Pod Running and Ready, but Application Exhibits Unexpected Behaviour

A pod can contain one or more application containers, and may also include one or more init containers.

Init containers run sequentially before the main application containers start. Each must complete successfully before any main container in the pod can begin running.

If an init container fails or cannot complete, the main container responsible for serving traffic may remain stuck in the Pending state. This means the pod never progresses to running the main workload.

To verify whether a pod is unable to start because of a failing init container, describe the pod with:

```powershell
kubectl describe pod <pod-name> -n cluedin
```
Returns
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

In the example above, the main container named ui is in a Waiting state. This usually means it is waiting for the init containers to complete successfully.

The events also show that the init container wait-cluedin-gql has failed. In such cases, the pod cannot progress to running the main container until the init container issue is resolved.

Sometimes, an init container may run indefinitely without explicitly failing. In both scenarios, it is useful to inspect the init container logs for more details.

You can view the logs of a specific init container by adding the -c <init-container-name> flag to the kubectl logs command:

```powershell
kubectl logs <pod-name> -n cluedin -c <init-container-name>
```

This will help you understand why the init container is failing or stuck, and therefore why the main container cannot proceed.