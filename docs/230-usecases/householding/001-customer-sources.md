---
layout: cluedin
title: Householding Use Case
nav_order: 180
has_children: false
permalink: /householding
parent: Use Cases Summary
---

# Householding MDM in CluedIn — Step-by-Step Implementation Guide

**Householding MDM** creates a reliable, privacy-aware view of the people who live together and their shared attributes (address, contact channels, preferences, relationships). This guide walks you through the end-to-end build in CluedIn: ingest → standardize → match/link (person & address) → household formation → golden record → governance → publish.

---

## Outcomes

- One **golden Household** per dwelling (with effective dating for moves).
- Linked entities: **Household ↔ Person(s) ↔ Address(es) ↔ Accounts/Orders/Policies ↔ Preferences/Consents**.
- Accurate **roles** (e.g., Head, Partner, Dependent, Roommate) and membership periods.
- Better targeting, deduplication, and compliance (opt-outs and legal notices aggregated).

---

## Prerequisites

- Source access: CRM, billing/subscriptions, e-commerce/loyalty, service/support, marketing lists, (optional) property/geo sources.
- **RACI**: Ensure stewards have **Accountable** access to governed objects.
- For heavy matching runs, use a **dedicated server/VM** (not a laptop) to avoid timeouts.
- Agreed business rules for:
  - How to define a “household” (shared address + time overlap ± surname/relationship evidence).
  - How to aggregate preferences/consents (“most restrictive wins” recommended).

---

## Reference Data Model

**Core entities**
- `Person` (individual)
- `Address` (standardized, geocoded; includes unit/apartment)
- `Household` (grouping)
- `HouseholdMembership` (Person ↔ Household with role & date range)
- `Preference` / `Consent` (per Person; optionally aggregated to Household)
- `Account` / `Order` / `Policy` (linked for analytics)

**Key attributes (examples)**
- Address: Line1, Line2/Unit, City, Region, Postcode, Country, GeoPoint, GeoID/PropertyID, DPV/AV status.
- Household: HouseholdId (stable key), PrimaryAddressId, Type (Family, Shared, Multi-Family, Dorm), Size, Start/End dates.
- Membership: Role, StartDate, EndDate, Evidence (AddressOverlap, Relationship, FinancialLink).

---

## Step 1 — Connect & Ingest Sources

**Portal**: *Data Sources → Add Source*  
1. CRM persons/contacts, service/install addresses, billing/ship addresses.  
2. Marketing lists (email/phone), loyalty/e-com profiles.  
3. Optional: property datasets (parcel/building IDs), geocoding service outputs.  
4. Load ad-hoc spreadsheets for legacy segments.

> Capture provenance on ingest: `SourceSystem`, `SourceRecordID`, `LoadTimestamp`.

---

## Step 2 — Define Entities & Mappings

**Portal**: *Entity Explorer → + Create Entity Type*  
- Create `Person`, `Address`, `Household`, `HouseholdMembership`, `Preference/Consent`.  
- Map source fields to canonical attributes (normalize naming; keep `Unit/Apt` explicit).  
- Persist `Address.Raw` alongside parsed components for lineage.

---

## Step 3 — Address Standardization & Geocoding

**Portal**: *Governance → Rules (Data Part Rules)*  
Create rules to normalize addresses **before** matching:
- Parse Line1/Line2, extract **Unit/Apt**; normalize street types and directional suffixes.  
- Normalize **Postcode/Region** (ISO where applicable).  
- Geocode to **GeoPoint**; attach **GeoID/PropertyID** when available.  
- Validate deliverability (e.g., DPV/AV flags) and tag issues.

**Recommended tags**: `StandardizedAddress`, `InvalidAddress`, `MissingUnit`, `POBox`.

---

## Step 4 — Person Identity Resolution

**Portal**: *Entity Matching → Person*  
1. **Blocking keys**: (Email), (Phone), (LastName + DOB), (CustomerId).  
2. **High-confidence**: exact email OR exact phone OR government/customer ID.  
3. **Medium**: fuzzy name + same birthdate OR same email domain + strong address similarity.  
4. Review in **Data Stewardship**; approve merges; **Unmerge** when needed.

> Avoid over-merging roommates with same last name but different emails/phones.

---

## Step 5 — Address Deduplication

**Portal**: *Entity Matching → Address*  
1. **Blocking**: (Postcode + HouseNumber), (GeoID), (GeoPoint rounded).  
2. **High-confidence**: exact normalized address (including **Unit/Apt**).  
3. **Candidate**: same building (GeoID) + similar line components; send to stewardship.  
4. Keep **P.O. Boxes** separate; never merge PO Box with street delivery points.

---

## Step 6 — Household Formation Rules

**Portal**: *Governance → Rules (Golden Record & Data Part Rules)*  
Create **Household keys** and membership logic:

- **Household Key (example)**  
  `HHKey = hash(GeoID or (Address.Line1+Line2+Postcode+Country) + CohabitationWindow)`  
- **Formation conditions** (any of):  
  - ≥2 `Person` entities share the **same normalized Address (including Unit)** with overlapping **residency periods**.  
  - A `Person` moves in (address change) to an existing household and shares a **relationship** (spouse/child) or **financial link** (shared account).  
- **Membership periods**: set `StartDate` when first evidence appears; set `EndDate` when address changes or account closes.

**Tags**: `CandidateHousehold`, `ConfirmedHousehold`, `SharedResidence`, `Dormitory`, `MultiUnit`.

---

## Step 7 — Roles & Evidence

**Portal**: *Data Stewardship → Household Review*  
- Assign roles per member: `Head`, `Partner`, `Dependent`, `Roommate`.  
- Evidence priority: Shared last name & age gap (family), shared contract/account (financial), tenancy record, emergency contact links.  
- Store `EvidenceType` on `HouseholdMembership`.

---

## Step 8 — Household Golden Survivorship

**Portal**: *Governance → Rules (Golden Record Rules)*  
Define how household-level attributes are chosen:

| Attribute             | Precedence (high → low)                                | Tie-breaker                         |
|----------------------|---------------------------------------------------------|-------------------------------------|
| PrimaryAddress       | Verified service/billing > CRM mailing > marketing      | Most recent verified                |
| PrimaryPhone/Email   | Landline at address > Head’s preferred > shared contact | Consent state = granted             |
| Language/Locale      | Majority of members > Head’s preference                 | Most recent update                  |
| HouseholdType        | Evidence-based (Family > Shared > Dorm > Multi-Family)  | Steward override                    |
| Preferences/Consents | **Most restrictive wins** (opt-out propagates)          | N/A                                 |

- Compute `HouseholdSize`, `HasChildren` (derived), and `CompletenessScore`.  
- Tag `DoNotContact` at **household** if any member has `DoNotContact=true` (policy).

---

## Step 9 — Consent & Preference Aggregation

**Portal**: *Rules (Data Part & Golden)*  
- Household **suppression**: if any member opt-outs, set household `DoNotContact=true`.  
- Channel logic: e.g., suppress SMS if **no** members consent to SMS; allow email if **any** consenting adult (confirm legal stance).  
- Keep **person-level** consent for precision; use household-level only for targeting/ops.

---

## Step 10 — Quality Scoring & Dashboards

**Portal**: *Data Quality → Profiling / Dashboards*  
Track KPIs:
- Address deliverability %, unit capture rate, geocoding success.  
- Duplicate person rate, duplicate address rate.  
- Household coverage (people with a HouseholdId).  
- False-merge & unmerge counts; membership with missing dates.

---

## Step 11 — Governance, Security & Lifecycle

**Portal**: *Governance → Permissions / Retention / Policies*  
- Restrict access to **sensitive** person attributes (DOB, IDs).  
- Retention: keep ended memberships and prior addresses for N years (audit & analytics).  
- Enable rollback: merges, household formation, and role changes captured in **History** (undo/restore supported).

---

## Step 12 — Publish / Integrate

**Portal**: *Exports*  
- CRM/Marketing: export Household table (id, primary address/contact, size, type) + HouseholdMembership for segmentation.  
- Service/Billing: publish golden addresses to reduce delivery failures.  
- Analytics/DW: wide conformed model (Person ↔ Household ↔ Address).  
- APIs/Eventing: emit **household-changed** events for downstream sync.

> Start **read-only**, validate mapping & suppression behavior; then make CluedIn authoritative where appropriate.

---

## Step 13 — Scheduling & Operations

- Schedule person/address matching, household refresh, consent aggregation, and exports.  
- Run heavy matching and rebuilds **off-peak** on a dedicated VM/server to avoid timeouts.  
- Alert on spikes: sudden household churn can indicate address parsing issues upstream.

---

## Step 14 — Validate & UAT

- Sample 100–200 households across multi-unit buildings, single-family homes, dorms/aged-care.  
- Verify roles, membership dates, and suppression logic.  
- Business sign-off from CRM/Marketing/Service & Privacy teams.

---

## Go-Live Checklist

- [ ] Address standardization + geocoding > 95% success; unit capture validated.  
- [ ] Person & Address matching thresholds tuned; unmerge tested.  
- [ ] Household formation rules approved; role assignment guidelines documented.  
- [ ] Consent aggregation (“most restrictive wins”) validated end-to-end.  
- [ ] Exports/APIs tested with downstream systems.  
- [ ] Permissions & retention configured; audit/rollback verified.  
- [ ] Product Toolkit package built & promoted from staging to prod (run on **dedicated box** with **Accountable** access).

---

## Example Rules (Snippets)

**Address Normalize (Data Part Rule)**
- Condition: `Address.Raw present`  
- Actions: parse components; standardize abbreviations; set `Address.Normalized`; geocode; tag `StandardizedAddress` or `InvalidAddress`.

**Create Household Key**
- Condition: `Address.Valid=true`  
- Action: `HouseholdKey = hash(Address.Normalized+Postcode+Country)`; (optionally add `Unit` and `GeoID`).

**Membership Inference**
- Condition: two Persons share `HouseholdKey` with residence overlap ≥ 60 days  
- Action: create `HouseholdMembership` for both with role defaults (`Head` for account holder; else `Unknown`); tag `CandidateHousehold`.

**Consent Aggregation**
- Condition: any member `DoNotContact=true`  
- Action: set `Household.DoNotContact=true`; store `AggregatedFrom=PersonIds`.

**Golden Survivorship**
- PrimaryAddress: verified service address > billing address > CRM; tie-break newest verified.  
- PrimaryPhone: shared landline > Head’s preferred > most recent; require consent.

---

## Common Pitfalls & How to Avoid Them

- **Merging different apartments**: always include **Unit/Apt** or **GeoID** in address matching.  
- **Dorms & aged-care**: many unrelated people at one address — require extra evidence (relationship/financial link) to form a household.  
- **Surname-only logic**: causes roommate conflation — use multi-evidence (address + email/phone + relationship).  
- **PO Boxes**: do not use for household formation; treat separately from street delivery points.  
- **Churn from upstream formatting changes**: lock down address normalization and monitor drift.  
- **Running big rebuilds on laptops**: use dedicated compute to prevent timeouts.

---

## Success Metrics

- Household precision ≥ 98% (low false merges); recall ≥ 95% for eligible addresses.  
- Mail bounce rate ↓; delivery success ↑ after golden address adoption.  
- Suppression accuracy ≥ 99% for household-level opt-outs.  
- Duplicate Person rate ↓; average time to household new mover ↓.  
- Unmerge rate trending down month-over-month after tuning.

---

## Summary

Householding MDM in CluedIn depends on **clean addresses**, **robust person/address matching**, and **clear household formation rules** with dates and roles. Keep golden household attributes canonical, aggregate preferences conservatively, and validate across tricky dwelling types (multi-unit, dorms, aged-care) before go-live.
.