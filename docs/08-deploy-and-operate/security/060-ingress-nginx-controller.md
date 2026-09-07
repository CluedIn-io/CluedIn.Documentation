---
layout: cluedin
title: Ingress NGINX vulnerabilities (not impacted)
parent: Security
grand_parent: Deploy & operate
nav_order: 60
permalink: /operate/security/ingress-nginx-controller
content_type: reference
redirect_from: ["/kb/ingress-nginx-controller"]
source_path: docs/200-kb/kb1004-ingress-nginx.md
tags: ["security"]
last_modified: 2025-03-25
---

[Wiz Research](https://www.wiz.io/blog/ingress-nginx-kubernetes-vulnerabilities) recently disclosed a series of critical unauthenticated Remote Code Execution (RCE) vulnerabilities affecting the Ingress NGINX Controller in Kubernetes (CVE-2025-1097, CVE-2025-1098, CVE-2025-24514, and CVE-2025-1974), collectively known as _IngressNightmare_. These vulnerabilities could allow attackers to execute arbitrary code and gain unauthorized access to Kubernetes secrets across namespaces. More information can be found in:

- [Infosecurity Magazine](https://www.infosecurity-magazine.com/news/ingressnightmare-critical-bugs-40/)

- [The Hacker News](https://thehackernews.com/2025/03/critical-ingress-nginx-controller.html)

{:.important}
CluedIn is not impacted by these vulnerabilities, as we do not use NGINX as our ingress controller. Instead, CluedIn relies on HAProxy, which is not affected by these issues.

If you have deployed CluedIn using the standard setup, you are not impacted. However, customers who have modified their Ingress setup outside of CluedIn's recommended configuration should review their infrastructure and apply any necessary security updates.

Our security team continuously monitors emerging threats and ensures that CluedIn remains secure. For any questions or further assistance, contact CluedIn support team at [support@cluedin.com](mailto:support@cluedin.com).