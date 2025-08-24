---
layout: cluedin
title: CluedIn for System Integrators
parent: Knowledge base
permalink: /kb/cluedin-system-integrators
nav_order: 2
---

# CluedIn for System Integrators — Integration Cookbook

**Audience:** System Integrators, Professional Services, SI practice leads  
**Goal:** Provide proven patterns, templates, and guardrails for integrating **CluedIn** with the wider ecosystem: **Data Lakes**, **Data Engineering tools**, **Data Governance tools**, **Power Platform & AI stacks (Power Automate, Power Apps, Copilot, Azure AI Foundry, OpenAI, Claude, Ollama)**, and **Dataverse**.

> Principles: **ELT-first**, **event-friendly**, **contracts & policies as code**, **least privilege**, and **observability by default**.

---

## 0) Engagement Blueprint (First Week)

- **Day 1–2:** Confirm SSO/roles, network allowlists, non-prod workspace, export destinations.  
- **Day 3–4:** Stand up one **Ingestion Endpoint** (stream or batch) + one **Export Target** (table or file).  
- **Day 5:** Wire **catalog scan/lineage**, **alerts**, and a demo to Power BI/Apps.  
- **Deliverables:** Diagrams (L0/L1), export contract, policy/masking file, runbook, and CI pipeline.

---

## 1) Patterns Overview

| Integration Area | Primary Pattern | Protocols | Artifacts to Deliver |
|---|---|---|---|
| Data Lakes | Export Parquet/Delta, partitioned | S3/ADLS/GCS | Export config, partition spec, retention policy |
| Data Engineering | Orchestrate deploy/run/monitor | Airflow/ADF/Fabric/Glue | DAG/pipeline JSON/YAML, webhook triggers, CI |
| Data Governance | Catalog scan + lineage push | Purview/Collibra/Atlas | Scan config, lineage job, label mapping |
| Power Platform & AI | Event in/out, API calls, guarded prompts | HTTP/Kafka/Webhooks/OAuth | Flow/App sketches, HMAC verify, AI guardrails |
| Dataverse | Delta → CluedIn, exports back to tables | Dataverse APIs, Power Automate | Connector flows, backfill scripts, SLA docs |

---

## 2) Data Lakes (ADLS / S3 / GCS)

### 2.1 Export Shapes
- **Columnar files**: Parquet (preferred), optional Delta/iceberg in your lake.  
- **Partitioning**: by `load_date` or business date (e.g., `event_date=YYYY-MM-DD`).  
- **Layout**: `s3://bucket/mdm/customers_wide_v1/event_date=2025-08-24/part-000.parquet`

### 2.2 Export Config (pseudo-JSON)
```json
{
  "name": "customers_wide_v1",
  "type": "file-parquet",
  "options": {
    "connection": "s3://company-analytics",
    "path": "mdm/customers_wide_v1/",
    "partition_by": ["event_date"],
    "compression": "snappy",
    "overwrite": false
  },
  "schedule": "0 * * * *"
}
```

### 2.3 Lake Guardrails
- **Small files kill performance**: use 128–512MB target file sizes.  
- **Schema evolution**: additive by default; break → new `_vN` path.  
- **Retention**: lifecycle policies in S3/ADLS; document RPO/RTO.

---

## 3) Data Engineering Tools

### 3.1 Airflow DAG (sketch)
```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import requests, os

def trigger_export(**ctx):
    r = requests.post(
        f"{os.environ['CLUE_HOST']}/api/exports/run",
        json={"name":"customers_wide_v1"},
        headers={
            "Authorization": f"Bearer {os.environ['CLUE_TOKEN']}",
            "X-Correlation-Id": ctx['run_id']
        }, timeout=30)
    r.raise_for_status()

with DAG("cluedin_customers_export", start_date=datetime(2025,8,1), schedule="@hourly", catchup=False) as dag:
    run = PythonOperator(task_id="run_export", python_callable=trigger_export)
```

### 3.2 Azure Data Factory / Fabric Data Pipelines
- Use **Web** activity to **POST** to CluedIn (ingest/export).  
- Handle **retry with exponential backoff**; bubble up non-2xx.  
- Emit **correlation_id** from pipeline run ID.

**ADF Web activity body (example)**
```json
{ "name": "warehouse-contacts-v1" }
```

### 3.3 AWS Glue / GCP
- Use **Job** step to call CluedIn APIs or read CluedIn exports.  
- Favor **Parquet** reads; push metrics back to CloudWatch/Stackdriver.

### 3.4 dbt / Semantic Layers
- dbt models consume CluedIn exports; keep **contracts** aligned.  
- Avoid heavy transformations in CluedIn mapping when dbt is authoritative downstream.

---

## 4) Data Governance Tools

### 4.1 Purview / Collibra Catalog Scans
- Register warehouse/lake connections where CluedIn writes.  
- Schedule **hourly/daily** scans; tag datasets with owners and classifications.

### 4.2 Lineage (Atlas-style)
```json
POST https://<purview>/api/atlas/v2/lineage
{
  "process": { "typeName": "cluedin_export", "attributes": {
    "name":"customers_wide_v1","qualifiedName":"cluedin.export.customers_wide_v1"} },
  "inputs": [{"qualifiedName":"cluedin.entity.Person"}],
  "outputs": [{"qualifiedName":"s3://company-analytics/mdm/customers_wide_v1"}]
}
```

### 4.3 Classification Sync
- Map CluedIn labels (`PII`, `Restricted`) to catalog **classifications**.  
- Drive **masking** policies consistently in BI and lake security layers.

---

## 5) Power Platform & AI Stacks

### 5.1 Power Automate (Flow) → CluedIn Ingestion
- Trigger: *When a row is added in Dataverse* (or any connector).  
- Action: **HTTP POST** to CluedIn `/api/ingest` with OAuth token.

**Flow HTTP action body**
```json
{
  "source": "dataverse-contacts",
  "payload": {
    "id": "@{triggerBody()?['contactid']}",
    "email": "@{triggerBody()?['emailaddress1']}",
    "updated_at": "@{utcNow()}"
  }
}
```

### 5.2 CluedIn Webhook → Flow / Teams
- Register `export.succeeded` webhook → verify **HMAC** → post to Teams.

**Node verify sketch**
```js
const crypto = require("crypto");
function verify(sig, raw, secret){
  const h = crypto.createHmac("sha256", secret).update(raw).digest("hex");
  return crypto.timingSafeEqual(Buffer.from(sig,"hex"), Buffer.from(h,"hex"));
}
```

### 5.3 Power Apps
- Stewarding app over CluedIn APIs (dedup review, fix invalids).  
- Use service principal; enforce **role checks** server-side.

### 5.4 Copilot (Power Platform)
- Feed **versioned exports** with clear semantics.  
- Mask PII for prompts; restrict to **masked views** for exploratory agents.

### 5.5 Azure AI Foundry / OpenAI / Claude / Ollama
**Pattern: AI Agents with Guardrails**
- **Read scope**: masked datasets or sample subsets.  
- **Modes**: `analysis` and `suggest`; **no auto_fix** until reviewed.  
- **Prompt logging**: store prompt/response IDs with **correlation_id**.  
- **PII/Secrets**: redact before sending to APIs; keep model configs in code.

**Example: calling an AI analysis job (pseudo)**
```json
POST /api/ai/agents/run
{
  "agent": "dq-analyzer",
  "target": { "entity": "Person" },
  "mode": "analysis",
  "options": { "sample": 5000 }
}
```

**Local inference (Ollama)**
- Use Ollama for in‑VPC/in‑laptop development; treat it like any external AI: masked data only and clear retention policy.

---

## 6) Dataverse Integration

### 6.1 Inbound (to CluedIn)
- **Dataverse → Flow → CluedIn** via HTTP ingestion for deltas.  
- For backfills, use **Dataverse Web API** paging and push batches to CluedIn.  
- Emit **idempotency key** (`id + updated_at`) and **correlation_id**.

### 6.2 Outbound (to Dataverse)
- Consume CluedIn export (wide table) and **Upsert** to Dataverse entity via Web API.  
- Respect concurrency (If‑Match ETag) and **retry** on 429s.

**Dataverse upsert (HTTP)**
```http
PATCH https://<org>.crm.dynamics.com/api/data/v9.2/contacts(<guid>)
If-Match: *
Content-Type: application/json

{ "emailaddress1": "a@example.com", "firstname": "Ada", "lastname": "Lovelace" }
```

### 6.3 Identity & Ownership
- Align **Person/Account** keys with Dataverse GUIDs or keep a **link table** in the export.  
- Document **survivorship** rules in the runbook for conflicts.

---

## 7) Security & Compliance Playbook

- **SSO-only** with OIDC/SAML; group‑based roles mapped to least privilege.  
- **Tokens**: short-lived; rotate ≤ 90 days; store in a vault; audit usage.  
- **Policies**: column masking (PII), row filters (region/tenant), export promotion approvals for sensitive labels.  
- **Webhooks**: HMAC signatures; allowlist source IPs; idempotent handlers.  
- **AI**: masked datasets by default; prompt logging; model registry with owner/purpose.  
- **Audit**: retain logs for 1–7 years; include SSO, role changes, tokens, policy updates, merges, and export promotions.

---

## 8) Observability & SLAs

- **Metrics**: ingestion success, DLQ size, export rows/latency, DQ KPIs (validity, completeness, duplicates), webhook retries.  
- **Dashboards**: per domain/export; include top error classes and freshness.  
- **Alerts**: export failure, schema drift, DQ breach, 429 storms, unusual token usage.  
- **Runbooks**: incident steps—contain, diagnose, rollback, backfill—with **correlation_id** examples.

---

## 9) CI/CD & Config-as-Code

- Keep **mappings**, **cleaning**, **validations**, **policies**, and **exports** in Git.  
- Pipeline: PR → **staging export diff** → approval → prod deploy.  
- Validate with schema/domain/FK tests and export contract checks; publish **release notes**.

**GitHub Actions sketch**
```yaml
name: cluedin-deploy
on: [pull_request, push]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: ./tools/validate-config.sh
  deploy-staging:
    if: github.ref == 'refs/heads/main'
    steps:
      - run: ./tools/apply.sh env/test
  deploy-prod:
    needs: deploy-staging
    steps:
      - run: ./tools/apply.sh env/prod
```

---

## 10) Ready-to-Use Templates

### 10.1 Export Contract (with governance)
```yaml
name: customers_wide_v1
owner: "Sales Ops"
primary_key: customer_id
delivery: { type: file-parquet, schedule: hourly }
sla: { freshness_p95_minutes: 60 }
labels: ["PII:email"]
compatibility: additive_only
lineage_required: true
approval_required_when_labels: ["PII","Restricted"]
```

### 10.2 Policy: Mask Email for Non-Owners
```yaml
policy: mask_email_default
target: entity:Person.field:email
actions: [read]
effect: allow_with_mask
mask: "partial_email"
unless: [{ role_in: ["Data Steward","Administrator"] }]
```

### 10.3 Webhook Registration
```json
POST /api/webhooks
{
  "name": "teams-export-success",
  "events": ["export.succeeded"],
  "url": "https://example.com/hooks/teams",
  "secret": "<HMAC>"
}
```

### 10.4 Airflow Backfill Operator (sketch)
```python
def backfill(start, end, step="1d"):
    # call CluedIn backfill endpoint or replay DLQ in windows
    ...
```

---

## 11) Common Pitfalls & How to Avoid Them

- **Pre-cleaning upstream** → breaks lineage and duplicates work. Use CluedIn cleaning projects.  
- **No contracts/versioning** → downstream breakage. Always publish contracts and bump `_vN` on breakers.  
- **Tiny Parquet files** → slow analytics. Batch/compact.  
- **Unbounded AI access** → privacy risk. Enforce masked views + logs.  
- **Webhook handlers not idempotent** → duplicate side effects. Store event IDs and use upserts.

---

## 12) One-Page SI Checklist

- Ingestion endpoints automated; no manual uploads.  
- One end‑to‑end **in→map→clean→dedup→out** path live.  
- Export contract + partitioning + retention documented.  
- Catalog scan + lineage push configured.  
- Policies/labels wired; approvals enforced for PII exports.  
- Dashboards + alerts + runbooks active.  
- CI/CD promotion path with rollback tested.  
- Power Platform/AI demos working end‑to‑end.  
- Dataverse upsert path proven with concurrency + rate limits.

---

**Outcome:** With these patterns and templates, you can plug CluedIn into lakes, warehouses, orchestration, catalogs, Power Platform & AI stacks, and Dataverse quickly—while preserving security, lineage, and SLAs. Clone the snippets, fill in environment details, and ship a thin slice first; iterate safely with contracts and policies.

