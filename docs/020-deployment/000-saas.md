---
layout: cluedin
title: CluedIn SaaS
parent: Installation
permalink: /deployment/cluedin-saas
nav_order: 1
has_children: false
headerIcon: "saas"
---

Getting started with CluedIn SaaS is fast, simple, and fully self-service. Whether you’re evaluating the platform or ready to operationalize your data, the onboarding and subscription process is designed to be frictionless and transparent.

---

### **Sign Up**

You can create your CluedIn SaaS account directly through our onboarding portal at  
**[https://landing.cluedin.com/signup](https://landing.cluedin.com/signup)**.  
The sign-up flow guides you through selecting the package that best matches your needs, and deployment begins immediately after registration. No lengthy setup or complex procurement steps are required.

---

### **Billing**

CluedIn SaaS includes a built-in payment module that allows you to complete your purchase by **credit card**, with charges billed **monthly**. This provides a straightforward and flexible way to manage your subscription as your usage grows.  
You can explore all available plans and pricing details at:  
**[https://www.cluedin.com/saas-pricing](https://www.cluedin.com/saas-pricing)**

---

### **Yearly Commitments**

If your organization prefers an annual commitment or requires custom commercial terms, our sales team is happy to help. To discuss yearly pricing, procurement requirements, or enterprise agreements, you can reach out via:  
**[https://www.cluedin.com/discovery-call](https://www.cluedin.com/discovery-call)**

### **Tenant Isolation**

CluedIn SaaS is a multi-tenant service. Some underlying infrastructure and databases are shared between customers, while each tenant’s data remains logically and cryptographically isolated.

Every request and background operation in CluedIn runs within a tenant-specific **Execution Context**. The Execution Context identifies the tenant performing the operation and automatically applies tenant-level filters whenever data is read, written, searched, processed, or exported. Application code cannot access data without operating within this context.

Each tenant is also assigned its own private cryptographic keys. These keys are unique to the tenant and provide an additional isolation boundary. Even if an operation attempted to reference data belonging to another tenant, the tenant filters would prevent the data from being retrieved, and the requesting tenant would not possess the keys required to access it.

This provides multiple layers of tenant isolation:

- **Tenant-scoped execution:** Every application operation is associated with a specific tenant.
- **Automatic data filtering:** The application layer automatically restricts database operations to the active tenant.
- **Tenant-specific cryptographic keys:** Each tenant has a separate set of private keys.
- **Fail-closed access:** Requests that do not match the active tenant context are rejected rather than returning data.
- **Consistent enforcement:** Tenant isolation applies to interactive requests, APIs, background jobs, and data-processing operations.

This architecture allows CluedIn SaaS to benefit from securely managed shared infrastructure while preventing one tenant from reading or operating on another tenant’s data.

### AKS workload boundaries

CluedIn SaaS workloads run on Microsoft Azure Kubernetes Service.

The SaaS service uses a shared AKS infrastructure. Kubernetes namespaces and worker nodes should therefore not be interpreted as the primary security boundary between customer organisations.

Tenant isolation is principally enforced through the CluedIn application, identity, encryption, authorisation, and data-access layers.

Within the Kubernetes environment, CluedIn uses workload-separation controls that may include:

- Kubernetes namespaces to organise and separate platform workloads
- Dedicated Kubernetes service accounts and workload identities
- Role-based access control for administrative and service operations
- Kubernetes network controls and restricted service exposure
- Separation of application components according to their operational responsibilities
- Controlled access to secrets and encryption-key material
- Resource requests, limits, and scaling policies
- Restricted administrative access to the AKS environment

Customer users do not receive direct access to the underlying:

- AKS cluster
- Kubernetes API
- Pods
- Worker nodes
- Namespaces
- Platform service accounts

Where a customer requires dedicated compute, networking, databases, or a dedicated Kubernetes environment as a contractual security requirement, CluedIn Private SaaS or CluedIn PaaS should be considered instead of the shared multi-tenant SaaS service.

### Identity and access isolation

User access is scoped to an organisation and governed by CluedIn's authentication and authorisation controls.

These controls include:

- Organisation membership validation
- Role-based access control
- Feature-level and data-level permissions
- Server-side authorisation for application and API requests
- Isolation of organisation-specific API credentials and tokens
- Validation of tenant context for service-to-service operations

A user must be both authenticated and authorised within the relevant organisation before tenant data can be accessed.

### Background processing and messaging

Asynchronous processing is tenant-aware.

Messages, scheduled jobs, ingestion operations, workflows, and other background activities retain the organisation context under which they were created.

Workers validate this context before loading or updating data. This prevents a background process created for one organisation from operating against another organisation's data.

Operational controls are also used to manage workload distribution and reduce the possibility that unusually high activity from one tenant adversely affects other tenants.

### Cache and search isolation

Cached and indexed information is associated with the relevant organisation context.

Cache keys, search queries, and index operations include tenant-scoping information so that results belonging to one organisation are not returned to another.

Tenant filtering is applied server-side and does not depend on filtering performed by the browser or another client application.

### Network and service protection

The CluedIn SaaS environment uses Azure and Kubernetes security controls to limit access to internal services and persistence components.

These controls include:

- TLS encryption for data in transit
- Restricted exposure of internal platform services
- Network access controls between platform components
- Controlled access to databases, storage, messaging, caching, and search services
- Managed identities or protected service credentials for service-to-service access
- Centralised management of secrets and sensitive configuration
- Monitoring of administrative and service activity

Underlying persistence services are not directly exposed to customer users.

### Operational access

Access by CluedIn personnel to production systems is restricted to authorised personnel with an operational requirement.

Administrative access is governed through access-control procedures and is designed to be attributable to an individual identity.

Production access, security events, and relevant platform activity are logged and monitored in accordance with CluedIn's security and compliance processes.

