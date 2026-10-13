---
title: Deploy & operate
url: https://documentation.cluedin.net/operate
content_type: landing
---

# Deploy & operate

How do I run the platform?
  Platform and DevOps teams running a CluedIn installation.

Everything a platform team does **to** a CluedIn installation: choosing a deployment model, installing it, configuring the cluster, upgrading it, backing it up, watching it, and keeping its cost and security in order.

Product administration - users, roles, UI configuration - is [Administer](https://documentation.cluedin.net/administer.md).

## In this section

- [Architecture overview](https://documentation.cluedin.net/operate/architecture.md) (concept): Below is a high-level design of what gets deployed from the Azure Marketplace Application (AMA) wizard and what you can expect after installing the product.
- [Queues in CluedIn](https://documentation.cluedin.net/operate/queues-in-cluedin.md) (concept): In this article, you will learn about the queue-based service bus architecture used by CluedIn and find a complete list of queues involved in its operations.
- [Deployment options](https://documentation.cluedin.net/operate/deployment-options.md): CluedIn runs as a managed SaaS service, as a private SaaS or PaaS deployment in your own Azure subscription, or locally for development.
- [Azure deployment](https://documentation.cluedin.net/operate/azure.md): Deploying CluedIn into your own Azure subscription: the cluster, the network, the certificates, the storage, and the Helm release that installs the platform onto them.
- [Azure Marketplace](https://documentation.cluedin.net/operate/azure-marketplace.md): Installing CluedIn from the Azure Marketplace, including the decisions to make and the checks to run before and after the managed application is deployed.
- [Local deployment](https://documentation.cluedin.net/operate/local.md): Running CluedIn on a single machine for development and evaluation, including how to add extension packages and how to upgrade it.
- [Configuration](https://documentation.cluedin.net/operate/configuration.md): Configuring a deployed installation: how you connect to it, how it authenticates people, how it reaches the network, and how it stores and secures its data.
- [External identity providers](https://documentation.cluedin.net/operate/identity-providers.md): CluedIn signs people in through Microsoft Entra, and Entra can federate other identity providers such as Okta, Auth0 or Google Workspace, so people keep using the account they already have.
- [Upgrade](https://documentation.cluedin.net/operate/upgrade.md): How to upgrade a CluedIn installation, and what each release requires.
- [Backup and restore](https://documentation.cluedin.net/operate/backup-and-restore.md): Protecting an installation and getting it back.
- [Monitoring](https://documentation.cluedin.net/operate/monitoring.md): Watching a running installation: the Engine Room shows what the platform is processing right now, and Log Analytics holds the detail when you need to go back through it.
- [Security](https://documentation.cluedin.net/operate/security.md): The security posture of a CluedIn installation, how to restrict access to individual components, and CluedIn's response to publicly disclosed vulnerabilities.
- [Cost and scaling](https://documentation.cluedin.net/operate/cost-and-scaling.md): What drives the cost of a CluedIn installation and what you can safely turn down or off when you do not need it.
- [Day-to-day operations](https://documentation.cluedin.net/operate/operations.md): The recurring operational tasks: promoting configuration between environments, resetting an instance, migrating the database, and knowing what CluedIn support covers.
