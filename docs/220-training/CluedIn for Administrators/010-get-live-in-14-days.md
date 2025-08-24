---
layout: cluedin
title: CluedI For Administrators
parent: Knowledge base
permalink: /kb/cluedin-for-administrators
nav_order: 2
---

# CluedIn for Administrators — The Practical Handbook

**Audience:** Platform admins, security engineers, data platform owners  
**Goal:** Give administrators a clear, actionable view of how to operate CluedIn securely at scale—identity, access, integrations, features, observability, and governance.

> This handbook focuses on *how* to run CluedIn day-to-day and *what good looks like*. It includes checklists, templates, and examples you can adapt to your environment.

---

## 0) Your First 48 Hours (Checklist)

**Identity & Access**
- [ ] Configure SSO (OIDC or SAML 2.0).  
- [ ] (Optional) Enable **SCIM** user/group provisioning.  
- [ ] Map **IdP groups → CluedIn roles** (least privilege).  
- [ ] Enforce **SSO-only** sign-in and MFA at your IdP.

**Access Control & Security**
- [ ] Review **built-in roles** and create **custom roles** as needed.  
- [ ] Define **data access policies** using classifications/labels (PII, Restricted).  
- [ ] Set **session timeout** and **token lifetimes**.  
- [ ] Create **API tokens** with minimal scopes; store secrets centrally.

**Features & Integrations**
- [ ] Turn on only the features you need for day‑1; keep others off.  
- [ ] Connect Microsoft **Purview** (catalog/lineage) via scanning or push.  
- [ ] Connect **Power Automate/Power Apps** to CluedIn APIs or webhooks.  
- [ ] (Optional) Configure **AI** integrations/AI Agents with guardrails.

**Observability**
- [ ] Decide your **log retention** strategy; export logs to your SIEM.  
- [ ] Enable **audit log** export and alerts on high‑risk events.  
- [ ] Create an **Admin dashboard**: pipeline health, ingestion/export SLAs.  
- [ ] Document a **runbook** and an **incident response** checklist.

---

## 1) Identity, SSO & Provisioning

CluedIn supports enterprise SSO via **OIDC** or **SAML 2.0** and optional **SCIM** for provisioning.

### 1.1 OIDC (OpenID Connect) Setup

**In your IdP (e.g., Microsoft Entra ID / Okta)**
1. Register a **Web** application.  
2. Set the **redirect URI** to your CluedIn callback (from CluedIn SSO settings).  
3. Issue a **Client ID** and **Client Secret**.  
4. Add **scopes/claims** you need mapped to roles and groups (e.g., `email`, `name`, `groups`).  
5. Assign users/groups to the app.

**In CluedIn → Admin → Authentication**
```json
{
  "type": "oidc",
  "issuer_url": "https://login.microsoftonline.com/<tenant>/v2.0",
  "client_id": "<CLIENT_ID>",
  "client_secret": "<CLIENT_SECRET>",
  "redirect_uri": "https://<your-cluedin-host>/auth/oidc/callback",
  "scopes": ["openid","profile","email","groups"],
  "group_claim": "groups",
  "enforce_sso_only": true
}
```

> **Tip:** Prefer OIDC where possible—simpler operations, modern token formats, and easy group claims.

### 1.2 SAML 2.0 Setup

**In your IdP**
- Create a **SAML** application.  
- Upload the **SP metadata** (from CluedIn) or configure the **ACS** (Assertion Consumer Service) URL manually.  
- Map attributes: `email`, `firstName`, `lastName`, and a **group attribute** (e.g., `memberOf`).  
- Download **IdP metadata** (XML).

**In CluedIn → Admin → Authentication**
```xml
<!-- Paste IdP Metadata -->
<EntityDescriptor entityID="https://idp.example.com/metadata">
  <!-- ... -->
</EntityDescriptor>
```
```json
{
  "type": "saml2",
  "acs_url": "https://<your-cluedin-host>/auth/saml/acs",
  "entity_id": "https://<your-cluedin-host>/auth/saml/metadata",
  "email_attribute": "email",
  "groups_attribute": "memberOf",
  "enforce_sso_only": true
}
```

### 1.3 Group-to-Role Mapping

Map IdP groups to CluedIn roles. Keep mappings in **code/config** for repeatability.

```yaml
# cluedin-role-mapping.yaml
mappings:
  - idp_group: "cluedin-admins"
    roles: ["Administrator"]
  - idp_group: "cluedin-data-engineers"
    roles: ["Data Engineer"]
  - idp_group: "cluedin-stewards"
    roles: ["Data Steward"]
  - idp_group: "cluedin-viewers"
    roles: ["Viewer"]
defaults:
  # Users with SSO but no mapped group get these roles (or none)
  roles: ["Viewer"]
```

> **Least privilege:** give broad read where required, but restrict write/config permissions to a small, accountable set.

### 1.4 SCIM Provisioning (Optional)

Enable SCIM to automate user/group lifecycle:
- **Create/Update/Deactivate** users in CluedIn based on IdP.  
- Sync **group membership** so role mappings stay current.

**IdP → SCIM config (example)**
```json
{
  "scim_base_url": "https://<your-cluedin-host>/scim/v2",
  "bearer_token": "<SCIM_PROVISIONING_TOKEN>",
  "sync_interval_minutes": 15
}
```

**Operational tips**
- Treat SCIM like code: change via PR, audit regularly.  
- Test **deprovisioning**; confirm tokens and sessions are revoked.

---

## 2) Connecting Systems: Purview, Power Automate, Power Apps, AI

### 2.1 Microsoft Purview (Catalog & Lineage)

You have two main patterns—pick one (or both):

1) **Scan exports** that CluedIn writes to your lake/warehouse.  
   - Register the storage/database in Purview.  
   - Schedule scans so Purview catalogs the **tables/files** produced by CluedIn.  
   - Pro: simple, no custom code. Con: lineage may be coarse.

2) **Push lineage/metadata** into Purview (Atlas-compatible APIs).  
   - Use a job to publish **processes/entities/lineage** after your exports run.  
   - Pro: explicit lineage from **source → CluedIn → export**. Con: you own jobs.

**Minimal lineage push (pseudo)**
```json
POST https://<purview-account>/api/atlas/v2/lineage
{
  "process": {
    "typeName": "cluedin_export",
    "attributes": {
      "name": "warehouse-contacts-v1",
      "qualifiedName": "cluedin.export.warehouse-contacts-v1"
    }
  },
  "inputs": [{"qualifiedName": "cluedin.entity.Person"}],
  "outputs": [{"qualifiedName": "sql.mdm.contacts_v1"}]
}
```

### 2.2 Power Automate (Flows) & Power Apps

**Pattern A — Call CluedIn APIs from a Flow**
- Use **HTTP** action with OAuth2 or PAT (preferred: OAuth client).  
- Trigger on events (e.g., a new record in Dataverse) → call **CluedIn ingestion endpoint** or **AI Agent**.

```http
POST https://<your-cluedin-host>/api/ingest/crm-contacts
Authorization: Bearer <ACCESS_TOKEN>
Content-Type: application/json

{"id":"c_123","email":"a@example.com","updated_at":"2025-08-22T12:00:00Z"}
```

**Pattern B — Webhooks from CluedIn → Flow**
- Register a **webhook** in CluedIn (on export success, DQ alert, dedup queue event).  
- The Flow receives the payload and notifies Teams/updates a ticket/starts approvals.

**Pattern C — Power Apps UI + CluedIn APIs**
- Build a simple app for **data stewarding** (approve merges, fix invalids).  
- Use a service principal for API access and enforce **role checks** server-side.

### 2.3 AI Integrations

- Configure your **AI provider** (e.g., Azure OpenAI) in CluedIn AI settings.  
- Scope **what entities** and **fields** AI Agents can read/write.  
- Restrict PII access, enable **redaction/masking** for prompts and logs.  
- Start with **read-only** analysis Agents; expand to suggestion/auto-fix flows after review.

---

## 3) Turning Features On/Off

Navigate to **Admin → Features** (or **Workspace Settings → Features**).

**Best practices**
- Keep **non-essential** features **off** until you need them.  
- Maintain separate **dev/test/prod** workspaces.  
- Use **change windows** and a **rollback plan** for feature toggles.  
- Document **compatibility** (some features require certain roles/integrations).

**Example (pseudo)**
```json
{
  "features": {
    "ai_agents": true,
    "dedup_projects": true,
    "experimental_mappers": false,
    "webhooks": true,
    "custom_roles": true
  }
}
```

---

## 4) Access Control for Data

CluedIn uses **RBAC** (roles → permissions) and can layer **policy‑based** controls for **row/column** access (ABAC-style).

### 4.1 Levels of Control
- **Workspace/project level:** who can configure ingestion, mapping, cleaning, exports.  
- **Entity/Dataset level:** who can read/write specific entities or exports.  
- **Field/Column level:** mask, hash, or hide selected attributes (e.g., PII).  
- **Row level:** filter rows by attributes (region, tenant, ownership).

### 4.2 Example Policies

**Column masking**
```yaml
policy: mask_pii_email
target: entity:Person.field:email
actions: [read]
effect: allow_with_mask
mask: "partial_email"  # e.g., a***@example.com
conditions:
  - role_in: ["Viewer","Analyst"]
```

**Row-level filter**
```yaml
policy: restrict_region
target: entity:Order
actions: [read]
effect: allow_when
when: "record.region in user.allowed_regions"
applies_to:
  - roles: ["Analyst"]
  - groups: ["finance-emea"]
```

**Deny write to exports for non-owners**
```yaml
policy: export_write_guardrail
target: export:mdm.contacts_v1
actions: [write,configure]
effect: deny
unless:
  - role_in: ["Administrator","Data Engineer"]
```

> **Order of evaluation:** explicit **deny** should override broad allows; test with staging identities.

### 4.3 Classifications & Tags

Apply **labels** (`PII`, `Restricted`, `Confidential`, `Public`) at the entity/field level and drive policies from labels:
- Auto-mask `PII` for non‑steward roles.  
- Require **approval** for exports that include `Restricted` fields.

---

## 5) Managing API Tokens

CluedIn supports **Personal Access Tokens (PATs)** and/or **OAuth clients** for service‑to‑service access.

### 5.1 Creating Tokens
- Go to **Admin → API Tokens**.  
- Create a token with the **minimal scopes** and a **short expiry**.  
- Tag tokens by **purpose** (`power-automate-flow-42`).

**Token example (pseudo)**
```json
{
  "name": "power-automate-contact-sync",
  "scopes": ["ingest:write","export:read"],
  "expires_at": "2025-12-31T23:59:59Z"
}
```

**Usage**
```bash
curl -H "Authorization: Bearer <TOKEN>" https://<host>/api/exports/status
```

### 5.2 Rotation & Hygiene
- Rotate on a **90‑day** cadence (or faster).  
- Revoke tokens immediately on **user departure** (SCIM + audit).  
- Keep secrets in a **vault**; never in code or chat.  
- Log **who/what** uses tokens (user agent, IP), alert on anomalies.

---

## 6) Reading Logs

CluedIn exposes logs across categories; forward them to your SIEM/Observability stack for long‑term analytics.

### 6.1 Types
- **Ingestion logs:** HTTP status, schema/parse issues, dead‑letter entries.  
- **Mapping & cleaning logs:** transformation steps, validation failures.  
- **Export logs:** schedule triggers, job durations, row counts, schema diffs.  
- **System logs:** auth, feature toggles, config changes.

**Example log (pseudo)**
```json
{
  "ts": "2025-08-23T10:15:08Z",
  "category": "export",
  "export": "warehouse-contacts-v1",
  "status": "success",
  "duration_ms": 4213,
  "records_out": 15234,
  "correlation_id": "a6c9-...-4f",
  "actor": "system@scheduler"
}
```

### 6.2 Practical Use
- Always capture **correlation_id** from UI/API; thread it through pipelines.  
- Build alerts for **error rate** spikes and **duration** regressions.  
- Keep **log levels** sane in prod; switch to debug only during incidents.

---

## 7) Reading Audit Logs

Audit logs track **who did what, when, and from where**—critical for compliance.

**Common events**
- SSO sign‑ins, failed logins.  
- Role/permission changes; token creation/revocation.  
- Feature toggles; workspace settings changes.  
- Policy updates; data export configuration changes.  
- Bulk actions (dedup merges, cleaning jobs with write effects).

**Sample audit record (pseudo)**
```json
{
  "ts": "2025-08-23T11:02:44Z",
  "actor": {"type":"user","id":"tiw@cluedin.com"},
  "action": "role.update",
  "target": {"type":"role","id":"Data Steward"},
  "old": {"permissions":["entity.read","dq.view"]},
  "new": {"permissions":["entity.read","dq.view","dedup.review"]},
  "ip": "203.0.113.5"
}
```

**Best practices**
- Export audit logs daily; retain for **1–7 years** per policy.  
- Monitor **high‑risk** actions (token create, role grant, export schema change).  
- Automate **tickets/approvals** for sensitive actions.

---

## 8) Controlling Access to Functionality (Roles & Users)

Start with **built‑in roles** and add **custom roles** only when needed.

### 8.1 Example Permission Matrix (excerpt)
| Capability | Viewer | Data Steward | Data Engineer | Administrator |
|---|---:|---:|---:|---:|
| Read entities/exports | ✅ | ✅ | ✅ | ✅ |
| Approve dedup merges | ❌ | ✅ | ✅ | ✅ |
| Edit cleaning projects | ❌ | ✅ (limited) | ✅ | ✅ |
| Configure ingestion/export | ❌ | ❌ | ✅ | ✅ |
| Manage roles & policies | ❌ | ❌ | ❌ | ✅ |
| Manage feature toggles | ❌ | ❌ | ❌ | ✅ |
| Create API tokens | ❌ | ❌ | ✅ (scoped) | ✅ |

> Use **scoped custom roles** to carve out precise abilities (e.g., “Export Maintainer” can edit exports in project `sales`, but nowhere else).

### 8.2 Custom Role Definition (template)
```yaml
role: "Export Maintainer"
description: "Manage exports for Sales project only"
permissions:
  - export.read:project:sales
  - export.write:project:sales
  - policy.read
constraints:
  - deny: ["feature.toggle","role.manage"]
```

### 8.3 Change Management
- Approvals for **role grants** beyond Viewer/Steward.  
- **Time‑boxed** elevated roles (auto‑expire admin for break‑glass).  
- Quarterly **access reviews** with audit evidence.

---

## 9) Operational Runbooks

**Daily**
- Check **pipeline health** (last run status, latency, volumes).  
- Review **alerts** (ingestion failures, DQ thresholds).  
- Triage **dedup review queues** (if enabled).

**Weekly**
- Review **audit log highlights** and **token usage**.  
- Patch/rotate **secrets** and **service principals** as needed.  
- Validate **Purview** lineage completeness for top datasets.

**Monthly**
- Access reviews; role/permission drift check.  
- Capacity planning (storage/compute) and cost review.  
- Disaster recovery **tabletop**: restore from backup or re‑build exports.

**Incident (example)**
1. **Identify**: Error rate spike on export, correlation_id `X`.  
2. **Contain**: Pause affected schedules; toggle feature if implicated.  
3. **Diagnose**: Compare config (`git/PR`), check last mapping/cleaning changes.  
4. **Remediate**: Rollback mapping or re-run cleaning; backfill export.  
5. **Review**: Post‑incident notes; add alert/test; update runbook.

---

## 10) Security & Compliance Quick Wins

- Enforce **SSO-only** and **MFA** at IdP.  
- Use **least-privilege** roles; prefer **group-based** access.  
- **Mask PII** by default; require approvals to export PII.  
- **Short-lived** tokens; rotate frequently; monitor token use.  
- **Immutable audit logs** with long retention.  
- **Secrets in a vault**, never in pipelines or notebooks.  
- **Data residency** and **encryption**: document and validate with your infra team.

---

## Appendix A — SSO Attribute Mapping (examples)
```yaml
attributes:
  email: "user.email || user.userprincipalname"
  first_name: "user.given_name"
  last_name: "user.family_name"
  groups: "user.groups"  # or saml:memberOf
```

## Appendix B — SCIM Field Mapping (examples)
```yaml
user:
  id: "id"
  userName: "mail"
  active: "accountEnabled"
  name.givenName: "givenName"
  name.familyName: "surname"
  emails[0].value: "mail"
group:
  displayName: "displayName"
  members[].value: "members[].id"
```

## Appendix C — Power Automate Flow (HTTP) Sketch
```yaml
trigger: "When a row is added in Dataverse"
steps:
  - name: Compose payload
    action: compose
    inputs:
      id: "@{triggerBody()?['contactid']}"
      email: "@{triggerBody()?['emailaddress1']}"
      updated_at: "@{utcNow()}"
  - name: POST to CluedIn
    action: http
    inputs:
      method: POST
      uri: "https://<host>/api/ingest/crm-contacts"
      headers:
        Authorization: "Bearer @{parameters('CLUE_TOKEN')}"
        Content-Type: "application/json"
      body: "@{outputs('Compose payload')}"
```

## Appendix D — Sample Policies (copy/paste)

**D1. Require approval for exports with PII**
```yaml
policy: export_pii_guard
target: export:*   # any export
actions: [promote]
effect: require_approval
when: "export.contains_label('PII')"
approvers: ["Data Protection Officer","Administrator"]
```

**D2. Deny field read of government_id to all but Stewards/Admins**
```yaml
policy: hide_government_id
target: entity:Person.field:government_id
actions: [read]
effect: deny
unless:
  - role_in: ["Data Steward","Administrator"]
```

**D3. Limit AI access to masked views**
```yaml
policy: ai_masking
target: ai:agents
actions: [read]
effect: allow_when
when: "agent.mode == 'analysis' and dataset.view == 'masked'"
```

---

## Final Notes

- Keep **configuration as code** (YAML/JSON in a repo) where possible to enable PR reviews, versioning, and quick rollbacks.  
- Separate **people permissions** (roles) from **data policies** (labels/rules); you’ll evolve both independently.  
- Start with **simple** integrations and tighten controls as you scale.

---

**You’ve now got the admin view:** set up identity, connect the Microsoft ecosystem, control features and data access, run with observability, and govern with audit + policy. Clone the templates, fill in your env details, and you’re production‑ready.
