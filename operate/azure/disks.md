---
title: Disks
url: https://documentation.cluedin.net/operate/azure/disks
content_type: how-to
section: Deploy & operate > Azure deployment
---

# Disks

> how-to: Steps to accomplish one task.

By default, AKS creates the disks to keep your data, but these disks will be deleted with the AKS cluster if you decide to recreate it. To preserve your data, you must create [Azure Managed disks](https://docs.microsoft.com/en-us/azure/virtual-machines/managed-disks-overview) configure CluedIn instance to use it. We will cover the managed disks configuration in the [Helm](https://documentation.cluedin.net/operate/azure/helm.md) section. Also, see [Sizing](https://documentation.cluedin.net/operate/azure/aks.md#sizing) for the recommended disks sizes.

Up: [Azure deployment](https://documentation.cluedin.net/operate/azure.md)
