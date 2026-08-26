---
layout: cluedin
title: Business domains, vocabularies, golden records, and the Global Data Model
parent: Data Architect course
grand_parent: Learning paths
nav_order: 20
permalink: /learning-paths/data-architect-course/platform-model-business-domains-vocabularies-and-golden-records
---

## Learning outcome

Design the semantic model for a domain and validate that the resulting golden records and Global Data Model express the intended business structure.

## Scenario

A new source uses its own terminology and identifiers. Before building mappings, you need a stable semantic model that downstream teams and Data Stewards can understand.

## Read

- [Golden records](/key-terms-and-features/golden-records)
- [Vocabulary](/management/data-catalog/vocabulary)
- [Business domains](/management/entity-type)

## Exercise

1. Define the business domain represented by your training data.
2. Define the vocabulary and naming conventions that should survive beyond any one source system.
3. Identify the properties that are business identifiers, descriptive attributes, and relationship keys.
4. Record how source-specific field names map conceptually into the shared model.
5. Process a representative sample and inspect the resulting golden records.
6. Open the Global Data Model and verify that the expected business domains and relationships are visible and understandable.
7. Record any modeling change required before ingestion design continues.

## Deliverable

A semantic-model decision record containing domain boundaries, vocabulary decisions, key properties, expected relationships, and Global Data Model validation notes.

## Complete when

- The model is expressed in business terms rather than source-system terminology.
- Golden records expose the properties needed for identity and downstream use.
- The Global Data Model reflects the intended domain relationships.

## Next

Continue to [Build ingestion pipelines and support incremental or CDC ingestion](/learning-paths/data-architect-course/ingestion-design-and-mapping-strategy).
