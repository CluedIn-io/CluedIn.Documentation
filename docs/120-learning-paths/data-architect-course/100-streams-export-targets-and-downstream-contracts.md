---
layout: cluedin
title: Streams, export targets, and downstream contracts
parent: Data Architect course
grand_parent: Learning paths
nav_order: 100
permalink: /learning-paths/data-architect-course/streams-export-targets-and-downstream-contracts
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

Data architecture is not finished when records look good inside CluedIn. It is finished when downstream consumers receive data with the shape, timeliness, and change behavior they expect. Streams and export targets are where that contract becomes real.

## What you should get from this module

- understand the documented stream configuration flow
- design downstream exports with clear behavioral expectations
- account for hierarchy, glossary, and relation effects in exports

![create-stream-6.png]({{ "/assets/images/getting-started/data-streaming/create-stream-6.png" | relative_url }})

## Guided walkthrough

Walk through the streaming guide in architectural terms.

### Export target
This defines the technical destination and therefore the integration boundary.

### Stream configuration
The architect chooses:
- the filter logic
- the export connector
- the streaming mode
- the properties exported
- whether edges should be exported

Explain the two documented streaming modes clearly:
- **Synchronized** means the destination reflects the current CluedIn state.
- **Event log** means changes accumulate as new events.

Now connect streams to other platform features:
- glossary terms can define the exported population
- hierarchy and relation export settings determine whether downstream systems can reconstruct graph context
- clean projects and rule activity can change what appears downstream automatically

The key architectural question is not merely "can we export this?" It is "what contract are we offering the consuming team?" For example:
- what constitutes identity in the export?
- which properties are stable?
- what changes should consumers expect after merges or cleaning?
- how will relations appear, if at all?

## Role lens

Architects own the contract between CluedIn and its consumers. A stream is not just a pipe. It is a promise about data shape and change behavior.

## Practice assignment

Draft a downstream contract for one stream:

- target audience or consuming system
- selection logic
- synchronized or event-log mode and why
- exported properties
- whether relations or hierarchy edges are included
- how consumers should interpret future corrections, merges, or glossary changes

## Exit criteria

- The learner understands the main stream configuration choices.
- The learner can explain synchronized versus event-log mode.
- The learner can define a downstream contract instead of just an export setup.

## Suggested source material

- [Stream data](/getting-started/data-streaming)
- [Create hierarchies](/getting-started/hierarchy-builder)
- [Work with glossary](/getting-started/glossary)
- [Add relations between records](/getting-started/relations)
