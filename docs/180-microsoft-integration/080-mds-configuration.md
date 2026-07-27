---
layout: cluedin
title: Master Data Services (MDS) Integration
parent: Microsoft Integration
permalink: /microsoft-integration/mds-integration
nav_order: 080
has_children: true
---

CluedIn can crawl Microsoft SQL Server Master Data Services (MDS) to bring your master data into CluedIn.

MDS only accepts Windows (NTLM/Negotiate) authentication by default. This does not work reliably from CluedIn's Linux-based crawler containers, so one of the following connection methods is required instead:

- [Direct connection](/microsoft-integration/mds-integration/direct-connection) - expose a dedicated Basic authentication endpoint on your MDS server, and connect to it directly. Use this if CluedIn has a routable network path to your on-premises MDS server (for example, through a firewall rule or VPN).

- [Azure Relay](/microsoft-integration/mds-integration/azure-relay) - expose your on-premises MDS server to CluedIn through an Azure Relay WCF Relay. Use this if CluedIn does not have a routable network path to your on-premises MDS server.

MDS can be installed either as its own IIS site, or as an application under an existing site (for example, Default Web Site). The IIS Manager screenshots in these guides show one particular setup as an example - the path shown in the tree will vary depending on how MDS is installed in your environment, but the steps are otherwise the same.
