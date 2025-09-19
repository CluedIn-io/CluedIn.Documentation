---
layout: cluedin
nav_order: 5
parent: Playbooks
permalink: /playbooks/start-your-it-journey
title: Start your IT journey
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

| Audience | Time to read |
|--|--|
| Administrator | 7 min |

This article outlines the key stages of your IT journey, from installing CluedIn and integrating it with necessary external systems and sources, to ensuring that user access aligns with your organization policies.

## Main aspects of IT journey

There are several aspects of the IT journey that you should consider in order to configure CluedIn according to your business needs. 

![connections.png]({{ "/assets/images/playbooks/connections.png" | relative_url }})

The primary aspect is **authentication and authorization** to ensure that only legitimate users can access the system.

Your business data typically resides in various sources, such as databases, ERP systems, CRM systems, and other applications. One of the key tasks in CluedIn is data ingestion, which requires establishing **connections to these data sources**. Additionally, to enrich your data with information from third-party sources, you can **connect to the appropriate enrichers**. Finally, to share ready-to-use data, CluedIn must **connect to the external systems** of your choice, often referred to as landing zones. All these tasks are part of the IT journey.

In this section, you'll find recommendations for the starting points of each aspect of the IT journey.

### Authentication and authorization

Establish the groundwork based on the rules of your IT organization. You will likely need to use your **single sign-on (SSO)** systems and roles in CluedIn.

If you are starting with the development environment, perhaps SSO is not needed for it. If it is, CluedIn can assist, but always try to minimize steps to get started on your project.

### Connection to the sources

For your first use case, CluedIn will likely need to connect to the source. This generally involves IT steps managed by the system administrator.

Here are some scenarios that explain the actions to take for different levels of access to the source:

- Full API access – discuss next steps with your CluedIn expert.  

- File export access – if full access is not possible, but you can get an export file, use that file. 

- No access – if you can't get access, ask for the shape of the data and fake it. If you can't even get this, escalate. Data is the fuel of your data transformation journey. CluedIn has encountered these situations many times, so let us know if you need help.

### Connection to enrichers

Enrichers are slightly more challenging because we can't really fake them. You either have access or you don't. If you don't have access to one enricher, try another provided by CluedIn that doesn't rely on IT (for example, Libpostal). It is important to see enrichers in action for a value perspective. It's like having free, quality data at your disposal. But if you can't access enrichers now, don't wait and move forward. CluedIn is an agile platform, and you can always revisit this later.

### Connection to export targets

As a CluedIn user, you'll want to share your improved data with other systems or places in your organization. To do this automatically, you'll want to export directly to another source. As with any IT integration, you'll need an owner ready to receive the data.

If you face resistance or are blocked, there's a trick: you can stream into the CluedIn database directly. This exercise proves that you are streaming the data to external destination. After all, it is better to have one stream than no stream. This will help you understand the kind of data you're sending and the pace.

## Types of IT journey

You have the flexibility to adopt CluedIn at your own pace. Since we offer 2 cloud models of CluedIn—PaaS and SaaS—the IT journey for each is different. In this section, you'll find the details about IT journey for both SaaS and PaaS.

![cloud-service-model.png]({{ "/assets/images/playbooks/cloud-service-model.png" | relative_url }})

### SaaS IT journey

With CluedIn SaaS, the installation process is fully automated: we'll provide everything you need to install CluedIn. What is more, if you have a committed SaaS deal, we can offer you a development or test environment at hosting cost. However, keep in mind that we'll have to work together to implement the [main aspects of IT journey](#main-aspects-of-it-journey) in order to configure CluedIn for your business needs.

{:.important}
CluedIn team performs installation activities on all business days **except Friday**. Deploying on a Friday carries higher risk because issues may not surface immediately and can escalate into weekend incidents with fewer people available to respond. As a best practice, it is recommended to schedule installations earlier in the week (Tuesday–Thursday) to allow time for monitoring, troubleshooting, and stabilization.

Useful links to learn more about CluedIn SaaS:

- [CluedIn SaaS installation](/deployment/saas)

- [Onboarding path for CluedIn SaaS](/get-cluedin#onboarding-path-for-cluedin-saas)

### PaaS IT journey

With CluedIn PaaS, the installation process is automated, enabling you to install CluedIn in your own Azure infrastructure. The entire installation process can be **simple and straightforward**, especially if **full access** is provided to CluedIn and the IT team. Our experience in installing CluedIn in some of the most challenging environments ensures that we’re well-equipped to support you throughout the process. To facilitate a smooth installation process, we typically schedule meetings for each step:

- [Pre-installation check](/deployment/azure-marketplace/step-2)

- [Installation](/deployment/azure-marketplace/step-3)

- [Post-installation](/deployment/azure-marketplace/step-4)

![paas-it-journey.png]({{ "/assets/images/playbooks/paas-it-journey.png" | relative_url }})

These meetings give you the opportunity to discuss any questions or concerns you may have with a CluedIn expert, ensuring that you're fully informed and comfortable at every stage of your IT journey.

{:.important}
CluedIn team performs installation activities on all business days **except Friday**. Deploying on a Friday carries higher risk because issues may not surface immediately and can escalate into weekend incidents with fewer people available to respond. As a best practice, it is recommended to schedule installations earlier in the week (Tuesday–Thursday) to allow time for monitoring, troubleshooting, and stabilization.

The CluedIn PaaS **IT journey timeline** depends on two aspects:

- **Privilege** – this refers to the access level you have in the given resource group where CluedIn is installed (read-only, partial edit, full edit).

- **Access to resource** – this refers to your access for connecting to the CluedIn cluster (you can connect, you can connect but require an approval, or you can't connect and someone has to give access to CluedIn cluster).

![paas-it-timeline.png]({{ "/assets/images/playbooks/paas-it-timeline.png" | relative_url }})

Based on your privileges and access to the resource group, there can be 3 IT journey scenarios:

1. **CluedIn PaaS managed service** – with high privilege and access to the resource group, the installation and IT journey might take days.

2. **CluedIn PaaS managed instance** – with high privilege but limited access to the resource group, the installation and IT journey might take weeks.

3. **CluedIn PaaS self-hosted** – with no privilege and no access to the resource group, the installation and IT journey might take months.

### Installation in a restrictive environment

The entire IT journey can be smooth and easy, but it will **depend on your IT infrastructure and the policies** in place. Since CluedIn requires connections to various [external systems and sources](#main-aspects-of-it-journey), you may need to take additional steps during IT journey. If your infrastructure is restrictive, you might face problems related to network restrictions, private and service endpoints, custom DNS settings, firewall policies, token expiration, and so on. If this is your case, we might have to work with you on the following tasks to **set up the foundational infrastructure**:

- Creation of a Virtual Network (VNet) with 2 subnets:

    - AKS subnet – dedicated subnet for AKS resources.

    - Delegated subnet for CI – subnet specifically delegated for Container Instance (CI) operations.

- Configuration of service endpoints for secure access to storage account and key vault.

- Enabling the routing table and network security groups (NSGs) for network management and enhanced security.

- Creation of user identity to manage access and permissions across the infrastructure.

Depending on your **security and infrastructure policies**, we might have to implement some of the following changes:

- Remove automatic creation and assignment of user identities from the publisher onboard module to streamline security management.

- Disable the setup of a private DNS zone in the storage account.

- Configure the storage account and the key vault to use only private endpoints.

- Other changes might be required to comply with your security and infrastructure policies.

Additionally, your Azure administrator might be required to perform the following tasks to **support infrastructure provisioning**:

- Role assignments:

   - Assign the Owner role to manage resources.

   - Assign the Storage File Data Contributor role at the storage account to manage file-level permissions.

   - Assign the Key Vault Administrator role to the user identity to enable Key Vault management and secret handling.

- Private DNS Zone Vnet Link:

   - Virtual network link enabled for [privatelink.file.core.windows.net](http://privatelink.file.core.windows.net/)

   - Virtual network link enabled for [privatelink.blob.core.windows.net](http://privatelink.blob.core.windows.net/)

   - Virtual network link enabled for [privatelink.vaultcore.azure.net](http://privatelink.vaultcore.azure.net/)

{:.important}
The tasks listed above are provided as an example. They may or may not fit your IT infrastructure and policies. You can discuss your requirements and plan the IT journey with a CluedIn expert.<br>CluedIn team performs installation activities on all business days **except Friday**. Deploying on a Friday carries higher risk because issues may not surface immediately and can escalate into weekend incidents with fewer people available to respond. As a best practice, it is recommended to schedule installations earlier in the week (Tuesday–Thursday) to allow time for monitoring, troubleshooting, and stabilization.

Useful links to learn more about CluedIn PaaS:

- [CluedIn PaaS installation](/deployment/azure-marketplace)

- [Onboarding path for CluedIn PaaS](/get-cluedin#onboarding-path-for-cluedin-paas)

- [CluedIn PaaS operations](/paas-operations)