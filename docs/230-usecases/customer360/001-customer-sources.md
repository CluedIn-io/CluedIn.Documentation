---
layout: cluedin
title: Customer 360 Case
nav_order: 180
has_children: false
permalink: /customer360
parent: Use Cases Summary
---

# Customer 360 in CluedIn — Step-by-Step Implementation Guide

Customer 360 creates a single, trusted view of each customer across CRM, e-commerce, marketing, support, billing, and product systems. This guide walks you end-to-end: ingest → standardize → match/link → golden record → enrich → govern → publish.

---

## Outcomes

- A **golden customer record** per real-world customer (person or organization).
- Linked entities: **Customer/Person/Account ↔ Contacts/Addresses ↔ Orders/Tickets/Subscriptions/Interactions ↔ Consents/Preferences**.
- Quality, lineage, and rollback for stewardship and compliance.
- **Publish/Sync** to CRM, marketing, CS tooling, and analytics.

---

## Prerequisites

- Source access: CRM, e-commerce, marketing automation, support/ITSM, billing/subscriptions, product telemetry (optional), spreadsheets.
- Clarify the **customer model**:
  - B2C: primary entity = `Person` with optional `Household`.
  - B2B: `Account/Organization` with linked `Contact(Person)` and roles.
- **RACI**: Stewards/owners need **Accountable** access.
- Use a **dedicated server/VM** for heavy ingestion/matching/toolkit operations (avoid laptops).

---

## Reference Data Model

**Core entities**
- `Person` (B2C or contact in B2B)
- `Account` / `Organization` (B2B)
- `Customer` (canonical wrapper pointing to Person or Account)
- `Address`, `ContactPoint` (Email/Phone), `Consent`, `Preference`
- `Order`, `Subscription`, `Ticket`/`Case`, `Interaction` (events)
- Optional: `Household` (for Householding), `Segment`, `LifecycleStage`

**Key attributes (examples)**
- Person: FirstName, LastName, DOB, Email(s), Phone(s), PrimaryAddress, MarketingOptIn, Country.
- Account: LegalName, TaxID/DUNS, Domain, Industry, Size, BillingAddress.
- Customer (derived): Status, Segment, LTV, LastActivity, CompletenessScore.

**Relationships**
- Account ↔ Contacts(Person)
- Customer ↔ Orders/Subscriptions/Tickets/Interactions
- Customer ↔ Consents/Preferences
- Person ↔ Household (optional)

---

## Step 1 — Connect & Ingest Sources

**Portal**: *Data Sources → Add Source*  
1. CRM masters (leads/contacts/accounts).  
2. E-commerce platform (customers, orders).  
3. Marketing automation (lists, events, consents).  
4. Support/ITSM (tickets/cases).  
5. Billing/subscriptions (plans, invoices).  
6. Spreadsheets/CSV (legacy imports).

> Capture provenance on ingest: `SourceSystem`, `SourceRecordID`, `IngestedAt`.

---

## Step 2 — Define Entities & Mappings

**Portal**: *Entity Explorer → + Create Entity Type*  
- Create `Person`, `Account`, `Customer`, `Address`, `ContactPoint`, `Consent`, `Order`, `Subscription`, `Ticket`, `Interaction`.  
- Map source fields → canonical attributes (e.g., `crm.email` → `ContactPoint.Email`).  
- Persist **lineage** (original values + mapping metadata).

**B2B note**: Model `Customer` as the Account golden, with linked Contacts for communications.

---

## Step 3 — Standardization & Normalization (Data Part Rules)

**Portal**: *Governance → Rules (Data Part Rules)*  
Create rules to clean inputs **before** matching:

- **Names/Text**: trim, case, punctuation; strip HTML/emoji where policy requires.  
- **Emails**: lower-case; basic regex; (optional) provider-specific canonicalization.  
- **Phones**: convert to **E.164**; tag `InvalidPhone` if parse fails.  
- **Addresses**: parse components; normalize ISO-2 `Country`; optional geocoding.  
- **IDs**: normalize CustomerID, AccountID; validate TaxID/DUNS for B2B.  
- **Domains**: extract from email for B2B domain inference.  

**Recommended tags**: `Standardized`, `InvalidEmail`, `InvalidPhone`, `InvalidAddress`, `LegacySource`.

---

## Step 4 — Identity Resolution (Matching & Linking)

**Portal**: *Entity Matching*  

### Person (B2C / Contacts)
- **Blocking keys**: (Email), (Phone), (LastName + DOB), (CustomerId).  
- **High-confidence**: exact Email OR exact Phone OR exact CustomerId.  
- **Candidate**: fuzzy Name ≥ 0.92 AND Address similarity ≥ 0.9 (same Country).  
- Review in **Data Stewardship**; approve merges; **Unmerge** errors.

### Account (B2B)
- **Blocking**: (Domain), (TaxID), (Country + CleanNameSoundex).  
- **High-confidence**: exact `TaxID` OR exact `Domain`.  
- **Candidate**: fuzzy `LegalName` ≥ 0.92 AND same Country; supplement with address/phone.

### Person↔Account Linking (B2B)
- Link Contacts to Accounts by explicit AccountId; else infer by email domain + stewardship review.

**Pitfalls to avoid**
- Over-merging by name alone (married names, common surnames). Require multi-evidence.  
- Cross-country merges; guard with `Country`.

---

## Step 5 — Stewardship Workflow

**Portal**: *Data Stewardship → Match Review*  
- Triage by confidence and impact (e.g., number of linked orders).  
- Approve/Reject; tag `AmbiguousMatch` for edge cases.  
- Use **History** for traceability; **Unmerge** if needed (rollback captured).

---

## Step 6 — Golden Record Survivorship

**Portal**: *Governance → Rules (Golden Record Rules)*  
Define attribute precedence and tie-breakers:

| Attribute        | Precedence (high → low)                     | Tie-breaker                          |
|------------------|----------------------------------------------|--------------------------------------|
| Primary Email    | CRM > E-com > Support > Marketing            | Most recently verified/active        |
| Primary Phone    | CRM > Support > E-com                        | Valid E.164 + last confirmed         |
| Name             | CRM > E-com                                  | Longest non-marketing version        |
| Address          | Verified Delivery > Billing > CRM            | Most recent verified                  |
| Account Domain   | CRM > Verified from Email Domain             | Steward override                      |
| Segment/Stage    | CRM > Derived (rules)                        | Most recent                           |
| Consents         | **Most restrictive wins** (by channel)       | N/A                                   |

**Actions**
- Compute `CompletenessScore` (weight required attributes).
- Tag `MarketingReachable` when Email valid + opt-in and Phone valid (if SMS).
- Tag `CustomerLifecycleStage` (Lead/Prospect/Active/ChurnRisk) via rules.

---

## Step 7 — Consent & Preference Management

**Portal**: *Entity Explorer / Rules*  
- Model `Consent` with Purpose, Channel, Status, Timestamp, Source.  
- Enforce via rules:
  - If `Consent(Marketing.Email) != granted` → tag `DoNotContactEmail`.  
  - If `DoNotSell`/CPRA → tag and propagate to exports.  
- Aggregate consents from multiple systems; preserve source and evidence.

---

## Step 8 — Enrichment (Optional)

**Portal**: *Data Sources / Rules*  
- Append firmographics (B2B: industry, size), demographics (B2C policy-dependent), geocoding, or CLV/propensity scores.  
- Track `LastEnrichedAt`, provider, and confidence; re-check on schedule.

---

## Step 9 — Data Quality Scoring & Dashboards

**Portal**: *Data Quality → Profiling / Scorecards / Dashboards*  
- KPIs: valid email/phone %, address standardization %, duplicate rate, consent coverage, completeness by segment/source.  
- Create **alerts** on regressions (e.g., Valid Email < 98%).

---

## Step 10 — Governance, Security & Lifecycle

**Portal**: *Governance → Permissions / Policies / Retention*  
- Restrict PII fields; apply least-privilege access.  
- **Retention** (e.g., inactive leads > 24 months → archive/delete).  
- Audit: merges/overrides/exports are captured in **History**; **Undo/Restore** supported for data changes and cleaning projects.

---

## Step 11 — Publish / Integrate

**Portal**: *Exports*  
- **CRM**: push Golden Customer + key attributes; keep GUID mapping (old→new).  
- **Marketing**: export reachable audiences with consent flags and suppression lists.  
- **Support/CS**: sync authoritative contact details and lifecycle stage.  
- **Analytics/DW**: publish wide `DimCustomer` + relationship tables (Orders, Tickets, Interactions).  
- **APIs/Eventing**: emit customer-changed events.

> Start **read-only** to validate mappings, then make CluedIn authoritative where appropriate.

---

## Step 12 — Scheduling & Operations

- Schedule ingestion, matching, golden updates, enrichment, and exports (run heavy jobs off-peak on a **dedicated VM/server** to avoid timeouts).  
- Monitor job runtimes and queue depth; investigate spikes (often source drift).

---

## Step 13 — Validate & UAT

- Sample 100–200 customers across sources/segments.  
- Verify no cross-person conflation; confirm B2B Person↔Account links.  
- Validate survivorship outcomes and consent enforcement end-to-end.  
- Business sign-off from CRM/Marketing/Support/Compliance.

---

## Go-Live Checklist

- [ ] All in-scope sources ingested with provenance.  
- [ ] Matching thresholds tuned; **Unmerge** tested; false-positive rate low.  
- [ ] Golden survivorship rules approved; `CompletenessScore` thresholds set.  
- [ ] Consent model enforced; suppression feeds validated.  
- [ ] Exports mapped and tested in CRM/MA/CS and DW.  
- [ ] Permissions & retention configured; audit/rollback verified.  
- [ ] Product Toolkit package built and promoted (run on **dedicated box** with **Accountable** access).

---

## Example Rules (Snippets)

**Normalize Email (Data Part Rule)**
- Condition: `Email present`  
- Actions: lower-case; regex validation; tag `InvalidEmail` on fail.

**Phone to E.164**
- Condition: `Phone present`  
- Actions: parse/format; tag `InvalidPhone` on failure.

**Customer Identity (Person Auto-merge)**
- If `Email exact` OR `Phone exact` OR `CustomerId exact` → Confidence = 1.0 (auto).  
- Else if `FuzzyName ≥ 0.92` AND `AddressSim ≥ 0.9` AND `Country equal` → Confidence = 0.95 (steward).

**Golden Survivorship (Primary Email)**
- Precedence: CRM > E-com > Support > Marketing; tie-break = most recently verified + reachable consent.

**MarketingReachable Flag**
- If `ValidEmail` AND `Consent(Email)=granted` → `MarketingReachable=true`; else false.

**Lifecycle Stage (Derived)**
- If `Orders>0 AND LastOrder < 365d` → `Active`;  
- If `Orders>0 AND LastOrder ≥ 365d` → `ChurnRisk`;  
- If `Orders=0 AND LastInteraction < 90d` → `Prospect`.

---

## Common Pitfalls & How to Avoid Them

- **Over-fuzzy merges** → require high-confidence evidence (email/phone/ID); steward candidates.  
- **Channel overrides pollute golden** → keep Golden canonical; apply channel transforms in exports.  
- **Ignoring consent in exports** → wire suppression flags into all downstream feeds.  
- **Address issues cause duplicates** → standardize and geocode before matching.  
- **Running heavy jobs on laptops** → use dedicated compute to prevent timeouts.

---

## Success Metrics

- Duplicate rate (Person/Account) **< 1–2%** with high precision auto-merge.  
- Valid Email ≥ **98%**, Valid Phone ≥ **95%**; Address standardized ≥ **97%**.  
- Consent coverage for marketable customers ≥ **99%** accurate.  
- Time-to-resolve stewardship queue ↓; `MarketingReachable` growth ↑.  
- Downstream CRM/MA/CS exception rate ↓ after go-live.

---

## Summary

Customer 360 in CluedIn unifies identities, standardizes attributes, enforces consent, and publishes a governed, audit-ready customer truth to every system. Start with clean identifiers and solid survivorship, validate merges with real samples, and keep Golden canonical while handling channel-specific needs in your exports.
