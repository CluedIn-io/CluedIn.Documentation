---
layout: cluedin
nav_order: 13
parent: How-to guides for PaaS
grand_parent: Installation
permalink: /deployment/infra-how-tos/aks-upgrade
title: AKS upgrade
tags: ["deployment", "ama", "marketplace", "azure", "aks", "kubernetes", "upgrade"]
last_modified: 2024-03-27
---
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

In this article, you will learn how to upgrade your Azure Kubernetes Service (AKS) to a supported version.
This is included as part of the AMA agreement with us, however, there may be times where CluedIn are unable to facilitate this upgrade for you due to missing levels of permission. 

**Important!** Before starting the AKS upgrade, make sure that you have followed all pre-requisites.

## Pre-requisites
When doing a Kubernetes upgrade, nodes will `surge` to try minimise downtime of the application. This means that additional Nodes in the `Node Pool` will be spun up at upgrade time and may cause issues if preparation isn't done beforehand.

- Quota
    Each node will eventually spin up a new replica of the same SKU. It's important to make sure you have additional allocated quota so that these nodes can be spun up without any problems

- IP address allocation
    If your environment is using `Azure CNI without Dynamic Allocation` your nodes will reserve IP addresses for each potential pod. By default, this is between 30-50 pods per node. As a result, this will mean that each node will use the same amount of IP addresses and may mean when additional nodes are spun up during surge, there's not enough available space to allocate.

    Please see if there's enough space before going ahead.

If you do not meet the pre-requisites, please scroll down to the [here]() to follow the steps to get around this.

## Documentation

- Confirm pre-requisites
- Scale down
- API bypass (if necessary)
- Perform upgrade
- Scale up
- Validate working
