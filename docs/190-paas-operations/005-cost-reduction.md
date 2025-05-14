---
layout: cluedin
title: Operating cost reduction
parent: PaaS operations
permalink: /paas-operations/cost-reduction
nav_order: 5
tags: ["kubernetes", "azure", "aks", "microsoft", "marketplace", "azure-marketplace", "cost", "reduction", "reducing"]
headerIcon: "paas"
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

CluedIn runs on Azure Kubernetes Service (AKS), which uses node pools as the underlying resources. As part of the deployment, many Azure resources will be created in your environment, each with its own costs associated with it.

The purpose of this guide is to explain what you can do to reduce the cost of CluedIn in your environment whilst maintaining a supported setup.

To find out about the base cost, see [CluedIn Azure costs](https://www.cluedin.com/cluedin-azure-costs). Additionally, keep the following considerations in mind:

- You do not need to have the production environment running during development.

- You can reduce the cost of your production environment by reserving the VM:

    - A 1-year reservation can save approximately 30% of the base cost.
    
    - A 3-year reservation can save up to 50% of the base cost.

- We can provide and set up a script for scaling the environment up or down, potentially saving up to 40% of the base cost.

## Shut down environments in times of low or no usage

CluedIn is a product that is intended to run as part of your MDM pipeline. As a business, this may be during certain hours of the day (e.g. 0900-1700), which means that outside of these hours, the environments will be running and not being used.

One easy way to reduce cost is to shut down your AKS during these hours and start the environment back up when it is needed. We only recommend these for your **dev** and **test** environments, and not production. Stopping the AKS cluster reduces costs, but you will still pay for other resources such as storage, networking, and so on. However, the overall cost will be significantly reduced.

**To stop AKS cluster**

1. Navigate to https://portal.azure.

1. Search for the Managed Resource Group (MRG) that houses your CluedIn instance.

1. Select the Kubernetes service resource. It usually starts with `aks-` followed by a unique string.

1. At the top, select **Stop**, which should then begin to power down your instance.

If you require any further assistance, reach out to CluedIn support. The CluedIn team can help set this up in your environment by deploying an Automation Account along with a runbook and setting the schedule at your preferred downtime.

## Reserve Azure instances

Azure, like many cloud services, offers the ability to reserve virtual machines and other Azure resources upfront by committing to a year or more. This is one of the ways to save up to 72% on the virtual machine resources and is something we recommend when you are serious about CluedIn.

For more information, see [Microsoft documentation](https://azure.microsoft.com/en-gb/pricing/reserved-vm-instances).

## Run a local environment

CluedIn is container-based and therefore can run on almost any kind of setup that can run containers. We support [local installation](/deployment/local), which eliminates the need for a full cluster setup for development purposes. It still requires quite a powerful machine but there are no running costs as a result.

This is only recommended for experienced IT professionals due to the complexity of setting up a local running instance.

For more information, refer to the local installation [documentation](/deployment/local) or reach out to CluedIn support who will be happy to answer any questions.