---
layout: cluedin
nav_order: 4
parent: Enricher
grand_parent: Preparation
permalink: /preparation/enricher/azure-openai
title: Brreg
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

This article explains how to add the Azure OpenAI enricher. The purpose of this enricher is to enhance data quality by providing more complete, current, and detailed information for your golden records. It can automate the process of data research, offering up-to-date intelligence on your records and reducing the need for manual efforts.

The Azure OpenAI enricher supports the following endpoints:

- `{baseUrl}/openai/deployments/{deploymentName}/completions?api-version=2022-12-01`
    
- `{baseUrl}/openai/deployments/deploymentName}/chat/completions?api-version=2024-06-01`

You can instruct the Azure OpenAI enricher to enhance your golden records with the help of prompts. These prompts must contain at least:

- One input property – the vocabulary key that contains the information you provide to an AI model to process and generate a response.

- One output property – the vocabulary key where the desired result will be stored.

Here are some examples of prompts:

- Finding the country based on address:

    ```
    Using the address in {Vocabulary:organization.address} provide the country of the organization in {output:vocabulary:organization.CountryAI}
    ```

- Translating the text from one language to another:

    ```
    Please get {output:vocabulary:organization.japaneseName} by translating {Vocabulary:organization.name} into Japanese.
    ```

- Generating the summary or description based on some text:

    ```
    Generate a brief summary {output:vocabulary:website.SummaryAI} based on {Vocabulary:website.WebsiteDescription} and {Vocabulary:website.Title}
    ```

## Add Azure OpenAI enricher

To use the Azure OpenAI enricher, you need to have an [Azure OpenAI Service](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/create-resource?pivots=web-portal) resource set up in the Azure portal and provide the necessary credentials for that resource in CluedIn.

**To configure Azure OpenAI integration in CluedIn**

1. Go to **Administration** > **Azure Integration** > **Azure AI Services**.

1. Enter the **API Key** used to authenticate and authorize access to your Azure OpenAI resource.

1. Enter the **Base URL** for your Azure OpenAI resource in the format similar to the following: `https://{resource-name}.openai.azure.com/`.

1. Leave the **Resource Key** field empty.

1. Enter the **Deployment Name** assigned to a specific instance of a model when it was deployed.

1. Specify the number of **Maximum Requests** that can be sent to the Azure OpenAI deployment.

    ![azure-openai-enricher-1.png](../../assets/images/preparation/enricher/azure-openai-enricher-1.png)

1. Select **Save**.

    Once the Azure OpenAI integration is configured in CluedIn, proceed to add the Azure OpenAI enricher.

**To add Azure OpenAI enricher**

1. On the navigation pane, go to **Preparation** > **Enrich**. Then, select **Add Enricher**.

1. On the **Choose Enricher** tab, select **Azure OpenAI**, and then select **Next**.

    ![azure-openai-enricher-2.png](../../assets/images/preparation/enricher/azure-openai-enricher-2.png)

1. On the **Configure** tab, provide the following details:

    1. **AI Deployment Name** – enter the deployment name assigned to a specific instance of a model when it was deployed. This is the same deployment name as in **Administration** > **Azure Integration** > **Azure AI Services**.

    1. **Accepted Business Domain** – enter the business domain to define which golden records will be enriched.

    1. **Prompt** – enter the instruction for Azure OpenAI to generate results. The prompt requires at least one input (e.g., `Vocabulary:XXXX.YYYY`) and one output (e.g., `output:Vocabulary:PPPP.QQQQ`). For example, the following prompt asks Azure OpenAI to translate the company name and store the result in a dedicated vocabulary key:

        ```
        Translate {Vocabulary:trainingcompany.name} into French and put the output into {output:vocabulary:trainingcompany.frenchName}.
        ```

        ![azure-openai-enricher-3.png](../../assets/images/preparation/enricher/azure-openai-enricher-3.png)

1. Select **Test Connection** to make sure the enricher is properly configured, and then select **Add**.

    The Azure OpenAI enricher is added and has an active status. This means that it will enrich relevant golden records during processing or when you trigger external enrichment.

After the Azure OpenAI enricher is added, you can modify its details:

- **Settings** – add a user-friendly display name, select the description for data coming from the enricher, and define the source quality for determining the winning values.

- **Authentication** – modify the details you provided while configuring the enricher.

## Properties from Azure OpenAI enricher

You can find the properties added to golden records from the Azure OpenAI enricher on the **Properties** page. The vocabulary keys added to golden records by the Azure Open AI enricher are grouped under **No Source** source type. 

![azure-openai-enricher-4.png](../../assets/images/preparation/enricher/azure-openai-enricher-4.png)

For a more detailed information about the changes made to a golden record by the Azure OpenAI enricher, check the corresponding data part on the **History** page.

![azure-openai-enricher-5.png](../../assets/images/preparation/enricher/azure-openai-enricher-5.png)