---
layout: cluedin
title: CluedIn for Solution Architects — integration & reference architecture guide
parent: Knowledge base
permalink: /kb/cluedin-solution-architects
nav_order: 2
---
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

**Audience:** Solution/Enterprise Architects, Platform Owners, Domain Architects  
**Goal:** Explain where **CluedIn** fits in the wider data landscape, which architectural patterns it enables, and how to integrate it cleanly with surrounding systems (sources, lakes/warehouses, catalogs, BI/AI/Apps, and governance).

> Assumptions: You favor **event-driven**, **ELT**, **infrastructure-as-code**, and **least-privilege** security. This guide is platform-agnostic with callouts for Azure/AWS/GCP and the Microsoft Power Platform.

---

## 1) What CluedIn Is (and Isn’t)

- **Is:** a **data unification + quality** platform that **ingests raw data**, **maps to canonical entities**, enables **cleaning**, **validation**, **dedup/golden records**, and **exports** reliable outputs to your downstream systems. It supports **streaming** and **batch**, **policy-based access**, and **auditability**, with **AI Agents** for analysis/suggestions.
- **Is not:** a heavy ETL monolith, BI semantic layer, or a general-purpose orchestrator. It plays **with** those systems, not instead of them.

**Positioning vs common components**
- **With ETL/ELT tools** (ADF/Airflow/Glue/Fabric): CluedIn owns **entity modeling, quality, unification**; your orchestrator triggers/schedules.
- **With Lake/Warehouse** (ADLS/S3/GCS + Fabric/Synapse/BigQuery/Snowflake): CluedIn exports **golden/wide/star** data to these stores.
- **With MDM**: CluedIn’s dedup + survivorship can act as **operational MDM-lite** or feed/consume a dedicated MDM if present.
- **With Catalog/Lineage** (Purview/Data Catalog/Collibra): CluedIn publishes **metadata/lineage** and respects **classifications**.
- **With Reverse ETL / Apps** (Power Apps/Automate, Kafka topics, APIs): CluedIn provides **operationalized, trustworthy** datasets and events.

---

## 2) Reference Architectures

### 2.1 High-Level (Hybrid Streaming + Batch)

```
[SaaS/DB/Events] ──► (Producers: CDC/HTTP/Kafka/S3) ──► CluedIn Ingestion Endpoints
       |                                                    │
       |                                              Raw Landing (ELT)
       |                                                    │
       └─────────────► (Optional Lake Zone) ◄───────────────┘
                                                           │
                                         Mapping ⇢ Cleaning ⇢ Validations ⇢ Dedup/Golden
                                                           │
                                      ┌─────────────────────┴─────────────────────┐
                                      │                                           │
                           Export Targets (Tables/Files)               Export Targets (Topics/APIs)
                         ► Warehouse/Lake (Snowflake/Fabric/        ► Kafka/Event Hub/Webhooks/Reverse‑ETL
                           BigQuery/Synapse/Databricks)             ► Apps/Operational CX
                                      │                                           │
                                  BI/AI/Analytics                         Apps/Workflows/Automation
                                      │                                           │
                         Catalog/Lineage (Purview/Collibra)        Observability (SIEM, APM, Dashboards)
```

### 2.2 Microsoft-Centric Blueprint

```
Dataverse/D365/Apps → Power Automate (Flows) → CluedIn Ingestion (HTTP/Webhook/Event Hub)
                                            ↑                                       │
                                     Teams/Approvals                        AI Agents (masked)
ADLS/Fabric OneLake ← Exports (Parquet/SQL) ← CluedIn                         │
    Power BI / Fabric Semantic Model   ↑                                      │
Purview Catalog & Lineage ◄────────────┴────────────── Metadata/Lineage Push ◄┘
```

### 2.3 Data Mesh Placement
- CluedIn can be a **domain data product factory**: each domain owns **ingestion→golden→export** with governance guardrails and shared platform controls (SSO, policies, audit, catalog).

---

## 3) Integration Patterns

### 3.1 Ingestion Into CluedIn
- **Streaming:** Kafka/Event Hubs; prefer JSON lines, include `event_id`, `updated_at`, `schema_version` headers; key by business ID for ordering.
- **HTTP/Webhooks:** simple producers (Power Automate/Apps, custom services) POST to ingestion endpoints; include **idempotency keys**.
- **Batch/Landing:** S3/ADLS/GCS watchers for **CSV/JSON/Parquet** on a schedule; use **manifests** for completeness; automate backfills.
- **CDC:** Debezium/ADF/Fabric Data Pipelines to stream DB changes; normalize op codes.

**Architectural note:** Keep producers **dumb** (no pre-clean). CluedIn is **ELT**: land first, transform inside via cleaning projects and policies.

### 3.2 Outbound from CluedIn
- **Tables/Views:** export to warehouses (Fabric/Synapse, Snowflake, BigQuery, Databricks). Choose **upsert** with **stable PKs**; version breaking changes (`_vN`).
- **Files:** Parquet to lake zones for batch analytics; partition by date/entity.
- **Events:** publish to Kafka/Event Hubs when exports finish or when golden records change (perfect for **Reverse ETL** patterns).
- **APIs/Webhooks:** push updates to SaaS; sign webhooks (HMAC) and design **idempotent** handlers.

### 3.3 Catalog & Lineage
- **Scan** exported datasets from lake/warehouse with your catalog (Purview/Collibra/Glue).  
- **Push** process lineage (`source → CluedIn → export`) via Atlas/REST where supported.  
- Synchronize **classifications/labels** (PII/Restricted) and use them to drive policies in CluedIn and your BI/lake security layers.

### 3.4 Power Platform Integration
- **Power Automate:** trigger on business events → call CluedIn ingestion endpoints; or receive CluedIn webhooks (DQ alerts, export complete) → route to Teams/Dataverse.
- **Power Apps:** stewarding UIs (review duplicates, fix invalids) over CluedIn APIs.
- **Power BI/Fabric:** consume versioned exports (star/wide); manage **semantic models** separately but aligned with CluedIn contracts.

---

## 4) Solution Design Decisions (Playbook)

### 4.1 Choosing Export Shapes
- **Star schema** → BI at scale, facts + SCD2 dims.
- **Wide operational tables** → CX apps, CRM backfills, support tooling.
- **Event streams** → near‑real‑time syncs and automation.
- **API endpoints** → per‑entity CRUD patterns are *not* the goal; favor batch/event outputs for scalability.

### 4.2 Identity & Golden Records
- Start with **deterministic dedup** (email/phone/customer_id).  
- Define **survivorship**: source precedence + recency.  
- Emit **stable entity IDs** to downstreams to avoid churn.

### 4.3 Temporal Strategy
- Decide **SCD1 vs SCD2** per entity; BI usually needs **SCD2** for dims.  
- For events, carry `event_time` (business) and `ingest_time` (processing).

### 4.4 Contracts & Versioning
- Every export has a **contract** (schema, keys, SLA, labels).  
- Breaking changes → new `_vN` and a **dual‑run** window with migration notes.

### 4.5 Governance Hooks
- **Labels** (`PII`, `Restricted`) at field/entity drive **masking** and **approval** workflows (e.g., PII export requires Governance approval).  
- **Audit logs** must cover promotions, policy changes, merges, and deletions.

---

## 5) End‑to‑End Blueprints

### 5.1 Real‑Time Customer 360 (Ops + BI)
1. **Sources:** CRM, Support, Marketing streams.  
2. **Ingest:** Kafka topics into CluedIn; CDC for legacy DB.  
3. **Unify:** Mapping + cleaning + deterministic dedup → `Person` golden.  
4. **Exports:**  
   - `customers_wide_v1` (ops wide) → CRM/Support via Reverse ETL.  
   - `customers_dim_v1` + `orders_fct_v1` → warehouse for BI.  
5. **Catalog:** Purview scan + lineage push.  
6. **Apps/AI:** Power Apps for stewarding; AI Agent reports DQ trends weekly.

### 5.2 B2B Product Catalog Harmonization
- **Ingest** vendor feeds (S3/HTTP) + ERP/Kanban events.  
- **Standardize** attributes (units, categories), deduplicate SKUs.  
- **Exports** to commerce PIM and search index; event stream on SKU changes.  
- **DQ KPIs**: completeness of attributes, invalid GTIN rate, duplicate rate.

### 5.3 “Data Quality Firewall” for Downstream
- **Ingest** raw; **validate** with rules (regex, referential, domain lists).  
- **Quarantine** failures; webhook to ticketing; weekly auto‑fixes via cleaning projects.  
- **Export** only passing records to a downstream operational DB.  
- **Metrics**: validity %, quarantine count, MTTR per issue type.

---

## 6) Security, Privacy & Compliance (Architect View)

- **SSO‑only** with OIDC/SAML; SCIM for lifecycle; **group‑to‑role** mapping.  
- **Least privilege** roles; **feature toggles** isolated per env.  
- **Data policies**: column masking, row filters, deny‑by‑default for sensitive exports.  
- **PII handling**: masked views for AI Agents and non‑prod environments.  
- **Secrets** in a vault; short‑lived tokens; IP allowlists on webhooks.  
- **Retention & legal holds**: encode as policies; export destruction evidence.  
- **Multi‑region**: active/active for ingestion; exports regionally localized; clear RPO/RTO.

---

## 7) Non‑Functional Requirements (NFRs)

| NFR | Guidance |
|---|---|
| **SLA (freshness)** | Export contracts with `freshness_p95_minutes`; alarms on breach. |
| **Latency** | For near‑real‑time, prefer event pipelines with small batches. |
| **Throughput** | Partition events; scale consumers; avoid tiny files. |
| **Resilience** | DLQ + replay; idempotent producers; backpressure control. |
| **Observability** | Correlation IDs; structured logs; dashboards for volumes/latency/errors. |
| **Cost** | Columnar formats; partition strategy; right‑size schedules. |
| **Compliance** | Immutable audit logs; approvals for PII exports; evidence packs. |

---

## 8) Orchestration & CI/CD

- Use **Airflow/ADF/Fabric Data Pipelines/GitHub Actions** to deploy configs (mappings, cleaning, policies, exports) as **code**.  
- Promotion: **PR → staging diff → prod**, with a **change window** and rollback plan.  
- Tests: schema/domain/FK/contract checks; regression diffs across exports.  
- Automate **lineage publishing** post‑export and **catalog scans**.

---

## 9) Observability & Runbooks

- **Dashboards:** ingestion success/latency, export success/rows, DQ KPIs, dedup queue size.  
- **Alerts:** export failure, schema drift, DQ breach (validity/duplicate spikes), webhook retry storms.  
- **Runbooks:** ingestion 4xx/5xx spikes, export schema drift, duplicate surges, SLA breaches; each with **contain/diagnose/rollback/backfill** steps.

---

## 10) Decision Helpers (When to…)

- **Use CluedIn mapping vs ETL transforms?**  
  - Entity semantics and unification → **CluedIn**.  
  - Heavy joins/enrichment external to CluedIn or compute‑intensive transforms → **ETL/warehouse**.

- **Star vs Wide exports?**  
  - BI → **Star (SCD2 dims + facts)**.  
  - Operational syncs/apps → **Wide**.

- **Streaming vs Batch ingestion?**  
  - Event‑driven, low‑latency needs → **Streaming**.  
  - Bulk daily snapshots/backfills → **Batch**.

- **Deterministic vs Fuzzy dedup?**  
  - Start **deterministic**; add fuzzy rules off‑peak once precision is measured.

---

## 11) Templates (Copy/Paste)

### 11.1 Export Contract (with governance fields)
```yaml
name: customers_wide_v1
owner: "Sales Ops"
primary_key: customer_id
delivery: { type: sql-table, schedule: hourly }
sla: { freshness_p95_minutes: 60 }
labels: ["PII:email"]
compatibility: additive_only
lineage_required: true
approval_required_when_labels: ["PII","Restricted"]
```

### 11.2 Policy Sketches
```yaml
policy: mask_email_default
target: entity:Person.field:email
actions: [read]
effect: allow_with_mask
mask: "partial_email"
unless: [{ role_in: ["Data Steward","Administrator"] }]
```

```yaml
policy: export_requires_approval
target: export:*
actions: [promote]
effect: require_approval
when: "export.contains_label('PII')"
approvers: ["Governance Manager","DPO"]
```

### 11.3 Webhook Registration (pseudo)
```json
POST /api/webhooks
{
  "name": "teams-export-success",
  "events": ["export.succeeded"],
  "url": "https://example.com/hooks/teams",
  "secret": "<HMAC>"
}
```

---

## 12) Operating Cadence (Architecture Guild)

**Bi‑weekly design review:** incoming sources, export changes, lineage completeness, PII exposure checks.  
**Monthly scorecard:** export contract coverage, DQ trend, incident classes, cost, catalog lineage %, AI usage review.  
**Quarterly roadmap:** domains onboarding, deprecations of `_v0`, platform upgrades, governance maturity.

---

## 13) Anti‑Patterns to Avoid

- Designing a **grand unified model** before shipping any export.  
- Pre‑cleaning upstream; defeating ELT and lineage transparency.  
- Shipping **breaking changes** without contracts/versioning and a dual‑run window.  
- Treating AI Agents as unrestricted data readers; avoid unmasked access.  
- Ignoring **catalog/lineage**; producing orphaned BI datasets.

---

## 14) One‑Page Checklist (Print This)

- Ingestion endpoints (stream/batch) automated, no manual uploads.  
- Minimal mapping → **exports live** → iterate mapping/cleaning.  
- Dedup deterministic first; survivorship clarified.  
- Contracts for each export; `_vN` for breakers.  
- Policies/labels on PII; approvals enforced.  
- Catalog & lineage integrated; Purview scan/push verified.  
- Dashboards + alerts + runbooks in place.  
- CI/CD promotion path; rollback tested; audit logs retained.

---

**Bottom line for architects:** Place CluedIn at the **heart of unification and quality**, bridging raw sources and trustworthy consumer outputs. Keep it event‑friendly, contract‑driven, catalog‑connected, and governed by policy. Integrate tightly with your orchestrator, lake/warehouse, catalog, Power Platform/Apps, and SIEM—so the rest of your architecture can move faster with confidence.

