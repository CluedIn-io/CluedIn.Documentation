---
layout: cluedin
title: Writing data back to operational systems
parent: Knowledge base
permalink: /kb/writing-back-to-operational-systems
nav_order: 2
---

# How to write clean data back to your operational systems

After CluedIn has unified and cleaned your data, you can **write mastered data back** to the systems that run your business. This article covers two proven patterns:

- **Export Targets to generic data backplanes** such as **Azure Event Hubs** and **Azure Service Bus**.  
- **Reverse ETL via the CluedIn Power Automate integration**, giving you access to **1000+ connectors** to write back into SaaS and line‑of‑business apps.

Use these approaches together: publish an authoritative event stream for broad consumption, and use targeted Reverse ETL flows where you must invoke system‑specific APIs or business logic.

---

## When to use which pattern

| Pattern | Use when | Strengths | Considerations |
|---|---|---|---|
| **Event backplane (Event Hubs / Service Bus)** | Many consumers need the same change events (analytics, integration, microservices) | High throughput, decoupled, replayable | Consumers must subscribe and apply changes |
| **Power Automate (Reverse ETL)** | You need to push updates into specific SaaS/LOB systems using native connectors | 1000+ connectors, low/no‑code, retries built‑in | Per‑system flow logic; throughput depends on connector limits |

---

## Architecture at a glance

```
CluedIn (Mastered Changes)
        │
        ├─ Export Target → Azure Event Hubs  → Subscribers (microservices, Synapse, Databricks, Functions)
        │
        └─ Export Target → Power Automate    → 1000+ connectors (Dynamics, Salesforce, ServiceNow, SharePoint, SAP, custom APIs)
```

> Tip: Start by publishing to an event backplane for broad access. Add Power Automate flows for systems that require validated API calls, complex transforms, or approvals.

---

## Prerequisites

- A CluedIn environment with **Export Targets** enabled.  
- Access to **Azure Event Hubs** and/or **Azure Service Bus** (namespace, hub/queue, credentials/Managed Identity).  
- Access to **Microsoft Power Automate** with permission to create flows and use target connectors.  
- A clear definition of **which entity types** and **which changes** you want to publish (e.g., Customer upserts, Address deletes, Product price changes).

---

## Event backplanes with Azure Event Hubs / Service Bus

CluedIn can publish change events (golden record upserts/deletes, property changes, edge changes) to an Azure messaging fabric. Consumers subscribe and apply those changes to their own stores.

### 1) Create an Export Target
1. In CluedIn, go to **Integrations → Export Targets**.  
2. Choose **Azure Event Hubs** (streaming) or **Azure Service Bus** (queue/topic).  
3. Provide **Namespace**, **Hub/Queue/Topic** name, and credentials. Prefer **Managed Identity** or short‑lived SAS tokens.  
4. Select **entity types** to publish (e.g., `Customer`, `Organization`, `Product`) and the **event kinds** (Upsert, Delete).  
5. Set **partition key** (recommended: stable identity such as `entityId` or a composite like `entityType:entityId`).

### 2) Event shape (recommended)
Emit compact, versioned, self‑describing messages.

```json
{
  "specVersion": "cluedin-1.0",
  "eventType": "EntityChanged",        // EntityChanged | EntityDeleted
  "entityType": "Customer",
  "entityId": "cluedin:entity:7f2a...",
  "version": 42,                        // monotonically increasing
  "timestamp": "2025-08-24T03:15:21Z",
  "externalIds": [
    { "system": "crm", "id": "12345" },
    { "system": "billing", "id": "ACME-001" }
  ],
  "changes": {
    "attributes": {
      "name": { "value": "Acme Pty Ltd", "provenance": "crm", "confidence": 0.98 },
      "email": { "value": "ap@acme.com", "provenance": "crm" }
    },
    "edges": [
      { "rel": "billTo", "to": { "externalId": { "system": "erp", "id": "ACME-001" } } }
    ]
  },
  "hash": "sha256:...",
  "previousHash": "sha256:..."
}
```

**Headers (suggested for Service Bus):**
- `messageId`: `${entityType}:${entityId}:${version}` (deduplication)  
- `correlationId`: CluedIn request or pipeline correlation id  
- `contentType`: `application/json`  
- `subject`: `${entityType}.${eventType}`

### 3) Delivery & reliability tips
- **At‑least‑once**: Make consumers idempotent using `messageId` and `version`.  
- **Ordering**: Choose a partition key that keeps related updates together (e.g., `entityId`).  
- **Replay**: Use Event Hubs consumer groups and checkpoints to reprocess. For Service Bus, use sessions and dead‑letter queues.  
- **Filtering**: Publish only fields that downstreams need, or keep full payloads and let consumers select.  
- **PII**: Mask/redact fields not required by consumers. Apply data classification tags for governance.

---

## Reverse ETL via Power Automate (CluedIn integration)

Use CluedIn’s integration with **Power Automate** to call system‑specific connectors (Dynamics 365, Salesforce, ServiceNow, SharePoint, SAP, custom HTTP, etc.).

### 1) Create a Power Automate Export Target
1. In CluedIn, create an **Export Target → Power Automate**.  
2. Choose **which entities and events** to send (e.g., `Customer` upserts).  
3. Copy the **Flow endpoint URL** or connect using the CluedIn Power Automate connector (if available in your tenant).

### 2) Build the flow in Power Automate
- **Trigger**: *When an HTTP request is received* **or** *CluedIn — On entity change*.  
- **Parse JSON**: Use the sample payload above to generate a schema.  
- **Branching**: Use conditions to route by `entityType`, `eventType`, or changed fields.  
- **Actions**: Use target connectors (e.g., *Dynamics 365 — Update a row*, *Salesforce — Upsert record*, *ServiceNow — Update record*, *SharePoint — Create item*, *HTTP — Invoke API*).  
- **Idempotency**: Use `entityId` + `version` as a natural de‑dup key; many connectors support *upsert* based on an external ID.  
- **Error handling**: Configure **retry policies**, **scope** with **run after** on failure, and send alerts to Teams/Email.

**Example mapping (pseudo):**
```
IF eventType == 'EntityChanged' AND entityType == 'Customer':
    Dynamics.UpdateRow(
        table='account',
        key=externalIds['crm'],
        name=changes.attributes.name.value,
        email=changes.attributes.email.value,
        source='CluedIn',
        version=version
    )
```

### 3) Throughput & limits
- Use **concurrency control** in the trigger and action steps.  
- Batch writes where connectors support it; otherwise, shard by `entityType` or route via Event Hubs → Azure Functions → Connector.  
- Respect connector API quotas; enable **per‑flow** and **per‑user** limits as needed.

---

## Best practices

- **Publish only “clean” changes**: filter on golden status, minimum confidence, or approved stewardship state.  
- **Model deletes as tombstones**: send `EntityDeleted` with `entityId`, `version`, and timestamp; let consumers decide physical delete vs. soft‑delete.  
- **Use consistent versions**: monotonic `version` per entity to simplify consumer logic.  
- **Keep provenance**: include `provenance` and `lastSeen` per attribute for auditability.  
- **Protect sensitive data**: apply column‑level masking where not needed downstream; prefer per‑consumer event contracts.  
- **Observability**: capture delivery success rate, dead‑letter counts, consumer lag, connector API errors, and average end‑to‑end latency.  
- **Rollout safely**: canary by entity type or by subset of records; use shadow topics/queues before switching consumers.

---

## Common patterns

### Backplane → Function → System
Use Event Hubs as the single export; **Azure Functions** subscribe, transform, and write to SAP/CRM/ERP with native SDKs or Power Automate webhooks.

### Direct Reverse ETL
For business apps with well‑behaved connectors (Dynamics, Salesforce), send **directly** to Power Automate and upsert into the target object. Keep a control table/log of last pushed `version` per entity in the target for audit and rollback.

---

## Security & governance

- **Authentication**: Use **Managed Identity** for Event Hubs/Service Bus where possible. Store secrets in **Key Vault**.  
- **Authorization**: Scope connectors and SAS tokens to least privilege.  
- **Network**: Restrict namespaces with private endpoints where feasible.  
- **Compliance**: Tag messages with data classification; ensure downstreams inherit retention/DSAR policies.  

---

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Consumers see duplicates | At‑least‑once delivery | Use `messageId` + `version` for idempotency; ignore lower versions |
| Lost ordering for the same entity | Partitioning by a non‑stable key | Partition by `entityId`; enable sessions (Service Bus) |
| Connector throttling (429/5xx) | API limits | Enable retries with backoff, add concurrency caps, batch where supported |
| Flow runs succeed but target doesn’t change | Wrong key mapping | Verify external ID used for upsert; log target response IDs |
| PII leakage to broad consumers | Over‑rich event payload | Publish per‑consumer schemas; mask unnecessary attributes |

---

## FAQ

**Can I publish only approved stewarded changes?**  
Yes. Filter on stewardship state or confidence before emitting to the Export Target.

**What about bi‑directional sync?**  
Treat inbound changes from operational systems as new facts; CluedIn re‑masters and emits a new version. Avoid blind echo loops by checking `provenance` or `version` before writing back.

**Do I need both Event Hubs and Power Automate?**  
Not always. Use Event Hubs for broad distribution and analytics; add Power Automate when you must call specific application connectors or orchestrate approvals.

---

## Quick start checklists

**Event Hubs / Service Bus**
- [ ] Export Target created with correct namespace & hub/queue/topic  
- [ ] Partition key = `entityId` (or stable composite)  
- [ ] Message headers set (`messageId`, `subject`, `correlationId`)  
- [ ] Consumer checkpoints configured; dead‑letter monitored

**Power Automate**
- [ ] Flow trigger wired to CluedIn export (HTTP or connector)  
- [ ] Parse JSON step with validated schema  
- [ ] Upsert action mapped to correct external ID  
- [ ] Retry and alerting configured; concurrency tuned

---

### Summary

- Use **Azure Event Hubs / Service Bus** Export Targets to publish a high‑quality, replayable stream of mastered changes.  
- Use **Power Automate (Reverse ETL)** to push clean data into operational systems via **1000+ connectors** with minimal code.  
- Design for **idempotency, ordering, security, and observability** so downstream systems remain accurate and auditable.
