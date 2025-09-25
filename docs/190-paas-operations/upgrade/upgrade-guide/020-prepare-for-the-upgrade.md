---
layout: cluedin
nav_order: 2
parent: CluedIn upgrade guide
grand_parent: Upgrade
permalink: /paas-operations/upgrade/guide/prepare-for-the-upgrade
title: Prepare for the upgrade
tags: ["deployment", "ama", "marketplace", "azure", "aks", "kubernetes", "upgrade"]
last_modified: 2025-09-22
headerIcon: "paas"

---
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

Before upgrading CluedIn, it’s important to make sure your environment is ready. Proper preparation helps reduce downtime, avoid data loss, and ensures a smooth transition to the new version. This page covers stage 2 of the [CluedIn upgrade process](/paas-operations/upgrade/guide). It walks you through the key steps to check and complete before starting the upgrade process.

## Get access to CluedIn application

Before starting an upgrade, it’s best practice to open the CluedIn UI and confirm that all services are running as expected. If you don’t have direct access, make sure someone who does is available and ready to assist throughout the upgrade process.

[Verifying CluedIn UI](/paas-operations/upgrade/guide/common-upgrade-operations#check-cluedin-ui)

## Connect Helm and kubectl to the CluedIn AKS cluster

Helm and kubectl are command-line tools used to manage Kubernetes clusters. To connect them to the CluedIn Azure Kubernetes Service (AKS) cluster, you will need a valid kubeconfig file.

### Obtaining the kubeconfig

- The kubeconfig file must be securely provided by your Azure administrator.  
- Treat this file as sensitive information—it contains access credentials and cluster details.  
- Store it in a secure location and **never** check it into source control.

### Setting up your environment

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

## Configure kubectl 

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

## Configure Helm

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

## Connect Lens to your CluedIn cluster

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