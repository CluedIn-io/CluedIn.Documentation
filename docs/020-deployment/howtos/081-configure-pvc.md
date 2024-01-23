---
grand_parent: Deployment
layout: cluedin
nav_order: 9
parent: How-to guides
grand_parent: Installation
permalink: /deployment/kubernetes/persistence
title: Configure PVC
tags: ["deployment", "kubernetes", "persistence"]
---
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

## Resizing

By default, all deployments that store state (sqlserver, elasticsearch, rabbitmq, redis, openrefine) are defined with some storage in order to persist the state. We deploy with a recommended size by default, but there may be times where you want to adjust the size of the storage.

You can do this by setting the following property (for each deployment) in the values file:

```yaml
infrastructure:
  neo4j: #name of the deployment
    core:
      persistentVolume:
        size: 1G
```

Using persistence in this manner, a volume can only be linked to a single pod; so you won't be able to scale the number of pods. In addition, the strategy for updating the pods is set to `Recreate` for exactly the same reason (as setting it to `Rollout` would require to have two pods accessing the volume simultaneously).

The deployment to Azure will automatically handle the sizing. However, you cannot size down easily due to the way infrastructure disks work on Azure. Therefore, it is recommended to only size up.

When working locally, you have more freedom as this is controlled by the user.

## Use existing volume claims

If you don't want a service to create the PVC disks for you, you can:

1. Create the PVCs ahead of time (if possible - see examples in this directory for each service)
2. Update `values.yaml` with the names of the PVCs (see example `values.yaml` in this article - as different charts work differently the syntax is not consistent.).

For certain services (ElasticSearch, Neo4J) you have to use specific names for the PVC in order to get them to work. These are listed in the example `values.yaml`. 

## Getting AKS to create the disks on another resource group

If you want to create a disk on a different resource group (for increased resilience against cluster death), you can create a new `StorageClass` resource, in the `cluedin` namespace, with the configuration you want in it.

1. Create a new `StorageClass` object which links to the resource group 

```yml
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
  name: external-rg-hdd
provisioner: kubernetes.io/azure-disk
parameters:
  skuname: Standard_LRS
  kind: Managed
  cachingMode: ReadOnly
  resourceGroup: RESOURCE_GROUP_NAME
allowVolumeExpansion: true
```

2. Update the `storageClass` / `storageClassName` in the appropriate chart .. 

```yml
mssql:
  persistence:
    storageClass: "external-rg-hdd"
```

When it provisions the PVC for the first time it will provision them on a different resource group.

Note: Its is **unsupported/not possible** to create disks in another *subscription*.
Microsoft have said they have no plans to support this.

## Different SKUs in Azure

### SSD/Premium

```yml
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
  name: ssd
provisioner: kubernetes.io/azure-disk
parameters:
  skuname: Premium_LRS
  kind: managed
  cachingMode: ReadOnly
  ```

### Link directly to Azure Disk

```yml

apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv-azuredisk
spec:
  capacity:
    storage: 5Gi
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  azureDisk:
    diskName: {disk-id}
    diskURI: /subscriptions/{sub-id}/resourcegroups/{group-name}/providers/microsoft.compute/disks/{disk-id}
    kind: Managed
    cachingMode: ReadOnly
    fsType: ext4
    readOnly: false
```

## References

Lots of example of different Azure/AKS `StorageClass` definitions can be found here:
[https://github.com/andyzhangx/demo/tree/master/pv](https://github.com/andyzhangx/demo/tree/master/pv).

## Examples

### values.yml

```yml
mssql:
  persistence:
    existingDataClaim: "cluedin-sqlserver-data"
    existingTransactionLogClaim: "cluedin-sqlserver-translog"
    existingBackupClaim: "cluedin-sqlserver-backup"
    existingMasterClaim: "cluedin-sqlserver-master"

seq:
  persistence:
    existingClaim: "cluedin-seq-data"
    
rabbitmq:
  persistence:
    existingClaim: "cluedin-rabbitmq-data"

# Note: If you are going to scale REDIS up and run multiple replicas etc then just create PVCs with the same name
# as the PVC its *going* to create ahead of installation.

redis:
  master:
    persistence:
      existingClaim: "cluedin-redis-data"
      
# Note: For ELASTICSEARCH you need to create a PVC with the same name as the one its *going* to create ahead of
# installation. This is because it uses a volumeClaimTemplate.

```

### cluedin-elastic-pvc.yml

```yml
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: cluedin-elasticsearch-cluedin-elasticsearch-0
  labels:
    app: elasticsearch
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 30Gi
```

### cluedin-neo4j-pvc.yml

```yml
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: datadir-cluedin-neo4j-core-0
  labels:
    app: neo4j
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 12Gi
```

### cluedin-rabbitmq-pvc.yml

```yml
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: cluedin-rabbitmq-data
  labels:
    app: rabbitmq
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
```

### cluedin-redis-pvc.yml

```yml
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: cluedin-redis-data
  labels:
    app: redis
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
```

### cluedin-seq-pvc.yml

```yml
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: cluedin-seq-data
  labels:
    app: seq
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
```

### cluedin-sqlserver-pvc.yml

```yml
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: cluedin-sqlserver-master
  labels:
    app: sqlserver
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 4Gi
---
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: cluedin-sqlserver-backup
  labels:
    app: sqlserver
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 4Gi
---
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: cluedin-sqlserver-data
  labels:
    app: sqlserver
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 4Gi
---
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: cluedin-sqlserver-translog
  labels:
    app: sqlserver
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 4Gi
```