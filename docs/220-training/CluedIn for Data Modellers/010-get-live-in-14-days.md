---
layout: cluedin
title: CluedIn for Data Modellers
parent: Knowledge base
permalink: /kb/cluedin-data-modellers
nav_order: 2
---

# CluedIn for Data Modellers — Canonical & Export Schema Playbook

**Audience:** Data Modellers, Semantic Layer Owners, Analytics Architects  
**Goal:** Provide a practical handbook to model data in CluedIn—canonical entities, relationships, semantics, temporal patterns, export schemas, contracts, and safe iteration with Stewards, Engineers, Admins, and Governance.

> Assumption: CluedIn runs **ELT**—land raw first, then model/standardize in-platform. Your superpower is designing schemas that evolve safely and power trustworthy exports.

---

## 0) Your First 48 Hours (Checklist)

**Context & Access**
- [ ] Sign in via **SSO**; verify your role (Model/Engineer/Steward).  
- [ ] Review the **Use‑Case Brief**, **Runbook**, and **Export Contracts** already defined.  
- [ ] Browse **Entities Explorer** and current **Exports** for your domain.

**Model Scope**
- [ ] Identify the **canonical entities** (e.g., `Person`, `Organization`, `Order`, `Product`).  
- [ ] List **critical attributes** and **business keys** per entity.  
- [ ] Document **relationships** (cardinality, optionality).

**Standards**
- [ ] Agree on **naming conventions**, **data types**, **timezones/temporal fields**.  
- [ ] Align with **labels/classifications** (PII, Restricted).  
- [ ] Pick **SCD** strategy per entity (SCD1 vs SCD2).

**Change Safety**
- [ ] Confirm **staging export** for rehearsing model changes.  
- [ ] Set up **schema diff** and **contract tests**.  
- [ ] Define a **versioning policy** for exports (e.g., `_v1`, `_v2`).

---

## 1) Role Scope (What You Own)

- Canonical **entity & relationship** design; attribute semantics and units.  
- **Keys & identity** strategy (surrogates, natural keys, source keys).  
- **Temporal modeling** (SCD types, event time vs processing time).  
- **Reference/master data** modeling and code lists.  
- **Semantics** for metrics and derived attributes (definitions & lineage).  
- **Export schemas** (star/wide/event) and **contracts** with consumers.  
- **Change governance**: backward compatibility, deprecations, and documentation.

You partner with:
- **Stewards** (quality rules, dedup survivorship, glossary),  
- **Engineers** (ingestion, mapping, cleaning, exports),  
- **Admins/Governance** (access, labels, approvals).

---

## 2) Modelling Principles in CluedIn

1. **Start minimal; evolve rapidly.** Model only what you need for current exports.  
2. **Prefer additive changes.** Breakers require new versioned exports.  
3. **Separate concerns:** mapping ≠ cleaning ≠ export shaping.  
4. **Make identity explicit.** Always carry `source_system`, `source_id`, `updated_at`.  
5. **Document semantics adjacent to schema** (glossary + YAML spec).  
6. **Model for query patterns.** Choose star/wide/event based on consumers.  
7. **Label sensitive fields.** PII/Restricted labels drive masking/access policies.

---

## 3) Canonical Entities & Attributes

### 3.1 Naming & Types
- `snake_case` for fields, `UpperCamel` for entities (e.g., `Person`).  
- Use **typed timestamps** with timezone (`*_at` in UTC).  
- Store IDs as **strings** unless arithmetic is required.  
- Enumerations use **UPPER_SNAKE** values (document the domain list).

### 3.2 Keys
- **Surrogate key**: `person_id` (stable, synthetic).  
- **Business keys**: `email`, `customer_number` (may change).  
- **Source link**: `{source_system, source_id}` as unique pair.

### 3.3 Example Canonical Spec
```yaml
entity: Person
keys:
  surrogate: person_id
  natural: [email]        # optional; can be multi
sources:
  - system: "crm"
    id_field: "id"
attributes:
  person_id: { type: string, required: true, semantics: "stable synthetic id" }
  email: { type: string, labels: ["PII"], constraints: { regex: "^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$" } }
  first_name: { type: string }
  last_name: { type: string }
  phone_e164: { type: string, labels: ["PII"] }
  updated_at: { type: timestamp, required: true }
lineage_fields: [source_system, source_id, source_updated_at]
```

---

## 4) Relationships

### 4.1 Patterns
- **1:M** (`Organization` → `Person`) via foreign key `organization_id`.  
- **M:M** (`Person` ↔ `Product`) via bridge `PersonProduct` with role/effective dates.  
- **Hierarchies** (e.g., org trees) via `parent_id` + path/level fields.

### 4.2 Relationship Spec
```yaml
relationship: EMPLOYED_BY
from: Person
to: Organization
cardinality: many_to_one
navigability: from_to
keys:
  from_fk: organization_id
semantics: "Employment at current employer"
```

> Record **direction**, **cardinality**, and whether the relationship is **current** or **historical**.

---

## 5) Temporal Modeling (SCD)

### 5.1 Choose per entity
- **SCD1** (overwrite): current snapshot only. Good for operational exports.  
- **SCD2** (history): track changes with `effective_from`, `effective_to`, `is_current`.  
- **SCD3** (limited history): carry previous value fields for comparison.

### 5.2 SCD2 Template
```yaml
entity: Organization_dim
scd: type2
keys: { surrogate: organization_sk, business: [organization_id] }
temporal:
  effective_from: valid_from
  effective_to: valid_to
  current_flag: is_current
defaults:
  valid_to: "9999-12-31T23:59:59Z"
```

### 5.3 Event vs Snapshot
- **Event** models (append‑only) are ideal for BI with time series.  
- **Snapshot** exports provide easy point‑in‑time queries.

---

## 6) Reference & Master Data

### 6.1 Code Lists
Document controlled vocabularies and map source variants during cleaning:
```yaml
reference: country_codes
canonical: ISO_3166_1_ALPHA2
values: ["US","AU","GB","DE","FR","JP","NZ"]
aliases:
  "United States": "US"
  "U.S.": "US"
```

### 6.2 Master Data (Golden Records)
- Use **dedup** rules (deterministic first) to converge sources.  
- Define **survivorship** (source precedence, recency, field overrides).

```yaml
survivorship:
  precedence: ["crm","support","marketing"]
  recency_win: true
  field_overrides:
    email: "most_recent_non_null"
```

---

## 7) Mapping Strategy (Raw → Canonical)

### 7.1 Principles
- Map **minimum** attributes for v0 exports.  
- Normalize in **cleaning projects** (case, formats, code lists).  
- Keep **source fields** for traceability.

### 7.2 Example Mapping (pseudo)
```yaml
entity: Person
source: "crm-contacts"
fields:
  person_id: $.id              # or synthetic from source id
  email: $.email
  first_name: $.first_name
  last_name: $.last_name
  phone_e164: normalize_phone($.phone, "AU")
  updated_at: $.updated_at
stash:
  source_system: "crm"
  source_id: $.id
  source_updated_at: $.updated_at
```

---

## 8) Export Schema Patterns

### 8.1 Star Schema (BI)
- **Facts** (events/measures) with keys to **Dims**.  
- **Dims** carry attributes (SCD2 dims for history).

```yaml
fact: orders_fct_v1
grain: "order_line"
dimensions: [date_dim, customer_dim, product_dim]
measures:
  - name: gross_amount
    type: decimal(18,2)
  - name: net_amount
    type: decimal(18,2)
```

### 8.2 Wide Tables (Operational Analytics)
- One row per business entity; denormalize child counts or latest states.

### 8.3 Event Streams
- Append-only export (e.g., to Kafka/Event Hub) with `event_time` + `correlation_id`.

### 8.4 Export Contract
```yaml
name: customers_v1
primary_key: customer_id
delivery: { type: sql-table, schedule: hourly }
schema:
  - name: customer_id  ; type: string ; required: true
  - name: email        ; type: string ; labels: ["PII"]
  - name: status       ; type: string ; domain: ["ACTIVE","INACTIVE"]
sla:
  freshness_p95_minutes: 60
compatibility: additive_only
```

---

## 9) Semantics & Metric Definitions

- Write **metric specs** with business logic, filters, and grain.  
- Align with BI/semantic layer (e.g., Power BI/Looker definitions).

```yaml
metric: active_customers_90d
grain: "day"
entity: Person
definition: "Customers with ≥1 completed order in last 90 days"
filters: { order_status: "COMPLETED" }
owner: "Sales Ops"
```

---

## 10) Constraints, Validations & Labels

- Enumerations (`status`, `country_code`).  
- Regex constraints (email, phone).  
- Cross-field checks (`order_date <= ship_date`).  
- **Labels** to tie to policies (`PII`, `Restricted`).

```yaml
constraints:
  - field: status
    in: ["ACTIVE","INACTIVE","PROSPECT"]
labels:
  - field: email
    add: ["PII"]
```

---

## 11) Internationalization (i18n) & Addresses

- Store **addresses** as structured fields (`line1`, `line2`, `city`, `region`, `postal_code`, `country_code`).  
- Use **ISO** codes; normalize during cleaning.  
- Timezones: store **UTC** plus `timezone` field if needed for local rendering.

---

## 12) Performance & Scale Considerations

- Use **columnar** formats (Parquet) for batch exports.  
- Avoid excessive high‑cardinality dimensions in star schemas; pre-aggregate where needed.  
- Partition facts by **event_date**; cluster by keys frequently filtered.  
- For wide tables, cap column count; offload blobs/json to sidecar tables if necessary.

---

## 13) Change Management & Versioning

### 13.1 Backward Compatibility
- **Additive** changes (new nullable columns) are safe for minor versions.  
- **Breaking** changes (rename, type change, remove) → new `_vN` export.

### 13.2 Deprecation Policy
- Announce N+1 version availability; **run both** for at least one cycle.  
- Share diffs and migration notes; set a **sunset date**.

### 13.3 Review Checklist
- [ ] Contract updated & docs linked  
- [ ] Staging diff reviewed (row counts, nulls)  
- [ ] DQ metrics unaffected or improved  
- [ ] Policies/labels reviewed (PII exposure unchanged)  
- [ ] Backfill strategy and rollback plan

---

## 14) Tests for Models

- **Schema tests**: required fields, types.  
- **Domain tests**: enum membership, regex validity.  
- **Referential tests**: FK integrity for relationships.  
- **Contract tests**: export schema + SLA.  
- **Regression tests**: distribution drift checks between versions.

```yaml
tests:
  - name: fk_person_org
    type: referential
    from: Person.organization_id
    to: Organization.organization_id
    on_fail: error
```

---

## 15) Collaboration Patterns

- With **Stewards**: agree validations, classifications, dedup rules; co-own glossary.  
- With **Engineers**: design mapping inputs & export outputs; stage & compare.  
- With **Governance**: approvals for PII exports, policy impacts; DPIA inputs.  
- With **Admins**: roles and access for model editors; feature toggles.

**Change cadence:** small PRs, peer review, staging rehearsal, measured rollout.

---

## 16) Common Anti‑Patterns (Avoid)

- **Big‑bang models** aiming to cover all sources before shipping anything.  
- Encoding complex business logic in **mapping** instead of cleaning/exports.  
- **Breaking changes** without versioning and consumer migration.  
- Overusing **free‑text** fields for coded values (lose constraints).  
- Ignoring **temporal** requirements—no way to do point‑in‑time analysis.  
- Missing **source link** fields → poor traceability and incident triage.

---

## 17) Operating Rhythm

**Daily**
- Skim DQ dashboard for your entities; validate last export.  
- Chat with Stewards on new rule breaches; raise PRs for tweaks.

**Weekly**
- Add 1–2 additive attributes or a new relationship.  
- Review export usage & feedback; plan next iteration.

**Monthly**
- Version review: candidates for `_vN` due to breaking needs.  
- Glossary audit; ensure CDEs are complete and accurate.

---

## 18) “What Good Looks Like”

- Canonical model **simple**, well‑documented, and **stable**.  
- Exports **versioned**, with clear contracts and predictable SLAs.  
- **DQ metrics** trending up; few long‑lived red alerts.  
- Consumers can self‑serve because semantics are explicit.  
- Change velocity stays high without breaking downstreams.

---

## 19) Templates & Snippets

### 19.1 Canonical Entity Template
```yaml
entity: <EntityName>
description: "<short purpose>"
keys:
  surrogate: <entity>_id
  natural: []
attributes:
  <field>: { type: string|int|decimal|timestamp|bool, required: false, labels: [], constraints: {} }
relationships: []
labels: []
lineage_fields: [source_system, source_id, source_updated_at]
```

### 19.2 Relationship Bridge (M:M)
```yaml
entity: PersonProduct
keys: { surrogate: person_product_id }
attributes:
  person_id: { type: string, required: true }
  product_id: { type: string, required: true }
  role: { type: string, domain: ["OWNER","VIEWER","BUYER"] }
  valid_from: { type: timestamp }
  valid_to: { type: timestamp }
constraints:
  - fk: { from: person_id, to: Person.person_id }
  - fk: { from: product_id, to: Product.product_id }
```

### 19.3 Export Contract (Ops Wide)
```yaml
name: customers_wide_v1
primary_key: customer_id
delivery: { type: sql-table, schedule: daily }
schema:
  - name: customer_id ; type: string ; required: true
  - name: primary_email ; type: string ; labels: ["PII"]
  - name: total_orders ; type: int
  - name: last_order_at ; type: timestamp
compatibility: additive_only
consumers: ["crm_ops","support_reporting"]
```

### 19.4 Enum Definition
```yaml
enum: order_status
values: ["PENDING","PAID","SHIPPED","CANCELLED","REFUNDED"]
```

### 19.5 Changelog Entry
```yaml
date: "2025-08-24"
change: "Add order_status enum and relationship Person ↔ Organization"
impact: "Enables churn analysis by employer"
links: ["PR#314", "staging diff", "audit event #1578"]
```

---

**Summary:** As a Data Modeller on CluedIn, design minimal but powerful canonical entities, encode semantics, choose the right temporal pattern, and publish consumer‑friendly exports with contracts—then iterate safely. Keep identity, labels, and lineage front‑and‑center, and version any breaking change.

