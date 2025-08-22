---
layout: cluedin
title: Centralised Master Data Management
nav_order: 180
has_children: false
permalink: /centralised-master-data-management
parent: Use Cases Summary
---

# Centralised Master Data Management (MDM) with CluedIn — End-to-End Implementation Guide
**Goal:** Operate a single, governed “system of record” for master data (Customers, Suppliers, Products, etc.) with **CluedIn** at the core. Use **Microsoft Power Apps** to capture/maintain master data via forms and **Power Automate** to orchestrate validation, approvals, deduplication, and write-back — with full auditability, stewardship, and rollback in CluedIn.

---

## What You’ll Build (at a glance)

1. **CluedIn Core**
   - Canonical entities & relationships
   - Reference data (RDM), quality rules, matching, survivorship
   - Stewardship work queues, audit history, rollback
   - Exports/APIs to downstream apps

2. **Power Platform Layer**
   - **Power Apps**: secure forms for create/update requests (new customer, supplier update, product introduction, etc.)
   - **Power Automate**: early validation, duplicate check, approvals (business + data stewardship), and commit to CluedIn
   - Optional **Dataverse**: staging + business workflow metadata

3. **Operational Guardrails**
   - Least-privilege access, API tokens, environment separation
   - Monitoring & alerts; runbooks for rollback and incident response

---

## Outcomes

- A **centralised MDM hub** in CluedIn with golden records for in-scope domains.
- **Standardised, validated, deduplicated** master data pushed to consuming systems.
- **Self-service** create/update via **Power Apps** with **Power Automate** approvals.
- **Early validation** and **dedupe preview** before anything hits production data.
- Full **lineage, audit, and rollback** for every change.

---

## Prerequisites

- CluedIn environment (non-prod + prod) with admin access.
- Defined **MDM scope & ownership** (data domains, data owners, stewards).
- API access to CluedIn (see *Administration → API Tokens*).
- Power Platform environment with permissions to create **Power Apps**, **Power Automate** flows, and (optionally) **Dataverse** tables.
- A **dedicated VM/server** for heavy CluedIn jobs (ingestion, matching, toolkit), not a laptop (prevents timeouts).

---


---

# PART A — Establish the CluedIn MDM Foundation

## Step A1 — Define Scope, Ownership, and SLAs
1. **Pick domains** for the first wave (e.g., Customer, Supplier, Product).
2. **Assign RACI** per domain (Data Owner, Steward, Approver).
3. Define **SLAs** for requests (e.g., new supplier in ≤ 1 business day).
4. Document **mandatory fields**, validation policies, and matching evidence (e.g., TaxID/DUNS for suppliers; GTIN/Brand+MPN for products).

**Deliverables:** Scope doc, RACI matrix, SLA table, mandatory-field matrix.

---

## Step A2 — Model Canonical Entities & Relationships
1. In **Entity Explorer**, create canonical types (e.g., `Customer`, `Supplier`, `Product`, `Address`, `Contact`, etc.).
2. Define attributes, data types, and constraints; keep **variant vs base** split when relevant (e.g., `Product` vs `Variant`).
3. Model relationships (edges) you’ll need for survivorship and governance (e.g., `Supplier -> Product`, `Customer -> Address`).

**Tip:** Keep entity design **stable**; evolve via versioning, not breaking changes.

---

## Step A3 — Reference Data Management (RDM)
1. Load canonical sets (ISO country, currency, UoM, tax codes, product categories).
2. Build **mappings** from source codes → canonical codes.
3. Version and **Publish** approved sets.
4. Add rules for **Find Closest Match** where semantics matter (e.g., category alignment).

**Goal:** 100% code mapping coverage to avoid downstream fragmentation.

---

## Step A4 — Data Quality Rules (Normalize + Validate)
Implement **Data Part Rules** to standardize before any matching:
- Names/text: trim, case, punctuation, diacritics
- Emails: regex; Phones: E.164; Addresses: parsing + country ISO-2
- Identifiers: checksums/structure (VAT/DUNS/GTIN/IBAN)
- RDM canonicalization (currency, UoM, tax code)
- Tags: `Standardized`, `InvalidEmail`, `InvalidPhone`, `UnknownCountry`, etc.

**Outcome:** Reliable inputs for deterministic matching.

---

## Step A5 — Matching & Survivorship (Golden Records)
1. Configure **blocking & match keys** per domain (e.g., Supplier uses TaxID/DUNS → high confidence).
2. Set thresholds: auto-merge (≥0.97), steward review (0.90–0.97).
3. Define **Golden Record Rules** (attribute precedence + tie-breakers).
4. Add **actions**: completeness scoring, verification flags, tags.

**Safety:** Prove **Unmerge** and **Undo** on a sandbox dataset before live.

---

## Step A6 — Stewardship & Governance
1. Configure **work queues** (invalids, duplicates, missing mandatory fields).
2. Enable **History** and train stewards on **Undo** and **Unmerge**.
3. Set **Permissions** (roles, least privilege; sensitive fields restricted).

---

## Step A7 — Exports & Downstream Interfaces
1. Define export views for consuming systems (CRM, ERP, PIM, DW).
2. Start **read-only**, validate mappings, then move to **authoritative sync**.
3. Keep **lineage columns** (source IDs, timestamps, quality flags).

---

# PART B — Power Platform Intake: Forms, Early Validation, Workflow

> Two patterns are common. Pick the one that fits your org (or mix them):
>
> **Pattern 1 — Direct-to-CluedIn**: Power Apps → Flow → CluedIn API (no Dataverse).  
> **Pattern 2 — Dataverse Staging**: Power Apps writes to a Dataverse table; Flow orchestrates validation + CluedIn upsert.

---

## Step B1 — Security & Connectors

### In CluedIn
1. Generate a **least-privilege API token** (Administration → API Tokens).
2. Scope it to create/update the specific domain(s) and read for dedupe preview.
3. Store the token securely (Key Vault/Power Platform environment variable).

### In Power Platform
1. Create a **Custom Connector** (or use HTTP actions):
   - **Base URL**: your CluedIn API endpoint.
   - **Auth**: Bearer token header (or OAuth if your environment supports it).
2. Define operations you’ll call often (examples):
   - `POST /entities/{type}/validate` (preflight validation)  
   - `POST /entities/{type}/staging` (stage request)  
   - `POST /matching/preview` (dedupe preview)  
   - `POST /workflows/{name}/trigger` (optional)  
   - `GET  /entities/{type}/{id}` (read back)  
   *(Endpoint names vary by tenant/version; map to your API catalogue.)*

**Tip:** Store the token in a **Power Platform connection reference** or **environment variable**; never hardcode in flows.

---

## Step B2 — Power Apps: Build the Request Forms
1. **App Type:** Canvas app (start with “New Customer/Supplier/Product” form).
2. **Data Model:** Either write directly to CluedIn via custom connector or to a **Dataverse staging table** (recommended for audit + drafts).
3. **Form Sections:** 
   - **Identity:** legal name/trading name, TaxID/DUNS (B2B), GTIN/Brand/MPN (Product), key personal info (B2C policy).
   - **Contact/Address:** email/phone, parsed address fields (Line1/City/Region/Postcode/Country).
   - **Reference Data:** country/currency/UoM/category (driven by RDM).
   - **Attachments (optional):** documents for KYC/Onboarding (ID proof, contracts).
   - **Notes & Justification** for business approval.

4. **Client-side early checks (Power Apps)**
   - Regex for email/phone; country code in a picklist bound to canonical RDM.
   - Simple **duplicate hint**: as the user types TaxID/Domain/GTIN, call a **search endpoint**; surface “Possible match found” links.
   - Visualize **completeness** with a progress bar.

**UX tip:** Use **normalisers** (uppercasing codes, trimming whitespace) in the form before submit.

---

## Step B3 — Power Automate: Early Validation Flow
**Trigger:** Power Apps (OnSelect) or Dataverse (OnCreate).

**Flow steps (detailed):**
1. **Initialize context** (request id, domain, requester, environment).
2. **Compose payload** (map form fields to CluedIn schema).
3. **HTTP — Validation**: call CluedIn *preflight validation* (or rules evaluate endpoint).  
   - On fail → return errors to the app; highlight fields; set status = `ValidationFailed`.
4. **HTTP — Dedupe Preview**: call CluedIn *matching preview* with high-confidence keys.  
   - If **candidate matches** exist (score ≥ review threshold), return list to the app for user review.
   - Optionally, **halt** and require steward review before continuing.
5. **HTTP — Reference Matching** (optional): use **Find Closest Match** for categories/payment terms etc. Keep original value for lineage.
6. **Branch:** 
   - If **No risk** (passes threshold + no candidates) → **Auto-route to Approval**.  
   - If **Medium risk** (candidates exist) → Create a **Steward Task** in CluedIn; wait for decision.  
   - If **High risk** (strong dupes or policy flags) → **Reject** with guidance.

7. **Approval(s):**
   - Use **Start and wait for an approval** (Power Automate).  
   - Approvers: Data Owner + Domain Steward (parallel or sequential).  
   - Reminder/timeout policy aligned to SLA.  
   - Store decision & comments (Dataverse or in CluedIn notes).

8. **Commit:**
   - **HTTP — Upsert to Staging** in CluedIn with `RequestId` and `RequestedBy`.  
   - **HTTP — Trigger Rules** to normalize & compute completeness.  
   - **HTTP — Run Matching** (if not already) and **Promote to Golden** per survivorship.

9. **Notify & Return:**
   - Update Power Apps with **result id**, completeness score, and any steward actions.
   - Send Teams/Email confirmation (optional).

10. **Error handling:**
    - Catch 4xx/5xx → log to Dataverse “IntegrationLog”, notify support channel, and surface user-friendly message.

**Best practices:**
- Keep **idempotency**: pass a `requestId`; replays don’t create duplicates.
- Use **parallel branches** for enrichment that doesn’t block approval.

---

## Step B4 — Power Automate: Update Requests (Change Management)
Repeat B3 for **update** scenarios:
1. Lock **sensitive fields** (e.g., TaxID, DUNS) behind extra approval.
2. Pre-check: compare proposed changes vs current Golden; highlight **breaking changes** (e.g., category re-map).
3. Route to **Data Owner** for approval and **Steward** for quality checks.
4. Commit via CluedIn upsert with **change reason** and **source evidence**.

---

## Step B5 — Steward Collaboration & Exception Handling
- If dedupe preview returns **ambiguous matches**, the flow:
  1. Creates a **CluedIn Steward Task** referencing the request data.
  2. Waits for the steward to **Approve/Reject/Request changes**.
  3. Continues or exits based on steward outcome.
- For **policy exceptions** (e.g., missing documents), branch to a **conditional approval** that requires additional evidence uploaded in the app.

---

# PART C — CluedIn Workflows Post-Commit

## Step C1 — Rules & Matching Execution
- On upsert: run **Data Part Rules**, **Find Closest Match** (for lookups), then **Matching** with thresholds.
- If **auto-merge**: promote to Golden and tag `Verified`.
- If **steward review required**: record sits in **Match Review** queue.

---

## Step C2 — Golden Record Survivorship & Publishing
- Apply attribute precedence (ERP > Registry > CRM, etc.).
- Compute `CompletenessScore`, `VerificationFlags`, and channel-specific `Reachability`.
- Include **lineage** (SourceSystem, SourceRecordID) and **request metadata** for traceability.
- Publish to **downstream exports** (CRM/ERP/PIM/DW) on schedule or ev



