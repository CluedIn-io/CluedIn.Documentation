---
layout: cluedin
title: Use AI agents safely for stewardship work
parent: Data Steward course
grand_parent: Learning paths
nav_order: 90
permalink: /learning-paths/data-steward-course/ai-assisted-stewardship
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

AI is useful in stewardship when it shortens repetitive remediation work without weakening review discipline. The current documentation is strongest around built-in AI agents and AI-assisted repair launched from Tag Monitoring, so this module teaches practical use rather than abstract hype.

## What you should get from this module

- understand what the built-in Data Steward agent is meant to help with
- launch AI-assisted remediation from a tagged population responsibly
- treat AI as a force multiplier, not a substitute for review

![fix_with_ai_panel.png]({{ "/assets/images/governance/tag-monitoring/fix-records-with-ai/Images/fix_with_ai_panel.png" | relative_url }})

## Guided walkthrough

Return to the built-in AI agents page and remind the learner that the Data Steward agent is documented with two default purposes: fixing data quality issues and looking for duplicates. Then connect that description to the more concrete Tag Monitoring flow.

In the documented AI-assisted governance workflow, the learner:

1. opens Tag Monitoring
2. selects a tag
3. chooses **Fix Data Quality Issues with AI**
4. creates an AI job
5. reviews the prefilled **Data** and **Skills** sections
6. tests the job
7. runs it
8. reviews the results
9. returns to Tag Monitoring to verify whether the flagged volume decreased

The most important lesson here is restraint. The learner should never treat AI as an opaque cleanup button. They should test on a scoped set, review instructions carefully, confirm the job is working on the intended records, and inspect outcomes afterwards.

Also explain where AI is especially useful:
- repeated formatting issues at scale
- large tagged populations with a clear corrective intent
- exploratory duplicate discovery that still needs human review

And where AI should be used carefully:
- ambiguous business rules
- high-risk identity merges
- cases where the source system is authoritative and manual platform fixes would merely mask a deeper issue

## Role lens

The steward's job with AI is not to surrender judgment. It is to add leverage while preserving accountability. The steward remains responsible for scope selection, testing, review, and post-run verification.

## Practice assignment

From a tagged population in a safe environment:

- create an AI job
- inspect the automatically populated data scope
- add any clarifying instructions needed
- test the job before a broader run
- review the results and return to the tag view to see whether the queue changed

Write down one case where AI clearly helped and one case where you would still prefer manual or architect-led remediation.

## Exit criteria

- The learner can describe the documented AI-assisted remediation workflow.
- The learner knows how to test and review an AI job before trusting it.
- The learner understands where AI is appropriate and where caution is needed.

## Suggested source material

- [Built-in AI agents](/management/ai-agents/built-in-ai-agents)
- [Tag monitoring](/governance/tag-monitoring)
