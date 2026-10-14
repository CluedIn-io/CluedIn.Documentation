# Redirects for unpublished pages

Old URLs whose page is no longer published, and the live page each one now
redirects to.

## Why this exists

`jekyll-redirect-from` builds a page's redirect stubs only when it builds the
page. A `redirect_from` on a page with `published: false` therefore builds
nothing, and the old URL serves a 404.

107 old URLs were in that state: 83 on pages in `docs/archive/`, and 24 on
unpublished pages inside the live sections. Every one of those pages was
already unpublished before the lifecycle restructure; `/development/modelling`,
for example, has been unpublished since June 2024 (commit `08989e957`). So the
restructure did not break them, but they were still 404s, and
`/development/modelling` is linked from two pages on www.cluedin.com
(`/paas-customer-welcome` and `/saas-welcome-page`).

Each old URL was moved from the unpublished page's `redirect_from` to the
`redirect_from` of the live page that now covers the subject. Where nothing
covers it any more, it points at the nearest section or subsection index.
`redirects.csv` was updated to match.

One URL, `/deployment/infra-how-tos/ama-backup`, was already redirected by the
Backup and restore index as well as the archived draft. Only the duplicate on
the archived draft was removed.

## Keeping it this way

`validate.py` now fails when:

- an unpublished page has a `redirect_from`
- a `redirect_from` is also some page's `permalink`
- two pages claim the same `redirect_from`

When you unpublish or archive a page, move its `redirect_from` entries to the
page that replaces it, and add a row here.

## Archived pages (`docs/archive/`)

| Old URL | Unpublished page | Now redirects to | Why |
|---|---|---|---|
| `/deployment/infra-how-tos/ama-backup` | Backup and restore (superseded draft) | [`/operate/backup-and-restore`](/operate/backup-and-restore) | Already redirected by the Backup and restore index; the duplicate on the archived draft was removed. |
| `/development/modelling` | Modelling | [`/develop/integrations`](/develop/integrations) | Explains feeding data in through custom integrations (providers and enrichers). |
| `/development/administration-operations` | Administration Operations | [`/api/administration-and-configuration`](/api/administration-and-configuration) | Admin-only operations invoked through the API. |
| `/development/changing-configuration-settings` | Changing Configuration Settings | [`/operate/configuration`](/operate/configuration) | Changing configuration of an installation. |
| `/development/content-extractors` | Content Extractors | [`/develop/integrations`](/develop/integrations) | Extension point for custom integrations; no current equivalent page. |
| `/development/downloading-file-indexing-content` | Downloading a File and Indexing the Content | [`/develop/integrations`](/develop/integrations) | Extension point for custom integrations; no current equivalent page. |
| `/development/commands` | Commands | [`/operate/monitoring/processing-pipeline`](/operate/monitoring/processing-pipeline) | Commands are the messages that move through the processing pipeline. |
| `/development/adding-datastore-provider` | Adding a new Datastore Provider | [`/operate/architecture`](/operate/architecture) | Datastores are now described as part of the platform architecture. |
| `/development/datastores` | Datastores | [`/operate/architecture`](/operate/architecture) | Datastores are now described as part of the platform architecture. |
| `/development/switching-datastore-provider` | Switching a Datastore Provider | [`/operate/architecture`](/operate/architecture) | Datastores are now described as part of the platform architecture. |
| `/development/events` | Events | [`/operate/monitoring/processing-pipeline`](/operate/monitoring/processing-pipeline) | Events raised while records are processed. |
| `/development/deploying-search-provider` | Deploying a New External Search Provider | [`/develop/build-custom-enricher`](/develop/build-custom-enricher) | External search providers are now called enrichers. |
| `/development/external-search-providers` | External Search Providers | [`/develop/build-custom-enricher`](/develop/build-custom-enricher) | External search providers are now called enrichers. |
| `/development/validate-server-health` | Validate Server Health | [`/operate/monitoring`](/operate/monitoring) | Checking that an installation is healthy. |
| `/development/one-time-jobs` | One Time Jobs | [`/administer/jobs`](/administer/jobs) | Background jobs. |
| `/development/recurring-time-jobs` | Recurring Time Jobs | [`/administer/jobs`](/administer/jobs) | Background jobs. |
| `/development/scheduled-time-jobs` | Scheduled Time Jobs | [`/administer/jobs`](/administer/jobs) | Background jobs. |
| `/development/building-logging-provider` | Building a new Logging Provider | [`/operate/configuration/configure-logging`](/operate/configuration/configure-logging) | Logging configuration. |
| `/development/entity` | Entity | [`/get-started/core-concepts/golden-records`](/get-started/core-concepts/golden-records) | Entities are now called golden records. |
| `/development/person-entity-type` | Person Entity Type | [`/model/business-domains/business-domains-explained`](/model/business-domains/business-domains-explained) | Entity types are now called business domains. |
| `/development/infrastructure-user-entity` | Infrastructure User Entity Type | [`/model/business-domains/business-domains-explained`](/model/business-domains/business-domains-explained) | Entity types are now called business domains. |
| `/development/organization-user-entity` | Organization Entity Type | [`/model/business-domains/business-domains-explained`](/model/business-domains/business-domains-explained) | Entity types are now called business domains. |
| `/development/vocabulary-values` | Vocabulary Values | [`/model/vocabularies/vocabulary-keys`](/model/vocabularies/vocabulary-keys) | Allowed values are a property of vocabulary keys. |
| `/development/vocabulary-groupings` | Vocabulary Groupings | [`/model/vocabularies/vocabularies-explained`](/model/vocabularies/vocabularies-explained) | Vocabulary concepts. |
| `/development/core-vocabularies` | Core Vocabularies | [`/model/vocabularies/vocabularies-explained`](/model/vocabularies/vocabularies-explained) | Vocabulary concepts. |
| `/development/dynamic-vocabularies` | Dynamic Vocabularies | [`/model/vocabularies/vocabularies-explained`](/model/vocabularies/vocabularies-explained) | Vocabulary concepts. |
| `/development/person-vocabulary` | Person Vocabulary | [`/model/vocabularies/vocabularies-explained`](/model/vocabularies/vocabularies-explained) | Vocabulary concepts. |
| `/development/organization-vocabulary` | Organization Vocabulary | [`/model/vocabularies/vocabularies-explained`](/model/vocabularies/vocabularies-explained) | Vocabulary concepts. |
| `/development/clue` | Clue | [`/get-started/core-concepts/clue-reference`](/get-started/core-concepts/clue-reference) | Same subject. |
| `/development/change-verbs` | Change Verbs | [`/get-started/core-concepts/clue-reference`](/get-started/core-concepts/clue-reference) | Change verbs are a property of a clue. |
| `/development/data-part` | Data Part | [`/get-started/core-concepts/golden-records`](/get-started/core-concepts/golden-records) | Data parts are the source records that make up a golden record. |
| `/development/edge-types` | Edge Types | [`/model/relationships/edges`](/model/relationships/edges) | Same subject. |
| `/development/common-design-decisions` | Common Design Decisions | [`/model/data-catalog/modeling-approaches`](/model/data-catalog/modeling-approaches) | Modelling design choices. |
| `/developer/rules` | Rules in CluedIn | [`/govern/rules`](/govern/rules) | Same subject. |
| `/developer/iprocessingfilter` | Adding a new IProcessingFilter | [`/operate/monitoring/processing-pipeline`](/operate/monitoring/processing-pipeline) | Processing pipeline extension point; no current equivalent page. |
| `/developer/processing-pipeline` | Adding a new Processing Pipeline | [`/operate/monitoring/processing-pipeline`](/operate/monitoring/processing-pipeline) | Processing pipeline. |
| `/developer/preprocessor` | Adding a new PreProcessor | [`/operate/monitoring/processing-pipeline`](/operate/monitoring/processing-pipeline) | Processing pipeline extension point; no current equivalent page. |
| `/developer/idatapartprocessor` | Adding a new IDataPartProcessor | [`/operate/monitoring/processing-pipeline`](/operate/monitoring/processing-pipeline) | Processing pipeline extension point; no current equivalent page. |
| `/developer/ientitypypeprocessor` | Adding a new IEntityTypeProcessor | [`/operate/monitoring/processing-pipeline`](/operate/monitoring/processing-pipeline) | Processing pipeline extension point; no current equivalent page. |
| `/developer/imergepreprocessor` | Adding a new IMergePreProcessor | [`/master/deduplication/concept-of-deduplication`](/master/deduplication/concept-of-deduplication) | Custom logic before records merge. |
| `/developer/agent-jobs` | Agent Jobs | [`/ingest/connectors/using-agents`](/ingest/connectors/using-agents) | Same subject. |
| `/developer/common-problems` | Common Problems | [`/troubleshooting`](/troubleshooting) | Symptom-led troubleshooting. |
| `/developer/extending-pipelines` | Extending the Existing Pipeline Process | [`/operate/monitoring/processing-pipeline`](/operate/monitoring/processing-pipeline) | Processing pipeline. |
| `/developer/ignoring-changes` | Ignoring Insignificant Changes | [`/develop/integrations/delts-crawls`](/develop/integrations/delts-crawls) | Skipping unchanged data during ingestion. |
| `/developer/parent-aggregation` | Parent Aggregation | [`/model/hierarchies/concept-of-hierarchy`](/model/hierarchies/concept-of-hierarchy) | Parent hierarchies of records. |
| `/developer/clue-preview-image` | Setting a Preview Image for a Clue | [`/develop/integrations`](/develop/integrations) | Integration-development detail; no current equivalent page. |
| `/developer/thumbnail-extractors` | Thumbnail Extractors | [`/develop/integrations`](/develop/integrations) | Integration-development detail; no current equivalent page. |
| `/developer/processedentitymetadata` | Turning Clues into ProcessedEntityMetadata | [`/get-started/core-concepts/golden-records`](/get-started/core-concepts/golden-records) | How a golden record's preferred values are built. |
| `/developer/workflow-event-handlers` | Workflow Event Handlers | [`/govern/workflows`](/govern/workflows) | Workflows. |
| `/developer/webhooks` | Webhooks | [`/ingest/data-sources/endpoint`](/ingest/data-sources/endpoint) | Receiving pushed data over HTTP. |
| `/user-interface/entity-page` | Entity Page | [`/master/golden-records`](/master/golden-records) | The entity page is now the golden record page. |
| `/user-interface/all-properties` | All Properties | [`/master/golden-records`](/master/golden-records) | Properties of a golden record. |
| `/user-interface/followed-entitie` | Followed Entities | [`/master/search`](/master/search) | Finding records you return to. |
| `/user-interface/history` | History | [`/master/golden-records/history`](/master/golden-records/history) | Same subject. |
| `/user-interface/keep-in-the-loop` | Keep in the Loop | [`/master/search`](/master/search) | Saved and repeated searches. |
| `/user-interface/pending-changes` | Pending Changes | [`/govern/workflows/manage-approval-requests`](/govern/workflows/manage-approval-requests) | Changes waiting for approval. |
| `/user-interface/adding-search-filters` | Adding Search Filters | [`/master/filters`](/master/filters) | Same subject. |
| `/user-interface/searching-for-data` | Searching for Data | [`/master/search`](/master/search) | Same subject. |
| `/user-interface/suggested-searches` | Suggested Searches | [`/master/search`](/master/search) | Search. |
| `/governance/access-control` | Access Control | [`/administer/access-control`](/administer/access-control) | Same subject. |
| `/governance/consent-management` | Consent Management | [`/govern`](/govern) | Unsupported feature; nearest section. |
| `/governance/data-breaches` | Data Breaches | [`/govern`](/govern) | Unsupported feature; nearest section. |
| `/governance/data-catalog` | Data Catalog | [`/model/data-catalog`](/model/data-catalog) | Same subject. |
| `/governance/data-glossary` | Data Glossary | [`/govern/work-with-glossary`](/govern/work-with-glossary) | Same subject. |
| `/governance/data-policies` | Data Policies | [`/govern/rules`](/govern/rules) | Policies are now implemented as rules. |
| `/governance/data-privacy` | Data Privacy | [`/administer/access-control`](/administer/access-control) | Restricting access to sensitive data. |
| `/governance/data-retention` | Data Retention | [`/govern/set-retention`](/govern/set-retention) | Same subject. |
| `/governance/mesh-api` | Mesh API | [`/publish/integration-patterns/writing-back-to-operational-systems`](/publish/integration-patterns/writing-back-to-operational-systems) | Writing values back to source systems. |
| `/governance/subject-access-request` | Subject Access Request | [`/govern`](/govern) | Unsupported feature; nearest section. |
| `/preparation/data-quality-metrics` | Data Quality Metrics | [`/solutions/use-cases/data-quality-use-case`](/solutions/use-cases/data-quality-use-case) | Data quality management. |
| `/preparation/data-quality-metrics/most-used-data-quality-metrics` | Most Used Data Quality Metrics | [`/solutions/use-cases/data-quality-use-case`](/solutions/use-cases/data-quality-use-case) | Data quality management. |
| `/preparation/data-quality-metrics/how-to-add-a-data-quality-metric` | How to add a new Data Quality Metric | [`/solutions/use-cases/data-quality-use-case`](/solutions/use-cases/data-quality-use-case) | Data quality management. |
| `/preparation/data-quality-metrics/data-quality-metric-explanations` | Data Quality Metric Explanations | [`/solutions/use-cases/data-quality-use-case`](/solutions/use-cases/data-quality-use-case) | Data quality management. |
| `/preparation/aggregation` | Aggregation | [`/operate/monitoring/processing-pipeline`](/operate/monitoring/processing-pipeline) | Turning clues into records in the processing pipeline. |
| `/preparation/cluedin-connect` | CluedIn Connect | [`/ingest/connectors`](/ingest/connectors) | Connecting data sources. |
| `/consume/data-marts` | Data Marts | [`/publish/streams`](/publish/streams) | Data is now delivered out through streams. |
| `/consume/configuration-search-relevance` | Configuration Search Relevance | [`/master/search`](/master/search) | Search. |
| `/consume/outgoing-streams` | Outgoing Streams | [`/publish/streams`](/publish/streams) | Same subject. |
| `/consume/rest-api` | Rest API | [`/api/get-started`](/api/get-started) | Same subject. |
| `/consume/running-searches` | Running Searches | [`/master/search`](/master/search) | Same subject. |
| `/management/modelling` | Modelling (superseded) | [`/model/data-catalog/modeling-approaches`](/model/data-catalog/modeling-approaches) | Same subject. |
| `/preparation/enricher/clearbit` | Clearbit | [`/govern/enrichment`](/govern/enrichment) | Clearbit enricher is withdrawn; list of current enrichers. |
| `/govern/enrichment/clearbit` | Clearbit | [`/govern/enrichment`](/govern/enrichment) | Clearbit enricher is withdrawn; list of current enrichers. |

## Unpublished pages in live sections

| Old URL | Unpublished page | Now redirects to | Why |
|---|---|---|---|
| `/kb/cel` | CluedIn Expression Language (C.E.L.) | [`/govern/rules`](/govern/rules) | Expression language for manipulating data; nearest live subject. |
| `/workflow/prerequisites` | Prerequisites | [`/govern/workflows`](/govern/workflows) | Workflows. |
| `/administration/user-interface` | User interface | [`/administer/ui-configuration`](/administer/ui-configuration) | Same subject. |
| `/preparation/entity-setup` | Business domain page layout | [`/model/business-domains/manage-business-domains`](/model/business-domains/manage-business-domains) | Entity types are now called business domains. |
| `/preparation/entity-type-translation` | Business domain translation | [`/model/business-domains/manage-business-domains`](/model/business-domains/manage-business-domains) | Entity types are now called business domains. |
| `/administration/permissions` | Permissions | [`/administer/access-control`](/administer/access-control) | Restricting access to data. |
| `/kb/cost-efficience` | Running CluedIn efficiently for cost | [`/operate/cost-and-scaling`](/operate/cost-and-scaling) | Same subject. |
| `/kb/stop-cluster` | Stop AKS cluster to reduce cost | [`/operate/cost-and-scaling`](/operate/cost-and-scaling) | Reducing cost. |
| `/kb/basic-auth-cluedin-clean` | Restricting access to CluedIn Clean Basic Authentication | [`/operate/security`](/operate/security) | Securing the installation. |
| `/kb/sso-auth-cluedin-clean` | Restricting access to CluedIn Clean via SSO Authentication | [`/operate/security`](/operate/security) | Securing the installation. |
| `/kb/azure-customer-usage-attribution` | Azure customer usage attribution | [`/operate/azure-marketplace`](/operate/azure-marketplace) | Azure Marketplace deployments. |
| `/deployment/infra-how-tos/ama-upgrade` | Marketplace upgrade | [`/operate/upgrade`](/operate/upgrade) | Same subject. |
| `/microsoft-integration/powerapps/setup-credentials` | Credentials and application setup | [`/solutions/power-apps/configuration-guide`](/solutions/power-apps/configuration-guide) | Power Apps setup. |
| `/microsoft-integration/powerapps/setup-connections` | Connections setup | [`/solutions/power-apps/configuration-guide`](/solutions/power-apps/configuration-guide) | Power Apps setup. |
| `/microsoft-integration/powerapps/external-features` | Power Apps external features | [`/solutions/power-apps`](/solutions/power-apps) | Power Apps integration. |
| `/microsoft-integration/powerapps/features/sync-entitytypes` | Sync business domains to Dataverse tables | [`/solutions/power-apps`](/solutions/power-apps) | Power Apps integration. |
| `/microsoft-integration/powerapps/features/sync-dataverse` | Sync Dataverse table to Cluedin business domains/vocabularies | [`/solutions/power-apps`](/solutions/power-apps) | Power Apps integration. |
| `/microsoft-integration/powerapps/features/create-workflow` | Create ingestion endpoint workflow | [`/solutions/power-apps`](/solutions/power-apps) | Power Apps integration. |
| `/microsoft-integration/powerapps/features/create-batch-approval-workflow` | Create a batch approval workflow process | [`/solutions/power-apps`](/solutions/power-apps) | Power Apps integration. |
| `/microsoft-integration/powerapps/features/create-streams` | Create streams from Power Apps | [`/solutions/power-apps`](/solutions/power-apps) | Power Apps integration. |
| `/microsoft-integration/purview/introduction` | Purview integration features | [`/solutions/purview`](/solutions/purview) | Purview integration. |
| `/microsoft-integration/purview/setup` | Setup credentials and permissions | [`/solutions/purview/configuration-guide`](/solutions/purview/configuration-guide) | Purview setup. |
| `/kb/elastic-index-rebuild` | Rebuilding Elasticsearch index | [`/troubleshooting`](/troubleshooting) | Symptom-led troubleshooting. |
| `/kb/platform-versioning` | Versioning and release schedule | [`/release-notes`](/release-notes) | Versions and release schedule. |
