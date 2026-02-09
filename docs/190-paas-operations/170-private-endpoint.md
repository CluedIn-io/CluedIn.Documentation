---
layout: cluedin
title: Private Endpoints
parent: PaaS operations
permalink: /paas-operations/private-endpoint
nav_order: 17
tags: ["private endpoints", "private links"]
headerIcon: "paas"
---

CluedIn supports private endpoint connections via an internal load balancer. The architecture below outlines the recommended approach for securely connecting private endpoints to CluedIn.

![private-endpoint.png]({{ "/assets/images/paas-operations/private-endpoint.png" | relative_url }})

## Key Notes

- A standard load balancer supports **up to eight private links per frontend IP**.
- If your service requires private connectivity for **more than eight private endpoints**, you have the following options:
  - Add an additional frontend IP to the load balancer. Each frontend IP supports up to eight private links.
  - Use a single private link, which can support **up to 512 private endpoints**.
- Use dedicated subnets for Private Link Services to avoid NSG interference.
- Disable public access on the internal load balancer or AKS ingress.

## Support

If you have any questions about the information in this document, or need assistance with configuration or renewals, please contact **CluedIn Support**.
