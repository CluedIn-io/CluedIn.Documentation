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

The fastest way to fail a Data Steward course is to drop a learner directly into feature screens without explaining the operating model. A steward needs to know what kind of user they are expected to become, what environment they should work in, and how their daily work connects to ingestion, modeling, rules, and downstream consumers.

## What you should get from this module

- understand the difference between stewardship work and architecture work
- set up a safe learning environment and a repeatable practice dataset
- adopt the right mental model for how to move through the instance

![builtin_agents_sp.png]({{ "/assets/images/management/ai-agents/built-in-ai-agents/builtin_agents_sp.png" | relative_url }})

## Guided walkthrough

Start with the built-in AI agents page because it quietly states the platform's role distinction. The built-in **Data Steward** agent is documented as focusing on fixing data quality issues and looking for duplicates, while the built-in **Data Architect** agent is documented as focusing on rule creation. That split is useful because it tells the learner where they should spend their energy first: investigate, validate, fix, review, and escalate structural issues rather than redesigning the platform from day one.

For training, use a non-production environment and a dataset you are allowed to experiment on. The "Getting started" ingestion guide uses small training files for a reason: a steward learns faster when they can create mistakes, reprocess data, and compare before-and-after behavior without worrying about business impact.

Define a simple operating model for the course:

1. Work from **observable symptoms** first.
2. Trace the symptom back to **source, mapping, or golden-record behavior**.
3. Pick the lightest correct remediation path:
   - fix a few values manually
   - use a clean project for repeatable data issues
   - review validations
   - create or review a deduplication project
   - use tags, glossary terms, or AI-assisted remediation for scalable work
4. When a problem is structural, hand it off with evidence to a Data Architect.

The steward should also keep one small issue log while learning. For each issue, capture the search used, the record examples found, where the issue appears in the UI, and whether the likely fix belongs to stewardship or architecture. That log becomes the learner's first practical runbook.

## Role lens

A strong steward is not just a person who edits values. A strong steward knows when not to edit values directly. The steward should understand the difference between:

- an isolated error in a few records
- a recurring pattern suitable for clean projects or rules
- a source-data issue that should be fixed upstream
- a modeling or identifier issue that requires architectural change

This distinction is what turns the role from reactive cleanup into disciplined operational governance.

## Practice assignment

Set up a sandbox or training instance. Write down:

- which business domain or dataset you will use for practice
- who plays the role of Data Architect for escalation
- what evidence you will capture when something looks wrong
- what change types you are allowed to make directly during training

Then review the built-in AI agents page and explain, in your own words, what work belongs to the steward and what belongs to the architect.

## Exit criteria

- The learner can explain the stewardship operating loop in plain language.
- The learner has a safe dataset and environment for practice.
- The learner knows what evidence to capture before escalating a structural issue.

## Suggested source material

- [Built-in AI agents](/management/ai-agents/built-in-ai-agents)
- [Ingest data](/getting-started/data-ingestion)
