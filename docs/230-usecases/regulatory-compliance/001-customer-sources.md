---
layout: cluedin
title: Regulatory Compliance
nav_order: 180
has_children: false
parent: Use Cases Summary
permalink: /regulatory-compliance
---

# Regulatory Compliance in CluedIn — Step-by-Step Implementation Guide

This guide shows how to implement a Regulatory Compliance program in CluedIn covering **data discovery, classification, subject rights (DSAR/SAR), minimization, retention, lineage, and auditing**. It’s designed to help you meet frameworks like **GDPR, CCPA/CPRA, LGPD**, and sector policies.

---

## Outcomes

- End-to-end visibility of **where personal data lives**, how it’s processed, and who can access it.
- Automated **classification, tagging, and policy enforcement** (minimization, masking, retention).
- **Subject rights fulfillment** (access/export/delete/restrict) with auditability.
- **Dashboards & alerts** for continuous compliance posture monitoring.

---

## Prerequisites

- Source access to systems that store personal data (CRM, ERP, Support, Product, Marketing, Data Warehouse, File Stores).
- **RACI** set so the implementation team has **Accountable** access to governed objects.
- A **dedicated VM/server** for heavy jobs (discovery scans, toolkit exports/imports).

---

## Reference Compliance Model

**Core entities**
- `Person` (data subject), `Customer`, `Employee`, `Prospect`
- `Consent` (purpose, lawful basis, status, timestamp)
- `ProcessingActivity` (system/process, purpose, legal basis)
- `DataAsset` (tables/files/collections with PII)
- `DSAR` (request, identity proof, scope, due date, status)

**Tags & Taxonomy (examples)**
- Sensitivity: `PII`, `SensitivePII`, `Financial`, `Health`, `Minor`
- Purpose: `Marketing`, `Support`, `Billing`, `Analytics`
- Residency/Transfer: `EU`, `US`, `RestrictedTransfer`
- Policy state: `RetentionDue`, `DoNotSell`, `DoNotContact`, `MaskInUI`

---

## Step 1 — Connect & Ingest Sources

**Portal**: *Data Sources → Add Source*  
Connect systems that likely contain personal data (CRM, support/ticketing, auth/IdP, billing, web/app events, marketing automation, data lake/warehouse, shared file stores).  
- Start with **read-only** access where possible.
- Capture source metadata (owner, region, DPO contact) as attributes.

---

## Step 2 — Data Discovery Scan

**Portal**: *Compliance → Discovery*  
Run automated scans to detect PII patterns (email, phone, national IDs, names, addresses).  
- Include **unstructured** stores (notes, PDFs, CSV drops) if available.
- Tag assets with `PII`/`SensitivePII` and map them to **ProcessingActivities**.

---

## Step 3 — Classification & Tagging Rules

**Portal**: *Governance → Rules (Data Part Rules)*  
Create rules to consistently classify records/fields:
- Pattern rules: detect emails, phones, tax IDs → tag `PII`.
- Domain-specific rules: payroll/benefits → tag `SensitivePII`.
- Source-based rules: marketing lists → tag `Marketing`.
- Confidence scoring + tags: `ClassifiedHigh/Medium/Low`.

> Tip: Keep names short and consistent (e.g., `ContainsPII`, `DoNotSell`).

---

## Step 4 — Build the Person Graph

**Portal**: *Entity Matching → Person/Customer/Employee*  
Link identities across systems to a single `Person`:
- Blocking keys: `(email)`, `(phone)`, `(name+dob)`, `(customerId)`.
- High-confidence rules: exact email/phone; Medium: fuzzy name + same domain/country.
- Review candidates in **Data Stewardship**; enable **Unmerge** for errors.

This enables **subject-centric** compliance actions later.

---

## Step 5 — Consent & Purpose Management

**Portal**: *Entity Explorer / Rules*  
Model `Consent` with attributes (purpose, lawful basis, source, timestamp, expiry).  
- Rules to **enforce** consent:  
  - If `Consent(purpose=Marketing).status != granted` → tag `DoNotContact`.  
  - If `DoNotSell` (CPRA) → exclude from ad/export segments; tag `DoNotSell`.

---

## Step 6 — Data Minimization & Masking

**Portal**: *Governance → Rules (Golden Record & Data Part)*  
- Masking rule examples:
  - Mask PAN/IBAN except last 4 for UI: set `MaskInUI=true` + store hashed surrogate.
  - Drop free-text PII from analytics exports: remove or redact fields.
- Minimization:
  - For `Analytics` purpose, persist only hashed IDs; remove names/emails.

---

## Step 7 — Retention Policies

**Portal**: *Governance → Retention Policies*  
- Define policies by entity/purpose (e.g., **Billing data = 7 years**, **Marketing leads = 24 months inactivity**).  
- Action: `Archive` first; promote to `Delete` after validation.  
- Add tags on approaching expiry: `RetentionDue`.

---

## Step 8 — DSAR / SAR Workflow (Subject Rights)

**Portal**: *Compliance → Requests (DSAR)*  
1. **Intake**: Create a `DSAR` entity with requester identity proof and scope (access/export/delete/restrict).  
2. **Locate**: Use the **Person graph** to collect linked records across systems.  
3. **Assemble**: Generate export package (JSON/CSV/PDF) excluding masked internal notes.  
4. **Delete/Restrict**: Apply rules to remove or lock records (respect legal holds).  
5. **Audit**: Log timestamps, handler, and evidence.  
6. **SLAs**: Track due dates (e.g., GDPR 30 days); dashboard alerts for SLA breaches.

---

## Step 9 — Data Lineage & Auditability

**Portal**: *Entity Explorer → History* and *Dashboards*  
- Ensure merges, overrides, masking, exports, and deletions are captured in **History**.  
- Maintain lineage from `DataAsset` → `ProcessingActivity` → `Person`.

---

## Step 10 — Access Control & RACI

**Portal**: *Governance → Permissions*  
- Restrict `SensitivePII` fields; grant **Accountable** to stewards.  
- Create data-domain roles (DPO, Marketing, Support).  
- Enforce `MaskInUI` in views and exports.

---

## Step 11 — Compliance Dashboards

**Portal**: *Data Quality / Compliance Dashboards*  
Track:
- % entities with `PII` classified  
- DSAR backlog & SLA compliance  
- Records by purpose & consent status  
- Retention due/overdue  
- Access/permission change logs  
- Cross-border transfer inventory

---

## Step 12 — Publish/Integrate Controls

**Portal**: *Exports*  
- Marketing suppression list: export `DoNotContact`/`DoNotSell`.  
- Analytics feed: export **minimized** Person view (no direct identifiers).  
- Security tooling: send `AccessAudit` events to SIEM.  
- ERP/CRM: sync consent flags and masked fields.

> Start **read-only**; validate mapping; then enable authoritative syncs.

---

## Step 13 — Scheduling & Operations

- Schedule discovery rescans, consent refresh, retention checks, DSAR jobs.  
- Run heavy scans off-peak on a **dedicated server/VM** to avoid timeouts.  
- Alert on anomalies (sudden surge in PII detection, SLA breach risk).

---

## Step 14 — Validate, UAT & Promote

- Test on 50–100 real subjects; verify consent enforcement, masking, and DSAR outputs.  
- Legal/DPO sign-off on survivorship, masking, and retention behaviors.  
- Package with **Product Toolkit**; ensure **Accountable** permissions; promote to staging → production.

---

## Example Rules (Snippets)

**Classify Email as PII**
- Condition: `Email matches pattern`  
- Action: add tag `PII`; set `MaskInUI=true`.

**Enforce Do Not Contact**
- Condition: `Consent(Marketing).status != granted` OR tag `DoNotSell`  
- Action: add tag `DoNotContact`; exclude from Marketing exports.

**Retention — Marketing Lead Inactivity 24m**
- Condition: `LastActivity > 24 months ago` AND `Customer=false`  
- Action: tag `RetentionDue`; after approval → `Archive` (then `Delete`).

**DSAR — Restrict Processing**
- Condition: `DSAR(type=Restrict).status = approved`  
- Action: set `ProcessingStatus=Restricted`; mask identifiers in exports.

---

## Go-Live Checklist

- [ ] All high-risk `DataAssets` scanned and classified (`PII`, `SensitivePII`).  
- [ ] Person graph validated; false merges < 2%.  
- [ ] Consent model enforced; suppression feeds tested.  
- [ ] Masking/minimization rules verified in UI and exports.  
- [ ] Retention jobs scheduled; archive → delete flow validated.  
- [ ] DSAR workflow tested (access/export/delete/restrict) with audit artifacts.  
- [ ] Permissions/RACI applied; sensitive fields restricted.  
- [ ] Dashboards and alerts configured; SIEM integration (if applicable).  
- [ ] Promotion package built with Product Toolkit on a **dedicated box**.

---

## Common Pitfalls & How to Avoid Them

- **Over-matching people by name only** → require email/phone or multi-evidence.  
- **Unscoped masking** → accidentally remove needed analytics fields; prefer **minimize** over blanket delete.  
- **Retention deletes re-ingested data** → align ingestion filters with retention policies.  
- **Consent not enforced downstream** → wire suppression tags into every export and segment.  
- **Running scans on laptops** → use dedicated compute to avoid timeouts and throttling.

---

## Success Metrics

- ≥ 95% PII assets classified; 100% of sensitive stores inventoried.  
- DSAR SLA compliance ≥ 99%; end-to-end time ↓ month over month.  
- % of entities with valid consent for each purpose; suppression accuracy ≥ 99.5%.  
- Retention coverage (% entities under active policy) and overdue items = 0.  
- Reduction in access to sensitive fields (least-privilege trend).

---

## Summary

By combining **discovery, classification, consent enforcement, minimization/masking, retention, subject-rights workflows, lineage, and auditing**, CluedIn gives you a repeatable, auditable framework for regulatory compliance. Start small, validate with real samples, and iterate rules until legal and operational stakeholders sign off.
