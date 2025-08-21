---
layout: cluedin
title: Customer Acceleration Case
nav_order: 180
has_children: true
permalink: /customer-acceleration-case
---

# Customer Onboarding Acceleration in CluedIn — Step-by-Step Implementation Guide

Accelerate onboarding by using CluedIn to **ingest**, **validate**, **enrich**, **deduplicate**, and **publish** complete, compliant customer records to CRM and workflow systems. This guide shows you how to go from raw application data to a **ready-to-work** Golden Customer with SLAs, dashboards, and audit-ready governance.

---

## Outcomes

- **Golden Customer** (Person/B2C or Account+B2B Contacts) created automatically when requirements are met.
- **Readiness score** and **checklist** (KYC/consent/completeness) driving downstream task creation.
- **Fewer manual touches** via auto-standardization, enrichment, and duplicate prevention.
- **Faster time-to-first-action** (e.g., welcome email, provisioning, contract activation).
- Full **audit & rollback** for every transformation and decision.

---

## Prerequisites

- Source access: web forms, CRM leads, identity/KYC providers, e-signature, payments/billing, support/ITSM, legacy sheets.
- Clarify your **onboarding policy**:
  - Required documents/fields (per segment/region).
  - KYC/sanctions/credit checks needed by product or jurisdiction.
  - SLA targets (e.g., 95% within 24h).
- **RACI**: Stewards/owners must have **Accountable** access to governed objects.
- Use a **dedicated server/VM** for heavy runs (ingestion/matching/toolkit)—avoid laptops to prevent timeouts.

---

## Reference Data Model

**Core entities**
- `Lead` / `Application`
- `Person` (B2C) and/or `Account` (B2B) + `Contact`
- `Address`, `ContactPoint` (Email/Phone)
- `Document` (ID proof, contracts), `Consent`
- `KYCCheck` / `SanctionsCheck` / `CreditCheck`
- `Subscription` / `Contract` (optional)
- `Task` / `Case` (stewardship or operational follow-ups)

**Key attributes (examples)**
- Required fields by policy: Name, Email, Phone, Country, Address, DOB (B2C), TaxID/DUNS + Domain (B2B).
- Evidence: `KYCStatus`, `SanctionsStatus`, `CreditStatus`, `ConsentStatus`, `DocsReceived`.
- Derived: `ReadinessScore`, `OnboardingStage`, `CompletenessScore`.

**Tags (suggested)**
- `Standardized`, `InvalidEmail`, `InvalidPhone`, `InvalidAddress`, `MissingDocs`, `KYCRequired`, `KYCFailed`, `SanctionsHit`, `NeedsStewardReview`, `ReadyToCreate`, `ReadyToActivate`.

---

## Step 1 — Define Onboarding Policy & SLAs

**Portal**: *Governance → Policies*  
1. List mandatory fields & documents per segment/region/product.  
2. Define gating checks (KYC, sanctions, credit, consent).  
3. Set SLA thresholds and owners (e.g., “All retail signups KYC within 4 hours”).  
4. Translate policy into **rule specs** (see Steps 4–7).

---

## Step 2 — Connect & Ingest Sources

**Portal**: *Data Sources → Add Source*  
- Web form/app feed (applications), CRM leads, e-sign, KYC providers, payments/billing, ticketing/ITSM.  
- Capture provenance: `SourceSystem`, `SourceRecordID`, `IngestedAt`.  
- Start with samples; then enable scheduled or event-driven ingestion.

---

## Step 3 — Standardize & Validate Inputs (Pre-Checks)

**Portal**: *Governance → Rules (Data Part Rules)*  
Create normalization rules **before** matching:

- **Names/Text**: trim, case, punctuation, diacritics.  
- **Email**: lower-case; regex; tag `InvalidEmail`.  
- **Phone**: format to **E.164**; tag `InvalidPhone` on parse fail.  
- **Address**: parse components; ISO-2 `Country`; optional geocoding; tag `InvalidAddress`.  
- **IDs**: normalize TaxID/ABN/DUNS (B2B), DOB (B2C) validation.  
- **Consent**: standardize purposes/channels; store source & timestamp.

---

## Step 4 — Identity Resolution (Duplicate Prevention)

**Portal**: *Entity Matching*  

### Person (B2C / Contacts)
- **Blocking**: (Email), (Phone), (LastName + DOB).  
- **Auto-merge**: exact Email or exact Phone.  
- **Candidate**: Fuzzy Name ≥ 0.92 AND Address similarity ≥ 0.9 (same Country) → steward.

### Account (B2B)
- **Blocking**: (Domain), (TaxID), (Country + CleanNameSoundex).  
- **Auto-merge**: exact Domain or exact TaxID.  
- **Candidate**: Fuzzy LegalName ≥ 0.92 + Country guard.

**Linking**
- Link new `Lead`/`Application` to existing Golden `Customer` when a high-confidence match exists—reduces re-keying and speeds onboarding.

---

## Step 5 — Evidence & Risk Checks (KYC/Sanctions/Credit)

**Portal**: *Data Sources (KYC/Risk)* + *Rules*  
- Ingest results from KYC/AML/Sanctions/Credit providers.  
- Normalize statuses to a common schema (`Passed`, `Review`, `Failed`, `Expired`).  
- Rules:
  - If `SanctionsHit=true` → tag `SanctionsHit`, block readiness.  
  - If `KYCStatus=Expired` OR `DocsMissing=true` → tag `KYCRequired`; create **Task**.  
  - If `CreditStatus < threshold` → tag `NeedsStewardReview` or route to manual approval.

---

## Step 6 — Golden Record Survivorship

**Portal**: *Governance → Rules (Golden Record Rules)*  
Define attribute precedence and tie-breakers:

| Attribute        | Precedence (high → low)                      | Tie-breaker                        |
|------------------|-----------------------------------------------|------------------------------------|
| Primary Email    | CRM > Application > Support > Marketing       | Most recently verified              |
| Primary Phone    | CRM > Application > Support                   | Valid E.164 + last confirmed       |
| Address          | Verified delivery > Billing > CRM             | Most recent verified               |
| Account Domain   | CRM > Verified from Email Domain              | Steward override                   |
| Segment/Plan     | Application > CRM                             | Most recent                        |
| Consents         | **Most restrictive wins** per channel         | N/A                                |

**Derived**
- `CompletenessScore` and `ReadinessScore` (see Step 7).  
- `OnboardingStage` (Application → KYC → Contract → Activated).

---

## Step 7 — Readiness Score & Checklist

**Portal**: *Data Quality → Scorecards* or *Rules*  
Compute a **ReadinessScore** and a binary **ReadyToActivate** flag:

.