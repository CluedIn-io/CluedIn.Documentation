---
layout: cluedin
title: Get access to CluedIn Copilot
parent: Copilot
grand_parent: Solutions & integrations
nav_order: 10
permalink: /solutions/copilot/get-access-to-copilot
content_type: how-to
redirect_from: ["/microsoft-integration/copilot-integration/get-access-to-copilot"]
source_path: docs/180-microsoft-integration/copilot/010-get-access-to-copilot.md
---

In this article, you will learn what you need to do to make the AI assistant available in CluedIn.

**For Azure Administrators and CluedIn Organization Administrators**

CluedIn does not provide an LLM or API token to interact with Copilot. You need to provide credentials for one of the available Azure OpenAI models. We recommend using **GPT-5.1 or higher**. You cannot use different models for different skills. 

To make the AI assistant available in CluedIn, you need to fulfill several prerequisites:

1. In your Azure OpenAI resource, make sure that you have created a deployment that uses **GPT-5.1 or higher**.

1. Enable development features for your CluedIn instance. Depending on the type of CluedIn installation, do one of the following:

    - If you have CluedIn AMA, contact CluedIn support to get this feature in your system.

    - If you are running the local installation of CluedIn, in the **.env** file for your environment, set ENABLE_DEVELOPMENT_FEATURES to **true**, and then stop and start your CluedIn instance.

1. In CluedIn, go to **Administration** > **Feature Flags**, and then enable the **AI Copilot** feature.

    ![The AI Copilot feature flag card, labelled Development, with its toggle set to Enabled]({{ "/assets/images/key-terms-and-features/copilot-1.png" | relative_url }})

1. Skip this step if you already have exactly one AI endpoint configured under **Administration** > **Artificial Intelligence** (see [Prerequisites to using AI agents]({{ "/govern/ai-agents/prerequisites-to-using-ai-agents" | relative_url }})) - Copilot uses that endpoint automatically in that case. Otherwise, in CluedIn, go to **Administration** > **Azure Integration** > **Copilot**. Then, complete the following fields:

    - **Base Url** – you can find this value in your Azure OpenAI resource. In Azure portal, go to **Resource Management** > **Keys and Endpoint**, and then get the value from the **Endpoint** field. Alternatively, you can find this value in Azure OpenAI Studio by going to **Playground** > **View code**.

    - **API Key** – you can find this value in your Azure OpenAI resource. In Azure portal, go to **Resource Management** > **Keys and Endpoint**. You can use either KEY 1 or KEY 2.

    - **Deployment** – specify the custom name you chose for your deployment when you deployed a model. In Azure portal, go to **Resource Management** > **Deployments**. Alternatively, you can find this value in Azure OpenAI Studio by going to **Management** > **Deployments**.

    - **Deployment Max Tokens** – specify the number of tokens that correspond to the [model](https://platform.openai.com/docs/models/moderation) used. The minimum number should be **16384**.

    - **Minimum Skill Development Stage** – specify which skills—alpha, beta, or production—you want to have available in CluedIn. Currently, almost all skills are **alpha**.

        ![Copilot settings with the Base Url, API Key, Deployment, Deployment Max Tokens (16384) and Minimum Skill Development Stage (Alpha) fields]({{ "/assets/images/key-terms-and-features/copilot-2.png" | relative_url }})

        For more information about the required variables, see [Microsoft documentation](https://learn.microsoft.com/en-us/azure/ai-services/openai/quickstart?tabs=command-line%2Cpython&pivots=programming-language-python#retrieve-key-and-endpoint).