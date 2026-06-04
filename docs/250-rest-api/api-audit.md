# CluedIn REST API Documentation Audit

> **Scope:** Documentation-discovery audit of the CluedIn C# / ASP.NET Web API codebase
> (`C:\Users\AleksandarKovacevic\source\repos\CluedIn`).
> **Goal:** Identify which API controllers/endpoints should be included in public/product documentation.
>
> **Methodology & caveat:** All 173 `*Controller.cs` classes were swept for route attributes, HTTP verbs,
> and `[Authorize]` / `[RaciAuthorize]` / `[AllowAnonymous]` decorators. The Search, Rules, and Glossary
> controllers were read in full detail. For very large controllers (e.g. `EntityController`,
> `AdminCommandsController`, with 50+ actions each), routes are summarized at the prefix level.
> **No application code was modified.** "Document" uses a default-deny stance: a controller is only
> recommended for docs if it is genuinely product/customer-facing.

---

## Part 0 — GraphQL is the primary query mechanism (document first)

Of all 173 controllers, **only two actually execute GraphQL** — and they *are* the
GraphQL endpoints:

| Controller | Route | Notes |
|---|---|---|
| `PublicApiGraphQLController` | `POST api/v1/graphql` | Public GraphQL API |
| `Consume/GraphQLController`  | `POST api/graphql`    | Internal / UI GraphQL |

Both call `CluedInGraphQLExecuter.ExecuteAsync(...)` against one shared schema
(`Core.GraphQL/CluedInQuery.cs`) exposing `me`, `entity`, `latest`, `upcoming`, and
`search`. Other controllers (e.g. `RuleDataPreviewController`, `SearchController.v3`)
only *import* GraphQL types (`ExecutionError`, `PagingCursor`, `EntityBase`) for
serialization — they do **not** run queries.

**Implication for docs:** GraphQL is the product's primary read/query path, so the
GraphQL endpoint (query shape, auth, the `search`/`entity` root fields) should be
documented **first / with highest priority**, ahead of the equivalent REST reads.
The accompanying API tester (`_tools/api-tester/`) runs the GraphQL-backed surface
first for the same reason.

---

## Part 1 — Priority areas: Search, Rules, Glossary

| Controller | Endpoint / Route | Purpose | Recommendation | Reason |
|---|---|---|---|---|
| **SearchController** | `GET api/search`, `api/v1/search`, `/suggest`, `/id`, `api/entitysearch`, `api/dynamicfacets`, `api/joinsearch`, `api/subsearch`, `/morelikethis`, `/terms`, `/facets` | Core search against the CluedIn graph + search index (v1/v2/v3 variants) | **Document** | Primary product-facing search API. Auth: bearer (IdentityServer). |
| SearchController (obsolete actions) | `api/search/subscribe`, `/unsubscribe`, `/count`, `/clear` | Saved-search subscriptions & counters | **Do not document** | Marked `[Obsolete]` in code. |
| **SuggestedSearchController** | `GET api/suggestedsearch`, `api/v1/suggestedsearch` | Query suggestions / typeahead | **Document** | Product-facing companion to search. |
| **SavedSearchController** | `GET/POST/DELETE api/v1/savedsearch`, `/{id}`, `/favorites` | CRUD for user saved & favorite searches | **Document** | Product-facing user feature. |
| SearchToCleanController | `POST api/v2/searchtoclean/checkquery` | Debug comparison of query translators | **Do not document** | Code comment: "DO NOT USE IN PRODUCTION" — internal debug. |
| **RulesController** (Management) | `GET/POST/PUT/DELETE api/rules` (+ `/byprocessingorder`, `/{id}/activate`, `/{id}/deactivate`, `/preview`, `/{id}/reprocess`, `/actions`, `/operators`, `/objecttypes`) | Full CRUD + lifecycle for processing rules | **Document** | Explicitly in-scope. Product-facing rule builder (RACI: `Management.RuleBuilder`). |
| RuleErrorLogController | `GET api/ruleerrorlog/{objectTypeId}/{objectId}` (+ classification/vocab summaries) | Rule engine error logs | **Needs review** | Useful for power users but diagnostic-flavored — confirm if customer-facing. |
| RuleDataPreviewController | `POST api/ruledatapreview` | Sample rule output preview | **Document** | Directly supports the documented rule-builder workflow. |
| RulesAutoCompleteController | `GET api/ruleautocomplete/list` | Autocomplete for rule property values | **Needs review** | UI-support helper; document only if exposing rule authoring API. |
| EvaluationController (PowerFx) | `POST api/powerfx/eval` | Evaluate PowerFx expressions | **Needs review** | **No `[Authorize]` attribute found** — flag to team; likely internal formula-bar support. |
| LanguageServerController (PowerFx) | `POST api/powerfx/lsp`, `GET api/powerfx/context` | LSP intellisense for formula bar | **Do not document** | Internal IDE/UI protocol, not a usable API. Also no auth attribute. |
| RulesController (**Deduplication**) | `api/deduplication/projects/{projectId}/rules` (CRUD, activate, order) | Dedup matching rules within projects | **Document** | Product-facing (dedup management) — but note this is a *different* "Rules" than the rule builder; disambiguate in docs. |
| **GlossaryController** | `GET/POST/PUT/DELETE api/glossary` (+ `/category`, `/tag`, `/termlexicon`, `/endorsement`, `/rating`, `/import`, `/stream`, `/clean`, `/dependencies/{id}`) | CRUD for glossary terms, categories, tags, lexicons | **Document** | Explicitly in-scope. Product-facing (RACI: `Management.Glossary`). |
| **GlossarySearchController** | `GET api/v1/glossarysearch/entities`, `/metrics`, `/lineage`, `/analytics`, `/pii` | Search & analytics over glossary terms | **Document** | Product-facing glossary analytics. |

---

## Part 2 — Full audit (remaining controllers, grouped by recommendation)

### Recommend: Document (product / public-facing)

| Controller | Route prefix | Purpose | Reason |
|---|---|---|---|
| **PublicApi.WebApi — ClueController** | `api/clue`, `api/v1/clue`, `api/v2/clue` | Submit/process clues (core data ingestion) | The canonical public ingestion API. |
| **PublicApi.WebApi — PublicApiGraphQLController** | `api/v1/graphql` | GraphQL query API over entity graph | Primary public query interface. |
| PublicApi.WebApi — EnrichmentReconciliationController | `api/v1/reconciliation/enrichment` | OpenRefine reconciliation + extension API | Documented public integration (OpenRefine). |
| PublicApi.WebApi — OrganizationLookupController | `api/v1/enrichment/lookup/organization` | Org enrichment lookup | Public enrichment API. |
| PublicApi.WebApi — PersonLookupController | `api/v1/enrichment/lookup/person` | Person enrichment lookup | Public enrichment API. |
| PublicApi.WebApi — PublicApiMeshController | `api/v1/mesh` | Data mesh transform/push | Public data API. |
| PublicApi.WebApi — Excel/OpenRefine Clustering | `api/v1/exceladdin/clustering`, `api/v1/openrefine/clustering` | Clustering for add-ins | Public integration endpoints. |
| **ApiTokenController** (Auth/PublicApi) | `api/apitoken` | Generate/list/revoke API tokens | Essential — documents *how to authenticate* to all the above. |
| WebhookController / StaticWebhookController | `services/v{version}/...` | Inbound provider webhooks | Product-facing ingestion (signature-validated). |
| StreamsController (+ StreamMappings, StreamLog, StreamIngestionLog, ConnectorController, ConnectorHealthController) | `api/streams`, `api/connector`, etc. | Stream/export-target (Consume) management | Product-facing "Consume" feature surface. |
| VocabularyController / VocabularyUsageController | `api/vocabs`, `api/vocabusage` | Vocabulary & key management/lineage | Core data-modeling feature. |
| EntityController (top-level) | `api/entity` | Entity retrieval & manipulation (50+ actions) | Core product API (read in summary; recommend a focused doc pass). |
| EntityHistoryController / EntityOriginController | `api/entityhistory`, `api/entityorigin` | Entity change history & origins | Product-facing. |
| HierarchiesController | `api/hierarchies` | Entity hierarchy management | Product-facing. |
| DuplicateEntitiesController + Deduplication (Project/Results/Automate) | `api/duplicates`, `api/deduplication/projects` | Dedup detection & review | Product-facing dedup suite. |
| CleanController (v2) | `api/v2/clean` | Data cleaning projects | Product-facing. |
| EnterpriseFlowsController | `api/enterpriseFlows` | Workflow builder | Product-facing. |
| GlobalDataModelController | `api/globaldatamodel` | Global data model schema | Product-facing. |
| Tasks (Task / TaskApproval / TaskRoleRequest), ApprovalItem, AuditLog | `api/tasks`, `api/approvalitem`, `api/auditLog` | Tasks, approvals, audit | Product-facing governance UX. |
| AI product controllers (AiEndpoint, AiPlatformDefinition, AiJob, AiJobSkill, AIAgent) | `api/ai/endpoint`, `api/aijob`, `api/aiagent`, … | AI agents/jobs/endpoints (non-admin) | Product-facing AI features. |
| ConfigurationController, Integration/Enricher controllers | `api/configuration/providers`, `api/integration/*` | Provider/integration config & listing | Product-facing integration management. |
| Profile, Setting, Notification, Activities, Blob, Ownership, EntityTypeInfo, Copilot, Widgets/Onboarding | various | User profile, settings, notifications, activity feed, blobs, AI copilot, dashboards | Product-facing UX endpoints. |

### Recommend: Do not document (internal / infra / admin / legacy)

| Controller(s) | Route prefix | Why not |
|---|---|---|
| **AuthenticationServer auth flows**: Account, Logout, Password, RefreshTokens, External, ExternalSso, SingleSignOn, OAuthLogin, DynamicClientRegistration, ExternalApplicationAuthentication, EntraOrganizationSSO | `api/Account`, `api/External`, `connect/register`, `account/oauth`, … | Internal login/SSO/OAuth/token plumbing — not a product API surface (auth itself is documented via ApiToken, not these). |
| **All `Admin*` controllers** (13): AdminCommands, AdminEntity, AdminCrawler, AdminClusterSettings, AdminDeadLetterQueue, AdminDistributedJobs, AdminIndexCommands, DataSource, Enrichers, OrganizationAdminCommands, OrganizationAdminCrawler, StreamLog (admin), AuthenticationAdminCommands | `api/admin/*` | Operator/maintenance commands (reprocess, remap, dead-letter, deduplicate). Admin-role gated; internal. |
| Health/infra: HealthLiveness, HealthReadiness, Status, RobotsTxt, DefaultRedirect, GoogleDomainCheck (×2), SentryController | `/health`, `/status`, catch-all, etc. | Infrastructure/ops endpoints. |
| Internal services/agents: AgentController, AgentWebApiController, RemoteAgentController, IAgentController, JobController, IdentityCounterController, Notificationv2 (AlertManager), MeshProcessorController, LoggingController | various | Internal job/agent/monitoring plumbing. |
| Governance admin: GDPRAnonymization, GDPRPII, MeshCenter, EntityDataDeletion, ExplainLog | `api/gdpr`, `api/meshcenter`, `api/entityDataDeletion`, `api/explainLog` | Admin/governance ops; some already `ApiExplorerSettings(IgnoreApi)`. |
| Tenant admin: CleanUp (delete org), Role, UserRoles, OrganizationAccount, OrganizationProfile, AccessControlPolicies, PageTemplate(s), Migration Export/Import, StrongTyping, Log, ConfigurationController (engine), MeteredBilling | various | Admin-only tenant/role/config management. |
| Legacy/deprecated: CluedInCleanController (v1, `[Obsolete]`), InsightController (`[Obsolete]`), obsolete actions in Search/Configuration/Organization | `api/v1/clean`, `api/insight` | Explicitly obsolete in code. |

### Recommend: Needs review

| Controller | Route | Open question |
|---|---|---|
| RuleErrorLogController, RulesAutoCompleteController | `api/ruleerrorlog`, `api/ruleautocomplete` | Part of the documented rule-builder UX, or internal helpers? |
| PowerFx Evaluation/LanguageServer | `api/powerfx/*` | **No `[Authorize]` attribute** — confirm intended exposure before documenting. |
| Organization Providers controllers (AddProviders, EnableProviders, UpdateProviders, TeamBroadcast, Upload) | `api/v2/organization/providers/*` | Several have **no class-level auth attribute** — confirm whether intentional (RACI may be applied elsewhere) before publishing. |
| EntityActionsController | `api/entityActions` | Agent reported **missing `[Authorize]`** — verify before documenting. |
| ExternalFeatureController, ExtendedConfigurationController, DistributedJobsController | various | Mixed product/internal signals. |
| Two `EntityInfoController` and two `OrganizationController` / `UserController` classes | — | Duplicate class names in different namespaces; pick the canonical one per doc area to avoid route confusion. |

---

## Part 3 — Summary

### Should be documented (priority + public surface)

- **Priority:** Search (`SearchController`, `SuggestedSearchController`, `SavedSearchController`), Rules (Management `RulesController` + `RuleDataPreview`, and separately Deduplication `RulesController`), Glossary (`GlossaryController`, `GlossarySearchController`).
- **Public API project:** `Clue`, `GraphQL`, enrichment `reconciliation`/`lookup`, `mesh`, clustering, and crucially **`ApiTokenController`** (authentication).
- **Product features:** Streams/Connectors, Vocabularies, Entity (+history/origin), Hierarchies, Deduplication, Clean v2, Enterprise Flows, Tasks/Approvals, AI agents/jobs, Integrations/Providers config, profile/settings/notifications.

### Should not be documented

- All auth/SSO/OAuth plumbing, all `Admin*` maintenance controllers, health/infra endpoints, internal agent/job/monitoring services, tenant/role admin, governance/deletion ops, and anything marked `[Obsolete]` (Clean v1, Insight).

### Open questions for the team

1. **Doc scope** — is the public surface only the `PublicApi.WebApi` project, or the broader `Server.WebApi` product API (Search/Rules/Glossary live here)? This determines ~80 controllers' fate.
2. **Two "Rules" concepts** — processing **rule builder** vs **deduplication** rules. Should both be documented, and how do we disambiguate them for readers?
3. **Unauthenticated endpoints** — PowerFx (`api/powerfx/*`), some `OrganizationProviders` controllers, and `EntityActionsController` appear to lack `[Authorize]`. Is this intentional? (Surfaced for awareness — no code change made.)
4. **Diagnostic endpoints** (`RuleErrorLog`, `RulesAutoComplete`, `StreamLog`) — customer-facing or internal-only?
5. **Versioning** — most endpoints expose both `api/...` and `api/v1/...`; which should docs present as canonical?
