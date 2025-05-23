---
layout: cluedin
nav_order: 1
parent: Upgrade
grand_parent: PaaS operations
permalink: /paas-operations/upgrade/aks
title: AKS upgrade
tags: ["deployment", "ama", "marketplace", "azure", "aks", "kubernetes", "upgrade"]
last_modified: 2024-03-27
headerIcon: "paas"
---
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

In this article, you will learn how to upgrade your Azure Kubernetes Service (AKS) to a supported version. This is included as part of the AMA agreement with us, and we'll normally facilitate these upgrades on your behalf. However, there may be times where we are unable to do this upgrade due to missing levels of permission or other factors. 

{:.important}
Before starting the AKS upgrade, make sure that you have read the prerequisites section.

## Prerequisites

### Tools
- `az cli` and a shell. This guide will primarily use `az cli` along with `PowerShell` to manage the AKS cluster. It is recommended to follow along, but not necessarily required.

### Azure checks
When doing a Kubernetes upgrade, nodes will `surge` to try minimise downtime of the application. This means that additional nodes in the `Node Pool` will be spun up at upgrade time and may cause issues if preparation isn't done beforehand.

- **Quota** – each node will eventually spin up a new replica of the same SKU. It's important to make sure you have additional allocated quota so that these nodes can be spun up without any problems.

- **IP address allocation** – if your environment is using `Azure CNI without Dynamic Allocation`, your nodes will reserve IP addresses for each potential pod. By default, this is between 30-50 pods per node. As a result, each node will use the same amount of IP addresses. This can mean that when additional nodes are spun up during surge, there's not enough available space to allocate.

    Please see if there's enough space before going ahead.

If you do not meet the prerequisites, please scroll down to the [here](#upgrade-with-azure-checks-not-passed) to follow the steps to get around this.

For reference information, see [Microsoft documentation](https://learn.microsoft.com/en-us/azure/aks/upgrade-aks-cluster).

## Upgrade setup

Before proceeding, please check the prerequisites as it will determine which upgrade path to take.

Before any Kubernetes upgrades take place, we **highly recommend** you scale down your instance to avoid any potential data loss. Whilst upgrading without scaling down is possible, it's best to be safe here.

**To scale down your instance**

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

1. Run the following commands to get the list of availble version to upgrade

    ```powershell
    $params = @(
      '--name', ${aksClusterName}
      '--resource-group', ${resourceGroup}
      '--subscription', ${subscription}
    )
    az aks get-upgrades @params -o table
    ```
Pick the version to upgrade from the output list

With the above steps completed, it's time to upgrade. Depending on if you pass or fail the prerequisites, please follow the appropriate path below:

- [Passed](#upgrade-with-azure-checks-passed)   
- [Failed](#upgrade-with-azure-checks-not-passed)

### Upgrade with Azure checks passed

Because everything checks out from the Azure side, you should be able to upgrade the Kubernetes cluster without any issues. Please note that Kubernetes follows an upgrade path and it's not always possible to upgrade from a lower version to a much higher version. You may need to perform this operation a number of times.

**To upgrade the cluster**
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
1. It will take between 5-15 minutes to complete each upgrade. Once you have completed the upgrade path to the necessary version, scale up your environment again following the steps [here](#post-upgrade).

If you are unsure about any of the steps above, please reach out to CluedIn support.

### Upgrade with Azure checks NOT passed

When you do not have the correct setup to perform a smooth upgrade, additional steps are going to be required to get your environment upgraded to the desired supported version. If at any point in this section you are not comfortable with the steps, please reach out to CluedIn support.

{:.important}
Make notes of the current node pools as these will be deleted as part of the process. This includes taints, labels, and any other potential configurations.

1. Open up `pwsh`
1. Run the following commands:

    ```powershell
    $aksClusterParams = @(
        '--name', ${aksClusterName}
        '--resource-group', ${resourceGroup}
        '--subscription', ${subscription}
    )
    $aksCluster = az aks show @aksClusterParams | ConvertFrom-Json

    $aksNodePools = $aksCluster.agentPoolProfiles
    ```

1. The above will return back an object that contains the agent pool configuration. This can be queried by running `$aksNodePools` in your shell and making notes of the configuration. It is unlikely you need to touch the `System` node pool, so chances are you only need to make notes of the `User` node pools which is what CluedIn runs on.

    Make notes of the following configuration for each node you need to delete:

    - name
    - nodeCount
    - nodeVmSize
    - maxPods
    - vnetSubnetId
    - labels
    - taints

    **Note**: As long as the `PowerShell` session doesn't get closed, this object will always exist to reference.

1. In `PowerShell`, run the following commands:

    ```powershell
    $params = @(
        '--nodepool-name', ${nodeName} # This is the name of the node pool you are attempting to delete
        '--cluster-name', ${aksClusterName}
        '--resource-group', ${resourceGroup}
        '--subscription', ${subscription}
    )
    az aks nodepool delete @params
    ```

    **Note**: You need to repeat this for all node pools that are affected by either the IP address allocation or quota (based on the VM SKU it is using).

1. Because all affected node pools have now been deleted, you should perform the upgrade steps next until your desired version. Follow the steps above [here](#upgrade-cluster) and return back here once you have hit your version.

1. With Kubernetes control plane now updated, it's time to recreate the node pools before scaling the application back up.

1. In `pwsh` run the following commands:

    ```powershell
    $params = @(
        '--cluster-name', ${aksClusterName}
        '--resource-group', ${resourceGroup}
        '--subscription', ${subscription}
        '--name', ${nodeName}
        '--mode', 'User'
        '--node-count', ${nodeCount}
        '--node-vm-size', ${nodeVmSku}
        '--max-pods', ${nodeMaxPods}
        '--vnet-subnet-id', ${nodeVnetSubnetId}
        # Optionals
        #   '--node-taints', ${nodeTaints} key=value format
        #   '--labels', ${nodeLabels} # key=value format
        #   '--enable-cluster-autoscaler'
    )
    az aks nodepool add @params
    ```

    **Note**: You need to repeat this for all node pools that were affected by either the IP address allocation or quota (based on the VM SKU it is using).

1. All nodepools should now be added back. You can validate in the Azure portal by navigating to the AKS cluster resource and selecting `Node Pools` on the left hand blade. If everything has the status `Succeeded` you can resume down below and scale the application back up.

## Post-upgrade

With the upgrade successfully completed, it's time to bring the application back up into a running state and validate access.

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

1. The commands will complete before the application is technically ready. Please wait another 5-15 minutes after running the above and validating access to the environment.

With CluedIn now back up and running, please navigate to the front end you would normally use and ensure you can sign in. If successful, you can now conclude that the AKS has been upgraded to the correct version.