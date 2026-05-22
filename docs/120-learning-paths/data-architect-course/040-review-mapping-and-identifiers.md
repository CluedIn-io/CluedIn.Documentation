---
layout: cluedin
title: Review mapping and identifiers
parent: Data Architect course
grand_parent: Learning paths
permalink: /learning-paths/data-architect-course/review-mapping-and-identifiers
nav_order: 40
tags: ["learning-paths", "data-architect", "training"]
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

This module teaches an architect how to inspect and challenge source onboarding decisions.

## Learning objective

Review a mapped source and judge whether the entity, identifiers, and relationships will produce good downstream behavior.

## What to learn

- how columns map to vocabulary keys;
- what a primary identifier does;
- when additional identifiers help;
- how relationships should be represented.

![Review mapping]({{ "/assets/images/integration/data-sources/review-mapping-1.gif" | relative_url }})

![Primary identifier options]({{ "/assets/images/integration/data-sources/review-mapping-2.png" | relative_url }})

![Additional identifiers]({{ "/assets/images/integration/data-sources/review-mapping-5.png" | relative_url }})

## Exercises

1. Open an existing mapped source and review the **Map columns to vocabulary key** tab.
1. Inspect the selected primary identifier and explain why it is or is not strong enough.
1. Identify one possible additional identifier.
1. Propose one relationship the source should create.

## Architect judgment to reinforce

Weak identifier design creates avoidable stewardship pain later. Strong identifier design gives CluedIn cleaner pre-merged records and better downstream deduplication behavior.

## Related documentation

- [Review mapping](/integration/review-mapping)
- [Add relationships between records](/getting-started/relations)
