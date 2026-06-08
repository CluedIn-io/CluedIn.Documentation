---
layout: cluedin
title: API reference
parent: REST API
permalink: /rest-api/api-reference
nav_order: 20
has_children: true
tags: ["api", "rest api"]
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

The CluedIn REST API is documented endpoint by endpoint across the categories listed below. Each category is its own page, with an interactive reference for just that subset of the API. Splitting the reference keeps each page fast even though the full API has more than 900 endpoints.

Before making requests, review [Get started](/rest-api/get-started) for base URLs, authentication, and conventions that apply across the whole API.

## Try it out against your environment

Each category page (and the full-screen viewer) includes a connection bar at the top. Enter your environment's **base URL** (for example, `https://acme.cluedin.com`), your **email**, and your **password**, then select **Connect**. The viewer requests a bearer token on your behalf and attaches it to every request, which enables the **Try it out** button on every endpoint so you can send live calls and inspect the responses.

The token and base URL are held in your browser's session storage and shared across the category pages until you close the tab or select **Disconnect**. If your CluedIn organization name differs from the first part of the host, expand **Advanced** to set the **Client ID** explicitly.

{:.important}
The calls run from your browser, so the target environment must allow cross-origin (CORS) requests from wherever you are viewing this documentation. If a request is blocked, host the documentation on an allowed origin, or use the `curl`/PowerShell examples in [Get started](/rest-api/get-started) instead. Credentials are sent only to the environment you specify and are never stored beyond the browser session.

## Categories

| Category | Description |
|---|---|
| [Access control & governance](/rest-api/api-reference/access-control-and-governance) | Access control policies, audit logs, GDPR operations, and ownership. |
| [Entities](/rest-api/api-reference/entities) | Read, create, modify, merge, split, and inspect golden records. |
| [Search](/rest-api/api-reference/search) | Query the CluedIn graph and manage saved and suggested searches. |
| [Vocabularies](/rest-api/api-reference/vocabularies) | Manage vocabularies and vocabulary keys. |
| [Glossary](/rest-api/api-reference/glossary) | Manage glossary categories and terms. |
| [Hierarchies](/rest-api/api-reference/hierarchies) | Build and manage hierarchies and the global data model. |
| [Rules & evaluation](/rest-api/api-reference/rules-and-evaluation) | Manage rules, preview rule output, and inspect evaluation logs. |
| [Data ingestion](/rest-api/api-reference/data-ingestion) | File uploads, imports, integrations, and jobs. |
| [Streams, connectors & export](/rest-api/api-reference/streams-and-export) | Configure, operate, and monitor export streams and connectors. |
| [Data preparation & enrichment](/rest-api/api-reference/data-preparation-and-enrichment) | Clean and enrich records. |
| [Workflow & automation](/rest-api/api-reference/workflow-and-automation) | Tasks, approvals, automation flows, and the processing mesh. |
| [AI](/rest-api/api-reference/ai) | AI agents, jobs, skills, endpoints, deployments, and Copilot. |
| [Administration & configuration](/rest-api/api-reference/administration-and-configuration) | Configuration, settings, logs, and metered billing. |
| [Organization](/rest-api/api-reference/organization) | Organization profile and provider configuration. |
| [Insights & UI](/rest-api/api-reference/insights-and-ui) | Page templates, notifications, profiles, activities, and other UI-related endpoints. |

## Download the specification

The full CluedIn OpenAPI specification is bundled with this documentation and can be downloaded directly. Per-category specifications are linked from each category page.

<p>
  <a class="btn btn-primary" href="{{ '/assets/api/swagger.json' | relative_url }}" download>Download full swagger.json</a>
</p>

