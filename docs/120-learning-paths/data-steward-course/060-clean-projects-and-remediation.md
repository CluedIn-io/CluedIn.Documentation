---
layout: cluedin
title: Clean recurring quality issues with clean projects
parent: Data Steward course
grand_parent: Learning paths
nav_order: 60
permalink: /learning-paths/data-steward-course/clean-projects-and-remediation
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

Clean projects are where stewardship becomes systematic. They let the learner move beyond one-off edits and work on recurring patterns of bad data with a repeatable workflow.

## What you should get from this module

- create and run clean projects from a targeted record set
- use the clean application efficiently for bulk remediation
- understand when generated rules should take over future prevention

![manage-clean-project-3.png]({{ "/assets/images/preparation/clean/manage-clean-project-3.png" | relative_url }})

## Guided walkthrough

Start from the manual data cleaning guide, then deepen it using the more detailed preparation documentation.

### Find the right slice of data
Good clean projects start from a well-defined search or tagged set of records. The learner should not open Clean until they know exactly which records and which properties need attention.

### Create the clean project
Show how a search can become a clean project. Then explain why selecting only the relevant properties matters: the project should expose the problem clearly, not overwhelm the steward with every column in the record.

### Generate results
Emphasize that Clean works on a snapshot. This matters. The learner is not editing a live synchronized spreadsheet. They are operating on a captured slice of data that may need regeneration later.

### Clean data efficiently
Use the clean-application concepts to teach efficient behavior:
- common transforms for broad normalization
- text facets for repeated variants
- cluster-and-edit for near-duplicate representations
- single-cell editing only when truly necessary

### Process cleaned data
Explain stale-data strategy in plain language and show why automatic rule generation is important. A steward should not want to solve the same issue manually forever. When the clean project reveals a durable pattern, generated rules or architect-authored rules should prevent recurrence.

### Revert and regenerate
These features teach humility. Sometimes a cleaning attempt was wrong or incomplete. The learner needs to know that remediation can be undone and that fresh snapshots can be loaded when data has moved on.

## Role lens

The steward's target is not just cleaner records. The real target is a lower volume of repeated manual work over time. Clean projects are successful when they both fix current records and inform better future automation.

## Practice assignment

Choose one recurring issue from a saved search and turn it into a clean project.

- Generate results.
- Use a bulk cleaning technique rather than only single-cell edits.
- Process the project.
- Review whether rule auto-generation should remain enabled.
- Verify the outcome by returning to the saved search or affected records.

Then write down whether the issue should continue to be owned by stewardship or moved into rules or source correction.

## Exit criteria

- The learner can create a focused clean project from a search result set.
- The learner uses at least one bulk-cleaning method appropriately.
- The learner understands snapshot behavior, processing, and rule generation.

## Suggested source material

- [Clean data](/getting-started/manual-data-cleaning)
- [Clean](/preparation/clean)
- [Manage a clean project](/preparation/clean/manage-clean-project)
