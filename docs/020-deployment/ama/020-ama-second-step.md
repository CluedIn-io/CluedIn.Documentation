---
layout: default
nav_order: 2
parent: Azure Marketplace
grand_parent: Deployment
permalink: /deployment/azure-marketplace/step-2
title: 2. Pre-installation checklist
tags: ["deployment", "ama", "marketplace", "azure"]
last_modified: 2023-06-20
---

In this article, you will learn about the pre-installation processes that you must perform to ensure successful installation of CluedIn.

![Pre-installation checklist](../../assets/images/ama/install-guide/020-ama-second-step =900x)

# Check qualification

As a Microsoft Azure Administrator, you should have expertise in implementing, managing, and monitoring your organization’s Microsoft Azure environment.

Because CluedIn will be installed in your Azure resource group, you need to be the **Owner** of that resource group or at least the **Contributor** to that resource group.  

In addition, you should have **permission to purchase paid applications** from the Azure Marketplace. Set the permission to **Free + Paid** to complete the purchase registration in the Azure Marketplace.

![Check_qualification_Purchasing.png](../../assets/images/ama/install-guide/check-qualitifcation.png =650x)

To learn how to allow purchases, see [Azure Marketplace purchasing](https://learn.microsoft.com/en-us/marketplace/azure-purchasing-invoicing).


# Check quota

You should perform a quota check to make sure that your subscription has enough quotas for creating VMs required for CluedIn clusters.

There are 3 common VM family types that CluedIn will create as part of the AKS node pools. Your subscription must have **enough spare vCPU quota** to provision different nodes. For details on the quota for each VM, see the table below.

| VM | Quota |
|--|--|
| System Pool (1 x Standard_DS2_v2) | At least 2 vCPUs in the Standard DSv2 Family vCPUs quota |
| General Pool (2 x Standard_D8s_v4) and Data Pool (3 x Standard_D8s_v4) | At least 40 vCPUs in the Standard DSv4 Family vCPUs quota |

In addition, check if you have **enough quota for your plan**.

| Plan | Quota |
|--|--|
| Essential | At least 8 vCPUs in the StandardFSv2Family quota |
| Professional | At least 16 vCPUs in the StandardFSv2Family quota |
| Elite | At least 32 vCPUs in the StandardFSv2Family quota |

You can check if you have enough quota by running a [verification script](https://dev.azure.com/CluedIn-io/CluedIn/_wiki/wikis/CluedIn.wiki/1184/Step-2-Pre-installation-checklist?anchor=verification-script).

**Important!** If the quota is not available, then the installation will fail.

# Register resource providers

Before using a resource provider, register your Azure subscription for that specific resource provider.

Make sure that the following **resource providers are registered**:

- Microsoft.Cache
- Microsoft.Capacity
- Microsoft.Compute
- Microsoft.ContainerService
- Microsoft.EventHub
- Microsoft.KeyVault
- Microsoft.ManagedIdentity
- Microsoft.Network
- Microsoft.OperationalInsights
- Microsoft.OperationsManagement
- Microsoft.Resources
- Microsoft.Storage
- Microsoft.Sql

You can register the resource providers in two ways: [manually in the Azure portal](https://dev.azure.com/CluedIn-io/CluedIn/_wiki/wikis/CluedIn.wiki/1184/Step-2-Precheck?anchor=manual-registration-of-resources) or [automatically by running a script in Azure CLI](https://dev.azure.com/CluedIn-io/CluedIn/_wiki/wikis/CluedIn.wiki/1184/Step-2-Precheck?anchor=automatic-registration-of-resources).

After you register the resource providers, run the [verification script](https://dev.azure.com/CluedIn-io/CluedIn/_wiki/wikis/CluedIn.wiki/1184/Step-2-Precheck?anchor=verification-script) to make sure that all resource providers are registered.

## Manual registration of resource providers

This section contains the step-by-step procedure for manual registration of resource providers in the Azure portal.

**To register resource providers**

1. In the Azure portal, find and select the subscription where you need to install CluedIn.
For more information about the subscription, see [Get subscription and tenant IDs in the Azure portal](https://learn.microsoft.com/en-us/azure/azure-portal/get-subscription-tenant-id).

1. On the left menu, under **Settings**, select **Resource providers**.

1. One by one, find and select the resource providers that you want to register, and then select **Register**.
![Manual_Registration_1](../../assets/images/ama/install-guide/register-resource-provider-1.png =650x)
Wait until the status of the resource provider is changed from **Registering** to **Registered**.
![Manual_Registration_2](../../assets/images/ama/install-guide/register-resource-provider-2.png =650x)
1. Run the [script](https://dev.azure.com/CluedIn-io/CluedIn/_wiki/wikis/CluedIn.wiki/1184/Step-2-Precheck?anchor=verification-script) to verify that all resource providers are registered.

For more information about registering resource providers, see [Azure documentation](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/resource-providers-and-types).

**Note:** There is no additional charge for registering resource providers.

## Automatic registration of resource providers - Add script that Admin user can download and run

If you want a faster way to register the needed resource providers, execute the script in Azure CLI. Before that, make sure that you have installed [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli).

1. Open the command prompt and run the `az login` command.
1. Paste the script that would automatically register all the needed resources. _(Add the script)_
1. Run another [script](https://dev.azure.com/CluedIn-io/CluedIn/_wiki/wikis/CluedIn.wiki/1184/Step-2-Precheck?anchor=verification-script) to verify that all resources are registered.

## Verification script
The verification script checks if you have enough quota and if all required resource providers are registered.

**Prerequisites**

1. PowerShell 7.
We recommend installing PowerShell via Winget: `winget search Microsoft.PowerShell`. For more details, see [Installing PowerShell on Windows](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-windows).
1. Azure CLI.
We recommend installing Azure CLI via Winget: `winget install -e --id Microsoft.AzureCLI`. For more details, see [Install Azure CLI on Windows](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-windows?tabs=azure-cli).
1. Your Azure subscription ID.
For more details, see [Get your Azure subscription ID](https://dev.azure.com/CluedIn-io/CluedIn/_wiki/wikis/CluedIn.wiki/1193/Get-your-Azure-subscription-ID).
1. Azure region that you will select during installation.

<hr>

**To run the verification script**

1. Download the [check.ps1]() verification script and save it to a folder of your choice on your computer.
1. Open your PowerShell terminal and run the following:

```powershell
.\check.ps1 -SubscriptionId <subscrioptionId> -Location <location>
# e.g. .\check.ps1 -SubscriptionId abc68d12-8e99-4890-b3a0-ca25816b1c26 -Location uksouth
```
As a result, you will get a file named **results_<location>.json** that will be stored in the same directory. The file will contain the details about the quota and the status of resource providers.

**Example output of quota check**
  
```
"Location": "westeurope",
  "Quotas": [
    {
      "Name": "Standard Dv4 Family vCPUs",
      "Plan": "All",
      "Required": 40,
      "Available": 50,
      "IncreaseRequired": false
    }
```

**Example output of resource providers check**

```
"Providers": [
    {
      "Name": "Microsoft.Authorization",
      "Registered": "Registered"
    },
    {
      "Name": "Microsoft.Cache",
      "Registered": "Registered"
    }
```

# Configure firewall settings

Your Azure Firewall should cover the following:
- **Default AKS functionality** – logs and pods should be able to see Kubernetes API Server (as recommended in [Azure AKS documentation](https://learn.microsoft.com/en-us/azure/aks/outbound-rules-control-egress)).
- **CluedIn resource access** – resources needed for the CluedIn installation.

Add the following rules to your Azure Firewall as described in the table.

| Rule address | Port | Description |
|--|--|--|
| `cluedinprod.azurecr.io` | 443 | CluedIn container registry |
| `api.nuget.org` | 443 | NuGet packages |
| `github.com` | 433 | GitHub artifacts |
| `billing.cluedin.com` | 443 | CluedIn licensing server |
| `*.grafana.com` | 443 | Grafana chart content |
| `mcr.microsoft.com` | 443 | Microsoft container registry |

**Important!** If the rules have not been added, then the installation will fail.


# Configure network settings

```
DO NOT INCLUDE IN DOC - those are things we need to work on a dedicated network guide

NOTE?: so the AMA deploys two parts a standard AKS managed cluster just  like if you went to the Azure portal and deployed  a 'vanilla' AKS no secret sauce or additional config
NOTE2?: second part is the HELM deployment that deploys the cluedin application on top of that standard AKS deployment.
NOTE 3?: the base for the AMA is a AKS public Cluster where the AKS API is managed by MS and accessed via a  public endpoint
```
CluedIn is very flexible in terms of network configuration. If you have any network-related questions, contact one of our infrastructure experts.

## Define VNet
During the installation process, CluedIn will install a newly created Azure VNet using an address space 10.0.0.0/8 and a subnet 10.0.0.0/16 for the Azure Kubernetes Service.

If you have an existing VNet and you want to reuse it for CluedIn installation, contact one of our infrastructure experts for assistance. You can specify the existing VNet in the [Advanced configuration](https://dev.azure.com/CluedIn-io/CluedIn/_wiki/wikis/CluedIn.wiki/1188/Step-3-Installation-guide?anchor=review-the-advanced-configuration-tab) step of CluedIn installation.

## Analyze CluedIn network configuration

CluedIn comes with a default network configuration. Changing network settings after installation is a very tedious task. Therefore, make sure that you have analyzed how you want to set up the CluedIn instance at the network level before starting the installation process.

The following diagram shows default CluedIn network configuration after installation.

![ama-network-1.jpeg](../../assets/images/ama/install-guide/ama-network-1.jpeg)

As part of the AKS managed cluster, AMA or AKS (public cluster) is deployed as a single standard Public Azure Load Balancer for both egress and ingress traffic.

## Configuration changes and support

If you need to change some network configurations, you can do that after you install CluedIn. For details about network customization, see [Advanced network configuration](https://dev.azure.com/CluedIn-io/CluedIn/_wiki/wikis/CluedIn.wiki/1210/Y-Advanced-network-configuration).

CluedIn provides support of Azure Load Balancer and Application Gateway. Other network configurations are not supported out of the box in any of our plans, so you might need the CluedIn infrastructure package hours.

# Results

1. You are qualified to perform the CluedIn installation process, and you have all the required permissions.
1. Your Azure subscription can sustain the required quota.
1. You have registered the required resource providers.
1. Your firewall is ready and configured to support the installation of CluedIn.
1. You are comfortable with the default network architecture.

# Next steps

Start the CluedIn installation process as described in our [Installation guide](https://dev.azure.com/CluedIn-io/CluedIn/_wiki/wikis/CluedIn.wiki/1188/Step-3-Install-on-AMA).