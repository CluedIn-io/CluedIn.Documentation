---
layout: cluedin
title: Power Apps Integration
parent: Microsoft Integration
permalink: /microsoft-integration/powerapps
nav_order: 010
has_children: true
tags: ["integration", "microsoft", "powerapps", "dataverse", "powerautomate"]
---

Power Apps is a key component of the Power Platform, which is Microsoft's suite of tools designed for low-code development, automation, and data analysis. Power Apps allows you to build custom applications with minimal coding. In Power Apps, you can connect to Dataverse, which provides a unified and simplified data schema that allows you to integrate data from multiple sources into a single store. Dataverse is a scalable data service and app platform that lets you securely store and manage data used by business applications.

Power Apps can be integrated with CluedIn to enable you to **manage your master data directly in the Dataverse platform** and **automatically sync it with CluedIn**.

![dataverse.png](/.attachments/dataverse-49d149dd-e53b-4e19-8b7b-c6ea276ee6e4.png)

Power Apps integration offers the following benefits:

- 2-way synchronization of Dataverse metadata to CluedIn entity types and vocabularies and vice versa:

    - CluedIn stream to export golden records from CluedIn to the Dataverse tables.

    - Data ingestion workflow to push data from Dataverse tables to CluedIn ingestion endpoint.
    
- Auto-mapping of columns, keys, and relationships.

To achieve a **2-way synchronization between Dataverse and CluedIn**, the Power Apps integration also involves **Power Automate workflows**. However, these workflows should not be confused with the approval workflows that are available in the **Workflow** module in CluedIn. We discuss the approval workflows as part of [Power Automate integration](/microsoft-integration/power-automate).

To sync master data between CluedIn and the Dataverse platform, start from the [Power Apps pre-configuration guide](/microsoft-integration/powerapps/pre-configuration-guide).