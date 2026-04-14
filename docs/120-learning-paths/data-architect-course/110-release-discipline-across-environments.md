---
layout: cluedin
title: Release discipline across dev, test, and production
parent: Data Architect course
grand_parent: Learning paths
nav_order: 110
permalink: /learning-paths/data-architect-course/release-discipline-across-environments
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

The documentation is strong on individual product surfaces, but real implementations fail or succeed on promotion discipline. This module turns the course into an environment-aware architecture practice.

## What you should get from this module

- treat CluedIn changes as promotable architecture, not ad hoc UI edits
- define test criteria before moving changes forward
- separate experimentation from production operation

## Guided walkthrough

This module is intentionally process-heavy because the technical parts have already been covered elsewhere.

In **Development**, the architect should:
- explore mapping alternatives
- test identifier strategies
- draft rules
- experiment with enrichment and stream design
- deliberately create bad examples to prove diagnostic behavior

In **Test**, the architect should:
- validate with realistic data volumes and shapes
- involve stewards in workflow walkthroughs
- verify search usability, duplicate behavior, and tag or glossary clarity
- confirm downstream export structure and change behavior

In **Production**, the architect should:
- promote only tested patterns
- monitor post-release behavior
- provide handoff notes and rollback thinking
- avoid using production as a discovery surface

Tie this back to the rest of the course. Every change class should have explicit validation:
- mapping changes validated in search and sample records
- identifier changes validated with merge-risk review
- rules validated through reprocessing expectations
- stream changes validated through downstream contract checks
- governance changes validated through tag or queue clarity

The architect should also define how steward feedback feeds future releases. Production teaches, but it should teach through observation and measured follow-up, not uncontrolled experimentation.

## Role lens

Release discipline is architecture in motion. Without it, even good designs become operational risk.

## Practice assignment

Create a one-page promotion checklist covering:

- mapping and identifier changes
- rule changes
- glossary or tag changes
- stream changes
- expected post-release monitoring
- rollback or mitigation notes

## Exit criteria

- The learner can explain what belongs in dev, test, and production.
- The learner can define validation gates for major CluedIn change types.
- The learner sees promotion discipline as part of architecture, not admin overhead.

## Suggested source material

- [Review mapping](/integration/review-mapping)
- [Create rules](/getting-started/rule-builder)
- [Stream data](/getting-started/data-streaming)
- [Tag monitoring](/governance/tag-monitoring)
