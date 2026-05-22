---
layout: cluedin
title: Identifiers, review mapping, and relation design
parent: Data Architect course
grand_parent: Learning paths
nav_order: 40
permalink: /learning-paths/data-architect-course/identifiers-review-mapping-and-relations
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

Identifiers are where architectural intent meets identity behavior. The architect needs to understand exactly how primary identifiers, additional identifiers, and relation design will affect merges, edges, and downstream trust.

## What you should get from this module

- select primary and additional identifiers responsibly
- use review mapping as an architecture checkpoint rather than an afterthought
- design relations and hierarchies that remain understandable downstream

![review-mapping-3.png]({{ "/assets/images/integration/data-sources/review-mapping-3.png" | relative_url }})

## Guided walkthrough

Use the review-mapping article as the center of this module.

### Primary identifier
Explain the options clearly:
- single key
- auto-generated key
- compound key

Then teach the practical consequences. A convenient field is not necessarily a safe identifier. The architect should actively test uniqueness and think about change stability. If the chosen identifier can legitimately repeat, it is not an identifier.

### Additional identifiers
These can improve merge quality, but they also increase merge reach. The architect should use them when they genuinely represent identity, not merely similarity.

### Relation design
Move from review mapping into the relations guide. Relation setup forces the architect to decide:
- which property points to the target record
- whether edge, strict edge, or fuzzy edge is appropriate
- which edge type expresses the business meaning

This is not just about making a pretty graph. Relation design affects the Relations tab, hierarchy behavior, and exported edge tables downstream.

### Hierarchy
Then briefly connect to Hierarchy Builder. Even if hierarchy projects are constructed later, the architect should already understand that relation quality, business-domain scoping, and edge export choices influence whether hierarchies remain useful or become noise.

## Role lens

Weak identifiers create false unity. Weak relations create false context. Both damage trust. The architect's responsibility is to make identity and connection behavior explicit, testable, and explainable.

## Practice assignment

Choose one domain and answer:

- what is the primary identifier and why is it safe?
- what additional identifiers, if any, should exist?
- what would a false merge look like in this domain?
- what relation types should commonly exist?
- should relation creation happen during mapping, via rules, or through later governance structures?

## Exit criteria

- The learner can compare single-key, auto-generated, and compound identifier choices.
- The learner can explain the role of additional identifiers without overusing them.
- The learner can design a relation with a clear business meaning and operational consequence.

## Suggested source material

- [Review mapping](/integration/review-mapping)
- [Add relations between records](/getting-started/relations)
- [Create hierarchies](/getting-started/hierarchy-builder)
