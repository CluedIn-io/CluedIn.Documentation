---
layout: cluedin
nav_order: 12
parent: Enricher
grand_parent: Preparation
permalink: /preparation/enricher/google-images
title: Google Images
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

This article explains how to add the Google Images enricher. The purpose of this enricher is to search for an image based on the provided text—such as a company, organization, or any other name—and add the retrieved image to the golden record.

The Google Images enricher supports the following endpoint:

- `https://www.googleapis.com/customsearch/v1?key={APIKey}&cx=000950167190857528722:vf0rypkbf0w&q={Name}&searchType=image`

## Add Google Images enricher

To use the Google Images enricher, you must provide the API key. To get the API key, follow the instructions [here](https://cloud.google.com/docs/authentication/api-keys#create). The enricher uses the defined image search text (from a vocabulary key) as the query for retrieving relevant images.

**To add Google Images enricher**

1. On the navigation pane, go to **Preparation** > **Enrich**. Then, select **Add Enricher**.

1. On the **Choose Enricher** tab, select **Google Images**, and then select **Next**.

    ![google-images-enricher-1.png]({{ "/assets/images/preparation/enricher/google-images-enricher-1.png" | relative_url }})

1. On the **Configure** tab, provide the following details:

    1. **API Key** – enter the API key required to authenticate with the Google Images endpoint.

    1. **Accepted Business Domain** – enter the business domain to define which golden records will be enriched.

    1. **Image Search text** – enter the vocabulary key that contains the text to be used for the image search.

        ![google-images-enricher-2.png]({{ "/assets/images/preparation/enricher/google-images-enricher-2.png" | relative_url }})

1. Select **Test Connection** to make sure the enricher is properly configured, and then select **Add**.

    The Google Images enricher is added and has an active status. This means that it will enrich relevant golden records during processing or when you trigger external enrichment.

After the Google Images enricher is added, you can modify its details:

- **Settings** – add a user-friendly display name, select the description for data coming from the enricher, and define the source quality for determining the winning values.

- **Authentication** – modify the details you provided while configuring the enricher.

## Properties from Google Images enricher

You can find the image added to the golden record on the golden record **Overview** page.

![google-images-enricher-3.png]({{ "/assets/images/preparation/enricher/google-images-enricher-3.png" | relative_url }})

For a more detailed information about the changes made to a golden record by the Google Images enricher, check the corresponding data part on the **History** page.

![google-images-enricher-4.png]({{ "/assets/images/preparation/enricher/google-images-enricher-4.png" | relative_url }})