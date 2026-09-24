---
layout: cluedin
title: Work with CluedIn Copilot
parent: Copilot Integration
grand_parent: Microsoft Integration
permalink: /microsoft-integration/copilot-integration/work-with-copilot
nav_order: 020
has_children: false
last_modified: 2026-09-24
---
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

In this article, you will learn about Copilot skills that are available in CluedIn and find examples of the types of tasks you can ask Copilot to perform.

## Copilot overview

CluedIn Copilot is an AI assistant designed to help you with day-to-day data management tasks through conversational prompts in any language.

You can open the Copilot chat from any place in CluedIn by clicking on the message icon in the lower-right corner of the page. The Copilot pane contains your chats. If you want to rename or delete a chat, select **Copilot** next to the search bar.

CluedIn Copilot provides a broad set of skills (also called functions) that cover data onboarding, data quality, cleaning, deduplication, rules, AI jobs, streams, vocabularies, search, and other data management tasks.

To ask Copilot what it can do, use prompts similar to:

- What functions can you call?
- What are all the functions that I can use?
- What skills are available for data quality?
- What skills are available for AI jobs?

You'll find the current skill catalogue in [Copilot skills](#copilot-skills).

![functions.gif]({{ "/assets/images/microsoft-integration/copilot/functions.gif" | relative_url }})

### Chain skills together

You can **chain different skills together** in a single request. For example, instead of separately creating, activating, and reprocessing a rule, you can ask Copilot to perform the complete task.

```
Create a rule that tags all records with customer.country set to 'Norway' as 'Nordic', then activate and reprocess the rule.
```

You can also combine analysis and remediation. For example:

```
Find anomalies in training.country. For each anomaly, suggest how it should be fixed and create the appropriate rule for /TrainingContact records.
```

CluedIn Copilot is multilingual, so you can invoke skills in the language that is most convenient for you.

In many cases, Copilot can also use the page you are currently viewing as context. This means you can refer to objects as _this data set_, _this vocabulary key_, _this rule_, or _this record_ instead of supplying an ID explicitly.

You can combine general knowledge with CluedIn actions in the same prompt.

```
Create a golden record rule that tags Company records where company.state is not one of the Australian states.
```

For actions that support previewing, Copilot can use `PreviewCopilotActionSkill` so that the proposed action can be inspected before it is applied.

## Copilot skills

The following sections list the Copilot skills currently available in CluedIn. Skill names below use their implementation class names so they can be matched directly to the CluedIn Copilot codebase.

{:.important}
The exact skills available to you can depend on the CluedIn version, enabled features, permissions, and the context in which Copilot is being used.

### AI Jobs

AI Job skills allow Copilot to discover AI agents, create and update jobs, inspect job configuration and runs, preview input, start test or production runs, review results, approve results, and delegate work to an AI job.

| Skill | Purpose |
|--|--|
| `ApproveAiJobRunResultsSkill` | Approves results produced by an AI job run. |
| `CreateAiJobsSkill` | Creates AI jobs. |
| `DelegateToAiJobSkill` | Delegates a task to an AI job. |
| `GetAiAgentsSkill` | Lists or retrieves the AI agents available for use by AI jobs. |
| `GetAiJobSkill` | Retrieves details for a specific AI job. |
| `GetAiJobActionsSkill` | Retrieves the actions configured for an AI job. |
| `GetAiJobDataReferencesSkill` | Retrieves the data references configured for an AI job. |
| `GetAiJobRunResultsSkill` | Retrieves results from an AI job run. |
| `GetAiJobRunsSkill` | Retrieves runs associated with an AI job. |
| `GetAiJobsSkill` | Lists AI jobs. |
| `PreviewAiJobInputSkill` | Previews the data that will be supplied to an AI job. |
| `ReportAiJobDelegationOutcomeSkill` | Reports the outcome of work delegated to an AI job. |
| `StartAiJobProductionRunSkill` | Starts a production run for an AI job. |
| `StartAiJobTestRunSkill` | Starts a test run for an AI job. |
| `UpdateAiJobsSkill` | Updates AI job configuration. |

For example, you can ask:

```
Create an AI job that finds and fixes missing company websites, test it first, and show me the results.
```

### Cleaning

Cleaning skills help Copilot create cleaning projects, identify anomalous values, normalize vocabulary-key values, and inspect existing cleaning projects.

| Skill | Purpose |
|--|--|
| `CreateCleanProjectSkill` | Creates a clean project. |
| `DetectVocabularyKeyValueAnomaliesSkill` | Detects anomalies in values for a vocabulary key. |
| `ListCleaningProjectsSkill` | Lists existing clean projects. |
| `NormalizeVocabularyKeyValuesSkill` | Normalizes or standardizes values for a vocabulary key. |

### Data Quality

Data Quality skills help Copilot assess data quality and propose a plan for improving it.

| Skill | Purpose |
|--|--|
| `DataQualitySkill` | Analyzes or reports on data quality. |
| `PlanDataQualityImprovementsSkill` | Produces a plan for improving identified data quality issues. |

A useful pattern is to ask Copilot to assess the current state first and then plan the remediation:

```
Assess the data quality of Customer records and give me a plan to improve the most important issues.
```

### Data Sets

Data Set skills support discovery, onboarding, mapping, processing, and analysis of ingested data sets.

| Skill | Purpose |
|--|--|
| `AutoCreateDataSetMappingSkill` | Automatically creates a mapping for a data set. |
| `DescribeDataSetSkill` | Describes a data set and its contents. |
| `EntitySearchByDataSetColumnSampleSkill` | Searches existing entities using sample values from a data-set column. |
| `ListDataSetsSkill` | Lists available data sets. |
| `OnboardDataSetsSkill` | Guides or performs data-set onboarding. |
| `ProcessDataSetSkill` | Processes a data set. |
| `SuggestDataSetMappingSkill` | Suggests how data-set columns should be mapped. |

For example:

```
Describe this data set, suggest the best mapping, and onboard it as Company data.
```

### Deduplication

Deduplication skills allow Copilot to create deduplication projects, create matching rules, explain duplicate groups, generate project results, and inspect existing projects.

| Skill | Purpose |
|--|--|
| `CreateDeduplicationProjectSkill` | Creates a deduplication project. |
| `CreateMatchingRuleSkill` | Creates a matching rule for a deduplication project. |
| `ExplainDeduplicationGroupSkill` | Explains why records in a deduplication group are considered potential duplicates. |
| `GenerateResultsDeduplicationProjectSkill` | Generates results for a deduplication project. |
| `ListDeduplicationProjectSkill` | Lists existing deduplication projects. |

For example:

```
Create a deduplication project for Customer records, add a matching rule based on email and phone, and generate the results.
```

### Entity

| Skill | Purpose |
|--|--|
| `DescribeEntitySkill` | Describes a golden record, including its identity and available data. |

### Entity Type

Entity Type skills operate on CluedIn business domains.

| Skill | Purpose |
|--|--|
| `CreateEntityTypeSkill` | Creates a new entity type/business domain. |
| `ListEntityTypesSkill` | Lists available entity types/business domains. |

### Export Targets

| Skill | Purpose |
|--|--|
| `ListExportTargetsSkill` | Lists configured export targets that can be used by streams. |

### Glossary

| Skill | Purpose |
|--|--|
| `CreateGlossaryTermSkill` | Creates a glossary term in a glossary category. |
| `ListGlossaryCategoriesSkill` | Lists available glossary categories. |

### Hierarchy

| Skill | Purpose |
|--|--|
| `CreateHierarchySkill` | Creates a hierarchy from related records. |
| `ListHierarchiesSkill` | Lists existing hierarchies. |

### General

| Skill | Purpose |
|--|--|
| `PreviewCopilotActionSkill` | Previews a proposed Copilot action before it is applied when the action supports previewing. |

### Profiling

| Skill | Purpose |
|--|--|
| `ProfilingVocabularyKeySkill` | Profiles the values of a vocabulary key to help understand distribution, quality, and anomalies. |

### Rules

Rule skills allow Copilot to create and manage data part, survivorship, and golden record rules.

| Skill | Purpose |
|--|--|
| `CloneRuleSkill` | Creates a copy of an existing rule. |
| `CreateGoldenRecordRuleSkill` | Creates a golden record rule. |
| `CreateProcessingRuleSkill` | Creates a data part/processing rule. |
| `CreateSurvivorshipRuleSkill` | Creates a survivorship rule. |
| `GetRuleSkill` | Retrieves details of a rule. |
| `ListRulesSkill` | Lists rules. |
| `ReprocessRuleSkill` | Reprocesses a rule so that it is applied to matching records. |
| `UpdateRuleSkill` | Updates an existing rule. |
| `ActivateRuleSkill` | Activates a rule. |
| `DeactivateRuleSkill` | Deactivates a rule. |

`ActivateRuleSkill` and `DeactivateRuleSkill` inherit indirectly from the abstract `SetRuleActivationStateSkillBase<T>` intermediary. The base class contains shared rule activation-state behavior and is not itself a concrete Copilot action that an end user invokes.

For example:

```
Create a golden record rule that tags Company records with no website as "Missing Website", activate it, and reprocess the rule.
```

### Search

| Skill | Purpose |
|--|--|
| `AdvancedSearchSkill` | Performs an advanced search using more detailed search criteria. |
| `SimpleSearchSkill` | Performs a straightforward search for records. |

### Streams

Stream skills let Copilot create, copy, inspect, and start streams.

| Skill | Purpose |
|--|--|
| `CloneStreamSkill` | Creates a copy of a stream. |
| `CreateStreamSkill` | Creates a stream. |
| `ListStreamsSkill` | Lists existing streams. |
| `StartStreamSkill` | Starts a stream. |

### Vocabulary

| Skill | Purpose |
|--|--|
| `CreateVocabularySkill` | Creates a vocabulary. |
| `ListDynamicDomainCatalogSkill` | Lists the dynamic domain catalogue available to Copilot. |
| `ListVocabulariesSkill` | Lists vocabularies. |

### Vocabulary Keys

Vocabulary Key skills support creation, mapping, lineage, glossary lookups, and rule suggestions.

| Skill | Purpose |
|--|--|
| `ApplyVocabularyMappingPlanSkill` | Applies a prepared vocabulary mapping plan. |
| `ChangeVocabularyKeyToGlossaryTermLookupSkill` | Changes a vocabulary key so that it uses a glossary term lookup. |
| `CreateVocabularyKeySkill` | Creates a vocabulary key. |
| `GetVocabularyMappingLineageSkill` | Retrieves lineage information for vocabulary mappings. |
| `ListVocabularyKeysSkill` | Lists vocabulary keys. |
| `MapVocabularyKeysSkill` | Maps vocabulary keys. |
| `PrepareVocabularyKeyMappingsSkill` | Prepares a vocabulary-key mapping plan before it is applied. |
| `SuggestVocabularyKeyRulesSkill` | Suggests rules that are appropriate for a vocabulary key. |

A useful mapping workflow is:

```
Inspect the vocabulary keys in this data set, prepare a mapping plan to the Company vocabulary, show me the plan, and then apply it.
```

## Tips for using Copilot skills

You do not need to know the implementation class name to use a skill. Describe the outcome you want in natural language and Copilot will select the appropriate skills.

For multi-step tasks, state the desired end result rather than issuing every individual operation yourself. For example:

```
Onboard this data set, map it to the Customer domain, identify data quality problems, and suggest the next steps.
```

For actions that change configuration or data, include enough context to make the intended scope clear—for example, the business domain, data set, vocabulary, vocabulary key, rule, stream, or AI job that you want Copilot to work with.
