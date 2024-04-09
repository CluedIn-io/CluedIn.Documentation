---
layout: cluedin
nav_order: 30
parent: Azure
grand_parent: Deployment
permalink: /deployment/azure/certificate
title: TLS Certificate
tags: ["deployment", "kubernetes", "azure", "certificate", "ssl", "tls"]
last_modified: 2021-11-15
headerIcon: "paas"
---

When you have a [cluster with a public IP](./aks) and [DNS](./dns) links your domain name to that cluster, it's about time to think about the security and prepare a TLS-certificate that you that the CluedIn application will use when users access it via HTTPS.

You can buy a certificate or get a free one via a service like [Let's Encrypt](https://letsencrypt.org/). It has to be either a wildcard certificate for all the subdomains of your primary domain or a multi-domain certificate that will cover the URLs listed in the [DNS](./dns).