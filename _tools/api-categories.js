/*
 * Single source of truth for the customer-facing REST API documentation
 * categories. The grouping and inclusion list here is derived from the
 * "Ongoing REST API Audit" (docs/250-rest-api/030-api-audit.md): every tag
 * listed below is a controller the audit marked **Document** / **Document
 * (admin)**. Any swagger tag that is NOT listed here is treated as **Exclude**
 * — prune-spec.js removes it from the published swagger.json and split-spec.js
 * drops it from the per-category specifications.
 *
 * Order controls the order of categories in the generated manifest. The
 * per-category doc pages set their own nav_order, but keep the two in sync.
 *
 * Both _tools/split-spec.js and _tools/prune-spec.js consume this module.
 */
module.exports = [
  { slug: 'access-control-and-governance', title: 'Access control & governance',
    description: 'Access control policies, audit logs, entity ownership, and tag metadata.',
    tags: ['AccessControlPolicies','AuditLog','Ownership','TagMetadata'] },
  { slug: 'entities', title: 'Entities',
    description: 'Read, create, modify, merge, and inspect golden records and their metadata.',
    tags: ['Entity','EntityDataDeletion','EntityHistory','EntityInfo','EntityModification','EntityOrigin','EntitySource','EntityTopology','EntityTypeInfo'] },
  { slug: 'search', title: 'Search',
    description: 'Query the CluedIn graph and manage saved searches.',
    tags: ['Search','SavedSearch'] },
  { slug: 'vocabularies', title: 'Vocabularies',
    description: 'Manage vocabularies and vocabulary keys.',
    tags: ['Vocabulary','VocabularyUsage'] },
  { slug: 'glossary', title: 'Glossary',
    description: 'Manage glossary categories and terms, and search the glossary.',
    tags: ['Glossary','GlossarySearch'] },
  { slug: 'hierarchies', title: 'Hierarchies',
    description: 'Build and manage hierarchies and the global data model.',
    tags: ['Hierarchies','GlobalDataModel'] },
  { slug: 'deduplication', title: 'Deduplication',
    description: 'Find, review, and resolve duplicate records: deduplication projects, automation, match results, and entity split.',
    tags: ['Project','Automate','Results','DuplicateEntities','SplitEntity'] },
  { slug: 'rules-and-evaluation', title: 'Rules & evaluation',
    description: 'Manage data, survivorship, and golden record rules; preview rule output and inspect evaluation logs.',
    tags: ['Rules','RuleDataPreview','RuleErrorLog','ExplainLog'] },
  { slug: 'streams-and-export', title: 'Streams, connectors & export',
    description: 'Configure, operate, and monitor export streams and the connectors they use.',
    tags: ['Streams','StreamIngestionLog','StreamLog','StreamMappings','StreamsVocabularyKeyUsage','Connector','ConnectorHealth'] },
  { slug: 'data-preparation-and-enrichment', title: 'Data preparation & enrichment',
    description: 'Clean and enrich records using built-in cleaning and enricher providers.',
    tags: ['Clean','Enricher'] },
  { slug: 'ai', title: 'AI',
    description: 'AI agents, jobs, skills, and Copilot.',
    tags: ['AIAgent','AiJob','AiJobSkill','Copilot'] },
  { slug: 'administration-and-configuration', title: 'Administration & configuration',
    description: 'Settings, logs, and metered billing.',
    tags: ['Setting','Log','MeteredBilling'] },
  { slug: 'organization', title: 'Organization',
    description: 'Organization profile and usage statistics.',
    tags: ['Organization','OrganizationProfile'] }
];
