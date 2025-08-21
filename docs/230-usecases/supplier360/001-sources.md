---
layout: cluedin
title: Supplier 360
nav_order: 180
has_children: true
permalink: /supplier360
---

# Supplier 360 in CluedIn — Step-by-Step Implementation Guide

Supplier 360 delivers a single, trusted, and actionable view of each supplier across ERP, procurement, finance/AP, risk, and contract systems. This guide walks you through the end-to-end build in CluedIn: ingest → standardize → match/link → golden record → enrich → govern → publish.

---

## Outcomes

- A **golden supplier record** per supplier (and per site) with complete, standardized attributes.
- **Linked entities**: supplier ↔ sites ↔ contacts ↔ contracts ↔ POs ↔ invoices ↔ risk events.
- **Quality, lineage, and auditability** for compliance and operations.
- **Publish/Sync** to downstream systems (ERP, procurement, analytics).

---

## Prerequisites

- Access to source systems (e.g., SAP/Oracle ERP, Ariba/Coupa, AP platform, spreadsheets).
- RACI: Ensure you have **Accountable** access for the objects you’ll import/export.
- A dedicated environment (or VM) for heavy jobs (ingestion, matching, toolkit operations).

---

## Reference Data Model

**Core entities**
- `Supplier` (legal entity level)  
- `SupplierSite` (site/plant/branch)  
- `Contact` (people)  
- `Contract`  
- `PurchaseOrder`  
- `Invoice`  
- `RiskEvent` (e.g., sanctions hit, delivery failure, ESG breach)

**Common attributes (examples)**
- Supplier: LegalName, TradingName, TaxID (VAT/ABN/EIN), DUNS, RegistrationNo, Country, Address, BankAccount (IBAN/BIC), EmailDomain, Category, Status.
- SupplierSite: SiteName, Address, Country, GLN, ParentSupplierId.

**Relationships**
- Supplier **has** many SupplierSites, Contacts, Contracts, POs, Invoices, RiskEvents.

---

## Step 1 — Connect & Ingest Sources

**Portal**: *Data Sources → Add Source*  
1. Add ERP master data (Vendors/Suppliers + bank data).  
2. Add procurement networks (catalog, onboarding).  
3. Add AP/Finance (invoices, payments).  
4. Add risk/enrichment sources (sanctions, credit, ESG), optional.  
5. Add ad-hoc files (CSV/XLS) for legacy/one-off data.

**Tips**
- Use **sampling** first to inspect field sparsity and formats.
- Define **source metadata** (system name, extraction time, primary keys).

---

## Step 2 — Define Entities & Mappings

**Portal**: *Entity Explorer → + Create Entity Type*  
1. Create `Supplier` and `SupplierSite` entity types.  
2. Map source fields → target attributes (normalize names like `VendorName` → `LegalName`).  
3. Track **provenance** (SourceSystem, SourceRecordID).

**Tip**: Keep site-level data **separate** from the parent supplier; many duplicates stem from conflating these.

---

## Step 3 — Standardization & Normalization Rules

**Portal**: *Governance → Rules (Data Part Rules)*  
Create rules to standardize inputs **before** matching:
- **Names**: strip punctuation/stopwords; uppercase/lowercase consistency.  
- **Addresses**: split house/street/city/postcode; normalize country codes (ISO-2).  
- **Phones**: E.164 standardization.  
- **Tax IDs**: remove separators; validate checksum per country.  
- **Bank**: IBAN/BIC validation.  
- **Email domains**: extract domain from contact emails.

**Recommended tags**
- `Standardized`, `NeedsValidation`, `InvalidTaxID`, `InvalidBank`, `LegacySource`.

---

## Step 4 — Configure Identity Resolution (Matching)

**Portal**: *Entity Matching → Supplier*  
1. **Blocking keys** (to reduce comparisons):  
   - `(Country + CleanedLegalNameSoundex)`  
   - `(TaxID)` when present  
   - `(EmailDomain)` (fallback)
2. **Match rules** (examples):  
   - **High-confidence**: exact `TaxID` OR exact `DUNS`.  
   - **Medium**: `CleanedLegalName` fuzzy ≥ 0.92 AND same `Country`.  
   - **Supplemental**: phone OR email domain OR address similarity ≥ 0.9.
3. Set **thresholds** (e.g., Auto-merge ≥ 0.97; Steward review 0.90–0.97).
4. Run a **matching job** and review candidates in **Data Stewardship**.

**Pitfall to avoid**: Over-aggressive fuzzy name matching across different countries. Always include **Country** as a condition unless you have multi-national evidence.

---

## Step 5 — Stewardship: Review & Merge

**Portal**: *Data Stewardship → Match Review*  
1. Inspect candidate pairs; verify with TaxID, DUNS, or contracts.  
2. Approve merges; reject false positives; tag edge cases (`AmbiguousMatch`).  
3. Use **Unmerge** if a mistake is found (audit captured in History).

**Tip**: Triage by **confidence** and **impact** (number of downstream links).

---

## Step 6 — Golden Record Survivorship

**Portal**: *Governance → Rules (Golden Record Rules)*  
Define attribute precedence and tie-breakers:

| Attribute      | Precedence (highest → lowest)                             | Tie-breaker                 |
|----------------|------------------------------------------------------------|-----------------------------|
| LegalName      | ERP > Procurement > AP > CSV                               | Most recent update          |
| TaxID/DUNS     | ERP only                                                   | N/A                         |
| Address        | Site-specific registry > ERP > Procurement                 | Highest quality score       |
| BankAccount    | ERP (verified) > AP                                        | Verified flag = true        |
| Category       | Procurement taxonomy > ERP                                 | Most frequent value         |
| Status         | Risk compliant > Pending > On hold                         | Most recent risk check      |

Add **Actions**:
- Tag `VerifiedSupplier` when TaxID valid & sanctions clear.
- Compute **completeness score** and tag `LowCompleteness` < 0.8.

---

## Step 7 — Enrichment & Risk

**Portal**: *Data Sources → Add Source* (enrichment), *Governance → Rules*  
- Pull official registry details (legal address, directors where available).  
- Run **sanctions/PEP** checks; tag `SanctionsHit` with evidence fields.  
- Append credit/ESG risk ratings; store dates and providers.

**Tip**: Separate **enrichment freshness** (LastCheckedAt) and set a rule to re-check periodically.

---

## Step 8 — Quality Scoring & Dashboards

**Portal**: *Data Quality → Profiling / Dashboards*  
- Define KPIs: completeness %, duplicates, invalid TaxID, invalid bank, address parse rate.  
- Track Golden Record creation rate and match precision (steward overrides vs auto-merge).

---

## Step 9 — Governance, Security & Lifecycle

**Portal**: *Governance → Policies / Retention / Permissions*  
- Apply **RACI**: Accountable access for stewards; Restricted for sensitive fields (bank).  
- **Retention**: e.g., archive inactive suppliers after N years; delete after audit closure.  
- **Audit**: Ensure changes (merges, overrides) are captured in History; enable rollback.

---

## Step 10 — Publish / Integrate

**Portal**: *Exports*  
- **ERP sync**: push Supplier + Site golden attributes.  
- **Procurement**: push status/category/compliance flags.  
- **Analytics**: export wide table to warehouse/BI.  
- **Eventing/APIs**: expose CRUD/read APIs for master data consumers.

**Tip**: Start with a **read-only** feed to validate mapping, then switch to authoritative sync.

---

## Step 11 — Scheduling & Operations

- Schedule ingestion, matching, and golden updates (off-peak where possible).  
- Monitor job runtimes; alert on spikes (likely due to source anomalies).  
- For large batches, run heavy jobs on a **dedicated server/VM** to avoid timeouts.

---

## Step 12 — Validate & UAT

- Sample checks: 50–100 suppliers across regions and sources.  
- Verify tax/bank/address survivorship; confirm no cross-supplier conflation.  
- Have AP/Procurement/Compliance sign off on a **go-live checklist** (below).

---

## Step 13 — Package & Promote

**Portal/CLI**: *Product Toolkit*  
- Export entities, rules, policies, dashboards.  
- Promote to staging → production.  
- Ensure you have **Accountable RACI** and run large toolkit jobs on a **dedicated box**.

---

## Go-Live Checklist

- [ ] Ingestion schedules configured and ran successfully.  
- [ ] Matching thresholds tuned; low false-positive rate verified.  
- [ ] Golden survivorship rules approved by data owners.  
- [ ] Sanctions/credit enrichment configured and refreshed.  
- [ ] Exports mapped and validated in target systems.  
- [ ] Retention & access policies applied.  
- [ ] Runbooks for **rollback/unmerge** documented.

---

## Common Pitfalls & How to Avoid Them

- **Conflating sites with legal entities** → Model `SupplierSite` separately; match on site identifiers.  
- **Over-reliance on name similarity** → Require TaxID/DUNS or multi-evidence for auto-merge.  
- **Dirty TaxID formats** → Normalize and validate before matching.  
- **Bank detail risk** → Use verified source precedence; never crowdsource survivorship.  
- **Timeouts on big runs** → Stagger jobs; use dedicated compute; batch by country or source.  
- **Re-polluting golden records** → Disable or adjust problematic Rules *before* rollback/re-runs.

---

## Example Rules (Patterns)

**Data Part Rule — Normalize TaxID**
- Condition: `TaxID` present  
- Action: strip non-alphanumerics; upper; set `TaxID_Normalized`; validate checksum; tag `InvalidTaxID` if fail.

**Matching — Auto-merge**
- If `TaxID_Normalized` exact OR `DUNS` exact → Confidence = 1.0 (auto).  
- Else if `CleanedLegalName` fuzzy ≥ 0.92 AND `Country` equal AND (`EmailDomain` OR `AddressSim` ≥ 0.9) → Confidence = 0.96 (steward).

**Golden Record — Survivorship**
- `LegalName`: ERP > Registry > Procurement (most recent tie-break).  
- `Status`: if `SanctionsHit` then `OnHold` else `Active`.  
- Tag `VerifiedSupplier` when (`TaxIDValid` AND `SanctionsClear` AND completeness ≥ 0.85).

---

## Troubleshooting

- **Too many duplicates**: Lower auto-merge threshold; add blocking by Country; require TaxID/DUNS.  
- **Missed matches**: Add alternative keys (RegistrationNo, GLN, EmailDomain); tune fuzzy threshold upward/downward.  
- **Wrong golden values**: Review precedence order; check source quality; re-run with corrected rules.  
- **Slow processing**: See performance article; run heavy jobs on dedicated compute; schedule off-peak.

---

## Success Metrics

- Duplicate rate ↓, auto-merge precision ≥ 98%.  
- Golden record completeness ≥ 85–95% (target by region).  
- Time to onboard new supplier ↓ (days → hours).  
- Sanctions/risk check freshness ≤ N days.  
- Downstream exception rate (ERP/procurement) ↓.

---

## Summary

Supplier 360 in CluedIn combines **standardization**, **robust matching**, **clear survivorship**, and **governed publishing** to deliver one trusted view of every supplier. Follow the steps above, validate with real samples, and iterate your rules until precision and completeness meet your business targets.
.