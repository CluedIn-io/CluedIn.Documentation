---
layout: cluedin
nav_order: 40
parent: Power Automate Integration
grand_parent: Microsoft Integration
permalink: /microsoft-integration/power-automate/private-network
title: Power Automate private network configuration guide
tags: ["integration", "microsoft", "powerapps", "dataverse"]
last_modified: 2025-06-17
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this guide, you will learn how configure access for power automate within a private instance of CluedIn.

{:.important}
This guide is applicable to only private CluedIn instances.

## Advanced Configuration: Power Automate / Power Apps in a Private Network

To enable **Power Automate** or **Power Apps** to communicate with **CluedIn** from within a private network, external access must be configured through a publicly accessible endpoint.

### Connectivity Requirements

Power Automate must access CluedIn through a **public URL**. The data flow diagram (see below) illustrates how Power Automate routes requests to CluedIn.
To support this setup, the following components are required:
*   **Public DNS**
    
*   **Public IP Address**
    


### CluedIn Server Configuration

The **public DNS** must be defined on the CluedIn server using an environment variable:

    CLUEDIN_APPSETTINGS__PROXY_PUBLICURL = "workflow-{env}.{your-domain}"
    

*   Replace `{env}` with your deployment environment (e.g., `dev`, `prod`)
    
*   Replace `{your-domain}` with your organization’s domain name
    

### Firewall Configuration

Power Automate operates from Microsoft-managed IP ranges, which must be allowed through your network perimeter.
*   [Azure IP Ranges & Service Tags](https://www.microsoft.com/en-us/download/details.aspx?id=56519)

*   [Outbound Firewall rules](https://documentation.cluedin.net/deployment/infra-how-tos/configure-firewall#power-apps-and-power-automate)
    
If you're using **Azure Firewall**, Microsoft provides a **service tag** to simplify rule configuration:
*   Use the service tag: `AzureConnectors` `LogicApps`
    
*   This automatically includes all required outbound IP ranges for Power Automate and related services

![network-with-power-automate.png]({{ "/assets/images/microsoft-integration/power-automate/network-with-power-automate.png" | relative_url }})