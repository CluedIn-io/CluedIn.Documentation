---
layout: cluedin
title: Copilot
parent: Solutions & integrations
nav_order: 70
has_children: true
permalink: /solutions/copilot
content_type: landing
summary: Asking questions about your golden records in natural language through Copilot.
redirect_from: ["/microsoft-integration/copilot-integration"]
source_path: docs/180-microsoft-integration/030-copilot.md
---

CluedIn Copilot is an AI assistant designed to streamline your interactions within the CluedIn platform using natural language commands. With the AI assistant, tasks such as adding tags to records based on specific criteria become effortless—simply prompt the assistant, and it automatically generates rules for you. The CluedIn Copilot experience can be personalized according to your language preference.

Note that CluedIn Copilot is not enabled by default. For more information, see [Get access to CluedIn Copilot](/solutions/copilot/get-access-to-copilot).

The following diagram shows how CluedIn AI assistant can help you with your day-to-days tasks in CluedIn.

![copilot-diagram.png]({{ "/assets/images/microsoft-integration/copilot/copilot-diagram.png" | relative_url }})

{:.important}
Sometimes you may encounter issues with CluedIn Copilot where it does not understand your requests as expected. In such cases, as with any generative AI solution, please start over and create a new chat.

**Notes on CluedIn's integration with Azure OpenAI**

- CluedIn integrates with Azure OpenAI services solely to enable you to make requests and store responses through our platform.

- To interact with Azure OpenAI services via CluedIn's Rule Engine, AI mapping, or Copilot, you must decide where to host Azure OpenAI, including which tenants and locations to use. CluedIn does not provide a default Azure OpenAI token; you must configure CluedIn with your own Azure OpenAI token. Selection of Azure OpenAI services and models within your environment is entirely at your discretion.

- CluedIn transmits your prompts and the data contained within them to Azure OpenAI, giving you full control over the models and deployments used within your environment. Your prompts and results are also stored in CluedIn's SQL server to preserve your prompt history.

- CluedIn cannot comment on how Azure OpenAI manages or processes data internally. Data handling by Azure OpenAI is governed solely by the agreement established directly between you and Microsoft Azure.