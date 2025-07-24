---
layout: cluedin
nav_order: 11
parent: Configuration
grand_parent: PaaS operations
permalink: {{ site.baseurl }}/deployment/infra-how-tos/configure-firewall
title: Firewall
tags: ["deployment", "ama", "marketplace", "azure"]
last_modified: 2023-06-23
headerIcon: "paas"
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

Your Azure Firewall should cover the following:

- **Default AKS functionality** – logs and pods should be able to see Kubernetes API Server (as recommended in <a href="https://learn.microsoft.com/en-us/azure/aks/outbound-rules-control-egress">Outbound network and FQDN rules for AKS clusters</a>).
- **CluedIn resource access** – resources needed for the CluedIn installation.
- **CluedIn and custom enrichers** - external web endpoints to enrich your data.

Additionally, if you want to use Power Automate integration for [workflows](/workflow) in CluedIn and/or [Power Apps integration](/microsoft-integration/powerapps), you need to add specific URLs to your Azure Firewall as described [here](#power-apps-and-power-automate)

## AKS and CluedIn resources

Below are the required endpoints for CluedIn to be functional out of the box.

| Rule address | Port | Description |
|--|--|--|
| `cluedinprod.azurecr.io` | 443 | CluedIn container registry |
| `*.blob.core.windows.net` | 443 | storage account endpoint provided by the registry |
| `api.nuget.org` | 443 | NuGet packages |
| `github.com` | 443 | GitHub artifacts |
| `objects.githubusercontent.com` | 443 | GitHub artifacts |
| `billing.cluedin.com` | 443 | CluedIn licensing server |
| `*.grafana.com` | 443 | Grafana chart content |
| `acme-v02.api.letsencrypt.org` | 443 | (Optional) Let's Encrypt service. Only required if not supplying own certificate |
| `quay.io/jetstack` | 443 | (Optional) The cert-manager Let's Encrypt ACME service uses images. Not required if using own certificate |
| `*.file.core.windows.net` | 445 | The Azure File CSI driver mounts some shares via NFS/SMB using this port |
| `pkgs.dev.azure.com` | 443 | download the nuget dlls from cluedin public |
| `*.hcp.<location>.azmk8s.io` | 443 | (For public clusters only) Required for Node <-> API server communication. Replace <location> with the region where your AKS cluster is deployed. Can skip if Private cluster. |
| `mcr.microsoft.com` | 443 | Microsoft container registry |
| `*.data.mcr.microsoft.com` | 443 | MCR storage backed by the Azure content delivery network |
| `management.azure.com	` | 443 | Required for Kubernetes operations against the Azure API. |
| `login.microsoftonline.com` | 443	| Required for Microsoft Entra authentication. |
| `packages.microsoft.com` | 443 | This address is the Microsoft packages repository used for cached apt-get operations. Example packages include Moby, PowerShell, and Azure CLI. |
| `acs-mirror.azureedge.net` | 443 | This address is for the repository required to download and install required binaries like kubenet and Azure CNI. |
| `packages.aks.azure.com` | 443 | This address will be replacing acs-mirror.azureedge.net in the future and will be used to download and install required Kubernetes and Azure CNI binaries. |

## Jumpbox & bastion resources

Below are the required endpoints for Jumpbox/bastion access

| Rule address | Port | Description |
|--|--|--|
| `cluedin-io.github.io` | 443 | Cluedin helm repository |
| `community.chocolatey.org` | 443 | community.chocolatey.org |
| `get.helm.sh` | 443 | Helm binary downloads |
| `chocolatey.org` | 443 | Chocolatey package repository |
| `aka.ms` | 443 | Microsoft redirection service (Azure CLI) |
| `packages.microsoft.com` | 443 | Azure CLI and Kubernetes CLI packages |
| `dl.k8s.io` | 443 | Kubernetes CLI downloads |
| `openssl.org` | 443 | OpenSSL downloads |



## Enricher examples

Below are optional additions to the above and are only required if you use enrichers. Below are two of our common enrichers, but each enricher will have its own endpoint configured. If you require assistance with what endpoint is used for each CluedIn enricher, please reach out to CluedIn support who will be happy to assist.

| Enricher name | Port | Description |
|--|--|--|
| `CompanyHouse` | 443 | Our companies house enricher will call the endpoint `https://api.companieshouse.gov.uk` to validate UK based businesses |
| `GoogleMaps` | 443 | The endpoint `https://maps.googleapis.com/maps/api` is called to query an address for correct address formatting and other metadata |

Because both enrichers call external addresses, this traffic will leave the Kubernetes cluster and will need to be whitelisted if using CluedIn enrichers or developing your own enrichers that require external endpoints.

{: .important }
If the rules have not been added, the installation may fail.

## Power Apps and Power Automate

If you want to use Power Automate integration for [workflows](/workflow) in CluedIn and/or [Power Apps integration](/microsoft-integration/powerapps), you need to add the following rules to your Azure Firewall:

- `https://api.flow.microsoft.com`
- `https://<env-name>.api.crm4.dynamics.com` – for example, `https://org7bfc52cb.api.crm4.dynamics.com`
- `https://<env-name>.crm4.dynamics.com` – for example, `https://org7bfc52cb.crm4.dynamics.com`
- `https://graph.microsoft.com`
- `https://api.powerapps.com`
- `https://*.<region>.logic.azure.com` – for example, `https://prod-251.westeurope.logic.azure.com`

Additionally, you need to add the following domains, which are hosts for incoming requests from Power Automate:

- `https://<name>.consent.azure-apihub.net` – for example, `https://europe002-002.consent.azure-apihub.net`
- `https://*.azure-apihub.net` – for example, `https://europe002-002.consent.azure-apihub.net` and  `https://europe002-002.azure-apihub.net`

Instead of using the domains above, you may choose to whitelist them by [service tags](https://learn.microsoft.com/en-us/azure/virtual-network/service-tags-overview):  

- `AzureConnectors`
- `LogicApps`

There are options to further narrow down by region, for example, `AzureConnectors.NorthEurope`. This would depend on your Power Platform region. For example, if Power Platform is created in the Europe region, it is not clear whether it is North or West Europe, so you would add both regions in Europe:

- `AzureConnectors.NorthEurope`
- `AzureConnectors.WestEurope`
