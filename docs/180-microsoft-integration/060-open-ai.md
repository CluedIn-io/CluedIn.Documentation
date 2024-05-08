---
layout: cluedin
title: Azure Open AI Integration
parent: Microsoft Integration
permalink: /microsoft-integration/open-ai-integration
nav_order: 060
---

With Azure OpenAI integration, you can leverage AI capabilities to analyze data and determine mapping for you.

In this article, you will learn what you need to do to make the AI mapping available in CluedIn.

**For Azure Administrators and CluedIn Organization Administrators**

1. In CluedIn, go to **Administration** > **Feature Flags**, and then enable the **AI Mapping** feature.

    ![ai-mapping-1.png](../../assets/images/microsoft-integration/open-ai/ai-mapping-1.png)

1. Go to **Administration** > **Settings**. Scroll down to the **Open AI** section and complete the following fields:

    - **API Key** – you can find this value in your Azure OpenAI resource. In Azure portal, go to **Resource Management** > **Keys and Endpoint**. You can use either KEY 1 or KEY 2.

    - **Base URL** – you can find this value in your Azure OpenAI resource. In Azure portal, go to **Resource Management** > **Keys and Endpoint**, and then get the value from the **Endpoint** field. Alternatively, you can find this value in Azure OpenAI Studio by going to **Playground** > **View code**.

    - **Resource Key** – you can find this value in your Azure OpenAI resource. In Azure portal, go to **Resource Management** > **Keys and Endpoint**. Since you have already used one key in the **API Key** field, use the other key in the **Resource Key** field.

    - **Deployment Name** – this is the custom name you chose for your deployment when you deployed a model. You can find this value in your Azure OpenAI resource. In Azure portal, go to **Resource Management** > **Model Deployments**. Alternatively, you can find this value in Azure OpenAI Studio by going to **Management** > **Deployments**.

        ![ai-mapping-2.png](../../assets/images/microsoft-integration/open-ai/ai-mapping-2.png)

        For more information about the required variables, see [Microsoft documentation](https://learn.microsoft.com/en-us/azure/ai-services/openai/quickstart?tabs=command-line%2Cpython&pivots=programming-language-python#retrieve-key-and-endpoint).