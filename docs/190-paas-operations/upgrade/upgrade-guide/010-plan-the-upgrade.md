---
layout: cluedin
nav_order: 1
parent: CluedIn upgrade guide
grand_parent: Upgrade
permalink: /paas-operations/upgrade/guide/plan-the-upgrade
title: Plan the upgrade
tags: ["deployment", "ama", "marketplace", "azure", "aks", "kubernetes", "upgrade"]
last_modified: 2025-09-22
headerIcon: "paas"

---
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

Careful planning ensures that the upgrade process is efficient, minimizes downtime, and accounts for dependencies across your environment. This page covers stage 1 of the [CluedIn upgrade process](/paas-operations/upgrade/guide). It outlines the decisions and preparations you should make before executing the upgrade.

## Get familiar with the versioning scheme 

CluedIn releases version numbers follow this format: **`{year}.{month}.{patch}`**. For example, **`2025.05.02`**.

## Prepare the prerequisites 

Before starting an upgrade, make sure you have the following in place: 

1. Access to live CluedIn application.

1. Access to the kubeconfig file – this must be provided by your Azure administrator.

1. A machine or a virtual machine (VM) with all the [required tools](#required-tools) installed.

### Required tools

Before starting the upgrade, make sure you have the necessary tools installed and ready:

- [kubectl](#kubectl)

- [Helm](#helm)

- (Optional) [Visual Studio Code](#visual-studio-code)

- (Optional) [Lens or FreeLens](#lens-or-freelens)

#### kubectl

[kubectl](https://kubernetes.io/docs/reference/kubectl/) is command-line tool for interacting with Kubernetes clusters. It lets you deploy applications, inspect and manage cluster resources, and view logs.

When it comes to CluedIn, kubectl lets you communicate directly with the Kubernetes API server defined in your kubeconfig file. This means that you can: 

  - Inspect cluster resources (pods, services, deployments, and nodes). 

  - Apply configuration files (`kubectl apply -f deployment.yaml`). 

  - Scale applications up or down. 

  - Restart, delete, or debug the workloads. 

Without kubectl, there is no simple way to manage or query what’s running inside your AKS cluster.

- Required version: 1.30 or higher.

- For installation instructions, see [Kubernetes documentation](https://kubernetes.io/docs/tasks/tools/#kubectl).

#### Helm

[Helm](https://helm.sh/docs/) is a package manager for Kubernetes. It simplifies the deployment, upgrade, and management of applications by using reusable, versioned packages called charts.

When it comes to CluedIn, we use Helm for upgrades because it makes updating applications simple, consistent, and reversible. With a single command, you can apply changes while keeping version history for easy rollbacks.

- Required version: 3.x.x.

- For installation instructions, see [Helm documentation](https://helm.sh/docs/intro/install/).

#### Visual Studio Code

[Visual Studio Code](https://code.visualstudio.com/) is lightweight, cross-platform code editor. The editor is useful for editing YAML files and reviewing configuration files during the upgrade.

- This tool is optional to use.

- You can download Visual Studio Code from the [official website](https://code.visualstudio.com/Download).

#### Lens or Freelens

[Lens](https://k8slens.dev/) and [Freelens](https://freelensapp.github.io/) are powerful, free tools designed to monitor and manage Kubernetes clusters. They provide a user-friendly graphical interface that simplifies multiple everyday Kubernetes tasks. By reducing the need to recall and execute long or complex command-line instructions, these tools improve productivity and save valuable time. 

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

Lens and Freelens are optional to use. You can download them from:

- [Official Lens website](https://k8slens.dev/download)

- [Official Freelens website](https://freelensapp.github.io/) 

## Perform pre-upgrade actions 

Before performing an upgrade, complete the following steps to ensure a smooth process and minimize risks:

1. **Schedule downtime** – Plan the upgrade during a period when the application is not in use. The application will be unavailable throughout the upgrade process. 

1. **Perform a full backup** – Back up all persistent disks and user values. This step is critical in case a rollback becomes necessary.

1. **Allocate sufficient time** – Ensure you have enough time for the full upgrade and, if required, disaster recovery.

1. **Inform the stakeholders** – Communicate at all stages of the upgrade:

    - Before the upgrade: Provide advance notice of the planned upgrade window, expected downtime, and potential business impact. 

    - During the upgrade: Provide updates if the upgrade takes longer than anticipated or if issues arise. 

    - After the upgrade: Confirm completion, communicate any changes affecting users, and explain how to report issues. 

## Review the upgrade documentation 

CluedIn publishes [upgrade documentation](/paas-operations/upgrade) with each new release. Be sure to review this documentation in full before beginning the upgrade process. While many upgrades follow common steps, not all are identical, and some may include specialized procedures. 

{:.important}
Pay particular attention to any infrastructure-related changes, as these may require additional preparation or configuration. 