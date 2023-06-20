---
layout: default
nav_order: 1
parent: How tos
grand_parent: Deployment
permalink: /deployment/infra-how-tos/advanced-network
title: Advanced network configuration
tags: ["deployment", "ama", "marketplace", "azure"]
last_modified: 2023-06-20
---

In this article, you will learn about advanced network configuration options that are available to you during CluedIn installation.

# Default network configuration example

The following diagram shows default network configuration of CluedIn after installation.

![ama-network-1.jpeg](../../assets/images/ama/install-guide/ama-network-1.jpeg)

# Advanced network configuration example

The following diagram shows advanced network configuration of CluedIn.

![ama-network-2.jpeg](../../assets/images/ama/howtos/ama-network-2.jpeg)


Advanced network configuration (ingress vNet integration) allows you to specify the vNet and/or subnet address spaces that will be used to deploy your CluedIn platform. If you are deploying into your own network, see the following Microsoft guidelines for planning your Kubernetes networking model:

- [Plan IP addressing for your cluster](https://learn.microsoft.com/en-us/azure/aks/configure-azure-cni#plan-ip-addressing-for-your-cluster)
- [Configure Azure CNI networking in Azure Kubernetes Service (AKS)](https://learn.microsoft.com/en-us/azure/aks/configure-azure-cni)

The CluedIn platform requires the use of the **Azure CNI networking plug-in**. This plug-in is configured using routable vNet-based IP address at a per pod and node level. You need to plan the IP addressing for your cluster according to your current network topology. 

During the CluedIn installation, you will be asked for the **Kubernetes service address range**. Microsoft default values will work fine with CluedIn. However, these values can be customized, and it is important that your network is planned in accordance with the Microsoft guidance.

CluedIn can operate inside CIDR /23 with 510 available IP addresses. However, this is an absolute minimum configuration, and it does not consider any additional services and associated overhead.

## Advanced network configuration options

**Important!** If you do not plan to make any changes to the default out-of-the-box network configuration, you can skip this section and check other configuration-related topics:
- [Configure SSO](https://dev.azure.com/CluedIn-io/CluedIn/_wiki/wikis/CluedIn.wiki/1211/SSO)
- [Configure DNS](https://dev.azure.com/CluedIn-io/CluedIn/_wiki/wikis/CluedIn.wiki/1197/DNS)
- [Configure certificates](https://dev.azure.com/CluedIn-io/CluedIn/_wiki/wikis/CluedIn.wiki/1199/TLS-SSL)

<hr>

When installing CluedIn from the Azure Marketplace, you can set up advanced network configuration on the **CluedIn - Advanced Configuration** tab. You can choose from three networking options: 

- **Default** – a new vNet will be created using default values that may not allow you to integrate with the existing networks.

- **Modify IP ranges** – a new vNet will be created with IP address ranges that you specify. 

- **Use Existing vNet** – an existing vNet will be used and you need to specify both the vNet and the IP address ranges.
    
The following section focuses on the IP address configuration because it is universal to both the **Modify IP ranges** option and the **Use Existing vNet** option.

## IP address configuration

The following example is based on CluedIn essential configuration using the default node pool configuration with the existing Azure vNet.

![advanced-network-ama-tab.png](../../assets/images/ama/howtos/advanced-network-ama-tab.png)


When configuring vNet integration, only the following values need to be changed unless you have a very specific use case: 

- AKS subnet
- Kubernetes DNS service IP address 
- Kubernetes service address range
 
### AKS subnet

In the example above, the existing vNet was used to configure the AKS subnet. This is a non-overlapping subnet in the target network space, so it can communicate with other Azure vNets and Azure resources.

_10.240.0.0/23_  has a range of 10.240.0.0–10.240.1.255, totalling 512 IP addresses. The AKS subnet is used to allocate IP address to pods, nodes, and the load balancer IP.  

Under a normal operation, the cluster and CluedIn use around 350 addresses, leaving around 162 addresses for scaling, upgrading, and additional services.  

**Warning!** CluedIn can operate inside CIDR /23 with 510 available IP addresses. However, this is an absolute minimum configuration, and it may not provide sufficient headroom in the future or for some scaling scenarios. If CIDR /22 with 1022 IP addresses is available, you will have a little more headroom. 

### Kubernetes service address range

The Kubernetes service address range shouldn't be used by any network element on or connected to the ABA-DEV-IMPL-VNET-03 virtual network. The service address CIDR must be less than /12. You can reuse this range across different AKS clusters. In the example, we used 10.241.0.0/23, which is sufficient for the current services and any future growth.  

### Kubernetes DNS service IP address

The Kubernetes DNS service IP address is the IP address within the Kubernetes service address range that will be used by cluster service discovery. Don't use the first IP address in your address range. The first address in your address range is used for the kubernetes.default.svc.cluster.local address. In the example above, we have selected 10.241.0.10, which is inside the service CIDR range. 
 
# Azure Load Balancer

If you are using Azure Load Balancer as part of your CluedIn deployment, you need to consider the following security aspects:

- The cluster identity used by the AKS cluster must have at least **Network Contributor** permissions on the subnet within your virtual network.

- If you want to define a **custom role** instead of using the built-in Network Contributor role, the following permissions are required:
  - Microsoft.Network/virtualNetworks/subnets/join/action
  - Microsoft.Network/virtualNetworks/subnets/read
  - Microsoft.Authorization/roleAssignments/write

For details on creating custom roles, see [Azure custom roles](https://learn.microsoft.com/en-us/azure/role-based-access-control/custom-roles).

# Internal load balancer

This section contains a procedure for configuring CluedIn to use your internal load balancer and IP address.

**Prerequisites**

- You should be comfortable working in either PowerShell or bash terminal via Azure Cloud Shell.
- You should be connected to your AKS cluster.
See [Connect to CluedIn cluster](https://dev.azure.com/CluedIn-io/CluedIn/_wiki/wikis/CluedIn.wiki/1226/Connect-to-CluedIn-cluster) for detailed instructions.
- Your Helm repository is set up.
See [Helm](https://dev.azure.com/CluedIn-io/CluedIn/_wiki/wikis/CluedIn.wiki/1220/Helm) for detailed instructions on how to set up the repository.

If you have any questions, you can request CluedIn support by sending an email to support@cluedin.com (or reach out to your delivery manager if you have a committed deal).

<hr>

**To configure CluedIn to use your load balancer and internal IP address**

1. Download the current cluster configuration file by running the following command:
`helm get values cluedin-platform -n cluedin -o yaml > Cluster-Current-values.yaml`

2. Open the file in nano editor by running the following command:
`nano Cluster-Current-values.yaml`

3. In the file, find a section that looks like the example below.
```
  haproxy-ingress:
    controller:
      service:
        annotations:
          service.beta.kubernetes.io/azure-load-balancer-resource-group: mrg-azurecluedin
        loadBalancerIP: 20.0.189.xxx
```

This section controls the load balancer configuration and associated IP address. The example shows external load balancer with external IP address.

4. Replace the section that you found with the following section.

```  
haproxy-ingress:
    controller:
      service:
        annotations:
          service.beta.kubernetes.io/azure-load-balancer-internal: "true"
        loadBalancerIP: XXX.XXX.XXX.XXX
```

4. Reconfigure a new load balancer to use your internal IP address. To do this, replace `xxx.xxx.xxx.xxx` with the IP address from your AKS subnet range.
The IP address can be any IP from the range that is not in use by the nodes, pods, or other resources. To verify that the IP address is not in use, look at connected devices in the vNet resource page in the Azure portal.

5. Save the file.

6. Post the new configuration to the cluster by running the following command:

```
helm upgrade -i cluedin-platform cluedin/cluedin-platform  -n cluedin --create-namespace  --values Cluster-Current-values.yaml --set application.system.runDatabaseJobsOnUpgrade=false
```
After a short time, a confirmation appears in the console. It means that CluedIn is now configured to use your new load balancer and internal IP address.
 