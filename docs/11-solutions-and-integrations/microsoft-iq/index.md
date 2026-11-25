---
layout: cluedin
title: Microsoft IQ
parent: Solutions & integrations
nav_order: 45
has_children: true
permalink: /solutions/microsoft-iq
content_type: landing
summary: Publish CluedIn's mastered data into Microsoft IQ - Fabric IQ, Foundry IQ, Work IQ and Web IQ - so Microsoft 365 Copilot and AI agents ground on governed golden records.
---

## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

[Microsoft IQ](https://learn.microsoft.com/en-us/microsoft-iq/) is the intelligence layer that grounds Microsoft 365 Copilot and AI agents. CluedIn publishes its mastered data into each of the four IQ products:

| Product | What CluedIn publishes | Where it lands |
|--|--|--|
| [Fabric IQ](/solutions/microsoft-iq/fabric-iq) | The global data model: business domains, their vocabulary keys and relationships, through the existing **Sync with Microsoft Fabric Ontology** | A Fabric IQ **ontology** in a Fabric workspace |
| [Foundry IQ](/solutions/microsoft-iq/foundry-iq) | Golden records | An Azure AI Search index, a **knowledge source** over it, and a **knowledge base** agents connect to |
| [Work IQ](/solutions/microsoft-iq/work-iq) | Golden records | A **Microsoft 365 Copilot connector**, so Microsoft 365 Copilot and Work IQ agents can answer questions about them |
| [Web IQ](/solutions/microsoft-iq/web-iq) | The websites held on golden records | A named Web IQ **scope**, so web grounding can be restricted to, for example, your suppliers' own sites |

Fabric IQ is the existing global data model to Fabric ontology sync, managed as a Microsoft IQ connection. It reuses an existing Microsoft Fabric connection, so it needs no credentials of its own.

## How it works

Each target is a **Microsoft IQ connection**: the product, the credentials, the target resource names and what to publish. A connection can publish on demand or on a schedule.

- **Credentials** are a Microsoft Entra ID app registration (tenant ID, client ID and client secret), the same pattern as the Microsoft Fabric connection. Foundry IQ can use a search admin API key instead. Secrets are stored encrypted and are never returned by the API.
- **What to publish** is a list of business domains (entity types, for example `/Organization`). Leave it empty to publish every business domain. `maxRecords` caps how many golden records one run publishes (10,000 by default).
- **Every connection is checked against Microsoft** when it's created or updated, so a wrong secret, a missing permission or an unreachable endpoint is reported straight away.
- **Re-publishing is safe.** Records are keyed by their CluedIn golden record id, so a later run updates them in place, and ontology elements keep their identity across runs.

{: .important }
CluedIn's access control policies don't travel with the data. Anyone who can use the target in Microsoft 365 or Foundry can see what you publish, so choose the business domains deliberately. Work IQ connections can be limited to one Microsoft Entra group.

## Manage connections

Go to **Administration** > **Azure Integration** > **Microsoft IQ**. You need the **Consume > Export Targets** claim.

- **Add connection** opens a panel. Choose the product, fill in its settings, and select **Preview** to see what a publish would send, built from your current data. Nothing is sent to Microsoft until you select **Create connection**, which checks the settings with Microsoft first. If they're rejected, the reason appears next to the button.
- The list shows each connection's status (**Published**, **Failed**, **Pending** or **Not run yet**), its schedule, and the result of its last run.
- Each row's actions are **Publish now**, **Test connection**, **Edit** and **Delete**. When you edit a connection, leave a secret empty to keep the stored one.

### API

The same operations are available through the CluedIn API, under `https://<your CluedIn host>/api/api/microsoft-iq`. Call it with a CluedIn API token or a user token that has the **Consume > Export Targets** claim.

| Request | What it does |
|--|--|
| `POST /preview` | Shows exactly what a publish would send, built from your live data, without credentials and without calling Microsoft. Start here. |
| `POST /connections` | Creates a connection after checking it against Microsoft. |
| `GET /connections`, `GET /connections/{id}` | Lists connections, with the outcome of each one's last publish. |
| `PUT /connections/{id}` | Changes a connection. Omitted secrets keep their stored values. |
| `GET /connections/{id}/preview` | Shows what publishing this connection would send. |
| `POST /connections/{id}/test` | Checks the credentials and target again. |
| `POST /connections/{id}/publish` | Publishes now. The response carries the outcome in `lastResult` or `lastError`. |
| `DELETE /connections/{id}` | Deletes the connection and its schedule. What was already published stays in Microsoft IQ. |
| `POST /connections/{id}/web-iq-search` | Web IQ only: runs a real Web IQ search restricted to the published scope. |

To publish on a schedule, set `cronSchedule` (for example `0 2 * * *` for 02:00 every day) and `enabled: true`.

These fields apply to every connection:

| Field | Description |
|--|--|
| `name` | A friendly name. |
| `product` | `FabricIQ`, `FoundryIQ`, `WorkIQ` or `WebIQ`. Can't be changed later. |
| `tenantId`, `clientId`, `clientSecret` | The Microsoft Entra ID app registration. Not used by Fabric IQ. |
| `entityTypes` | The business domains to publish, for example `["/Organization"]`. Empty publishes all of them. Fabric IQ always publishes the whole global data model. |
| `maxRecords` | The most golden records one run publishes. |
| `cronSchedule`, `enabled` | The publish schedule. |

The product pages list the fields each product needs, the permissions to grant, and a step-by-step validation with the results to expect.

## Copilot web search through Web IQ

CluedIn Copilot and AI agents can search the live web for information that isn't in CluedIn. Microsoft retired the Bing Search APIs in August 2025, and Web IQ is the replacement. To use it, set **Microsoft Web IQ API Key** under **Administration** > **Azure Integration** > **Copilot**, using an API key from [Profile Management](https://webiq.microsoft.ai/profiles) in the Web IQ portal. When it's set, it takes precedence over a Bing Search API key.
