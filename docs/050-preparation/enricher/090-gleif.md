---
layout: cluedin
nav_order: 9
parent: Enricher
grand_parent: Preparation
permalink: /preparation/enricher/gleif
title: Gleif
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

This article explains how to add the [Gleif](https://www.gleif.org/en) enricher. The purpose of this enricher is to provide a wide range of information about an organization (for example, legal name, address, entity status, and so on). More details are provided in [Properties from Gleif enricher](#properties-from-gleif-enricher).

The Gleif enricher supports the following endpoint:

- `https://api.gleif.org/api/v1/lei-records?page[size]=1&page[number]=1&filter[lei]={leicode}`, where `{leicode}` is the LEI code of the company.

## Add Gleif enricher

The enricher uses the Legal Entity Identifier (LEI) code to search for information about companies.

**To add the Gleif enricher**

1. On the navigation pane, go to **Preparation** > **Enrich**. Then, select **Add Enricher**.

1. On the **Choose Enricher** tab, select **Gleif**, and then select **Next**.

    ![gleif-enricher-1.png](../../assets/images/preparation/enricher/gleif-enricher-1.png)

1. On the **Configure** tab, provide the following details:

    - **Accepted Entity Type** – enter the entity type to define which golden records will be enriched.

    - **Lei Code Vocabulary Key** – enter the vocabulary key that contains LEI codes of companies that you want to enrich.

    - **Skip Entity Code Creation (Lei Code)** – turn on the toggle if you don't want to add new entity codes that come from the source system to the enriched golden records. Otherwise, new entity codes containing LEI codes will be added to the enriched golden records.

        ![gleif-enricher-5.png](../../assets/images/preparation/enricher/gleif-enricher-5.png)

1. Select **Add**.

    The Gleif enricher is added and has an active status. This means that it will enrich relevant golden records during processing or when you trigger external enrichment.

After the Gleif enricher is added, you can modify its details:

- **Settings** – add a user-friendly display name, select the description for data coming from the enricher, and define the source quality for determining the winning values.

    ![gleif-enricher-2.png](../../assets/images/preparation/enricher/gleif-enricher-2.png)

- **Authentication** – modify the details you provided while configuring the enricher.    

## Properties from Gleif enricher

To quickly find the properties added to golden records from the Gleif enricher, use the integrations filter on the **Properties** page.

![gleif-enricher-3.png](../../assets/images/preparation/enricher/gleif-enricher-3.png)

For a more detailed information about the changes made to a golden record by the Gleif enricher, check the corresponding data part on the **History** page.

![gleif-enricher-4.png](../../assets/images/preparation/enricher/gleif-enricher-4.png)

The following table lists the properties that can be added to golden records by the Gleif enricher.

| Display name | Vocabulary key |
|--|--|
| Lei Code | gleif.organization.leiCode |
| Legal Name | gleif.organization.legalName |
| Address | gleif.organization.legalAddress+address |
| Number | gleif.organization.legalAddress+number |
| Number Within Building | gleif.organization.legalAddress+numberWithinBuilding |
| Mail Routing | gleif.organization.legalAddress+mailRouting |
| Additional Address | gleif.organization.legalAddress+additionalAddress |
| Region | gleif.organization.legalAddress+region |
| City | gleif.organization.legalAddress+city |
| Postal Code | gleif.organization.legalAddress+postalCode |
| Country Code | gleif.organization.legalAddress+countryCode |
| Legal Jurisdiction | gleif.organization.legalJurisdiction |
| Legal Form Code | gleif.organization.legalFormCode |
| Legal Form Type | gleif.organization.legalFormType |
| Address | gleif.organization.headquartersAddress+address |
| Number | gleif.organization.headquartersAddress+number |
| Number Within Building | gleif.organization.headquartersAddress+numberWithinBuilding |
| Mail Routing | gleif.organization.headquartersAddress+mailRouting |
| Additional Address | gleif.organization.headquartersAddress+additionalAddress |
| Region | gleif.organization.headquartersAddress+region |
| City | gleif.organization.headquartersAddress+city |
| Postal Code | gleif.organization.headquartersAddress+postalCode |
| Country Code | gleif.organization.headquartersAddress+countryCode |
| Other Entity Names | gleif.organization.otherEntityNames |
| Entity Status | gleif.organization.entityStatus |
| Initial Registration Date| gleif.organization.initialRegistrationDate |
| Last Update Date | gleif.organization.lastUpdateDate |
| Registration Status | gleif.organization.registrationStatus |
| Next Renewal Date | gleif.organization.nextRenewalDate |
| Managing LOU | gleif.organization.managingLOU |
| Entity Category | gleif.organization.entityCategory |