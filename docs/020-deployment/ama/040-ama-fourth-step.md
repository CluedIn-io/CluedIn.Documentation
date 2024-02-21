---
layout: cluedin
nav_order: 4
parent: Azure Marketplace
grand_parent: Installation
permalink: /deployment/azure-marketplace/step-4
title: Post-installation guide
tags: ["deployment", "ama", "marketplace", "azure"]
last_modified: 2023-06-20
---
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

At this point, you have a working, secure CluedIn environment. However, the default configuration provided by installation from the Azure Marketplace may not fit your organization's security policy. This guide will help you understand how to configure CluedIn to meet your needs.

![overview-fourth-step.png](../../assets/images/ama/install-guide/overview-fourth-step.png)

## Configure custom DNS

To avoid interruption in the adoption of CluedIn, external DNS names are provided by the <a href="https://sslip.io/">sslip.io</a> service by default without any upfront configuration. The sslip.io service is a DNS service that returns the IP address when queried with a host name that contains an embedded IP address.

The default DNS configuration ensures security by using the Automated Certificate Management Environment (ACME) protocol to issue SSL Certificates via the HTTP challenge method. For more information about certificates, see [Configure certificates](/deployment/infra-how-tos/configure-certificates).

If you want to set up custom DNS entries, see [Configure DNS](/deployment/infra-how-tos/configure-dns).

## Configure custom SSL certificates

By default, CluedIn installation is secured by using TLS. CluedIn uses the Automated Certificate Management Environment (ACME) protocol and the public Let's Encrypt certificate authority to issue certificates. However, this default configuration might not comply with your organization's security policy. If you want to use a Subject Alternative Name (SAN) or wildcard certificate for you domain, see [Configure certificates](/deployment/infra-how-tos/configure-certificates).

## Configure alerts

By default, CluedIn contains built-in alerts that are sent to our support team. You can configure your own alerts in the Azure portal. For more information about alerts, see [Configure alerts](/deployment/infra-how-tos/configure-alerts).

## Configure logging

CluedIn uses structured logging, and only the console sink is enabled by default. If you want to use another sink, see [Configure logging](/deployment/infra-how-tos/configure-logging).

By default, your CluedIn containers are configured to log at the production level. The production log level allows you to view high-level information about the server and the tasks it is performing. The production log level provides an output with the following log entry types:

- INF – informational messages
- WRN – system warnings
- ERR – system errors
- FTL – fatal system logs

## Set up SSO

CluedIn does not set up SSO directly out of the box. If you want to use SSO, see [Configure SSO](/deployment/infra-how-tos/configure-sso).

## Set up a backup solution

Currently, a backup solution is a post-install step because Microsoft does not support the ability to deploy backup policies within AMA. To set up a backup solution, see [AMA backup and restore](/deployment/infra-how-tos/ama-backup).

## Results

At this point, your CluedIn instance is up and running and configured according to your organization's needs.

## Next steps

Review procedures for basic maintenance operations:

- [Connect to CluedIn cluster using Azure Cloud Shell](/deployment/infra-how-tos/connect-to-cluedin)
