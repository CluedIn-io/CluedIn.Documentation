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

AI can help a steward move faster, especially when the work is repetitive, pattern-driven, or broad in volume. But AI should not replace stewardship judgement. In CluedIn, the steward’s job is to use AI with scope control, verification discipline, and clear expectations.

![builtin_agents_sp.png]({{ "/assets/images/management/ai-agents/built-in-ai-agents/builtin_agents_sp.png" | relative_url }})

## What this module teaches

By the end of this module, you should be able to:

- explain what the built-in Data Steward AI agent is meant to do
- know when AI is appropriate and when it is not
- use tagged or filtered record sets as safe AI inputs
- test and review AI work before trusting it
- integrate AI into stewardship rather than outsourcing stewardship to it

## The built-in Data Steward AI agent

The built-in Data Steward agent is positioned around two broad task types:

- fixing data quality issues
- looking for duplicates

This is useful because those are exactly the kinds of repetitive, pattern-rich tasks where automation can help a steward scale.

But the steward still owns the decision to use AI, the definition of scope, the instructions, and the final review.

## What AI is good at in stewardship

AI is most helpful when:

- the issue is repeated across many records
- the task has a clear quality goal
- the likely action can be described well
- the steward can validate the output afterwards
- the cost of reviewing results is lower than doing all work manually

Examples:

- standardizing descriptive text
- proposing fixes for obvious data-quality issues
- grouping likely duplicates for review
- suggesting actions on tagged defect queues

## What AI is bad at in stewardship

AI is a poor first choice when:

- the issue depends on undocumented business nuance
- the acceptable answer is ambiguous
- one wrong change would have major downstream consequences
- the steward cannot define success clearly
- the record set is not well scoped

A good rule is: **if you cannot explain what good output looks like, you are not ready to automate it.**

## AI starts with good scope

The best AI jobs start from carefully defined data, not from broad hope.

Good input scopes include:

- records with a specific quality tag
- a glossary term with a clear meaning
- a search-defined population already reviewed by a steward
- one business domain rather than the whole platform

The steward should be able to say, before creating the job:

- who is in scope
- why those records are in scope
- what the agent should improve
- how success will be verified

## Tag Monitoring and AI

One of the strongest AI workflows for stewards begins in Tag Monitoring. If a tag cleanly marks a defect class, the steward can create an AI job from that tagged set.

This is useful because:

- the records are already grouped by a meaningful problem
- the issue can often be described clearly
- post-run verification can compare the before and after tag count

In other words, tags can act as AI input and as AI success signals.

![fix_with_ai_panel.png]({{ "/assets/images/governance/tag-monitoring/fix-records-with-ai/Images/fix_with_ai_panel.png" | relative_url }})

## How to write better AI instructions

Weak instructions are vague:

> Fix the data.

Strong instructions are operational:

> Review records tagged with invalid phone values. Correct only clearly invalid phone numbers when a safe normalized representation can be inferred. Do not invent missing values. Preserve values when confidence is low.

A steward should specify:

- what issue to fix
- what records are in scope
- what counts as an acceptable change
- what the agent must not do
- when uncertainty should result in no change rather than guessed change

## The importance of testing

Never jump straight from idea to broad AI execution.

A strong steward tests first by:

- using a small subset
- reviewing the proposed outcomes closely
- checking whether instructions are precise enough
- identifying false positives and false corrections
- deciding whether the task is ready for larger execution

Testing is not bureaucracy. It is the core of safe stewardship.

## Reviewing AI output

After a test or run, review the results the same way you would review manual work:

- did the visible values improve?
- did the issue count go down?
- did new errors appear?
- were any records changed that should have been left alone?
- does the history of the record still make sense?

If the AI changed data in a way you cannot explain or defend, the job is not yet trustworthy.

## When AI should lead to rule or architecture work

Sometimes AI is the fastest way to clean a large existing population. But if the same pattern keeps recurring, the steward should ask whether the right long-term answer is actually:

- a rule
- a validation
- a mapping change
- a source correction
- a better tag strategy

AI is often an accelerator for today, not the durable answer for tomorrow.

## Steward guardrails for AI use

Use these guardrails every time:

1. define scope narrowly
1. state the goal clearly
1. test before broad run
1. review output critically
1. verify impact with search, tags, or record inspection
1. escalate recurring patterns for durable prevention

## Practice exercise

Write a draft AI use case for one quality issue in your training domain.

Include:

- the input record set
- the quality issue
- the instruction you would give
- what the agent must not do
- how you would test the job
- how you would verify success

If you cannot fill in all six points, the use case is not ready yet.

## You are ready for the next module when

You can explain:

- why AI is useful but insufficient on its own
- why scoping matters more than excitement
- how tags and saved searches support safe AI work
- how to decide whether AI output is trustworthy

## What comes next

The next module closes a gap many stewards do not appreciate enough: downstream impact. When a steward changes values, those changes do not end at the screen. They can flow into streams, exports, and consuming systems.
