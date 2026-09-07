---
layout: cluedin
title: Release discipline across dev, test, and production
parent: Data Architect course
grand_parent: Learning paths
nav_order: 110
permalink: /learning-paths/data-architect/release-discipline-across-environments
content_type: tutorial
redirect_from: ["/learning-paths/data-architect-course/release-discipline-across-environments"]
source_path: docs/120-learning-paths/data-architect-course/110-release-discipline-across-environments.md
---

## Learning outcome

Define validation gates for promoting ingestion, mapping, identity, matching, rule, Export Target, and Stream changes across environments.

## Scenario

An architecture change works in development and the team wants it in production. You need to prove not only that the configuration can be promoted, but that ingestion, golden records, matching behavior, and downstream delivery remain correct.

## Read

Use the documentation for the change types you are promoting:

- [Ingest data](/ingest/tutorial-ingest-data)
- [Review mapping](/ingest/mapping/review-mapping)
- [Deduplicate data](/master/deduplication/tutorial-deduplicate-data)
- [Create rules](/govern/rules/tutorial-create-rules)
- [Export targets](/publish/export-targets)
- [Stream data](/publish/streams/tutorial-stream-data)

## Exercise

1. Choose one representative architecture change from the course.
2. Define what is tested in development and what additional evidence is required in test.
3. Define ingestion and record-level validation for mapping, identity, matching, or rule changes.
4. Define connection and downstream validation for Export Target or Stream changes.
5. Define Steward acceptance criteria when the change affects matching review or another operational workflow.
6. Define post-production monitoring and rollback or mitigation steps.

## Deliverable

A promotion checklist with change scope, development evidence, test gate, production verification, monitoring, handoff, and rollback notes.

## Complete when

- Production is not used as an experimentation environment.
- Each architect-owned change type has an observable validation gate.
- Steward acceptance is included where architecture changes alter operational work.
- Post-release verification and mitigation are planned before promotion.

## Next

Continue to [Capstone: build and validate an end-to-end data pipeline](/learning-paths/data-architect/capstone-architecture-review).
