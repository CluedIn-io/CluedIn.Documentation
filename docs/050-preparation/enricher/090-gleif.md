---
layout: cluedin
nav_order: 9
parent: Enricher
grand_parent: Preparation
permalink: /preparation/enricher/companies-house
title: Gleif
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

This article explains how to add the Gleif enricher. The purpose of this enricher is to find information about the company using its Legal Entity Identifier (LEI).

## Add Gleif enricher

The Gleif enricher doesn't require specific configuration.

**To add the Gleif enricher**

1. On the navigation pane, go to **Preparation** > **Enrich**. Then, select **Add Enricher**.

1. On the **Choose Enricher** tab, select **Gleif**, and then select **Next**.

    ![gleif-enricher-1.png](../../assets/images/preparation/enricher/gleif-enricher-1.png)

1. On the **Configure** tab, select **Add**.

    The Gleif enricher is added and has an active status. This means that it will enrich relevant golden records during processing or when you trigger external enrichment.

After the Gleif enricher is added, you can modify its settings—add a user-friendly display name, select the description for data coming from the enricher, and define the source quality for determining the winning values.

![gleif-enricher-2.png](../../assets/images/preparation/enricher/gleif-enricher-2.png)

## Properties from Gleif enricher

To quickly find the properties added to golden records from the Gleif enricher, use the integrations filter on the **Properties** page.

![gleif-enricher-3.png](../../assets/images/preparation/enricher/gleif-enricher-3.png)

For a more detailed information about the changes made to a golden record by the Gleif enricher, check the corresponding data part on the **History** page.

![gleif-enricher-4.png](../../assets/images/preparation/enricher/gleif-enricher-4.png)

The following table lists the properties that can be added to golden records by the Gleif enricher.

| Display name | Vocabulary key |
|--|--|
| Entity Category | gleif.organization.entityCategory |
| Entity Status | gleif.organization.entityStatus |
| gleif.organization.legalAddress+address | gleif.organization.legalAddress+address |
| Address | gleif.organization.headquartersAddress+address |
| City | gleif.organization.headquartersAddress+city |
| Country Code | gleif.organization.headquartersAddress+countryCode |
| Postal Code | gleif.organization.headquartersAddress+postalCode |
| Initial Registration Date| gleif.organization.initialRegistrationDate |
| Last Update Date | gleif.organization.lastUpdateDate |
| Legal Form Code | gleif.organization.legalFormCode |
| Legal Jurisdiction | gleif.organization.legalJurisdiction |
| Managing LOU | gleif.organization.managingLOU |
| Next Renewal Date | gleif.organization.nextRenewalDate |
| Other Entity Names | gleif.organization.otherEntityNames |
| Registration Status | gleif.organization.registrationStatus |