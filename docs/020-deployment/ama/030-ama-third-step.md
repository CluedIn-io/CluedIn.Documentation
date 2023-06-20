---
layout: default
nav_order: 1
parent: Azure Marketplace
grand_parent: Deployment
permalink: /deployment/azure-marketplace/step-2
title: 3. Installation guide
tags: ["deployment", "ama", "marketplace", "azure"]
last_modified: 2023-06-20
---


In this article, you will learn how to install CluedIn from the Azure Marketplace.

**Important!** Make sure that you have completed all of the actions described in [Pre-installation checklist](https://dev.azure.com/CluedIn-io/CluedIn/_wiki/wikis/CluedIn.wiki/1184/Step-2-Pre-installation-checklist).

![How_to_install_CluedIn.png](/.attachments/How_to_install_CluedIn-807aed97-fa53-4963-8e20-3d786204dd7d.png =900x)

# Find CluedIn

Start the installation process by finding CluedIn in the Azure Marketplace.

**To find CluedIn**

1. In the Azure Marketplace, search for CluedIn.
1. From the results, select **CluedIn Master Data Management**.
![Azure_Marketplace_CluedIn.png](/.attachments/Azure_Marketplace_CluedIn-837b759f-669d-4ce1-84eb-419748196c29.png =250x)
1. On the **CluedIn Master Data Management** page, select **Get It Now**.
1. In the dialog box that appears, in **Software plan**, select **CluedIn Platform**.
![Azure_Marketplace_Software_Plan.png](/.attachments/Azure_Marketplace_Software_Plan-9d7f8d4e-24b5-4d9e-9647-c0596d8baa9b.png =500x)
1. Review your contact information, and then select **Continue**.

# Complete the Basics tab
On the **Basics** tab, you can select the Azure resource group where CluedIn will be installed and provide license details.

**To complete the Basics tab**

1. Fill in the **Project details** section:
   1. In **Subscription**, select your Azure subscription where you want to install CluedIn.
   1. In **Resource group**, create a new resource group.
![Basics_tab_Project_details.png](/.attachments/Basics_tab_Project_details-e66bf2c3-4e67-4439-9715-3aab349d8799.png =650x)
You can select the existing resource group, but it must be empty. If the resource group that you select contains other Azure resources, you will get an error.
2. Fill in the **Instance details** section:
   1. In **Region**, specify the Azure region where different resources will be created. The region will probably match your resource group location.
   1. Depending on whether you have the license key, do one of the following:
      - If you have the license key, in **CluedIn License Version**, select **Existing License Key**. Then, in **CluedIn License Key**, paste the license key.
      - If you don't have the license key, in **CluedIn License Version**, select a plan that was chosen by your company (Essential, Professional, or Elite).

   1. Make sure that the **Installation Name** field is filled out correctly. This field is usually filled out by default, but you can make changes if needed.
![Basics_tab_Instance_details.png](/.attachments/Basics_tab_Instance_details-e1699bc4-f139-4288-b336-708d9d469942.png =650x)
1. Make sure that the **Managed Application Details** section is filled out correctly. This section is usually filled out by default, but you can make changes if needed.

# Complete the Initial Setup tab

On the **CluedIn - Initial Setup** tab, you can create the organization and the administrator account for your CluedIn instance, specify SMTP details, and enable SSO.

**To complete the Initial Setup tab**

1. Specify organization details:
   1. Specify **Organization Name**. The organization name will be used as part of the URL. Ideally, it should be one word with no dashes or hyphens.
   1. Specify **Administrator Email Address**.
   1. Specify **CluedIn Administrator Password**, and then **Confirm password**. The password must be more than 12 characters long.
![Initial_setup_tab_Organization_details.png](/.attachments/Initial_setup_tab_Organization_details-54c98d4c-83d7-4508-84c2-19b73e8c7ed6.png =650x)
2. Specify SMTP details:
   1. Specify **SMTP - Server**.
   1. In **SMTP - Port**, specify SSL port.
   1. Add details about the email that will be used for sending invitations to other users to join CluedIn.
![Initial_setup_tab_SMTP.png](/.attachments/Initial_setup_tab_SMTP-7908849f-1be1-45c0-b036-9e57fc5ea838.png =650x)
**Important!** You can change SMTP details after installation by submitting a ticket to CluedIn support.
1. If needed, enable SSO access for CluedIn, and then specify SSO details.
![Initial_setup_tab_SSO.png](/.attachments/Initial_setup_tab_SSO-444dd67d-7ba0-48a2-8143-ead9eb138ead.png =650x)
**Important!** You can enable SSO access for CluedIn after installation. This is often the preferable option because some mapping of Azure AD groups to product groups is required. For more information, see [SSO](https://dev.azure.com/CluedIn-io/CluedIn/_wiki/wikis/CluedIn.wiki/1211/SSO).

# Review the AKS Setup tab
On the **CluedIn - AKS Setup** tab, you can customize the number of nodes that you want to use in your CluedIn instance, and you can also define autoscaling parameters.

**Important!** In most cases, you do not need to adjust anything on this tab unless advised to do so by CluedIn support.

The **AKS Setup** tab contains the following settings:
- **General node pool** that runs the main application services.
![AKS_Setup_tab_General_node_pool.png](/.attachments/AKS_Setup_tab_General_node_pool-2ecfb162-1e00-4d7b-8a85-e7007b5042a1.png =650x)
**General Node Pool VM Count** contains a minimum number of VMs to ensure that all resources can be scheduled. If you need to increase the VM count, consult with CluedIn support.
- **Data node pool** that runs any database and data collection services.
![AKS_Setup_tab_Data_node_pool.png](/.attachments/AKS_Setup_tab_Data_node_pool-278a2c8f-d53f-412c-81b5-6ec90eaa2b7b.png =650x)
**Data Node Pool VM Count** contains a minimum number of VMs to ensure that all resources can be scheduled. If you need to increase the VM count, consult with CluedIn support.
- **Processing node pool** that runs any CluedIn processing services.
![AKS_Setup_tab_Processing_node_pool.png](/.attachments/AKS_Setup_tab_Processing_node_pool-c49672ac-7385-4fba-b25c-7383eb27a3c2.png =650x)
**Processing Node Size** depends on the license type you have selected on the **Basics** tab. If you have entered a license key on the **Basics** tab, then the machine type will be hidden because it is encoded into the license.
You can enable **auto-scaling** for the processing node pool. It means that when CPU pressure (high workload) builds up in this node pool, AKS can start up new nodes to compensate for the increase in load. When the load returns to normal, the extra nodes will be shut down. However, be aware that there are additional infrastructure and licensing costs associated with scaling up. For more information about auto-scaling, contact CluedIn support.
**Important!** You can enable auto-scaling after installation. 

# Review the Service Setup tab
On the **CluedIn - Service Setup** tab, you can review major services that make up CluedIn’s data layer. By default, CluedIn uses the resources provisioned inside the cluster and the Azure managed (encrypted) disks to store any data created.

**Important!** The default configuration is sufficient, so you don't need to adjust anything on this tab. You can change service details after installation by submitting a ticket to CluedIn support.

The installer can use the existing services or provision new services as part of the setup. However, the provisioning of new services may incur additional infrastructure charges from Azure.

**SQL Server**

By default, CluedIn creates an instance of SQL Server inside the cluster, backed with 1TB disks.

![Service_Setup_tab_SQL_Server.png](/.attachments/Service_Setup_tab_SQL_Server-0fb69504-34a0-4c25-9ff9-6efdffaeaa07.png =650x)

The installer can provision an Azure SQL instance (Elastic Pool) to install all the databases. The Azure SQL resource will be created inside the managed resource group.

**Redis**

By default, CluedIn creates a scalable instance of Redis inside the cluster.

![Service_Setup_tab_Redis.png](/.attachments/Service_Setup_tab_Redis-c7b8979a-d700-4ff4-aa3d-b9e0dd70b2f4.png =650x)

CluedIn can be configured to use the existing Redis instance if provided with connection details. The installer can also provide a new Azure Redis instance that will be created inside the managed resource group.

**ElasticSearch**

By default, CluedIn creates a scalable instance of ElasticSearch inside the cluster, backed with 1TB disks.

![Service_Setup_tab_ElasticSearch.png](/.attachments/Service_Setup_tab_ElasticSearch-dbd982b3-91d9-4641-bc91-4913f5b2dcce.png =650x)

CluedIn can be configured to use the existing ElasticSearch instance if provided with connection details.

**Event Hub**

By default, CluedIn doesn't create an Event Hub instance.

![Service_Setup_tab_Event_Hub.png](/.attachments/Service_Setup_tab_Event_Hub-d0faf8c8-1f6a-4d9b-b435-6f943fb4bec6.png =650x)

The installer can provide a new Azure Event Hub instance that will be created inside the managed resource group.


# Review the Advanced Configuration tab

On the **CluedIn - Advanced Configuration** tab, you can find technical and debugging switches that are used by CluedIn support. Most of the options on this tab should not be adjusted. Any misconfiguration or changes to these options can cause the installation to fail.

![Advanced_configuration_tab.png](/.attachments/Advanced_configuration_tab-a9c648f0-7f79-4fb9-93f0-a19235d9ff06.png =650x)

**Important!** You can make changes on this tab only with the advice of CluedIn support.

**Advanced Networking**

You may be required to change the address CIDR ranges of the vNet that is created. For example, you can do it if you are connecting to a vNet that has similar internal IP addresses and you want to avoid a clash.

You can enable the **Advanced Networking** section to make changes to the vNet defaults.

![Advanced_configuration_tab_Advanced_networking.png](/.attachments/Advanced_configuration_tab_Advanced_networking-792cd769-43ed-4964-a088-75b4a8c25734.png =650x)

**Important!** The installer cannot verify these IP ranges and their validity before the installation starts, so double-check all settings before proceeding.

# Complete the Review + Create tab

On the **Review + Create** tab, review and accept the terms and conditions. To start the deployment process in your own cloud environment, select **Create**.

# Results

You have CluedIn running in your own cloud environment.

# Next steps

Customize CluedIn to meet your organization's needs as described in our [Post-installation guide](https://dev.azure.com/CluedIn-io/CluedIn/_wiki/wikis/CluedIn.wiki/1189/Step-4-Post-installation-guide).
