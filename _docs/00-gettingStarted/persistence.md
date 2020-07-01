# TODO
* List all services that have persistence configurable

---
category: Get Started
title: Configuring the Helm Chart
hideMenu: true
---

## Persistence

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
