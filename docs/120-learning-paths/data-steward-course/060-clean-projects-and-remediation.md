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

Clean projects are one of the most practical stewardship tools in CluedIn. They let you define a target set of records, load the relevant fields into a focused clean application, apply bulk remediation, and publish corrected values back into the operational golden records.

![manage-clean-project-3.png]({{ "/assets/images/preparation/clean/manage-clean-project-3.png" | relative_url }})

## What this module teaches

By the end of this module, you should be able to:

- explain what a clean project is and when to use it
- build a clean project from a saved search or tagged record set
- understand how clean-project snapshots work
- use the clean application effectively
- process cleaned data safely and verify the outcome

## What a clean project is

A clean project is a focused remediation container. It takes a defined subset of records and fields and prepares them for steward-driven correction.

Use a clean project when:

- the issue affects multiple records
- the issue is repetitive
- manual one-by-one editing would be wasteful
- you need an audit-friendly, repeatable remediation unit
- the records already exist operationally and need improvement now

Do **not** reach for a clean project first when the issue is clearly a mapping or identifier design flaw. In that case, fix today’s records if needed, but escalate the root cause too.

## The three phases of clean work

### 1. Define the target set

Usually this starts with search, filters, tags, or a glossary term.

A good target set is:

- small enough to understand
- broad enough to matter
- precise enough that nearly every returned record belongs in the same remediation workflow

### 2. Generate results

This loads a **snapshot** of the targeted values into the clean application.

This point is critical: you are not cleaning a live infinite stream of changing values. You are cleaning a captured working set.

### 3. Process cleaned data

After your edits are ready, processing publishes corrected values back into CluedIn and updates the affected golden records.

## Why snapshots matter

New stewards often assume a clean project is live and always current. It is not. When you generate results, you capture the data state at that moment.

This has consequences:

- new matching records are not automatically included
- if more bad data arrives later, you may need to regenerate or run another project
- if you regenerate before processing, you can lose in-progress work

This is why discipline matters in clean work.

## How to create a strong clean project

A strong clean project begins before you click **Clean**.

### Step 1: prove the issue in search

Before creating the project, make sure:

- the issue is visible in your result set
- the right columns are present
- the scope feels operationally correct
- you can name the issue clearly

### Step 2: keep only relevant fields

When creating the project, remove fields that do not need remediation. This keeps the clean application focused and lowers cognitive noise.

### Step 3: choose the right remediation level

Ask:

- Is this a typo cluster?
- Is this whitespace or casing?
- Is this a standardization exercise?
- Is this missing-data completion?
- Is this something AI might help with later instead?

## Working inside the clean application

The clean application is built for bulk remediation, not random editing.

### Good steward behavior inside Clean

Prefer the most scalable safe action available:

- common transforms for formatting issues
- text facets for repeated values
- cluster and edit for near-duplicates or alternative representations
- one-cell editing only when the issue is genuinely isolated

![manage-clean-project-4.png]({{ "/assets/images/preparation/clean/manage-clean-project-4.png" | relative_url }})

### Common transforms

Use these for mechanical normalization:

- trim whitespace
- collapse repeated whitespace
- title case or upper/lower case where appropriate

These are efficient and often predictable.

### Text facets

Use text facets when the same wrong value appears many times and should become one correct value.

This is excellent for:

- misspellings
- inconsistent abbreviations
- repeated formatting errors

### Cluster and edit

Use clustering when many different textual variants are likely intended to mean the same thing.

This is excellent for:

- organization names with slight differences
- location or department variants
- free-text inconsistencies

### Single-cell editing

Use this sparingly. It is the least scalable option and usually means either:

- the case is genuinely one-off
- the project scope is too broad and mixed
- you need a different remediation strategy

## Processing cleaned data

When you process cleaned data, you send corrected values back into CluedIn.

Two decisions matter here:

### Stale data strategy

You may need to decide whether to skip stale data or write stale data. In steward terms:

- **Skip stale data** is the safer option when you do not want older project snapshots to overwrite more recent operational truth
- **Write stale data** is riskier and should be used only when you are confident your project values should still win

### Rules auto generation

If your cleaning actions are significant and repeatable, CluedIn can generate rules based on those actions.

This matters because a steward’s best result is often not just fixing today’s bad values, but preventing tomorrow’s copies of the same issue.

![process-cleaned-data.png]({{ "/assets/images/preparation/clean/process-cleaned-data.png" | relative_url }})

## How to verify a clean project worked

A steward should always verify after processing.

Use this sequence:

1. reopen the original saved search
1. confirm the count of affected records is lower or zero
1. open a few representative corrected records
1. check History or Topology if the record structure matters
1. confirm no unexpected side effects appeared

If a stream exports the cleaned records downstream, remember that your changes may now have external impact too.

## When to generate rules from clean behavior

Rules generated from clean work are useful when:

- the transformation is repeatable
- the same source pattern appears often
- the operation is deterministic
- you want future records to arrive cleaner without repeating manual work

Do not assume every clean action should become a rule. One-off business judgement should usually remain manual.

## When to archive, duplicate, or regenerate

### Archive a clean project when

- the work is complete
- the project is no longer needed operationally
- the issue is now handled by rules or upstream correction

### Duplicate a clean project when

- you want the same scope but a different remediation approach
- you want to preserve one project while exploring another

### Regenerate when

- new matching data has arrived
- you are done with the current cycle
- you understand that regeneration resets the working snapshot

## Common mistakes

### Mistake: creating a clean project before proving the scope

This creates noisy projects and poor remediation quality.

### Mistake: using one-cell edits for repeated problems

That is slow and does not teach the platform anything durable.

### Mistake: processing without verification

A steward must always prove the outcome.

### Mistake: treating Clean as a substitute for root-cause design

Clean is operational remediation, not a replacement for good mapping, validation, or rule design.

## Practice exercise

Build or review one clean-project scenario and answer:

- What exact issue is the project solving?
- Why is Clean the right tool instead of deduplication or direct source correction?
- Which fields belong in scope?
- Which operation would you use first: transform, facet, cluster, or single-cell edit?
- After processing, how would you verify success?

## You are ready for the next module when

You can explain:

- why clean projects operate on snapshots
- how to choose the right level of editing inside the clean application
- when to process with caution
- when a clean project should lead to rule generation or architectural escalation

## What comes next

Next you will handle another major stewardship workflow: duplicates. This is where many learners get nervous, because deduplication changes structure, not just values. The next module teaches you how to review duplicates safely.
