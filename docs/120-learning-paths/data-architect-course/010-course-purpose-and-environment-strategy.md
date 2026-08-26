---
layout: cluedin
title: Architect responsibilities and environment strategy
parent: Data Architect course
grand_parent: Learning paths
nav_order: 10
permalink: /learning-paths/data-architect-course/course-purpose-and-environment-strategy
---

## Learning outcome

Define what the Data Architect owns in CluedIn, what belongs to Data Stewardship, and how architecture changes move safely through environments.

## Scenario

Your team is onboarding a new source and a downstream consumer. You are responsible for building the structural data pipeline: ingestion, modeling, matching, initial rules, and publishing. Data Stewards will operate the resulting quality workflows after handoff.

## Read

- [Roles](/administration/roles)
- [Feature access](/administration/user-access/feature-access)

## Exercise

1. Identify the non-production environment you will use throughout this course.
2. Record the source system, representative domain, and downstream consumer for the training scenario.
3. Define the Architect-owned responsibilities: ingestion, mappings, identifiers, edges, matching projects, initial rules, Export Targets, Streams, and Global Data Model validation.
4. Define the Steward-owned responsibilities: cleaning data, reviewing and merging duplicate groups, operating enrichers, and approving routine AI-assisted remediation.
5. Define the evidence required before an architecture change can move from development to test and from test to production.
6. Record who can approve architectural changes and who accepts the operational handoff.

## Deliverable

An architecture responsibility charter containing role boundaries, environments, approval points, evidence requirements, and the handoff to Data Stewards.

## Complete when

- Architect and Steward responsibilities do not overlap ambiguously.
- Production is not used for experimentation.
- Every architecture change has a validation and handoff path.

## Next

Define the semantic model that the ingestion and processing pipeline will produce.
