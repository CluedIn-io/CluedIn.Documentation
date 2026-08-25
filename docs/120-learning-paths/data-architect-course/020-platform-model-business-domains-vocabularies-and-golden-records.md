---
layout: cluedin
title: Platform model: business domains, vocabularies, and golden records
parent: Data Architect course
grand_parent: Learning paths
nav_order: 20
permalink: /learning-paths/data-architect-course/platform-model-business-domains-vocabularies-and-golden-records
---

## Learning outcome

Design a coherent business domain and vocabulary model and explain how it supports understandable golden records.

## Scenario

A new entity type must be onboarded. Several teams use different names for the same concepts, and the resulting model needs to support search, stewardship, governance, and downstream reuse.

## Read

- [Golden records](/key-terms-and-features/golden-records)
- [Vocabulary](/management/data-catalog/vocabulary)

## Exercise

1. Choose one real or representative entity type.
2. Define its business domain and explain the boundary of that domain.
3. Design a vocabulary name, key prefix, ownership, and five to ten important keys.
4. Identify naming collisions or ambiguous concepts that should be resolved before ingestion.
5. Describe two stewardship questions and one downstream use case the model must support.
6. Record the decisions and rejected alternatives in your architecture decision log.

## Deliverable

A domain and vocabulary design with rationale, ownership, key examples, and operational use cases.

## Complete when

- Domain boundaries are understandable to someone outside the implementation team.
- Vocabulary keys use consistent business meaning and naming.
- You can explain how the design improves search, governance, and golden-record interpretation.

## Next

Apply the semantic model while designing ingestion and mappings.
