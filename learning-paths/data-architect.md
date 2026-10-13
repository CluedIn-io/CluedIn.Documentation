---
title: Data Architect course
url: https://documentation.cluedin.net/learning-paths/data-architect
content_type: landing
section: Learning paths
---

# Data Architect course

The Data Architect course is for people who build and own the structural data pipeline in CluedIn. Data Architects establish how data enters CluedIn, how it is modeled and matched, how the initial processing logic works, and how trusted data leaves CluedIn.

The course does not duplicate product instructions. Every module has a **Read** section that points to the relevant product documentation. Use those pages for the mechanics, then complete the architecture exercise and produce the requested design evidence.

## Architect responsibilities

In this learning path, a Data Architect is expected to:

- build ingestion pipelines and feed incremental or CDC data into CluedIn
- design business domains, vocabularies, mappings, identifiers, and edges
- build and tune matching projects without making operational merge decisions
- establish the first set of rules, using AI Agents where useful to accelerate rule design
- configure Export Targets and Streams and define downstream contracts
- validate that the Global Data Model represents the intended domain relationships
- promote architecture changes through environments with explicit validation gates

A Data Architect is not expected to clean data, turn enrichers on, merge records, or approve routine AI Agent remediation suggestions. Those are operational stewardship activities.

Workflow setup is intentionally outside the core course. An organization may choose to have Data Architects bootstrap the first workflows, but the core path assumes operational workflows are enabled and operated by Data Stewards or other process owners.

## Course outcomes

By the end of the course, you should be able to:

- build an ingestion design that supports initial and incremental data loads
- design coherent business domains, vocabularies, mappings, identifiers, and relations
- configure matching projects that produce explainable candidate groups for stewards
- create an initial rule set and validate its effect on golden records
- configure Export Targets and Streams for downstream consumers
- validate the resulting Global Data Model and record behavior
- promote changes through environments with clear validation gates

## Before you begin

Use a non-production environment and choose one representative domain or dataset that can be used throughout the course. Keep an architecture decision log containing assumptions, decisions, alternatives, expected behavior, validation evidence, and rollback considerations.

The learner should have authoritative access to the architectural features used in the course. Do not substitute broad organization-administrator access for the specific architecture permissions required by the exercises.

## Module sequence

1. [Architect responsibilities and environment strategy](https://documentation.cluedin.net/learning-paths/data-architect/course-purpose-and-environment-strategy.md)
2. [Business domains, vocabularies, golden records, and the Global Data Model](https://documentation.cluedin.net/learning-paths/data-architect/platform-model-business-domains-vocabularies-and-golden-records.md)
3. [Build ingestion pipelines and support incremental or CDC ingestion](https://documentation.cluedin.net/learning-paths/data-architect/ingestion-design-and-mapping-strategy.md)
4. [Design mappings, identifiers, and edges](https://documentation.cluedin.net/learning-paths/data-architect/identifiers-review-mapping-and-relations.md)
5. [Validate architecture through search, record history, and diagnostics](https://documentation.cluedin.net/learning-paths/data-architect/search-record-anatomy-and-diagnostics.md)
6. [Build the initial rule set and processing logic](https://documentation.cluedin.net/learning-paths/data-architect/initial-rules-and-processing-logic.md)
7. [Build matching projects and hand review to stewards](https://documentation.cluedin.net/learning-paths/data-architect/matching-projects-and-steward-handoff.md)
8. [Use AI Agents to accelerate initial rule design](https://documentation.cluedin.net/learning-paths/data-architect/ai-assisted-rule-design.md)
9. [Configure Export Targets](https://documentation.cluedin.net/learning-paths/data-architect/export-targets-and-destination-setup.md)
10. [Configure Streams and downstream contracts](https://documentation.cluedin.net/learning-paths/data-architect/streams-and-downstream-contracts.md)
11. [Release discipline across dev, test, and production](https://documentation.cluedin.net/learning-paths/data-architect/release-discipline-across-environments.md)
12. [Capstone: build and validate an end-to-end data pipeline](https://documentation.cluedin.net/learning-paths/data-architect/capstone-architecture-review.md)

## In this section

- [Architect responsibilities and environment strategy](https://documentation.cluedin.net/learning-paths/data-architect/course-purpose-and-environment-strategy.md) (tutorial): Define what the Data Architect owns in CluedIn, what belongs to Data Stewardship, and how architecture changes move safely through environments.
- [Business domains, vocabularies, golden records, and the Global Data Model](https://documentation.cluedin.net/learning-paths/data-architect/platform-model-business-domains-vocabularies-and-golden-records.md) (tutorial): Design the semantic model for a domain and validate that the resulting golden records and Global Data Model express the intended business structure.
- [Build ingestion pipelines and support incremental or CDC ingestion](https://documentation.cluedin.net/learning-paths/data-architect/ingestion-design-and-mapping-strategy.md) (tutorial): Design and validate an ingestion pipeline that brings source data into CluedIn reliably for both initial loads and ongoing incremental or CDC-style updates.
- [Design mappings, identifiers, and edges](https://documentation.cluedin.net/learning-paths/data-architect/identifiers-review-mapping-and-relations.md) (tutorial): Build mappings that establish stable identity, map source fields into the shared vocabulary, and create the relationships needed by the domain model.
- [Search, record anatomy, history, and diagnostic workflows](https://documentation.cluedin.net/learning-paths/data-architect/search-record-anatomy-and-diagnostics.md) (tutorial): Use Search, golden-record details, History, and relations as architecture validation surfaces.
- [Build the initial rule set and processing logic](https://documentation.cluedin.net/learning-paths/data-architect/initial-rules-and-processing-logic.md) (tutorial): Create the first set of architect-owned rules that establish durable processing behavior for the domain without taking on day-to-day data cleaning.
- [Build matching projects and hand review to stewards](https://documentation.cluedin.net/learning-paths/data-architect/matching-projects-and-steward-handoff.md) (tutorial): Configure a matching project that produces explainable duplicate candidates and define a clean handoff to Data Stewards for review and merge decisions.
- [Use AI Agents to accelerate initial rule design](https://documentation.cluedin.net/learning-paths/data-architect/ai-assisted-rule-design.md) (tutorial): Use AI Agents as a design aid for the initial architect-owned rule set while keeping rule intent, validation, and activation under explicit human control.
- [Configure Export Targets](https://documentation.cluedin.net/learning-paths/data-architect/export-targets-and-destination-setup.md) (tutorial): Configure and validate the destination connection that CluedIn will use to publish trusted data to a downstream system.
- [Configure Streams and downstream contracts](https://documentation.cluedin.net/learning-paths/data-architect/streams-and-downstream-contracts.md) (tutorial): Configure a Stream as an explicit downstream data contract covering population, identity, shape, change behavior, and relationships.
- [Release discipline across dev, test, and production](https://documentation.cluedin.net/learning-paths/data-architect/release-discipline-across-environments.md) (tutorial): Define validation gates for promoting ingestion, mapping, identity, matching, rule, Export Target, and Stream changes across environments.
- [Capstone: architecture review](https://documentation.cluedin.net/learning-paths/data-architect/capstone-architecture-review.md) (tutorial): Build and validate one representative CluedIn pipeline from source ingestion through semantic modeling, matching, initial rules, and downstream publishing, then hand operational decisions to Data Stewards.

Up: [Learning paths](https://documentation.cluedin.net/learning-paths.md)
