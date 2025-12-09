---
layout: cluedin
title: AI agents FAQs
parent: AI agents
grand_parent: Management
nav_order: 060
permalink: /management/ai-agents/ai-agents-faqs
tags: ["management", "ai agents", "faq"]
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

{:.important}
The information in this article applies to the following [CluedIn deployment models](/get-cluedin): PaaS, private SaaS.

This article addresses commonly asked questions about [AI agents](/management/ai-agents) in CluedIn, including their setup, operation, and security controls.

## Available architecture and deployment options

CluedIn is deployed inside your Azure tenant. CluedIn does not build its own AI or large language models (LLMs); instead, customers bring their own LLMs.

As of now, CluedIn supports two mechanisms for enabling AI features in CluedIn. In future, a third mechanism will be added. Details about these mechanisms are provided below.

### Fully local (on-premises or private infrastructure)

- CluedIn is deployed within an [Azure Kubernetes Service (AKS)](https://learn.microsoft.com/en-us/azure/aks/what-is-aks) environment that hosts multiple [Docker](https://www.docker.com/) containers orchestrated with [Kubernetes](https://kubernetes.io/).
- One of these containers runs [Ollama](https://ollama.com/), an open-source product that allows hosting open-source LLMs such as [Phi](https://azure.microsoft.com/en-us/products/phi), [Llama](https://www.llama.com/), [Mistral](https://docs.mistral.ai/getting-started/models/models_overview/), and others.
- CluedIn comes pre-installed with 8 open-source LLMs, ranging from 1 billion to 8 billion parameters. These smaller models are useful for local inference but are not equivalent in performance or quality to hosted models.
- The value of this approach is that all communication between CluedIn and the LLM occurs within the Kubernetes environment. Therefore, no data is sent to a third-party service, not even to [Microsoft Azure](https://azure.microsoft.com/en-us/).

### Azure AI Foundry (controlled cloud environment)

[Azure AI Foundry](https://azure.microsoft.com/en-us/products/ai-foundry) supports over 11,000 models, though CluedIn currently supports chat/completion-based LLMs only. It is recommended to use [GPT models](https://platform.openai.com/docs/models), as they are the most tested and widely used with CluedIn.

How it works:
- CluedIn application uses the data hosted in CluedIn and sends it securely (over encrypted transport) to the LLM hosted in your Azure tenant.
- Communication stays entirely within the Azure network.
- You can whitelist IP addresses so that only the CluedIn application can access your Azure AI Foundry endpoint.

This is the most common setup that CluedIn customers use for AI features.

<!-- Hiding this section since the code is peding rebase, test and merge activities>
### Open chat/public API (coming in November 2025)

- This option will support publicly hosted LLMs (including [Google Gemini](https://gemini.google.com/), [Open AI](https://openai.com/), and [Anthropic Claude](https://claude.ai/)).
- In this configuration, communication occurs over the public internet, secured via HTTPS and authenticated API tokens.
- Data remains encrypted during transit and at rest, but customers must ensure they trust the provider’s Terms and Conditions regarding data usage. For example, some providers commit not to use API data for training.

-->

## AI agent configuration

- Each AI agent in CluedIn can use its own LLM. There is no requirement for all agents to use the same LLM.
- There are no limits on the number of LLMs you can use in CluedIn.
- All data mounted to an AI agent respects [CluedIn’s access control rules](/management/access-control) – access can be restricted or even masked at the cell level.
- For configuration instructions, see [Create, configure, and run an AI agent](/management/ai-agents/create-configure-and-run-an-ai-agent).

## How AI agents operate

Each AI agent is configured with the following elements:

- A set of text instructions (prompts).
- The ability to generate recommendations for a human reviewer.
- The ability to use a single LLM to do its work.
- An optional schedule defining how often it runs.
- Access to one or more datasets, governed by [CluedIn’s access control rules](/management/access-control).

Key principles:
- AI Agents only have read-only access. They cannot directly modify data or create objects (for example, rules, deduplication projects etc.). It can only suggest recommendations. 
- Agents run a set of jobs (prompts) toward defined goals.
- Once an agent completest its run, it a set of suggestions for human review.

Human-In-The-Loop (HITL):

By default, every suggestion must be explicitly reviewed and approved by a Human-In-The-Loop (HITL). Approval actions are recorded in the audit log, including:
- Which AI agent proposed the action
- Which human user approved and executed it
- What decision was taken

Auto-approval of AI suggestions:

CluedIn provides an optional setting that allows organizations to automatically approve AI suggestions without manual HITL review.

When this setting is enabled:
- The AI agent still remains read-only, it does not perform updates directly.
- However, CluedIn automatically executes the suggested actions on the user’s behalf, as if a human approved them
- All auto-approved actions are logged for audit and traceability

This mode is intended for low-risk, trusted workflows where continuous human review would create unnecessary overhead.


Data access boundaries:


An AI agent can only read data explicitly provided to it. The agent cannot access data of its own volition.

End users have an open canvas where they can enter their own prompts. However, strict, deterministic guardrails ensure that AI agents can only read data they have been explicitly granted access to, nothing more.

{:.important}
AI agents do not have Create, Update or Delete permissions.

## Data handling and transmission

- All data handling occurs over HTTPS.
- API tokens are used for authentication and encryption in transit.
- All stored data is also encrypted at rest.

## Monitoring

You can monitor the following:
 - What data is sent and to which destinations.

    CluedIn audits all communications between the AI agent and its LLM, including data payloads. You can [review](/management/ai-agents/review-the-results-returned-by-an-ai-agent) this information on the **Results** tab of the AI agent.

 - Data flows between internal and external components.

    For detailed information, refer to the description of the [three LLM hosting models](#available-architecture-and-deployment-options).

 - Outbound API calls and integration activity.

    - For fully local and Azure Foundry AI hosting options, you can whitelist API calls coming from CluedIn – and if necessary, CluedIn only.

    - With the open chat/public API hosting option, you can monitor outbound traffic. Public providers (for example, Open AI) have API monitoring analytics to track requests.

## Data update and oversight controls

AI agents in CluedIn have no ability to create, update, or delete data. They operate in a read-only capacity, preparing recommendations for human approval. This means that AI agents cannot:

- Fix or modify data
- Create rules
- Tag records

All changes suggested by AI agents require human approval. If a suggestion is approved, CluedIn records this as a human-initiated change, not an AI-initiated one.

You can also enforce limits at the LLM level to control:

- The number of API calls
- The type of prompts
- Prompt size

In Azure AI Foundry, additional model-level restrictions can be applied, defining what the LLM can or cannot respond to.

## Controls around automated data updates

When it comes to automated data updates, this includes:

- How auto-updates or AI-initiated changes are reviewed.
- The required level of human oversight.
- Bulk approval mechanisms that are required before data changes are committed.

Key rules:

- AI agents cannot auto-update anything. They can only surface suggestions to a human or group of humans.
- All suggestions have a workflow enabled by default, which can be customized for your approval process (for example, to get approval from multiple people).
- AI agent suggestions can be approved individually or in bulk, but all approvals must be done by a human.
- An AI agent cannot self-approve any changes.
