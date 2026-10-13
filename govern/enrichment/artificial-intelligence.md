---
title: AI enricher
url: https://documentation.cluedin.net/govern/enrichment/artificial-intelligence
content_type: reference
section: Govern & improve > Enrichment
---

# AI enricher

> reference: Facts, options, APIs.

This article explains how to add the Artificial Intelligence enricher. The purpose of this enricher is to enhance data quality by providing more complete, current, and detailed information for your golden records. It can automate the process of data research, offering up-to-date intelligence on your records and reducing the need for manual efforts.

You can instruct the Artificial Intelligence enricher to enhance your golden records with the help of prompts. These prompts must contain at least:

- One input property – the vocabulary key that contains the information you provide to an AI model to process and generate a response.

- One output property – the vocabulary key where the desired result will be stored.

Here are some examples of prompts:

- Finding the country based on address:

    ```
    Using the address in {Vocabulary:organization.address} provide the country of the organization in {output:Vocabulary:organization.aiCountry}
    ```

- Translating the text from one language to another:

    ```
    Please get {output:vocabulary:organization.japaneseName} by translating {Vocabulary:organization.name} into Japanese.
    ```

- Generating the summary or description based on some text:

    ```
    Generate a brief summary {output:vocabulary:website.SummaryAI} based on {Vocabulary:website.WebsiteDescription} and {Vocabulary:website.Title}
    ```

## Add Artificial Intelligence enricher

To use the Artificial Intelligence enricher, you need to have an [Azure OpenAI Service](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/create-resource?pivots=web-portal) resource set up in the Azure portal and provide the necessary credentials for that resource in CluedIn.

**To configure Artificial Intelligence integration in CluedIn**

1. Go to **Administration** > **Artificial Intelligence**.

   ![Administration - Artificial Intelligence page with Platforms, Deployments and Endpoints cards, each with a View all link](https://documentation.cluedin.net/assets/images/preparation/enricher/ai-enricher/ai-enricher-1.png)

1. Create a platform using your Azure OpenAI resource. Enter the **Base URL** for your Azure OpenAI resource in the format similar to the following: `https://{resource-name}.openai.azure.com/`.

   ![Create platform pane with name Azure OpenAI, platform Azure Open AI, an API key, and the Base Url of the Azure OpenAI resource](https://documentation.cluedin.net/assets/images/preparation/enricher/ai-enricher/ai-enricher-2.png)

1. Create a deployment using the platform created. Please include the cost details for the deployment, if any.

   ![Create deployment pane for gpt-4.1 on the Azure OpenAI platform, with currency, cost per input and output token, and max input tokens](https://documentation.cluedin.net/assets/images/preparation/enricher/ai-enricher/ai-enricher-3.png)

1. Create an endpoint using the deployment created.

   ![Create endpoint pane with name gpt-4.1, deployment gpt-4.1, and endpoint type Chat](https://documentation.cluedin.net/assets/images/preparation/enricher/ai-enricher/ai-enricher-4.png)

**To add Artificial Intelligence enricher**

1. On the navigation pane, go to **Preparation** > **Enrich**. Then, select **Add Enricher**.

1. On the **Choose Enricher** tab, select **Artificial Intelligence**, and then select **Next**.

   ![Choose enricher tab of the Add Enricher pane with Artificial Intelligence selected](https://documentation.cluedin.net/assets/images/preparation/enricher/ai-enricher/ai-enricher-5.png)

1. On the **Configure** tab, provide the following details:

    1. **Endpoint** – select the endpoint created in **Administration** > **Artificial Intelligence** > **Endpoints**.

    1. **Accepted Business Domain** – enter the business domain to define which golden records will be enriched.

    1. **Prompt** – enter the instruction for Artificial Intelligence to generate results. The prompt requires at least one input (e.g., `Vocabulary:XXXX.YYYY`) and one output (e.g., `output:Vocabulary:PPPP.QQQQ`). For example, the following prompt asks Artificial Intelligence to translate the company name and store the result in a dedicated vocabulary key:

        ```
        Using the address in {Vocabulary:companies2.address} provide the country of the organization in {output:Vocabulary:companies2.aiCountry}.
        ```

        ![Configure tab of the Add Enricher pane with an Endpoint, Organization as the accepted type, and a prompt with input and output vocabulary keys](https://documentation.cluedin.net/assets/images/preparation/enricher/ai-enricher/ai-enricher-6.png)

1. Click **Save**. The Artificial Intelligence enricher is added and has an active status. This means that it will enrich relevant golden records during processing or when you trigger external enrichment.

After the Artificial Intelligence enricher is added, you can modify its details:

- **Settings** – add a user-friendly display name, select the description for data coming from the enricher, and define the source quality for determining the winning values.

- **Authentication** – modify the details you provided while configuring the enricher.

## Properties from Artificial Intelligence enricher

You can find the properties added to golden records from the Artificial Intelligence enricher on the **Properties** page. 

![Properties page of a golden record showing an AI Country property whose source is the Artificial Intelligence enricher](https://documentation.cluedin.net/assets/images/preparation/enricher/ai-enricher/ai-enricher-7.png)

For a more detailed information about the changes made to a golden record by the Artificial Intelligence enricher, check the corresponding data part on the **History** page.

![History page of a golden record with the expanded Artificial Intelligence data part showing the added AI Country value](https://documentation.cluedin.net/assets/images/preparation/enricher/ai-enricher/ai-enricher-8.png)

Up: [Enrichment](https://documentation.cluedin.net/govern/enrichment.md)
