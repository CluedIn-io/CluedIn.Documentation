---
layout: cluedin
nav_order: 13
parent: Enricher
grand_parent: Preparation
permalink: /preparation/enricher/libpostal
title: Libpostal
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

This article outlines how to configure the Libpostal enricher. The purpose of this enricher is to parse and normalize street addresses from around the world using statistical NLP and open data. More details can be found in [Properties from Libpostal enricher](#properties-from-libpostal-enricher).

The Libpostal enricher supports the following endpoint:

- `http://<host>:<port>/parser    body = {query: {address}}`

## Add Libpostal enricher

The Libpostal enricher uses the address as input to parse and normalize the street address used in a golden record. You can use this enricher to parse and normalize street addresses for organizations, users, persons, and locations. Depending on the business domain you specify in the enricher configuration, you will need to provide the appropriate vocabulary key that contains the address. If you don't provide the vocabulary key, CluedIn will use the following vocabulary keys by default:

- **Person Address Vocab Key** - person.home.address

- **Organization Address Vocab Key** - organization.address

- **User Address Vocab Key** - user.home.address

- **Location Address Vocab Key** - location.fullAddress

**To add the Libpostal enricher**

1. On the navigation pane, go to **Preparation** > **Enrich**. Then, select **Add Enricher**.

1. On the **Choose Enricher** tab, select **Libpostal**, and then select **Next**.

    ![libpostal-enricher-1.png](../../assets/images/preparation/enricher/libpostal-enricher-1.png)

1. On the **Configure** tab, provide the following details:

    - **Accepted Business Domain** – enter the business domain to define which golden records will be enriched using the Libpostal enricher. Depending on the business domain that you provide, you need to fill out one more field to define the vocabulary key that contains addresses of golden records that you want to enrich.

    - **Person Address Vocab Key** – if you entered /Person as the accepted business domain, enter the vocabulary key that contains the home addresses of persons that you want to enrich.

    - **Organization Address Vocab Key** – if you entered /Organization as the accepted business domain, enter the vocabulary key that contains the addresses of organizations that you want to enrich.

    - **User Address Vocab Key** – if you entered /User as the accepted business domain, enter the vocabulary key that contains the addresses of users that you want to enrich.

    - **Location Address Vocab Key** – if you entered /Location as the accepted business domain, enter the vocabulary key that contains the addresses of locations that you want to enrich.

        ![libpostal-enricher-2.png](../../assets/images/preparation/enricher/libpostal-enricher-2.png)

1. Select **Add**.

    The Libpostal enricher is added and has an active status. This means that it will enrich golden records based on the configuration details during processing or when you trigger external enrichment.

After the Libpostal enricher is added, you can modify its details:

- **Settings** – add a user-friendly display name, select the description for data coming from the enricher, and define the source quality for determining the winning values.

    ![libpostal-enricher-3.png](../../assets/images/preparation/enricher/libpostal-enricher-3.png)

- **Authentication** – modify the details you provided while configuring the enricher.

## Properties from Libpostal enricher

You can find the properties added to golden records from the Libpostal enricher on the **Properties** page.

![libpostal-enricher-4.png](../../assets/images/preparation/enricher/libpostal-enricher-4.png)

For a more detailed information about the changes made to a golden record by the Libpostal enricher, check the corresponding data part on the **History** page.

![libpostal-enricher-5.png](../../assets/images/preparation/enricher/libpostal-enricher-5.png)

The following table lists the properties that can be added to golden records by the Libpostal enricher.

| Display name | Vocabulary key |
|--|--|
| Category | libpostal.location.Category |
| City | libpostal.location.City |
| City_district | libpostal.location.City_district |
| Country | libpostal.location.Country |
| Country_region | libpostal.location.Country_region |
| Entrance | libpostal.location.Entrance |
| House | libpostal.location.House |
| House_number | libpostal.location.House_number |
| Island | libpostal.location.Island |
| Level | libpostal.location.Level |
| Near | libpostal.location.Near |
| Po_box | libpostal.location.Po_box |
| Postcode | libpostal.location.Postcode |
| Road | libpostal.location.Road |
| Staircase | libpostal.location.Staircase |
| State | libpostal.location.State |
| State_district | libpostal.location.State_district |
| Suburb | libpostal.location.Suburb |
| Unit | libpostal.location.Unit |
| World_region | libpostal.location.World_region |