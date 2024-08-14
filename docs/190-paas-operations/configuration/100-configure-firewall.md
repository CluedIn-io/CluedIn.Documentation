---
layout: cluedin
nav_order: 11
parent: Configuration
grand_parent: PaaS operations
permalink: /deployment/infra-how-tos/configure-firewall
title: Firewall
tags: ["deployment", "ama", "marketplace", "azure"]
last_modified: 2023-06-23
headerIcon: "paas"
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
| `quay.io/jetstack` | 443 | (Optional) The cert-manager Lets Encrypt ACME service uses images. Not required if using own certificate |
| `AKS Control Plane` | 443 | (For public clusters only) FQDN can be found under the AKS resource next to the **API server address** property (for example, `aks-cluedin.hcp.westeurope.azmk8s.io`) |
| `*.file.core.windows.net` | 445 | The Azure File CSI driver mounts some shares via NFS/SMB using this port. |

### Enricher examples
Below are optional additions to the above and are only required if you use enrichers. Below are two of our common enrichers, but each enricher will have its own endpoint configured. If you require assistance with what endpoint is used for each CluedIn enricher, please reach out to CluedIn support who will be happy to assist.


| Enricher name | Port | Description |
|--|--|--|
| `CompanyHouse` | 443 | Our companies house enricher will call the endpoint `https://api.companieshouse.gov.uk` to validate UK based businesses |
| `GoogleMaps` | 443 | The endpoint `https://maps.googleapis.com/maps/api` is called to query an address for correct address formatting and other metadata |

Because both enrichers call external addresses, this traffic will leave the Kubernetes cluster and will need to be whitelisted if using CluedIn enrichers or developing your own enrichers that require external endpoints.

{: .important }
If the rules have not been added, the installation may fail.