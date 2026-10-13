---
title: Master Data Services
url: https://documentation.cluedin.net/solutions/master-data-services
content_type: landing
section: Solutions & integrations
---

# Master Data Services

CluedIn can crawl Microsoft SQL Server Master Data Services (MDS) to bring your master data into CluedIn.

MDS only accepts Windows (NTLM/Negotiate) authentication by default. This does not work reliably from CluedIn's Linux-based crawler containers, so one of the following connection methods is required instead:

- [Direct connection](https://documentation.cluedin.net/solutions/master-data-services/direct-connection.md) - expose a dedicated Basic authentication endpoint on your MDS server, and connect to it directly. Use this if CluedIn has a routable network path to your on-premises MDS server (for example, through a firewall rule or VPN).

- [Azure Relay](https://documentation.cluedin.net/solutions/master-data-services/azure-relay.md) - expose your on-premises MDS server to CluedIn through an Azure Relay WCF Relay. Use this if CluedIn does not have a routable network path to your on-premises MDS server.

MDS can be installed either as its own IIS site, or as an application under an existing site (for example, Default Web Site). The IIS Manager screenshots in these guides show one particular setup as an example - the path shown in the tree will vary depending on how MDS is installed in your environment, but the steps are otherwise the same.

## In this section

- [Direct connection](https://documentation.cluedin.net/solutions/master-data-services/direct-connection.md) (how-to): In this article, you will learn how to connect CluedIn to on-premises Master Data Services (MDS) directly over HTTPS.
- [Azure Relay](https://documentation.cluedin.net/solutions/master-data-services/azure-relay.md) (how-to): In this article, you will learn how to expose on-premises Master Data Services (MDS) to CluedIn in Azure by using Azure Relay.

Up: [Solutions & integrations](https://documentation.cluedin.net/solutions.md)
