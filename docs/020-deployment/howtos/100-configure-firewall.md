---
layout: default
nav_order: 1
parent: How tos
grand_parent: Installation
permalink: /deployment/infra-how-tos/configure-firewall
title: Configure firewall
tags: ["deployment", "ama", "marketplace", "azure"]
last_modified: 2023-06-23
---

Before installing CluedIn, you need to set up the firewall policy. To do that, add the following rules to your Azure Firewall as described in the table.

| Rule address | Port | Description |
|--|--|--|
| `cluedinprod.azurecr.io` | 443 | CluedIn container registry |
| `api.nuget.org` | 443 | NuGet packages |
| `github.com` | 433 | GitHub artifacts |
| `billing.cluedin.com` | 443 | CluedIn licensing server |
| `*.grafana.com` | 443 | Grafana chart content |
| `mcr.microsoft.com` | 443 | Microsoft container registry |

**Important!** If the rules have not been added, then the installation will fail.