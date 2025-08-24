---
layout: cluedin
title: CluedIn for Developers
parent: Knowledge base
permalink: /kb/cluedin-for-developers
nav_order: 2
---

# CluedIn for Developers — Build, Integrate, Automate

**Audience:** Application developers, integration engineers, platform/DevOps engineers  
**Goal:** Give developers a practical, end‑to‑end handbook to build against CluedIn: auth, APIs/SDK patterns, ingestion producers, export consumers, webhooks, cleaning/validation-as-code, AI Agents, dedup, logging/audit, testing, CI/CD, and secure operations.

> Assumptions: Your org uses SSO, keeps config as code, and prefers automated ingestion (streams/batches) over manual file uploads.

---

## 0) Your First 48 Hours (Checklist)

**Access & Tools**
- [ ] Sign in via **SSO**; confirm a **Developer/Engineer** role with needed scopes.
- [ ] Get a **short‑lived token** (OAuth client) or **scoped PAT** for local dev.
- [ ] Install: HTTP client (curl/Postman), language SDKs, and repo with config‑as‑code.

**Hello, CluedIn**
- [ ] Call **`/api/me`** to test auth.  
- [ ] Create a **sandbox Ingestion Endpoint** and push a sample record.  
- [ ] Create a **staging Export** and run an end‑to‑end smoke.

**Guardrails**
- [ ] Set **correlation_id** conventions for all requests.  
- [ ] Configure **retries with jitter** and **idempotency keys**.  
- [ ] Wire a **dead‑letter** path and a simple **replay** tool.

---

## 1) Architecture (Developer View)

```
[Producer] → Ingestion Endpoint → Raw Store → Mapping → Cleaning/Validation →
Dedup/Golden → Exports (tables/topics/APIs/files) → [Consumers/Apps/BI]
                                 ↓
                            AI Agents (analysis/suggestions)
```

You primarily write:
- **Producers** that push data *in* (HTTP/Kafka/Batch/CDC).
- **Consumers** that react to **Exports** or **Webhooks**.
- **Jobs** or **functions** that call CluedIn APIs (AI Agents, dedup, policies).
- **Infra glue** (CI/CD, secrets, logging, alerts).

---

## 2) Authentication & Identity

### 2.1 OAuth 2.0 Client (preferred for services)
```json
POST /oauth/token
{
  "grant_type": "client_credentials",
  "client_id": "<ID>",
  "client_secret": "<SECRET>",
  "scope": "ingest:write export:read policy:read"
}
```

### 2.2 Personal Access Tokens (PAT) (for local dev)
- Create in **Admin → API Tokens** with **minimal scopes** and **expiry**.
- Store in a **secret manager**; never commit to git.

### 2.3 Request Hygiene
Always send:
- `Authorization: Bearer <token>`  
- `X-Correlation-Id: <uuid>`  
- `Content-Type: application/json` (for JSON payloads)

---

## 3) API Patterns (Paging, Filtering, Errors)

**Paging**
```
GET /api/entities?type=Person&limit=200&cursor=<token>
→ 200 + { "items": [...], "next_cursor": "..." }
```

**Filtering**
```
GET /api/exports/runs?name=warehouse-contacts-v1&since=2025-08-20T00:00:00Z
```

**Common errors (illustrative)**
- `400` invalid schema / missing required fields  
- `401/403` auth/permission issues  
- `409` conflict (idempotency violation)  
- `429` rate limit → backoff and retry  
- `5xx` transient → exponential backoff with jitter

**Retry policy (pseudo)**
```ts
const base = 250; // ms
retry = attempt => Math.min(30_000, base * 2 ** attempt) + rand(0, 200);
```

---

## 4) Ingestion Producers

### 4.1 HTTP/Webhook (JSON lines)
```bash
curl -X POST \
  -H "Authorization: Bearer $TOKEN" \
  -H "X-Correlation-Id: $(uuidgen)" \
  -H "Content-Type: application/json" \
  -d '{"source":"crm-contacts","payload":{"id":"c_123","email":"a@example.com","updated_at":"2025-08-22T12:00:00Z"}}' \
  https://<HOST>/api/ingest
```

**Best practices**
- **Idempotency**: include stable `id` and `updated_at`.  
- **Batching**: prefer small batches (e.g., 1–5k records).  
- **Compression**: `Content-Encoding: gzip` for large payloads.  
- **DLQ**: send parse failures to a durable store with replay tooling.

### 4.2 Node.js example
```ts
import axios from "axios";
const client = axios.create({ baseURL: process.env.CLUE_HOST });
async function ingestContact(c) {
  const r = await client.post("/api/ingest", {
    source: "crm-contacts",
    payload: c,
  }, {
    headers: {
      Authorization: `Bearer ${process.env.CLUE_TOKEN}`,
      "X-Correlation-Id": crypto.randomUUID()
    },
    timeout: 10000
  });
  return r.data;
}
```

### 4.3 Python example
```python
import os, uuid, requests, json
host = os.environ["CLUE_HOST"]; token = os.environ["CLUE_TOKEN"]
payload = {"source":"crm-contacts","payload":{"id":"c_123","email":"a@example.com"}}
r = requests.post(f"{host}/api/ingest", json=payload,
  headers={"Authorization":f"Bearer {token}","X-Correlation-Id":str(uuid.uuid4())}, timeout=10)
r.raise_for_status()
print(r.json())
```

### 4.4 Kafka/Event Hub
- One topic per domain/entity; include schema version in headers.  
- Ensure **producer idempotence** and **ordered keys** (e.g., `id`).

### 4.5 Batch (S3/Blob/ADLS)
- Land **JSON/CSV/Parquet** on schedule; register a bucket‑watch endpoint.  
- Keep **manifest** files for completeness and replay.

---

## 5) Mapping, Cleaning, Validation as Code

### 5.1 Minimal Mapping (pseudo‑YAML)
```yaml
entity: Person
source: "crm-contacts"
fields:
  id: $.id
  email: $.email
  first_name: $.first_name
  last_name: $.last_name
  updated_at: $.updated_at
```

### 5.2 Cleaning Project
```yaml
project: normalize_contacts
schedule: "0 * * * *"
steps:
  - name: normalize_email
    action: set
    field: email
    value: lower(trim(email))
  - name: e164_phone
    when: phone is not null
    action: set
    field: phone
    value: to_e164(phone, default_country="AU")
```

### 5.3 Validations
```yaml
rule: email_regex
entity: Person
check: { regex: "^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$" }
severity: high
on_fail: { action: "flag" }
```

**Dev loop:** edit YAML → PR → staging export diff → promote.

---

## 6) Exports & Contracts

### 6.1 Export Config (table)
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

### 6.2 Contract (YAML)
```yaml
name: contacts_v1
primary_key: contact_id
delivery: { type: sql-table, schedule: hourly }
sla: { freshness_p95_minutes: 60 }
compatibility: additive_only
```

**Versioning:** breaking changes → `_v2`; run both until consumers migrate.

---

## 7) Webhooks & Eventing

### 7.1 Registering a Webhook (pseudo)
```json
POST /api/webhooks
{
  "name": "export-success-teams",
  "events": ["export.succeeded"],
  "url": "https://example.com/hooks/export",
  "secret": "<HMAC_SECRET>"
}
```

### 7.2 Verify Signatures
```ts
import crypto from "crypto";
function verify(sig, body, secret) {
  const h = crypto.createHmac("sha256", secret).update(body).digest("hex");
  return crypto.timingSafeEqual(Buffer.from(sig,"hex"), Buffer.from(h,"hex"));
}
```

**Retry model:** Webhooks are retried on non‑2xx; make handlers **idempotent**.

---

## 8) AI Agents (Programmatic Use)

### 8.1 Run an Analysis
```json
POST /api/ai/agents/run
{
  "agent": "dq-analyzer",
  "target": { "entity": "Person" },
  "mode": "analysis",            // analysis | suggest | auto_fix (guarded)
  "options": { "sample": 10000 }
}
```

### 8.2 Retrieve Findings
```
GET /api/ai/agents/runs/<run_id>/findings
→ { "issues":[{"field":"email","type":"invalid","examples":[...]}, ...] }
```

**Guardrails**
- Restrict to **masked** views for PII.  
- Treat auto‑fixes as code changes (reviewable, reversible).

---

## 9) Dedup APIs

### 9.1 Create Rules (deterministic first)
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

### 9.2 Merge/Unmerge (pseudo)
```
POST /api/dedup/merge { "entity":"Person", "ids":["p1","p2"] }
POST /api/dedup/unmerge { "entity":"Person", "id":"p1" }
```

Log decisions; update **survivorship** config.

---

## 10) Logs, Audit & Observability

### 10.1 Fetch Logs (illustrative)
```
GET /api/logs?category=export&name=warehouse-contacts-v1&since=2025-08-23T00:00:00Z
```

### 10.2 Audit Events
- SSO sign‑ins, role grants, token lifecycle, policy changes, export promotions, merges.

```
GET /api/audit?action=policy.update&since=2025-08-01
```

### 10.3 Correlation & Tracing
- Pass a **correlation_id** end‑to‑end and include it in logs and errors.  
- Emit **metrics**: success/failure counts, latency, row counts, DLQ size.

---

## 11) Testing & Local Dev

### 11.1 Unit Tests
- Validate normalization helpers and schema mappers.  
- Golden files for tricky encodings, null behavior, and long strings.

### 11.2 Contract Tests
- Assert export **schema** and **SLA** (freshness).

### 11.3 Stubs & Mocks
- Spin a **mock CluedIn** (OpenAPI stub) for local dev.  
- Record/replay HTTP using tools like `vcrpy`/`nock`.

### 11.4 Example PyTest
```python
def test_email_normalization():
    assert normalize_email("  A@Example.COM  ") == "a@example.com"
```

---

## 12) CI/CD & Promotion

### 12.1 GitHub Actions (sketch)
```yaml
name: cluedin-pipelines
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: ./tools/validate-config.sh   # lint YAML/JSON
      - run: pytest -q                    # unit tests
  deploy-staging:
    needs: validate
    if: github.ref == 'refs/heads/main'
    steps:
      - run: ./tools/apply.sh env/test
  deploy-prod:
    needs: deploy-staging
    steps:
      - run: ./tools/apply.sh env/prod    # change window only
```

### 12.2 Release Notes
- Summarize mapping/cleaning/export diffs, risk, rollback, owners, metrics to watch.

---

## 13) Security Essentials

- **Least privilege** scopes for tokens; rotate ≤ 90 days.  
- Secrets in **vaults**, never in code or logs.  
- **Mask PII by default** in non‑prod and in AI prompts.  
- Validate **webhook signatures** and protect endpoints with allowlists.  
- Log **who**, **what**, **where** (IP), and **when** for sensitive ops.

---

## 14) Performance & Cost

- Prefer **Parquet** for batch; partition by date/time.  
- Tune **batch size** and **parallelism**; avoid tiny files.  
- Cache reference data; precompute hot aggregates.  
- Run heavy dedup or fuzzy steps **off‑peak**.

---

## 15) Cookbooks

### 15.1 Build an Ingestion Microservice (Node.js)
1. Read from CRM API delta endpoint.  
2. Transform minimal fields; add `updated_at`.  
3. POST to `/api/ingest` with retries+DLQ.  
4. Emit metrics and pass `X-Correlation-Id`.

### 15.2 Export‑Driven Reverse ETL (Python)
1. Poll `/api/exports/runs?name=contacts_v1&status=success`.  
2. Diff changed rows since last watermark.  
3. Upsert to downstream SaaS/CX via their API.  
4. Log audit record with counts and latency.

### 15.3 Webhook to Teams
- Register `export.succeeded` webhook.  
- Verify HMAC, format message card, post to Teams webhook URL.

### 15.4 Backfill CLI
- Accept `start/end` timestamps and entity type.  
- Read source snapshots; push batches with rate limit and progress bar.  
- Tag runs with `correlation_id` and write a resumable state file.

---

## 16) Templates

### 16.1 `.env.example`
```
CLUE_HOST=https://your-cluedin-host
CLUE_TOKEN=
LOG_LEVEL=info
```

### 16.2 Makefile
```makefile
lint: ; ./tools/validate-config.sh
test: ; pytest -q
run:  ; node src/index.js
```

### 16.3 Dockerfile (Node)
```dockerfile
FROM node:20-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --omit=dev
COPY . .
CMD ["node","src/index.js"]
```

---

## 17) Troubleshooting

**`401/403`**: token scope/expiry; SSO group‑to‑role mapping.  
**`429`**: respect `Retry-After`; backoff with jitter; reduce concurrency.  
**Schema null explosion**: check mapping field paths and cleaning order.  
**Webhook storms**: dedupe by event id; idempotent handlers; collapse alerts.  
**Export drift**: switch to staging export; diff schemas; version bump if breaking.

---

## 18) Operating Rhythm

**Daily**: glance pipeline health, DLQ, last export run, top errors.  
**Weekly**: ship 1–2 improvements; tighten tests; review costs.  
**Monthly**: token/secrets rotation; access review; deprecate old exports.

---

## 19) Definition of Done (Dev)

- Config in repo with PR review & audit links.  
- Staging run green; prod run green ×3.  
- DQ metrics same or better.  
- Runbook updated; alert routed; rollback noted.

---

**You’re set:** build producers and consumers, codify mapping/cleaning/validations, leverage AI Agents with guardrails, program the dedup lifecycle, observe everything, and ship safely with versioned exports and CI/CD.

