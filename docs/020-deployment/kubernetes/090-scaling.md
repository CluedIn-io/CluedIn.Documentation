---
layout: default
nav_order: 9
parent: Kubernetes
grand_parent: Installation
permalink: /deployment/kubernetes/scaling
title: Scaling
tags: ["deployment", "kubernetes", "scaling"]
---

The CluedIn Server is performing 3 main functions:
- responding to web API calls
- retrieving data from integrations (crawling)
- processing updated data

These three functions can be segregated into specialized containers - it is also possible to scale the number of pods performing each function and the resources allocated to each. 

If the `count` property for the `processing` and/or `crawling` roles is set to `0`, the `main` role will take over those tasks. 

All this is controlled by the following section of the `values.yaml` configuration:

```yaml
cluedin:
  roles:
    main:
      count: 1
      resources:
        limits:
          cpu: "1"
          memory: "8Gi"
        requests:
          cpu: "0.5"
          memory: "4Gi"
    processing:
      count: 1
      resources:
        limits:
          cpu: "1"
          memory: "8Gi"
        requests:
          cpu: "0.5"
          memory: "4Gi"
    crawling:
      count: 1
      resources:
        limits:
          cpu: "1"
          memory: "8Gi"
        requests:
          cpu: "0.5"
          memory: "4Gi"
```
