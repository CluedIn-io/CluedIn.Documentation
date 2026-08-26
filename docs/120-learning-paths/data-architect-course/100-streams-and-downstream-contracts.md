---
layout: cluedin
title: Configure Streams and downstream contracts
parent: Data Architect course
grand_parent: Learning paths
nav_order: 100
permalink: /learning-paths/data-architect-course/streams-and-downstream-contracts
---

## Learning outcome

Configure a Stream as an explicit downstream data contract covering population, identity, shape, change behavior, and relationships.

## Scenario

The Export Target is healthy. You now need to define exactly which trusted records CluedIn publishes, which properties and relations are included, and how downstream consumers experience changes over time.

## Read

- [Stream data](/getting-started/data-streaming)
- [Add relations between records](/getting-started/relations)

## Exercise

1. Choose the Export Target configured in the previous module.
2. Define the business population that belongs in the Stream.
3. Select the appropriate streaming mode for the consumer.
4. Define exported properties, identity expectations, and any relations or edges that belong in the contract.
5. Configure the Stream and its Export Target connection.
6. Test a representative create or update and confirm the downstream behavior.
7. Describe how later corrections or steward-approved merges should appear downstream without performing those stewardship actions yourself.
8. Define a consumer-facing acceptance test and monitoring expectations.

## Deliverable

A downstream contract containing audience, selection logic, mode, schema expectations, identity, edge behavior, change semantics, and acceptance test.

## Complete when

- The Stream has a business contract, not only technical configuration.
- The consumer can explain identity and change behavior.
- The configured Stream and Export Target pass an observable acceptance test.

## Next

Put the architecture under controlled promotion and verification across environments.
