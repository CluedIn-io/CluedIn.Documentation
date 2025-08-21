---
layout: cluedin
title: Product 360
nav_order: 180
has_children: false
permalink: /product360
parent: Use Cases Summary
---

# Product 360 in CluedIn — Step-by-Step Implementation Guide

Product 360 delivers a single, trusted view of each product across ERP, PIM, e‑commerce, supplier feeds, and catalog systems. This guide walks you through the end-to-end build in CluedIn: ingest → standardize → match/link → golden record → enrich → govern → publish.

---

## Outcomes

- One **golden product record** per product (and per variant) with complete, standardized attributes.
- Linked entities: **Product ↔ Variant ↔ Category/Taxonomy ↔ Supplier ↔ Price ↔ Inventory ↔ Assets (images/specs)**.
- Quality, lineage, and auditability for compliance and omnichannel consistency.
- Publish/sync to PIM, e‑commerce, ERP, search, and analytics.

---

## Prerequisites

- Source access: ERP (item master), PIM, e‑commerce platform, supplier feeds (CSV/Excel/API), DAM (images/specs), pricing/inventory.
- **RACI**: Ensure **Accountable** access to objects you will import/export.
- Use a **dedicated server/VM** for heavy runs (ingestion, matching, toolkit exports/imports).

---

## Reference Data Model

**Core Entities**
- `Product` (base/SPU)  
- `Variant` (SKU level)  
- `Category` / `Taxonomy` (canonical categories, possibly multiple hierarchies)  
- `Supplier` (links to Supplier 360)  
- `Price` (list/promo, channel, currency, effective dates)  
- `Inventory` (location, on‑hand, safety stock)  
- `Asset` (images, datasheets, manuals, specs PDF)

**Key Attributes (examples)**
- Product: Brand, Manufacturer, MPN, Title, Description, Category, Attributes (JSON or normalized columns), LifecycleStatus.
- Variant: SKU, GTIN/EAN/UPC, Size, Color, Material, Dimensions, Weight, Pack/Case/Unit relationships.
- Asset: URL/Path, Type, Format, Resolution, Primary/Secondary, Hash.

**Relationships**
- Product **has many** Variants, Assets, Prices, Inventory records.
- Product **belongs to** one or more Categories/Taxonomies.
- Product **supplied by** Supplier(s); kit/bundle links to components (BOM).

---

## Step 1 — Connect & Ingest Sources

**Portal**: *Data Sources → Add Source*  
1. Add ERP item master and attributes.  
2. Add PIM/e‑commerce catalogs (including channel overrides).  
3. Add supplier feeds (cost, specs) and DAM (assets).  
4. Add pricing and inventory sources (if modeled in CluedIn).

**Tips**
- Start with **samples** to inspect field coverage and formats.  
- Capture source metadata: `SourceSystem`, `LoadTimestamp`, primary keys.

---

## Step 2 — Define Entities & Mappings

**Portal**: *Entity Explorer → + Create Entity Type*  
1. Create `Product`, `Variant`, `Category`, `Asset`, `Price`, `Inventory`.  
2. Map source fields to target attributes (e.g., `ShortDesc` → `Title`).  
3. Persist **provenance** (SourceSystem, SourceRecordID, SourceField).

**Tip**: Keep variant‑level attributes (SKU, GTIN, Color/Size) separate from product‑level attributes (Brand, Title).

---

## Step 3 — Standardization & Normalization

**Portal**: *Governance → Rules (Data Part Rules)*  
Create rules to normalize inputs before matching:
- **Text**: trim, case, punctuation; remove HTML; normalize diacritics.  
- **Units**: convert dimensions/weight to canonical units (e.g., cm/kg).  
- **Identifiers**: validate/checksum for GTIN/EAN/UPC; normalize MPN (strip spaces).  
- **Taxonomy**: map source categories → canonical taxonomy (use RDM if available).  
- **Assets**: compute file hash; flag duplicates; classify by type.

**Tags (recommended)**: `Standardized`, `InvalidGTIN`, `MissingKeyAttrs`, `LegacySource`.

---

## Step 4 — Product Identity Resolution (Matching)

**Portal**: *Entity Matching → Product / Variant*  
1. **Blocking keys** to reduce comparisons:  
   - `(GTIN)` when present | `(Brand + MPN)` | `(NormalizedTitle + Category)`  
2. **Match rules (examples)**:  
   - **Variant (SKU) auto‑merge**: exact `GTIN` OR exact `SKU` within same Brand.  
   - **Product (SPU) auto‑merge**: exact `Brand + MPN`.  
   - **Candidate (steward)**: `FuzzyTitle ≥ 0.92` AND `Brand` equal AND similar key attributes (e.g., size/pack).  
3. Set thresholds (e.g., Auto‑merge ≥ 0.97; Steward review 0.90–0.97).  
4. Run matching; review in **Data Stewardship** (approve/reject/Unmerge).

**Pitfall**: Don’t merge variants across **different packs** (e.g., single vs 12‑pack). Include `PackSize` / `UoM` in rules.

---

## Step 5 — Stewardship: Review & Merge

**Portal**: *Data Stewardship → Match Review*  
- Validate candidates using GTIN, Brand+MPN, and key attributes.  
- Approve merges, reject false positives, and tag `AmbiguousMatch` when needed.  
- Use **Unmerge** if a mistake is found (audit preserved in History).

---

## Step 6 — Golden Record Survivorship

**Portal**: *Governance → Rules (Golden Record Rules)*  
Define precedence per attribute and tie‑breakers:

| Attribute       | Precedence (high → low)                         | Tie‑breaker                       |
|-----------------|--------------------------------------------------|-----------------------------------|
| Brand, MPN      | ERP > PIM > Supplier                             | Most recent verified              |
| Title           | PIM > ERP > e‑commerce                           | Longest non‑marketing title       |
| Description     | PIM (tech) > ERP > e‑commerce                    | Richest (char count + spec fields)|
| Category        | Canonical Taxonomy (RDM) > Source                | Steward override                  |
| GTIN            | PIM/ERP only                                     | N/A                               |
| Attributes      | PIM > ERP > Supplier                             | Highest completeness              |
| Images/Assets   | DAM > PIM > e‑commerce                           | Resolution & aspect ratio         |
| LifecycleStatus | ERP > PIM                                        | Most restrictive status           |

**Actions**
- Tag `Sellable` when required attributes complete and status active.  
- Compute `CompletenessScore` and tag `LowCompleteness < 0.85`.

---

## Step 7 — Asset Management (Images/Docs)

**Portal**: *Data Sources (DAM) / Rules*  
- Deduplicate by hash; pick **PrimaryImage** per variant (min resolution, white background if policy).  
- Validate asset links; move broken links to stewardship queue.  
- Channel‑specific renditions (size/aspect) can be generated downstream; store metadata.

---

## Step 8 — Pricing & Inventory (Optional Modeling)

**Portal**: *Entity Explorer / Rules*  
- Price: store `List`, `Sale`, `Currency`, `Channel`, `EffectiveFrom/To`.  
- Inventory: store `Location`, `OnHand`, `AvailableToSell`.  
- Compute `InStock` flag for channel exports.

---

## Step 9 — Quality Scoring & Dashboards

**Portal**: *Data Quality → Profiling / Dashboards*  
KPIs: completeness %, invalid identifiers, duplicate rate, image coverage, attribute fill by category, enrichment freshness.

---

## Step 10 — Governance, Security & Lifecycle

**Portal**: *Governance → Permissions / Policies*  
- Restrict sensitive attributes (e.g., cost).  
- Enforce RACI for stewards and domain owners.  
- Apply **Retention** (e.g., archive discontinued after N years; keep specs/lineage).

---

## Step 11 — Enrichment (Optional)

**Portal**: *Data Sources / Rules*  
- Pull manufacturer specs, regulatory attributes (RoHS/REACH), and alternate identifiers.  
- Track `LastEnrichedAt` and provider; re‑check on schedule.

---

## Step 12 — Publish / Integrate

**Portal**: *Exports*  
- **PIM/e‑commerce**: golden product + variant attributes, primary assets, channel flags.  
- **ERP**: authoritative updates where CluedIn is source of truth.  
- **Analytics/DW**: wide denormalized table for BI/search.  
- **APIs/Eventing**: expose read endpoints and change events.

> Start **read‑only** to validate mappings, then switch to authoritative syncs.

---

## Step 13 — Scheduling & Operations

- Schedule ingestion, matching, golden updates, enrichment, and exports (off‑peak for heavy jobs).  
- Monitor runtimes; alert on spikes or queue backlogs.  
- Use **Product Toolkit** for packaging to staging/prod; run on a **dedicated box** with **Accountable** access.

---

## Step 14 — Validate & UAT

- Sample 50–100 high‑volume products across categories.  
- Verify no cross‑product conflation; confirm variant separation and image correctness.  
- Business sign‑off from PIM/e‑commerce/ERP owners.

---

## Go‑Live Checklist

- [ ] All in‑scope sources ingested; mappings validated.  
- [ ] Matching thresholds tuned; false‑positive rate low; unmerge tested.  
- [ ] Golden survivorship approved; completeness thresholds set.  
- [ ] Canonical taxonomy mapping verified.  
- [ ] Asset primary/alt images validated.  
- [ ] Exports tested end‑to‑end in target systems.  
- [ ] Permissions, retention, and audit verified.  
- [ ] Promotion package built with Product Toolkit on **dedicated VM**.

---

## Example Rules (Snippets)

**Normalize GTIN / MPN**
- Condition: `GTIN present`  
- Action: strip non‑digits; validate checksum; tag `InvalidGTIN` on fail.  
- Condition: `MPN present` → uppercase, remove spaces/hyphens → `MPN_Normalized`.

**Auto‑merge Variant**
- If `GTIN` exact OR (`SKU` exact AND `Brand` equal) → Confidence 1.0 (auto).

**Candidate Product Merge**
- If `Brand` equal AND `MPN_Normalized` equal → Confidence 0.98 (auto).  
- Else if `FuzzyTitle ≥ 0.92` AND `Category` equal AND `KeyAttrSim ≥ 0.9` → Confidence 0.95 (steward).

**Golden Survivorship**
- `Title`: PIM > ERP > e‑commerce; prefer longest non‑marketing title.  
- `PrimaryImage`: choose highest resolution; white background preferred; tag `Primary`.

**Sellable Flag**
- If required attrs complete (Title, Brand, Category, GTIN, PrimaryImage) AND `LifecycleStatus=Active` AND `InStock=true` → set `Sellable=true`.

---

## Common Pitfalls & How to Avoid Them

- **Merging different pack sizes** → include Pack/UoM in match rules.  
- **Over‑reliance on fuzzy title** → require GTIN or Brand+MPN for auto‑merge.  
- **Channel overrides pollute golden** → keep **Golden** canonical; apply channel transforms in exports.  
- **Dirty units/attributes** → standardize units before matching; centralize UoM with RDM.  
- **Running heavy jobs on laptops** → use dedicated compute to avoid timeouts.

---

## Success Metrics

- Duplicate rate ↓; auto‑merge precision ≥ 98%.  
- Golden completeness ≥ 90% per category; image coverage ≥ 95%.  
- Time‑to‑publish new SKU ↓ (hours, not days).  
- Downstream catalog exceptions ↓; price/inventory sync accuracy ↑.

---

## Summary

Product 360 in CluedIn unifies product and variant data, establishes clear survivorship, governs taxonomy and assets, and reliably syndicates to every channel. Start with clean identifiers and taxonomy, validate merges with high‑confidence evidence, and keep golden canonical while handling channel‑specific needs in exports.
