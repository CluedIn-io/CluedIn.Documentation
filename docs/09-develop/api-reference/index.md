---
layout: cluedin
title: API reference
parent: Develop & APIs
nav_order: 40
has_children: true
permalink: /api
content_type: landing
summary: The REST API is generated from CluedIn's OpenAPI specification and covers more than a thousand endpoints, grouped below by the part of the product they act on.
list_children: false
redirect_from: ["/rest-api/api-reference", "/rest-api"]
source_path: docs/250-rest-api/020-api-reference.md
tags: ["api", "rest api"]
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

The CluedIn REST API is documented endpoint by endpoint across the categories listed below. Each category is its own page, with an interactive reference for just that subset of the API. Splitting the reference keeps each page fast even though the full API has more than 700 endpoints.

Before making requests, review [Get started](/api/get-started) for base URLs, authentication, and conventions that apply across the whole API.

## Try it out against your environment

Each category page (and the full-screen viewer) includes a connection bar at the top. Enter your environment's **base URL** (for example, `https://acme.cluedin.com`), your **email**, and your **password**, then select **Connect**. The viewer requests a bearer token on your behalf and attaches it to every request, which enables the **Try it out** button on every endpoint so you can send live calls and inspect the responses.

The token and base URL are held in your browser's session storage and shared across the category pages until you close the tab or select **Disconnect**. If your CluedIn organization name differs from the first part of the host, expand **Advanced** to set the **Client ID** explicitly.

{:.important}
The calls run from your browser, so the target environment must allow cross-origin (CORS) requests from wherever you are viewing this documentation. If a request is blocked, host the documentation on an allowed origin, or use the `curl`/PowerShell examples in [Get started](/api/get-started) instead. Credentials are sent only to the environment you specify and are never stored beyond the browser session.

## Categories

| Category | Description |
|---|---|
| [Access control & governance](/api/access-control-and-governance) | Access control policies, audit logs, ownership, and tag metadata. |
| [Entities](/api/entities) | Read, create, modify, merge, and inspect golden records. |
| [Search](/api/search) | Query the CluedIn graph and manage saved searches. |
| [Vocabularies](/api/vocabularies) | Manage vocabularies and vocabulary keys. |
| [Glossary](/api/glossary) | Manage glossary categories and terms. |
| [Hierarchies](/api/hierarchies) | Build and manage hierarchies and the global data model. |
| [Deduplication](/api/deduplication) | Deduplication projects, automation, match results, and entity split. |
| [Rules & evaluation](/api/rules-and-evaluation) | Manage rules, preview rule output, and inspect evaluation logs. |
| [Streams, connectors & export](/api/streams-and-export) | Configure, operate, and monitor export streams and connectors. |
| [Data preparation & enrichment](/api/data-preparation-and-enrichment) | Clean and enrich records. |
| [AI](/api/ai) | AI agents, jobs, skills, and Copilot. |
| [Administration & configuration](/api/administration-and-configuration) | Settings, logs, and metered billing. |
| [Organization](/api/organization) | Organization profile and usage statistics. |

## Download the specification

The full CluedIn OpenAPI specification is bundled with this documentation and can be downloaded directly. Per-category specifications are linked from each category page.

<p>
  <a class="btn btn-primary" href="{{ '/assets/api/swagger.json' | relative_url }}" download>Download full swagger.json</a>
</p>

