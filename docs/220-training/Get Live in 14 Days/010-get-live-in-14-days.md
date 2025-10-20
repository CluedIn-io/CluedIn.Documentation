---
layout: cluedin
title: Go live in 14 days with CluedIn — step‑by‑step playbook
parent: Knowledge base
permalink: /kb/14-days-live
nav_order: 2
---
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

**Audience:** Data engineers, analytics engineers, solutions architects  
**Goal:** Get a working, production‑minded slice of your use case live in **14 days**—with real data flowing **in** via **Ingestion Endpoints** and **out** via **Export Targets**, while building the habits that make CluedIn successful over time.

---

## Why this works

This plan embraces **ELT** and **iteration**:
- **Push data as‑is** (raw) into CluedIn. Don’t pre‑clean. Let CluedIn’s schema inference, lineage, mapping, and cleaning projects do the heavy lifting.
- **Start small** (one incoming asset), **ship data out** early, and **improve** mapping and quality as you learn.
- **Automate ingestion** (streaming or scheduled batches) so you never have to re‑upload files manually.
- **Lean on AI Agents** to spot quality issues, suggest validations, and surface duplicates.
- **Measure progress** with data quality metrics. Improve frequently in small increments.
- **Practice mapping changes**: try, test, revert. Lower the cost of change.

---

## 14‑Day Overview (at a glance)

| Day | Theme | Outcome |
|---:|---|---|
| 1 | Business slice & target destinations | A crisp “thin slice” of the use case and where data will be exported |
| 2 | Ingestion Endpoints (stream/batch) | Endpoints created for one **single** source |
| 3 | First raw data in | One asset flowing into CluedIn “as‑is” |
| 4 | Minimal mapping v0 | Just enough mapping to recognize entities and relationships |
| 5 | Export Targets v0 | First export wired to BI / ops surface |
| 6 | End‑to‑end smoke test | Data reliably moving **in → out** on a schedule |
| 7 | Retrospective & plan | Add tasks for Week 2 improvements |
| 8 | AI Agents for QA | Findings list: missingness, invalids, duplicates |
| 9 | Cleaning projects | First incremental fixes running on a cadence |
| 10 | Data quality metrics | Baselines + alerts; choose KPIs and thresholds |
| 11 | Iterative mapping | Practice change/test/rollback; improve coverage |
| 12 | Dedup projects | Deterministic rules + auto‑approve high‑confidence |
| 13 | Second asset | Expand model; regression check exports |
| 14 | Go‑live checklist | Runbook, ownership, on‑call and next 30/60/90 |

> **Scope guardrails:** One source → one export in week 1. In week 2, add fixes, dedup, and one more source. That’s enough to go live credibly and safely.

---

## Prerequisites

- CluedIn workspace access and a service account (API key) with **Ingestion** and **Export** permissions.
- A target **Export** destination (e.g., data warehouse table, analytics lake, CRM, reverse‑ETL).  
- One **initial source** you can stream or batch on a schedule (e.g., Kafka topic, webhook producer, S3/Blob folder, database CDC).  
- A lightweight success metric (e.g., “Daily pipeline success + record count within ±5%”, “<2% invalid emails”, “<1% duplicates”).

---

## Core principles you’ll follow

1. **Push to CluedIn via Ingestion Endpoints.** Prefer **live streams** (Kafka/webhooks) or **automated batches** (S3/Blob schedulers). Avoid manual uploads after day 1.
2. **Drop data “as‑is.”** Don’t pre‑clean or reshape. CluedIn is **ELT**: land first, then transform/clean in place.
3. **Don’t perfect mapping up front.** Get **data in and out** first. Iteratively refine mapping as you learn.
4. **Start small—one asset.** Don’t model the world. Bring data in, then let requirements inform the model.
5. **Lean on AI Agents.** Use them to find issues, propose validations, and surface duplicate candidates.
6. **Cleaning projects > one‑off fixes.** Ship frequent, small improvements on a schedule.
7. **Measure constantly.** Set DQ baselines now; raise the bar gradually.
8. **Make mapping change cheap.** Practice modify → test → revert. Embrace versioning.
9. **Deduplicate safely.** Start deterministic; auto‑approve only high‑confidence matches.

---

## Day‑by‑Day Guide

### Day 1 — Define the thin slice and “data out” first
**Objectives**
- Pick **one concrete question** you want to answer or workflow to power.
- Define the **Export Target** and format: table, topic, API, or file layout.
- Identify **one source** (asset) that supports the outcome, even if imperfect.

**Artifacts**
- **Use‑case brief** (1 page): purpose, users, downstream surface, SLAs.
- **Data contract (minimal)** for the export: the final fields and semantics.
- **Runbook skeleton** (who owns what, escalation, observability).

**Tip:** If the export is a table, decide **primary key**, **update strategy** (upsert vs. append), and **schema evolution** policy now.

---

### Day 2 — Create Ingestion Endpoints (stream or batch)
**Objectives**
- Create an **Ingestion Endpoint** for **one** asset, using a streaming or scheduled path:
  - **Streaming:** Kafka topic / webhook that produces JSON lines
  - **Batch:** S3/Blob folder with daily/hourly drops (CSV/JSON/Parquet)

**Example: HTTP ingestion (webhook)**
```bash
curl -X POST \
  -H "Authorization: Bearer <CLUEDIN_API_KEY>" \
  -H "Content-Type: application/json" \
  -d '{"source":"crm-contacts","payload":{"id":"c_123","email":"a@example.com","first_name":"Ada","last_name":"Lovelace","updated_at":"2025-08-22T12:00:00Z"}}' \
  https://<YOUR_INGESTION_ENDPOINT_URL>/ingest
```

**Example: S3/Blob batch registration (pseudo‑JSON)**
```json
{
  "name": "s3-sales-orders",
  "type": "s3-bucket-watch",
  "options": {
    "bucket": "acme-prod-orders",
    "prefix": "daily/",
    "file_types": ["json","csv","parquet"],
    "schedule": "cron(0 * * * ? *)"  // hourly
  }
}
```

**Checklist**
- [ ] Endpoint created for a single asset
- [ ] Producer (or object drop) automated
- [ ] Authentication/authorization confirmed
- [ ] Observability: ingestion success counter + dead‑letter path

> **Rule:** From here on, **no manual uploads**. Everything arrives via the endpoint.

---

### Day 3 — Land the first raw data “as‑is”
**Objectives**
- Send a **small but real** sample through the endpoint.
- Verify CluedIn can **parse** and **persist** the records.
- Capture **lineage** and **metadata** (source system, timestamps, version).

**Validation**
- [ ] Ingestion dashboard shows new records
- [ ] Sample record previewed (raw fields visible)
- [ ] **No pre‑cleaning** done upstream

**Anti‑pattern:** Don’t pause to cleanse/massage data **before** landing it. That’s what cleaning projects are for later this week.

---

### Day 4 — Minimal mapping v0 (don’t perfect it)
**Objectives**
- Create just‑enough **entity mapping** to recognize core entities (e.g., `Person`, `Organization`, `Order`) and a few relationships.
- Avoid exotic field logic; capture **IDs**, **names**, **keys**, **timestamps**.

**Tactics**
- Start with 5–10 high‑value fields only.
- Mark known **primary keys** and **foreign keys**.
- Add a **default namespace** for unmapped attributes.

**Success looks like**
- [ ] Records appear as proper entities
- [ ] Core joins/relationships visible
- [ ] No blocking errors preventing export

> **Remember:** You will change this mapping many times. That’s normal.

---

### Day 5 — Wire up Export Targets v0
**Objectives**
- Create the **first export** to your chosen destination (warehouse table, topic, API, file). Aim for a stable daily/hourly schedule.

**Example: table export config (pseudo‑JSON)**
```json
{
  "name": "warehouse-contacts-v0",
  "type": "sql-table",
  "options": {
    "connection": "analytics-warehouse",
    "schema": "mdm",
    "table": "contacts_v0",
    "mode": "upsert",
    "primary_key": ["contact_id"]
  },
  "mapping": {
    "contact_id": "Person.id",
    "email": "Person.email",
    "first_name": "Person.first_name",
    "last_name": "Person.last_name",
    "updated_at": "Person.updated_at"
  },
  "schedule": "0 * * * *"  // hourly
}
```

**Validation**
- [ ] Export task succeeds end‑to‑end
- [ ] Downstream surface can query/use the output
- [ ] Row counts within expected bounds

---

### Day 6 — End‑to‑end smoke test on a schedule
**Objectives**
- Run the pipeline **in → through → out** a few times on an **automatic schedule**.
- Add alerts for **failures** and **volume anomalies** (±X% vs baseline).

**Checklist**
- [ ] End‑to‑end schedule in place
- [ ] Alerting/notifications configured
- [ ] Runbook updated with failure modes and triage steps

---

### Day 7 — Retrospective & Week‑2 plan
**Discuss (30–45 min)**
- What slowed us down?
- What parts of mapping are confusing downstream?
- Which fields are most error‑prone?
- What small fixes would materially improve trust?

**Plan**
- Pick **3–5 fixes** for Week 2 (AI Agents, cleaning, metrics, dedup).
- Nominate owners and define “done” for each.

---

### Day 8 — Use AI Agents to analyze data quality
**Objectives**
- Run AI Agents to **scan** entities for:
  - Missingness, invalid formats, out‑of‑range values
  - Suggested **validations** (e.g., regex, domain lists, referential checks)
  - Duplicate candidates (e.g., person/org dedup)

**Workflow**
1. Run an analysis prompt or playbook against your entity set.
2. Review the **findings list** with counts and examples.
3. Accept or tailor proposed **validation rules** and **dedup hints**.
4. Open issues/tasks directly from findings.

**Deliverables**
- [ ] Findings doc with top 5 issues
- [ ] Proposed validation rules drafted
- [ ] Candidate dedup keys identified

---

### Day 9 — Create cleaning projects (incremental fixes)
**Objectives**
- Build **cleaning projects** that remediate the top issues. Examples:
  - Standardize phone/email formats
  - Trim/normalize names
  - Resolve country/state codes
  - Impute defaults (only where safe)
  - Enforce referential integrity

**Practices**
- Small, **re-runnable** steps
- **Idempotent** logic (safe to run multiple times)
- **Versioned** transformations; review & rollback friendly
- **Scheduled** execution (hourly/daily)

**Success**
- [ ] Cleaning pipeline runs on a cadence
- [ ] Changes land back in CluedIn entities
- [ ] No breaking changes to the export schema

---

### Day 10 — Establish data quality metrics & alerts
**Objectives**
- Define and baseline **key metrics** for your use case:
  - **Completeness** (non‑null %, required fields)
  - **Validity** (regex/domain compliance)
  - **Uniqueness** (duplicate rate)
  - **Consistency** (cross‑field rules)
  - **Timeliness** (SLA latency from source → export)

**Actions**
- Capture baselines per entity/table.
- Configure **thresholds** and alerts.
- Add a dashboard panel to your downstream surface.

**Rule of thumb**
- Improve by **small increments** frequently (e.g., +0.5–1.0% per day).

---

### Day 11 — Iterate on mapping (practice change/revert)
**Objectives**
- Evolve mapping to add fields demanded by downstream users.
- **Practice** safe change:
  1. Branch/version your mapping
  2. Apply change to a staging export
  3. Compare outputs (row count, nulls, schema drift)
  4. Promote or revert

**Checklist**
- [ ] Version history for mapping changes
- [ ] Staging export used for trials
- [ ] Rollback tested at least once

---

### Day 12 — Set up deduplication projects
**Objectives**
- Create **dedup** projects for key entities (Person/Organization) with a **deterministic first pass**.
- **Auto‑approve** only **high‑confidence** matches; queue the rest for review.

**Example deterministic rules (pseudo)**
```yaml
rules:
  - name: exact_email
    when: lower(email) matches lower(other.email)
    confidence: 0.98
  - name: phone_e164
    when: e164(phone) == e164(other.phone)
    confidence: 0.95
  - name: org_name_address
    when: norm(name)==norm(other.name) and norm(addr)==norm(other.addr)
    confidence: 0.92
auto_approve_threshold: 0.97
queue_threshold: 0.85
```

**Success**
- [ ] High‑confidence duplicates auto‑merged or flagged for auto‑action
- [ ] Reviewer queue created for the “gray area”
- [ ] Export logic updated to respect master records

---

### Day 13 — Add a second asset, adapt the model
**Objectives**
- Onboard the **second** source that enriches the same entities or introduces a related one.
- Validate that mapping, cleaning, and dedup logic still holds.

**Regression checks**
- [ ] Row counts within expected bounds
- [ ] DQ metrics didn’t regress
- [ ] Export schema unchanged (or managed evolution with version bump)

---

### Day 14 — Go‑live checklist & handover
**Go‑live gates**
- [ ] End‑to‑end schedule stable for 3 consecutive runs
- [ ] Alerts firing to the right channel with owners
- [ ] DQ metrics tracked and improving
- [ ] Dedup auto‑approve threshold validated
- [ ] Runbook complete (how to pause/retry/backfill; RTO/RPO notes)
- [ ] Ownership clear: source, mapping, cleaning, export

**Handover packet**
- Use‑case brief, data contract, runbook, dashboard link, “what changed” log, next 30/60/90 roadmap.

---

## How‑To Details & Templates

### A. Minimal export data contract (template)
```yaml
name: contacts_v0
primary_key: contact_id
delivery:
  type: sql-table
  schedule: hourly
fields:
  - name: contact_id
    type: string
    semantics: stable synthetic id from source
    required: true
  - name: email
    type: string
    constraints:
      - regex: "^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$"
  - name: first_name
    type: string
  - name: last_name
    type: string
  - name: updated_at
    type: timestamp
    semantics: last update from any contributing source
```

### B. AI Agent prompt starter
> “Analyze the **Person** entity for missingness, invalid formats, and duplicates. Suggest concrete validation rules with examples and propose deterministic dedup keys. Prioritize fixes that unlock downstream usage of the **contacts_v0** export.”

### C. Cleaning project sketch
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
  - name: e164_phone
    when: phone is not null
    action: set
    field: phone
    value: to_e164(phone, default_country="US")
  - name: drop_impossible_dates
    when: birthdate < "1900-01-01" or birthdate > now()
    action: set
    field: birthdate
    value: null
```

### D. Data quality metric tracker (example)
```yaml
entity: Person
metrics:
  completeness:
    email_non_null: pct_non_null(email)
    name_non_null: pct_non_null(first_name) & pct_non_null(last_name)
  validity:
    email_regex_ok: pct_match(email, "^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$")
  uniqueness:
    email_unique: 1 - duplicate_rate(email)
  timeliness:
    export_latency_minutes: p95(now() - updated_at)
alerts:
  - metric: email_regex_ok
    threshold: ">= 0.98"
    action: "notify #data-quality"
```

### E. Mapping iteration checklist
- [ ] Create mapping branch/version
- [ ] Add 1–3 fields only
- [ ] Run staging export & compare
- [ ] Roll forward or revert
- [ ] Update runbook & data contract

### F. Dedup reviewer guide
- Approve only when you’d be comfortable auto‑approving next time.
- Leave notes; encode your decision as a **new rule** where possible.
- Track **precision** (false merge rate) and **recall** (missed dupes).

---

## Troubleshooting

**Ingestion fails intermittently**  
- Check auth tokens, rate limits, and payload size.  
- Use a dead‑letter queue/folder and replay tool.

**Mapping produces nulls**  
- Verify source field names and paths (case/array/indexing).  
- Add defaults in cleaning; avoid lossy transforms early.

**Export breaks schema**  
- Switch to staging target and diff schemas.  
- Use versioned exports (`_v1`, `_v2`) and deprecate gracefully.

**Duplicate cascades**  
- Tighten deterministic rules and raise auto‑approve threshold.  
- Add secondary keys (email+phone, name+DOB, org name+address).

---

## Operating Rhythm (after go‑live)

- **Daily:** Pipeline run checks + key DQ metrics glance (2 mins).  
- **Weekly:** Review AI Agent findings; ship 2–3 cleaning tweaks.  
- **Bi‑weekly:** Add/adjust a mapping field; test rollback.  
- **Monthly:** Revisit dedup thresholds; expand export consumers.

---

## Summary

In two weeks you can have a resilient, automated **in→through→out** slice in CluedIn, built on repeatable habits:
- **Automated ingestion** (no manual uploads)
- **As‑is landing** (ELT)
- **Exports first**, mapping evolves with needs
- **AI‑assisted** quality and dedup
- **Incremental cleaning projects**
- **Metrics‑driven** improvement
- **Cheap mapping changes** you can revert anytime

Ship small, ship often—and keep the pipeline warm.
