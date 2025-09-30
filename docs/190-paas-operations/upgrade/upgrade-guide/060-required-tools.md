---
layout: cluedin
nav_order: 6
parent: CluedIn upgrade guide
grand_parent: Upgrade
permalink: /paas-operations/upgrade/guide/required-tools
title: Required tools for CluedIn upgrade
tags: ["deployment", "ama", "marketplace", "azure", "aks", "kubernetes", "upgrade"]
last_modified: 2025-09-22
headerIcon: "paas"

---
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

Before starting [CluedIn upgrade](/paas-operations/upgrade/guide), make sure you have the necessary tools installed and ready:

- [Kubernetes](#kubernetes)
- [Azure Kubernetes Service (AKS)](#azure-kubernetes-service)
- [kubectl](#kubectl)
- [Helm](#helm)
- (Optional) [Visual Studio Code](#visual-studio-code)
- (Optional) [Lens or Freelens](#lens-or-freelens)

In addition to the above, you also need a valid [kubeconfig file](#kubeconfig-file).

## Kubernetes

[Kubernetes](https://kubernetes.io/) is an open-source container orchestration platform. It automates the deployment, scaling, and management of containerized applications.

**Download link:** [Official website](https://kubernetes.io/releases/download/).

## Azure Kubernetes Service

[Azure Kubernetes Service (AKS)](https://azure.microsoft.com/en-us/products/kubernetes-service) is a managed [Kubernetes](#kubernetes) service provided by Microsoft Azure. It simplifies running Kubernetes by handling cluster management tasks such as upgrades, scaling, and security.

**Link to get AKS:** [Official website](https://azure.microsoft.com/en-us/pricing/purchase-options/azure-account).

## Kubeconfig file

The kubeconfig file is a configuration file used by [kubectl](#kubectl) and other [Kubernetes](#kubernetes) tools to connect to a cluster. It contains the information required for authentication and cluster access, including:

- Cluster details – The API server address and certificate data.

- User credentials – Authentication tokens, certificates, or keys.

- Contexts – Mappings that define which cluster, user, and namespace to use by default.

The kubeconfig is a plain-text YAML file that stores access details (credentials and cluster information):

- The file does not require a file extension.

- By default, the file is stored in the user’s home directory under the hidden .kube folder:

    ```
    ~/.kube/config
    ``` 

**To get the kubeconfig file**

1. Contact your Azure administrator and ask them to provide the kubeconfig file to you.

    Your administrator can find the kubeconfig file in Azure Portal.

    ![get-kube-config.png]({{ "/assets/images/paas-operations/upgrade/get-kube-config-2.png" | relative_url }})

1. Store the file in a secure location. 

    {:.important}
    Treat this file as sensitive information – it contains access credentials and cluster details.<br>**Do not commit** the file to a source control tool.

## kubectl

[kubectl](https://kubernetes.io/docs/reference/kubectl/) is command-line tool for interacting with [Kubernetes](#kubernetes) clusters. It lets you deploy applications, inspect and manage cluster resources, and view logs.

When it comes to CluedIn, kubectl lets you communicate directly with the Kubernetes API server defined in your [kubeconfig file](#kubeconfig-file). This means that you can: 

  - Inspect cluster resources (pods, services, deployments, and nodes). 

  - Apply configuration files (`kubectl apply -f deployment.yaml`). 

  - Scale applications up or down. 

  - Restart, delete, or debug the workloads. 

Without kubectl, there is no simple way to manage or query what’s running inside your [AKS](#azure-kubernetes-service) cluster.

**Required version:** 1.30 or higher.

**Installation instructions:** See [Kubernetes documentation](https://kubernetes.io/docs/tasks/tools/#kubectl).

## Helm

[Helm](https://helm.sh/) is a package manager for [Kubernetes](#kubernetes). It simplifies the deployment, upgrade, and management of applications by using reusable, versioned packages called charts.

When it comes to CluedIn, we use Helm for upgrades because it makes updating applications simple, consistent, and reversible. With a single command, you can apply changes while keeping version history for easy rollbacks.

**Required version:** 3.x.x.

**Installation instructions:** See [Helm documentation](https://helm.sh/docs/intro/install/).

## Visual Studio Code

[Visual Studio Code](https://code.visualstudio.com/) is lightweight, cross-platform code editor. The editor is useful for editing YAML files and reviewing configuration files during the upgrade.

This tool is optional to use.

**Download link:** [Official website](https://code.visualstudio.com/Download).

## Lens or Freelens

[Lens](https://k8slens.dev/) and [Freelens](https://freelensapp.github.io/) are powerful, free tools designed to monitor and manage [Kubernetes](#kubernetes) clusters. They provide a user-friendly graphical interface that simplifies multiple everyday Kubernetes tasks. By reducing the need to recall and execute long or complex command-line instructions, these tools improve productivity and save valuable time. 

Reasons to use Lens:

  - Ease of use – It offers an intuitive dashboard to view and manage cluster resources.

  - Productivity boost – It eliminates the need to memorize [kubectl](#kubectl) commands for common tasks. 

  - Built-in logs – The Freelens version includes built-in log viewing, which makes it especially useful for troubleshooting.

We recommend using Freelens, as it includes built-in log access and offers a more complete out-of-the-box experience. For teams that work regularly with Kubernetes, Lens can quickly become an indispensable daily tool for monitoring and troubleshooting clusters.

Once you [connect Lens (or Freelens) your CluedIn cluster](/paas-operations/upgrade/guide/prepare-for-the-upgrade#connect-lens-or-freelens-to-your-cluedin-cluster), it allows you to:
 
  - View and manage pods, services, deployments, and namespaces.
 
  - Monitor CPU, memory, and other resource usage. 

  - Access and search through logs directly from the UI. 

  - Inspect and edit Kubernetes objects without leaving the dashboard. 

Lens and Freelens are optional to use.

**Download links**:

- [Official Lens website](https://k8slens.dev/download)

- [Official Freelens website](https://freelensapp.github.io/) 
