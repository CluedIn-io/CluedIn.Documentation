---
layout: cluedin
title: Identifiers, review mapping, and relation design
parent: Data Architect course
grand_parent: Learning paths
nav_order: 40
permalink: /learning-paths/data-architect-course/identifiers-review-mapping-and-relations
---

## Learning outcome

Select defensible identifiers and design relations whose identity and business meaning remain clear after processing and export.

## Scenario

Your source contains several candidate identifiers and a property that links records to another domain. Choosing convenience over identity could cause false merges or misleading relations.

## Read

- [Review mapping](/integration/review-mapping)
- [Add relations between records](/getting-started/relations)
- [Create hierarchies](/getting-started/hierarchy-builder)

## Exercise

1. Evaluate candidate primary identifiers for uniqueness and stability.
2. Decide whether a single, generated, or compound identity strategy is appropriate.
3. Review any additional identifiers and state why each represents identity rather than similarity.
4. Design one relation: source property, target domain, edge type, and matching behavior.
5. Process representative records and inspect merge and relation outcomes.
6. Record the failure mode you are trying to prevent.

## Deliverable

An identity and relation decision record with assumptions, test evidence, expected edge behavior, and false-merge risk.

## Complete when

- The primary identifier has a documented identity rationale.
- Additional identifiers are justified individually.
- The relation has a clear business meaning and testable outcome.

## Next

Validate these architectural choices from the same search and record surfaces stewards will use.
