---
layout: cluedin
title: Course purpose, setup, and operating model
parent: Data Steward course
grand_parent: Learning paths
nav_order: 10
permalink: /learning-paths/data-steward-course/course-purpose-and-setup
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

A Data Steward course fails when it throws learners into feature screens before they understand what kind of work a steward actually owns. This first module defines the role, the working habits, the safe learning setup, and the mental model you should use every time you move through CluedIn.

![builtin_agents_sp.png]({{ "/assets/images/management/ai-agents/built-in-ai-agents/builtin_agents_sp.png" | relative_url }})

## What this module teaches

By the end of this module, you should be able to:

- describe the difference between stewardship work and architecture work
- explain what “good stewardship” looks like in CluedIn
- set up a safe way to practice without creating accidental production impact
- adopt a repeatable method for investigating data-quality issues

## What a Data Steward is responsible for

A Data Steward is the operational owner of data trust. In practice, that means the steward is the person who notices that something is wrong, proves that it is wrong, narrows the scope of the issue, chooses the right remediation path, and confirms that the outcome is better after the fix.

A steward usually owns work such as:

- finding bad or incomplete records
- investigating how widespread the issue is
- deciding whether the issue should be fixed manually, through clean projects, through deduplication review, through tags, or through AI assistance
- validating that the fix improved the records
- documenting patterns that need to be escalated to a Data Architect

A steward usually does **not** own deep platform design decisions such as:

- designing the long-term vocabulary model
- changing identifier strategy across multiple sources
- implementing complex rule architecture
- designing export schemas for downstream systems
- building custom integrations or custom enrichers

The steward and the architect work together. The steward brings evidence from real records. The architect turns repeated evidence into durable platform changes.

## The difference between Data Steward and Data Architect

Use this simple rule:

- the **Data Steward** works closest to actual bad records and the day-to-day operation of trust
- the **Data Architect** works closest to durable platform behavior and model design

A good steward asks questions like:

- Which records are wrong?
- How many are affected?
- Is the issue caused by source data, mapping, survivorship, deduplication, or user edits?
- What is the safest way to fix this set of records right now?
- What evidence should I hand to the architect?

A good architect asks questions like:

- Should the mapping be changed?
- Are identifiers wrong?
- Should a rule or survivorship strategy be introduced?
- Should the stream export different properties?
- Is this issue source-specific or model-wide?

## The steward operating loop

You can treat nearly all stewardship work as one loop:

1. **Notice** an issue.
1. **Isolate** the affected records.
1. **Inspect** records, history, and source context.
1. **Classify** the type of issue.
1. **Choose** the right remediation path.
1. **Apply** the fix.
1. **Verify** the result.
1. **Escalate** the pattern if the issue should be prevented structurally.

This course follows exactly that loop.

## Set up a safe learning environment

The best learner experience is a safe environment where mistakes are allowed. The steward should practice in a non-production instance if possible. If that is not available, the next best option is a limited-scope practice dataset and clear rules about what must not be changed.

### Recommended learning setup

Use the following setup whenever you can:

- a test or sandbox instance
- a known training dataset or small business domain
- a short list of allowed actions
- one or two saved searches that isolate the practice records
- agreement on whether streams, rules, AI jobs, and reprocessing are allowed

### Why this matters

In CluedIn, many actions have platform consequences. Clean projects change data. Deduplication changes record structures. Rules can affect future processing. Streams can publish changes downstream. A steward must learn to ask, before acting, “What will this touch?”

## The working surfaces you will use most often

A new steward does not need to memorize every menu in CluedIn. Instead, they should become fluent in a smaller set of surfaces:

- **Search** for finding and isolating records
- **Golden record pages** for understanding what a record currently looks like
- **History** and **Topology** for understanding why it looks that way
- **Ingestion** for checking source datasets, mappings, and validations
- **Clean projects** for systematic remediation
- **Deduplication** for duplicate review and merge decisions
- **Glossary** and **Tag Monitoring** for organizing recurring quality work
- **AI agents** for controlled automation
- **Streams** for understanding downstream consequences

As you go through the course, the same idea repeats: never act on a record set until you know what surface gives you the best evidence.

## The steward decision model

When you find a problem, classify it before you fix it.

### Issue type 1: source-quality issue

Examples:

- empty emails
- malformed phone numbers
- invalid country codes
- inconsistent formats within a dataset

Usually investigate in:

- Ingestion
- Validations
- Mapping review

Usually fix through:

- source correction
- source-side validation
- mapping improvements
- clean project if the records are already in the system and need remediation now

### Issue type 2: golden-record quality issue

Examples:

- wrong winning value
- stale value beating a better value
- properties that look correct in one source but wrong in the final record
- manual changes that conflict with incoming data

Usually investigate in:

- Search
- Golden record page
- History
- Topology

Usually fix through:

- clean project
- manual stewardship
- survivorship or rule escalation to architect

### Issue type 3: duplication issue

Examples:

- the same entity appears as multiple records
- one record contains merged values that look suspicious
- matching and conflicting values need review

Usually investigate in:

- Search
- Deduplication project
- History
- Topology

Usually fix through:

- deduplication project
- identifier and mapping escalation if the same issue repeats

### Issue type 4: governance and prioritization issue

Examples:

- you need to track a class of defects
- business users need a named set of records
- a repeated problem needs a monitored queue

Usually investigate in:

- Glossary
- Tag Monitoring
- Search / saved searches

Usually fix through:

- glossary term
- tag rule
- clean project
- AI-assisted remediation

## How a steward should document findings

A strong steward never hands off vague statements like “data seems wrong.” A good handoff includes:

- the affected business domain
- the saved search or filter logic used
- one or more example records
- the observed bad value
- the expected correct behavior
- whether the issue appears source-specific or broad
- whether the issue is best fixed once or prevented structurally

A good short handoff looks like this:

> In the /Person domain, records from source X contain job titles with repeated whitespace and casing inconsistencies. I isolated 143 records with a saved search. The issue is visible in the final golden records and appears to be source-specific. I fixed the current values in a clean project, but this should probably become a data part rule or upstream normalization pattern.

## Practice exercise

Before moving on, do the following:

1. Identify the instance where you will practice.
1. Write down which business domain or dataset you are allowed to use.
1. List which actions are safe in that environment.
1. Write your own one-sentence definition of the steward role.
1. Write your own escalation rule for when an issue should move to a Data Architect.

## You are ready for the next module when

You can confidently answer these questions:

- What is the steward supposed to optimize for?
- Which actions are safe in my learning environment?
- How do I decide whether this is a steward fix or an architect fix?
- What evidence should I gather before I change anything?

## What comes next

Next you will learn the most important CluedIn concept for a steward: the golden record. If you do not understand what a golden record is, every remediation action will feel random. If you do understand it, the rest of the platform becomes much easier to reason about.
