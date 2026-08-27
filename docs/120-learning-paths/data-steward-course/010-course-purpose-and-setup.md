---
layout: cluedin
title: About this learning path
parent: Data Steward course
grand_parent: Learning paths
nav_order: 10
permalink: /learning-paths/data-steward-course/course-purpose-and-setup
---

This learning path is for Data Stewards who are responsible for the operational quality and trustworthiness of data in CluedIn.

As a Data Steward, you investigate data-quality problems, establish evidence, choose an appropriate remediation, verify the result, and escalate structural issues when they need architectural changes. The goal of this course is to teach that operating loop using realistic tasks rather than repeat the product documentation.

## What you will learn

By working through the modules, you will learn how to:

- understand how source data contributes to golden records
- find and isolate data-quality problems
- distinguish record-level issues from source, mapping, processing, and identity problems
- use validations, clean projects, deduplication, glossary, tags, and AI-assisted remediation where appropriate
- verify that a remediation actually fixed the affected population
- recognize when a problem belongs to a Data Architect and provide enough evidence for a useful handoff

## How the learning path works

The remaining modules follow a consistent structure:

1. **Learning outcome** – what you should be able to do after completing the module.
2. **Scenario** – a realistic stewardship problem to solve.
3. **Read** – links to the canonical CluedIn product documentation for the features used in the module.
4. **Exercise** – the practical work to complete in CluedIn.
5. **Deliverable** – the evidence or decision you should produce.
6. **Complete when** – the conditions that show you are ready to move on.

The **Read** section is intentionally concise. Use the linked product documentation for feature instructions, configuration details, and reference information. Use the learning path to understand when and why to apply those capabilities as a Data Steward.

## Before you begin

Use a non-production environment and choose one representative business domain or dataset that you can use throughout the course.

Keep a simple issue log while you work. For each problem, record:

- the problem or symptom
- the affected population
- evidence and representative records
- the action taken
- the verification result
- any escalation to a Data Architect

Using the same dataset and issue log throughout the course makes it easier to build from investigation through remediation and verification.

## Steward and Architect responsibilities

Data Stewards operate on data-quality problems. They investigate, clean, review duplicate candidates, make merge decisions, govern operational populations, review AI-assisted remediation, and verify outcomes.

Data Architects own structural configuration such as ingestion pipelines, mappings, identifiers, edges, matching-project design, initial rules, Export Targets, and Streams.

When a stewardship investigation shows that the underlying structure needs to change, the Steward should capture the evidence and hand the issue to a Data Architect rather than working around the architecture.

## Next

Continue to [First tour of the instance and the golden record mindset](/learning-paths/data-steward-course/instance-tour-and-golden-record-mindset).
