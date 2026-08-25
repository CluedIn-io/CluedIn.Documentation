---
layout: cluedin
title: Ingestion design and mapping strategy
parent: Data Architect course
grand_parent: Learning paths
nav_order: 30
permalink: /learning-paths/data-architect-course/ingestion-design-and-mapping-strategy
---

## Learning outcome

Design and review an ingestion mapping for stable identity, searchability, stewardship, and downstream use rather than only successful loading.

## Scenario

A source can be imported successfully, but you need to decide whether its dataset boundaries and mapping will remain understandable and safe after processing.

## Read

- [Ingest data](/getting-started/data-ingestion)
- [Review mapping](/integration/review-mapping)

## Exercise

1. Use one training dataset and review its source grouping and dataset boundary.
2. Choose or review the target business domain and vocabulary.
3. Review display fields, data types, ignored fields, and fields needed for diagnostics or export.
4. Choose a candidate primary identifier and state the assumptions behind it.
5. Process in a safe environment and inspect representative records in Search.
6. Record any mismatch between intended mapping semantics and visible processed behavior.

## Deliverable

A mapping review containing semantic choices, identifier assumptions, retained diagnostic fields, expected downstream behavior, and validation evidence.

## Complete when

- The mapping has an explicit semantic rationale.
- Identity and searchability consequences are documented before production use.
- Processed examples support the intended design.

## Next

Deepen the identity design and define relations between records.
