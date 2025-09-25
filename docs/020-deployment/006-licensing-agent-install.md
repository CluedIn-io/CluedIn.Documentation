---
layout: cluedin
title: CluedIn Licensing Agent
parent: Installation
permalink: /deployment/marketplace-licensing-agent
nav_order: 2
has_children: true
tags: ["deployment", "licensing-agent", "azure", "microsoft", "marketplace", "azure-marketplace"]
headerIcon: "paas"
---

## CluedIn Licensing Agent

The CluedIn licensing agent is delivered as an Azure Managed Application and is installed via the Azure Marketplace. It enables CluedIn to bill customers directly through the Marketplace.

The installation process is straightforward: you complete a short form, which then provisions a Managed Application in the customer’s azure subscription. Once installed, any agreed CluedIn charges can be billed to that subscription.

{:.important}
The person performing the installation must have the appropriate Azure permissions to install paid applications. While the process is generally simple, please note that existing Azure policies can sometimes block the installation.

## Installation Steps
In the Azure Marketplace, navigate to our PaaS offering:     [CluedIn Master Data Management](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/cluedin.azure_cluedin?tab=Overview).

  - On the CluedIn Master Data Management page, select Get It Now.
  ![ama-cluedin-page.png]({{ "/assets/images/ama/install-guide/ama-cluedin-page.png" | relative_url }})
  - Under Software plan, choose the option that suits your needs:
    CluedIn Licensing Agent – select this plan to install the licensing agent.
  ![paas-software-plan.png]({{ "/assets/images/deployment/paas-installation-guide/licensing-agent-plan.png" | relative_url }})
  - Review your contact information and select Continue to proceed.
  - Review your contact information, and then select **Continue**.

### Basics Tab
#### Project Details

1. In **Subscription**, select the Azure subscription where you want to install CluedIn.
2. In **Resource group**, create a new resource group.

   ![Basics_tab_Project_details.png]({{ "/assets/images/ama/install-guide/ama-install-basic-tab-1.png" | relative_url }})

   > You may also select an existing resource group, but it must be empty. If the selected resource group contains other Azure resources, an error will occur.

#### Instance Details

1. In **Region**, specify the Azure region where the resources will be created. Typically, this should match the region of your resource group.
2. Enter the following information:

   * **Name**
   * **Company Name**
   * **Contact Name**
   * **Contact Email**
3. Verify that the **Managed Application Details** section is filled in correctly:

   * Keep the application name as **cluedinlicense**.
   * The managed resource group is usually filled in by default, but you can make changes if required.

   ![managed-app-details.png]({{ "/assets/images/deployment/paas-installation-guide/licensing-agent-basics-tab.png" | relative_url }})

#### License

* In the **License** section, keep the installation name as **cluedinlicense**.

  ![Licensing-agent-Name.png]({{ "/assets/images/deployment/paas-installation-guide/licensing-agent-licesne-tab.png" | relative_url }})

### Review + Create Tab

1. Review all settings and accept the terms and conditions.
2. When you are ready to deploy to your cloud environment, select **Create**.
3. After a few minutes, the Azure portal will notify you once the installation is complete.
