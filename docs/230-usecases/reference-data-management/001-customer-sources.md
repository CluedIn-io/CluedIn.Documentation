---
layout: cluedin
title: Reference Data Management
nav_order: 180
has_children: true
permalink: /reference-data-management
---

# Reference Data Management (RDM) in CluedIn — Step-by-Step Implementation Guide

Reference data (codes, lists, and hierarchies) underpins every analytics and operational workflow: countries, currencies, units of measure, cost centers, product categories, payment terms, GL accounts, etc. This guide shows how to build a governed, versioned, and syndicated RDM capability in CluedIn.

---

## Outcomes

- **Authoritative code sets** (canonical values) for each domain (e.g., Country, Currency, UoM, ProductCategory, CostCenter).
- **Mappings/crosswalks** from source codes → canonical codes, with full lineage and audit.
- **Versioning & effective dating** for controlled change (draft → approved → published).
- **Hierarchies** (single or alternate rollups) with validation and impact awareness.
- **Syndication** of approved sets to ERP/CRM/data warehouse/BI via exports/APIs.

---

## Prerequisites

- Read access to systems that currently host code lists (ERP, CRM, e-commerce, finance, spreadsheets).
- Agreement on **canonical owners** per domain (who approves changes).
- RACI: Implementers and data stewards need **Accountable** access to governed objects.
- A **dedicated VM/server** for heavy initial loads, matching, and toolkit operations.

---

## Reference Model

**Entities (suggested)**
- `CodeSet` — e.g., `Country`, `Currency`, `UoM`, `ProductCategory`, `CostCenter`.
- `CodeValue` — one row per canonical value (attributes: `Code`, `Label`, `Description`, `EffectiveFrom`, `EffectiveTo`, `Status`).
- `SourceCodeValue` — raw values from each source system (attributes: `SourceSystem`, `SourceCode`, `SourceLabel`).
- `CodeMapping` — crosswalk from `SourceCodeValue` → `CodeValue` (attributes: `MatchConfidence`, `ApprovedBy`, `ApprovedAt`).
- `HierarchyNode` — parent/child structure for hierarchical sets (attributes: `ParentId`, `ChildId`, `AltHierarchyName`, `Level`, `EffectiveFrom/To`).

**Statuses**
- `Draft` → `Proposed` → `Approved` → `Published` → `Deprecated` → `Retired`

---

## Step 1 — Define Scope & Ownership

**Portal**: *Governance → Policies / Permissions*  
1. List domains in scope (start with 2–3 high-impact sets, e.g., `Country`, `Currency`, `ProductCategory`).  
2. Assign **Domain Owner(s)** and **Stewards** per set.  
3. Document approval SLAs and release frequency (e.g., monthly).

---

## Step 2 — Connect & Ingest Source Lists

**Portal**: *Data Sources → Add Source*  
1. Connect ERP/CRM/Finance lists and relevant spreadsheets.  
2. For each list, ingest into `SourceCodeValue` with `SourceSystem` and load timestamp.  
3. Profile data (duplicates, nulls, length/format distribution).

**Tip**: Use *sampling* to inspect variants early (e.g., `US` vs `USA` vs `840`).

---

## Step 3 — Create Code Sets & Canonical Schemas

**Portal**: *Entity Explorer → + Create Entity Type*  
1. Create `CodeSet`, `CodeValue`, `SourceCodeValue`, `CodeMapping`, `HierarchyNode`.  
2. Seed **canonical** `CodeValue` tables for stable domains (e.g., ISO 3166 country, ISO 4217 currency).  
3. Add validation attributes: `Status`, `EffectiveFrom/To`, `Owner`, `Version`.

---

## Step 4 — Standardize & Validate Source Codes

**Portal**: *Governance → Rules (Data Part Rules)*  
Create rules to clean and normalize incoming source codes:
- Trim/uppercase codes; collapse whitespace and punctuation.  
- Normalize diacritics in labels; map known synonyms (`U.S.` → `US`).  
- Validate against canonical patterns (length, charset).  
- Tag issues: `InvalidFormat`, `UnknownCode`, `NeedsStewardReview`.

> Recommended tags: `Standardized`, `Alias`, `DeprecatedSourceCode`.

---

## Step 5 — Build the Mapping (Crosswalk)

**Portal**: *Entity Matching / Data Stewardship*  
1. **Auto-match** exact code or exact label to canonical `CodeValue`.  
2. **Fuzzy match** for labels (e.g., similarity ≥ 0.95) as *candidates* only.  
3. Create/maintain `CodeMapping` for each `(SourceSystem, SourceCode)` → `CodeValue`.  
4. Route low-confidence matches to **Steward Review**; capture `ApprovedBy/At`.

**Pitfall**: Do **not** auto-create new canonical values from fuzzy matches; require steward approval.

---

## Step 6 — Golden Rules for Canonical Survivorship

**Portal**: *Governance → Rules (Golden Record Rules)*  
- For shared domains (e.g., product categories coming from multiple apps), set precedence:  
  `MasterTaxonomy` > `ERP` > `eCommerce` > `CSV`.  
- Tie-breakers: most recent change, highest steward confidence, or owner’s source.  
- Prevent conflicting edits by locking `Approved/Published` values to **owner role** only.

**Action examples**
- On approval → set `Status=Published`, add tag `Authoritative`.  
- On deprecation → set `EffectiveTo`, tag `Deprecated`, update mappings to successor value.

---

## Step 7 — Versioning & Effective Dating

**Portal**: *Entity Explorer / Rules*  
1. Add a `Version` to `CodeSet` (e.g., `ProductCategory v2025.08`).  
2. When changing codes/labels:  
   - Create new `CodeValue` with `EffectiveFrom=YYYY-MM-DD`.  
   - Set predecessor `EffectiveTo`.  
   - Migrate `CodeMapping` entries (track change reason).  
3. Keep **Draft** vs **Published** states; only publish after UAT.

---

## Step 8 — Hierarchy Management

**Portal**: *Entity Explorer → Hierarchies (via `HierarchyNode`)*  
1. Load parent/child edges for the set (e.g., Category tree, Cost Center rollup).  
2. Validate **acyclic** structure; enforce single parent (or allow alternate hierarchies using `AltHierarchyName`).  
3. Add effective dates for time-variant hierarchies.  
4. Create **validation rules**: no orphans, root count = 1 (unless multi-root by design), max depth.

---

## Step 9 — Stewardship Workflow

**Portal**: *Data Stewardship*  
1. Work queue for: new code proposals, unmapped source codes, hierarchy edits, deprecations.  
2. Approve/Reject with justification; changes recorded in **History**.  
3. Use tags to drive workflow: `NeedsApproval`, `NeedsMapping`, `BreakingChange`.

---

## Step 10 — Quality Checks & Policies

**Portal**: *Data Quality → Profiling / Rules*  
- **Uniqueness**: canonical `Code` unique per `CodeSet`.  
- **Completeness**: required attributes populated for `Published`.  
- **Integrity**: every `SourceCodeValue` maps to a `CodeValue`.  
- **No deprecated usage** in exports (flag if `EffectiveTo` < today).  
- **Policy**: new values must have owner + description; hierarchy edits require two-person approval.

---

## Step 11 — Publish & Integrate

**Portal**: *Exports*  
- Publish **lookup tables** and **mappings** to ERP/CRM/DW/ML features.  
- Provide both **wide** (`CodeValue`) and **narrow** (`SourceCode` → `CanonicalCode`) feeds.  
- Offer **read API** for applications that need live lookups.  
- Start **read-only**, validate with consumers, then make CluedIn **authoritative**.

---

## Step 12 — Scheduling & Release Management

- Schedule source refresh, rematching, validation, and export jobs.  
- Run large batch reconciliations off-peak on a **dedicated server/VM**.  
- Use **Product Toolkit** to package `CodeSet`, `CodeValue`, rules, and exports; ensure **Accountable** permissions before promoting to staging → prod.

---

## Step 13 — UAT & Go-Live Checklist

- [ ] All in-scope source codes ingested and standardized.  
- [ ] 100% of `SourceCodeValue` entries mapped or triaged.  
- [ ] Golden survivorship/precedence approved by domain owners.  
- [ ] Hierarchies validated (no cycles/orphans; effective dates correct).  
- [ ] Version labeled and **Published**; change log prepared.  
- [ ] Downstream consumers validated against new lookups and mappings.  
- [ ] Runbooks for **deprecations**, **renames**, and **rollback** documented.

---

## Example Rules (Snippets)

**Normalize Code (Data Part Rule)**
- Condition: `SourceCode` present  
- Action: uppercase; strip punctuation; set `Code_Normalized`; tag `Standardized`.

**Auto-map Exact Codes**
- Condition: `Code_Normalized` equals canonical `Code` in same `CodeSet`  
- Action: create `CodeMapping` with `MatchConfidence=1.0`; tag `AutoMapped`.

**Candidate Fuzzy Label Match**
- Condition: label similarity ≥ 0.95  
- Action: create candidate `CodeMapping` with `MatchConfidence=0.95`; tag `NeedsStewardReview`.

**Deprecate & Redirect**
- Condition: `CodeValue.Status = Deprecated`  
- Action: enforce `SuccessorCode`; update downstream export to map deprecated → successor.

---

## Monitoring & KPIs

- Mapping coverage: `% SourceCodeValue mapped` (target ≥ 99.5%).  
- Data quality: duplicates = 0; invalid/unknown codes trend ↓.  
- Time to approve new code: median hours/days vs SLA.  
- Consumer adoption: % downstream systems using CluedIn lookups.  
- Incident rate from reference data changes (should trend to zero).

---

## Common Pitfalls & How to Avoid Them

- **Letting sources drift** (new codes appear unmapped) → schedule nightly ingest + alert on `UnknownCode`.  
- **Over-fuzzy mapping** → require steward approval for < 1.0 confidence.  
- **Breaking changes mid-cycle** → use `Draft` versions; publish on release cadence; communicate impact.  
- **Hierarchy loops** → enforce acyclic validation + tests before publish.  
- **Running heavy reconciliations on laptops** → use dedicated compute to avoid timeouts.

---

## Rollback & Audit

- Every change (new code, rename, mapping edit, hierarchy move) appears in **History** with who/when/why.  
- Use **Undo/Restore Previous Value** for attribute fixes; **Unmerge** not typically needed for RDM but available for accidental consolidations.  
- For erroneous releases: republish the prior **Version** (set its `EffectiveFrom` to now, mark failed version `Deprecated`).

---

## Summary

With CluedIn you can centralize reference data, create reliable crosswalks, govern changes with versioning and approvals, and distribute authoritative values to every consumer. Start with high-impact sets, lock down ownership, automate the mundane, and publish on a predictable cadence to eliminate code chaos.
