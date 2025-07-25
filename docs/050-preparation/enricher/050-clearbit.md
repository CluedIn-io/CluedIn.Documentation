---
layout: cluedin
nav_order: 5
parent: Enricher
grand_parent: Preparation
permalink: preparation/enricher/clearbit
title: Clearbit
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

This article outlines how to configure the Clearbit enricher. [Clearbit](https://clearbit.com/) is a marketing data engine that provides tools for data enrichment, lead generation, marketing intelligence, and more. The purpose of Clearbit enricher is to retrieve company logo and domain information.

The Clearbit enricher supports the following endpoint:

- `https://autocomplete.clearbit.com/v1/companies/suggest?query=`

## Add Clearbit enricher

The enricher requires at least one of the following attributes to search for company logo and domain:

- **Website** – if your golden records have websites, you can enter the corresponding vocabulary key to configure the enricher. As a result, the enricher will use the website to search for domain and logo information. If your golden records do not have websites, then one of the other attributes will be used for search.

- **Organization Name** – if your golden records have organization names, you can enter the corresponding vocabulary key to configure the enricher. As a result, the enricher will use the organization name to search for domain and logo information. If your golden records do not have organization names, then one of the other attributes will be used for search.

- **Email Domain** – if your golden records have email domain names, you can enter the corresponding vocabulary key to configure the enricher. As a result, the enricher will use the email domain name to search for domain and logo information. If your golden records do not have email domain names, then one of the other attributes will be used for search. 

**To add the Clearbit enricher**

1. On the navigation pane, go to **Preparation** > **Enrich**. Then, select **Add Enricher**.

1. On the **Choose Enricher** tab, select **Clearbit**, and then select **Next**.

    ![clearbit-enricher-1.png]({{ "/assets/images/preparation/enricher/clearbit-enricher-1.png" | relative_url }})

1. On the **Configure** tab, provide the following details:

    - **Accepted Business Domain** – enter the business domain to define which golden records will be enriched.

    - **Website Vocabulary Key** – enter the vocabulary key that contains company websites that will be used to search for company domain and logo.

    - **Organization Name Vocabulary Key** – enter the vocabulary key that contains company names that will be used to search for company domain and logo.

    - **Email Domain Vocabulary Key** – enter the vocabulary key that contains company email domains that will be used to search for company domain and logo.

        ![clearbit-enricher-2.png]({{ "/assets/images/preparation/enricher/clearbit-enricher-2.png" | relative_url }})

1. Select **Test Connection** to make sure the enricher is properly configured, and then select **Add**.

    The Clearbit enricher is added and has the active status. It means that it will enrich relevant golden records when they are processed or when your trigger external enrichment.

After the Clearbit enricher is added, you can modify its details:

- **Settings** – add a user-friendly display name, select the description for data coming from the enricher, and define the source quality for determining the winning values.

- **Authentication** – modify the details you provided while configuring the enricher.

## Properties from Clearbit enricher

To quickly find the properties added to golden records from the Clearbit enricher, use the integrations filter on the **Properties** page.

![clearbit-enricher-4.png]({{ "/assets/images/preparation/enricher/clearbit-enricher-4.png" | relative_url }})

For a more detailed information about the changes made to a golden record by the Clearbit enricher, check the corresponding data part on the **History** page.

![clearbit-enricher-5.png]({{ "/assets/images/preparation/enricher/clearbit-enricher-5.png" | relative_url }})

The following table lists the properties that can be added to golden records by the Clearbit enricher.

| Display name | Vocabulary key |
|--|--|
| Domain | clearbit.organization.domain |
| Logo | clearbit.organization.logo |
