---
layout: cluedin
title: Architecture overview
parent: Deploy & operate
nav_order: 10
permalink: /operate/architecture
content_type: concept
redirect_from: ["/deployment/architecture", "/development/adding-datastore-provider", "/development/datastores", "/development/switching-datastore-provider"]
source_path: docs/190-paas-operations/001-architecture.md
tags: ["deployment", "ama", "marketplace", "azure", "architecture"]
last_modified: 2023-11-08
headerIcon: "paas"
---

Below is a high-level design of what gets deployed from the Azure Marketplace Application (AMA) wizard and what you can expect after installing the product. 

![Architecture diagram: the AMA resource group holds the Azure Managed Application resource. The managed resource group holds core resources (Key Vault, Log Analytics workspace, ingress public IP, virtual network) and Kubernetes. The node resource group holds a storage account, egress public IP, load balancer, network security group, AKS node pools (Data, DataNeo, DataES, General, Processing, System) and AKS managed disks]({{ "/assets/diagrams/cluedin-architecture-hlsd.png" | relative_url }})

For a detailed design surrounding the networking, please visit [Advanced network configuration](/operate/configuration/advanced-network)