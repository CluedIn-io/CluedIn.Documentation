---
layout: cluedin
title: Streams, export targets, and downstream contracts
parent: Data Architect course
grand_parent: Learning paths
nav_order: 100
permalink: /learning-paths/data-architect-course/streams-export-targets-and-downstream-contracts
---

## Learning outcome

Define a stream as an explicit downstream data contract covering population, identity, shape, change behavior, and relationships.

## Scenario

A consuming system needs trusted records from CluedIn. Configuring a destination is not enough: consumers need to know which records appear, what identity means, and what happens after corrections or merges.

## Read

- [Stream data](/getting-started/data-streaming)
- [Create hierarchies](/getting-started/hierarchy-builder)
- [Work with glossary](/getting-started/glossary)
- [Add relations between records](/getting-started/relations)

## Exercise

1. Choose a target consumer and define the population to export.
2. Select synchronized or event-log behavior using the documented stream model.
3. Define exported properties and identity expectations.
4. Decide whether relations or hierarchy edges belong in the contract.
5. Describe how corrections, merges, and population changes should appear downstream.
6. Define a consumer-facing validation test before release.

## Deliverable

A downstream contract containing audience, selection logic, mode, schema expectations, identity, edge behavior, change semantics, and acceptance test.

## Complete when

- The stream has a business contract, not only technical configuration.
- Consumers can explain how later data corrections will affect them.
- The release has an observable acceptance test.

## Next

Put the architecture under controlled promotion and verification across environments.
