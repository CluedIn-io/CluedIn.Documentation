---
layout: cluedin
title: CluedIn For Data Stewards
parent: Knowledge base
permalink: /kb/cluedin-for-data-stewards
nav_order: 2
---

# CluedIn for Data Stewards — Field Guide

**Audience:** Data Stewards, Data Quality Leads, Business Owners  
**Goal:** Give stewards a clear, practical playbook for operating CluedIn: profiling, validation, cleaning, dedup review, metadata & glossary, and day‑to‑day rhythms with engineers and admins.

> This is the “how we actually work” guide. It favors repeatable workflows, small changes shipped often, and evidence from metrics and audit trails.

---

## 0) Your First 48 Hours (Checklist)

**Get access & context**
- [ ] Sign in via **SSO**; verify your **Steward** role permissions.  
- [ ] Join the **#data-quality** and **#cluedin-ops** channels (or equivalent).  
- [ ] Open the **Entities Explorer** and **Exports** you own.  
- [ ] Skim the **Runbook** and **Use‑Case Brief** for your domain.

**Profile & label**
- [ ] Run **profiling** on top entities (completeness, validity, uniqueness).  
- [ ] Apply **labels/classifications** (PII, Restricted, Confidential).  
- [ ] Note top 3 issues (e.g., invalid emails, duplicate orgs).

**Set foundations**
- [ ] Draft **validation rules** for the highest‑impact fields.  
- [ ] Create a **Cleaning Project** with 1–2 safe normalizations.  
- [ ] Review **Dedup queue**; define deterministic auto‑approve rules (with Admin/Engineer).

**Observability**
- [ ] Pin **DQ metrics** and set initial thresholds.  
- [ ] Learn where to find **logs** and **audit logs** for your domain.  

---

## 1) What a Steward Does in CluedIn

- **Profiling & Monitoring** — Understand data shapes, trends, outliers.  
- **Validation & Policy** — Encode business rules as validations/policies.  
- **Cleaning** — Build small, idempotent improvements that run on a cadence.  
- **Dedup & Golden Records** — Review matches, define survivorship, and unmerge safely.  
- **Metadata & Glossary** — Maintain definitions, semantics, classifications, and lineage notes.  
- **Governance & Evidence** — Track DQ metrics, create change records, use audit logs.  
- **Collaboration** — Work with Engineers (pipelines/mapping) and Admins (access/roles).

> Principle: **Ship smaller changes more often**. Each step should be low‑risk, easy to revert, and measurable.

---

## 2) Finding and Understanding Your Data

### 2.1 Entities Explorer & Catalog
- Browse **Entities** (e.g., `Person`, `Organization`, `Order`) and their attributes.  
- Check **relationships** (e.g., Person ↔ Organization) and **lineage** from sources to exports.  
- Use **labels** (PII, Restricted) to drive access and masking policies.

### 2.2 Profiling (What to look at)
- **Completeness:** non‑null %, blank %, cardinality.  
- **Validity:** regex/domain compliance (emails, country codes).  
- **Uniqueness:** duplicates by natural/business keys.  
- **Distributions:** skew, min/max, outliers.  
- **Timeliness:** update latency vs SLAs.

**Quick profiling questions**
1. Which 5 fields most impact downstream decisions?  
2. Where are the biggest drops in completeness/validity?  
3. Which sources disagree (consistency check)?

---

## 3) Writing Validations (Guardrails)

### 3.1 Validation Rule Template
```yaml
rule: email_must_be_valid
entity: Person
when:
  - field: email
    is_not_null: true
check:
  regex: "^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$"
severity: high
on_fail:
  action: "flag"          # flag | quarantine | auto_fix
  message: "Invalid email format"
labels: ["PII","contactability"]
```

### 3.2 Cross‑Field Rules
```yaml
rule: order_dates_consistent
entity: Order
check:
  expression: "order_date <= ship_date"
severity: medium
on_fail: { action: "flag", message: "Ship date precedes order date" }
```

### 3.3 Domain Lists & Reference Data
```yaml
rule: country_in_iso3166
entity: Address
check:
  in_list:
    field: country_code
    list: ["US","AU","GB","DE","FR","JP","NZ"]
on_fail: { action: "flag" }
```

**Tips**
- Start **allow‑listing** (valid patterns), avoid complex negative logic.  
- Add **labels** to rules to group them by policy (e.g., `privacy`, `finance`).  
- Prefer **flag or quarantine** first; adopt **auto_fix** only when safe and deterministic.

---

## 4) Cleaning Projects (Small, Safe, Scheduled)

### 4.1 Design Principles
- **Idempotent:** Running twice doesn’t double‑change.  
- **Observable:** Log counts changed, keep before/after examples.  
- **Revertible:** Version the project; easy rollback.  
- **Scoped:** 1–3 steps per release; avoid big‑bang refactors.

### 4.2 Starter Project
```yaml
project: normalize_contacts
schedule: "0 * * * *"  # hourly
steps:
  - name: trim_names
    action: set
    field: first_name
    value: trim(first_name)
  - name: normalize_email
    action: set
    field: email
    value: lower(trim(email))
  - name: drop_impossible_birthdates
    when: "birthdate < '1900-01-01' or birthdate > now()"
    action: set
    field: birthdate
    value: null
observability:
  sample_before_after: 25
  emit_metrics: true
```

### 4.3 Approval & Promotion
- Test in **staging** export. Compare row counts, nulls, and schema.  
- Peer review from another Steward/Engineer.  
- Promote with a short **changelog** entry and link to metrics.

---

## 5) Deduplication & Golden Records

### 5.1 Review Workflow
1. Open **Dedup queue** for your entity (e.g., `Person`).  
2. Start with **high‑confidence** candidates; verify examples.  
3. **Approve** merges that are deterministic; send ambiguous ones to **manual review** with notes.  
4. If needed, **unmerge** with documented rationale.

### 5.2 Deterministic First, then Fuzzy
```yaml
rules:
  - name: exact_email
    when: lower(email) == lower(other.email)
    confidence: 0.98
  - name: phone_e164
    when: e164(phone) == e164(other.phone)
    confidence: 0.95
auto_approve_threshold: 0.97
queue_threshold: 0.85
```

### 5.3 Survivorship (Golden Record)
Define how fields are chosen on merge:
```yaml
survivorship:
  precedence:
    - source: "crm"
    - source: "support"
    - source: "marketing"
  recency_win: true     # prefer latest updated_at when sources tie
  field_overrides:
    email: "most_recent_non_null"
    phone: "most_trusted_source_first"
```
- Maintain a **decision log** for merges/unmerges.  
- Update **dedup rules** after recurring manual decisions to reduce future toil.

---

## 6) Mapping & Schema with a Steward’s Lens

- Propose new fields/semantics based on business needs.  
- Keep **business definitions** (glossary) aligned with mapped fields.  
- Avoid heavy transformation in mapping; use **Cleaning Projects** for standardization.  
- When adding fields, coordinate with Engineers to run **staging exports** and **diff** results.

**Change Checklist**
- [ ] Impacted dashboards identified  
- [ ] Export contracts updated (if needed)  
- [ ] Backfill plan (if required)  
- [ ] Rollback tested

---

## 7) Metadata, Glossary & Classifications

### 7.1 Glossary Entries
Include: business definition, calculation notes, owner, example, data quality caveats.
```yaml
term: "Active Customer"
definition: "Customer with at least one completed order in the last 90 days"
owner: "Sales Ops"
sources: ["orders_v1","subscriptions_v2"]
dq_notes: "Relies on order status != 'cancelled'"
```

### 7.2 Classifications & Policy Hooks
- Tag fields/entities with `PII`, `Restricted`, `Confidential`, or `Public`.  
- Policies can **mask**, **hash**, or **deny** reads based on labels.  
- Steward task: keep labels accurate as new fields arrive.

---

## 8) Data Quality Metrics & Dashboards

Track **few, meaningful** KPIs per entity:
- **Completeness**: `pct_non_null(email)`  
- **Validity**: `pct_match(email, regex)`  
- **Uniqueness**: `1 - duplicate_rate(email)`  
- **Timeliness**: `p95(now() - updated_at)`

**Thresholds**
```yaml
metrics:
  email_validity: { warn: ">= 0.97", fail: "< 0.95" }
  duplicate_rate_email: { warn: "<= 0.03", fail: "> 0.05" }
alerts:
  - metric: email_validity
    action: "notify #data-quality"
```
**Habit:** Improve by **small, frequent** increments (e.g., +0.5–1.0% per week).

---

## 9) Reading Logs & Audit Logs (Steward View)

### 9.1 Operational Logs
- **Cleaning logs** for before/after counts, failures.  
- **Validation logs** for rule breaches and quarantines.  
- **Export logs** for schema diffs and row counts.

**Grab the correlation_id** from UI errors and filter logs by it when triaging.

### 9.2 Audit Logs
- Who approved a merge? Who changed a rule? When was a policy updated?  
- Use audit logs to **evidence** changes and for **post‑incident** analysis.  
- Include audit links in your **changelog** notes.

---

## 10) Working with AI Agents (Your Co‑pilot)

### 10.1 Analysis Prompt Starters
> “Analyze **Person** for missingness, invalid formats, and duplicates. Propose validation rules with example failing records. Suggest deterministic dedup keys first.”

> “Given recent invalid email spikes, propose a stricter validation with back‑compat and estimate false positive rate.”

### 10.2 Safe Auto‑Fix Patterns
- Normalize casing/whitespace.  
- Standardize ISO codes (countries, states).  
- Convert phone numbers to **E.164** (with default country).  

**Guardrails**
- Keep auto‑fixes **reversible**; log original values.  
- Restrict AI write scope to **masked views** where needed.

---

## 11) Collaboration & Change Management

- Submit **PRs** or change requests for new validations/cleaning steps.  
- Pair with Engineers for mapping/export impacts.  
- Ask Admins for **labels/policy updates** and **role changes**.  
- Document **user impact** and **rollback** in each change.

**Promotion flow**
1. Draft in staging → 2. Peer review → 3. Scheduled deploy → 4. Post‑deploy checks → 5. Changelog & metric snapshot.

---

## 12) Day‑to‑Day Operating Rhythm

**Daily (5–10 minutes)**
- DQ dashboard glance; triage new alerts.  
- Dedup queue: approve high‑confidence; flag edge cases.  
- Check last cleaning run; scan error logs.

**Weekly**
- Ship 1–3 cleaning improvements.  
- Review validation breach trends; tighten where safe.  
- Update glossary entries if semantics changed.

**Monthly**
- Access review for your domain (with Admins).  
- Revisit dedup thresholds; sample precision/recall.  
- Retire deprecated fields/exports.

---

## 13) Steward Runbook (Common Situations)

**Spike in invalid emails**
1. Confirm via validation logs and sample records.  
2. Identify source; check recent mapping/cleaning changes.  
3. Add temporary **quarantine** rule; propose stricter regex.  
4. Communicate downstream impact; backfill if needed.

**Duplicate surge after new source onboarded**
1. Lower auto‑approve threshold; pause auto‑merge.  
2. Add deterministic rule (e.g., exact phone or customer_id).  
3. Review queue; update survivorship precedence with the new source.

**Export schema drift detected**
1. Compare staging vs prod exports; find mapping change.  
2. Coordinate rollback with Engineer; file a changelog entry.  
3. Add a validation to catch the offending pattern next time.

---

## 14) Templates & Snippets

### 14.1 Validation Pack (copy/paste)
```yaml
- rule: phone_is_e164_or_null
  entity: Person
  when: [{ field: phone, is_not_null: true }]
  check: { regex: "^\\+\\d{8,15}$" }
  severity: medium
  on_fail: { action: "flag" }

- rule: name_min_length
  entity: Person
  check: { expression: "len(trim(first_name)) >= 1 and len(trim(last_name)) >= 1" }
  severity: low
  on_fail: { action: "flag" }
```

### 14.2 Cleaning Steps
```yaml
- name: fix_common_email_typos
  action: set
  field: email
  value: replace_multi(lower(email), {"gmal.com":"gmail.com","hotnail.com":"hotmail.com"})
```

### 14.3 Dedup Reviewer Notes (template)
```yaml
pair_id: "dup_7f3a"
decision: "approve"
evidence:
  - "exact_email"
  - "matching phone_e164"
comment: "Same person from CRM and Support; safe to auto‑approve rule next time."
```

### 14.4 Changelog Entry
```yaml
date: "2025-08-24"
change: "Added phone E.164 normalization; tightened email regex"
impact: "Duplicate rate down from 5.2% → 2.1%; validity up 96.8% → 98.9%"
links: ["run logs", "audit event #1432"]
```

---

## 15) What Good Looks Like

- **DQ metrics trending up**, no long‑lived red alerts.  
- **Small, frequent** improvements with audit evidence.  
- **Glossary & labels** kept up to date.  
- **Dedup queue** under control; high precision merges; rare unmerges.  
- **Change notes** clear enough that a new Steward can follow the story.

---

## Appendix — Steward Permission Profile (Typical)

| Capability | Viewer | Steward | Engineer | Admin |
|---|---:|---:|---:|---:|
| Read entities/exports | ✅ | ✅ | ✅ | ✅ |
| Edit validations | ❌ | ✅ | ✅ | ✅ |
| Edit cleaning projects | ❌ | ✅ | ✅ | ✅ |
| Review dedup & approve merges | ❌ | ✅ | ✅ | ✅ |
| Configure ingestion/export | ❌ | ❌ | ✅ | ✅ |
| Manage roles/policies | ❌ | ❌ | ❌ | ✅ |
| Toggle features | ❌ | ❌ | ❌ | ✅ |

> If you need elevated access temporarily, request a **time‑boxed** role with Admin approval.

---

**You now have the Steward playbook:** profile, validate, clean, dedup, document, measure—then repeat. Keep changes small, keep evidence, and keep the pipeline healthy.

