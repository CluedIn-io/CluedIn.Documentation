---
layout: cluedin
title: Data Architect course
parent: Learning paths
nav_order: 20
permalink: /learning-paths/data-architect-course
has_children: true
---

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

1. [Architect responsibilities and environment strategy](/learning-paths/data-architect-course/course-purpose-and-environment-strategy)
2. [Business domains, vocabularies, golden records, and the Global Data Model](/learning-paths/data-architect-course/platform-model-business-domains-vocabularies-and-golden-records)
3. [Build ingestion pipelines and support incremental or CDC ingestion](/learning-paths/data-architect-course/ingestion-design-and-mapping-strategy)
4. [Design mappings, identifiers, and edges](/learning-paths/data-architect-course/identifiers-review-mapping-and-relations)
5. [Validate architecture through search, record history, and diagnostics](/learning-paths/data-architect-course/search-record-anatomy-and-diagnostics)
6. [Build the initial rule set and processing logic](/learning-paths/data-architect-course/initial-rules-and-processing-logic)
7. [Build matching projects and hand review to stewards](/learning-paths/data-architect-course/matching-projects-and-steward-handoff)
8. [Use AI Agents to accelerate initial rule design](/learning-paths/data-architect-course/ai-assisted-rule-design)
9. [Configure Export Targets](/learning-paths/data-architect-course/export-targets-and-destination-setup)
10. [Configure Streams and downstream contracts](/learning-paths/data-architect-course/streams-and-downstream-contracts)
11. [Release discipline across dev, test, and production](/learning-paths/data-architect-course/release-discipline-across-environments)
12. [Capstone: build and validate an end-to-end data pipeline](/learning-paths/data-architect-course/capstone-architecture-review)
