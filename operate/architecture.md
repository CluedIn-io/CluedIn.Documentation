---
title: Architecture overview
url: https://documentation.cluedin.net/operate/architecture
content_type: concept
section: Deploy & operate
---

# Architecture overview

> concept: Explains how something works.

Below is a high-level design of what gets deployed from the Azure Marketplace Application (AMA) wizard and what you can expect after installing the product. 

![Architecture diagram: the AMA resource group holds the Azure Managed Application resource. The managed resource group holds core resources (Key Vault, Log Analytics workspace, ingress public IP, virtual network) and Kubernetes. The node resource group holds a storage account, egress public IP, load balancer, network security group, AKS node pools (Data, DataNeo, DataES, General, Processing, System) and AKS managed disks](https://documentation.cluedin.net/assets/diagrams/cluedin-architecture-hlsd.png)

For a detailed design surrounding the networking, please visit [Advanced network configuration](https://documentation.cluedin.net/operate/configuration/advanced-network.md)

Up: [Deploy & operate](https://documentation.cluedin.net/operate.md)
