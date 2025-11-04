---
layout: cluedin
title: CluedIn licensing agent
parent: Installation
permalink: /deployment/marketplace-licensing-agent
nav_order: 2
has_children: false
tags: ["deployment", "licensing-agent", "azure", "microsoft", "marketplace", "azure-marketplace"]
headerIcon: "paas"
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

The CluedIn licensing agent is delivered as an [Azure Managed Application](https://learn.microsoft.com/en-us/azure/azure-resource-manager/managed-applications/overview) and is installed via the Azure Marketplace. It enables CluedIn to bill customers directly through the Marketplace.

The installation process is straightforward:

1. You complete a short form, which then provisions a Managed Application in the customer’s Azure subscription.

1. Once installed, any agreed CluedIn charges can be billed to that subscription.

{: .warning}
**Azure Policy Notice**  
The installation of the licensing agent may fail if your subscription includes an Azure Policy that blocks public storage accounts. To proceed, temporarily exclude this resource group from that policy before installation.

## Prerequisites

1. **Azure account**. If you already have an Azure account, you can proceed to the next prerequisite. If you do not have an Azure account, create a [pay-as-you-go](https://azure.microsoft.com/en-us/pricing/purchase-options/pay-as-you-go/search/?ef_id=_k_EAIaIQobChMIwOntxpn2hAMV_AYGAB3AMAFmEAAYASAAEgJ8LPD_BwE_k_&OCID=AIDcmmbnk3rt9z_SEM__k_EAIaIQobChMIwOntxpn2hAMV_AYGAB3AMAFmEAAYASAAEgJ8LPD_BwE_k_&gad_source=1&gclid=EAIaIQobChMIwOntxpn2hAMV_AYGAB3AMAFmEAAYASAAEgJ8LPD_BwE) account using a valid credit card.

1. **Marketplace purchases and Contributor role**. Make sure that you have enabled Marketplace purchases and configured the required user permissions (at least **Contributor**) for the subscription where you want to store the CluedIn SaaS application. For more information, see [Enable marketplace purchases in Azure](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/enable-marketplace-purchases).

## Installation steps
1. In Azure Marketplace, navigate to [CluedIn PaaS offering](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/cluedin.azure_cluedin?tab=Overview).

1. Select **Get It Now**.

    ![ama-cluedin-page.png]({{ "/assets/images/deployment/licensing-agent/marketplace_page_get_now_button.png" | relative_url }})

1. In the **Create this app in Azure** window, under **Software plan**, select **CluedIn Licensing Agent**.

    ![licensing-agent-plan.png]({{ "/assets/images/deployment/licensing-agent/licensing-agent-plan-2.png" | relative_url }})

1. Review your contact information, and then select **Continue**.

1. On the **Basics** tab, fill in the **Project details** section:

    1. In **Subscription**, select the Azure subscription where you want to install CluedIn.

    1. In **Resource group**, create a new resource group.

        ![Basics_tab_Project_details.png]({{ "/assets/images/ama/install-guide/ama-install-basic-tab-1.png" | relative_url }})
        
        {:.important}
        You may also select an existing resource group, but it must be empty. If the selected resource group contains other Azure resources, an error will occur.

1. Fill in the instance details:

    1. In **Region**, specify the Azure region where the resources will be created. Typically, this should match the region of your resource group.

    1. Enter the following information:

        * **Name**

        * **Company Name**

        * **Contact Name**

        * **Contact Email**

    1. Verify that the **Managed Application Details** section is filled in correctly:

        * Keep the application name as **cluedinlicense**.

        * The managed resource group is usually filled in by default, but you can make changes if needed.

    ![managed-app-details.png]({{ "/assets/images/deployment/licensing-agent/licensing-agent-basics-tab.png" | relative_url }})

1. On the **License** tab, keep the installation name as **cluedinlicense**.

    ![Licensing-agent-Name.png]({{ "/assets/images/deployment/licensing-agent/licensing-agent-licesne-tab.png" | relative_url }})

1. On the **Review + create** tab, do the following:

    1. Review all settings and accept the terms and conditions.

    1. When you are ready to deploy to your cloud environment, select **Create**.

        After a few minutes, the Azure portal will notify you once the installation is complete.
