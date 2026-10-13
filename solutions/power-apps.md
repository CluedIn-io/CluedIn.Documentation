---
title: Power Apps
url: https://documentation.cluedin.net/solutions/power-apps
content_type: landing
section: Solutions & integrations
---

# Power Apps

Power Apps is a key component of the Power Platform, which is Microsoft's suite of tools designed for low-code development, automation, and data analysis. Power Apps allows you to build custom applications with minimal coding. In Power Apps, you can connect to Dataverse, which provides a unified and simplified data schema that allows you to integrate data from multiple sources into a single store. Dataverse is a scalable data service and app platform that lets you securely store and manage data used by business applications.

Power Apps can be integrated with CluedIn to enable you to **manage your master data directly in the Dataverse platform** and **automatically sync it with CluedIn**.

![Diagram: CluedIn business domains, vocabularies and keys are transformed into Dataverse table metadata in the Power Apps environment; a stream syncs golden records to Dataverse; added or updated Dataverse data triggers a Power Automate data ingestion workflow that sends it to a CluedIn ingestion endpoint with auto-mapping](https://documentation.cluedin.net/assets/images/microsoft-integration/power-apps/power-apps-diagram.png)

Power Apps integration offers the following benefits:

- 2-way synchronization of Dataverse metadata to CluedIn business domains and vocabularies and vice versa:

    - CluedIn stream to export golden records from CluedIn to the Dataverse tables.

    - Data ingestion workflow to push data from Dataverse tables to CluedIn ingestion endpoint.

- Auto-mapping of columns, keys, and relationships.

To achieve a **2-way synchronization between Dataverse and CluedIn**, the Power Apps integration also involves **Power Automate workflows**. However, these workflows should not be confused with the approval workflows that are available in the **Workflow** module in CluedIn. We discuss the approval workflows as part of [Power Automate integration](https://documentation.cluedin.net/solutions/power-automate.md).

To sync master data between CluedIn and the Dataverse platform, start from the [Power Apps pre-configuration guide](https://documentation.cluedin.net/solutions/power-apps/pre-configuration-guide.md).

## In this section

- [Power Apps pre-configuration guide](https://documentation.cluedin.net/solutions/power-apps/pre-configuration-guide.md) (how-to): In this guide, you will learn how to prepare for configuring Power Apps integration in CluedIn.
- [Power Apps configuration guide](https://documentation.cluedin.net/solutions/power-apps/configuration-guide.md) (how-to): In this guide, you will learn how to configure Power Apps integration in CluedIn.
- [Power Apps features](https://documentation.cluedin.net/solutions/power-apps/features.md) (concept): This feature allows you to sync CluedIn business domains, vocabularies, and vocabulary keys with Dataverse table and columns.

Up: [Solutions & integrations](https://documentation.cluedin.net/solutions.md)
