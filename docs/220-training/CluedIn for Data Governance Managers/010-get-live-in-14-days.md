---
layout: cluedin
title: CluedIn for Data Governance Manager — Operating Manual
parent: Knowledge base
permalink: /kb/cluedin-data-governance-manager
nav_order: 2
---

## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

**Audience:** Data Governance Managers, Chiefs of Data/Privacy, Risk & Compliance leads  
**Goal:** Provide a practical, prescriptive playbook to govern data on CluedIn—policy/controls, ownership, privacy & consent, access & retention, DQ governance, lineage, AI use, audit evidence, and operating cadence.

> This manual is tool-aware (CluedIn), but policy-oriented. It favors governance-as-code, minimal bureaucracy, and measurable outcomes.

---

## 0) Your First 48 Hours (Checklist)

**People & Ownership**
- [ ] Confirm **domain owners** and **data stewards** for top entities (e.g., Person, Organization, Order).
- [ ] Stand up the **Data Governance Council** (DGC) rhythm and RACI.
- [ ] Publish the **use‑case brief** and **policy pack** for day‑1 scope.

**Policy & Access**
- [ ] Approve **classification scheme** (PII/Restricted/Confidential/Public).  
- [ ] Enable **SSO‑only**, group‑based roles, least privilege defaults.  
- [ ] Define **SoD** (Segregation of Duties) and approval thresholds.

**Controls & Observability**
- [ ] Turn on **audit log export** and set retention ≥ your compliance need.  
- [ ] Require **export contracts** and **PII masking policies** by default.  
- [ ] Select **DQ KPIs** and set initial thresholds/alerts.

**Privacy & Retention**
- [ ] Map **legal bases** and **purpose** for PII processing.  
- [ ] Approve **retention schedules** and **deletion/hold** workflows.  
- [ ] Validate **DSR (Data Subject Request)** process with runbook.

---

## 1) Governance Model & Roles

### 1.1 RACI Snapshot
| Area | DGC | Governance Manager | Admin | Data Steward | Data Engineer | Legal/Privacy |
|---|---|---|---|---|---|---|
| Classifications & policies | A/R | R | C | C | C | C/A |
| Roles & access | A/R | R | R | C | C | C |
| DQ KPIs & SLAs | A | R | C | R | R | C |
| Retention & deletion | A | R | C | C | C | R |
| AI guardrails | A | R | C | C | C | R |
| Audit evidence | A | R | C | C | C | C |

*A = Accountable, R = Responsible, C = Consulted*

### 1.2 Governance Objects
- **Classification scheme** (labels/tiers).  
- **Policies** (masking, row/column access, export approvals).  
- **Export contracts** (schema, semantics, SLA).  
- **DQ metrics** & thresholds, **issue register**.  
- **Lineage** and **glossary** (CDEs—Critical Data Elements).  
- **Retention schedule** and **legal hold** register.  
- **AI policy** and **model/agent registry**.

---

## 2) Classification & Policy-as-Code

### 2.1 Standard Labels
```yaml
labels:
  - name: PII
    description: "Personal data subject to privacy rules"
  - name: Restricted
    description: "Sensitive business data; limited access"
  - name: Confidential
  - name: Public
```

### 2.2 Masking & Access Policies (CluedIn-style pseudo)
```yaml
policy: mask_email_default
target: entity:Person.field:email
actions: [read]
effect: allow_with_mask
mask: "partial_email"          # e.g., a***@example.com
unless:
  - role_in: ["Data Steward","Administrator"]
labels_required: ["PII"]
```

```yaml
policy: row_filter_region
target: entity:Order
actions: [read]
effect: allow_when
when: "record.region in user.allowed_regions"
applies_to:
  - roles: ["Analyst","Viewer"]
```

### 2.3 Export Approval for Sensitive Data
```yaml
policy: export_requires_approval
target: export:*
actions: [promote]              # moving to prod
effect: require_approval
when: "export.contains_label('PII') or export.contains_label('Restricted')"
approvers: ["Data Governance Manager","Data Protection Officer"]
```

> **Principle:** Policies must be machine-evaluable, versioned, and reviewed via PRs.

---

## 3) Access Control & Segregation of Duties (SoD)

- **Group to Role** mapping from IdP; no direct user grants unless time-boxed.  
- **Least privilege** defaults; **read-mostly** for wide audiences.  
- **SoD matrix** to prevent a single actor from authoring and approving sensitive changes.

### 3.1 Example SoD
| Action | Allowed | Requires Approval |
|---|---|---|
| Create export with PII | Engineer/Steward | Governance Manager |
| Change masking policy | Admin | Governance Manager + DPO |
| Grant Admin role | Admin | DGC chair approval |
| Create long-lived API token | Admin/Engineer | Governance Manager |

---

## 4) Data Quality Governance

### 4.1 Select KPIs (by entity/CDE)
- **Completeness** (required fields non-null %)  
- **Validity** (regex/domain rules)  
- **Uniqueness** (duplicate rate)  
- **Consistency** (cross-field rules)  
- **Timeliness** (source→export latency)

### 4.2 KPI Template
```yaml
entity: Person
kpis:
  completeness_email: { warn: ">= 0.98", fail: "< 0.95" }
  validity_email_regex: { warn: ">= 0.98", fail: "< 0.95" }
  duplicate_rate_email: { warn: "<= 0.03", fail: "> 0.05" }
alerts:
  - metric: validity_email_regex
    action: "notify #data-quality"
review_cadence: "weekly"
```

### 4.3 Issue Management
- Central **DQ issue register** with owner, ETA, and business impact.  
- **SLAs**: high-severity breach triage within 24h, fix within 7 days or approved waiver.  
- **Evidence**: charts, logs, and audit events linked to each closure.

---

## 5) Privacy, Consent & Purpose Limitation

### 5.1 Legal Bases & Purposes
Maintain a register of **processing purposes** and legal bases (GDPR Art. 6, CCPA/CPRA analogs). Map fields/entities to purposes.

```yaml
purpose: "Customer Support"
legal_basis: "Legitimate Interests"
entities: ["Person","Ticket"]
fields:
  Person.email: ["PII"]
retention: "3 years from last activity"
```

### 5.2 DSR (Access/Deletion/Correction)
- Standard **DSR runbook** with time targets (e.g., 30 days).  
- Use CluedIn search and policies to **locate**, **mask**, or **delete** records.  
- **Soft-delete** first; schedule **hard-delete** post-hold checks.  
- Record **audit trail** for every DSR.

### 5.3 Anonymization & Pseudonymization
- Prefer **masking/hasing** for analytics where possible.  
- Track **re-identification** risk; document controls.

---

## 6) Retention, Deletion & Legal Hold

### 6.1 Retention Schedules
Create per-entity schedules with legal references; encode as policy.

```yaml
policy: retention_person
target: entity:Person
actions: [delete]
effect: schedule_delete
when: "now() > record.last_activity + duration('3 years')"
exceptions:
  - "legal_hold == true"
```

### 6.2 Legal Hold
- Admin can set `legal_hold=true` at entity or export scope.  
- Prevents deletion; logs an **audit event** with case ID.  
- Review holds quarterly with Legal.

### 6.3 Destruction Evidence
- Produce **destruction certificates** with counts, time window, and correlation IDs.  
- Store centrally with retention policy evidence.

---

## 7) Catalog, Glossary & Lineage

### 7.1 Glossary & CDEs
- Each **CDE** has definition, owner, calculation notes, and DQ caveats.  
- Stewards maintain; Governance approves changes.

```yaml
term: "Active Customer"
definition: "Customer with at least one completed order in the last 90 days"
owner: "Sales Ops"
cdes: ["Person.id","Order.completed_at"]
dq_notes: "Exclude orders with status in ('cancelled','fraud')"
```

### 7.2 Lineage & Purview
- Ensure exports are **scannable** by Purview or push **Atlas** lineage after runs.  
- Require lineage for **all prod exports**; no “unknown source” data in BI.

---

## 8) AI Governance on CluedIn

### 8.1 Allowed Uses
- **Read‑only analysis** by Agents on **masked** datasets by default.  
- **Suggestion workflows** (validations, dedup rules) require human approval.  
- **Auto-fix** limited to **deterministic** transformations with rollback.

### 8.2 Guardrails (policy sketch)
```yaml
policy: ai_mask_pii
target: ai:agents
actions: [read]
effect: allow_when
when: "dataset.view == 'masked' and agent.mode in ['analysis','suggest']"
```

- Log **prompts & outputs**; retain for investigation period.  
- Maintain an **AI model/agent registry** with owner, purpose, and data scope.

---

## 9) Audit, Evidence & Compliance

### 9.1 Audit Log Requirements
- Retention ≥ policy (e.g., 3–7 years).  
- Immutable storage (WORM) where mandated.  
- Coverage: SSO events, role grants, token lifecycle, policy changes, export promotions, dedup merges, retention deletes.

**Audit record (illustrative)**
```json
{
  "ts": "2025-08-23T11:02:44Z",
  "actor": "tiw@cluedin.com",
  "action": "policy.update",
  "target": "mask_email_default",
  "old": {"mask": "none"},
  "new": {"mask": "partial_email"},
  "ip": "203.0.113.5",
  "correlation_id": "a6c9-...-4f"
}
```

### 9.2 Control Library & Evidence Plan
- Map **controls → evidence** (log queries, screenshots, configs).  
- Pre‑build **audit packets** (SSO config, RBAC matrices, policy files, retention jobs, DQ dashboards, incident postmortems).

---

## 10) Change Management & Exceptions

- All policy/config changes via **PR** with risk notes and rollback.  
- **CAB/DGC** approves sensitive changes (PII exports, masking off).  
- **Exception register** with owner, expiry, and mitigation; auto‑review cadence.

**Change ticket template**
```yaml
change: "Enable dedup auto-approve @ 0.97 for Person"
risk: "Potential false merges"
mitigation: "Raise reviewer sampling, add unmerge runbook"
rollback: "Set threshold to 1.0; disable auto-approve"
approvers: ["Governance Manager","DPO"]
```

---

## 11) Incident Response (Data Incidents/Breaches)

**Trigger examples**: PII exposure, policy disabled in prod, unauthorized token use, export schema exposing restricted fields.

**Runbook (condensed)**
1. **Identify**: Alert triage, correlation_id, scope quantification.  
2. **Contain**: Re-enable policies, revoke tokens, pause exports.  
3. **Eradicate**: Fix mapping/cleaning/policy root cause.  
4. **Recover**: Backfill corrected outputs; notify consumers.  
5. **Notify**: Legal assesses regulatory notifications (GDPR 72h, etc.).  
6. **Review**: Post-incident with preventive controls & tests.

---

## 12) Operating Cadence

**Weekly DGC (30–45 min)**
- DQ breaches & trends; top 5 risks.  
- Policy changes awaiting approval.  
- Export lineage gaps and consumers onboarded.  
- Retention/DSR stats; exceptions expiring.

**Monthly Governance Review**
- KPI scorecard by domain, audit log sampling results, AI usage review, access recertification outcomes.

**Quarterly**
- Maturity assessment; roadmap; control gap remediation.

---

## 13) KPIs & Scorecard (Examples)

- % CDEs with owner, glossary entry, lineage ✅  
- DQ: completeness/validity at or above threshold for top entities ✅  
- Access: % users via group‑based roles; # exceptions open ↓  
- Privacy: DSR SLA hit rate; # PII exports with approvals ✅  
- Retention: % due-for-delete completed; # holds reviewed ✅  
- AI governance: % agents constrained to masked datasets ✅

```yaml
scorecard:
  cde_coverage: { target: "100%", actual: "92%" }
  pii_export_approvals: { target: "100%", actual: "100%" }
  dsr_sla: { target: ">= 95%", actual: "97%" }
```

---

## 14) Templates & Artifacts

### 14.1 Classification Policy (excerpt)
```yaml
tiers:
  - Public
  - Confidential
  - Restricted
labels:
  PII:
    description: "Personal data"
    defaults:
      mask_read: true
      export_requires_approval: true
```

### 14.2 Export Contract (governance fields)
```yaml
name: contacts_v1
owner: "Sales Ops"
pii: true
approval_ids: ["chg-2025-1032"]
sla:
  freshness_p95_minutes: 60
lineage_required: true
```

### 14.3 Access Request Workflow
```yaml
workflow: request_export_access
steps:
  - submit: requester -> manager_approval
  - review: governance -> approve_or_deny
  - provision: admin -> role_grant(group)
  - audit: evidence_link + expiry_date
```

### 14.4 DPIA Checklist (snapshot)
- Purpose & legal basis documented  
- Data categories & flows mapped  
- Risks & mitigations listed  
- Residual risk accepted by DPO  
- Re‑assessment date set

---

## 15) Maturity Roadmap

**Level 1 → 2**
- Classifications applied to top 3 entities; basic masking; manual approvals.  
- DQ KPIs defined; weekly review established.

**Level 2 → 3**
- Policies as code; PR reviews; automated approvals with conditions.  
- Full lineage coverage; DSR automation; retention jobs live.

**Level 3 → 4**
- Predictive DQ & anomaly detection; auto‑fix playbooks with guardrails.  
- AI agents widely used on masked data; real‑time policy observability.

---

## 16) Quick Reference (Who to Call)

- **Admin:** SSO/RBAC, tokens, feature toggles.  
- **Engineer:** mappings, cleaning, exports, incident on-call.  
- **Steward:** validations, dedup, glossary, labels.  
- **Legal/Privacy:** DPIA, DSR, notifications, holds.  
- **You (Gov Mgr):** policies, approvals, exceptions, audits, council.

---

**Bottom line:** Treat governance as a **product**: versioned configs, small safe changes, clear owners, and measurable outcomes. With CluedIn, encode policies, label data, control access, automate retention, prove lineage, and keep your audit shelf ready.
