---
layout: cluedin
nav_order: 16
parent: Enricher
grand_parent: Preparation
permalink: /preparation/enricher/vatlayer
title: Vatlayer
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

This article outlines how to configure the [Vatlayer](https://vatlayer.com/) enricher. The purpose of this enricher is to validate EU VAT numbers and retrieve company information (for example, address, CVR number, full VAT, and so on). More details can be found in [Properties from Vatlayer enricher](#properties-from-vatlayer-enricher).

## Add Vatlayer enricher

To use the Vatlayer enricher, you will need to provide the API key. To get it, sign up for an account on the [Vatlayer website](https://vatlayer.com/). The enricher uses the VAT number to retrieve VAT-related information.

**To add the Vatlayer enricher**

1. On the navigation pane, go to **Preparation** > **Enrich**. Then, select **Add Enricher**.

1. On the **Choose Enricher** tab, select **Vatlayer**, and then select **Next**.

    ![vatlayer-enricher-1.png](../../assets/images/preparation/enricher/vatlayer-enricher-1.png)

1. On the **Configure** tab, provide the following details:

    - **API Key** – enter the API key for retrieving information from the Vatlayer website.

    - **Accepted Entity Type** – enter the entity type to define which golden records will be enriched using the Vatlayer enricher.

    - **Accepted Vocab Key** – enter the vocabulary key that contains the VAT numbers of companies that you want to enrich.

        ![vatlayer-enricher-2.png](../../assets/images/preparation/enricher/vatlayer-enricher-2.png)

1. Select **Add**.

    The Vatlayer enricher is added and has an active status. This means that it will enrich golden records based on the configuration details during processing or when you trigger external enrichment.

After the Vatlayer enricher is added, you can modify its details:

- **Settings** – add a user-friendly display name, select the description for data coming from the enricher, and define the source quality for determining the winning values.

    ![vatlayer-enricher-3.png](../../assets/images/preparation/enricher/vatlayer-enricher-3.png)

- **Authentication** – modify the details you provided to configure the enricher: **API Key**, **Accepted Entity Type**, and **Accepted Vocab Key**.

## Properties from Vatlayer enricher

You can find the properties added to golden records from the Vatlayer enricher on the **Properties** page.

![vatlayer-enricher-4.png](../../assets/images/preparation/enricher/vatlayer-enricher-4.png)

For a more detailed information about the changes made to a golden record by the Vatlayer enricher, check the corresponding data part on the **History** page.

![vatlayer-enricher-5.png](../../assets/images/preparation/enricher/vatlayer-enricher-5.png)

The following table lists the properties that can be added to golden records by the Vatlayer enricher.

| Display name | Vocabulary key |
|--|--|
| Address | vatLayer.organization.address |
| Country Code | vatLayer.organization.countryCode |
| Cvr Number | vatLayer.organization.cvrNumber |
| Full Vat | vatLayer.organization.fullVat |
| Name | vatLayer.organization.name |