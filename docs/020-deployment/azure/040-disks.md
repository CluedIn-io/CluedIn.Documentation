---
layout: cluedin
nav_order: 40
parent: Azure
grand_parent: Deployment
permalink: /deployment/azure/disks
title: Disks
tags: ["deployment", "kubernetes", "azure", "aks", "disk"]
last_modified: 2021-11-15
---

By default, AKS creates the disks to keep your data, but these disks will be deleted with the AKS cluster if you decide to recreate it. To preserve your data, you must create [Azure Managed disks](https://docs.microsoft.com/en-us/azure/virtual-machines/managed-disks-overview) configure CluedIn instance to use it. We will cover the managed disks configuration in the [Helm](./helm) section. Also, see [Sizing](./aks#sizing) for the recommended disks sizes.