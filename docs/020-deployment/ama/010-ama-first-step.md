---
layout: default
nav_order: 1
parent: Azure Marketplace
grand_parent: Deployment
permalink: /deployment/azure-marketplace/step-1
title: 1. Business decisions
tags: ["deployment", "ama", "marketplace", "azure"]
last_modified: 2023-06-20
---

CluedIn is an Azure Managed Application (AMA) that is deployed within your company's Azure infrastructure. As a managed application, CluedIn is easy to deploy and operate. In addition, our support team can help you with the installation processes.

In this article, you will learn about the decisions you need to make before starting the CluedIn installation process.

![Business decisions before installation](../../assets/images/ama/install-guide/overview-first-step.png)

# Choose a license

We offer two types of licenses: [pay-as-you-go](#pay-as-you-go-license) and [committed-deal](#committed-deal-license).


|  | Pay-as-you-go | Committed-deal |
|--|--|--|
| All CluedIn features | Yes | Yes |
| Billing | Per hour | Upfront |
| Discount on billing | No | Yes |
| CluedIn support | No | Yes |
| Welcome package | No | Yes |

## Pay-as-you-go license

If you choose the **pay-as-you go license**, you can install CluedIn directly from the Azure Marketplace and start using it without the need to contact anyone at CluedIn. Check out our [training materials](https://vimeo.com/showcase/10332033) to get started. With this type of license, you do not get a fixed price for using CluedIn and you will be charged per hour of use.

## Committed-deal license

If you choose the **committed-deal license**, contact your Account Executive or our [sales team](https://www.cluedin.com/get-in-touch)  to discuss the contract. We’ll make sure you get the best deal to get started with CluedIn. After you sign the contract, we’ll send you the **license key by email**.

The committed-deal license comes with such benefits as a **welcome package**, which includes real-time training where we explain how to run a CluedIn project, and a **fixed price** for the license. In addition, you will automatically get 2 free CluedIn licenses for **development and test environments**.

We recommend using 3 different environments:

- **Development** – for your development team or partner customizing your CluedIn application.  
- **Test** – for your business users to validate the changes made by the development team.
- **Production** – for real data and daily operations.

The license type is required during the installation of CluedIn from the Azure Marketplace, so be sure to tell your Azure Administrator which license type you want.

# Choose a plan

We offer three types of plans: Essential, Professional, and Elite.

Before choosing a plan, consider **how many records you want to process**. The more records you want to process, the more CPU cores you will need.

Review the details of each plan to choose the one that is right for you.


|  | Essential | Professional | Elite |
|--|--|--|--|
| **All licenses** |  |  |  |
| CluedIn features | All | All | All |
| CPU cores | 8 | 16 | 32 |
| Records | Up to 500,000 | Up to 2,000,000 | Up to 5,000,000 |
| Overcharge fees for exceeding the maximum number of records | $6 per hour per license | $7 per hour per license | $5 per hour per license |
| Maintenance (for AMA installation) | Yes | Yes | Yes |
| Maintenance (for Vanilla installation) | No | No | No |
| **Committed-deal license** |  |  |  |
| CluedIn support | Yes | Yes | Yes |

The plan is required during the installation of CluedIn from the Azure Marketplace, so be sure to tell your Azure Administrator which plan you want.

**Exceeding the maximum number of records?**

If you exceed the maximum number of records allowed for your plan, you will be charged an additional fee (as mentioned in the **Overcharge fees** row in the table). We encourage you to contact us directly to check if there is a more efficient plan for you.

# Get familiar with billing

The invoice for using CluedIn will be based on the following:

- Type of license
- Number of licenses
- Plan

With the pay-as-you-go license, you’ll be charged per hour of using CluedIn. With the committed-deal license, you get a fixed price for using CluedIn that you pay upfront.

Your CluedIn instance sends us information about your **license** and the **number of records** that were processed. We need to verify that you have a valid license and that the number of records is within your plan. If you exceed the number of records, you’ll be charged an additional fee.

We send the billing information to the Azure Marketplace. Every month, you’ll get an Azure invoice that will include:
- **CluedIn usage**, which you discuss directly with CluedIn.
- **Azure hosting**, which covers all your Azure services.

To pay an invoice, contact your procurement team.

# Review terms and conditions

For CluedIn, we use the [Standard Contract from Microsoft](https://www.cluedin.com/hubfs/microsoft-standard-contract-march-2019.pdf) . Please note that if you are a Microsoft user, your legal department has probably already approved this Standard Contract.

To make sure that the terms and conditions are appropriate for you, contact your legal team.

# Choose Azure Administrator

Now that you have decided on your license and plan and reviewed our billing and legal information, you are ready to start the CluedIn installation process.

The CluedIn installation process must be performed by an IT professional who is skilled in managing your organization’s Microsoft Azure environment. So, make sure that you choose a dedicated **Azure Administrator** from your organization who will be responsible for the installation. 

# Results

1. You have decided which license you need. If you have chosen the committed-deal license, then you should have a license key issued to you by CluedIn.
1. You have chosen a plan based on the number of records that you want to process.
1. You understand how CluedIn will issue invoices.
1. You are comfortable with our Standard Contract from Microsoft.
1. You have chosen an Azure Administrator who will be responsible for carrying out the CluedIn installation process.


# Next steps

Provide your Azure Administrator with the following information:

- If you have signed a committed deal:
  - Email with the license key issued by CluedIn.
  - Link to our [Pre-installation checklist](https://dev.azure.com/CluedIn-io/CluedIn/_wiki/wikis/CluedIn.wiki/1184/Step-2-Pre-installation-checklist).

- If you have decided to use the pay-as-you-go approach:
  - Plan that you have chosen.
  - Link to our [Pre-installation checklist](https://dev.azure.com/CluedIn-io/CluedIn/_wiki/wikis/CluedIn.wiki/1184/Step-2-Pre-installation-checklist).


