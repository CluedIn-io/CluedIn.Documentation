---
layout: cluedin
title: Implement Data Quality Management
nav_order: 180
has_children: false
permalink: /data-quality-use-case
parent: Use Cases Summary
---

# Data Quality in CluedIn — Step‑by‑Step Implementation Guide

A Data Quality (DQ) program in CluedIn gives you **measurable, automated, and auditable** control over your data. This guide walks you through: define scope → profile → standardize → validate → score → steward → monitor → publish.

---

## Outcomes

- Clear **DQ policy** (dimensions, rules, thresholds, SLAs).
- Automated **profiling, validation, and standardization** with rules.
- **Scorecards & dashboards** per entity/attribute and per source.
- **Stewardship workflows** for remediation with full audit & rollback.
- Continuous monitoring and **alerts** on regressions.

---

## Prerequisites

- Source access to data domains in scope (e.g., Customers, Products, Suppliers, Orders).
- Business‑agreed definitions for DQ dimensions and **pass/fail thresholds**.
- **RACI**: Stewards/Owners must have **Accountable** permissions.
- A **dedicated server/VM** for heavy profiling, matching, and toolkit operations.

---

## Step 1 — Define Scope & Quality Policy

**Portal**: *Governance → Policies*  
1. Pick entities/attributes in scope (e.g., `Customer.Email`, `Product.GTIN`, `Address.Country`).  
2. Choose dimensions & thresholds (examples):  
   - **Completeness**: `Email` ≥ 98%, `Phone` ≥ 90%  
   - **Validity**: `GTIN` checksum pass ≥ 99.5%  
   - **Uniqueness**: unique `CustomerID` = 100%  
   - **Consistency**: `Country` uses ISO‑2 = 100%  
   - **Timeliness**: `LastUpdated < 30 days` ≥ 95%  
3. Document SLAs and owners per rule (who fixes what, by when).

---

## Step 2 — Connect & Ingest Sources

**Portal**: *Data Sources → Add Source*  
- Add CRM/ERP/PIM/e‑commerce/finance/file feeds as required.  
- Capture provenance: `SourceSystem`, `SourceRecordID`, `IngestedAt`.  
- Start with **sample loads**, then scale.

---

## Step 3 — Baseline Profiling

**Portal**: *Data Quality → Profiling*  
- Run profiling per entity to see: null counts, distinct counts, pattern distributions, min/max/avg lengths, outliers.  
- Export the baseline as your **before** snapshot.  
- Tag anomalies: `DataDrift`, `OutlierPattern`, `UnexpectedNulls`.

---

## Step 4 — Standardization (Normalize Inputs)

**Portal**: *Governance → Rules (Data Part Rules)*  
Create normalization rules **before** validation so checks are fair:

- **Names & Text**: trim, case normalization, strip HTML.  
- **Addresses**: parse line components; normalize country codes (ISO‑2); optional geocoding.  
- **Phones**: convert to **E.164**; tag `InvalidPhone` on failure.  
- **Emails**: lower‑case, canonicalize dots for known providers (policy‑dependent).  
- **Identifiers**: remove spaces/dashes; compute checks (e.g., VAT/ABN/GTIN).  
- **Units**: convert to canonical (e.g., cm/kg) and tag `UnitNormalized`.

**Recommended tags**: `Standardized`, `NeedsValidation`, `InvalidFormat`, `LegacySource`.

---

## Step 5 — Validation Rules (Attribute‑Level)

**Portal**: *Governance → Rules (Data Part Rules)*  
Express the pass/fail logic per attribute and tag failures:

- **Email Validity**: regex + MX (if available) → tag `InvalidEmail`.  
- **Phone Validity**: E.164 parse → tag `InvalidPhone`.  
- **Country Consistency**: enforce ISO‑2 set; map aliases; tag `UnknownCountry`.  
- **Date Validity**: not in future/past-policy; tag `InvalidDate`.  
- **Identifier Checks**: checksum (VAT/ABN/GTIN/IBAN); tag `InvalidTaxID`, `InvalidGTIN`.  

Keep rules **simple & modular**; prefer many small, focused rules over one complex rule.

---

## Step 6 — Entity‑Level Constraints

**Portal**: *Entity Matching / Rules*  
- **Uniqueness**: assert unique keys (`CustomerID`, `SKU`). On conflict, tag `DuplicateKey` and route to stewardship.  
- **Referential Integrity**: child → parent exists (e.g., `Order.CustomerId` must exist). Tag `OrphanReference`.  
- **Cross‑field Consistency**: e.g., `State` valid for `Country`, `EndDate >= StartDate`.

---

## Step 7 — Compute Scores & Scorecards

**Portal**: *Data Quality → Scorecards* (or implement via Rules)  
Define per‑attribute and per‑entity scores. Example weighting:

- Store `Score_AttributeX`, `Score_Entity`, `Score_Source`.  
- Tag entities by band: `DQ_Gold (≥0.95)`, `DQ_Silver (0.90–0.95)`, `DQ_Bronze (<0.90)`.

---

## Step 8 — Stewardship & Cleaning Projects

**Portal**: *Data Stewardship* & *Data Quality → Cleaning Projects*  
- Auto‑create **work queues** from rule failures (e.g., all `InvalidEmail` for `Customer`).  
- Use Cleaning Projects to bulk fix: standardize values, remap codes, correct formats.  
- Everything is logged in **History**; you can **Undo Project** or **Restore Previous Value** if needed.

---

## Step 9 — Dashboards & Alerts

**Portal**: *Data Quality → Dashboards*  
Track by **entity**, **attribute**, and **source**:

- Completeness %, validity %, uniqueness violations, orphan counts.  
- Score trends (7/30/90‑day).  
- Top failing rules and top offending sources.

Set **alerts** (email/webhook) when:
- A KPI breaches threshold (e.g., Valid Email < 98%).  
- **Regression** from previous week by > X%.  
- New **pattern** emerges (data drift).

---

## Step 10 — Automated Remediation (Where Safe)

**Portal**: *Rules (Data Part & Golden)*  
- Safe auto‑fixes (e.g., country alias mapping, phone formatting) can run continuously.  
- Risky fixes route to **stewards**; tag `NeedsStewardReview`.  
- For downstream **suppression** (e.g., invalid emails), tag `DoNotContact`.

---

## Step 11 — Governance, Access & Lifecycle

**Portal**: *Governance → Permissions / Policies / Retention*  
- Restrict sensitive fields (PII) and steward-only attributes.  
- Apply **Retention Policies** where appropriate (e.g., delete stale logs after N days).  
- Maintain audit: every change is in **History** with who/when/why.

---

## Step 12 — Publish Quality‑Assured Data

**Portal**: *Exports*  
- Publish **conformed** entity views plus quality flags/scores.  
- Provide **suppression lists** (e.g., invalid emails).  
- Offer **wide tables** for BI with `Score_Entity` and failure counts.

Start **read‑only** to validate, then wire quality gates into downstream loaders.

---

## Step 13 — Scheduling & Operations

- Schedule profiling, validation, scoring, and exports (off‑peak for heavy runs).  
- For big jobs, use a **dedicated VM/server** to avoid timeouts and throttling.  
- Monitor job durations and queue depth; investigate spikes.

---

## Step 14 — UAT & Go‑Live

- Validate on a sample set across sources.  
- Confirm rule accuracy (precision/recall) with business owners.  
- Dry‑run alerts and dashboards; tune thresholds.  
- Package with **Product Toolkit** and promote (ensure **Accountable** access).

---

## Go‑Live Checklist

- [ ] DQ policy documented (dimensions, thresholds, SLAs, owners).  
- [ ] Normalization & validation rules active; tests passing.  
- [ ] Scorecards & dashboards show baseline and targets.  
- [ ] Steward queues configured; Cleaning Projects tested; **Undo** verified.  
- [ ] Exports include quality flags/scores; consumers validated.  
- [ ] Schedules & alerts configured; on‑call/triage process in place.

---

## Example Rules (Snippets)

**Email Validity**
- Condition: `Email present`  
- Actions: lower‑case; regex check; tag `InvalidEmail` on fail.

**Phone Normalize**
- Condition: `Phone present`  
- Actions: parse to E.164; tag `InvalidPhone` on parse failure.

**Country ISO‑2 Enforcement**
- Condition: `Country not in ISO2 set`  
- Actions: map alias (e.g., `UK`→`GB`, `U.S.`→`US`); if unknown, tag `UnknownCountry`.

**Date Consistency**
- Condition: `EndDate < StartDate`  
- Actions: tag `InvalidDateRange`; send to stewardship.

**Uniqueness (CustomerID)**
- Condition: duplicate `CustomerID` detected  
- Actions: tag `DuplicateKey`; route to steward queue.

**GTIN Check**
- Condition: `GTIN present`  
- Actions: strip non‑digits; checksum; tag `InvalidGTIN` on fail.

**Timeliness**
- Condition: `Now - LastUpdated > 30 days`  
- Actions: tag `StaleRecord`.

---

## KPIs & Targets (Examples)

- Valid Email ≥ **98%**, Valid Phone ≥ **95%**.  
- Address Standardized ≥ **97%**; Unknown Country < **0.1%**.  
- Duplicate Key violations = **0**.  
- Orphan References = **0**.  
- Entity Score ≥ **0.95** sustained over 30 days.  
- Mean time to remediate stewarded issues **< 5 days**.

---

## Common Pitfalls & How to Avoid Them

- **Skipping standardization before validation** → false failures. Normalize first.  
- **Over‑aggressive regex** → false negatives; keep patterns realistic.  
- **One giant rule** → hard to debug; split into small rules.  
- **No owner for each KPI** → assign accountable roles.  
- **Running profiling on laptops** → use dedicated compute to avoid timeouts.  
- **Fixes re‑applied by other rules** → adjust/disable the problematic rule before reprocessing.

---

## Summary

A successful Data Quality program in CluedIn combines **clear policy**, **modular rules**, **transparent scoring**, and **active stewardship**. Start small, measure relentlessly, automate safe fixes, and keep governance tight so improvements stick.

