---
layout: cluedin
title: Licensing agent (PAAS)
parent: Installation
permalink: /deployment/azure-policy-exemption
nav_order: 7
has_children: false
nav_exclude: true
tags: ["deployment", "licensing-agent", "azure", "microsoft", "marketplace", "azure-marketplace"]
last_modified: 2025-11-20
headerIcon: "paas"
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

# Request for Azure Policy Exemption: Deployment Script Storage Accounts

## Summary

This document explains why an exemption is required for the Azure Policy currently enforcing restrictive network/firewall settings on Storage Accounts. These restrictions prevent Azure Deployment Scripts from functioning correctly, causing deployments to fail with errors related to blocked access or unsupported firewall configurations.

## Background

CluedIn uses deployment scripts when deploying via the azure marketplace. An Azure Deployment Script rely on a temporary Storage Account to store:

- Script logs  
- Output artifacts  
- Execution state  

During deployment, the Deployment Script resource must be able to **read** and **write** to this Storage Account using its **managed identity**.

If an Azure Policy automatically applies restrictive network settings—such as:

- Enforcing *Selected Networks only*
- Blocking public network access
- Disabling “Allow Azure services on the trusted services list to access this storage account”
- Overriding `networkAcls` using `Deny` or `Modify` effects

—then Deployment Scripts cannot access the storage account, resulting in deployment failure.

Microsoft documents this behavior as a known limitation: Deployment Scripts **are not supported** with storage accounts placed behind certain firewall or service endpoint configurations.

## Why the Policy Breaks Deployment Scripts

Customers encounter errors such as:

```

DeploymentScriptStorageAccountWithServiceEndpointEnabled
Storage account <name> has firewall settings enabled which are not supported for deployment scripts.

````

This happens because Deployment Scripts access the storage account using Azure’s backend infrastructure, which requires:

- “Allow Azure services on the trusted services list to access this storage account” enabled  
- Public network access enabled (or a compatible configuration)  
- The storage account *not* being restricted to a private subnet unless explicitly configured for Deployment Scripts  

When a policy denies or rewrites these values, the Deployment Script resource cannot function.

---

## Why an Exemption Is the Correct Approach

Deployment Script storage accounts are:

- **Ephemeral** (created and deleted during deployments)
- **Used only for logs and temporary artifacts**
- **Isolated within deployment resource groups**

Enforcing production-grade firewall restrictions on these accounts:

- Provides **no meaningful security benefit**
- Causes **deployment failures**
- Conflicts with Microsoft’s design for Deployment Script execution

### A scoped exemption:
- Restores deployment reliability  
- Reduces operational friction  
- Maintains strict security for all production storage accounts  
- Aligns with Microsoft best practices  

## Security Considerations

A scoped exemption does **not** weaken the overall security posture because:

* It applies only to deployment-related storage accounts
* These accounts are short-lived and contain no production data
* Access is still governed by Azure RBAC and managed identities
* No customer or sensitive content is stored
* Production storage accounts remain fully governed by existing policies

## Microsoft Guidance (Summary)

Microsoft officially notes that Deployment Scripts:

* Require more permissive network access
* Do not support storage accounts restricted by certain firewall configurations
* May fail if policies enforce unsupported settings
* Should be deployed using storage accounts that allow trusted Azure services

When policies interfere, Microsoft recommends:

> “Use exemption scopes or policy exclusions for storage accounts used by deployment scripts.”

## Request

We request an exemption for the Azure Policy that currently enforces network/firewall restrictions on Storage Accounts used by Deployment Scripts because:

* The policy blocks critical deployment automation
* The restriction is incompatible with Microsoft-supported deployment behavior
* The exemption is low-risk, narrow, and industry-standard
* It preserves the customer’s security posture while enabling reliable deployments
* Ongoing deployments will continue to fail without it

## Simple Example of an Exemption
```
{
  "type": "Microsoft.Authorization/policyExemptions",
  "apiVersion": "2022-07-01-preview",
  "name": "deployment-scripts-storage-exemption",
  "properties": {
    "policyAssignmentId": "/subscriptions/<subscription-id>/providers/Microsoft.Authorization/policyAssignments/<policy-assignment-name>",
    "exemptionCategory": "Mitigated",
    "description": "Exempts deployment script storage account from storage firewall policy so deployment scripts can run.",
    "scope": "/subscriptions/<subscription-id>/resourceGroups/<rg-name>/providers/Microsoft.Storage/storageAccounts/<storage-account-name>"
  }
}
```

## References
[Deployment script templates](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/Deployment-script-template?utm_source=chatgpt.com)

[Alternate - private storage account](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deployment-script-vnet-private-endpoint)


