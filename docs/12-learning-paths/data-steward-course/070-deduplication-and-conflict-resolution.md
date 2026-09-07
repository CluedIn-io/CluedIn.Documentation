---
layout: cluedin
title: Resolve duplicates and understand merge decisions
parent: Data Steward course
grand_parent: Learning paths
nav_order: 70
permalink: /learning-paths/data-steward/deduplication-and-conflict-resolution
content_type: tutorial
redirect_from: ["/learning-paths/data-steward-course/deduplication-and-conflict-resolution"]
source_path: docs/120-learning-paths/data-steward-course/070-deduplication-and-conflict-resolution.md
---

## Learning outcome

Review duplicate candidates conservatively, justify a merge decision, and recognize when duplicate symptoms indicate an identity-design problem.

## Scenario

Two records appear to describe the same real-world entity, but some fields disagree. You must decide whether to merge them or keep them separate.

## Read

- [Deduplicate data](/master/deduplication/tutorial-deduplicate-data)
- [Review mapping](/ingest/mapping/review-mapping)
- [History](/master/golden-records/history)

## Exercise

1. Open or create a deduplication project in a training domain.
2. Select one duplicate group and list the evidence supporting a match.
3. List any conflicting evidence that could indicate distinct entities.
4. Decide whether to merge, reject, or defer the candidate and record why.
5. If you merge, inspect the resulting record and its History.
6. Decide whether the duplicate pattern suggests weak identifiers, mappings, or source harmonization.

## Deliverable

A duplicate-review note containing the candidate evidence, decision, conflict handling, post-merge verification if applicable, and any architecture escalation.

## Complete when

- You can distinguish exact identifier-driven consolidation from fuzzy duplicate review.
- Your merge decision is supported by evidence.
- You know when repeated duplicate symptoms require architectural investigation.

## Next

Continue to [Use glossary, tags, and governance views to organize work](/learning-paths/data-steward/glossary-tags-and-governance).
