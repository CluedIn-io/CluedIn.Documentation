---
layout: cluedin
nav_order: 16
parent: Configuration
grand_parent: PaaS operations
permalink: /paas-operations/config/modify-response-headers
title: Modify web response headers
tags: ["deployment", "kubernetes", "web", "frontend"]
headerIcon: "paas"
---

By default, CluedIn is configured with web security in mind and out of the box is quite secure. In certain cases, security teams may require additional configuration on the response headers to comply with policies.

This guide explains how you can modify these headers to comply with your organization.

**Prerequisites**
- Access to your Kubernetes cluster
- Helm installed

**To modify web response headers**
In order to modify the headers, we'll recommend updating the configMap of HAProxy Ingress Controller by amending your values.yaml file to add the supported key:value pairs.

1. Export your current values file from a given environment.
1. Edit the now exported values file in the following section:

   ```yaml
   infrastructure:
     controller:
       config: # This is additions to the configMap
         config-backend: | # This refers to: https://haproxy-ingress.github.io/docs/configuration/keys/#configuration-snippet
           http-response add-header Cache-Control no-store
           http-response add-header X-Content-Type-Options nosniff

           # The above will add two additional response header entries for Cache-Control and X-Content-Type.
           # This can be updated to something more suitable to your organization.
   ```

1. Run helm update with the new values. After a few minutes, the config map `cluedin-haproxy-ingress` should now have a new entry for `config-backend`
1. To validate that the headers are being passed, go to your front end in the browser, open up the developer tools (In Chrome, this is F12), and check the response headers from the front end.

   You should notice that the added responses are now part of the overall response.

For any further assistance or an edge case, reach out to CluedIn support.