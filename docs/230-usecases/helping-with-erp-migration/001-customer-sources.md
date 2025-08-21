---
layout: cluedin
title: ERP Migration
nav_order: 180
has_children: false
permalink: /erp-migration
parent: Use Cases Summary
---

# ERP Migration in CluedIn — Step-by-Step Implementation Guide

ERP migrations (e.g., SAP, Oracle, Dynamics, NetSuite) demand clean, reconciled, and governed master and transactional data. CluedIn helps you **discover, cleanse, standardize, deduplicate, enrich, and publish** trusted data into the target ERP, reducing risk and accelerating migration timelines.

---

## Outcomes

- Trusted **Golden Records** for master data domains (Customers, Suppliers, Products, Chart of Accounts, Cost Centers, etc.).  
- Standardized and reconciled **reference data** (currencies, units of measure, payment terms, tax codes).  
- Cleansed and deduplicated **transactions** (open POs, invoices, orders) linked to correct masters.  
- **Audit trail** and rollback capabilities for all transformations.  
- **Exports** packaged in migration-ready format for ERP cutover.  

---

## Prerequisites

- Source system access: legacy ERP(s), CRM, PIM, Finance/HR systems, spreadsheets.  
- Agreement on **scope**: which entities are in migration wave (Customers, Vendors, Products, GL, etc.).  
- **Target ERP design**: field mappings, canonical formats, mandatory attributes, coding standards.  
- **RACI**: Ensure stewards/owners have **Accountable** access to governed objects.  
- Dedicated environment/VM for heavy ingestion and matching runs.  

---

## Reference Data Model

**Core Master Data Entities**  
- `Customer`  
- `Supplier`  
- `Product` / `Material`  
- `Employee` (for HR modules)  
- `GLAccount`, `CostCenter`  

**Reference Data Entities**  
- `Currency`  
- `UnitOfMeasure`  
- `TaxCode`  
- `PaymentTerms`  

**Transactional Entities (optional, for cutover)**  
- `PurchaseOrder`  
- `SalesOrder`  
- `Invoice`  

---

## Step 1 — Connect & Ingest Legacy Sources

**Portal**: *Data Sources → Add Source*  
1. Add legacy ERP extracts (Customers, Vendors, Products, GL, etc.).  
2. Add supporting systems (CRM, PIM, Finance).  
3. Add spreadsheets/flat files for reference data overrides.  
4. Profile volumes, completeness, duplicates, and data health.  

**Tip**: Load into staging entities with clear provenance (`SourceSystem`, `SourceRecordID`).  

---

## Step 2 — Define Target Canonical Entities

**Portal**: *Entity Explorer → + Create Entity Type*  
1. Create canonical entity types aligned with **target ERP design**.  
2. Map legacy attributes → canonical attributes.  
   - Example: `VendorName` → `Supplier.LegalName`  
   - Example: `MatDesc` → `Product.Description`  
3. Preserve lineage: store original values + mapping metadata.  

---

## Step 3 — Standardize & Cleanse Data

**Portal**: *Governance → Rules (Data Part Rules)*  
- **Names**: trim, case, remove stopwords.  
- **Addresses**: parse, normalize, geocode, standardize country codes (ISO).  
- **Identifiers**: validate Tax IDs, DUNS, IBANs, GTINs.  
- **Reference Data**: map currencies, UoM, tax codes to canonical sets.  
- **Contacts**: normalize phone numbers to E.164; validate emails.  

**Tags**: `Standardized`, `InvalidTaxID`, `InvalidUoM`, `LegacyCode`.  

---

## Step 4 — Deduplicate & Match

**Portal**: *Entity Matching*  
1. Configure blocking & matching keys per domain:  
   - Customer: Tax ID, Email, Fuzzy Name + Address.  
   - Supplier: Tax ID, DUNS, Fuzzy Name + Country.  
   - Product: Brand + MPN, GTIN, Fuzzy Title + Category.  
2. Run matching jobs; steward ambiguous cases in **Data Stewardship**.  
3. Approve merges, unmerge mistakes, tag ambiguous records.  

---

## Step 5 — Golden Record Survivorship

**Portal**: *Governance → Rules (Golden Record Rules)*  
- Define attribute precedence: ERP > CRM > Spreadsheet > Other.  
- Apply tie-breakers (most recent, highest quality, verified source).  
- Compute `CompletenessScore`.  
- Tag records: `ReadyForERP`, `Incomplete`, `NeedsStewardship`.  

---

## Step 6 — Reference Data Management

**Portal**: *Governance → Reference Data (RDM)*  
- Create canonical code sets for Currency, UoM, Tax Codes, Payment Terms.  
- Map all legacy codes to canonical values.  
- Validate completeness: 100% of source codes must map.  
- Version & publish approved sets for ERP cutover.  

---

## Step 7 — Transactional Data Preparation (Optional)

**Portal**: *Entity Explorer / Rules*  
- Cleanse open transactions (POs, invoices, orders).  
- Link to new Golden Records (CustomerId, SupplierId, ProductId).  
- Validate mandatory fields required by target ERP.  
- Drop obsolete/closed transactions per business rules.  

---

## Step 8 — Stewardship & Governance

**Portal**: *Data Stewardship / Governance*  
- Queue unresolved duplicates, invalid addresses, or unmapped codes for review.  
- Enforce RACI roles (Accountable = stewards, Informed = migration team).  
- Track approvals in History; enable **rollback** for changes.  

---

## Step 9 — Export Migration Packages

**Portal**: *Exports*  
1. Create export pipelines aligned with ERP **migration load templates**.  
   - Example: Customer master load (CSV/XML/JSON).  
   - Example: Supplier master load.  
   - Example: Product master load.  
2. Include **mapping keys** (old → new IDs).  
3. Validate against ERP staging load; adjust formats.  

---

## Step 10 — Validate & UAT

- Sample 100+ customers/suppliers/products across sources.  
- Confirm Golden attributes align with ERP requirements.  
- Validate reference data usage (currencies, UoM, tax codes).  
- Test full end-to-end load into ERP test environment.  
- Steward sign-off + ERP functional team approval.  

---

## Step 11 — Cutover & Go-Live

- Freeze legacy systems for final extract.  
- Re-run ingestion, cleansing, matching, golden record, and exports.  
- Deliver final migration package to ERP team.  
- Run post-load reconciliation dashboards (counts, sums, duplicates).  

---

## Step 12 — Post-Migration Governance

- Use CluedIn as ongoing **MDM hub** feeding ERP & other systems.  
- Continue to steward Golden Records; enforce retention & policies.  
- Monitor KPIs: duplicate rate, completeness, ERP load exceptions.  

---

## Example Rules (Snippets)

**Normalize Address**
- Condition: `Address.Raw present`  
- Action: parse into Line1, City, Postcode, Country (ISO); geocode; tag `StandardizedAddress`.

**Currency Mapping**
- Condition: `CurrencyCode not in ISO4217`  
- Action: map legacy code (e.g., `USDOLLARS`) → `USD`; tag `LegacyCode`.

**Golden Survivorship (Customer Name)**
- Source precedence: ERP > CRM > Marketing list.  
- Tie-breaker: longest non-abbreviated version.

**Tag Ready for ERP**
- If completeness ≥ 90% AND mandatory fields populated → `ReadyForERP=true`.  

---

## Common Pitfalls & How to Avoid Them

- **Ignoring reference data**: unmapped codes cause ERP load failures → enforce 100% mapping.  
- **Over-merging customers/suppliers**: require Tax ID or multi-evidence for auto-merge.  
- **Late data freeze**: always plan final extract & delta runs.  
- **Running heavy jobs on laptops**: use a dedicated VM/server to avoid timeouts.  
- **Skipping audit trail**: regulators may require proof → keep History enabled.  

---

## Success Metrics

- Duplicate rate < 2% across Customers/Suppliers/Products.  
- 100% reference code mapping coverage.  
- Completeness ≥ 95% for mandatory ERP attributes.  
- ERP load exception rate < 0.5%.  
- Stewardship backlog cleared before cutover.  

---

## Summary

ERP Migration with CluedIn ensures that data entering the new system is **clean, standardized, governed, and auditable**. By creating Golden Records, reconciling reference data, preparing transactions, and exporting in ERP-ready formats, you minimize cutover risk and establish CluedIn as an ongoing MDM hub post-migration.
