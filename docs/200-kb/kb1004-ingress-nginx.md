---
layout: cluedin
title: CluedIn Security - [NOT impacted] Ingress NGINX Controller vulnerabilities
permalink: /kb/ingress-nginx-controller
parent: Knowledge base
tags: ["security"]
last_modified: 2025-03-25
nav_order: 6
---

[Wiz Research](https://www.wiz.io/blog/ingress-nginx-kubernetes-vulnerabilities) recently disclosed a series of critical unauthenticated Remote Code Execution (RCE) vulnerabilities affecting the Ingress NGINX Controller in Kubernetes (CVE-2025-1097, CVE-2025-1098, CVE-2025-24514, and CVE-2025-1974), collectively known as **IngressNightmare**. These vulnerabilities could allow attackers to execute arbitrary code and gain unauthorized access to Kubernetes secrets across namespaces. More information can be found in [Infosecurity Magazine](https://www.infosecurity-magazine.com/news/ingressnightmare-critical-bugs-40/) and [The Hacker News](https://thehackernews.com/2025/03/critical-ingress-nginx-controller.html).

{:.important}
CluedIn is not impacted by these vulnerabilities, as we do not use NGINX as our ingress controller. Instead, CluedIn relies on HAProxy, which is not affected by these issues.

If you have deployed CluedIn using our standard setup, you are not impacted. However, customers who have modified their ingress setup outside of our recommended configuration should verify their infrastructure and apply any necessary security updates. Our security team continuously monitors emerging threats and ensures our platform remains secure. If you have any questions, please contact our support team at [support@cluedin.com](mailto:support@cluedin.com).