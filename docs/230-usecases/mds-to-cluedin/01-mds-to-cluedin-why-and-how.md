---
layout: cluedin
nav_order: 20
parent: Playbooks
permalink: /playbooks/mds-to-cluedin/01-why-and-how
title: "MDS → CluedIn (Part 1): Why moving makes sense, and how migration is done"
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

| Audience | Time to read |
|--|--|
| Data Architect / MDM Lead / Data Engineer | 12–18 min |

This article explains:
- what MDS is typically used for,
- why moving to a modern MDM approach makes sense, and
- how you migrate into CluedIn using either the **MDS integration** or **database ingestion**.

---

## What MDS is typically used for (real-world pattern)

Most MDS implementations follow a hub-style approach:

1. **Define a controlled model**  
   Models/entities/attributes with members (records), including domain-based attributes. 

2. **Validate and govern**  
   Business rules for validating and setting values (often used as a quality gate). 

3. **Manage hierarchies**  
   Derived and explicit hierarchies and collections for navigation and reporting structures. 

4. **Publish mastered data downstream**  
   Often via **subscription views** (denormalized outputs) consumed by ETL/jobs/apps.

---

## Why moving away from MDS increasingly makes sense

### 1) Platform direction
If you're planning around newer SQL Server versions, be aware Microsoft documents that MDS is **discontinued/removed in SQL Server 2025 (17.x) Preview**, and supported in SQL Server 2022 (16.x) and earlier. 

### 2) Modern MDM is distribution-first
A modern MDM program is not "a master table and a UI." 
It's:
- unifying and mastering across sources
- improving data continuously (matching/survivorship/quality)
- distributing mastered data reliably to many consumers (apps, platforms, analytics)

CluedIn is designed around publishing mastered outputs through **Streams** to **Export Targets** (connectors), including synchronized (mirror) and event log (change events) modes. 

---

## What CluedIn provides in this migration context (at a glance)

CluedIn's key primitives you'll use during migration:

- **Streams**: define what entities to publish, when, and in which mode.   
- **Export Targets**: where the stream is delivered (connectors).   
- **Streaming modes** (most relevant for MDS replacement):
  * **Synchronized**: make a target reflect the mastered truth
  * **Event log**: emit create/update/delete style change events 

Common targets for modernization programs include Azure Event Hubs, OneLake, and ADLS Gen2 (via export targets/connector reference). 

---

## Migration options into CluedIn

### Option A — MDS integration (pull from on-prem MDS via Azure Relay)
CluedIn documents a dedicated **MDS integration** using **Azure Relay** to expose on-prem MDS into CluedIn running in Azure. 
Details on MDS Integration can be seen [here](https://documentation.cluedin.net/microsoft-integration/mds-integration)

In practice, this option is less about "moving MDS into CluedIn" and more about creating a safe bridge so CluedIn can read MDS content while you design the modern model and publishing contracts. The reason Azure Relay shows up here is simple: many MDS deployments sit in tightly controlled networks, and Relay enables controlled connectivity without opening inbound firewall access while still keeping the integration operationally manageable. 

This is the right choice when you want a coexistence period and need to validate outcomes side-by-side. It is also the most forgiving approach when your MDS estate is messy, because it lets you migrate in waves without first rewriting every extraction surface. That said, you still have to make the hard decisions early: how identifiers behave, how you treat MDS business keys, and whether your downstream consumers need synchronized "mirror" publishing or event-style publishing. Those decisions are what determine whether your migration is smooth or turns into a long-running argument about "parity."

Operationally, Relay-based setups add a small but real footprint. It needs configuration on the MDS side, credential/secret handling, and proper monitoring. If you run this for more than a short transition period, treat it like a production integration with clear ownership, alerts, and a runbook.

![MDS1](../../../assets/images/playbooks/mds/MDS1.svg)

---

### Option B — Database ingestion (treat MDS outputs as SQL surfaces)

If your MDS environment already produces stable extraction surfaces—commonly subscription views or curated extract tables—you can ingest those SQL surfaces into CluedIn and then shift governance and publishing into CluedIn.

Choosing this option is essentially saying: "MDS will be treated like another upstream system, and we will ingest the contract it already publishes." The advantage is speed. If your subscription views are stable and well understood by downstream teams, you can stand up ingestion quickly, get mastered outputs into CluedIn, and begin publishing to modern targets using Streams and Export Targets without waiting for deeper refactoring.

The trade-off is that correctness becomes your responsibility. With SQL ingestion, you must be disciplined about schema stability and incremental strategy. If the views change unexpectedly, your ingestion breaks. If hierarchies matter, you need to ensure the extraction surface contains relationship edges or path information rather than only flat attributes. If MDS business rules were acting as an entry-time gate, you will typically re-express that behavior as contract validation and exception handling around publishing, rather than assuming the legacy "hub gate" behavior carries over automatically.

![MDS2](../../../assets/images/playbooks/mds/MDS2.svg)

---

### Option C — Hybrid (common in practice)

Hybrid migration is common because it combines safety with forward momentum. You start by bridging MDS into CluedIn using the MDS integration so you can prove end-to-end publishing and validate parity without disrupting the current operational setup. In parallel, you build a cleaner long-term ingestion path that is less dependent on MDS, typically by ingesting from curated SQL extracts or, better, from the original source systems where master data actually originates. Once the cleaner path is stable and reconciled, you phase out MDS as an ingestion source and keep CluedIn as the mastering and distribution layer.

This approach tends to work best when you have multiple domains and multiple consumers, because it supports a wave-based migration where each wave proves one domain and one contract, while the overall dependency on MDS steadily decreases.

![MDS3](../../../assets/images/playbooks/mds/MDS3.svg)

## Migration decision matrix: MDS integration vs SQL ingestion vs Hybrid

Use this to choose the approach that best fits your constraints.

| Dimension                 | Option A: MDS integration (Azure Relay)              | Option B: SQL ingestion (views/tables)            | Option C: Hybrid                                           |
| ------------------------- | ---------------------------------------------------- | ------------------------------------------------- | ---------------------------------------------------------- |
| Time-to-first-value       | Medium                                               | Fast (if extracts exist)                          | Medium                                                     |
| Risk to operations        | Low (coexist friendly)                               | Medium (depends on extract correctness)           | Low–Medium                                                 |
| Dependency on MDS         | High during transition                               | Lower                                             | Medium → Low                                               |
| Best when                 | On-prem + need safe connectivity + parity validation | You already have clean "contract tables/views"    | You need parity now, but want to modernize ingestion later |
| Effort profile            | More setup for relay + integration                   | More work to define/validate extracts             | Balanced; staged                                           |
| Handles messy MDS estates | Better (fewer immediate refactors)                   | Worse (extract logic becomes your responsibility) | Better                                                     |

**Rule of thumb**

* If your estate is **on-prem and high-risk** → start with **Option A or C**.
* If you already have clean **subscription views/extract tables** and want speed → **Option B**.
* If you want safety *and* long-term cleanliness → **Option C**.

## What you do first (practical sequence)

1. **Inventory what matters in MDS**

   * entities, identifiers, key attributes
   * hierarchies/collections that are actually used
   * rules that truly matter (many are legacy workarounds)
   * consumers + contracts (who expects what shape, when)

2. **Pick your migration approach** using the matrix above.

3. **Publish early**
   Create Streams + Export Targets early to prove downstream contracts, even before mastering is "perfect".


---

## Best practices: how to approach migration to CluedIn

The migrations that succeed are not the ones with the fanciest model. **They're the ones that treat migration as a delivery program with measurable outcomes**. Start by defining what must change for the business to feel value: which consumers must be served first, what latency is acceptable for each consumer, what the minimum usable quality threshold is, and what "correct" means in reconciliation terms. If those answers are fuzzy, you'll end up debating screenshots of UIs and arguing about whether a record "looks right", instead of shipping working contracts.

**Treat every downstream feed as a contract, not as an export**. A contract should have a stable schema, clear field definitions, explicit required-field expectations, and clear update semantics. In CluedIn terms, this usually means agreeing whether a consumer needs a synchronized mirror of the golden record or an event-style feed that emits changes. The point isn't the mode itself; the point is that **publishing must be intentional and repeatable, not "here's a dump, good luck"**. Streams and Export Targets give you the mechanism; your job is to enforce contract discipline around them.

**Decide identity early and stick to it relentlessly**. Most MDS-to-modern migrations fail or drag on because teams postpone the decision about identifiers and then discover too late that every consumer has implicitly encoded expectations about keys. Whether you keep MDS identifiers, keep business keys, introduce a new canonical ID, or maintain a crosswalk, you must make the decision explicit and test it in publishing from the first wave. **Identity isn't a modeling detail; it's the backbone of trust**.

**Don't migrate everything that exists**. MDS environments accumulate rules, hierarchies, and "just in case" structures over years. Some of them are genuine compliance or operational needs; many are historical workarounds or reporting conveniences. A modern migration should translate only what is necessary to deliver working contracts, then iterate. **The fastest route to failure is trying to recreate the entire MDS universe before proving that you can publish a reliable mastered dataset to a real consumer**.

**Publish early, even if mastering is not perfect**. Publishing forces reality: missing required fields, mismatched identifiers, wrong latency assumptions, and hidden consumer dependencies show up immediately when you run a contract end-to-end. This is why wave-based migrations work. **One wave should include ingestion, mastering decisions, a stream, a target, reconciliation against the legacy feed, and a cutover**. Then you repeat with the next contract.

**Design for failure from day one, especially if you go event-driven**. Duplicates will happen, retries will happen, and out-of-order delivery will happen. If you ignore this, you'll ship a "demo integration" that collapses in production. Your publishing should enable idempotent processing downstream, and your integration should have a clear dead-letter or quarantine approach so failures are captured, explainable, and recoverable. CluedIn's Export Targets include health checks that help prevent starting a broken pipeline, but **reliability is still a system-level responsibility** that includes your downstream processors and monitoring.

**Finally, plan the retirement of MDS as a gated milestone**. MDS does not disappear by accident; it lingers because of hidden dependencies such as scheduled jobs, reporting extracts, and undocumented "someone's Excel" processes. Make retirement explicit, run dual-run reconciliation until confidence is earned, cut over consumer by consumer, and only then decommission. If you don't **treat retirement as a real deliverable with an owner and a checklist**, you will keep paying for MDS long after "the migration" was supposedly done.



Next: [Part 2](/playbooks/mds-to-cluedin/02-adoption-and-mindset) covers adoption and the mindset shift you can't avoid.
