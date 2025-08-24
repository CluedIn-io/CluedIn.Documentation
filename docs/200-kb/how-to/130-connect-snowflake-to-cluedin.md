---
layout: cluedin
title: Connect SnowFlake to CluedIn
parent: Knowledge base
permalink: /kb/snowflake-to-cluedin
nav_order: 2
---

# Push data from Snowflake to CluedIn Ingestion Endpoints

This guide shows practical patterns for pushing data directly from Snowflake into CluedIn **Ingestion Endpoints** using either a Snowpark Python stored procedure (batch) or a Snowflake External Function (event/row-oriented). It follows CluedIn’s recommended practices around payload shape, batching, idempotency, and operational monitoring.

---

## When to use this

Use this guide if you already have mastered data in Snowflake (curated views/tables) and want to **push** it into CluedIn for entity creation/enrichment, rather than having CluedIn pull from Snowflake.

---

## Prerequisites

- **CluedIn**  
  - An **Ingestion Endpoint** created (from *Ingestion → Endpoints* in your CluedIn UI).  
  - The endpoint **URL** and an **API token** (or tenant key) with rights to ingest.
- **Snowflake**  
  - A warehouse you can use for procedures/functions.  
  - Role privileges to create procedures/functions, tasks, integrations.  
  - (For outbound HTTP) **External Network Access** is enabled and allowed to reach your CluedIn domain.  
  - Optional but recommended: **Snowflake Secrets** to store the CluedIn token.

> **Note**  
> Every CluedIn environment exposes an HTTPS ingestion URL. The exact path format can differ by version/tenant. In the examples below, replace `https://<cluedin-host>/<ingestion-path>` and `CLUE_TOKEN` with your actual values from the CluedIn UI.

---

## Data model & payloads

CluedIn endpoints accept JSON (and typically NDJSON for high-volume). Send **one JSON object per record**. Include a stable identifier and a last-modified timestamp whenever possible.

**Minimal recommended shape (per line for NDJSON):**
```json
{
  "externalId": "CUST-000123",
  "type": "Customer",
  "timestamp": "2025-08-20T03:14:07Z",
  "properties": {
    "name": "Acme Pty Ltd",
    "country": "AU",
    "email": "ap@acme.example",
    "isActive": true,
    "updatedAt": "2025-08-20T03:14:07Z"
  }
}
```

**Tips**
- **Idempotency:** CluedIn deduplicates/merges best when `externalId` is stable for the same logical entity.  
- **Upserts:** Always send your system-of-record “last changed” timestamp so CluedIn can reason about freshness.  
- **Batching:** Prefer **500–5,000 records** per POST (NDJSON), gzip-compressed.  
- **Headers:** `Authorization: Bearer <token>`, `Content-Type: application/x-ndjson`, `Content-Encoding: gzip` (if gzipping).

---

## Option A — Batch push with Snowpark Python (stored procedure)

This pattern is ideal for scheduled loads or micro-batching (minutes).

### 1) (Once) Allow Snowflake to call CluedIn over HTTPS
Ask your Snowflake admin to:
- Create a **NETWORK RULE** for your CluedIn hostname.
- Create an **EXTERNAL ACCESS INTEGRATION** that references that rule.
- (Recommended) Create a **SECRET** that stores the CluedIn API token.

> If you can’t use Secrets yet, you can pass the token as a procedure argument for initial testing, then switch to Secrets.

### 2) Create the stored procedure

```sql
CREATE OR REPLACE PROCEDURE CLUEDIN_PUSH(
    endpoint STRING,              -- e.g. 'https://<cluedin-host>/<ingestion-path>'
    api_token STRING,             -- for production, read from a Snowflake Secret
    sql_query STRING,             -- SELECT ... that returns the rows to push
    batch_size NUMBER DEFAULT 1000
)
RETURNS VARCHAR
LANGUAGE PYTHON
RUNTIME_VERSION = 3.10
PACKAGES = ('snowflake-snowpark-python','requests')
-- If your account requires it, include the integration name below:
EXTERNAL_ACCESS_INTEGRATIONS = ('<YOUR_EXTERNAL_ACCESS_INTEGRATION>')
HANDLER = 'run'
AS
$$
import io, json, gzip, time
import requests
from snowflake.snowpark import Session

def _iter_rows(session, query):
    # Streams rows without collecting the full DataFrame in memory
    for row in session.sql(query).to_local_iterator():
        yield row.asDict()

def _batched(iterable, size):
    batch = []
    for item in iterable:
        batch.append(item)
        if len(batch) >= size:
            yield batch
            batch = []
    if batch:
        yield batch

def _post_ndjson(endpoint, token, records, timeout=30):
    lines = [json.dumps(r, default=str) for r in records]
    raw = ("\n".join(lines)).encode("utf-8")
    gz = io.BytesIO()
    with gzip.GzipFile(fileobj=gz, mode="wb") as f:
        f.write(raw)
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/x-ndjson",
        "Content-Encoding": "gzip",
        "Accept": "application/json",
    }
    resp = requests.post(endpoint, data=gz.getvalue(), headers=headers, timeout=timeout)
    if resp.status_code >= 300:
        raise Exception(f"CluedIn ingest failed: {resp.status_code} {resp.text[:500]}")
    return resp

def run(session: Session, endpoint: str, api_token: str, sql_query: str, batch_size: int = 1000) -> str:
    total = 0
    for batch in _batched(_iter_rows(session, sql_query), int(batch_size)):
        # Basic, polite retry on 429/5xx
        for attempt in range(5):
            try:
                r = _post_ndjson(endpoint, api_token, batch)
                break
            except Exception as ex:
                if attempt == 4:
                    raise
                time.sleep(2 ** attempt)  # backoff
        total += len(batch)
    return f"Pushed {total} records to CluedIn"
$$;
```

**Quick test**
```sql
CALL CLUEDIN_PUSH(
  'https://<cluedin-host>/<ingestion-path>',
  '<CLUE_TOKEN>',
  $$SELECT
      CUSTOMER_ID      AS externalId,
      'Customer'       AS type,
      UPDATED_AT       AS timestamp,
      OBJECT_CONSTRUCT(
        'name', NAME,
        'country', COUNTRY,
        'email', EMAIL,
        'isActive', IS_ACTIVE,
        'updatedAt', UPDATED_AT
      )                AS properties
    FROM ANALYTICS.DIM_CUSTOMER
    WHERE UPDATED_AT >= DATEADD(day,-1,current_timestamp())$$,
  1000
);
```

### 3) Schedule it with a Snowflake Task (example daily 01:00 AEST)
```sql
CREATE OR REPLACE TASK CLUEDIN_PUSH_DAILY
  WAREHOUSE = <YOUR_WH>
  SCHEDULE = 'USING CRON 0 1 * * * Australia/Brisbane'
AS
  CALL CLUEDIN_PUSH(
    'https://<cluedin-host>/<ingestion-path>',
    '<CLUE_TOKEN>',
    $$SELECT /* your incremental extract */ * FROM ... $$,
    2000
  );

-- Enable the task
ALTER TASK CLUEDIN_PUSH_DAILY RESUME;
```

> **Production hardening**  
> Replace the literal token with a **Snowflake Secret** and read it in the procedure (or pass it via a secure UDF argument). Keep batch sizes modest, enable backoff/retry, and consider watermarking with a control table to ensure exactly-once semantics for each run.

---

## Option B — Row-oriented push with External Function

Use this when you want to call CluedIn inline from SQL (e.g., as part of a pipeline or upon changes). Because Snowflake External Functions call through a managed API gateway, we proxy the request via a lightweight serverless function.

### Architecture

```
Snowflake SQL → External Function → (API Gateway + Lambda/Azure Function) → CluedIn Ingestion Endpoint
```

### 1) Create a tiny relay function (example: Node.js)

**AWS Lambda (sketch):**
```js
// Sends JSON payload received from Snowflake to CluedIn
export const handler = async (event) => {
  const payload = JSON.parse(event.body || "{}");     // Snowflake sends JSON
  const resp = await fetch(process.env.CLUE_ENDPOINT, {
    method: "POST",
    headers: {
      "Authorization": `Bearer ${process.env.CLUE_TOKEN}`,
      "Content-Type": "application/json",
      "Accept": "application/json"
    },
    body: JSON.stringify(payload)
  });
  const text = await resp.text();
  return { statusCode: resp.status, body: text };
};
```
Store `CLUE_TOKEN` and `CLUE_ENDPOINT` as function secrets. In Azure, create the same with an HTTP-triggered Function App.

### 2) Register the External Function in Snowflake
Create an **API INTEGRATION** (one-time) and then:

```sql
CREATE OR REPLACE EXTERNAL FUNCTION PUSH_TO_CLUEDIN(PAYLOAD VARIANT)
RETURNS VARIANT
API_INTEGRATION = <YOUR_API_INTEGRATION>
AS 'https://<your-api-gateway-endpoint>';
```

### 3) Call it from SQL
```sql
-- Push single object per call
SELECT PUSH_TO_CLUEDIN(
  OBJECT_CONSTRUCT(
    'externalId', CUSTOMER_ID,
    'type', 'Customer',
    'timestamp', UPDATED_AT,
    'properties', OBJECT_CONSTRUCT(
      'name', NAME, 'country', COUNTRY, 'email', EMAIL, 'isActive', IS_ACTIVE
    )
  )
)
FROM ANALYTICS.DIM_CUSTOMER
WHERE UPDATED_AT >= DATEADD(minute, -15, CURRENT_TIMESTAMP());
```

> **Tip**  
> For higher throughput, wrap multiple rows into an array and let your relay function POST NDJSON to CluedIn in batches.

---

## Validate in CluedIn

After a push:
1. Open **Ingestion → Endpoints** and select your endpoint.  
2. Check the **recent requests**, **throughput**, and **errors** (4xx/5xx).  
3. Navigate to **Ingestion → Processing** (or your entity overview) to verify created/updated entities.  
4. Review any **schema mapping** or **business rule** outcomes relevant to your entities.

---

## Operational guidance

- **Batch sizing:** Start with 1,000 records per batch. Increase while monitoring latency and server CPU.  
- **Compression:** Gzip NDJSON bodies; it drastically reduces egress cost and improves throughput.  
- **Retries:** Retry on HTTP 429/5xx with exponential backoff. Do not retry on 4xx without fixing the payload.  
- **Watermarking:** Track the max `UPDATED_AT` pushed in a control table to ensure incremental loads are correct.  
- **Observability:** Log run IDs, batch counts, response codes, and the CluedIn request correlation ID if provided.  
- **Security:** Never hard-code tokens. Prefer Snowflake Secrets or your cloud’s secret manager with short-lived tokens.  
- **Schema drift:** Add defensive guards (e.g., `COALESCE`/type casts) so payloads remain valid if upstream changes.

---

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| `403 Forbidden` | Token missing/invalid | Ensure `Authorization: Bearer <token>` and token scope includes ingest. Rotate if expired. |
| `413 Payload Too Large` | Batch too big | Reduce batch size or gzip; verify CluedIn’s configured max body size. |
| `429 Too Many Requests` | Rate limiting | Implement backoff; add jitter; schedule during off-peak. |
| `5xx` server errors | Temporary downstream issue | Retry with backoff; contact CluedIn support if persistent. |
| Entities not appearing | Wrong `externalId`/`type` or mapping | Verify payload shape and mapping rules; check processing logs in CluedIn. |

---

## Copy-paste snippets

**Transform a table into NDJSON-friendly rows**
```sql
SELECT
  CUSTOMER_ID      AS externalId,
  'Customer'       AS type,
  UPDATED_AT       AS timestamp,
  OBJECT_CONSTRUCT(
    'name', NAME,
    'country', COUNTRY,
    'email', EMAIL,
    'isActive', IS_ACTIVE
  )                AS properties
FROM ANALYTICS.DIM_CUSTOMER;
```

**Call the stored procedure with an ad-hoc filter**
```sql
CALL CLUEDIN_PUSH(
  'https://<cluedin-host>/<ingestion-path>',
  '<CLUE_TOKEN>',
  $$SELECT * FROM ANALYTICS.DIM_CUSTOMER WHERE UPDATED_AT >= '2025-08-01'$$,
  1000
);
```

**Cron schedule (every 15 minutes)**
```sql
CREATE OR REPLACE TASK CLUEDIN_PUSH_Q15
  WAREHOUSE = <YOUR_WH>
  SCHEDULE = 'USING CRON */15 * * * * Australia/Brisbane'
AS
  CALL CLUEDIN_PUSH('https://<cluedin-host>/<ingestion-path>', '<CLUE_TOKEN>',
    $$SELECT * FROM ANALYTICS.DIM_CUSTOMER WHERE UPDATED_AT >= DATEADD(minute,-15,current_timestamp())$$, 2000);
ALTER TASK CLUEDIN_PUSH_Q15 RESUME;
```

---

## FAQs

**Can I send CSV?**  
Yes, but JSON/NDJSON is strongly recommended—JSON preserves types and nested structures that CluedIn can use for mapping and enrichment.

**What about deletes?**  
Emit a tombstone signal (e.g., `{"externalId": "...", "type": "Customer", "deleted": true, "timestamp": "..."}`) and configure your downstream processing rules in CluedIn to interpret deletes.

**How do I handle nested relations?**  
Send separate entity payloads (e.g., `Customer`, `Address`) with stable `externalId`s. If your CluedIn build supports edge creation via ingestion, include reference keys; otherwise, model relationships in subsequent enrichment steps.

---

## Summary

- For **scheduled or micro-batch** loads, use the **Snowpark Python stored procedure** to POST **NDJSON** to CluedIn with gzip, backoff, and watermarking.  
- For **inline/row-oriented** flows, use a **Snowflake External Function** that relays to CluedIn via a small serverless function.  
- Always send **stable IDs**, **timestamps**, and **typed properties** to make CluedIn’s unification and lineage work in your favor.
