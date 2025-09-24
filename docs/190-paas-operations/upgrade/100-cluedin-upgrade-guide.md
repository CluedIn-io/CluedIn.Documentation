---
layout: cluedin
permalink: /paas-operations/upgrade/guide
title: CluedIn upgrade guide
nav_order: 1
parent: Upgrade
grand_parent: PaaS operations
tags: ["deployment", "ama", "marketplace", "azure", "aks", "kubernetes", "upgrade"]
last_modified: 2025-09-22
headerIcon: "paas"
---
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

## Plan your upgrade

This guide provides instructions for upgrading CluedIn after the initial [installation](/deployment). Regular upgrades are recommended to ensure access to the latest features, improvements, and fixes.

For details about the updates available in a specific release, see [Release overview](/release-notes).

### Versioning scheme 

CluedIn release version numbers follow the format: 

**`{year}.{month}.{patch}`** 

For example, **`2025.05.02`**.

### Prerequisites 

Before starting an upgrade, ensure you have the following:

  1. Access to the live CluedIn application.

  1. Access to the kubeconfig file – this must be provided by your Azure administrator.

  1. A machine or a virtual machine (VM) with the following tools installed: 

      - Kubectl (version 1.30 or higher) 
      - Helm 3.x.x 
      - (Optional) Visual Studio Code
      - (Optional) Lens (or FreeLens)

### Preparation and communication 

Before performing an upgrade, complete the following steps to ensure a smooth process and minimize risks: 

  1. **Schedule downtime** – Plan the upgrade during a period when the application is not in use. The application will be unavailable throughout the upgrade process. 

  1. **Perform a full backup** – Back up all persistent disks and user values. This step is critical in case a rollback becomes necessary.

  1. **Allocate sufficient time** – Ensure you have enough time for the full upgrade and, if required, disaster recovery.

  1. **Inform the stakeholders** – Communicate at all stages of the upgrade:

      - Before the upgrade: Provide advance notice of the planned upgrade window, expected downtime, and potential business impact. 
      - During the upgrade: Provide updates if the upgrade takes longer than anticipated or if issues arise. 
      - After the upgrade: Confirm completion, communicate any changes affecting users, and explain how to report issues. 

### Review the upgrade documentation 

CluedIn publishes [upgrade documentation](/paas-operations/upgrade) with each new release. Be sure to review this documentation in full before beginning the upgrade process.

While many upgrades follow common steps, not all are identical, and some may include specialized procedures. 

Pay particular attention to any infrastructure-related changes, as these may require additional preparation or configuration. 

## Preparing your environment 
### Access to CluedIn application

Before starting an upgrade, it is best practice to open the CluedIn UI and confirm that all services are running as expected. If you don’t have direct access, make sure that someone who does is available to assist throughout the upgrade process.

#### Connect Helm and kubectl to the CluedIn AKS cluster

Helm and kubectl are command-line tools used to manage Kubernetes clusters. To connect them to the CluedIn Azure Kubernetes Service (AKS) cluster, you will need a valid kubeconfig file.

#### Obtain the kubeconfig

- The kubeconfig file must be securely provided by your Azure administrator.
  
- Treat this file as sensitive information – it contains access credentials and cluster details.
  
- Store it in a secure location and **never** commit it source control.

#### Set up your environment

Once you have the kubeconfig file, configure your environment to use it. For example, in PowerShell:

```powershell
$env:KUBECONFIG="path-to-file"
```

This ensures that both kubectl and Helm commands will use the correct cluster context. 

**Access modes:** 

  - **Public cluster** – A Kubernetes cluster with a public endpoint accessible from anywhere on the internet. 

    Considerations: 

    - This setup is less common due to security risks. 
    - Ensure your personal or organizational firewalls allow outbound access. 
    - Always use role-based access control (RBAC) and strong authentication. 

  - **Private cluster** – In a private AKS cluster, the API server is accessible only within the virtual network (VNet). 

    Requirements: 

    - Your Azure administrator must peer your VM or workstation to the cluster's VNet. 
    - Once peered, you can securely connect to the cluster without exposing it to the public internet. 

------------

### Cluster management with kubectl 

Kubectl lets you communicate directly with the Kubernetes API server defined in your **kubeconfig** file. This means that you can: 

  - Inspect cluster resources (pods, services, deployments, and nodes). 
  - Apply configuration files (`kubectl apply -f deployment.yaml`). 
  - Scale applications up or down. 
  - Restart, delete, or debug the workloads. 

Without kubectl, there is no simple way to manage or query what’s running inside your AKS cluster.

1. To verify that kubectl is installed correctly, run the following command in PowerShell: 
 
    ```powershell
    kubectl version --client 
    ```
    
    - If installed, you’ll see the client version details (for example, **Client Version: v1.30.0**). 

    - If not, you’ll get a "command not found" error. In this case, contact your system administrator to install and configure it properly. 

1. To confirm that kubectl is correctly connected to your cluster, run the following command in PowerShell: 

    ```powershell
   kubectl get pods --namespace cluedin 
   ```
 
    - You should see a list of pods. 

    - If not, your kubeconfig or network access may not be configured correctly. Contact your administrator.

------------

### Helm configuration 

We use Helm for upgrades because it makes updating applications simple, consistent, and reversible. With a single command, you can apply changes while keeping version history for easy rollbacks.

1. To verify that Helm is installed correctly, run the following command in PowerShell:
 
    ```powershell
    helm version 
    ```

    - If installed, you’ll see the client version details (e.g., **v3.x.x**).
 
    - If you get the "command not found" error, this means that Helm is not installed or is not in your PATH. In this case, contact your system administrator to install and configure it properly.

1. To verify that you are connected to the cluster, run the following command in PowerShell:

    ```powershell
    helm config current-context 
    ```

    - You should see the cluster name (for example, **aks-cluedin-eastus**).

    - If you get an error similar to "current-context is not set", contact your system administrator to ensure that the kubeconfig is configured correctly. 

#### Verify the CluedIn Helm repository

CluedIn publishes its latest Helm charts to a dedicated Helm repository. To check if it is configured, run the following command in PowerShell: 

```powershell
helm repo list 
```

  - If CluedIn appears in the list, you are ready to use it.

  - If not, add the repository by running the following command: 

    ```powershell
    Helm repo add https://cluedin-io.github.io/Charts 
    Helm repo list 
    ```
 
#### Update charts before an upgrade

Before performing any upgrade, always fetch the latest CluedIn charts: 

```powershell
Helm repo update 
```

This ensures that you are deploying the most up-to-date configurations and fixes. 

-----------

### Lens 

Lens and Open Lens are powerful, free tools designed to monitor and manage Kubernetes clusters. They provide a user-friendly graphical interface that simplifies multiple everyday Kubernetes tasks. By reducing the need to recall and execute long or complex command-line instructions, these tools improve productivity and save valuable time. 

Reasons to use Lens:

  - Ease of Use – It offers an intuitive dashboard to view and manage cluster resources. 
  - Productivity boost – It eliminates the need to memorize kubectl commands for common tasks. 
  - Built-in logs – The Freelens version includes built-in log viewing, which makes it especially useful for troubleshooting.

{:.important}
We recommend using FreeLens, as it includes built-in log access and offers a more complete out-of-the-box experience. For teams that work regularly with Kubernetes, Lens can quickly become an indispensable daily tool for monitoring and troubleshooting clusters.

#### Connect to your cluster

Lens connects to Kubernetes using your kubeconfig file. You can add clusters in two ways: 

- Drop-in method – Place your kubeconfig into the system’s `.kube` folder (commonly located at `~/.kube/config`). 
- UI method – Import or configure your cluster directly through the Lens graphical interface. 

Once connected, Lens allows you to:
 
  - View and manage pods, services, deployments, and namespaces. 
  - Monitor CPU, memory, and other resource usage. 
  - Access and search through logs directly from the UI. 
  - Inspect and edit Kubernetes objects without leaving the dashboard. 
 

## Perform the upgrade 

With the previous steps complete, you are now ready to begin the upgrade process. Keep in mind that upgrade steps may vary depending on the release. The following sequence outlines a typical upgrade process.

  1. Get current values 
  1. Set up new values 
  1. System pre-checks
  1. Run Helm (basic)
  1. Complete the upgrade 
  1. Validate the upgrade

-----------

### Get current Helm user values  

The Helm user values file is a YAML file that defines the configuration values to be apply when upgrading a Kubernetes cluster. The user value file will look similar to this: 

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

We recommend the following format for naming your user values files: `values-<environment>-<release-version>.yml`, where:

  - `<environment>` – The target environment (for example, dev, staging, or prod).

  - `<release-version>` – The release identifier, written as a hyphen-separated date or version number. 

For example, for release 2024.12.02 on the dev environment, the file should be named `values-dev-2024-12-02.yml`.

To get your Helm user values, run the following command in PowerShell (replace `<environment>` and `<release-version>` with your values): 
 
```powershell
helm get values cluedin-platform -n cluedin -o yaml > ./ values-<environment>-<release-version>.yml 
```

- YAML file will be created in your working directory. Open it in your preferred IDE (we typically use Visual Studio Code). 
- The file should resemble the provided example. If it appears empty, this usually means you are not connected to the cluster correctly. In that case, revisit the earlier steps to verify your connection. 

-----------

### Prepare new user values 

1. The required values for the target release are published in CluedIn documentation. Before proceeding, carefully verify that your current release is compatible with the target release. Once verified, duplicate the values file created in the previous step and rename it to match the target release. 

    For example, to go to release 2025.05.00 on the dev environment, the file should be named: 
 
    ```
    values-dev-2025-05-00.yml 
    ```

1. Carefully compare your existing values file with the new release’s required values. Update any outdated entries and add newly introduced values. In most cases, you will update container image tags and package versions, but additional configuration keys may also be required.

    {:.important}
    YAML is whitespace-sensitive—use spaces (not tabs) and ensure correct indentation, or the deployment will fail.

1. An IDE such as Visual Studio Code will highlight any formatting or indentation issues as you edit the YAML file. Once everything looks correct, save the file. 

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

### System pre-checks
Before starting an upgrade, ensure the following checks are completed:

  - Verify that the UI is running correctly.
  - Confirm that all pods are in a healthy (green) state.
  - Review the server logs and ensure they are free of errors.

If any issues are detected, it is recommended to resolve them before proceeding with the upgrade. In some cases, the upgrade itself may address certain problems, but if you're uncertain, it’s best to consult CluedIn support team for guidance.

**Check CluedIn workload**

Determine whether CluedIn is currently processing a high volume of data. If the system is under heavy load, it is best to allow all data to finish processing before performing the upgrade.

Although any data still in the queues should remain forward-compatible, reducing the workload helps minimize risk during the upgrade.

Check the internal CluedIn queues and confirm their status before proceeding.

### Helm upgrade (basic) 

During a Helm upgrade, the UI will be temporarily unavailable. Make sure to notify all users in advance so that they are aware of the downtime. 

A standard CluedIn upgrade typically results in 20–30 minutes of downtime. If the upgrade includes data migrations or additional updates, the outage may take longer. 

#### Verify the current CluedIn Helm chart version
 
Run the following command to list all Helm releases in the CluedIn namespace: 

```powershell
helm list -a -n cluedin 
```

The output will display the currently installed chart version. For example: 

```powershell
cluedin-platform-2.5.1 
```

This indicates that the current Helm chart version in use is **2.5.1**. 
 
#### Prepare the Helm command
The exact Helm command for your update will be provided in the target release documentation. In general, the command follows this structure:

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
  - `{CluedInChartVersion}` – The target chart version specified in the documentation. 
  - `${CustomValues}` – The full path to the user values file you created in the previous step. 
  - `runDatabaseJobsOnUpgrade=true` – Ensures that the database is refreshed during the upgrade. 
  - `runNugetFullRestore=true` – Ensures that all packages are fully restored. 
  - `--timeout 10m0s` – A best practice is to allow a 10-minute timeout. If the upgrade fails due to a timeout, follow the documented mitigation steps. 

#### Run the Helm command
When you are ready, run the Helm command in PowerShell. 

The PowerShell prompt will remain active for several minutes—this is expected. Please be patient while the process runs. 

During the upgrade, the Helm release status will progress through the following states: 

 - Active → Pending Upgrade → Upgrading 

Allow the process to complete without interruption. 

#### Helm command completed
After about **10 minutes**, the Helm command in PowerShell should complete and display a confirmation message. This indicates that the Helm command executed successfully. 

However, while the Helm upgrade itself will be finished, some pods may still be starting up. It can take an additional **10–15** minutes for all pods to become fully healthy (green). 

You can monitor progress by checking: 

  - CluedIn pods 

  - CluedIn server logs. When checking the server logs, look for the following message: 

    ```
    Application started
    ``` 

    This indicates a successful startup.

Finally, check the CluedIn UI and verify that everything is running smoothly.

## Common operations
This guide outlines common CluedIn activities you may need to carry out during installation, upgrades, or when troubleshooting performance issues. It is designed to provide practical steps and references that help you keep your CluedIn environment running smoothly.

### Verify CluedIn UI 

A successful load of the CluedIn UI is a strong indication that your installation is functioning correctly. 

To access the UI, use the URL that was configured during installation (obtain the URL from your administrator). This URL may be either: 

  - Public URL – Accessible from any network without restrictions. 
  - Private URL – Requires that you are connected to the correct internal or VPN network. Make sure you have the necessary access before attempting to open the UI. 

**Get access to CluedIn**

Users can be granted access to CluedIn in two main ways:

- **SSO (Single Sign-On)** – Access is provisioned by your administrator through your organization’s SSO provider. 
- **Invitation Email** – Your CluedIn administrator sends you an email invitation to join.

**UI verification steps**

1. Sign in to CluedIn. The home dashboard should appear almost instantly.

1. Click through the left-hand menu. All pages should appear almost instantly.

1. Perform a search in the top menu, click on any of the entities in the results, and then browse through the entity tabs. All tabs should respond quickly.

{:.important}
If any page takes longer than 5 seconds to load, it may indicate a performance issue or that the upgrade has not fully completed.

------------

### Check CluedIn pods 
Monitoring the state of pods is a routine task in Kubernetes, and it is especially critical during installation and upgrades. Verifying that pods are running and healthy ensures that the CluedIn platform is functioning correctly and that new deployments are stable. 

**Prerequisites**

- Before checking the pods, make sure you are already connected to the target Kubernetes cluster via a valid **kubeconfig** file. Without this connection, you will not be able to query the cluster. 

**Check pod states** 

To view the status of all CluedIn pods, run the following command: 

```powershell
kubectl get pods -n cluedin 
```

The command returns the list of all pods in the CluedIn namespace (`-n cluedin`) along with their current state (for example, **Running**, **Pending**, **CrashLoopBackOff**, **Completed**, **Succeeded**, or **Failed**). This provides quick visibility into whether services are healthy or require troubleshooting. Ideally, all pods should be in a **Running** or **Completed** state.

- **All pods in a Running or Completed state**. All pods in **Running** or **Completed** state indicate that your CluedIn installation is healthy and the infrastructure is actively running.

    If all pods are **Green/Running** but the application still has issues, check the pod logs. See the [Check CluedIn logs](#check-cluedin-logs) section for details.

- **Pods in the Pending state**. If some pods remain in the **Pending** state, allow a few minutes for them to transition to **Running**. If a pod is still pending after **5 minutes**, review the logs to identify the cause. 

- **Pods in the CrashLoopBackOff state**. When a pod is in the **CrashLoopBackOff** state, it means Kubernetes is repeatedly trying to start the pod, but the container inside it keeps failing and crashing. After each crash, Kubernetes waits a little longer before attempting to restart it again (the “backoff” part).

    Common causes:

    - Configuration errors – Such as incorrect environment variables, secrets, or config maps.

        {:.important}
        CluedIn config maps are complex. If changes have been made to the recommended configurations, revert them to the default settings.

    - Application errors – The application may crash on startup due to bugs, missing dependencies, or incompatible versions.  

    - Resource limits (most common) – The container may not have sufficient CPU or memory and is killed by the system.  

    - Permission or connectivity issues – For example, firewall changes or Azure policies may block the pod from starting.  

    To get more details about a pod that is not starting or is stuck in a crash loop, run the following command:

    ```powershell
    kubectl describe pod <pod-name> -n cluedin 
    ```

------------

### Check CluedIn logs
All CluedIn pods generate logs that provide detailed information about what the system is doing. These logs help you do the following: 

  - Confirm that services are running smoothly.  
  - Diagnose issues when problems occur.  
  - Gain visibility into the internal behavior of the system.  

Reviewing pod logs is an essential step in troubleshooting errors and verifying that your installation is functioning correctly.

To check the logs of pod, run the following command: 

```powershell
kubectl logs <pod name> -n cluedin 
```

Pod logs are especially useful for troubleshooting in the following scenarios:  

  - **CrashLoopBackOff** – A pod repeatedly fails to start.  
  - **Running but Not Ready** – Readiness probes fail even though the pod is running.  
  - **Running and Ready, but Application Misbehaving** – The pod looks healthy but the application itself is not functioning correctly.  
  - **Init Containers Delayed or Failing** – The initialization steps take too long or do not complete successfully.  

{:.important}
Logs stored in a Kubernetes pod are limited to the default 10 MB size. If logs grow beyond this limit, older entries will no longer be visible when using `kubectl` logs. If you have log analytics configured to collect pod logs, it is recommended to use that to read the pod logs. 

------

### Check CluedIn queues
This guide explains how to identify and troubleshoot issues with CluedIn queues, which are powered by a messaging system called RabbitMQ.

**What are RabbitMQ queues?**

RabbitMQ is a message broker – it allows different parts of CluedIn to communicate by passing messages between them:

  - Think of a queue as a waiting line for messages.
  - One service in CluedIn places messages onto the queue.
  - Another service takes messages off the queue and processes them.

This setup helps CluedIn handle large volumes of data reliably and asynchronously.

**Why are queues important?**

If queues stop working correctly, CluedIn may not be able to move data between services efficiently. Common symptoms include:

  - Queues growing indefinitely (messages are piling up but not being processed).
  - Queues stuck (no new messages are being consumed).

Services that depend on these messages may experience failures or degraded performance.

By checking the queues, you can quickly determine if CluedIn’s internal messaging system is healthy, or if a backlog or failure might be affecting the platform.

#### Access RabbitMQ
To get access to the RabbitMQ credentials, run the following command: 
 
```powershell
kubectl get secret cluedin-rabbitmq -n cluedin -o jsonpath="{.data.rabbitmq-password}" | base64 --decode 
```

RabbitMQ includes a built-in management UI. To access it, you first need to open a port forward to the RabbitMQ pod:

```powershell
#kubectl port-forward service/cluedin-rabbitmq 15672:15672 -n cluedin 
```
This will return an output similar to the following:

```powershell
Forwarding from 127.0.0.1:15672 -> 15672 
Handling connection for 15672 
Handling connection for 15672 
Handling connection for 15672 
Handling connection for 15672 
Handling connection for 15672 
Handling connection for 15672 
```

The RabbitMQ dashboard becomes available at **http://localhost:15672**.

When signing in to the RabbitMQ UI, use the following credentials:

  - Username – **cluedin**.
  - Password – Retrieve the password from your stored CluedIn credentials.

#### Check queues 
After the signin, the system typically directs the user to the **Overview** tab. This dashboard provides a high-level summary of RabbitMQ, including:

- The total number of messages currently in the system.

- Key metrics related to queue activity.

Queues can be sorted by total messages to quickly identify the largest queues within RabbitMQ.

![rabbitmq-queues.png]({{ "/assets/images/upgrade/rabbitmq-queues.png" | relative_url }})

You can also review message rates to determine whether queues are processing the messages as expected:

  - **Incoming** – Indicates that messages are being published to the queue by a producer. These messages remain in the queue until they are consumed.

  - **Deliver/Get** – Indicates that messages from the queue are being consumed by a consumer.

![rabbitmq-rates.png]({{ "/assets/images/upgrade/rabbitmq-rates.png" | relative_url }})

If you see a large number of **Incoming** messages but no corresponding **Deliver/Get** activity, it may indicate that no consumers are currently available to process those messages.

To check the number of consumers attached to a queue, click the **+/–** icon on the right-hand side to display the **Consumers** column.

![rabbitmq-consumers.png]({{ "/assets/images/upgrade/rabbitmq-consumers.png" | relative_url }})

In the example above, the queue **RemoteEvents_cluedin-server-processing** is connected to a single consumer, with messages delivered at a rate of 224/s. This indicates that the queue is healthy and functioning as expected.

------

### Scenario 1: CrashLoopBackOff state

A pod is in a **CrashLoopBackOff** state, the container keeps starting, failing, and restarting in a loop. 

In this case, when you run `kubectl get pods –n cluedin`, you will see similar output showing a high number of restarts and the **CrashLoopBackOff** status. 

```
NAME                              READY STATUS           RESTARTS AGE
----                              ----- ------           -------- ---
cluedin-ui-7d9f8d7c9d-abc12       0/1   CrashLoopBackOff 9        5m
```

To troubleshoot this, it is important to review the logs of the previous container instance, not the current one that is restarting. The previous logs usually contain the exact error message that caused the crash. These logs often appear near the last few lines of the output. 

To check previous logs from before a pod crashed, add the `–p` (stands for previous) flag at the end of the `kubectl logs` command. 
 
```powershell
kubectl logs <pod name> -n cluedin –p 
```

<!-- Give an example error -->
<!-- Give an example resolution -->

------

### Scenario 2: Pod not ready
A pod can be in the **Running** state but still marked as **Not Ready** if it is failing its readiness probes.

This situation occurs when Kubernetes has successfully started the pod, but the application inside is not yet prepared to handle traffic. In other words, the container is alive, but it cannot serve requests.

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

    If you find repeated **Readiness probe failed** events, this confirms that the pod is starting but failing to pass the readiness check.

1. Examine the container logs, which may provide additional details on why the application is not ready to serve traffic.

    For example, a pod might be running but remain **Not Ready** until it successfully connects to its database. In this case, the readiness probe will continue to fail until the dependency becomes available.
 
    For example, when you run the following command:
    ```powershell
    kubectl logs <pod-name> -n cluedin 
    ```
    It will return the following:
    ```powershell
    2025-09-19T10:25:12Z INFO Starting CluedIn ... 
    2025-09-19T10:25:15Z WARN Waiting for database connection... 
    2025-09-19T10:25:30Z ERROR Timeout connecting to SQL at db-service:4133 
    ```

**Resolution**

In this example, the issue must be resolved by fixing the connectivity between the pod and the database.

Common causes include:
  - A misconfigured connection string (for example, wrong host, port, username, or password).

  - The database may be under resource pressure (for example, CPU or memory exhaustion), which can prevent it from accepting new connections.

Addressing these problems will allow the pod to pass its readiness probe and become ready to serve traffic.

------

### Scenario 3: Pod running and ready, but application exhibits unexpected behaviour

In some cases, a pod may be in the **Running** state and marked as **Ready**, but the application inside still shows unexpected or faulty behaviour. This indicates that the pod has passed its liveness and readiness probes, but the underlying issue lies within the application itself.

1. To begin diagnosing the issue, run the following command:
 
    ```powershell
    kubectl get pods –n cluedin 
    ```

    The output will be similar to the following:

    ```powershell
    NAME                              READY STATUS   RESTARTS AGE
    ----                              ----- ------   -------- ---
    cluedin-ui-7d9f8d7c9d-abc12       1/1   Running  0        5m
   ``` 

    This usually means that the problem is not with Kubernetes itself, but with the application inside the pod, or with network access between the user and the pod. 
 
1. Even if a pod appears healthy, the application inside might be failing silently. To check for hidden errors, review the pod logs by running the following command: 

    ```powershell
    kubectl logs <pod name> -n cluedin 
    ```

    If you want to read the log in a more convenient way, you can download it to a file and open it with any file reader. 

    ```powershell 
    kubectl logs <pod name> -n cluedin  >  <podname>.log 
    ```

<!-- Give an example error -->
<!-- Give an example resolution -->

### Scenario 4: Pod running and ready, but application exhibits unexpected behaviour

A pod can contain one or more application containers, and may also include one or more init containers:

- Init containers run sequentially before the main application containers start. Each must complete successfully before any main container in the pod can begin running.

- If an init container fails or cannot complete, the main container responsible for serving traffic may remain stuck in the **Pending** state. This means that the pod never progresses to running the main workload.

To verify whether a pod is unable to start because of a failing init container, describe the pod with the following command:

```powershell
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

- The main container named `ui` is in a `Waiting` state. This usually means it is waiting for the init containers to complete successfully.

- The events show that the init container `wait-cluedin-gql` has failed. In such cases, the pod cannot progress to running the main container until the init container issue is resolved. Sometimes, an init container may run indefinitely without explicitly failing. In both scenarios, it is useful to inspect the init container logs for more details.

    To view the logs of a specific init container, addi the `-c <init-container-name>` flag to the `kubectl logs` command:

    ```powershell
    kubectl logs <pod-name> -n cluedin -c <init-container-name>
   ```

    This will help you understand why the init container is failing or stuck, and therefore why the main container cannot proceed.