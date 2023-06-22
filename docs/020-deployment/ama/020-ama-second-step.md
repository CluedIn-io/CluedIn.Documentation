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
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

In this article, you will learn about the pre-installation processes that you must perform to ensure successful installation of CluedIn.

![Pre-installation checklist](../../assets/images/ama/install-guide/overview-second-step.png)

# Check qualification

As a Microsoft Azure Administrator, you should have expertise in implementing, managing, and monitoring your organization’s Microsoft Azure environment.

Because CluedIn will be installed in your Azure resource group, you need to be the **Owner** of that resource group or at least the **Contributor** to that resource group.  

In addition, you should have **permission to purchase paid applications** from the Azure Marketplace. Set the permission to **Free + Paid** to complete the purchase registration in the Azure Marketplace.

![Check_qualification_Purchasing.png](../../assets/images/ama/install-guide/check-qualitifcation.png)

To learn how to allow purchases, see <a href="https://learn.microsoft.com/en-us/marketplace/azure-purchasing-invoicing">Azure Marketplace purchasing</a>.

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

You can check if you have enough quota by running a [verification script](#verification-script).

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

You can register the resource providers in two ways: [manually in the Azure portal](#manual-registration-of-resource-providers) and [automatically by running a script](#automatic-registration-of-resource-providers).

After you register the resource providers, run the [verification script](#verification-script) to make sure that all resource providers are registered.

## Manual registration of resource providers

This section contains the step-by-step procedure for manual registration of resource providers in the Azure portal.

**To register resource providers**

1. In the Azure portal, find and select the subscription where you need to install CluedIn.

    For more information about the subscription, see <a href="https://learn.microsoft.com/en-us/azure/azure-portal/get-subscription-tenant-id">Get subscription and tenant IDs in the Azure portal</a>.

1. On the left menu, under **Settings**, select **Resource providers**.

1. One by one, find and select the resource providers that you want to register, and then select **Register**.
![Manual_Registration_1](../../assets/images/ama/install-guide/register-resource-provider-1.png)
Wait until the status of the resource provider is changed from **Registering** to **Registered**.
![Manual_Registration_2](../../assets/images/ama/install-guide/register-resource-provider-2.png)
1. Run the [verification script](#verification-script) to make sure that all resource providers are registered.

For more information about registering resource providers, see <a href="https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/resource-providers-and-types">Azure documentation</a>.

## Automatic registration of resource providers
If you want a faster way to register the needed resource providers, run the script for automatic registration of resource providers.

**Prerequisites**

* PowerShell 7.

    We recommend installing PowerShell via Winget: `winget search Microsoft.PowerShell`. For more details, see <a href="https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-windows">Installing PowerShell on Windows</a>.

* Azure CLI.
    
    We recommend installing Azure CLI via Winget: `winget install -e --id Microsoft.AzureCLI`. For more details, see <a href="https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-windows?tabs=azure-cli">Install Azure CLI on Windows</a>.

* Your Azure subscription ID.
    
    For more details, see [Get your Azure subscription ID](/deployment/infra-how-tos/get-subscription-id).

**To run the script for registering resource providers**

1. Download this <a href="../../../assets/ps1/pre-checks.ps1" download>script</a>.
1. Open your PowerShell terminal and run the following:
```
.\pre-checks.ps1 <subscrioptionId> -Register
# e.g. .\pre-checks.ps1 abc68d12-8e99-4890-b3a0-ca25816b1c26 -Register
```
You will get an autput similar to the following.
![output-automatic_registration.png](../../assets/images/ama/install-guide/output-automatic-registration.png)

## Verification script
The verification script checks if you have enough quota and if all required resource providers are registered.

**Prerequisites**

* PowerShell 7.
    
    We recommend installing PowerShell via Winget: `winget search Microsoft.PowerShell`. For more details, see <a href="https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-windows">Installing PowerShell on Windows</a>.

* Azure CLI.
    
    We recommend installing Azure CLI via Winget: `winget install -e --id Microsoft.AzureCLI`. For more details, see <a href="https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-windows?tabs=azure-cli">Install Azure CLI on Windows</a>.

* Your Azure subscription ID.
    
    For more details, see [Get your Azure subscription ID](/deployment/infra-how-tos/get-subscription-id).

* Azure region that you will select during installation.

**To run the verification script**

1. Download this <a href="../../../assets/ps1/check.ps1" download>verification script</a>.
1. Open your PowerShell terminal and run the following:
```
.\check.ps1 -SubscriptionId <subscrioptionId> -Location <location>
# e.g. .\check.ps1 -SubscriptionId abc68d12-8e99-4890-b3a0-ca25816b1c26 -Location uksouth
```
As a result, you will get a file named <b>results_<i>location</i>.json</b> that will be stored in the same directory. The file will contain the details about the quota and the status of resource providers.

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
- **Default AKS functionality** – logs and pods should be able to see Kubernetes API Server (as recommended in <a href="https://learn.microsoft.com/en-us/azure/aks/outbound-rules-control-egress">Azure AKS documentation</a>).
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

CluedIn is very flexible in terms of network configuration. If you have any network-related questions, contact one of our infrastructure experts.

## Define VNet
During the installation process, CluedIn will install a newly created Azure VNet using an address space 10.0.0.0/8 and a subnet 10.0.0.0/16 for the Azure Kubernetes Service.

If you have an existing VNet and you want to reuse it for CluedIn installation, contact one of our infrastructure experts for assistance. You can specify the existing VNet in the <a href="/deployment/azure-marketplace/step-3#review-the-advanced-configuration-tab">Advanced configuration</a> step of CluedIn installation.

## Analyze CluedIn network configuration

CluedIn comes with a default network configuration. Changing network settings after installation is a very tedious task. Therefore, make sure that you have analyzed how you want to set up the CluedIn instance at the network level before starting the installation process.

The following diagram shows default CluedIn network configuration after installation.

![ama-network-1.jpeg](../../assets/images/ama/install-guide/ama-network-1.jpeg)

As part of the AKS managed cluster, AMA or AKS (public cluster) is deployed as a single standard Public Azure Load Balancer for both egress and ingress traffic.

## Configuration changes and support

If you need to change some network configurations, you can do that after you install CluedIn. For details about network customization, see <a href="/deployment/infra-how-tos/advanced-network"> Advanced network configuration</a>.

CluedIn provides support of Azure Load Balancer and Application Gateway. Other network configurations are not supported out of the box in any of our plans, so you might need the CluedIn infrastructure package hours.

# Results

1. You are qualified to perform the CluedIn installation process, and you have all the required permissions.
1. Your Azure subscription can sustain the required quota.
1. You have registered the required resource providers.
1. Your firewall is ready and configured to support the installation of CluedIn.
1. You are comfortable with the default network architecture.

# Next steps

Start the CluedIn installation process as described in our <a href="/deployment/azure-marketplace/step-3">Installation guide</a>.
