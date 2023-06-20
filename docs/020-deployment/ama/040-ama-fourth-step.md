---
layout: default
nav_order: 4
parent: Azure Marketplace
grand_parent: Deployment
permalink: /deployment/azure-marketplace/step-4
title: 4. Post-installation guide
tags: ["deployment", "ama", "marketplace", "azure"]
last_modified: 2023-06-20
---

At this point, you have a working, secure CluedIn environment. However, the default configuration provided by installation from the Azure Marketplace may not fit your organization's security policy. This guide will help you understand how to configure CluedIn to meet your needs.

![overview-fourth-step.png](../../assets/images/ama/install-guide/overview-fourth-step.png =900x)

# Configure custom DNS

To avoid interruption in the adoption of CluedIn, external DNS names are provided by the sslip.io service by default without any upfront configuration. The sslip.io service is a DNS service that returns the IP address when queried with a host name that contains an embedded IP address.

The default DNS configuration ensures security by using the Automated Certificate Management Environment (ACME) protocol to issue SSL Certificates via the HTTP challenge method. For more information about certificates, see [Transport Layer Security](https://dev.azure.com/CluedIn-io/CluedIn/_wiki/wikis/CluedIn.wiki/1199/TLS-SSL).

If you want to set up custom DNS entries, see [Configure DNS](https://dev.azure.com/CluedIn-io/CluedIn/_wiki/wikis/CluedIn.wiki/1197/DNS).

# Configure custom SSL Certificates

By default, CluedIn installation is secured by using TLS. CluedIn uses the Automated Certificate Management Environment (ACME) protocol and the public Let's Encrypt certificate authority to issue certificates. However, this default configuration might not comply with your organization's security policy. If you want to use a Subject Alternative Name (SAN) or wildcard certificate for you domain, see [Using your own certificates and keys](https://dev.azure.com/CluedIn-io/CluedIn/_wiki/wikis/CluedIn.wiki/1199/TLS-SSL?anchor=using-your-own-certificates-and-keys).

# Set up backup - do not add to the documentation portal

By default, CluedIn does not include a backup solution setup. You must back up your CluedIn instance on your own. Based on our experience, each customer has their own backup strategy. However, we have created a guide on how to use a backup open-source system called Valero. For more information about Velero, see [Configure backup tool](https://dev.azure.com/CluedIn-io/CluedIn/_wiki/wikis/CluedIn.wiki/1201/Back-up).

Soon, we will create a guide on how to use the Azure Kubernetes Service (AKS) backup.

# Configure alerts

By default, CluedIn contains built-in alerts that are sent to our support team. You can configure your own alerts in the Azure portal. For details about alerts, see [Configure alerts](https://dev.azure.com/CluedIn-io/CluedIn/_wiki/wikis/CluedIn.wiki/1205/Alert).

![ama-registerAlert.png](../../assets/images/ama/install-guide/ama-registerAlert.png =650x)

# Configure logging

CluedIn uses structured logging, and only the console sink is enabled by default. If you want to use another sink, see [Logging](https://dev.azure.com/CluedIn-io/CluedIn/_wiki/wikis/CluedIn.wiki/1202/Logs).

By default, your CluedIn containers are configured to log at the production level. The production log level allows you to view high-level information about the server and the tasks it is performing. The production log level provides an output with the following log entry types:

- INF – informational messages
- WRN – system warnings
- ERR – system errors
- FTL – fatal system logs

**Logging format and examples**

By default, CluedIn will provide logs to the console in the following format:
`[#{ThreadId:000} {Timestamp:HH:mm:ss} {Level:u3}][{SourceContext}] {Message:lj}{NewLine}{Exception}`

Example of an information log created by thread 001 at 11:38:
`[#001 11:38:53 INF] Operating System: Unix 5.15.0.58`

Example of development/debug log:
`[#001 10:36:35 DBG] [ComponentHost] : Starting Metrics`

Example of verbose/trace logs:
`[#015 10:42:11 VRB][CluedIn.Core.ExecutionContext] Operation GetByEntityCode (/Organization#CluedIn xxxxx-XXXX-xxxx-xxxx) : 5475`

For more information, see [Logging](https://dev.azure.com/CluedIn-io/CluedIn/_wiki/wikis/CluedIn.wiki/1202/Logs).

# Set up SSO

CluedIn does not set up SSO directly out of the box. If you want to use SSO, see our [SSO guide](https://dev.azure.com/CluedIn-io/CluedIn/_wiki/wikis/CluedIn.wiki/1211/SSO).

# Results

At this point, your CluedIn instance is up and running and configured according to your organization's needs.

# Next steps

Review procedures for basic maintenance operations:

- [Connect to CluedIn cluster using Azure Cloud Shell](https://dev.azure.com/CluedIn-io/CluedIn/_wiki/wikis/CluedIn.wiki/1226/Connect-to-CluedIn-cluster)
- Connect to CluedIn cluster using Lens _(Add link)_
- [Helm with CluedIn](https://dev.azure.com/CluedIn-io/CluedIn/_wiki/wikis/CluedIn.wiki/1220/Helm)

