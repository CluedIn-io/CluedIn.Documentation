---
title: TLS Certificate
url: https://documentation.cluedin.net/operate/azure/certificate
content_type: how-to
section: Deploy & operate > Azure deployment
---

# TLS Certificate

> how-to: Steps to accomplish one task.

When you have a [cluster with a public IP](https://documentation.cluedin.net/operate/azure/aks.md) and [DNS](https://documentation.cluedin.net/operate/azure/dns.md) links your domain name to that cluster, it's about time to think about the security and prepare a TLS-certificate that you that the CluedIn application will use when users access it via HTTPS.

You can buy a certificate or get a free one via a service like [Let's Encrypt](https://letsencrypt.org/). It has to be either a wildcard certificate for all the subdomains of your primary domain or a multi-domain certificate that will cover the URLs listed in the [DNS](https://documentation.cluedin.net/operate/azure/dns.md).

Up: [Azure deployment](https://documentation.cluedin.net/operate/azure.md)
