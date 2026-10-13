---
title: Azure deployment
url: https://documentation.cluedin.net/operate/azure
content_type: landing
section: Deploy & operate
---

# Azure deployment

Deploying CluedIn into your own Azure subscription: the cluster, the network, the certificates, the storage, and the Helm release that installs the platform onto them.

## In this section

- [AKS](https://documentation.cluedin.net/operate/azure/aks.md) (how-to): There are several ways to install an AKS cluster: ARM templates, Azure CLI, Terraform - the choice is yours.
- [DNS](https://documentation.cluedin.net/operate/azure/dns.md) (how-to): To access CluedIn via domain name, you need to configure DNS.
- [TLS Certificate](https://documentation.cluedin.net/operate/azure/certificate.md) (how-to): When you have a cluster with a public IP and DNS links your domain name to that cluster, it's about time to think about the security and prepare a TLS-certificate that you that the CluedIn application will use when us...
- [Disks](https://documentation.cluedin.net/operate/azure/disks.md) (how-to): By default, AKS creates the disks to keep your data, but these disks will be deleted with the AKS cluster if you decide to recreate it.
- [Email](https://documentation.cluedin.net/operate/azure/email.md) (how-to): To receive email notifications and send invites to new CluedIn users, you need an email address and credentials (username and password) to the email server.
- [PAT](https://documentation.cluedin.net/operate/azure/pat.md) (how-to): To deploy CluedIn, you need a Personal Access Token (PAT) to access CluedIn NuGet feeds.
- [Helm](https://documentation.cluedin.net/operate/azure/helm.md) (how-to): Helm is the package manager for Kubernetes.
- [CluedIn Setup](https://documentation.cluedin.net/operate/azure/setup.md) (how-to): In order to prepare the setup of CluedIn in Azure, you need to have all required tools ready on your machine.
- [Walkthrough: Install CluedIn on Azure](https://documentation.cluedin.net/operate/azure/walkthrough.md) (tutorial): This installation process is done through command lines using PowerShell 7, Azure CLI, Kubectl and Helm.
- [Install CluedIn using PowerShell](https://documentation.cluedin.net/operate/azure/powershell.md) (how-to): This installation process is done through command lines using PowerShell 7, Azure CLI, Kubectl and Helm.

Up: [Deploy & operate](https://documentation.cluedin.net/operate.md)
