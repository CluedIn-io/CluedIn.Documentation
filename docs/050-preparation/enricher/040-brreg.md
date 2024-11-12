---
layout: cluedin
nav_order: 4
parent: Enricher
grand_parent: Preparation
permalink: /preparation/enricher/brreg
title: Brreg
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

This article explains how to add the [Brreg](https://www.brreg.no/) enricher. The purpose of this enricher is to provide a wide range of information about Norwegian and foreign businesses operating in Norway (for example, address, registration date, employee count, and so on). More details can be found in [Properties from Brreg enricher](#poperties-from-brreg-enricher).

## Add Brreg enricher

The Brreg enricher doesn't require specific configuration. However, it only affects golden records that meet the following criteria:

- Golden records belong to the **Organization** entity type.

- Golden records contain the **organization.codes.brreg** vocabulary key. This is the most important requirement because the enricher uses the code to extract additional information.

**To add the Brreg enricher**

1. On the navigation pane, go to **Preparation** > **Enrich**. Then, select **Add Enricher**.

1. On the **Choose Enricher** tab, select **Brreg**, and then select **Next**.

    ![brreg-enricher-1.png](../../assets/images/preparation/enricher/brreg-enricher-1.png)

1. On the **Configure** tab, select **Add**.

    The Brreg enricher is added and has an active status. This means that it will enrich relevant golden records during processing or when you trigger external enrichment.

After the Brreg enricher is added, you can modify its settings—add a user-friendly display name, select the description for data coming from the enricher, and define the source quality for determining the winning values.

![brreg-enricher-2.png](../../assets/images/preparation/enricher/brreg-enricher-2.png)

## Properties from Brreg enricher

To quickly find the properties added to golden records from the Brreg enricher, use the integrations filter on the **Properties** page.

![brreg-enricher-3.png](../../assets/images/preparation/enricher/brreg-enricher-3.png)

For a more detailed information about the changes made to a golden record by the Brreg enricher, check the corresponding data part on the **History** page.

The following table lists the properties that can be added to golden records by the Brreg enricher.

| Display name | Vocabulary key |
|--|--|
| Bankrupt | brreg.organization.bankrupt |
| Brreg Url | brreg.organization.brregUrl |
| Country | brreg.organization.businessPostAddress+country |
| Municipality | brreg.organization.businessPostAddress+municipality |
| Municipality Number | brreg.organization.businessPostAddress+municipalityNumber |
| Industry Code | brreg.organization.industryCode |
| Institution Sector Code | brreg.organization.institutionSectorCode |
| Institution Sector Description | brreg.organization.institutionSectorDescription |
| Language Variant | brreg.organization.languageVariant |
| Latest Filed Annual Accounts | brreg.organization.latestFiledAnnualAccounts |
| Organization Type | brreg.organization.organizationTyp |
| Address | brreg.organization.postAddress+address |
| Country | brreg.organization.postAddress+country |
| Country Code | brreg.organization.postAddress+countryCode |
| Municipality | brreg.organization.postAddress+municipality |
| Municipality Number | brreg.organization.postAddress+municipalityNumber |
| Postal Area | brreg.organization.postAddress+postalArea |
| Postal Code | brreg.organization.postAddress+postalCode |
| Registered Business Register | brreg.organization.registeredBusinessRegister |
| Registered Founding Register | brreg.organization.registeredFoundingRegister |
| Registered Im Goods Register | brreg.organization.registeredImGoodsRegister |
| Registration Date | brreg.organization.registrationDate |
| Under Liquidation | brreg.organization.underLiquidation |
| Under Liquidation Or Dissolution | brreg.organization.underLiquidationOrDissolution |
| Voluntary Registered | brreg.organization.voluntaryRegistered |
| Address | organization.address |
| Address Country Code | organization.address.countryCode |
| Address Postal Area | organization.address.postalArea |
| Address Zip Code | organization.address.zipCode |
| Codes Brreg | organization.codes.brreg |
| Employee Count | organization.employeeCount |
| Industry | organization.industry |
| Website | organization.website |