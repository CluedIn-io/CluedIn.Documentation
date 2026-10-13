---
title: Private Endpoints
url: https://documentation.cluedin.net/operate/configuration/private-endpoint
content_type: how-to
section: Deploy & operate > Configuration
---

# Private Endpoints

> how-to: Steps to accomplish one task.

CluedIn supports private endpoint connections via an internal load balancer. The architecture below outlines the recommended approach for securely connecting private endpoints to CluedIn.

![Diagram: Client A reaches CluedIn over the internet through a firewall to the internal load balancer; Client B uses private DNS and a private endpoint, connected by Private Link to the internal load balancer in front of CluedIn AKS](https://documentation.cluedin.net/assets/images/paas-operations/private-endpoint.png)

## Key Notes

- A standard load balancer supports **up to eight private links to be associated with it**.
- If your service requires private connectivity for **more than eight private endpoints**, you have the following option:
  - Use a single private link, which can support **up to 1000 private endpoints**.
- Use dedicated subnets for Private Link Services to avoid NSG interference.
- Disable public access on the internal load balancer or AKS ingress.

## Support

If you have any questions about the information in this document, or need assistance with configuration or renewals, please contact **CluedIn Support**.

Up: [Configuration](https://documentation.cluedin.net/operate/configuration.md)
