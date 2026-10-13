---
title: API reference
url: https://documentation.cluedin.net/api
content_type: landing
section: Develop & APIs
---

# API reference

The CluedIn REST API is documented endpoint by endpoint across the categories listed below. Each category is its own page, with an interactive reference for just that subset of the API. Splitting the reference keeps each page fast even though the full API has more than 700 endpoints.

Before making requests, review [Get started](https://documentation.cluedin.net/api/get-started.md) for base URLs, authentication, and conventions that apply across the whole API.

## Try it out against your environment

Each category page (and the full-screen viewer) includes a connection bar at the top. Enter your environment's **base URL** (for example, `https://acme.cluedin.com`), your **email**, and your **password**, then select **Connect**. The viewer requests a bearer token on your behalf and attaches it to every request, which enables the **Try it out** button on every endpoint so you can send live calls and inspect the responses.

The token and base URL are held in your browser's session storage and shared across the category pages until you close the tab or select **Disconnect**. If your CluedIn organization name differs from the first part of the host, expand **Advanced** to set the **Client ID** explicitly.

> **Important:** The calls run from your browser, so the target environment must allow cross-origin (CORS) requests from wherever you are viewing this documentation. If a request is blocked, host the documentation on an allowed origin, or use the `curl`/PowerShell examples in [Get started](https://documentation.cluedin.net/api/get-started.md) instead. Credentials are sent only to the environment you specify and are never stored beyond the browser session.

## Categories

| Category | Description |
|---|---|
| [Access control & governance](https://documentation.cluedin.net/api/access-control-and-governance.md) | Access control policies, audit logs, ownership, and tag metadata. |
| [Entities](https://documentation.cluedin.net/api/entities.md) | Read, create, modify, merge, and inspect golden records. |
| [Search](https://documentation.cluedin.net/api/search.md) | Query the CluedIn graph and manage saved searches. |
| [Vocabularies](https://documentation.cluedin.net/api/vocabularies.md) | Manage vocabularies and vocabulary keys. |
| [Glossary](https://documentation.cluedin.net/api/glossary.md) | Manage glossary categories and terms. |
| [Hierarchies](https://documentation.cluedin.net/api/hierarchies.md) | Build and manage hierarchies and the global data model. |
| [Deduplication](https://documentation.cluedin.net/api/deduplication.md) | Deduplication projects, automation, match results, and entity split. |
| [Rules & evaluation](https://documentation.cluedin.net/api/rules-and-evaluation.md) | Manage rules, preview rule output, and inspect evaluation logs. |
| [Streams, connectors & export](https://documentation.cluedin.net/api/streams-and-export.md) | Configure, operate, and monitor export streams and connectors. |
| [Data preparation & enrichment](https://documentation.cluedin.net/api/data-preparation-and-enrichment.md) | Clean and enrich records. |
| [AI](https://documentation.cluedin.net/api/ai.md) | AI agents, jobs, skills, and Copilot. |
| [Administration & configuration](https://documentation.cluedin.net/api/administration-and-configuration.md) | Settings, logs, and metered billing. |
| [Organization](https://documentation.cluedin.net/api/organization.md) | Organization profile and usage statistics. |

## Download the specification

The full CluedIn OpenAPI specification is bundled with this documentation and can be downloaded directly. Per-category specifications are linked from each category page.

  [Download full swagger.json](https://documentation.cluedin.net/assets/api/swagger.json)

## In this section

- [Get started with the REST API](https://documentation.cluedin.net/api/get-started.md) (how-to): This page explains how to connect to the CluedIn REST API: base URLs, authentication, and the conventions that requests and responses follow.
- [Access control & governance](https://documentation.cluedin.net/api/access-control-and-governance.md) (reference): Access control policies, audit logs, entity ownership, and tag metadata.
- [Entities](https://documentation.cluedin.net/api/entities.md) (reference): Read, create, modify, merge, split, and inspect golden records and their metadata.
- [Search](https://documentation.cluedin.net/api/search.md) (reference): Query the CluedIn graph and manage saved searches.
- [Vocabularies](https://documentation.cluedin.net/api/vocabularies.md) (reference): Manage vocabularies and vocabulary keys.
- [Glossary](https://documentation.cluedin.net/api/glossary.md) (reference): Manage glossary categories and terms, and search the glossary.
- [Hierarchies](https://documentation.cluedin.net/api/hierarchies.md) (reference): Build and manage hierarchies and the global data model.
- [Deduplication](https://documentation.cluedin.net/api/deduplication.md) (reference): Find, review, and resolve duplicate records: deduplication projects, automation, match results, and entity split.
- [Rules & evaluation](https://documentation.cluedin.net/api/rules-and-evaluation.md) (reference): Manage data, survivorship, and golden record rules; preview rule output and inspect evaluation logs.
- [Streams, connectors & export](https://documentation.cluedin.net/api/streams-and-export.md) (reference): Configure, operate, and monitor export streams and the connectors they use.
- [Data preparation & enrichment](https://documentation.cluedin.net/api/data-preparation-and-enrichment.md) (reference): Clean and enrich records using built-in cleaning and enricher providers.
- [AI](https://documentation.cluedin.net/api/ai.md) (reference): AI agents, jobs, skills, and Copilot.
- [Administration & configuration](https://documentation.cluedin.net/api/administration-and-configuration.md) (reference): Settings, logs, and metered billing.
- [Organization](https://documentation.cluedin.net/api/organization.md) (reference): Organization profile and usage statistics.

Up: [Develop & APIs](https://documentation.cluedin.net/develop.md)
