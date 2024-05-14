---
layout: cluedin
title: Operating cost reduction
parent: PaaS operations
permalink: /paas-operations/cost-reduction
nav_order: 5
has_children: true
tags: ["kubernetes", "azure", "aks", "microsoft", "marketplace", "azure-marketplace", "cost", "reduction", "reducing"]
headerIcon: "paas"
---

CluedIn runs on Azure Kubernetes Service (AKS), which uses node pools as the underlying resources. As part of the deployment, many Azure resources will be created in your environment, each with its own costs associated with it.

The purpose of this guide is to explain what you can do to reduce the cost of CluedIn in your environment whilst maintaining a supported setup.

# Shutdown environments in times of low or no usage

CluedIn is a product that is intended to run as part of your MDM pipeline. As a business, this may be during certain hours of the day (e.g. 0900-1700), which means that outside of these hours, the environments will be running and not being used.

One easy way to reduce cost is to shut down your AKS during this hours, and starting the environment back up when it's needed. We only recommend these for your **dev** and **test** environments, and not production.

The CluedIn team can help set this up in your environment by deploying an Automation Account along with a runbook and setting the schedule at your desired times of inoperation.

# Run a local environment

CluedIn is container-based and therefore can run on almost any kind of setup that can run containers.
We support [local installation](/deployment/local), which eliminates the need for a full cluster setup for development purposes. It still requires quite a powerful machine but there are no running costs as a result.

This is only recommended for experienced IT professionals due to the complexity of setting up a local running instance.

For more information, refer to the local installation [documentation](/deployment/local) or reach out to CluedIn support who will be happy to answer any questions.