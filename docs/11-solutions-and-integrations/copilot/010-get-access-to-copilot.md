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

CluedIn does not provide an LLM or API token to interact with Copilot. You need an [AI endpoint](/govern/ai-agents/prerequisites-to-using-ai-agents#configure-ai-settings) that points at one of the supported models. We recommend using **GPT-5.1 or higher**, or a comparable Claude (Anthropic) model. You cannot use different models for different skills.

To make the AI assistant available in CluedIn, you need to fulfill several prerequisites:

1. [Configure an AI platform, deployment and endpoint](/govern/ai-agents/prerequisites-to-using-ai-agents#configure-ai-settings) for the model you want Copilot to use.

1. Enable development features for your CluedIn instance. Depending on the type of CluedIn installation, do one of the following:

    - If you have CluedIn AMA, contact CluedIn support to get this feature in your system.

    - If you are running the local installation of CluedIn, in the **.env** file for your environment, set ENABLE_DEVELOPMENT_FEATURES to **true**, and then stop and start your CluedIn instance.

1. In CluedIn, go to **Administration** > **Feature Flags**, and then enable the **AI Copilot** feature.

    ![The AI Copilot feature flag card, labelled Development, with its toggle set to Enabled]({{ "/assets/images/key-terms-and-features/copilot-1.png" | relative_url }})

1. In CluedIn, go to **Administration** > **Azure Integration** > **Copilot**. Then, complete the following fields:

    - **Endpoint** – select the AI endpoint you configured for Copilot to use. Copilot sends its requests through this endpoint's credentials and deployment, and usage is tracked against it.

    - **Minimum Skill Development Stage** – specify which skills—alpha, beta, or production—you want to have available in CluedIn. Currently, almost all skills are **alpha**.

        ![Copilot settings with the Endpoint dropdown set to gpt-4.1 and Minimum Skill Development Stage set to Alpha]({{ "/assets/images/key-terms-and-features/copilot-2.png" | relative_url }})

1. Select **Save**.

    If the endpoint's credentials are invalid, or the model does not support a request Copilot sends, test it from **Administration** > **Artificial Intelligence** > **Endpoints** to see the underlying error.