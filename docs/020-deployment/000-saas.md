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

### Tenant Isolation

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
