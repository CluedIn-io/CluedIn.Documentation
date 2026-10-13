---
title: Post-installation guide
url: https://documentation.cluedin.net/operate/azure-marketplace/step-4
content_type: how-to
section: Deploy & operate > Azure Marketplace
---

# Post-installation guide

> how-to: Steps to accomplish one task.

At this point, you have a working, secure CluedIn environment. However, the default configuration provided by installation from the Azure Marketplace may not fit your organization's security policy. This guide will help you understand how to configure CluedIn to meet your needs.

![Diagram of customizing CluedIn PaaS in six steps: 1 configure DNS, 2 configure certificates, 3 configure alerts in Azure portal, 4 configure logging, 5 set up SSO in Microsoft Entra ID, 6 set up a backup solution for the AKS cluster](https://documentation.cluedin.net/assets/images/deployment/paas-post-installation-guide.gif)

## Configure custom DNS

> **Important:** If you did not set up CluedIn PaaS with a custom DNS, you may experience issues accessing CluedIn with sslip.io when using public Wi-fi (e.g. hotel, conferences,...). In such situations, if possible, use your mobile internet (3G/4G/5G).

To avoid interruption in the adoption of CluedIn, external DNS names are provided by the [sslip.io](https://sslip.io/) service by default without any upfront configuration. The sslip.io service is a DNS service that returns the IP address when queried with a host name that contains an embedded IP address.

The default DNS configuration ensures security by using the Automated Certificate Management Environment (ACME) protocol to issue SSL Certificates via the HTTP challenge method. For more information about certificates, see [Configure certificates](https://documentation.cluedin.net/operate/configuration/configure-certificates.md).

If you want to set up custom DNS entries, see [Configure DNS](https://documentation.cluedin.net/operate/configuration/configure-dns.md).

## Configure custom SSL certificates

By default, CluedIn installation is secured by using TLS. CluedIn uses the Automated Certificate Management Environment (ACME) protocol and the public Let's Encrypt certificate authority to issue certificates. However, this default configuration might not comply with your organization's security policy. If you want to use a Subject Alternative Name (SAN) or wildcard certificate for you domain, see [Configure certificates](https://documentation.cluedin.net/operate/configuration/configure-certificates.md).

## Configure alerts

By default, CluedIn contains built-in alerts that are sent to our support team. You can configure your own alerts in the Azure portal. For more information about alerts, see [Configure alerts](https://documentation.cluedin.net/operate/configuration/configure-alerts.md).

## Configure logging

CluedIn uses structured logging, and only the console sink is enabled by default. If you want to use another sink, see [Configure logging](https://documentation.cluedin.net/operate/configuration/configure-logging.md).

By default, your CluedIn containers are configured to log at the production level. The production log level allows you to view high-level information about the server and the tasks it is performing. The production log level provides an output with the following log entry types:

- INF – informational messages
- WRN – system warnings
- ERR – system errors
- FTL – fatal system logs

## Set up SSO

CluedIn does not set up SSO directly out of the box. If you want to use SSO, see [Configure SSO](https://documentation.cluedin.net/operate/configuration/configure-sso.md).

## Set up a backup solution

Currently, a backup solution is a post-install step because Microsoft does not support the ability to deploy backup policies within AMA. To set up a backup solution, see [AMA backup and restore](https://documentation.cluedin.net/archive/historical-operations/backup-and-restore-draft).

## Results

At this point, your CluedIn instance is up and running and configured according to your organization's needs.

## Next steps

Review procedures for basic maintenance operations:

- [Connect to CluedIn cluster using Azure Cloud Shell](https://documentation.cluedin.net/operate/configuration/connect-to-cluedin.md)

Up: [Azure Marketplace](https://documentation.cluedin.net/operate/azure-marketplace.md)
