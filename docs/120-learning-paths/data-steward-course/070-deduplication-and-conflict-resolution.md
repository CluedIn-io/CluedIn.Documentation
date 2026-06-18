---
layout: cluedin
title: Resolve duplicates and understand merge decisions
parent: Data Steward course
grand_parent: Learning paths
nav_order: 70
permalink: /learning-paths/data-steward-course/deduplication-and-conflict-resolution
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

Deduplication is where stewardship becomes structural. You are no longer just correcting a bad value. You are deciding whether multiple records represent the same real-world entity and, if they do, how their conflicting values should be combined into a trusted result.

![dedup-8.png]({{ "/assets/images/getting-started/deduplication/dedup-8.png" | relative_url }})

## What this module teaches

By the end of this module, you should be able to:

- explain what deduplication is for
- understand how matching rules identify candidate duplicates
- review duplicate groups safely
- make sensible conflict-resolution decisions
- recognize when repeated duplicate problems point to identifier or mapping issues

## Deduplication versus identifiers

A steward needs one distinction burned into memory:

- **identifier merging** is strict and usually happens on the fly during processing
- **deduplication** is a project-based review process for likely matches, often using fuzzier criteria

Why this matters:

- if duplicates keep showing up, the identifier strategy may be too weak
- if records keep merging incorrectly, the identifier strategy may be too aggressive
- deduplication can fix current operational duplicates, but it may also reveal design issues that need escalation

## What a deduplication project does

A deduplication project scopes the review to a business domain and applies matching logic to identify groups of records that may represent the same entity.

The steward then reviews those groups and decides:

- whether they are true duplicates
- which values should survive
- whether the merge should proceed

This is a high-impact action. Use care.

## How matching rules work in steward terms

A matching rule does not prove that two records are the same. It identifies records that are similar enough to deserve review.

A matching rule usually defines:

- the vocabulary key to compare
- the matching function
- one or more criteria

The quality of a deduplication project depends heavily on the quality of the criteria.

A steward should ask:

- does this key have real identity meaning?
- is the business domain narrow enough?
- are we likely to catch true duplicates without producing too many false positives?

![dedup-6.png]({{ "/assets/images/getting-started/deduplication/dedup-6.png" | relative_url }})

## What to do when results are generated

When deduplication results are generated, records are grouped into likely duplicate sets. Do not rush into merge.

Review each group with the following mindset:

- Are these records truly the same real-world thing?
- Do the matching values reflect identity, or just coincidence?
- Would merging hide an important distinction?
- Are conflicting values acceptable or suspicious?
- Would this group be better prevented through identifiers or source cleanup?

## The fix conflicts step

When you open a duplicate group, CluedIn separates:

- **Conflicting** values
- **Matching** values

This is where the steward’s judgement matters.

### How to choose values responsibly

Prefer values that are:

- more complete
- more trustworthy
- more recent when recency makes sense
- aligned with known business reality
- less likely to propagate obvious defects downstream

Do not choose a value only because it is filled in. A filled-in value can still be wrong.

![dedup-9.png]({{ "/assets/images/getting-started/deduplication/dedup-9.png" | relative_url }})

## Preview before merge

The preview step matters because it shows what the merged record will look like before the change becomes real.

Use preview to ask:

- Does the merged result look coherent?
- Are there hidden collisions in important fields?
- Would a downstream consumer misunderstand this record after merge?
- Are we about to combine two entities that merely look similar?

If the answer feels uncertain, stop and investigate more.

## Merge strategy and future data

When you confirm a merge, CluedIn may also ask how more recent data should be handled. This matters because deduplication is not a one-time fantasy world. New incoming data will continue to arrive.

A steward should think beyond the current click:

- Will future source data reinforce this merge?
- Could future data reintroduce confusion?
- Should the architect revisit identifiers to reduce repeat work?

![dedup-12.png]({{ "/assets/images/getting-started/deduplication/dedup-12.png" | relative_url }})

## How to verify a merge

After merging, verify in multiple ways:

- check that the duplicate group has been resolved
- search for the entity again
- inspect the resulting golden record
- review Topology or History if the structure is important
- confirm that the merged result still tells a sensible business story

A merge is not “done” until the surviving record looks trustworthy.

## Common duplicate scenarios

### Scenario 1: obvious duplicates with small formatting differences

These are usually safe candidates if the identifying fields line up strongly.

### Scenario 2: duplicates with conflicting contact or descriptive data

These require more caution. One source may be stale, or the records may actually represent different real-world entities.

### Scenario 3: large numbers of near-duplicates from one source

This often signals a deeper issue with source quality or identifier design.

### Scenario 4: repeated manual deduplication for the same type of entity

This strongly suggests the architect should revisit mapping, identifiers, or rules.

## Red flags that should trigger escalation

Escalate to the Data Architect when:

- matching rules produce too many false positives
- the same domain repeatedly needs large manual deduplication campaigns
- automatic merging already seems suspicious
- additional identifiers may be over-merging unrelated records
- current identifier choices do not reflect business uniqueness

## What deduplication does to stewardship confidence

Done well, deduplication reduces clutter and improves trust. Done poorly, it can create a false single source of truth by combining records that should not be combined.

That is why good stewards are conservative and evidence-driven. The goal is not to reduce record counts. The goal is to reflect reality more accurately.

## Practice exercise

Take one example duplicate scenario and answer:

- Why do these records look like duplicates?
- Which fields give you the most confidence?
- Which fields make you hesitate?
- What value would you choose in each major conflict?
- After the merge, what would you verify first?
- If this scenario kept recurring, what would you escalate?

## You are ready for the next module when

You can explain:

- the difference between identifier-based merging and deduplication projects
- why matching rules identify candidates rather than certainties
- how to review conflict resolution with caution
- when duplicate work is really a platform-design symptom

## What comes next

Now you can isolate, validate, clean, and merge. The next skill is organizing all of that work. You will learn how glossary terms, tags, and governance surfaces help stewards track, prioritize, and communicate quality work at scale.
