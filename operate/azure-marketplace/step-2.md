---
title: Pre-installation checklist
url: https://documentation.cluedin.net/operate/azure-marketplace/step-2
content_type: reference
section: Deploy & operate > Azure Marketplace
---

# Pre-installation checklist

> reference: Facts, options, APIs.

In this article, you will learn about the pre-installation processes that you must perform to ensure successful installation of CluedIn PaaS.

![Ready to install CluedIn PaaS checklist: 1 check qualification, 2 check quota, 3 register resource providers, 4 configure firewall settings, 5 analyze network configuration, 6 analyze policies and tagging](https://documentation.cluedin.net/assets/images/deployment/paas-pre-installation-checklist.gif)

## Check qualification

As a Microsoft Azure Administrator, you should have expertise in implementing, managing, and monitoring your organization’s Microsoft Azure environment.

Because CluedIn will be installed in your Azure resource group, you need to be the **Owner** of that resource group or at least the **Contributor** to that resource group.  

In addition, you should have **permission to purchase paid applications** from the Azure Marketplace. Set the permission to **Free + Paid** to complete the purchase registration in the Azure Marketplace.

![The Azure Marketplace purchases setting in Azure with Free + Paid selected](https://documentation.cluedin.net/assets/images/ama/install-guide/check-qualitifcation.png)

### Navigate to Billing Policies in Azure Portal
To access Policies for a specific billing tenant in the Azure Portal:

  1. Open the Azure Portal.
  1. In the left-hand navigation menu, go to Cost Management.
  1. Click on Billing Profiles.
  1. Select the appropriate Tenant from the list.
  1. In the sidebar, choose Settings.
  1. Under Settings, click on Policies.

> **Note:** Ensure you have the appropriate permissions to view or modify billing policies.
> If you don’t see these options, verify your directory and tenant context in the portal.

To learn how to allow purchases, see [Azure Marketplace purchasing](https://learn.microsoft.com/en-us/marketplace/azure-purchasing-invoicing).

## Check quota

You should perform a quota check to make sure that your subscription has enough quotas for creating VMs required for CluedIn clusters. Each cluster will contain multiple nodes which are made up of virtual machines (VM).

There are 3 common VM family types that CluedIn will create as part of the AKS node pools. Your subscription must have **enough spare vCPU quota** to provision different nodes. For details on the quota for each VM, see the table below.

| VM | Quota |
|--|--|
| System Pool (1 x Standard_DS2_v5) | At least 2 vCPUs in the Standard DSv5 Family vCPUs quota |
| General Pool (2 x Standard_D8s_v4)  | At least 16 vCPUs in the Standard DSv4 Family vCPUs quota |
| Data Pool (3 x Standard D8as_v5)  | At least 24 vCPUs in the Standard DASv5 Family vCPUs quota |

In addition, check if you have **enough quota for your plan**.

| Plan | Quota |
|--|--|
| Essential & PAYG | At least 8 vCPUs in the StandardDASv5Family quota |
| Professional | At least 16 vCPUs in the StandardDASv5Family quota |
| Elite | At least 32 vCPUs in the StandardDASv5Family quota |

And finally, ensure that the region you're deploying to also has enough quota.
This is called 'Total Regional vCPUs' in Azure and must be equal to or greater than the sum of all vCPUs being deployed.

You can check if you have enough quota by running a [verification script](#verification-script).

> **Important:** If the quota is not available, then the installation will fail.

## Register resource providers

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

### Manual registration of resource providers

This section contains the step-by-step procedure for manual registration of resource providers in the Azure portal.

**To register resource providers**

1. In the Azure portal, find and select the subscription where you need to install CluedIn.

    For more information about the subscription, see [Get subscription and tenant IDs in the Azure portal](https://learn.microsoft.com/en-us/azure/azure-portal/get-subscription-tenant-id).

1. On the left menu, under **Settings**, select **Resource providers**.

1. One by one, find and select the resource providers that you want to register, and then select **Register**.

    ![The Resource providers page of an Azure subscription, filtered to Microsoft.Capacity with status NotRegistered and the Register button highlighted](https://documentation.cluedin.net/assets/images/ama/install-guide/register-resource-provider-1.png)

    Wait until the status of the resource provider is changed from **Registering** to **Registered**.

    ![The Resource providers page showing Microsoft.Capacity with the status registered](https://documentation.cluedin.net/assets/images/ama/install-guide/register-resource-provider-2.png)

1. Run the [verification script](#verification-script) to make sure that all resource providers are registered.

For more information about registering resource providers, see [Azure documentation](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/resource-providers-and-types).

### Automatic registration of resource providers

If you want a faster way to register the needed resource providers, run the script for automatic registration of resource providers.

**Prerequisites**

* PowerShell 7. We recommend installing PowerShell via Winget: `winget search Microsoft.PowerShell`. For more details, see [Installing PowerShell on Windows](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-windows).

* Azure CLI. We recommend installing Azure CLI via Winget: `winget install -e --id Microsoft.AzureCLI`. For more details, see [Install Azure CLI on Windows](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-windows?tabs=azure-cli).

* Your Azure subscription ID. For more details, see [Find your Azure subscription](https://learn.microsoft.com/en-us/azure/azure-portal/get-subscription-tenant-id#find-your-azure-subscription).

**To run the script for registering resource providers**

1. Download this [script](https://documentation.cluedin.net/assets/ps1/pre-checks.ps1).

1. Open your PowerShell terminal and run the following:
```
.\pre-checks.ps1 <subscrioptionId> -Register
# e.g. .\pre-checks.ps1 abc68d12-8e99-4890-b3a0-ca25816b1c26 -Register
```

    You will get an autput similar to the following.

    ![Output of pre-checks.ps1 with -Register: All required providers registered, followed by a table of providers each marked Registered and Required True](https://documentation.cluedin.net/assets/images/ama/install-guide/output-automatic-registration.png)

### Verification script

The verification script checks if you have enough quota and if all required resource providers are registered.

**Prerequisites**

* PowerShell 7. We recommend installing PowerShell via Winget: `winget search Microsoft.PowerShell`. For more details, see [Installing PowerShell on Windows](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-windows).

* Azure CLI. We recommend installing Azure CLI via Winget: `winget install -e --id Microsoft.AzureCLI`. For more details, see [Install Azure CLI on Windows](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-windows?tabs=azure-cli).

* Your Azure subscription ID. For more details, see [Find your Azure subscription](https://learn.microsoft.com/en-us/azure/azure-portal/get-subscription-tenant-id#find-your-azure-subscription).

* Azure region that you will select during installation.

**To run the verification script**

1. Download this [verification script](https://documentation.cluedin.net/assets/ps1/check.ps1).
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

## Configure firewall settings

Your Azure Firewall should cover the following:
- **Default AKS functionality** – logs and pods should be able to see Kubernetes API Server (as recommended in [Outbound network and FQDN rules for AKS clusters](https://learn.microsoft.com/en-us/azure/aks/outbound-rules-control-egress)).
- **CluedIn resource access** – resources needed for the CluedIn installation.

For the list of firewall rules that should be added to your Azure Firewall, see [Configure firewall](https://documentation.cluedin.net/operate/configuration/configure-firewall.md).

> **Important:** If the rules have not been added, the installation will fail.

## Configure network settings

CluedIn is very flexible in terms of network configuration and comes out of the box with a new vnet with a predefined address space and subnet. CluedIn is isolated out of the box, and this should work for most setups, but we do allow granular control over the network to support zero-trust and integrations.

If you prefer to use an existing vnet or would like to do some advanced configuration, please contact one of our infrastructure experts before installation to ensure it's properly implemented as it can be challenging to change post-deployment.

### Define VNet

During the installation process, you will have the option to update the vnet from the default address space of `10.0.0.0/8` and a subnet `10.0.0.0/16` for the Azure Kubernetes Service. 

If you have an existing VNet and you want to reuse it for CluedIn installation, contact one of our infrastructure experts for assistance. You can specify the existing VNet in the [Network and monitoring](https://documentation.cluedin.net/operate/azure-marketplace/step-3.md#review-the-network-and-monitoring-tab) step of CluedIn installation.

### Analyze CluedIn network configuration

The following diagram shows default CluedIn network configuration after installation.

![CluedIn network architecture: ingress traffic reaches an internal load balancer and haproxy-ingress in the AKS subnet, which hosts the CluedIn pods and node pools; Helm and kubectl reach the AKS control plane through DNS; egress goes through an external load balancer and firewall to cluedinprod.azurecr.io](https://documentation.cluedin.net/assets/images/ama/install-guide/network-diagram-1.png)

The deployed Azure Kubernetes Service is deployed with a single Azure Load Balancer that is used for both ingress and egress traffic. It is possible to update this post-deployment so that access is only possible via internal vnet integration, but it does require a number of steps.

If you would like support on this, please reach out to one of CluedIn's infrastructure engineers to assist you with this change.

More information regarding networking can be found in[Advanced network configuration](https://documentation.cluedin.net/operate/configuration/advanced-network.md).

## Analyze Azure policies and tagging

The installation wizard supplies consumers to add resource tags during runtime. Please be aware of how tagging works before going through the installation as additional steps may be required.

Tags supplied at runtime will apply to the deployed CluedIn resources. This includes the AKS cluster, key vault, virtual network, log analytics, and a few other resources.

It does not apply to the managed resource group, the AKS node resource group, or the managed application resource itself. This is a limitation of how the Marketplace Applications works.

If your tenant has comprehensive tagging, it is recommended to add a temporary exemption for the subscription at install time, and then add tags post-deployment.

## Results

1. You are qualified to perform the CluedIn installation process, and you have all the required permissions.
1. Your Azure subscription can sustain the required quota.
1. You have registered the required resource providers.
1. Your firewall is ready and configured to support the installation of CluedIn.
1. You have planned your network architecture.
1. Your security team is comfortable with CluedIn having co-ownership of the deployed resources.

## Next steps

Start the CluedIn installation process as described in our [Installation guide](https://documentation.cluedin.net/operate/azure-marketplace/step-3.md).

Up: [Azure Marketplace](https://documentation.cluedin.net/operate/azure-marketplace.md)
