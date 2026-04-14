---
layout: cluedin
title: Run the steward operating loop
parent: Data Steward course
grand_parent: Learning paths
permalink: /learning-paths/data-steward-course/run-the-steward-operating-loop
nav_order: 70
tags: ["learning-paths", "data-steward", "training"]
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

This module turns the earlier lessons into a repeatable stewardship habit.

## Learning objective

Run a closed-loop operational process inside the product.

## Steward operating loop

1. Start from a saved search or known business domain.
1. Narrow the result set with filters.
1. Review source-level validation failures.
1. Review duplicate candidates where relevant.
1. Verify the visible outcome in the instance.
1. Document repeated patterns for architect follow-up.

## Using the built-in AI agent

The Data Steward AI agent can be used to accelerate investigation, but not to replace judgment. Use it to:

- surface likely duplicates;
- point out obvious quality issues;
- suggest what to inspect next.

The human steward still owns the final decision and verification path.

![Built-in AI agents]({{ "/assets/images/management/ai-agents/built-in-ai-agents/builtin_agents_sp.png" | relative_url }})

## Final completion check

A learner is ready to complete the course when they can independently do the following in sequence:

- prove where the issue appears;
- show which records are affected;
- explain what was fixed;
- confirm the visible outcome in CluedIn;
- identify whether the pattern should now be handed off to a Data Architect.

## Related documentation

- [Search](/key-terms-and-features/search)
- [Filters](/key-terms-and-features/filters)
- [Validations](/integration/additional-operations-on-records/validations)
- [Deduplicate data](/getting-started/data-deduplication)
