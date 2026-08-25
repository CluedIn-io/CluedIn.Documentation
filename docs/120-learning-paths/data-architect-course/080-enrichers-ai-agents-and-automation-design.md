---
layout: cluedin
title: Enrichers, AI agents, and automation design
parent: Data Architect course
grand_parent: Learning paths
nav_order: 80
permalink: /learning-paths/data-architect-course/enrichers-ai-agents-and-automation-design
---

## Learning outcome

Design enrichment or AI-assisted automation with explicit scope, testing, traceability, and operational ownership.

## Scenario

A domain could benefit from external enrichment and AI-assisted remediation, but the team needs to avoid opaque changes that are difficult to explain or unwind.

## Read

- [Enricher reference](/preparation/enricher/enricher-reference)
- [Built-in AI agents](/management/ai-agents/built-in-ai-agents)
- [Tag monitoring](/governance/tag-monitoring)

## Exercise

1. Choose one enrichment or AI-assisted use case for your training domain.
2. Define exactly which records and properties are in scope.
3. State the authoritative sources and the behavior expected when enrichment disagrees with existing data.
4. Define a small test and the evidence required before broader use.
5. Define how a steward can identify that automation changed a record.
6. Record rollback, disablement, or mitigation expectations.

## Deliverable

An automation design containing purpose, scope, authority assumptions, test plan, review owner, traceability, and failure handling.

## Complete when

- Automation scope is explicit.
- Success and failure can be observed on records or governance signals.
- A human owner remains accountable for review and operation.

## Next

Turn operational conditions into measurable governance signals with clear response paths.
