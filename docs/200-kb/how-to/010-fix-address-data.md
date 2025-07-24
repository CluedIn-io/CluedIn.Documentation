---
layout: cluedin
title: How to fix address data
parent: Knowledge base
permalink: kb/how-to-fix-address-data
nav_order: 1
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article, you will learn how to fix address data using various methods:

- [Enrichment via Libpostal](#fixing-address-data-using-libpostal-enricher) – use this method to parse and standardize the address.

- [Enrichment via Google Maps](#fixing-address-data-using-google-maps-enricher) – use this method to enhance your golden records with precise address details and comprehensive business information. This method requires a valid Google Maps API key. 

- Enrichment via Azure Maps – use this method to enhance your golden records with precise address details and comprehensive geographic information. This method requires a valid Azure Maps API key. The Azure Maps enricher is not yet available as an open-source package. If you would like to use it, reach out to CluedIn support at [support@cluedin.com](mailto:support@cluedin.com).

    The results of enrichment using Google Maps and Azure Maps are similar. Depending on the API key you have, use the corresponding method to enhance your golden records.

- [Validation and enhancement via AI-based rules](#fixing-address-data-using-ai-based-rule-action) – use this method to enrich any field in your golden records by leveraging AI-driven text prompts. For example, you can find an address based on the company name or retrieve the full postal code using the company name and address.

## Fixing address data using Libpostal enricher

The [Libpostal](/preparation/enricher/libpostal) enricher is particularly useful when you need to parse, standardize, and normalize addresses from various formats. It is a powerful tool that can break down a single address string into its components, such as street, city, and postal code. This helps in standardizing addresses and improving data quality.

The Libpostal enricher has its pros and cons, which can help you decide if it will solve your use case.

**Pros of Libpostal:**  

- It is open source and free to use, with no licensing costs.
- It is great at parsing and address standardization.
- It supports multiple languages and address formats.

**Cons of Libpostal:**  

- It lacks advanced enrichment features, thereby returning fewer details.
- It may experience performance issues when processing large volumes of data.

**Example of using Libpostal**

Let's consider an example of a CluedIn golden record that contains the address property. This property includes street address details all in one value. To ensure data accuracy and usability, we will use the Libpostal enricher to validate and parse this address.

![libpostal-address-input.png](../../assets/images/kb/how-to/libpostal-address-input.png)

To configure the Libpostal enricher, specify the business domain of golden records that you want to enrich and the vocabulary key that contains the initial address.

![libpostal-settings.png](../../assets/images/kb/how-to/libpostal-settings.png)

When the enricher is configured, [trigger](/preparation/enricher/add-enricher#trigger-enrichment) the enrichment for golden records. You can trigger the enrichment for all golden records of the specific business domain using the [GraphQL tool](/consume/graphql/graphql-actions). Alternatively, you can trigger the enrichment manually for each golden record. To do this, on the golden record page, select **More** > **Trigger external enrichment**.

![trigger-external-enrichment.png](../../assets/images/kb/how-to/trigger-external-enrichment.png)

As a result, the CluedIn golden record now contains parsed address with such components as house, house number, level, road, and unit.

![libpostal-enriched.png](../../assets/images/kb/how-to/libpostal-enriched.png)

## Fixing address data using Google Maps enricher

The [Google Maps](/preparation/enricher/google-maps) enricher can help you add valuable context about a specific place, such as its name, address, phone number, website, user reviews, and ratings. To use this enricher, you need to have a valid Google Maps API key.

The Google Maps enricher has its pros and cons, which can help you decide if it will solve your use case.

**Pros of Google Maps:**  

- It provides a comprehensive location data—extensive address validation, geocoding, and enrichment capabilities.
- It provides a global coverage and supports address validation in multiple countries and different languages.

**Cons of Google Maps:**

- To use the Google Maps enricher, you need an API key from the Google Maps Platform.
- Google Maps API keys are insecure if unrestricted.
- High usage of Google Maps can become expensive.

**Example of using Google Maps**

Let's consider an example of the same CluedIn golden record. To add more context about the company, we will use the Google Maps enricher to retrieve additional information. We are using the same golden record to illustrate the difference between two enrichers.

![google-maps-input.png](../../assets/images/kb/how-to/google-maps-input.png)

To configure the Google Maps enricher, specify the following details:

- **API Key** for retrieving information from the Google Maps Platform.

- **Accepted Business Domain** (previously entity type) to define which golden records will be enriched.

- **Vocabulary Key used to control whether it should be enriched** to indicate if the golden record should be enriched. If the value of the vocabulary key is _true_, then the golden record will be enriched. Otherwise, the golden record will not be enriched.

- **Organization Name Vocab Key** to define company names that will be used for searching the Google Maps Platform.

- **Organization Address Vocab Key** to define company addresses that will be used for searching the Google Maps Platform.

![google-maps-settings.png](../../assets/images/kb/how-to/google-maps-settings.png)

When the enricher is configured, [trigger](/preparation/enricher/add-enricher#trigger-enrichment) the enrichment for golden records. You can trigger the enrichment for all golden records of the specific business domain using the [GraphQL tool](/consume/graphql/graphql-actions), or you can trigger the enrichment manually for each golden record. Alternatively, you can trigger the enrichment manually for each golden record. To do this, on the golden record page, select **More** > **Trigger external enrichment**.

As a result, the CluedIn golden record now contains a variety of company details from Google Maps, such as administrative area level 1 and 2, business status, country code, and more.

![google-maps-enriched.png](../../assets/images/kb/how-to/google-maps-enriched.png)

## Fixing address data using AI-based rule action

The AI-based rule action can be used to enhance golden records with additional information based on their existing properties. The AI-based rule action has its pros and cons, which can help you decide if it will solve your use case.
 
**Pros of AI-based rule action:** 

- No need to prepare or configure third-party enrichers.
- AI-based rule action leverages AI prompts for free text queries.
- It provides full control over what to parse, standardize, transform, and use from the results within the same rule and prompt.

**Cons of AI-based rule action:**  

- It requires access to additional resources, such as Azure OpenAI Service for access to OpenAI’s models.
- Processing large volumes of prompts can be expensive.

**Example of AI-based rule action**

We'll use a Google golden record to illustrate how to validate the address and get full postal address based on the existing address data.
 
![ai-rules-address-input.png](../../assets/images/kb/how-to/ai-rules-address-input.png)

To validate the address, [create](/management/rules/create-rule) a data part rule and select an action to add value with CluedIn AI. In the action, do the following:

- Select the address vocabulary key that AI engine will use as an input.

- Enter the prompt for the AI engine explaining what to do with the address. For example, `Check the address in {vocabulary:trainingcompany.address} and company name in {vocabulary:trainingcompany.name} and return the full postal address only`.

- Enter the name of Azure OpenAI Service model—`gpt-35-turbo-instruct`.

- Select the field for AI-generated full postal address.

![ai-rules-address-action.png](../../assets/images/kb/how-to/ai-rules-address-action.png)

Next, save, activate and re-process the rule. To verify that the rule has been applied, find and open the Google golden record. As a result, new field—AI Address—containing full postal address has been added.

![ai-rules-address-output.png](../../assets/images/kb/how-to/ai-rules-address-output.png)