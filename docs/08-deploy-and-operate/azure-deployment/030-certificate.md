---
layout: cluedin
title: TLS Certificate
parent: Azure deployment
grand_parent: Deploy & operate
nav_order: 30
permalink: /operate/azure/certificate
content_type: how-to
redirect_from: ["/deployment/azure/certificate"]
source_path: docs/020-deployment/azure/030-certificate.md
tags: ["deployment", "kubernetes", "azure", "certificate", "ssl", "tls"]
last_modified: 2021-11-15
headerIcon: "paas"
---

When you have a [cluster with a public IP](/operate/azure/aks) and [DNS](/operate/azure/dns) links your domain name to that cluster, it's about time to think about the security and prepare a TLS-certificate that you that the CluedIn application will use when users access it via HTTPS.

You can buy a certificate or get a free one via a service like [Let's Encrypt](https://letsencrypt.org/). It has to be either a wildcard certificate for all the subdomains of your primary domain or a multi-domain certificate that will cover the URLs listed in the [DNS](/operate/azure/dns).