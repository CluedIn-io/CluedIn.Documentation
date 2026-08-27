---
layout: cluedin
title: Design mappings, identifiers, and edges
parent: Data Architect course
grand_parent: Learning paths
nav_order: 40
permalink: /learning-paths/data-architect-course/identifiers-review-mapping-and-relations
---

## Learning outcome

Build mappings that establish stable identity, map source fields into the shared vocabulary, and create the relationships needed by the domain model.

## Scenario

The source data is arriving, but records will only become useful if the mapping produces stable identifiers, understandable properties, and correct relationships to other business domains.

## Read

- [Review mapping](/integration/review-mapping)
- [Add relations between records](/getting-started/relations)

## Exercise

1. Review the source fields and choose the primary identifier based on uniqueness and stability.
2. Identify any additional identifiers needed to match the same business object across sources.
3. Map source properties into the vocabulary defined earlier in the course.
4. Identify source keys that should produce edges or relations to other business domains.
5. Configure the mapping and process a representative sample.
6. Inspect the resulting golden records and confirm that identifiers and relations behave as designed.
7. Record at least one failure mode caused by an unstable identifier, incorrect mapping, or missing relationship key.

## Deliverable

A mapping and identity design containing vocabulary mappings, identifier rationale, expected edges, validation evidence, and known failure modes.

## Complete when

- Identity is based on a stable business key rather than convenience.
- Source-specific fields are translated into the shared model deliberately.
- Expected edges appear on the resulting records and can be explained from source data.

## Next

Continue to [Search, record anatomy, history, and diagnostic workflows](/learning-paths/data-architect-course/search-record-anatomy-and-diagnostics).
