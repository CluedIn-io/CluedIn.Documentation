---
title: DNS
url: https://documentation.cluedin.net/operate/azure/dns
content_type: how-to
section: Deploy & operate > Azure deployment
---

# DNS

> how-to: Steps to accomplish one task.

To access CluedIn via domain name, you need to configure DNS. You would need to create DNS A-records that point the domain name to the AKS public IP address.

Say your AKS cluster public IP is `51.116.48.197`, the domain you want to associate with your CluedIn instance is `cluedin.mycompany.com`, and the tenant name is `hr`. Then you need to set up the following URLs to point to your AKS cluster:

- **app**.cluedin.mycompany.com
- **hr**.cluedin.mycomany.com
- **clean**.cluedin.mycompany.com

*Note: there could be more URLs to set up if you add more tenants or install additional tools on the cluster.*

The way you set up DNS depends on your domain registrar, but you usually need to create a set of `CNAME` and `A` [records](https://en.wikipedia.org/wiki/List_of_DNS_record_types) in your domain registrar admin panel.

Up: [Azure deployment](https://documentation.cluedin.net/operate/azure.md)
