---
layout: default
title: PowerApps Integration
parent: Microsoft Integration
permalink: /microsoft-integration/powerapps
nav_order: 40
has_children: true
tags: ["integration", "microsoft", "powerapps", "dataverse", "powerautomate"]
---

## Introduction
We are offering you an in-app experience for Power Apps and Power Automate. Now you can build your workflows directly within CluedIn or manage your master data directly in Power Apps.

## Capabilities
### PowerApps
Managing your master data directly in Power Apps (Dataverse) and automatically synchronizing the update with CluedIn via Ingestion Endpoint will make it easier for you to monitor the changes in your data. You can quickly see the changes in your data in CluedIn History.

Keep your Golden Record synced in the Dataverse table.

Synchronize both Dataverse and CluedIn metadata such as Columns/Vocabularies, Relationships/Edges, and so on.

### Power Automate
Utilizing the capability of Power Automate workflow in managing the data and providing an Approval sequence (through email or Teams notification) for any data that has been added or changed either in CluedIn or Dataverse.

## Architecture
The following diagram illustrates how CluedIn interacts with Microsoft Power Platform.
- 2-way synchronization of Dataverse Metadata to CluedIn Entity Types & Vocabularies and vice versa.
- Keeping the Golden Record data in the Dataverse platform.
- Auto-mapping of columns, keys, and relationships.
- Approval workflow (approved through Teams or Outlook) when there's a change in the data in Dataverse table and pushing the data to CluedIn via Ingestion Endpoint
- Approval workflow (approved through Teams or Outlook) during CluedIn Clean or Manual Data Entry Data Processing.

![Microsoft-CluedIn](./powerapps/images/microsoft-cluedin.jpg)