---
layout: cluedin
nav_order: 4
parent: CluedIn PaaS
grand_parent: Installation
permalink: /deployment/azure-marketplace/step-3
title: Installation guide
tags: ["deployment", "ama", "marketplace", "azure"]
last_modified: 2023-06-20
---
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

In this article, you will learn how to install CluedIn PaaS from the Azure Marketplace.

{:.important}
Make sure that you have completed all of the actions described in [Pre-installation checklist](/deployment/azure-marketplace/step-2).

![paas-installation-diagram.gif](../../assets/images/deployment/paas-installation-guide/paas-installation-diagram.gif)

## Find CluedIn

Start the installation process by finding CluedIn PaaS in the Azure Marketplace.

**To find CluedIn**

1. In the Azure Marketplace, go to our PaaS offering: [CluedIn Master Data Management](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/cluedin.azure_cluedin?tab=Overview).

1. On the **CluedIn Master Data Management** page, select **Get It Now**.

    ![ama-cluedin-page.png](../../assets/images/ama/install-guide/ama-cluedin-page.png)

1. In **Software plan**, select the plan of your choice:

    - **CluedIn MDM PaaS - Existing License** – select this option if you possess a CluedIn PaaS license key acquired through a committed deal.

    - **CluedIn MDM PaaS - Pay As You Go** – select this option if you want to use CluedIn on a pay-as-you-go basis. For more information, see [Pricing](/deployment/pricing).

        ![paas-software-plan.png](../../assets/images/deployment/paas-installation-guide/paas-software-plan.png)

1. Review your contact information, and then select **Continue**.

## Complete the Basics tab

On the **Basics** tab, you can select the Azure resource group where CluedIn will be installed and provide license or company details depending on the chosen software plan.

**To complete the Basics tab**

1. Fill in the **Project details** section:

   1. In **Subscription**, select your Azure subscription where you want to install CluedIn.

   1. In **Resource group**, create a new resource group.

        ![Basics_tab_Project_details.png](../../assets/images/ama/install-guide/ama-install-basic-tab-1.png)

        You can select the existing resource group, but it must be empty. If the resource group that you select contains other Azure resources, you will get an error.

1. Fill in the **Instance details** section:

    1. In **Region**, specify the Azure region where different resources will be created. The region will probably match your resource group location.

    1. Depending on the selected software plan, do one of the following:

        - If you selected **CluedIn MDM PaaS - Existing License**, enter the license key that you should have received in an email from CluedIn.

            ![instance-details-license.png](../../assets/images/deployment/paas-installation-guide/instance-details-license.png)

        - If you selected **CluedIn MDM PaaS - Pay As You Go**, enter the **Company name** and **Contact Email Address**.

            ![instance-details-payg.png](../../assets/images/deployment/paas-installation-guide/instance-details-payg.png)

1. Make sure that the **Managed Application Details** section is filled out correctly. This section is usually filled out by default, but you can make changes if needed.

    ![managed-app-details.png](../../assets/images/deployment/paas-installation-guide/managed-app-details.png)

## Complete the Instance Setup tab

On the **Instance Setup** tab, you can create the organization used within the CluedIn application along with an administrator account for your CluedIn instance as well as optionally specifying SMTP details.

**To complete the Instance Setup tab**

1. Make sure that the **Installation Name** field is filled out correctly. This field is usually filled out by default, but you can make changes if needed. This is the name of the Managed Application resource that gets created within the resource group specified on the **Basics** tab.

1. Specify organization details:

    1. Specify **Organization Name**. The organization name will be used as part of the URL. Ideally, it should be one word with no dashes or hyphens.

    1. Specify **Administrator Email Address**.

    1. Specify **CluedIn Administrator Password**, and then **Confirm password**. The password must be more than 12 characters long.

        ![Initial_setup_tab_Organization_details.png](../../assets/images/ama/install-guide/ama-install-basic-tab-3.png)

1. Specify SMTP details:

    1. Specify **SMTP - Server**.

    1. In **SMTP - Port**, specify SSL port.

    1. Add details about the email that will be used for sending invitations to other users to join CluedIn.

        ![Initial_setup_tab_SMTP.png](../../assets/images/ama/install-guide/ama-install-basic-tab-4.png)

        {:.important}
        You can change SMTP details after installation by submitting a ticket to CluedIn support.

## Review the Network and Monitoring tab

On the **Network and Monitoring** tab, you can review vNet default configuration settings and make changes if needed.

![network-and-monitoring.png](../../assets/images/deployment/paas-installation-guide/network-and-monitoring.png)

## Review the Azure Kubernetes tab

On the **Azure Kubernetes** tab, you can customize the number of nodes that you want to use in your CluedIn instance, and you can also define autoscaling parameters.

{:.important}
In most cases, you do not need to adjust anything on this tab unless advised to do so by CluedIn support.

The **AKS Setup** tab contains the following settings:

- **General Node Size** that runs the main application services. **General Node Pool VM Count** contains a minimum number of VMs to ensure that all resources can be scheduled. If you need to increase the VM count, consult with CluedIn support. 

- **Data Node Size** that runs any database and data collection services. **Data Node Pool VM Count** contains a minimum number of VMs to ensure that all resources can be scheduled. If you need to increase the VM count, consult with CluedIn support.

- **Data ES Node Size** and **Data ES Node Pool VM Count**.

- **Processing Node Size** that runs any CluedIn processing services. **Processing Node Size** depends on the license you have specified. If it is a pay-as-you-go installation, a basic SKU will be used at runtime.

![azure-kubernetes.png](../../assets/images/deployment/paas-installation-guide/azure-kubernetes.png)

You can enable **auto-scaling** for the processing node pool. It means that when CPU pressure (high workload) builds up in this node pool, AKS can start up new nodes to compensate for the increase in load. When the load returns to normal, the extra nodes will be shut down. However, be aware that there are additional infrastructure and licensing costs associated with scaling up. For more information about auto-scaling, contact CluedIn support.

{:.important}
You can enable auto-scaling after installation.

## Review the Advanced tab

On the **Advanced** tab, you can find technical and debugging switches that are used by CluedIn support. Most of the options on this tab should not be adjusted. Any misconfiguration or changes to these options can cause the installation to fail.

{:.important}
You can make changes on this tab only with the advice of CluedIn support.

![advanced.png](../../assets/images/deployment/paas-installation-guide/advanced.png)

## Review the Tags tab

On the **Tags** tab, you can add tags to categorize your resources and view consolidated billing by applying the same tag to multiple resources and resource groups.

{:.important}
Tags do not get applied to the managed application resource itself. This may cause issues if you have comprehensive tagging policies in place. 

![tags.png](../../assets/images/deployment/paas-installation-guide/tags.png)

## Complete the Review + Create tab

On the **Review + Create** tab, review and accept the terms and conditions. To start the deployment process in your own cloud environment, select **Create**.

## Results

You have CluedIn running in your own cloud environment.

## Next steps

Customize CluedIn to meet your organization's needs as described in our [Post-installation guide](/deployment/azure-marketplace/step-4).
