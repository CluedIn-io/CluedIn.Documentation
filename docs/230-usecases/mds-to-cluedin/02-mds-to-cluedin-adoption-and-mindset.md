---
layout: cluedin
nav_order: 21
parent: Playbooks
permalink: /playbooks/mds-to-cluedin/02-adoption-and-mindset
title: "MDS → CluedIn (Part 2): Best adoption approach and the mindset change"
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

| Audience | Time to read |
|--|--|
| MDM Lead / Data Steward Lead / Solution Architect | 12–20 min |

This article is about what makes migrations succeed: **adoption**. If you try to recreate MDS behavior inside CluedIn, you'll keep the same bottlenecks—just with new tooling.

---

## The core shift: hub mindset → mastering + distribution mindset

MDS programs often become:
- "the place where master data lives"
- "the UI where changes happen"
- "the view we publish to everybody"

CluedIn adoption works best when you treat the output as a **product**:
- master across sources
- improve continuously
- publish explicit contracts through Streams to Export Targets 

![MindsetShift](../assets/images/playbooks/mds/minsetshift.svg)

---

## Best approach to adopting CluedIn after MDS

### 1) Start with consumers and contracts (not with "porting the model")

Instead of asking "how do we model this like MDS?", ask:

* What is the mastered business concept (Customer/Product/Supplier)?
* Who consumes it?
* What shape does each consumer need?
* What cadence and delivery method do they require?

CluedIn makes publishing a first-class concern via:

* Streams configuration (what/how/when)
* Export Targets
* Modes like synchronized vs event log

### 2) Separate "mastering truth" from "consumer representation"

A frequent MDS anti-pattern is trying to force every consumer into one representation.

In modern MDM:

* the mastered truth stays consistent
* each consumer gets a contract-appropriate representation (codes, formats, fields)

This reduces downstream one-off transformation chaos.

### 3) Move publishing earlier than you feel comfortable with

If you wait until mastering is "done", you'll discover late that:

* consumers need extra fields
* keys don't match expectations
* latency assumptions are wrong

Instead:

* publish a minimal contract early
* validate with one consumer
* iterate

### 4) Treat distribution as an operational system

If you adopt CluedIn seriously, distribution needs:

* idempotency rules (safe repeated updates)
* error handling and retries
* monitoring of export targets/stream health (CluedIn performs health checks before starting streams)

---

## What users need to expect will be different

### "Where do I edit data?"

In MDS, editing often centers on the hub UI.
In a modern approach, editing is a capability—not the center. Expect a split between:

* operational systems where changes originate
* stewardship and governance processes
* mastering rules and quality logic

### "Where do rules live?"

In MDS, rules often act as a gate at entry time.
In modern MDM, rules are often split:

* contract-level rules (what must be present to publish to a consumer)
* quality rules (what must be improved/flagged)
* survivorship rules (who wins per attribute)

### "How do we release changes without versioning locks?"

You can still operate in release cycles, but modern publishing uses:

* contract gating (publish only what meets requirements)
* state/lifecycle control
* the stream configuration as your controlled release mechanism

---

## Adoption anti-patterns (avoid these)

1. **Port everything 1:1**
   Every legacy hierarchy and rule is not sacred. Most are accidents of history.

2. **Design only for one consumer**
   You'll rebuild the view sprawl in a different form.

3. **Ignore operational integration**
   No idempotency, no DLQ pattern, no monitoring → guaranteed pain.

4. **Make stewardship the bottleneck again**
   Stewardship should fix exceptions and guide improvement, not become "the only way data changes."

---

## A pragmatic 90-day adoption shape

### Days 0–30: prove a contract end-to-end

* ingest (MDS integration or SQL ingestion)
* model 1 entity
* publish 1 contract through Streams + Export Target

### Days 31–60: improve mastering + add a second consumer

* add matching/survivorship refinement
* publish a second contract with different requirements

### Days 61–90: cut over one consumer

* dual-run comparison
* cut-over
* repeat

Next: [Part 3](/playbooks/mds-to-cluedin/03-faq-mapping) is an FAQ + a worked example that maps typical MDS use cases into CluedIn patterns.


