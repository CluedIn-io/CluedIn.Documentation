---
layout: cluedin
title: Use glossary, tags, and governance views to organize work
parent: Data Steward course
grand_parent: Learning paths
nav_order: 80
permalink: /learning-paths/data-steward-course/glossary-tags-and-governance
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

At some point, stewardship stops being a series of isolated fixes and becomes an operating system for quality work. Glossary terms, tags, and governance views help you name record populations, monitor defects, communicate intent, and turn recurring issues into visible work queues.

![top_tags_chart_sp.png]({{ "/assets/images/governance/tag-monitoring/monitor-tag-usage/Image/top_tags_chart_sp.png" | relative_url }})

## What this module teaches

By the end of this module, you should be able to:

- explain the difference between glossary terms and tags
- know when to use each one
- understand how Tag Monitoring supports stewardship prioritization
- create better quality queues and named record sets
- connect governance views back to clean and AI workflows

## Glossary in steward language

A glossary term is a named set of records defined by conditions. Terms live inside categories.

Use glossary when you want:

- a human-readable business grouping
- a curated set of records with meaning beyond one-off remediation
- a reusable filter that business users and stewards can refer to
- a clean basis for downstream usage or stream targeting

Examples:

- “North America customers”
- “High-confidence suppliers”
- “Employees missing department assignment”

A glossary term is often a business-facing or collaboration-friendly way to describe a filtered population.

![create-term-1.png]({{ "/assets/images/getting-started/glossary/create-term-1.png" | relative_url }})

## Tag in steward language

A tag is a lightweight label applied to records, usually to mark a condition, state, or issue.

Use tags when you want:

- a fast operational signal
- a defect marker
- a way to count and monitor a quality issue
- a bridge into Tag Monitoring, Clean, or AI jobs

Examples:

- invalid-validation-phone
- missing-country
- suspect-duplicate
- review-required

Tags are especially strong for quality operations because they make defect classes visible.

## Glossary versus tag: the practical difference

Use this rule of thumb:

- use a **glossary term** when the set is meaningful as a named group of records
- use a **tag** when the label describes a state, issue, or operational flag

A single record set may use both:

- glossary term: “Prospective enterprise customers”
- tag: “missing-website”

The glossary tells you *what set this is*.  
The tag tells you *what issue this record has*.

## Tag Monitoring as a steward command center

Tag Monitoring turns individual record flags into an operational governance surface. It lets you see:

- which tags are used
- how many records carry a tag
- how tag usage changes over time
- which records are currently affected

For a steward, this is powerful because it changes defect management from anecdotal to measurable.

![tag_card.png]({{ "/assets/images/governance/tag-monitoring/monitor-tag-usage/Image/tag_card.png" | relative_url }})

## Enabling and using Tag Monitoring

If Tag Monitoring is not enabled, the governance view may not appear. Once enabled, you can inspect tag usage by business domain and time period.

A steward should use Tag Monitoring to ask:

- Which quality issues are most common right now?
- Is a defect class shrinking after remediation?
- Which business domain is struggling most?
- Which tag deserves a clean project or AI job next?

## From tag to action

One of the best things about Tag Monitoring is that it is not passive. From the monitored defect set, you can move directly into action:

- create a clean project
- create or review an AI job
- add more tags if the current taxonomy is weak
- inspect the underlying records

This makes Tag Monitoring a prioritization and execution bridge.

## Building a good steward tagging strategy

A weak tagging strategy creates vague tags like:

- issue
- invalid
- fixme

A stronger tagging strategy creates tags that are:

- specific
- operationally meaningful
- reusable
- easy to count over time

Better examples:

- invalid-validation-phone
- missing-required-job-title
- source-x-invalid-country
- duplicate-review-needed

A good tag name often contains the problem class and, if useful, the origin or scope.

## How glossary supports stewardship beyond defects

Glossary is not only for governance optics. It helps stewards:

- preserve useful record populations
- communicate with business stakeholders
- define a clean input set for a project
- simplify stream targeting later
- create repeatable operating categories

For example, a glossary term can describe a business-owned set of records, while tags describe current issues inside that set.

## When to use glossary, saved search, or tag

These three tools overlap enough to confuse new learners.

### Use a saved search when

- you personally need a reusable working view
- the main requirement is operational speed
- collaboration needs are limited

### Use a glossary term when

- the record set should have a business-meaningful name
- other users need to understand and reuse the set
- the set may become part of stream or governance workflows

### Use a tag when

- the label marks a problem or status
- you want monitoring and counts
- you want defect classes that can drive action

## How governance views change steward behavior

Without governance views, teams tend to work reactively and remember only the issue they saw this morning. With glossary and tags, work becomes more systematic:

- named groups are easier to discuss
- defect classes become measurable
- improvements can be verified over time
- handoffs become clearer

That is how governance supports better stewardship, even for operational users.

## Practice exercise

Design one glossary term and one tag for your learning domain.

For the glossary term, write:

- the category name
- the term name
- the conditions that define it
- why a business user would understand and value it

For the tag, write:

- the tag name
- the defect or state it marks
- whether it should be domain-specific
- what action the tag should usually trigger

## You are ready for the next module when

You can explain:

- the difference between glossary and tag
- why Tag Monitoring is useful to a steward
- how named record sets and defect labels support prioritization
- how governance views connect back to remediation workflows

## What comes next

Next you will learn how AI fits into stewardship. AI can accelerate quality work, but only when the steward controls scope, instructions, validation, and risk.
