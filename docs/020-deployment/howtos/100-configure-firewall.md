---
layout: default
nav_order: 1
parent: How-to guides
grand_parent: Installation
permalink: /deployment/infra-how-tos/configure-firewall
title: Configure firewall
tags: ["deployment", "ama", "marketplace", "azure"]
last_modified: 2023-06-23
---

Your Azure Firewall should cover the following:
- **Default AKS functionality** – logs and pods should be able to see Kubernetes API Server (as recommended in <a href="https://learn.microsoft.com/en-us/azure/aks/outbound-rules-control-egress">Outbound network and FQDN rules for AKS clusters</a>).
- **CluedIn resource access** – resources needed for the CluedIn installation.

To do that, add the following rules to your Azure Firewall as described in the table.

| Rule address | Port | Description |
|--|--|--|
| `cluedinprod.azurecr.io` | 443 | CluedIn container registry |
| `api.nuget.org` | 443 | NuGet packages |
| `github.com` | 433 | GitHub artifacts |
| `billing.cluedin.com` | 443 | CluedIn licensing server |
| `*.grafana.com` | 443 | Grafana chart content |
| `mcr.microsoft.com` | 443 | Microsoft container registry |

**Important!** If the rules have not been added, the installation will fail.