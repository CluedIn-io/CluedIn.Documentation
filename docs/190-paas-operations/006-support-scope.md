---
layout: cluedin
title: Support scope
parent: PaaS operations
permalink: {{ site.baseurl }}/paas-operations/support-scope
nav_order: 6
tags: ["kubernetes", "azure", "aks", "microsoft", "marketplace", "azure-marketplace", "cost", "reduction", "reducing"]
headerIcon: "paas"
---

This article outlines the scope of CluedIn support. The goal of this article is to answer the question of what happens if you change the default configuration installed using the Azure Marketplace offering.

Any modifications made to the default configuration, except those explicitly documented as [post-installation adjustments](/deployment/azure-marketplace/step-4), will result in the termination of support. This includes Premium Support, Azure Managed Application, and any other customer support service. The reason for this is the high probability that the cluster may not operate correctly. Changes outside the documented scope are considered out of support, and CluedIn will not provide assistance or troubleshooting for configurations that deviate from the originally installed setup.

Here is a list of allowed changes:

- Adjusting requests and limits on CluedIn operating pods for both CPU and memory.

- Setting up and receiving assistance with the CluedIn backup solution.

- Configuring single sign-on (SSO).

- Setting up SMTP details for welcome emails.

- Configuring extended alerts via CluedIn. This is related to CluedIn-specific alerts only, not customer-specific alerts.

- Troubleshooting ad-hoc cluster failures, if determined not to be caused by the customer.

- Upgrading environments.

- Installing the product using our default configuration.

- Usage of Azure Key Vault to provide secrets to the cluster.

- General AKS maintenance on the default configuration.

{:.important}
Any deviation from this list will be considered out of support, and assistance for the issue is not guaranteed and may incur charges.