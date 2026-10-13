---
title: Release discipline across dev, test, and production
url: https://documentation.cluedin.net/learning-paths/data-architect/release-discipline-across-environments
content_type: tutorial
section: Learning paths > Data Architect course
---

# Release discipline across dev, test, and production

> tutorial: Guided end-to-end learning.

## Learning outcome

Define validation gates for promoting ingestion, mapping, identity, matching, rule, Export Target, and Stream changes across environments.

## Scenario

An architecture change works in development and the team wants it in production. You need to prove not only that the configuration can be promoted, but that ingestion, golden records, matching behavior, and downstream delivery remain correct.

## Read

Use the documentation for the change types you are promoting:

- [Ingest data](https://documentation.cluedin.net/ingest/tutorial-ingest-data.md)
- [Review mapping](https://documentation.cluedin.net/ingest/mapping/review-mapping.md)
- [Deduplicate data](https://documentation.cluedin.net/master/deduplication/tutorial-deduplicate-data.md)
- [Create rules](https://documentation.cluedin.net/govern/rules/tutorial-create-rules.md)
- [Export targets](https://documentation.cluedin.net/publish/export-targets.md)
- [Stream data](https://documentation.cluedin.net/publish/streams/tutorial-stream-data.md)

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

Continue to [Capstone: build and validate an end-to-end data pipeline](https://documentation.cluedin.net/learning-paths/data-architect/capstone-architecture-review.md).

Up: [Data Architect course](https://documentation.cluedin.net/learning-paths/data-architect.md)
