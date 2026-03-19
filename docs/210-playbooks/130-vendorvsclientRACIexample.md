# Example of CluedIn vs Client RACI responsibilities matrix

**Assumption:** this version is for a **CluedIn-led implementation with no SI partner** and assumes **PaaS/customer-managed Azure** unless noted otherwise.

**Legend:** A = Accountable, R = Responsible, C = Consulted, I = Informed

| Workstream / Activity                                                                 | CluedIn | Client |
| ------------------------------------------------------------------------------------- | ------- | ------ |
| Program governance, delivery cadence, backlog, sprint planning                        | R       | A      |
| Business objectives, scope, use-case prioritization, success criteria                 | C       | A/R    |
| Target-state architecture and deployment model choice                                 | R       | A      |
| Enterprise architecture review, security review, GDPR/legal/procurement approvals     | C       | A/R    |
| Azure subscription readiness, quotas, RBAC, networking, policies, DNS/firewall (PaaS) | C       | A/R    |
| CluedIn installation, baseline platform setup, default environment configuration      | A/R     | C      |
| SSO enablement and role model mapping                                                 | R       | A      |
| Environment operations baseline (backup, monitoring, upgrades, supported config)      | A/R     | C/I    |
| Canonical data model, vocabularies, vocabulary keys, business-domain design           | R       | A      |
| Source-system access, extract readiness, source SMEs, sample data provision           | C       | A/R    |
| Ingestion pipelines, mappings, endpoints/crawlers, initial connectivity               | A/R     | C      |
| Data quality rules, validation logic, cleansing automation                            | R       | A      |
| Matching, deduplication, survivorship / golden-record behavior                        | R       | A      |
| Enrichment design and third-party reference-data hookup                               | R       | A/C    |
| Outbound integrations, streams, export targets, API/query enablement                  | R       | A/C    |
| Migration / initial load / reconciliation approach                                    | R       | A      |
| SIT / technical testing / defect fixing of configuration and integrations             | A/R     | C      |
| UAT, business validation, acceptance sign-off                                         | C       | A/R    |
| Cutover planning and go-live approval                                                 | R       | A      |
| Production deployment execution / go-live support                                     | A/R     | C      |
| Training, runbooks, admin enablement, handover documentation                          | R       | A      |
| Hypercare and L2/L3 platform support                                                  | A/R     | I/C    |
| Ongoing stewardship, source-data remediation, business ownership of mastered data     | C       | A/R    |
| Continuous improvement roadmap and future use-case expansion                          | R       | A      |

### What this means in plain English

**CluedIn should own the product-heavy work.**
That includes platform installation, technical onboarding, ingestion setup, data-model implementation, rule configuration, dedup/survivorship setup, export/stream/API enablement, training, handover, and hypercare. Internally, CluedIn’s implementation deck explicitly puts Delivery Manager, Data Implementation Engineers, Global Operations, and Product Engineers around setup, ingestion, deployment to PROD, training/handover, and transition to support. The deck also shows the implementation journey as a joint process from welcome/setup through delivery, live/handover, and support. 

**The client should own the business and enterprise-control work.**
That includes business goals, use-case prioritization, business-rule sign-off, source-system access, enterprise architecture/security/legal/procurement approvals, UAT, go-live approval, and ongoing stewardship. Recent CluedIn RFx material says successful implementations need customer-side roles such as Product Owner / Business Data Owner, Data Architect, Data Engineer, and Data Steward, and states that CluedIn typically runs a cross-functional RACI early around domain ownership, change control, and integration responsibilities. 

**For PaaS, the client owns the Azure foundation; CluedIn owns the platform on top of it.**
CluedIn’s public docs say the PaaS installation process must be carried out by a customer Azure Administrator with the right Azure permissions, quota, network planning, and readiness steps. The same docs also say CluedIn can handle most of the operational heavy lifting once the operations team has access, including post-installation, upgrades, backups, and monitoring. Public support-scope docs also make clear that unsupported infra deviations are out of support, so the customer should stay accountable for Azure guardrails while CluedIn stays accountable for supported CluedIn configuration and operations. ([CluedIn Documentation][2])

**Data modeling, configuration, integration, and migration are shared — but not equally.**
CluedIn’s docs make it clear that the platform’s data model is built through vocabularies and vocabulary keys, rules automate business logic and data transformation, streams/export targets push mastered data out, and GraphQL provides flexible pull/query access. That strongly supports a split where **CluedIn is responsible for building/configuring the mechanics**, while the **client is accountable for defining the business meaning, target-state behavior, and acceptance criteria**. ([CluedIn Documentation][3])

### Two important caveats

**1) If the deal is Private SaaS or SaaS, shift several infra rows toward CluedIn.**
In SaaS/Private SaaS, CluedIn takes more ownership for the environment itself. The client still remains accountable for identity decisions, business rules, source access, UAT, and data stewardship. The docs explicitly note that SSO applies to both PaaS and SaaS, but in SaaS the final enablement step is completed by CluedIn support. ([CluedIn Documentation][1])

**2) If an SI partner is involved, many “R” tasks move from CluedIn to the SI.**
That is especially true for integration build, migration factory work, and some rollout/change-management tasks. CluedIn should then stay **A/C** on product-specific design, supported configuration, and L2/L3 product support. That also lines up with the older internal three-party roles template, which separated CluedIn, Partner, and Customer responsibilities rather than forcing CluedIn to own every delivery task. 
