---
layout: cluedin
title: Rules, clean projects, and processing logic
parent: Data Architect course
grand_parent: Learning paths
nav_order: 60
permalink: /learning-paths/data-architect-course/rules-clean-projects-and-processing-logic
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

This module is about deciding where logic should live. CluedIn gives multiple mechanisms for changing or normalizing data: mapping logic, validations, clean projects, rules, manual edits, and generated rules. Architects need to place each kind of logic in the right layer.

## What you should get from this module

- understand the role of rules versus clean projects versus source fixes
- design processing logic that reduces repeated manual remediation
- connect clean outcomes to durable platform behavior

![rule-builder-3.png]({{ "/assets/images/getting-started/rule-builder/rule-builder-3.png" | relative_url }})

## Guided walkthrough

Start with the Rule Builder guide. Show that rules are not just automation for its own sake; they are the platform's way of operationalizing repeatable logic around filtering, conditions, and actions.

Then connect rules to clean projects:

- clean projects are excellent for identifying and fixing a recurring issue in the current population
- generated rules can help prevent the same issue from returning
- architect-authored rules are needed when the issue represents a durable platform policy, not just a local cleanup action

Also connect rules to processing. Some rules affect unprocessed data and should be applied during processing. Others affect already processed data and therefore require reprocessing. Architects need to understand the lifecycle implications of each choice.

Use this module to teach a common design test:
- If the issue is isolated and temporary, stewardship can own it.
- If the issue is repeated and pattern-based, a clean project may reveal the correct corrective action.
- If the issue is structural and should hold permanently, it probably belongs in architect-owned rule logic or source correction.

Do not ignore reversibility. Rule edits, inactivation, deletion, and reprocessing behavior all matter because the architect is responsible for how changes are introduced and, if necessary, unwound.

## Role lens

Architects should prefer durable, explainable prevention over endless repeated cleanup. But they should also avoid encoding brittle business logic too early. The trick is knowing when a pattern is real enough to formalize.

## Practice assignment

Take one recurring issue from stewardship and decide where it belongs:

- source-system fix
- validation
- clean project
- generated clean rule
- architect-authored rule

Write a short rationale that covers timing, repeatability, ownership, and reprocessing impact.

## Exit criteria

- The learner can distinguish between operational cleanup and durable platform logic.
- The learner understands when reprocessing is needed after rule changes.
- The learner can explain how clean projects and rules complement one another.

## Suggested source material

- [Create rules](/getting-started/rule-builder)
- [Manage a clean project](/preparation/clean/manage-clean-project)
- [Validations](/integration/additional-operations-on-records/validations)
