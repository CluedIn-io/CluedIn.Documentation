---
grand_parent: Deployment
layout: default
nav_order: 8
parent: Kubernetes
grand_parent: Installation
permalink: /deployment/kubernetes/persistence
title: Persistence
tags: ["deployment", "kubernetes", "persistence"]
---
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

By default all deployments that store state (sqlserver, elasticsearch, rabbitmq, redis, openrefine) are defined with some storage in order to persist the state. You can adjust the size of the storage by setting the following property (for each deployment):

```yaml
neo4j: #name of the deployment
    persistence:
        storageSize: 1G
```

Alternatively, you can also supply your own persistence volume claims that you may have created manually outside the chart. To do so, for each deployment, you can set the `claimName` property, e.g.:
```yaml
neo4j: #name of the deployment
    persistence:
        claimName: my-claim-name-I-have-already-created
```

Note that using persistence in this manner a volume can only be linked to a single pod; so you won't be able to scale the number of pods. In addition, the strategy for updating the pods is set to `Recreate` for exactly the same reason (as setting it to `Rollout` would require to have two pods accessing the volume simultaneously).

If you need to scale the number of pods, further customization would be required to use persistence in a different way.

Persistence can also be turned off, for each deployment, through the setting:

```yaml
neo4j: #name of the deployment
    persistence:
        enabled: false
```

### Azure Disk

If you are running on Azure, you can enable persistence to be configured so that it will store data on dedicated azure disks. This allows you to use some of the management and backup features of this product. 

To configure add the following section to the persistence section in your values file..

```yaml
 azureDisk: 
       data:
         diskName: 
         diskURI: 
         diskKind: 
```
