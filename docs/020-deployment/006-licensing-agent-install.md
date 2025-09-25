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

The CluedIn licensing agent is delivered as an Azure Managed Application and is installed via the Azure Marketplace. It enables CluedIn to bill customers directly through the Marketplace.

The installation process is straightforward: you complete a short form, which then provisions a Managed Application in the customer’s azure subscription. Once installed, any agreed CluedIn charges can be billed to that subscription.

The person performing the installation must have the appropriate Azure permissions to install paid applications. While the process is generally simple, please note that existing Azure policies can sometimes block the installation.

**To find CluedIn**

1. In the Azure Marketplace, go to our PaaS offering: [CluedIn Master Data Management](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/cluedin.azure_cluedin?tab=Overview).

1. On the **CluedIn Master Data Management** page, select **Get It Now**.

    ![ama-cluedin-page.png]({{ "/assets/images/ama/install-guide/ama-cluedin-page.png" | relative_url }})

1. In **Software plan**, select the plan of your choice:

    - **CluedIn Licensing Agent** – select this option to install licensing agent. 

        ![paas-software-plan.png]({{ "/assets/images/deployment/paas-installation-guide/licensing-agent-plan.png" | relative_url }})

1. Review your contact information, and then select **Continue**.

**To complete the Basics tab**

1. Fill in the **Project details** section:

   1. In **Subscription**, select your Azure subscription where you want to install CluedIn.

   1. In **Resource group**, create a new resource group.

        ![Basics_tab_Project_details.png]({{ "/assets/images/ama/install-guide/ama-install-basic-tab-1.png" | relative_url }})

        You can select the existing resource group, but it must be empty. If the resource group that you select contains other Azure resources, you will get an error.

1. Fill in the **Instance details** section:

    1. In **Region**, specify the Azure region where different resources will be created. The region will probably match your resource group location.

    1. Fill the Basic information in the fields **Name, Company Name, Contact name and Contact Email** 

    1. Make sure that the **Managed Application Details** section is filled out correctly. Keep the application name as **cluedinlicense**  and the managed resource group section is usually filled out by default, but you can make changes if needed.

    ![managed-app-details.png]({{ "/assets/images/deployment/paas-installation-guide/licensing-agent-basics-tab.png" | relative_url }})

1. Fill in the **Licesne** section:

    1. In the **License** section keep the Installation name as **cluedinlicense** 
     
     ![Licensing-agent-Name.png]({{ "/assets/images/deployment/paas-installation-guide/licensing-agent-licesne-tab.png" | relative_url }})

## Complete the Review + Create tab

On the **Review + Create** tab, review and accept the terms and conditions. To start the deployment process in your own cloud environment, select **Create**.

## Results

You have CluedIn Licensing Agent running in your own cloud environment.     