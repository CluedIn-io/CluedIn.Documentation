---
layout: cluedin
title: Release discipline across dev, test, and production
parent: Data Architect course
grand_parent: Learning paths
nav_order: 110
permalink: /learning-paths/data-architect-course/release-discipline-across-environments
---

## Learning outcome

Define validation gates for promoting mapping, identity, rule, governance, and stream changes across environments.

## Scenario

A change works in development and the team wants it in production. You need to prove not only that the configuration can be promoted, but that the resulting records and downstream behavior remain correct.

## Read

Use the documentation for the change types you are promoting:

- [Review mapping](/integration/review-mapping)
- [Create rules](/getting-started/rule-builder)
- [Stream data](/getting-started/data-streaming)
- [Tag monitoring](/governance/tag-monitoring)

## Exercise

1. Choose one representative architecture change.
2. Define what is tested in development and what additional evidence is required in test.
3. Define record-level validation for mapping, identity, or rule changes.
4. Define downstream validation for stream-related changes.
5. Define steward acceptance criteria when the change affects operational workflows.
6. Define post-production monitoring and rollback or mitigation steps.

## Deliverable

A promotion checklist with change scope, dev evidence, test gate, production verification, monitoring, and rollback notes.

## Complete when

- Production is not used as an experimentation environment.
- Each change type has an observable validation gate.
- Post-release verification and mitigation are planned before promotion.

## Next

Apply the entire course to an end-to-end architecture review.
