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
- Once an agent completest its run, it produces a set of suggestions for human review.

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

# Connecting CluedIn MCP to Claude, ChatGPT and Microsoft Copilot

CluedIn exposes a **Model Context Protocol (MCP) server** that allows supported AI assistants and agents to securely interact with CluedIn.

The MCP server is available from your CluedIn instance at:

```text
https://<your-cluedin-instance>/api/mcp/server
```

For example:

```text
https://name.weu.saas.cluedin.com/api/mcp/server
```

> **Important:** The hostname will be different for each CluedIn environment.
> The important part is the `/api/mcp/server` path at the end of your CluedIn URL.

For example, if you access CluedIn at:

```text
https://contoso.neu.saas.cluedin.com
```

your MCP server URL will be:

```text
https://contoso.neu.saas.cluedin.com/api/mcp/server
```

## Authentication

The CluedIn MCP server supports **OAuth authentication**.

You do **not** need to manually create or enter a Client ID or Client Secret when connecting through clients that support MCP OAuth discovery.

When the AI client connects to CluedIn, you will be redirected to CluedIn to:

1. Sign in to your CluedIn account.
2. Authenticate your identity.
3. Authorize the MCP connection.
4. Return automatically to the AI client.

The permissions available through MCP are associated with the authenticated CluedIn user.

---

# Claude

Claude supports remote MCP servers through **Custom Connectors**.

## Add CluedIn to Claude

1. Open Claude.

2. Go to:

   **Customize → Connectors**

3. Select the **+** button next to Connectors.

4. Select:

   **Add custom connector**

5. Enter a name for the connector, for example:

   ```text
   CluedIn
   ```

6. Enter your CluedIn MCP server URL:

   ```text
   https://<your-cluedin-instance>/api/mcp/server
   ```

   For example:

   ```text
   https://name.weu.saas.cluedin.com/api/mcp/server
   ```

7. You do **not** need to enter an OAuth Client ID or Client Secret in **Advanced settings**.

8. Select **Add**.

9. Select **Connect** when prompted.

10. Claude will redirect you to CluedIn.

11. Sign in to CluedIn and approve the connection.

12. Return to Claude once authentication completes.

CluedIn should now appear as a connected service.

## Using CluedIn in Claude

When starting a conversation, you can enable CluedIn from the connector controls in the chat.

You can then ask Claude to use the tools exposed by the CluedIn MCP server.

For example:

```text
Using CluedIn, find the records with the highest number of data quality issues.
```

Or:

```text
Use CluedIn to tell me what data is available for customers.
```

Or:

```text
Using CluedIn, investigate this customer and tell me what we know about them.
```

### Claude Team and Enterprise

For Claude Team and Enterprise environments, an **Owner or Primary Owner** might first need to add the connector for the organization.

The organization owner can go to:

**Organization settings → Connectors → Add → Custom → Web**

and enter the CluedIn MCP server URL.

Individual users can then connect their own CluedIn account using OAuth.

---

# ChatGPT

ChatGPT supports remote MCP servers through **custom apps / MCP connectors**.

Depending on your ChatGPT plan and workspace configuration, an administrator may first need to enable **Developer Mode**.

## Enable Developer Mode

If Developer Mode is not already available, a ChatGPT workspace administrator may need to enable it from:

**Workspace Settings → Permissions & Roles → Connected Data**

Enable the option for:

**Developer mode / Create custom MCP connectors**

Users who have access can then enable Developer Mode from:

**Settings → Apps → Advanced Settings**

> The exact options available depend on your ChatGPT plan and your organization's workspace policies.

## Add CluedIn to ChatGPT

1. Open ChatGPT.

2. Go to:

   **Settings → Apps**

3. Ensure **Developer Mode** is enabled.

4. Select:

   **Create**

5. Enter a name for the app, for example:

   ```text
   CluedIn
   ```

6. Enter your CluedIn MCP endpoint:

   ```text
   https://<your-cluedin-instance>/api/mcp/server
   ```

   For example:

   ```text
   https://name.weu.saas.cluedin.com/api/mcp/server
   ```

7. Select OAuth authentication if ChatGPT asks for the authentication mechanism.

   You do **not** need to manually provide a Client ID or Client Secret for the CluedIn MCP connection.

8. Select **Scan tools**.

ChatGPT will connect to the CluedIn MCP server and discover the tools that CluedIn makes available.

9. When the OAuth authentication window appears, sign in to CluedIn.
10. Approve the connection.
11. Return to ChatGPT.
12. Allow the tool scan to complete.
13. Select **Create**.

CluedIn should now appear as an available app in ChatGPT.

## Using CluedIn in ChatGPT

Start a new conversation and select **CluedIn** from the available Apps.

You can then ask ChatGPT to work directly with CluedIn.

For example:

```text
Use CluedIn to show me the data sources that are currently connected.
```

```text
Using CluedIn, investigate the data quality of our customer data.
```

```text
Ask CluedIn what information we have about Contoso.
```

```text
Using CluedIn, find potential duplicate customer records.
```

Depending on the tools made available by CluedIn, ChatGPT may ask for confirmation before performing operations that modify data.

---

# Microsoft Copilot

The simplest way to connect a remote MCP server to the Microsoft Copilot ecosystem is through **Microsoft Copilot Studio**.

Copilot Studio can add an existing MCP server as a tool for an agent.

## Add CluedIn to a Copilot Studio Agent

1. Open **Microsoft Copilot Studio**.

2. Open the agent that you want to connect to CluedIn.

3. Go to:

   **Tools**

4. Select:

   **Add a tool**

5. Select:

   **New tool**

6. Select:

   **Model Context Protocol**

The MCP onboarding wizard will open.

## Configure the MCP Server

Enter a server name such as:

```text
CluedIn
```

Enter a description, for example:

```text
Provides access to enterprise data, metadata, data quality, master data and other capabilities available through CluedIn.
```

For **Server URL**, enter:

```text
https://<your-cluedin-instance>/api/mcp/server
```

For example:

```text
https://name.weu.saas.cluedin.com/api/mcp/server
```

## Configure Authentication

For the authentication type, select:

**OAuth 2.0**

Where available, select:

**Dynamic discovery**

CluedIn supports OAuth discovery, so you should not need to manually provide a Client ID or Client Secret.

Continue through the wizard.

When Copilot establishes the connection, you will be asked to authenticate with CluedIn.

1. Select the option to create/connect the MCP connection.
2. Sign in to CluedIn.
3. Authenticate your account.
4. Approve the requested access.
5. Return to Copilot Studio.
6. Select **Add to agent**.

The tools exposed by the CluedIn MCP server will now be available to the agent.

## Using CluedIn from Copilot

Once the MCP server has been added to an agent, Copilot can select CluedIn tools when they are appropriate for the user's request.

For example:

```text
Check CluedIn and tell me whether we have any data quality problems with this customer.
```

```text
Use CluedIn to find everything we know about Contoso.
```

```text
Using CluedIn, identify potential duplicate records.
```

```text
Ask CluedIn which systems contributed data to this record.
```

The Copilot agent orchestrator uses the MCP server description and the descriptions of the tools provided by CluedIn to determine when CluedIn should be called.

---

# Finding Your CluedIn MCP URL

Your MCP URL is based on the URL of your CluedIn environment.

If your CluedIn URL is:

```text
https://name.weu.saas.cluedin.com
```

your MCP URL is:

```text
https://name.weu.saas.cluedin.com/api/mcp/server
```

If your CluedIn URL is:

```text
https://acme.eus.saas.cluedin.com
```

your MCP URL is:

```text
https://acme.eus.saas.cluedin.com/api/mcp/server
```

The rule is simply:

```text
<CluedIn URL> + /api/mcp/server
```

---

# Security and Permissions

Connections to the CluedIn MCP server are authenticated using OAuth.

This means:

* There is no need to share your CluedIn password with Claude, ChatGPT or Copilot.
* There is no need to copy a Client Secret into the AI application when OAuth discovery is supported.
* Each user authenticates using their own CluedIn identity.
* Access is associated with the authenticated user's permissions in CluedIn.
* Authentication tokens are used rather than repeatedly supplying usernames and passwords.
* Users can disconnect the integration from the relevant AI client if access is no longer required.

As with any AI integration, administrators should review which CluedIn capabilities and MCP tools are available before making the connection broadly available to users.

---

# Troubleshooting

## The MCP server cannot be found

Check that the URL ends with:

```text
/api/mcp/server
```

For example:

```text
https://name.weu.saas.cluedin.com/api/mcp/server
```

Do not use only the base CluedIn URL.

---

## I am being asked to authenticate

This is expected.

The CluedIn MCP server uses OAuth. The AI client will redirect you to authenticate with CluedIn before it can access the MCP tools.

---

## I am being asked for a Client ID or Client Secret

For the standard CluedIn MCP OAuth flow, these should not normally be required by clients that support MCP OAuth discovery.

For Claude, leave the optional Client ID and Client Secret fields empty.

For ChatGPT, allow the MCP authentication discovery process to complete when scanning the server.

For Copilot Studio, use:

**OAuth 2.0 → Dynamic discovery**

rather than manually configuring an OAuth Client ID and Client Secret.

---

## Authentication succeeds but I cannot perform an operation

The MCP connection operates using the permissions associated with your authenticated CluedIn account.

Check that your CluedIn user has permission to perform the requested operation.

---

## The connector works for one user but not another

MCP authentication is performed on behalf of the individual user.

Each user may therefore need to connect and authenticate their own CluedIn account, and the MCP tools available to them may be affected by their permissions within CluedIn.

---

# Quick Reference

| AI Platform       | Where to configure                                                   | MCP URL                            | Authentication                |
| ----------------- | -------------------------------------------------------------------- | ---------------------------------- | ----------------------------- |
| Claude            | Customize → Connectors → Add custom connector                        | `https://<cluedin>/api/mcp/server` | OAuth                         |
| ChatGPT           | Settings → Apps → Create                                             | `https://<cluedin>/api/mcp/server` | OAuth                         |
| Microsoft Copilot | Copilot Studio → Agent → Tools → Add a tool → Model Context Protocol | `https://<cluedin>/api/mcp/server` | OAuth 2.0 → Dynamic discovery |

No Client ID or Client Secret is required when using CluedIn's supported OAuth discovery flow.

---

# Example

For a CluedIn environment hosted at:

```text
https://name.weu.saas.cluedin.com
```

use the following MCP server address in Claude, ChatGPT or Copilot:

```text
https://name.weu.saas.cluedin.com/api/mcp/server
```

After adding the server, authenticate with your CluedIn account when redirected.

That's it — the AI client can now discover and use the capabilities that CluedIn exposes through MCP.

