---
layout: cluedin
title: CluedIn for Data Engineers — Build & Operate Handbook
parent: Knowledge base
permalink: /kb/cluedin-data-engineers
nav_order: 2
---

## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

**Audience:** Data Engineers, Analytics Engineers, MLEs  
**Goal:** Provide a practical, end‑to‑end playbook for building reliable, secure, and observable pipelines in CluedIn—from ingestion through mapping, cleaning, exports, CI/CD, and operations.

> This handbook favors configuration-as-code, small incremental releases, strong observability, and close collaboration with Admins and Stewards.

---

## 0) Your First 48 Hours (Checklist)

**Access & Environment**
- [ ] Sign in via **SSO**; verify **Data Engineer** role permissions.
- [ ] Identify **dev/test/prod** workspaces and which one you own.
- [ ] Configure the **CLI/API** credentials (short‑lived if possible).

**Repos & Config-as-Code**
- [ ] Clone the **platform-config** repo (mappings, policies, projects).
- [ ] Set up a **branching** model (feature → PR → staging → prod).
- [ ] Install pre-commit linters for YAML/JSON schema validations.

**Pipelines**
- [ ] Create **one Ingestion Endpoint** for your first source (stream or scheduled batch).
- [ ] Wire **one Export Target** (table/topic/API) for an end‑to‑end path.
- [ ] Add a **staging export** to test mapping/cleaning changes safely.

**Observability**
- [ ] Pin dashboards for ingestion/export **success, latency, rows**.
- [ ] Learn where to pull **logs** and **audit logs** with `correlation_id`.
- [ ] Set baseline **alerts** (failures, volume anomalies, schema drift).

---

## 1) Role Scope (What You Own)

- **Data ingress** (HTTP/Kafka/webhooks/batch/CDC) and **reliability** (retries, DLQ, replay).
- **Mapping** of sources → CluedIn entities/relationships; schema evolution.
- **Cleaning projects** and **validations** implementation with Stewards.
- **Exports** to warehouses, lakes, topics, APIs; versioning and contracts.
- **Automation** (schedules, webhooks) and **integration** (Power Platform, Purview).
- **Observability** (logs, metrics, tracing), **cost/perf**, and **incident response**.
- **Security** (secrets, tokens, PII handling) in partnership with Admins.

---

## 2) Environments & Config as Code

### 2.1 Workspace Layout
- **dev**: fast iteration, broad logs, feature flags on.
- **test/staging**: PR validation, near‑prod data scale, alerts to engineers.
- **prod**: tight scopes, change windows, alerts to on‑call.

### 2.2 Config Repository
Keep **mappings**, **policies**, **cleaning projects**, and **export configs** in a Git repo:
```
/cluedin/
  mappings/
  cleaning/
  exports/
  policies/
  ai-agents/
  env/
    dev/
    test/
    prod/
```

Use **overlay variables** per env (URIs, secrets references, schedules).

### 2.3 Promotion
- PR → **staging export** diff → approval → **prod**.
- Always include: change summary, risk, rollback, owner, metrics to watch.

---

## 3) Ingestion: Endpoints, Streams, Batches

Prefer **automated** producers; avoid manual uploads after day 1.

### 3.1 HTTP/Webhook (JSON lines)
```bash
curl -X POST \
  -H "Authorization: Bearer $CLUEDIN_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"source":"crm-contacts","payload":{"id":"c_123","email":"a@example.com","updated_at":"2025-08-22T12:00:00Z"}}' \
  https://<YOUR_INGESTION_ENDPOINT>/ingest
```

### 3.2 Kafka / Event Hub (stream)
- Topic per **domain** or **entity**; include **schema version** in headers.
- Enforce **idempotent** producers; include **event_id** and **updated_at**.

### 3.3 Batch (S3/Blob/ADLS)
```json
{
  "name": "s3-sales-orders",
  "type": "s3-bucket-watch",
  "options": {
    "bucket": "acme-prod-orders",
    "prefix": "daily/",
    "file_types": ["json","csv","parquet"],
    "schedule": "cron(0 * * * ? *)"
  }
}
```

### 3.4 CDC (Databases)
- Use Debezium/Log-based CDC to stream **inserts/updates/deletes**.
- Normalize **op** codes upstream; ensure **primary keys** present.

### 3.5 Reliability Patterns
- **Retries** with exponential backoff; cap attempts.
- **DLQ/Quarantine** for poison messages; add a replay tool.
- **Backfills**: separate lane (lower priority), preserve current SLAs.

---

## 4) Mapping: From Raw to Entities

### 4.1 Principles
- Start **minimal**: keys, names, timestamps, core relations.
- Keep heavy standardization in **cleaning projects**, not mapping.
- Make mapping **versioned** and **revertible**.

### 4.2 Example Mapping (pseudo-YAML)
```yaml
entity: Person
source: "crm-contacts"
fields:
  id: $.id
  email: $.email
  first_name: $.first_name
  last_name: $.last_name
  updated_at: $.updated_at
relationships:
  - type: "EMPLOYED_BY"
    to_entity: Organization
    from: $.org_id
    to: $.organization.id
```

### 4.3 Schema Evolution
- **Additive** first (new nullable fields).  
- For breaking changes, create `_v2` mapping and **staging export** to test.

---

## 5) Cleaning Projects & Validations

### 5.1 Cleaning (incremental, idempotent)
```yaml
project: normalize_contacts
schedule: "0 * * * *"  # hourly
steps:
  - name: normalize_email
    action: set
    field: email
    value: lower(trim(email))
  - name: e164_phone
    when: phone is not null
    action: set
    field: phone
    value: to_e164(phone, default_country="US")
```

### 5.2 Validations (guardrails)
```yaml
rule: email_regex
entity: Person
check:
  regex: "^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$"
severity: high
on_fail: { action: "flag" }
```

Work with **Stewards** for rules and thresholds; engineers implement safely.

---

## 6) Exports: Tables, Topics, APIs, Files

### 6.1 Contract & Versioning
Define a **data contract** per export (schema, keys, SLA, semantics).
Bump version on breaking changes (`contacts_v1` → `contacts_v2`).

### 6.2 Example Export Config (pseudo-JSON)
```json
{
  "name": "warehouse-contacts-v1",
  "type": "sql-table",
  "options": {
    "connection": "analytics-warehouse",
    "schema": "mdm",
    "table": "contacts_v1",
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
  "schedule": "0 * * * *"
}
```

### 6.3 Reliability
- **Upserts** require stable primary keys.  
- Add **row count** and **null ratio** checks per run.  
- Emit **correlation_id** to trace in logs.

---

## 7) Orchestration & Triggers

- Use CluedIn **schedules** for simple jobs.  
- For complex DAGs, trigger CluedIn via **webhooks** from Airflow/ADF.  
- Emit success/failure webhooks to **Power Automate** or incident channels.

---

## 8) Testing Strategy

### 8.1 Unit & Transform Tests
- Functions: normalization, parsing, enrichment.
- Golden datasets for edge cases (UTF‑8, nulls, long strings).

### 8.2 Contract Tests
- Validate **input** fields/types/required keys.  
- Validate **export** schema and **SLA** (latency, freshness).

### 8.3 Regression Diffs
- Compare **staging vs prod** exports for row counts, nulls, distribution drift.

### 8.4 CI Example (pseudo-YAML)
```yaml
name: cluedin-ci
on: [pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: pip install -r requirements.txt
      - run: pytest -q
      - run: ./tools/validate-config.sh  # schema check for YAML/JSON
```

---

## 9) Observability: Logs, Metrics, Tracing

### 9.1 What to Log
- Ingestion: status, bytes, parse errors, DLQ counts.  
- Mapping/Cleaning: records touched, rule breaches.  
- Exports: run duration, rows out, schema diffs.

### 9.2 Metrics to Track
- **Freshness/latency** per pipeline stage.  
- **Completeness/validity/duplicates** (with Stewards).  
- **Failure rate** by category.  
- **Cost signals** (records processed, reprocess volume).

### 9.3 Correlation
- Pass a **correlation_id** end‑to‑end; include it in user‑visible errors.

---

## 10) Performance & Cost Tuning

- Choose **columnar formats** for heavy batch (Parquet).  
- **Partition** by time/entity; avoid small files.  
- Tune **batch size** and **parallelism**; monitor backpressure.  
- Cache reference data; avoid N+1 lookups in hot loops.  
- For dedup, start deterministic; schedule fuzzy phases off‑peak.

---

## 11) Reliability Engineering

- **Idempotency**: dedupe by event_id + updated_at.  
- **Retries** with jitter; circuit‑break noisy sources.  
- **DLQ** for poison data; add a replay CLI that tags correlation_id.  
- **Backfills**: run in **read‑only** mode for exports first; promote after QA.  
- **Schema evolution**: additive default; versioned breaking changes.

---

## 12) Security & Compliance (Engineer View)

- Use **least‑privilege** tokens; scope to project/export.  
- Store secrets in a **vault**; never in repo or logs.  
- Respect **labels**: mask PII in staging and during AI prompts.  
- Use **audit logs** to evidence changes; link them in PRs.  
- Coordinate with Admins for **role** and **policy** changes.

---

## 13) AI Agents for Engineers

- Ask Agents to **profile** data, suggest **validations**, and generate **test cases**.  
- Use Agents to propose **mapping diffs** and **survivorship** rules.  
- Restrict to **masked** views when fields carry PII/Restricted labels.  
- Keep auto‑fixes **reversible**; log before/after samples.

---

## 14) Collaboration Model

- **Stewards**: define rules, thresholds, glossary; review DQ impacts.  
- **Admins**: SSO/roles, feature toggles, secrets, policies.  
- **Engineers**: implement, test, ship; own runtime health.

**Change cadence:** small PRs, clear runbooks, explicit rollback steps.

---

## 15) Runbooks (Common Incidents)

**A) Ingestion 4xx/5xx spike**
1. Identify source + correlation_id.  
2. Check auth/quotas; inspect DLQ samples.  
3. Throttle producer or widen batch; hotfix schema parse.  
4. Reprocess DLQ after fix; confirm metrics normal.

**B) Export schema drift**
1. Freeze prod export; route to staging.  
2. Diff mapping since last green; revert or bump `v2`.  
3. Notify consumers; run backfill if required.

**C) Duplicate surge**
1. Raise auto‑approve threshold; pause auto‑merge.  
2. Add deterministic rule; schedule fuzzy off‑peak.  
3. Review precision/recall; promote new rules.

**D) SLA breach (freshness)**
1. Identify slow stage (ingest, clean, export).  
2. Scale parallelism or adjust schedule.  
3. Add alert on pre‑cursor metrics (queue depth).

---

## 16) Templates & Snippets

### 16.1 Export Contract (YAML)
```yaml
name: contacts_v1
primary_key: contact_id
delivery:
  type: sql-table
  schedule: hourly
sla:
  freshness_minutes_p95: 60
schema:
  - name: contact_id
    type: string
    required: true
  - name: email
    type: string
  - name: updated_at
    type: timestamp
labels: ["PII:email"]
```

### 16.2 Policy Hook (mask PII for non-owners)
```yaml
policy: mask_email_for_non_owners
target: entity:Person.field:email
actions: [read]
effect: allow_with_mask
mask: "partial_email"
unless:
  - role_in: ["Data Steward","Administrator"]
```

### 16.3 Makefile Helpers
```makefile
lint:
\t./tools/validate-config.sh

deploy-staging:
\t./tools/apply.sh env/test

deploy-prod:
\t./tools/apply.sh env/prod
```

### 16.4 SQL Smoke Checks
```sql
-- Row count sanity vs yesterday (±10%)
SELECT
  CASE WHEN ABS((today.c - yday.c) / NULLIF(yday.c,0)) <= 0.10 THEN 'OK' ELSE 'ALERT' END AS status
FROM
  (SELECT COUNT(*) c FROM mdm.contacts_v1 WHERE _load_date = CURRENT_DATE) today,
  (SELECT COUNT(*) c FROM mdm.contacts_v1 WHERE _load_date = CURRENT_DATE - INTERVAL '1 day') yday;
```

---

## 17) Operating Rhythm

**Daily**
- Check pipeline **health** + last run metrics (2–5 min).  
- Triage DLQ; scan error logs by category.  
- Review DQ dashboard with Stewards.

**Weekly**
- Ship 1–2 mapping/cleaning improvements.  
- Tighten tests for any incident class seen.  
- Cost/perf review: partitions, parallelism, batch sizes.

**Monthly**
- Access & token review (with Admins).  
- Evaluate dedup thresholds (precision/recall).  
- Retire old export versions (`_v0`) after consumers migrate.

---

## 18) What “Good” Looks Like

- **Green** end‑to‑end runs with alert noise < 1%.  
- **Additive** schema changes dominate; breaking changes are versioned.  
- **DQ metrics** improving quarter‑over‑quarter.  
- **Runbooks** exercised; MTTR trending down.  
- **Config-as-code** with clear history, rollbacks, and audit links.

---

**You now have the Data Engineer blueprint:** land data reliably, map minimally then iterate, clean & validate safely, export with contracts, test and observe everything, and collaborate tightly with Stewards and Admins. Ship small, ship often, and keep the pipeline healthy.

