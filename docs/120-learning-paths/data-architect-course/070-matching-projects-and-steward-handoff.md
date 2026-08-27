---
layout: cluedin
title: Build matching projects and hand review to stewards
parent: Data Architect course
grand_parent: Learning paths
nav_order: 70
permalink: /learning-paths/data-architect-course/matching-projects-and-steward-handoff
---

## Learning outcome

Configure a matching project that produces explainable duplicate candidates and define a clean handoff to Data Stewards for review and merge decisions.

## Scenario

The domain contains records that may represent the same business object. You are responsible for configuring how CluedIn identifies candidate matches, but you are not responsible for approving or merging those groups.

## Read

- [Deduplicate data](/getting-started/data-deduplication)

## Exercise

1. Choose the domain and population to include in the matching project.
2. Define the properties that provide evidence of identity and the properties that should not be trusted for matching.
3. Configure the matching rules and generate candidate groups.
4. Inspect a sample of candidate groups only to evaluate whether the matching logic is producing understandable results.
5. Tune the matching configuration if the candidate set is too broad, too narrow, or difficult to explain.
6. Define the evidence a Data Steward should see when deciding whether a candidate group should be merged.
7. Hand the project over without approving, rejecting, or merging the groups yourself.

## Deliverable

A matching-project design containing scope, matching evidence, tuning decisions, sample validation, and the handoff criteria for Data Stewards.

## Complete when

- The project produces candidate groups that can be explained from the configured matching evidence.
- Matching quality has been validated without the Architect becoming the operational reviewer.
- The Steward handoff clearly separates matching configuration from merge approval.

## Next

Continue to [Use AI Agents to accelerate initial rule design](/learning-paths/data-architect-course/ai-assisted-rule-design).
