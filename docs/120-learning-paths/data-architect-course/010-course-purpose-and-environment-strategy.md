---
layout: cluedin
title: Course purpose, environments, and architecture responsibilities
parent: Data Architect course
grand_parent: Learning paths
nav_order: 10
permalink: /learning-paths/data-architect-course/course-purpose-and-environment-strategy
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

The Data Architect course starts with boundaries. CluedIn gives architects many powerful levers, but not every lever should be pulled in the same environment, by the same person, or at the same time. A good architect needs a clean responsibility model before touching mappings or rules.

## What you should get from this module

- understand the architectural scope of the role
- set up disciplined environment usage for learning and implementation
- define how stewardship and architecture collaborate in practice

![builtin_agents_sp.png]({{ "/assets/images/management/ai-agents/built-in-ai-agents/builtin_agents_sp.png" | relative_url }})

## Guided walkthrough

Use the built-in AI agents page as a simple role anchor: the documented **Data Architect** agent focuses on rule creation, while the **Data Steward** agent focuses on fixing data quality issues and looking for duplicates. That split is obviously simplified, but it is still useful. The architect owns how the platform should behave; the steward owns how day-to-day data quality work is operated within that behavior.

Now define environment discipline. The older implementation notes you already had were right on this point, but here it should be formalized into the course:

- **Development** is for experimentation, mapping changes, rule design, and proving a pattern.
- **Test** is for realistic validation with representative data and handoff exercises.
- **Production** is for controlled release and observation, not improvisation.

Set expectations for how an architect should work with learners and stewards:
- treat examples as patterns, not final production templates
- document assumptions behind business domains and identifiers
- validate downstream consequences before enabling streams or automation broadly
- use steward feedback as an input signal for modeling and rule improvements

Also explain the minimum evidence an architect should demand before changing the platform:
- sample records
- reproducible search or glossary scope
- the current and desired behavior
- where in the lifecycle the issue appears
- why the current design is failing operationally

## Role lens

A Data Architect succeeds when platform behavior becomes predictable, scalable, and explainable. That means fewer surprises in merges, better searchability, clearer governance signals, and less repeated manual work for stewards.

## Practice assignment

Document an environment policy for your implementation:

- what changes are allowed in dev, test, and production
- who can approve mapping, rule, and stream changes
- what evidence a steward must supply before an architectural change is made
- what rollback or verification steps are required after promotion

## Exit criteria

- The learner can articulate the architect's scope clearly.
- The learner can describe dev/test/prod responsibilities in CluedIn work.
- The learner has a basic stewardship-to-architecture escalation model.

## Suggested source material

- [Built-in AI agents](/management/ai-agents/built-in-ai-agents)
