---
layout: cluedin
nav_order: 11
parent: How-to guides for PaaS
grand_parent: Installation
permalink: /deployment/infra-how-tos/configure-firewall
title: Configure firewall
tags: ["deployment", "ama", "marketplace", "azure"]
last_modified: 2023-06-23
---

Your Azure Firewall should cover the following:
- **Default AKS functionality** – logs and pods should be able to see Kubernetes API Server (as recommended in <a href="https://learn.microsoft.com/en-us/azure/aks/outbound-rules-control-egress">Outbound network and FQDN rules for AKS clusters</a>).
- **CluedIn resource access** – resources needed for the CluedIn installation.
- **CluedIn and custom enrichers** - external web endpoints to enrich your data

To do that, add the following rules to your Azure Firewall as described in the table.

### AKS and CluedIn resources
Below are the required endpoints for CluedIn to be functional out of the box.

| Rule address | Port | Description |
|--|--|--|
| `cluedinprod.azurecr.io` | 443 | CluedIn container registry |
| `api.nuget.org` | 443 | NuGet packages |
| `github.com` | 443 | GitHub artifacts |
| `objects.githubusercontent.com` | 443 | GitHub artifacts |
| `billing.cluedin.com` | 443 | CluedIn licensing server |
| `*.grafana.com` | 443 | Grafana chart content |
| `mcr.microsoft.com` | 443 | Microsoft container registry |
| `acme-v02.api.letsencrypt.org` | 443 | (Optional) Let's Encrypt service. Only required if not supplying own certificate |

### Enricher Examples
Below are optional additions to the above and are only required if you use enrichers listed below.

| Enricher name | Port | Description |
|--|--|--|
| `CompanyHouse` | 443 | Our companies house enricher will call the endpoint `https://api.companieshouse.gov.uk` to validate UK based businesses |
| `GoogleMaps` | 443 | The endpoint `https://maps.googleapis.com/maps/api` is called to query an address for correct address formatting and other metadata |

Because both call external addresses, this traffic will leave the kubernetes cluster and will need to be whitelisted if using CluedIn enrichers or developing your own enrichers that require external endpoints 

{: .important }
If the rules have not been added, the installation may fail.