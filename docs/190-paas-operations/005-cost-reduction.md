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

CluedIn runs on Azure Kubernetes Service (AKS) which uses node pools as the underlying resources. As part of the deployment, many Azure resources will be created in your environment each with their own costs associated with it.

The purpose of this guide is to help explain what you can do to reduce the cost of CluedIn in your environment whilst maintaining a supported setup.

# Shutdown environments in times of low or no usage

CluedIn is a product that is intended to run when data is ingested. As a business, this may be during certain hours of the day (e.g. 0900-1700) which means that outside of these hours, the environment(s) will be running and not being used.

One easy way to reduce cost is to shut down your AKS during this hours, and starting the environment back up when it's needed.

The CluedIn team can help set this up in your environment by deploying an Automation Account along with a runbook and setting the schedule to your desired times of inoperation. 