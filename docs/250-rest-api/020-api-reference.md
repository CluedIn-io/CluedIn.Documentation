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

The CluedIn REST API is documented endpoint by endpoint across the categories listed below. Each category is its own page, with an interactive reference for just that subset of the API. Splitting the reference keeps each page fast even though the full API has more than 1,000 endpoints.

Before making requests, review [Get started](/rest-api/get-started) for base URLs, authentication, and conventions that apply across the whole API.

## Categories

| Category | Description |
|---|---|
| [System & health](/rest-api/api-reference/system) | Status, health, and platform-level endpoints. |
| [Access control & governance](/rest-api/api-reference/access-control-and-governance) | Access control policies, audit logs, GDPR operations, and ownership. |
| [Entities](/rest-api/api-reference/entities) | Read, create, modify, merge, split, and inspect golden records. |
| [Search](/rest-api/api-reference/search) | Query the CluedIn graph and manage saved, suggested, and autocomplete searches. |
| [Vocabularies](/rest-api/api-reference/vocabularies) | Manage vocabularies, vocabulary keys, and strong typing. |
| [Glossary](/rest-api/api-reference/glossary) | Manage glossary categories and terms. |
| [Hierarchies](/rest-api/api-reference/hierarchies) | Build and manage hierarchies and the global data model. |
| [Rules & evaluation](/rest-api/api-reference/rules-and-evaluation) | Manage rules, preview rule output, and inspect evaluation logs. |
| [Data ingestion](/rest-api/api-reference/data-ingestion) | Data sources, file uploads, onboarding, jobs, and crawlers. |
| [Streams, connectors & export](/rest-api/api-reference/streams-and-export) | Configure, operate, and monitor export streams and connectors. |
| [Data preparation & enrichment](/rest-api/api-reference/data-preparation-and-enrichment) | Clean and enrich records. |
| [Workflow & automation](/rest-api/api-reference/workflow-and-automation) | Tasks, approvals, automation flows, and the processing mesh. |
| [AI](/rest-api/api-reference/ai) | AI agents, jobs, skills, endpoints, deployments, and Copilot. |
| [Administration & configuration](/rest-api/api-reference/administration-and-configuration) | Cluster settings, admin commands, configuration, logging, and metered billing. |
| [Organization](/rest-api/api-reference/organization) | Organization profile, provider configuration, and team broadcasts. |
| [Insights & UI](/rest-api/api-reference/insights-and-ui) | Insights, widgets, page templates, notifications, and other UI-related endpoints. |

## Download the specification

The full CluedIn OpenAPI specification is bundled with this documentation and can be downloaded directly. Per-category specifications are linked from each category page.

<p>
  <a class="btn btn-primary" href="{{ '/assets/api/swagger.json' | relative_url }}" download>Download full swagger.json</a>
</p>

## Keeping the reference up to date

This documentation renders a point-in-time snapshot of the OpenAPI specification (`assets/api/swagger.json`). It is not refreshed automatically. To update it after the API changes:

1. Download the current specification from a CluedIn environment:

   ```
   https://<organization>.<domain>/api/swagger/v1/swagger.json
   ```

2. Replace `assets/api/swagger.json` with the downloaded file.

3. Regenerate the per-category sub-specifications by running the splitter inside the running Docker container:

   ```
   docker exec cluedin-docs node /srv/jekyll/_tools/split-spec.js
   ```

   The splitter rewrites every file in `assets/api/categories/`.

4. Commit the changes. The reference picks them up on the next site build.
