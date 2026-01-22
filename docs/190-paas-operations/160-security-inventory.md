---
layout: cluedin
title: Security Inventory
parent: PaaS operations
permalink: /paas-operations/security-inventory
nav_order: 16
tags: ["kubernetes", "azure", "aks", "microsoft"]
headerIcon: "paas"
---

This document provides an overview of the tokens, certificates, and secrets used within the CluedIn platform. It outlines their purpose, typical expiry, ownership, and renewal responsibilities to ensure clarity around security management and operational ownership.

Purpose of This Document:

- To provide transparency on security-related artifacts used by the platform

- To clearly define ownership and renewal responsibility

- To help customers plan and manage renewals proactively

- To support security and compliance audits

## Inventory Overview

| Type                          | Purpose                                                           | Typical Expiry | Owner / Responsibility | Renewal Process                    |
| ----------------------------- | ----------------------------------------------------------------- | -------------- | ---------------------- | ---------------------------------- |
| **Certificate**               | Internal server-to-server communication                           | ~1 year        | CluedIn                | Automatically rotated              |
| **Certificate**               | Frontend / public-facing TLS certificate                          | ~1 year        | Customer               | Managed by customer                |
| **NuGet PAT Token**           | Access to custom/private NuGet packages                           | ~180 days      | Customer               | Managed by customer                |
| **ACR Token**                 | Pull container images from CluedIn Azure Container Registry (ACR) | ~1 year        | CluedIn                | renewed during deployment |
| **Organisation Admin Secret** | CluedIn administrative account access                             | N/A            | Customer               | Not applicable                     |
| **SSO Client Secret**         | Authentication for Single Sign-On (SSO) integration               | ~1 year        | Customer               | Managed by customer                |
| **Infrastructure Secrets**    | Internal platform secrets (e.g. SQL, RabbitMQ credentials)        | N/A            | CluedIn                | Not applicable                     |


## Key Notes

- Customer-owned items must be monitored and renewed by the customer before expiry to avoid service disruption.

- CluedIn-owned items are either automatically rotated or renewed as part of operational processes.

- Expiry timelines are indicative and may vary depending on customer configuration or security policies.

- For any planned changes or renewals that could impact production, customers are advised to follow agreed change management procedures.

## Support

If you have questions regarding any item listed in this document or require assistance with renewals or configuration, please contact CluedIn Support.