---
layout: cluedin
title: Ongoing REST API Audit
parent: REST API
permalink: /rest-api/api-audit
nav_order: 30
tags: ["api-audit", "rest api audit"]
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}


# CluedIn REST API Documentation Audit (re-audit)

> **Scope:** Customer-facing re-audit of the CluedIn C# / ASP.NET Web API as it is now
> rendered in the docs (`assets/api/swagger.json` → `assets/api/categories/*.json`,
> surfaced under `docs/250-rest-api/020-api-reference/`).
> **Source verified against:** the application code at
> `C:\Users\AleksandarKovacevic\source\repos\CluedIn` (controller classes, route
> attributes, and `[Authorize]` / `[RaciAuthorize]` / `[AllowAnonymous]` / `[ApiExplorerSettings]`).
> **No application code was modified.**
>
> **What changed since the first audit:** all 59 `[Obsolete]` operations (Insight, CluedInClean v1,
> Search `subscribe`/`count`/`clear`, deprecated Entity-history reads, `Configuration/inactiveproviders`,
> `Organization/v2/duplicates`, Connector `datatypes`) were removed from the spec first. This file then
> covered the 1,176 live operations across 116 controllers (swagger tags) that remained, grouped by the
> 16 documentation categories.
>
> **✅ Action taken (this pass):** every controller marked **Exclude** below, plus the auth red-flag
> controllers and the loose ends (`DataverseConnector`, `PowerAutomate`), have now been **removed
> from the published spec**. The reference is down to **721 operations across 48 controllers (swagger
> tags) in 13 categories**: the *System & health*, *Data ingestion*, *Workflow & automation*, and
> *Insights & UI* categories were dropped entirely, and a standalone *Deduplication* category was split
> out of Entities, Rules, Workflow, and Insights. The **Document** and **Document (admin)** tables below
> describe what remains.

---

Each controller gets one of three verdicts:

| Verdict | Meaning | Doc action |
|---|---|---|
| **Document** | Core product surface a customer uses directly. | Keep, document as a first-class API. |
| **Document (admin)** | Real customer feature, but tenant-**admin** setup/config or a diagnostic/power-user tool. | Keep, but place in an "Administration" / "Diagnostics" sub-section with a role note. |
| **Exclude** | Operator/infra/internal-UI/debug — not a usable customer API. | Drop from the public reference (or move behind an "internal" filter). |

---

## Category-by-category verdict

### 1. System & health — *Exclude the whole category*

| Controller | Auth | Purpose | Verdict |
|---|---|---|---|
| Status, HealthLiveness, HealthReadiness | anonymous | Service/K8s liveness & readiness probes | **Exclude** — infra/ops. |
| DefaultRedirect | anonymous (catch-all) | 404 fallback for unmatched routes | **Exclude** — infra. |
| RobotsTxt | anonymous | Serves `robots.txt` | **Exclude** — infra. |

### 2. Access control & governance — *mostly Document*

| Controller | Auth | Purpose | Verdict |
|---|---|---|---|
| AccessControlPolicies | `Management.AccessControl` | CRUD + activate access-control policies | **Document (admin)** — tenant governance config. |
| GDPRAnonymization | `Governance.PersonalIdentifiers` | Anonymize / de-anonymize PII | **Exclude** — compliance feature. |
| GDPRPII | `Governance.PersonalIdentifiers` | Query PII identifiers & metrics | **Exclude** — compliance feature. |
| AuditLog | `[Authorize]` (per-area filtered) | Read audit logs | **Document** — compliance/monitoring. |
| Ownership | `AnyClaimRaciLevel` (≥ Consultant) | Manage object ownership | **Document** — governance. |
| TagMetadata | `Governance.Tags` | Tag metadata & folders | **Document** — governance. |

### 3. Entities — *core; trim the admin/internal pieces*

| Controller | Auth | Purpose | Verdict |
|---|---|---|---|
| Entity | `[Authorize]` | Core get/search/modify golden records | **Document** — flagship API. |
| EntityHistory | `[Authorize]` | Entity change history | **Document**. |
| EntityInfo / EntityTypeInfo | `[Authorize]` | Entity-type metadata / schema discovery | **Document**. |
| EntityOrigin / EntitySource | `[Authorize]` | Lineage & provenance | **Document**. |
| EntityTopology | `[Authorize]` | Relationship/topology graph | **Document**. |
| EntityModification | `Administration.Data` | Edit properties/edges (UI workflows) | **Document (admin)**. |
| EntityDataDeletion | `Administration.Data` | Bulk delete by provider/source/correlation | **Document (admin)** — destructive. |
| EntityActions | **no auth attribute** ⚠ | Run/list bulk rule actions on entities | **Exclude** — *confirm auth first*. |
| AdminEntity | `Roles = Admin`, `/api/admin/*` | Raw entity-blob / search-store debugging | **Exclude** — operator debug. |
| IdentityCounter | `[Authorize]` | Identity-counter plumbing for data generation | **Exclude** — internal. |

### 4. Search — *Document the search surface, drop the helpers*

| Controller | Auth | Purpose | Verdict |
|---|---|---|---|
| Search | `[Authorize]` (IdentityServer) | Query the CluedIn graph + index | **Document** — primary read API. |
| SavedSearch | `[Authorize]` | CRUD saved & favorite searches | **Document**. |
| SuggestedSearch | `[Authorize]` | Typeahead / suggestion | **Exclude**. |
| RulesAutoComplete | `[Authorize]` | Autocomplete values for the rule builder | **Exclude** — internal UI helper. |
| SearchToClean | `Preparation.Clean` | Debug query-translator comparison — *"DO NOT USE IN PRODUCTION"* | **Exclude** — debug-only. |

### 5. Vocabularies — *Document the model, drop maintenance*

| Controller | Auth | Purpose | Verdict |
|---|---|---|---|
| Vocabulary | `Management.DataCatalog` | CRUD vocabularies & keys, lineage | **Document** — core modelling. |
| VocabularyUsage | `Management.DataCatalog` | Key/vocab usage & impact analysis | **Document**. |
| StrongTyping | `[Authorize]` | Trigger strong-typing reindex upgrade | **Exclude** — maintenance job. |

### 6. Glossary — *Document both*

| Controller | Auth | Purpose | Verdict |
|---|---|---|---|
| Glossary | `Management.Glossary` | CRUD terms/categories/tags/lexicons | **Document**. |
| GlossarySearch | `Management.Glossary` | Glossary entities, metrics, lineage, analytics | **Document**. |

### 7. Hierarchies — *Document*

| Controller | Auth | Purpose | Verdict |
|---|---|---|---|
| Hierarchies | `Management.Hierarchies` | Build/publish/clone/export hierarchies | **Document**. |
| GlobalDataModel | `Administration.EntityTypes` | Global entity-relationship schema | **Document (admin)** — schema-level. |

### 8. Deduplication - *Document*

| Controller | Auth | Purpose | Verdict |
|---|---|---|---|
| Rules (Deduplication) | `Management.DeduplicationManagement` | Matching rules within dedup projects | **Document** — *disambiguate from the rule builder*. |
| Automate (Dedup) | `Management.DeduplicationManagement` | Run/cancel dedup automation | **Document**. |
| Project | `Management.DeduplicationManagement` | Dedup projects | **Document** — dedup. |
| Results | `Management.DeduplicationReview` | Dedup match-group review | **Document** — dedup. |
| SplitEntity | `[Authorize]` | Topology support for splitting data parts | **Document**. |
| DuplicateEntities | `Management.Duplicates` | Query potential duplicates | **Document** — dedup. |


### 9. Rules & evaluation — *Document the builder; gate the rest*

| Controller | Auth | Purpose | Verdict |
|---|---|---|---|
| Rules (Management) | `Management.RuleBuilder` | Processing rule CRUD + lifecycle | **Document** — rule builder. |
| RuleDataPreview | `Management.RuleBuilder` | Preview rule output | **Document** — supports the builder. |
| RuleErrorLog | `Management.RuleBuilder` | Rule execution error logs | **Document (admin)** — diagnostic. |
| ExplainLog | `Administration.Data` | Trace processing/property changes | **Document (admin)** — diagnostic. |
| Evaluation (PowerFx) | **no auth attribute** ⚠ | Evaluate PowerFx expressions | **Exclude** — internal formula-bar; *flag missing auth*. |

### 10. Data ingestion — *Document the ingestion/jobs; drop the admin/crawler ops*

| Controller | Auth | Purpose | Verdict |
|---|---|---|---|
| Integration | `[Authorize]` (+anon icon) | List connectors / provider metadata | **Exclude** — integration discovery. |
| Blob | `[Authorize]` | Serve stored blobs (images/reports) | **Exclude**. |
| Job | `[Authorize]` | Monitor agent job queues | **Exclude**. |
| DistributedJobs | `[Authorize]` | Job progress & cancel | **Exclude**. |
| OrganizationUpload | **no auth attribute** ⚠ | CSV upload to org blob store | **Exclude** — *confirm auth first*. |
| Import | `Administration.Tenant` | Import tenant data from ZIP | **Exclude** — migration. |
| OrganizationDataRemoval | `Administration.Provider` | Reset provider crawl state | **Exclude**. |
| Onboarding | `[Authorize]` | Most-connected-entity onboarding widget | **Exclude** — UI helper. |
| DataSource | `Roles = Admin` | Datasource upgrade checker | **Exclude** — internal. |
| AdminCrawler, OrganizationAdminCrawler | `Administration.Provider` | Recrawl / re-run all providers | **Exclude** — operator. |
| AdminDistributedJobs | `Roles = Admin` | Stale distributed-job maintenance | **Exclude** — operator. |
| AdminDeadLetterQueue | `Administration.Messaging` | Reprocess dead-letter messages | **Exclude** — operator. |

### 11. Streams, connectors & export — *Document the Consume surface; gate export*

| Controller | Auth | Purpose | Verdict |
|---|---|---|---|
| Streams | `Consume.Streams` | Stream lifecycle | **Document** — core Consume. |
| StreamMappings | `Consume.Streams` | Stream field mappings | **Document**. |
| StreamIngestionLog | `Consume.Streams` | Per-entity ingestion audit | **Document**. |
| StreamLog | `Consume.Streams` | Stream operation/diagnostic logs | **Document (admin)** — diagnostic. |
| StreamsVocabularyKeyUsage | `Consume.Streams` | Vocab keys used in stream filters | **Document**. |
| Connector | `Consume.ExportTargets` | Connector/container management | **Document** — core Consume. |
| ConnectorHealth | `Consume.ExportTargets` | Connector health status | **Document**. |
| DataverseConnector | *(controller not found in main tree)* ⚠ | Dataverse export integration (4 POST) | **Exclude** — *locate source & confirm*. |
| Export | `Administration.Tenant` | Export vocab/entity data to ZIP | **Exclude** — migration. |

### 12. Data preparation & enrichment — *Document Clean & Enricher*

| Controller | Auth | Purpose | Verdict |
|---|---|---|---|
| Clean (v2) | `Preparation.Clean` | Data-cleaning project lifecycle | **Document**. |
| Enricher | `Integrations.Enrichment` (+anon icon) | Configure/trigger enrichers | **Document**. |
| ExternalFeature | `[Authorize]` | External/dynamic UI feature URLs | **Exclude** — *confirm it's a real API, not UI glue*. |
| Enrichers | `[Authorize]` | Enricher software upgrade check | **Exclude** — maintenance. |

### 12. Workflow & automation — *Exclude tasks/flows; gate governance & internal*

| Controller | Auth | Purpose | Verdict |
|---|---|---|---|
| EnterpriseFlows | `Management.WorkflowBuilder` | Workflow templates / execution | **Exclude**. |
| Task | `[Authorize]` | User tasks & details | **Exclude**. |
| TaskApproval | `[Authorize]` | Approve/reject tasks | **Exclude**. |
| TaskRoleRequest | `[Authorize]` | Role-request tasks | **Exclude**. |
| ApprovalItem | `[Authorize]` | Batch approval processing | **Exclude**. |
| PowerAutomate | (in EntityModification) | Power Automate integration actions | **Exclude** — *confirm as a published integration*. |
| MeshCenter | `Preparation.MeshCenter` | GDPR mesh commands / deletion requests | **Exclude** — governance. |
| MeshProcessor | `[Authorize]`, internal | "Can entity accept mesh command" helper | **Exclude** — internal. |

### 13. AI — *Document product AI; gate platform/infra config*

| Controller | Auth | Purpose | Verdict |
|---|---|---|---|
| AIAgent | `Management.AiAgents` | CRUD AI agents | **Document**. |
| AiJob | `Management.AiAgents` | AI job execution & skills | **Document**. |
| AiJobSkill | `[Authorize]` | List AI skills | **Document**. |
| AiEndpoint (inference) | `[Authorize]` | Text/chat completions | **Exclude**. |
| AiPlatformDefinition | `[Authorize]` (+anon logo) | AI platform catalog | **Exclude**. |
| Copilot | `[Authorize]` | Copilot chat sessions | **Document**. |
| AiEndpoint (admin), AiDeployment, AiPlatform | `Administration.ArtificialIntelligence` | Configure AI endpoints/deployments/platforms | **Exclude** — tenant AI setup. |
| LanguageServer (PowerFx) | **no auth attribute** ⚠ | LSP intellisense for formula bar | **Exclude** — IDE/UI plumbing. |

### 14. Administration & configuration — *mostly Exclude*

| Controller | Auth | Purpose | Verdict |
|---|---|---|---|
| Setting | `[Authorize]` | User/org key-value settings | **Document**. |
| MeteredBilling | `[Authorize]` | Consumption/billing measurements | **Document**. |
| ExtendedConfiguration | `[Authorize]` | Resolve dynamic provider-config options | **Exclude** — provider setup. |
| Configuration | `Engine.ConfigurationGroups` | List configuration groups | **Exclude** — *confirm; may be internal*. |
| Log | `Roles = OrganizationalAdmin` | Stream org logs (live) | **Document (admin)** — diagnostic. |
| AdminClusterSettings | `Roles = Admin` | Cluster logging/config overrides | **Exclude** — operator. |
| AdminCommands | `Roles = Admin` | System maintenance commands (84 ops) | **Exclude** — operator. |
| AdminIndexCommands | `Administration.Data` | Full index remap/reindex | **Exclude** — operator. |
| Logging | `[Authorize]` | Sink for browser/client logs | **Exclude** — UI plumbing. |

### 15. Organization — *Document provider/profile; gate admin commands*

| Controller | Auth | Purpose | Verdict |
|---|---|---|---|
| Organization | `[Authorize]` | Org usage statistics | **Document**. |
| OrganizationProfile | `[Authorize]` (+`Administration.Tenant`) | Tenant profile/branding | **Document**. |
| OrganizationGetProviders | `[Authorize]` | List/inventory providers | **Exclude**. |
| OrganizationProviderStatus | `Administration.Provider` | Enable/disable a provider | **Exclude**. |
| OrganizationAddProviders | **no class auth** ⚠ | Add a provider | **Exclude** — *confirm auth first*. |
| OrganizationUpdateProviders | **no class auth** ⚠ | Update a provider | **Exclude** — *confirm auth first*. |
| OrganizationEnableProviders | **no class auth** ⚠ | Enable a provider | **Exclude** — *confirm auth first*. |
| OrganizationTeamBroadcast | **no class auth** ⚠ | Email teammates to add a provider | **Exclude** — *confirm auth first*. |
| OrganizationAdminCommands | `Administration.Data` | External-search / reprocess commands | **Exclude** — operator. |

### 16. Insights & UI — *mostly Exclude (UI plumbing)*

| Controller | Auth | Purpose | Verdict |
|---|---|---|---|
| Activities | `[Authorize]` | Activity feed / action events | **Exclude**. |
| Notification | `[Authorize]` | User/provider notifications | **Exclude**. |
| Profile | `[Authorize]` | Current-user profile | **Exclude**. |
| Person | `[Authorize]` | Person lookup by entity code | **Exclude**. |
| PageTemplate / PageTemplateEntities | `Administration.Tenant` | Page/layout template config | **Exclude** — UI configuration. |
| GenericWidget | `[Authorize]` | Dashboard widget data | **Exclude** — UI plumbing. |
| WidgetQuery | `[Authorize]` | Widget entity queries | **Exclude** — UI plumbing. |
| LayoutTemplate | `[Authorize]` | UI layout templates | **Exclude** — UI plumbing. |
| NotificationV2 | **no auth attribute** ⚠ | Post AlertManager notification to service bus | **Exclude** — internal alerting. |

---
