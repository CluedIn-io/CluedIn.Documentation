---
layout: cluedin
title: Connect multiple data sources to CluedIn
parent: Knowledge base
permalink: /kb/connect-lots-of-systems
nav_order: 2
---
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

Integrating **100+** sources isn’t a modeling marathon you finish upfront—it’s an incremental journey you steer with evidence from the data itself. CluedIn’s graph-first architecture, schema-on-read ingestion, and late-binding mapping make this practical at scale. This article distills field-proven practices to help you land sources quickly, let the model **evolve**, and still end up with trustworthy, connected master data.

---

## Core principles (TL;DR)

- **Don’t model upfront** — evolve the model **one dataset at a time** with schema-on-read.
- **Many models can represent the same business object** — let each source speak its native shape, then unify.
- **Prefer Edges over Strict Edges** in mapping — enable **eventual connectivity** across unordered loads.
- **Order doesn’t matter** — if your identities & edges are right, the graph will converge as sources arrive.
- **Build natural models from data** — don’t force-fit sources into preconceived structures.

---

## 1) Evolve the model one dataset at a time

### Why
Upfront “big design” collapses under heterogeneous, fast-changing sources. The winning pattern is **progressive modeling**: ingest → observe → map → harden → repeat.

### How
1. **Ingest raw, lossless payloads** as-is (JSON/NDJSON). Preserve lineage (source, system, timestamps).
2. **Inspect emergent fields** and candidate identifiers (emails, account numbers, GUIDs, URLs).
3. **Map minimally** to start: external IDs, core attributes, and a couple of high-value edges.
4. **Add survivorship rules** and standardization **after** you see real conflicts.
5. **Iterate** when the next source arrives—never block integration on a “final” schema.

> Tip: Keep a “New Source Intake” checklist per source: identifiers, key properties, candidate edges, expected volume/frequency, and known quality issues.

---

## 2) Embrace many models for the same business object

### Why
A “Customer” in CRM ≠ “Customer” in Billing ≠ “Customer” in Support. Let each source keep its natural model and **unify through identities and edges**, not by flattening everything into one canonical record upfront.

### How
- **Allow multiple shapes** (facets) to coexist: CRM.Person, Billing.Account, Support.Requester.
- **Unify through identity** (emails, account numbers, tax IDs, domain names) plus **similarity** (names, addresses, phones).
- **Use property namespaces** (e.g., `crm.name`, `billing.name`) and define **survivorship** rules (trusted source by field, recency, completeness).
- **Compute curated views** (golden records) downstream of the raw merged graph—don’t make sources pretend they’re identical at ingestion.

**Example: parallel models for the same customer**
```json
// CRM facet
{ "type": "Person", "externalId": "crm:123", "properties": { "name": "Alex Lee", "email": "alex@acme.com" } }
// Billing facet
{ "type": "Account", "externalId": "bill:9981", "properties": { "billingEmail": "alex@acme.com", "status": "Active" } }
// Support facet
{ "type": "Requester", "externalId": "sup:730", "properties": { "email": "alex@acme.com", "vip": true } }
```
These **different** models refer to the **same** human and will unify via shared identities (`email`), then contribute fields to the mastered view.

---

## 3) Prefer **Edges** over **Strict Edges** in mapping

### Concepts
- **Edges**: relationships that can be created **even if the target doesn’t exist yet**. The link resolves when the target appears or is recognized later (by identity).
- **Strict Edges**: relationships that **require the target to exist at mapping time** (and usually a direct key match).

### Why prefer Edges
- **Order-agnostic ingestion** — you don’t care which source lands first.
- **Resilience to late-arriving keys** — links snap into place when the target becomes known.
- **Fewer brittle dependencies** — no blocking on cross-system referential integrity on day one.

### When to consider Strict Edges
- You truly have **strong referential guarantees** and want validation failures when targets are absent.
- Tiny, tightly controlled domains where strictness prevents incorrect links.

**Example: edge-centric mapping**
```json
{
  "type": "Invoice",
  "externalId": "inv:2025-000045",
  "properties": { "total": 1200.50, "accountNumber": "ACME-001" },
  "edges": [
    { "rel": "billTo", "to": { "hint": { "accountNumber": "ACME-001" } } }
  ]
}
```
Mapping “billTo” as an **Edge** lets CluedIn resolve it later to the correct **Organization/Account** once that node is seen or matched.

---

## 4) Don’t worry about load order (if mapping is right)

### Why
In a graph, identity + edges provide **eventual connectivity**. You can load Support today, Billing tomorrow, CRM next week—links will converge as identities and edges accumulate.

### How
- **Always include** a stable `externalId` and a **last-changed timestamp**.
- **Emit edges with hints** (email, account number, domain) so relationships can **resolve later**.
- **Retry & reprocess** are safe when ingestion is idempotent (same `externalId` = upsert).
- **Backfills**: you can land historical data whenever it’s ready; the graph will merge it.

> Anti-pattern: sequencing complex multi-system pipelines to “guarantee” order. Prefer independent, frequent micro-loads with reconciling edges.

---

## 5) Build **natural models** from the data (don’t force-fit)

### Why
Forcing sources into rigid, predefined structures leads to data loss and brittle mappings. Natural models preserve signals you’ll later use for matching, survivorship, and quality rules.

### How
- Keep **nested structures** and arrays if the source has them (addresses, contacts, SKUs).
- Preserve **original field names** (with source namespaces) alongside standardized ones.
- Promote to standardized fields **after** you confirm semantic equivalence across sources.
- Capture **lineage** (source, file, system, timestamp) on every property to enable trust and audit.

**Example: natural → standardized (progressive)**
```json
// Natural (from e-commerce)
{ "type": "Order", "externalId": "web:O-5571",
  "properties": { "buyerEmail": "alex@acme.com", "items": [ {"sku":"A1","qty":2}, {"sku":"B4","qty":1} ] } }

// Later: add standardized fields (don’t delete natural)
{ "type": "Order", "externalId": "web:O-5571",
  "properties": { "customer.email": "alex@acme.com", "lineItems": [ {"sku":"A1","quantity":2}, {"sku":"B4","quantity":1} ] } }
```

---

## A repeatable workflow for each new source

1. **Ingest** the source as-is (lossless JSON/NDJSON).
2. **Identify** robust identifiers (stable keys, emails, domains) and add them to identity resolution.
3. **Map** a minimal set of properties + a couple of **Edges** (non-strict) to high-value neighbors.
4. **Unify** and inspect collisions; add survivorship & standardization rules **where needed**.
5. **Harden**: data quality checks, formats, code lists; keep the raw signals.
6. **Iterate** when the next source arrives (don’t refactor the world—add the next facet).

---

## Do / Don’t

| Do | Don’t |
|---|---|
| Add sources fast with minimal mapping, then evolve | Wait for a “final” enterprise model before ingesting |
| Use **Edges** (non-strict) to enable eventual linking | Depend on **Strict Edges** that require load order |
| Keep natural source fields + lineage | Flatten away nested structure you’ll need for matching |
| Define survivorship per field (trust, recency, completeness) | Declare one source “always wins” across the board |
| Backfill anytime; idempotent upserts | Build brittle orchestration to enforce source order |

---

## Practical mapping tips

- **Edge hints**: include multiple hints (email, accountNumber, domain) to raise link success.
- **Identity bundles**: combine deterministic (IDs, emails) with probabilistic (name + address).
- **Confidence scoring**: use higher confidence to auto-link; route lower scores to review.
- **Property provenance**: store `sourceSystem` & `lastSeen` per property for audit and rollbacks.
- **Deletes**: model as **tombstones** (soft-delete flags) unless you truly want to erase history.

---

## Anti-patterns to avoid

- **Massive canonical model upfront**: slows onboarding and guarantees rework.
- **Global strict referential integrity** across heterogeneous sources.
- **One-size-fits-all survivorship**: trust varies by attribute and by source.
- **Over-normalization early**: removes signals needed for matching and quality scoring.

---

## Example: making unordered loads converge

1. **Day 1**: Load Support tickets (`Requester.email`).  
2. **Day 3**: Load Billing accounts (`billingEmail`, `accountNumber`).  
3. **Day 7**: Load CRM persons (`email`, `phone`).  

Because tickets have an **edge** `reportedBy → { email }`, and billing has an edge `billTo → { accountNumber | email }`, once CRM lands, identity unification snaps edges together—no reruns required.

---

## Checklist for “ready to scale to 100+ sources”

- [ ] Every payload has **stable `externalId`** and **`timestamp`**.  
- [ ] Mappings use **Edges** (non-strict) wherever feasible.  
- [ ] Identity rules combine deterministic and probabilistic signals.  
- [ ] Survivorship is **per-field** and transparent.  
- [ ] Natural source fields are retained with **lineage**.  
- [ ] Backfill and reprocessing are **idempotent**.  
- [ ] Monitoring covers volume, link-rate, identity collisions, and edge resolution lag.  

---

## FAQ

**Q: Won’t multiple models make reporting harder?**  
A: Raw models stay natural; **curated views** and **golden records** provide stable shapes for analytics. You get flexibility *and* standardization—just at the right stage.

**Q: When would I choose a Strict Edge?**  
A: Small, controlled domains with guaranteed referential integrity where a missing target must fail fast (e.g., reference tax codes).

**Q: How do I control “who wins” when fields disagree?**  
A: Use **survivorship rules**: source trust ranking, last-updated recency, field completeness, or quality scores; never blanket “system X always wins”.

---

### Summary

To integrate hundreds of sources with CluedIn, **optimize for speed-to-land and correctness-over-time**. Let models **emerge** from real data, connect nodes with **Edges** that resolve as identities converge, and postpone strictness until you have evidence. Your graph will become richer, more accurate, and easier to maintain—without the drag of upfront over-modeling.
