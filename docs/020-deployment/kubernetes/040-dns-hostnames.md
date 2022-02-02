---
layout: default
nav_order: 4
parent: Kubernetes
grand_parent: Deployment
permalink: /deployment/kubernetes/dns-hostnames
title: Hostnames and Addresses
tags: ["deployment", "kubernetes", "dns", "hostnames"]
---

CluedIn is a web application, so users will access it from their browser. The main URL will take the form: 
 `https://<app-segment>.<prefix>.<hostname>`. 
 CluedIn is a multi-tenant application, so you can have different organizations/units in your company that can use CluedIn with total separation. So in order to use CluedIn you will need to create at least one *organization*. Each organization gets a different URL: `https://<organization>.<prefix>.<hostname>`. Since any number of organizations can be created from the application, the recommendation would be to map `*.<prefix>.<hostname>` to the public IP of the ingress of the cluster.

The `<prefix>` and `<hostname>` can be adjusted by changing the helm chart values in the `dns` section.

```yaml
dns:
  prefix: # defaults to the release name, set to none to disable prefixes.
  hostname: # add the hostname suffix - i.e. example.com
```