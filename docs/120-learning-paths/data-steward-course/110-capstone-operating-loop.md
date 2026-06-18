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

This final module is not another feature tour. It is the operational synthesis of the whole course. The goal is to prove that you can move through CluedIn like a steward: define the issue, isolate the scope, inspect the evidence, choose the right remediation path, verify the result, and hand off what should be prevented structurally.

## What this module teaches

By the end of this module, you should be able to:

- run a full stewardship cycle from start to finish
- choose the right tool for the issue type
- communicate findings clearly
- avoid common failure modes
- judge your own readiness for live stewardship work

## The full steward operating loop

Use this as your standard model every time.

### Step 1: notice

You notice a symptom:

- a business complaint
- a suspicious record
- a rising defect tag
- an invalid field population
- a duplicate cluster
- an AI recommendation or monitoring change

Do not act yet. First classify the symptom.

### Step 2: isolate

Use search, filters, tags, or glossary terms to define the exact population affected.

Your goal is to answer:

- what records are involved
- how many there are
- which domain they belong to
- whether one source, provider, tag, or condition dominates

### Step 3: inspect

Inspect representative records using:

- Properties / Overview
- History
- Topology
- dataset preview and validations where relevant
- deduplication groups where relevant

Your goal is to answer:

- what is wrong
- where it came from
- whether it is repeated
- whether the issue is source-level, golden-record-level, or structural

### Step 4: choose the right remediation path

Use the issue type to choose the tool.

#### Use validations or mapping review when

- the issue is close to the source
- field meaning or field quality is suspect
- early intervention is best

#### Use clean projects when

- the issue affects many current records
- the fix is repeatable
- bulk or semi-bulk remediation is appropriate

#### Use deduplication when

- multiple records likely represent the same entity
- merge review is required

#### Use tags and glossary when

- the work needs naming, monitoring, or organization
- the defect class should become visible as a queue

#### Use AI when

- the task is repetitive
- scope is controlled
- instructions are clear
- output can be reviewed safely

#### Escalate to the architect when

- the same issue will recur because of design
- mapping or identifiers appear wrong
- survivorship behavior is not acceptable
- stream or rule design should change

### Step 5: apply

Run the selected workflow carefully and intentionally.

### Step 6: verify

Verification is mandatory.

Use:

- the original saved search
- representative records
- tag counts or glossary membership if relevant
- history or topology where structure changed
- downstream awareness where streams may be affected

### Step 7: document and escalate

Document:

- issue type
- scope
- examples
- action taken
- result
- structural recommendation if needed

## The steward tool-selection cheat sheet

| If the issue is mainly about... | Start with... | Likely next step |
|--|--|--|
| bad source values | validations, dataset review | source correction, clean, or mapping escalation |
| wrong current record values | search + record inspection | clean, manual fix, or survivorship escalation |
| likely duplicate entities | search + deduplication | merge review or identifier escalation |
| recurring defect class | tags + Tag Monitoring | clean, AI, or rules/architect handoff |
| named business populations | glossary | clean, stream support, or governance |
| repetitive safe improvements | AI or rules | review, verify, then scale |

## Common failure modes

### Failure mode 1: tool-first thinking

A learner decides “I’m going to use Clean” before understanding the issue. This leads to noisy projects and poor fixes.

### Failure mode 2: scope blindness

The learner edits one record without proving how many records are affected.

### Failure mode 3: weak evidence

The learner says “the data is bad” without examples, saved search logic, or source context.

### Failure mode 4: no verification

The learner assumes a fix worked because the action completed.

### Failure mode 5: no escalation

The learner keeps solving the same structural problem manually and never hands it off.

## Capstone scenario

Use the following scenario as your mental practice.

You discover that people in one business domain have inconsistent job titles. Some are misspelled, some are oddly cased, and some are empty. A tag already exists for a related quality issue, and the records may be part of an active downstream stream.

A strong steward would:

1. open search and isolate the domain
1. add the relevant vocabulary columns
1. save the working search
1. inspect sample records and their history
1. decide whether the empties, formatting issues, and spelling issues should be treated together or separately
1. review whether validations or dataset-level source work is needed
1. create a clean project for the repeatable formatting and spelling issues
1. verify results using the saved search
1. check whether the remaining empties should be tagged or escalated
1. note any downstream stream impact
1. recommend a structural rule or source-side normalization if the same issue is clearly recurring

That is the behavior this course is trying to produce.

## Readiness checklist

You are ready for real steward work when you can honestly say yes to all of the following:

- I understand the difference between source records, data parts, and golden records.
- I can isolate a work queue using search and filters.
- I know how to use saved searches to make my work repeatable.
- I know how to inspect a record using History and not only the Properties tab.
- I know when validations are the right earlier-stage control.
- I know how to use a clean project without treating it as a cure-all.
- I know how to review duplicate groups carefully.
- I know when to use tags and glossary terms to organize work.
- I know how to use AI with guardrails rather than hope.
- I understand that stewardship can affect downstream consumers.
- I know when to escalate to a Data Architect.

## Final guidance

The best stewards are not the ones who click the fastest. They are the ones who develop sharp judgement, respect for scope, and discipline around evidence. CluedIn gives you many powerful surfaces. Your value as a steward comes from knowing which one to use, when to use it, and how to prove that the result is better than what was there before.

## Next step after course completion

After completing this course, the best next step is to operate on a small real backlog under supervision. Pick one business domain, one repeatable defect class, and one safe remediation path. Then practice the full loop until it becomes boringly repeatable. That is usually the point where a learner becomes dependable.
