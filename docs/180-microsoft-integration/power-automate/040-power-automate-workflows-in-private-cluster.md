---
layout: cluedin
nav_order: 40
parent: Power Automate Integration
grand_parent: Microsoft Integration
permalink: /microsoft-integration/power-automate/power-automate-private-cluster
title: Power Automate implementation in a private cluster
tags: ["integration", "microsoft", "powerapps", "dataverse"]
last_modified: 2025-03-27
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

This article explains the implementation of Power Automate workflows within a zero-trust architecture for the CluedIn application hosted in a private Azure Kubernetes cluster.

## Prerequisites

In order to use Power Automate workflows in a zero-trust corporate environment, make sure you fulfill the following prerequisites:

- **Firewall Application rule FQDN** – `api.flow.microsoft.com`, `*.api.crm4.dynamics.com`, `*.crm4.dynamics.com`, `graph.microsoft.com`, `api.powerapps.com`, `*.logic.azure.com`

- **Firewall Network rule** – tag `Appservice.<region>`

- Delegated subnet (Microsoft.App/environments) for Azure function with /26 IP range on your existing Vnet or a new one ( a new Vnet needs to be peered with AKS subnet).

## Overview

The solution ensures that incoming requests are securely proxied through an Azure Function and only accessible within a restricted IP range. This setup integrates Power Automate workflows using an Azure Logic Apps custom connector.

**Network diagram**

![power-automate-network-diagram.png](../../assets/images/microsoft-integration/power-automate/power-automate-network-diagram.png)

**Sequence diagram**

![power-automate-sequence-diagram.png](../../assets/images/microsoft-integration/power-automate/power-automate-sequence-diagram.png)

**Request flow**

1.  Power Automate invokes Logic Apps Custom Connector.
1.  Logic Apps Custom Connector sends the request to the Azure Function Proxy.
1.  Azure Function forwards the request to the CluedIn API.
1.  CluedIn processes the request and returns a response.
1.  Azure Function passes the response back to Power Automate.

**Assumptions**

- Azure Function does not need to handle any additional authentication or processing.
- There are no security policies that prevent the Azure Function from being installed.
- There are no security policies that prevent HTTP traffic to and from the Azure Function.

## Steps

1. Create the Azure Function app in the same virtual network as CluedIn.

1. Upload the code ([GitHub](https://github.com/CluedIn-io/CluedIn.AzureFunctionProxy)). To get access, contact our support at [support@cluedin.com](mailto:support@cluedin.com).

1. Under **Networking** > **Public network access**, restrict IP address to Service Group - Azure Connectors.

    The following screenshot shows the **Access Restrictions** page in the Azure portal with the list of access restriction rules defined for the selected app.

    ![access-restrictions-browse.png](../../assets/images/microsoft-integration/power-automate/access-restrictions-browse.png)

1. Set unmatched rule action to **Deny**.

1. Add a rule to restrict traffic from **Azure Connectors**.

## Components

**Azure Function App**

- Acts as a proxy, forwarding requests to CluedIn.
- Passes headers and content without modification.
- Anonymous authentication mode.
- Azure Function is configured with an IP restriction to allow only **Azure Connectors** using service tags.
- Example for a Power Platform environment in Europe region:
  - `AzureConnectors.NorthEurope`
  - `AzureConnectors.WestEurope`
  - `LogicApps.NorthEurope`
  - `LogicApps.WestEurope`

**Power Automate Custom Connector**

- Custom connector is configured to send requests to the Azure Function Proxy.    
- Uses the Azure Function as the host endpoint.    
- Power Automate triggers:
  - Calls CluedIn when a workflow is enabled or disabled.
  - Sends approval responses to CluedIn.
- APIs called by Power Automate:
  - **Enable Workflow:** `POST /api/enterpriseFlows/webhook`
  - **Disable Workflow:** `DELETE /api/enterpriseFlows/webhook`      
  - **Approval Response:** `POST /api/enterpriseFlows/callback`

## References

- [Restrict public access](https://learn.microsoft.com/en-us/azure/app-service/app-service-ip-restrictions?tabs=azurecli#set-a-service-tag-based-rule)
- [Restrict by service tag](https://learn.microsoft.com/en-us/azure/app-service/app-service-ip-restrictions?tabs=azurecli#set-a-service-tag-based-rule)
- [Service tags](https://learn.microsoft.com/en-us/azure/app-service/app-service-ip-restrictions?tabs=azurecli#set-a-service-tag-based-rule)