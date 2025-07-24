---
layout: cluedin
nav_order: 15
parent: Enricher
grand_parent: Preparation
permalink: preparation/enricher/perm-id
title: PermID
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

This article outlines how to configure the [PermID](https://permid.org/) enricher. The purpose of this enricher is to provide a wide range of information about an organization (for example, Legal Entity Identifier (LEI), headquarters location, industry classification, and so on). More details are provided in [Properties from PermID enricher](#properties-from-permid-enricher).

The PermID enricher supports the following endpoints:

- `https://api-eit.refinitiv.com/permid` – this API is called first.

- `https://permid.org/api/mdaas/getEntityById/` – this API is called second to get the social data.

## Add PermID enricher

To use the PermID enricher, you must provide the API key. To get the API key, register an account with [PermID.org](https://permid.org/). The enricher uses the organization name to retrieve information from the PermID database.

**To add the PermID enricher**

1. On the navigation pane, go to **Preparation** > **Enrich**. Then, select **Add Enricher**.

1. On the **Choose Enricher** tab, select **PermID**, and then select **Next**.

    ![permid-enricher-1.png](../../assets/images/preparation/enricher/permid-enricher-1.png)

1. On the **Configure** tab, provide the following details:

    - **API Key** – enter the API token for accessing the PermID database.

    - **Accepted Business Domain** – enter the business domain to define which golden records will be enriched using the PermID enricher.

    - **Organization Name Vocabulary Key** – enter the vocabulary key that contains the names of organizations that will be used for retrieving information from the PermID database.

        ![permid-enricher-2.png](../../assets/images/preparation/enricher/permid-enricher-2.png)

1. Select **Test Connection** to make sure the enricher is properly configured, and then select **Add**.

    The PermID enricher is added and has an active status. This means that it will enrich golden records based on the configuration details during processing or when you trigger external enrichment.

After the PermID enricher is added, you can modify its details:

- **Settings** – add a user-friendly display name, select the description for data coming from the enricher, and define the source quality for determining the winning values.

- **Authentication** – modify the details you provided while configuring the enricher.

## Properties from PermID enricher

You can find the properties added to golden records from the OpenCorporates enricher on the **Properties** page.

![permid-enricher-4.png](../../assets/images/preparation/enricher/permid-enricher-4.png)

For a more detailed information about the changes made to a golden record by the PermID enricher, check the corresponding data part on the **History** page.

![permid-enricher-5.png](../../assets/images/preparation/enricher/permid-enricher-5.png)

The following table lists the properties that can be added to golden records by the PermID enricher.

| Display name | Vocabulary key |
|--|--|
| Domiciled In | permId.organization.domiciledIn |
| Entity Type | permId.organization.entityType |
| Incorporated In | permId.organization.incorporatedIn |
| Latest Date Of Incorporation | permId.organization.latestDateOfIncorporation |
| Lei | permId.organization.lei |
| Organization Name | permId.organization.organizationName |
| Public | permId.organization.public |
| Status | permId.organization.status |
| Website | permId.organization.website, mapped to organization.website |
| Hq Address | permId.organization.hqAddress |
| Hq Fax | permId.organization.hqFax |
| Hq Phone | permId.organization.hqPhone |
| Registered Address | permId.organization.registeredAddress |
| Registered Fax | permId.organization.registeredFax |
| Registered Phone | permId.organization.registeredPhone |
| Main Quote Exchange | permId.organization.mainQuote.exchange |
| Main Quote Id | permId.organization.mainQuote.id |
| Main Quote Mic | permId.organization.mainQuote.mic |
| Main Quote Ric | permId.organization.mainQuote.ric |
| Main Quote Ticker | permId.organization.mainQuote.ticker |
| Main Quote Url | permId.organization.mainQuote.url |
| Primary Business Sector | permId.organization.primaryBusinessSector |
| Primary Business Sector Id | permId.organization.primaryBusinessSectorId |
| Primary Economic Sector | permId.organization.primaryEconomicSector |
| Primary Economic Sector Id | permId.organization.primaryEconomicSectorId |
| Primary Industry | permId.organization.primaryIndustry |
| Primary Industry Id | permId.organization.primaryIndustryId |
| Primary Instrument Id | permId.organization.primaryInstrument.id |
| Primary Instrument Name | permId.organization.primaryInstrument.name |
| Primary Instrument Type | permId.organization.primaryInstrument.type |
| Primary Instrument Type Url | permId.organization.primaryInstrument.typeUrl |
| Primary Instrument Url | permId.organization.primaryInstrument.url |