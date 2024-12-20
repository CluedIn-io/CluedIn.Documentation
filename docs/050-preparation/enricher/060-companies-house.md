---
layout: cluedin
nav_order: 6
parent: Enricher
grand_parent: Preparation
permalink: /preparation/enricher/companies-house
title: Companies House
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

This article outlines how to configure the [Companies House](https://www.gov.uk/government/organisations/companies-house#:~:text=Companies%20House%20is%20the%20%EE%80%80official%20agency%EE%80%81) enricher. The purpose of this enricher is to get information about companies registered in the UK (for example, address, date of creation, company status, and so on). More details can be found in [Properties from Companies House enricher](#properties-from-companies-house-enricher).

## Add Companies House enricher

To use the Companies House enricher, you must provide the API key. To get it, you need to [register a user account](https://developer.company-information.service.gov.uk/signin) with Companies House.

You can add input parameters for the enricher (organization name, country, and Companies House number). The enricher will use either organization name or Companies House number to retrieve information from the Companies House website. However, this step is optional. If you do not provide any input parameters, the following parameters will be used by default:

- **Organization Name Vocab Key** – organization.name

- **Country Vocab Key** – organization.address.countryCode

- **Companies House Number Vocab Key** - organization.codes.companyHouse

**To add the Companies House enricher**

1. On the navigation pane, go to **Preparation** > **Enrich**. Then, select **Add Enricher**.

1. On the **Choose Enricher** tab, select **Companies House**, and then select **Next**.

    ![comapnies-house-enricher-1.png](../../assets/images/preparation/enricher/comapnies-house-enricher-1.png)

1. On the **Configure** tab, provide the following details:

    - **API Key** – enter the API key for retrieving information from the Companies House website.

    - **Accepted Entity Type** – enter the entity type to define which golden records will be enriched.

    - **Companies House Number Vocab Key** – enter the vocabulary key that contains the Companies House number that will be used for searching the Companies House website.

    - **Country Vocab Key** – enter the vocabulary key that contains the countries of companies that will be used for searching the Companies House website.

    - **Organization Name Vocab Key** – enter the vocabulary key that contains the names of companies that will be used for searching the Companies House website.

    - **Skip Entity Code Creation (Company House Number)** – turn on the toggle if you don't want to add new entity codes that come from the source system to the enriched golden records. Otherwise, new entity codes containing Companies House number will be added to the enriched golden records.

    - **Skip Entity Code Creation (Company Name)** – turn on the toggle if you don't want to add new entity codes that come from the source system to the enriched golden records. Otherwise, new entity codes containing company names will be added to the enriched golden records.

        ![comapnies-house-enricher-2.png](../../assets/images/preparation/enricher/comapnies-house-enricher-2.png)

1. Select **Add**.

    The Companies House enricher is added and has an active status. This means that it will enrich golden records based on the configuration details during processing or when you trigger external enrichment.

After the Companies House enricher is added, you can modify its details:

- **Settings** – add a user-friendly display name, select the description for data coming from the enricher, and define the source quality for determining the winning values.

    ![comapnies-house-enricher-3.png](../../assets/images/preparation/enricher/comapnies-house-enricher-3.png)

- **Authentication** – modify the details you provided while configuring the enricher.

## Properties from Companies House enricher

You can find the properties added to golden records from the Companies House enricher on the **Properties** page.

![comapnies-house-enricher-4.png](../../assets/images/preparation/enricher/comapnies-house-enricher-4.png)

For a more detailed information about the changes made to a golden record by the Companies House enricher, check the corresponding data part on the **History** page.

![comapnies-house-enricher-5.png](../../assets/images/preparation/enricher/comapnies-house-enricher-5.png)

The following table lists the properties that can be added to golden records by the Companies House enricher.

| Display name | Vocabulary key |
|--|--|
| Address Line 1 | companyHouse.organization.address+addressLine1  |
| Address Line 2 | companyHouse.organization.address+addressLine2  |
| Locality | companyHouse.organization.address+locality |
| Post Code | companyHouse.organization.address+postCode |
| Charges | companyHouse.organization.charges |
| Company Number | companyHouse.organization.companyNumber |
| Company Status | companyHouse.organization.companyStatus |
| Date Of Creation | companyHouse.organization.dateOfCreation |
| Has_been_liquidated | companyHouse.organization.has_been_liquidated |
| Has_insolvency_history | companyHouse.organization.has_insolvency_history |
| Jurisdiction | companyHouse.organization.jurisdiction |
| Registered_office_is_in_dispute | companyHouse.organization.registered_office_is_in_dispute |
| Type | companyHouse.organization.type |