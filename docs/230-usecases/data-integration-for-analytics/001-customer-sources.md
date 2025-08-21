---
layout: cluedin
title: Data Analytics Use Case
nav_order: 180
has_children: true
permalink: /data-analytics-use-case
---

# MDM for Data Analytics in CluedIn — Step-by-Step Implementation Guide

This guide shows how to use CluedIn as the **master data backbone** for analytics: unify entities, standardize attributes, resolve identities, manage reference data, and publish **analytics-ready conformed dimensions and facts** to your data warehouse/BI stack.

---

## Outcomes

- Trusted **Golden Records** for core dimensions (Customer, Product, Supplier, Location, Employee).  
- Standardized **reference data** (currencies, UoM, tax codes, categories) with cross-system mappings.  
- Analytics-ready **conformed dimensions** (with surrogate keys and optional SCD Type 2 history).  
- Clean **facts** linked to conformed dimensions (optional), with quality flags and lineage.  
- Automated **exports** to the warehouse (e.g., Snowflake/BigQuery/Databricks) and semantic layer.

---

## Prerequisites

- Access to in-scope sources (ERP/CRM/PIM/e-commerce/support/finance + spreadsheets).  
- Target analytics design agreed (star/schema, mandatory attributes, SCD policy, surrogate key strategy).  
- **RACI**: stewards/owners have **Accountable** access to governed objects.  
- A **dedicated VM/server** for heavy ingestion, matching, and toolkit operations (avoid laptops).

---

## Reference Model

**Master Entities (dimensions)**
- `Customer`, `Product`, `Supplier`, `Location`, `Employee` (extend as needed)

**Reference Data (RDM)**
- `Currency`, `UoM`, `Country/Region`, `Category/Taxonomy`, `PaymentTerms`, `Channel`

**Analytics Views (publish)**
- `DimCustomer`, `DimProduct`, `DimSupplier`, `DimLocation`, `DimEmployee`  
- Optional facts: `FactOrder`, `FactInvoice`, `FactSubscription` (linked using surrogate keys)

**History Policy**
- Type 1 (overwrite) for non-analytical changes; Type 2 (row versioning) for attributes you want to trend over time.

---

## Step 1 — Define Analytics Scope & KPIs

**Portal**: *Governance → Policies*  
1. List target dashboards/models (e.g., Revenue, Retention, Supply Chain, Merchandising).  
2. For each, identify **conformed dimensions** required and **mandatory attributes**.  
3. Decide **SCD policy** per dimension (Type 1 vs Type 2 fields).  
4. Capture **business definitions** (data contracts) for key metrics.

---

## Step 2 — Connect & Ingest Sources

**Portal**: *Data Sources → Add Source*  
- Connect all contributing systems (ERP/CRM/PIM/etc.).  
- Capture provenance (`SourceSystem`, `SourceRecordID`, `IngestedAt`).  
- Start with samples; validate shapes; then schedule full loads.

---

## Step 3 — Standardize & Normalize Inputs

**Portal**: *Governance → Rules (Data Part Rules)*  
Create normalization rules so downstream matching and BI are reliable:

- **Text**: trim, case, punctuation, HTML strip, diacritics.  
- **Addresses**: parse components; ISO-2 for `Country`; optional geocoding.  
- **Identifiers**: validate VAT/ABN/DUNS/GTIN/IBAN; normalize MPN/SKU.  
- **Phones/Emails**: E.164 phone; email regex + canonicalization (policy-dependent).  
- **Units & Currency**: convert to canonical (RDM) and store both raw + canonical.

**Tags**: `Standardized`, `InvalidFormat`, `LegacySource`, `NeedsStewardReview`.

---

## Step 4 — Reference Data Management (RDM)

**Portal**: *RDM (or Entity Explorer + Rules)*  
- Load canonical code sets (ISO country, ISO 4217, UoM, tax codes, product categories).  
- Build **mappings** from source codes → canonical values (`CodeMapping`).  
- Version and **publish** approved sets; validate **100% mapping coverage**.

---

## Step 5 — Identity Resolution (Deduplicate & Link)

**Portal**: *Entity Matching*  
Configure per domain:

- **Customer**: TaxID/Email/Phone; Name+Address fuzzy with country guard.  
- **Product**: GTIN or Brand+MPN; FuzzyTitle + Category as candidate only.  
- **Supplier**: TaxID/DUNS; Name+Country; Email domain as supplemental.  
- **Location**: Address normalization + GeoID/GeoPoint.

Run matching; review in **Data Stewardship**; approve merges; **Unmerge** errors.

---

## Step 6 — Golden Record Survivorship

**Portal**: *Governance → Rules (Golden Record Rules)*  
Define attribute precedence and tie-breakers per entity (example):

| Attribute       | Precedence (high → low)               | Tie-breaker                     |
|-----------------|----------------------------------------|----------------------------------|
| Legal/Primary   | ERP > Registry > CRM                   | Most recent verified             |
| Contact fields  | CRM > ERP > Support                    | Consent state                    |
| Category/Taxon  | RDM canonical > source                 | Steward override                 |
| Identifiers     | Verified source only                   | N/A                              |
| Descriptions    | PIM/Tech > ERP > e-com                 | Richest (length + spec coverage) |

Compute `CompletenessScore`; tag `AnalyticsReady` when mandatory fields are present.

---

## Step 7 — Conformed Dimensions (Analytics Views)

**Portal**: *Exports (Modeling)*  
Create analytics-friendly **dimension views** from Golden Records:

- Add **surrogate keys** (`CustomerSK`, `ProductSK`, etc.).  
- Include **business keys** (source IDs) for lineage.  
- Flatten nested attributes; include **quality flags** and `CompletenessScore`.  
- Map reference data to canonical values (never raw codes in dims).

**SCD Type 2 (Optional)**
- Add `ValidFrom`, `ValidTo`, `IsCurrent`.  
- Version on material changes (e.g., Customer Segment, Product Category, Region).

---

## Step 8 — Facts Cleanup & Conformance (Optional)

**Portal**: *Entity Explorer / Rules*  
- Clean transactional facts (orders/invoices) — dates, currency, UoM.  
- **Link** to Golden dimensions using natural keys → then replace with **surrogate keys**.  
- Add **quality columns** (e.g., `IsLinked=1/0`, `DQ_FailCount`).

---

## Step 9 — Data Quality Gates for Analytics

**Portal**: *Data Quality → Profiling / Scorecards*  
- Define pass/fail gates (e.g., `DimCustomer.ValidEmail ≥ 98%`).  
- Track: completeness, validity, uniqueness, timeliness per **dimension and source**.  
- Create **alerts** on regressions and failed gates; route to stewards.

---

## Step 10 — Publish to Warehouse & Semantic Layer

**Portal**: *Exports*  
- Export `Dim*` and `Fact*` views to the warehouse (Snowflake/BigQuery/etc.).  
- Include **CDC** (changed rows only) where possible.  
- Optionally emit **events/APIs** for near-real-time consumption.  
- In the semantic layer/BI: map measures and join keys to `Dim*` SKs.

> Start **read-only** to validate joins and metrics, then operationalize.

---

## Step 11 — Governance, Security & Lineage

**Portal**: *Governance → Permissions / Policies / History*  
- Restrict sensitive fields (PII, cost).  
- Keep **History** for merges/overrides; enable **rollback/undo**.  
- Expose **lineage**: raw → standardized → golden → `Dim*`/`Fact*`.

---

## Step 12 — Scheduling & Operations

- Schedule ingestion, matching, golden updates, quality gates, and exports.  
- Run heavy jobs off-peak on a **dedicated server/VM**.  
- Monitor runtimes and queue depth; investigate anomalies (usually upstream drift).

---

## Step 13 — UAT & Go-Live

- Validate joins: `Fact*` rows match exactly with `Dim*` surrogate keys.  
- Reconcile key metrics vs legacy BI (tolerance agreed).  
- Stakeholder sign-off (Analytics, Finance, Ops).  
- Package with **Product Toolkit**; promote to staging → prod (ensure **Accountable** access).

---

## Go-Live Checklist

- [ ] RDM mappings complete; 100% of source codes mapped.  
- [ ] Golden survivorship rules approved; `AnalyticsReady` tagging accurate.  
- [ ] `Dim*` tables include SKs, lineage columns, SCD policy implemented.  
- [ ] Facts conformed and linked to dimensions; sample reconciliation passed.  
- [ ] DQ gates & alerts configured; dashboards show baselines.  
- [ ] Exports scheduled; CDC tested; warehouse/semantic models wired.  
- [ ] Rollback plan documented (unmerge, undo rules/cleaning projects).

---

## Example Rules (Snippets)

**Country Canonicalization (Data Part)**
- Condition: `Country not in ISO2`  
- Actions: map alias (`UK`→`GB`); on fail tag `UnknownCountry`.

**Customer Identity (Matching)**
- Auto-merge: exact `TaxID` OR exact `Email` OR exact `Phone`.  
- Candidate: fuzzy `Name` ≥ 0.92 AND same `Country` AND address similarity ≥ 0.9 (steward review).

**Golden Survivorship (Customer Segment)**
- Precedence: CRM > ERP;  
- If missing, infer from rules (e.g., lifetime value) and tag `Inferred`.

**SCD2 Versioning Trigger (DimCustomer)**
- Condition: `Segment` or `Region` changes  
- Actions: close current row (`ValidTo=now`, `IsCurrent=false`); open new row (`ValidFrom=now`, `IsCurrent=true`).

**AnalyticsReady Tag**
- If required attrs present AND no critical DQ failures → set `AnalyticsReady=true`.

---

## KPIs & Targets (Examples)

- Duplicate rate in Golden dimensions **< 1–2%**.  
- `DimCustomer.ValidEmail ≥ 98%`, `DimProduct.InvalidGTIN ≤ 0.5%`.  
- Mapping coverage for RDM **= 100%**.  
- % Facts linked to all required dims **≥ 99.5%**.  
- BI reconciliation error **≤ 0.5%** on core metrics.

---

## Common Pitfalls & How to Avoid Them

- **Skipping RDM** → unmapped codes create exploding cardinality in BI; enforce 100% mapping.  
- **Over-fuzzy matching** → require high-confidence evidence for auto-merge; steward the rest.  
- **Mixing channel overrides into Golden** → keep Golden canonical; handle channel transforms in exports/semantic layer.  
- **Not versioning analytical attributes** → adopt SCD2 for attributes used in cohorting/segmentation.  
- **Running heavy jobs on laptops** → use dedicated compute to avoid timeouts and throttling.

---

## Summary

With CluedIn, you can turn disparate operational data into **clean, governed, analytics-ready dimensions and facts**. Standardize inputs, resolve identities, manage reference data, define survivorship, and publish conformed tables with history and lineage so downstream analytics are trusted and repeatable.
