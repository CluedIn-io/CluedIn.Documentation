---
layout: cluedin
nav_order: 13
parent: How-to guides for PaaS
grand_parent: Installation
permalink: /deployment/infra-how-tos/aks-upgrade
title: AKS upgrade
tags: ["deployment", "ama", "marketplace", "azure", "aks", "kubernetes", "upgrade"]
last_modified: 2024-03-27
---
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

In this article, you will learn how to upgrade your Azure Kubernetes Service (AKS) to a supported version.
This is included as part of the AMA agreement with us, however, there may be times where CluedIn are unable to facilitate this upgrade for you due to missing levels of permission. This is more common when vnet integration is setup. 

**Important!** Before starting the AKS upgrade, make sure that you have followed all pre-requisites.

## Pre-requisites

### Tools used
- `az cli` and a shell

    This guide will primarily use `az cli` along with `PowerShell` to manage the AKS cluster. It is recommended to follow along, but not necessarily required.

### Azure checks
When doing a Kubernetes upgrade, nodes will `surge` to try minimise downtime of the application. This means that additional Nodes in the `Node Pool` will be spun up at upgrade time and may cause issues if preparation isn't done beforehand.

- Quota

    Each node will eventually spin up a new replica of the same SKU. It's important to make sure you have additional allocated quota so that these nodes can be spun up without any problems

- IP address allocation

    If your environment is using `Azure CNI without Dynamic Allocation` your nodes will reserve IP addresses for each potential pod. By default, this is between 30-50 pods per node. As a result, this will mean that each node will use the same amount of IP addresses and may mean when additional nodes are spun up during surge, there's not enough available space to allocate.

    Please see if there's enough space before going ahead.

If you do not meet the pre-requisites, please scroll down to the [here]() to follow the steps to get around this.

Reference material: https://learn.microsoft.com/en-us/azure/aks/upgrade-aks-cluster

## Upgrade Setup

Before proceeding, please check the pre-requisites as it will determine which upgrade path to take.

Before any Kubernetes upgrades take place, we **highly recommend** you scale down your instance to avoid any potential data loss. Whilst upgrading without scaling down is possible, it's best to be safe here.

1. Open up `pwsh` 
1. Run the following commands:

    ```powershell
    $aksParams = @(
        '--name', ${aksClusterName} # This is the name of the AKS cluster
        '--resource-group', ${resourceGroup} # This is the resource group name the AKS cluster resides in
        '--subscription', ${subscription} # This is the subscription the AKS cluster resides in
    )

    $command = 'kubectl scale statefulset -n cluedin --replicas=0 --all --timeout 5m'
    az aks command invoke @aksParams --command $command

    $command = 'kubectl scale deploy -n cluedin --replicas=0 --all --timeout 5m'
    az aks command invoke @aksParams --command $command
    ```

    The above may take a couple minutes to complete. But once done, it should be safe to upgrade the AKS cluster without any potential data loss.

1. Because CluedIn uses Kubernetes API, normally during upgrade time you may face an error when attempting to do the AKS upgrade. As a result, it will prevent you from upgrading without bypassing the API check first. 
To disable this API check, run the following command:

    ```powershell
    $params = @(
        '--name', ${aksClusterName}
        '--resource-group', ${resourceGroup}
        '--subscription', ${subscription}
        '--enable-force-upgrade'
        '--upgrade-override-until', ((Get-Date).AddDays(1).ToString('yyyy-MM-ddT00:00:00Z'))
    )
    az aks update @params
    ```

    This will take a few minutes to complete and should return back successfully

With the above steps completed, it's time to upgrade. Depending if you pass or fail the pre-requisites, please follow the appropriate path below.

[Passed](#i-have-passed-the-azure-checks-above)   
[Failed](#i-have-not-passed-the-azure-checks-above)

### I have passed the Azure Checks above

Because everything checks out from the Azure side, you should be able to upgrade the Kubernetes cluster without any issues. Please note that Kubernetes follows an upgrade path and it's not always possible to upgrade from a lower version to a much higher version. You may need to perform this operation a number of times.

1. Determine what version of Kubernetes you will need to get to, and then perform the below steps until you are successfully running that version.
1. Open up `pwsh`
1. Run the following commands:

    ```powershell
    $params = @(
        '--name', ${aksClusterName}
        '--resource-group', ${resourceGroup}
        '--subscription', ${subscription}
        '--kubernetes-version', '1.nn.n' # This will vary depending on what CluedIn version you are running.
        '--yes'
    )
    az aks upgrade @params
    ```
1. It will take between 5-15 minutes to complete each upgrade. Once you have completed the upgrade path to the necessary version, skip down to the bottom to scale up your environment again. [Post-upgrade](#post-upgrade)

If you are unsure about any of the steps above, please reach out to CluedIn support.

### I have **not** passed the Azure Checks above

When you do not have the correct setup to perform a smooth upgrade, additional steps are going to be required to get your environment upgraded to the desired supported version. If at any point in this section you are not comfortable with the steps. Please reach out to CluedIn support.

1. Make notes of the current node pools as these will be deleted

- Delete any node pools that cannot be surged
- Perform upgrade

### Post-upgrade

With the upgrade now successfully completed. It's time to bring the application back up into a running state and validate access.

1. Open up `pwsh`
1. Run the following commands:

    ```powershell
    $aksParams = @(
        '--name', ${aksClusterName}
        '--resource-group', ${resourceGroup}
        '--subscription', ${subscription}
    )

    $command = 'kubectl scale statefulset -n cluedin --replicas=1 --all --timeout 5m'
    az aks command invoke @aksParams --command $command

    $command = 'kubectl scale deploy -n cluedin --replicas=1 --all --timeout 5m'
    az aks command invoke @aksParams --command $command
    ```

1. The commands will complete before the application is technically ready. So please wait an additional 5-15 minutes after running the above and validating access to the environment.

With CluedIn now back up and running, please navigate to the frontend you would normally use and ensure you can login. If successful, you can now conclude that the AKS has been upgraded to the correct version.