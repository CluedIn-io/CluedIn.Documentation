---
layout: cluedin
nav_order: 22
parent: Playbooks
permalink: /playbooks/mds-to-cluedin/03-faq-mapping
title: "MDS → CluedIn (Part 3): FAQ + worked example (MDS use cases mapped to CluedIn)"
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

| Audience | Time to read |
|--|--|
| MDM Lead / Data Engineer / Data Steward Lead | 12–18 min |

This FAQ maps common "how we do it in MDS" use cases to how you solve them in a CluedIn-based operating model. It also includes a worked example (Customer) showing two downstream consumers: one batch, one event-driven.

---

## FAQ — Mapping common MDS use cases

### 1) "We organize everything into Models/Entities/Members. What's the equivalent?"
**MDS**: models/entities/attributes/members + domain-based attributes.   
**CluedIn**: master entities in a domain model and publish consumer-specific contracts via Streams + Export Targets. 

The key difference: you're not optimizing for "hub tables". You're optimizing for mastered truth + distribution.

| MDS term / concept | Rough meaning in MDS | Closest CluedIn term / concept | Notes / "what changes" |
|---|---|---|---|
| Model | Top-level container for master data (per subject area) | Solution / Data model scope (collection of Business Domains) | CluedIn doesn’t map 1:1 to "Model"; in practice you scope by the set of Business Domains you implement. |
| Entity | Master data table (Customer, Product, Supplier) | **Business Domain** | In CluedIn, Business Domains are the entity-type level concepts (Customer, Product, etc.). |
| Member | A record in an entity | Business Domain instance (record) / Entity (instance) | A single mastered record inside a Business Domain. |
| Attribute | Column/field on an entity | Vocabulary Key within a Vocabulary | Vocabulary Keys are expressed through vocabularies (definitions) rather than a single fixed column set. |
| Domain-based attribute | Attribute referencing another entity (lookup) | Relationship between Business Domains (reference) | Typically modeled as an explicit relationship, not just a lookup column. |
| Derived hierarchy | Hierarchy implied from relationships | Relationship traversal (graph-style hierarchy) | Relationships become first-class; hierarchy is often derived from them. |
| Explicit hierarchy | Manually curated parent/child structure | Curated relationships / Classification structure | Implemented as controlled relationships or taxonomy-like structures inside/around the domain. |
| Collection | A named group of members | Segment / Filtered set for publishing | Usually expressed as filters/segments used for publishing rather than a separate "collection object." |
| Business rules | Validate, set defaults, trigger notifications | Golden Record rules + Survivorship Rules + contract gates | Often split into survivorship/matching rules, quality exceptions, and per-consumer publishing requirements. |
| Validation issues | Rule violations | Quality exceptions / failed checks | Tags attached to record define exceptions and are used as gating what gets published. |
| Versioning (versions) | Staged release cycles (open/locked/committed) | Publishing lifecycle + controlled Streams | Instead of "commit a version," you control what gets published via stream configuration and gating. |
| Commit version | Make a version official for consumers | Publish/release a contract output | Equivalent is "stream output becomes authoritative for a consumer." |
| Transaction log / audit | Who changed what and when | Record/property history and audit trail | Same requirement; the tooling and operating model differ. |
| Master Data Manager (web UI) | Stewardship interface | Stewardship in CluedIn + external workflow tools | In CluedIn-style adoption, UI is less central; focus shifts to mastered outputs and contracts. |
| Excel Add-in | Steward editing in Excel | Excel Add-In + External editing/workflow + ingestion back | Although CluedIn offers Excel Add-in, often replaced by governed workflows/forms and controlled ingestion patterns. |
| Subscription views | Denormalized SQL outputs for consumers | Streams + Export Targets (synchronized mode) | If a consumer wants "table-shaped master," synchronized publishing is closest. |
| Change tracking notification | Detect changes for integration | Streams (event log mode) | Event log mode is the closest "emit changes" pattern for event-driven consumers. |
| Staging tables | ETL landing zone before loading MDS | Ingestion + mapping stage | Staging may still exist, but ingestion/mapping is treated as part of the pipeline design. |
| Data steward | Responsible for master data correctness | Data steward / data owner (same role) | Role stays; shifts from manual maintenance to exception handling and governance. |
| Golden record | Canonical mastered record | Mastered record in a Business Domain | Same concept; typically published in multiple vocabulary shapes per consumer. |
| Consumer-specific schema | Different output shapes per consumer | **Vocabulary** (definition) | A Business Domain can have multiple vocabularies to represent the same meaning in different shapes/codes. |
| Publish to downstream | Deliver mastered data to apps/BI | Export Targets / Connectors | Publishing becomes contract-driven and operational (monitoring, retries, idempotency). |


---

### 2) "We rely heavily on business rules. Can we keep the same rules?"
**Blunt answer:** expect translation, not copy/paste.

MDS rules are often used for:
- validation gates
- default/set value logic
- "notify someone" patterns 

In CluedIn-based implementations, you usually split this into:
- mastering logic (survivorship/matching)
- datapart/golden record rules and exception (tag) handling
- contract validation per consumer (publish gates)

---

### 3) "We use hierarchies and collections."
MDS supports derived and explicit hierarchies and collections. 

In CluedIn, you model relationships and classifications so they can be reused, then publish the representation each consumer needs.

Tip: migrate only the hierarchies that actually drive decisions and downstream behavior.

---

### 4) "We publish subscription views to downstream systems. What replaces that?"
In CluedIn, you publish using Streams to Export Targets in a mode that matches the consumer:
- **Synchronized** for "mirror the mastered dataset"
- **Event log** for "emit change events" 

Connector reference (targets) is documented in CluedIn docs. 

---

### 5) "We want event-driven integration."
Use Event log mode plus an event-capable target (e.g., Azure Event Hub connector). 

---

### 6) "How does CluedIn connect to on-prem MDS?"
CluedIn documents an MDS integration using Azure Relay and WCF relay configuration on the MDS server. 

---

### 7) "How do we choose migration path?"
Use the decision matrix in [Part 1](/playbooks/mds-to-cluedin/01-why-and-how). Most teams end up hybrid:
- start with MDS integration for safety and parity
- move to cleaner ingestion from source systems/extracts
- phase out MDS

---

## Worked example: Customer mastered in CluedIn, published to two consumers

### Scenario
You currently use MDS to manage Customer master data:
- entity: Customer
- key attributes: Name, VAT/Tax ID, Address, Country, Customer Status, Parent Customer
- hierarchy: Parent/Child customer structure
- business rules: required VAT, valid country code, "Status must be Active for ERP sync"

You want to move to CluedIn and serve:
1. **Consumer A (batch):** Data Lake / OneLake for analytics (daily full + incremental)
2. **Consumer B (event-driven):** CRM or integration bus via Event Hubs (near-real-time changes)

### Target contract choices (the "do it differently" part)
Instead of one schema for everyone:
- **Analytics contract** includes richer history/context and slower cadence
- **Operational contract** is minimal, stable, idempotent, and event-safe

---

### Step-by-step flow


![flowpart3](../assets/images/playbooks/mds/flowpart3.svg)

Streams and export targets are standard CluedIn mechanisms.

---

## Cutover plan for the worked example (consumer-by-consumer)


![exampleFlow](../assets/images/playbooks/mds/exampleFlow.svg)

---

## What to copy vs what to change (the mindset checkpoint)

**Copy (usually)**

* stable identifiers and key fields
* the downstream contracts that must not break

**Change (almost always)**

* "one schema to rule them all"
* "publish views as the integration strategy"
* "perfect the model before publishing anything"

::contentReference[oaicite:25]{index=25}
