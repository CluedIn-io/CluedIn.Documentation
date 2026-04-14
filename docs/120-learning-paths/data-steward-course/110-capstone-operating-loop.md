---
layout: cluedin
title: Capstone operating loop and readiness checklist
parent: Data Steward course
grand_parent: Learning paths
nav_order: 110
permalink: /learning-paths/data-steward-course/capstone-operating-loop
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

The capstone turns the course into a realistic operating loop. The steward is given a data-quality symptom, then asked to move through the platform in the right order, choose the correct remediation tool, verify the outcome, and decide whether anything should be escalated.

## What you should get from this module

- combine search, validation, clean, deduplication, governance, and AI patterns into one operating flow
- practice tool selection instead of treating every issue the same way
- self-assess readiness for real stewardship work

![view_tagged_records.png]({{ "/assets/images/governance/tag-monitoring/monitor-tag-usage/Image/view_tagged_records.png" | relative_url }})

## Guided walkthrough

Use a realistic scenario such as one of the following:

- a tagged population of records with invalid phone values is rising over time
- a saved search shows many records with missing key attributes
- a domain contains suspicious duplicates after a new source was processed
- a recurring typo pattern keeps returning after being fixed once

Ask the learner to work through the issue in this order:

1. **Define scope** with search, saved search, glossary, or tags.
2. **Inspect evidence** on the results page and sample records.
3. **Check lifecycle clues** in History, validations, or review mapping.
4. **Choose remediation**:
   - clean project for repeated value issues
   - deduplication for suspected duplicate populations
   - AI job for scalable tagged remediation
   - escalation for mapping or identifier defects
5. **Verify the result** by returning to the saved search, tag view, or affected records.
6. **Record the lesson** as a repeatable stewardship practice or an architect handoff.

The main idea is deliberate tool choice. Not every problem needs a clean project. Not every recurring issue should stay manual. Not every duplicate symptom should be merged immediately.

## Role lens

By the end of this capstone, the learner should sound less like a ticket processor and more like an informed operator who understands evidence, scope, remediation, and platform consequences.

## Practice assignment

Run one full scenario end to end and write a short after-action review:

- What was the initial symptom?
- Which UI surfaces did you use first?
- What evidence changed your understanding of the problem?
- Which remediation path did you choose and why?
- What would you monitor next week to make sure the issue stays fixed?

## Exit criteria

- The learner can select the correct stewardship path for at least one realistic issue.
- The learner verifies outcomes instead of assuming fixes worked.
- The learner can distinguish operational remediation from structural escalation.

## Suggested source material

- [Search](/key-terms-and-features/search)
- [Validations](/integration/additional-operations-on-records/validations)
- [Manage a clean project](/preparation/clean/manage-clean-project)
- [Deduplicate data](/getting-started/data-deduplication)
- [Tag monitoring](/governance/tag-monitoring)
