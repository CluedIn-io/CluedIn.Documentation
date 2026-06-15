---
layout: cluedin
title: REST API
nav_order: 105
has_children: true
permalink: /rest-api
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

CluedIn exposes a comprehensive REST API that lets external systems, scripts, and applications interact with the platform programmatically. In practice, anything you can do in the CluedIn UI—working with entities, rules, streams, vocabularies, the glossary, data sources, and administration—can also be done through the API.

The API is described by an **OpenAPI 3.0** specification that contains more than **1,000 endpoints** grouped into approximately 120 functional areas. You can download the full specification from this site, or browse it by category in the [API reference](/rest-api/api-reference).

<p>
  <a class="btn btn-primary" href="{{ '/assets/api/swagger.json' | relative_url }}" download>Download swagger.json</a>
</p>

## In this section

| Page | Description |
|---|---|
| [Get started](/rest-api/get-started) | Base URLs, authentication, request and response conventions, and code examples. |
| [API reference](/rest-api/api-reference) | Interactive, browsable reference for every endpoint, generated from the OpenAPI specification. |

## API at a glance

| | |
|---|---|
| Specification | OpenAPI 3.0 |
| Base path | `/api` (and versioned paths such as `/api/v1`) |
| Authentication | Bearer token (CluedIn API token) |
| Request and response format | JSON |
| Endpoints | 1,000+ across ~120 functional areas |

## Functional areas

The endpoints are organized by tag. Some of the most frequently used areas include the following.

| Area | Typical use |
|---|---|
| Entity, EntityInfo, EntityModification | Read, create, and modify golden records. |
| Search, SavedSearch, SuggestedSearch | Query the CluedIn graph and manage saved searches. |
| Vocabulary, VocabularyUsage | Manage vocabularies and vocabulary keys. |
| Rules, RuleDataPreview | Manage and preview data, survivorship, and golden record rules. |
| Streams, StreamMappings | Configure and operate export streams. |
| Glossary, GlossarySearch | Manage glossary categories and terms. |
| DataSource, Import, Export | Manage data sources and data ingestion or extraction. |
| Hierarchies | Build and manage hierarchies. |
| Organization, AdminCommands, Configuration | Administration and operational commands. |

For the complete list of areas and every available endpoint, see the [API reference](/rest-api/api-reference).
