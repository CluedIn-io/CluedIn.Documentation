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

This article explains how to add the [Brreg](https://www.brreg.no/) enricher. The purpose of this enricher is to provide a wide range of information about Norwegian and foreign businesses operating in Norway (for example, address, registration date, employee count, and so on). More details can be found in [Properties from Brreg enricher](#properties-from-brreg-enricher).

## Add Brreg enricher

The enricher requires at least one of the following attributes for searching the Brreg register:

- **Brreg Code** – if your golden records have Brreg codes, you can enter the corresponding vocabulary key to configure the enricher. As a result, the enricher will use the Brreg code to search the Brreg register.

- **Name**, **Country Code**, and **Website** – if your golden records do not have Brreg codes, you can enter these three attributes to configure the enricher. As a result, the enricher will use the combination of name, country, and website to search the Brreg register. For this method to work, the name must be a valid name—not empty, not numbers, not GUID, not equal to "Microsoft Office User", not email. Additionally, at least one of the following conditions must be met:

    - The name postfix contains one of the following values: **"A/S"**, **"AS"**, **"ASA"**, **"I/S"**, **"IS"**, **"K/S"**, **"KS"**, **"ENK"**, **"ANS"**, **"NUF"**, **"P/S"**, **"PS"**, **"Enkeltpersonforetak"**, **"Ansvarlig Selskap"**, **"Aksjeselskap"**, **"Norskregistrert utenlandsk foretak"**.

    - The name contains at least one of the following values: **" no"**, **"no "**, **"norway"**, **"norge"**, **"norsk"**, **"æ"**, **"ø"**, **"å"**.

    - The country is one of the following: **"no"**, **"NOR"**, **"Norway"**, **"Norge"**.

    - The website is valid and ends with **".no"** (for example: google.no).

**To add the Brreg enricher**

1. On the navigation pane, go to **Preparation** > **Enrich**. Then, select **Add Enricher**.

1. On the **Choose Enricher** tab, select **Brreg**, and then select **Next**.

    ![brreg-enricher-1.png](../../assets/images/preparation/enricher/brreg-enricher-1.png)

1. On the **Configure** tab, provide the following details:

    1. **Accepted Entity Type** – enter the entity type to define which golden records will be enriched.

    1. **Name Vocabulary Key** – enter the vocabulary key that contains the names of companies that will be used for searching the Brreg register.

    1. **Country Code Vocabulary Key** – enter the vocabulary key that contains the country codes of companies that will be used for searching the Brreg register.

    1. **Website Vocabulary Key** – enter the vocabulary key that contains the websites of companies that will be used for searching the Brreg register.

    1. **Brreg Code Vocabulary Key** – enter the vocabulary key that contains the Brreg codes of companies that will be used for searching the Brreg register.

    1. **Skip entity Code Creation (Brreg Code)** – turn on the toggle if you don't want to add new entity codes that come from the source system to the enriched golden records. Otherwise, new entity codes containing Brregs codes will be added to the enriched golden records.

        ![brreg-enricher-4.png](../../assets/images/preparation/enricher/brreg-enricher-4.png)

1. Select **Add**.

    The Brreg enricher is added and has an active status. This means that it will enrich relevant golden records during processing or when you trigger external enrichment.

After the Brreg enricher is added, you can modify its details:

- **Settings** – add a user-friendly display name, select the description for data coming from the enricher, and define the source quality for determining the winning values.

    ![brreg-enricher-2.png](../../assets/images/preparation/enricher/brreg-enricher-2.png)

- **Authentication** – modify the details you provided while configuring the enricher.    

## Properties from Brreg enricher

To quickly find the properties added to golden records from the Brreg enricher, use the integrations filter on the **Properties** page.

![brreg-enricher-3.png](../../assets/images/preparation/enricher/brreg-enricher-3.png)

For a more detailed information about the changes made to a golden record by the Brreg enricher, check the corresponding data part on the **History** page.

![brreg-enricher-5.png](../../assets/images/preparation/enricher/brreg-enricher-5.png)

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