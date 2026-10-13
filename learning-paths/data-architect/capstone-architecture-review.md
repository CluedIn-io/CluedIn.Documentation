---
title: Capstone: architecture review
url: https://documentation.cluedin.net/learning-paths/data-architect/capstone-architecture-review
content_type: tutorial
section: Learning paths > Data Architect course
---

# Capstone: architecture review

> tutorial: Guided end-to-end learning.

## Learning outcome

Build and validate one representative CluedIn pipeline from source ingestion through semantic modeling, matching, initial rules, and downstream publishing, then hand operational decisions to Data Stewards.

## Scenario

You are responsible for bringing a new business domain into CluedIn and making it ready for operational stewardship and downstream consumption. The implementation must be structurally sound before Stewards begin cleaning data, reviewing duplicate groups, or approving remediation.

## Read

Review the canonical documentation needed for the implementation:

- [Ingest data](https://documentation.cluedin.net/ingest/tutorial-ingest-data.md)
- [Golden records](https://documentation.cluedin.net/get-started/core-concepts/golden-records.md)
- [Review mapping](https://documentation.cluedin.net/ingest/mapping/review-mapping.md)
- [Vocabulary](https://documentation.cluedin.net/model/vocabularies/manage-vocabularies.md)
- [Deduplicate data](https://documentation.cluedin.net/master/deduplication/tutorial-deduplicate-data.md)
- [Create rules](https://documentation.cluedin.net/govern/rules/tutorial-create-rules.md)
- [Export targets](https://documentation.cluedin.net/publish/export-targets.md)
- [Stream data](https://documentation.cluedin.net/publish/streams/tutorial-stream-data.md)

## Exercise

Build or review one representative domain across these areas:

1. Source integration and initial plus incremental or CDC ingestion.
2. Business domain and vocabulary design.
3. Mapping, identifiers, and edges.
4. Golden-record and Global Data Model validation.
5. Matching-project configuration and candidate quality.
6. Initial architect-owned rule set.
7. Export Target configuration and health.
8. Stream population, schema, identity, relations, and change behavior.
9. Promotion and validation gates across environments.
10. Handoff to Data Stewards for cleaning, duplicate review and merge decisions, enrichers, and routine AI-assisted remediation.

For every architecture decision, capture evidence, expected behavior, validation method, owner, and rollback or mitigation approach.

Do not complete Steward activities as part of the capstone. The goal is to prove that the architecture produces a trustworthy operating surface for Stewards and downstream consumers.

## Deliverable

An end-to-end architecture package containing the ingestion design, semantic model, mapping and identity decisions, matching configuration, initial rules, downstream contract, validation evidence, release checklist, and Steward handoff.

## Complete when

- Initial and incremental data reach CluedIn through a repeatable ingestion path.
- Golden records, identifiers, edges, and the Global Data Model reflect the intended business model.
- Matching projects produce explainable candidates without the Architect performing merge review.
- Initial rules behave as designed on representative records.
- Export Targets and Streams pass downstream acceptance tests.
- Operational remediation responsibilities are explicitly handed to Data Stewards.

## Next

You have completed the Data Architect learning path. Return to the [Data Architect course overview](https://documentation.cluedin.net/learning-paths/data-architect.md) to review the full path.

Up: [Data Architect course](https://documentation.cluedin.net/learning-paths/data-architect.md)
