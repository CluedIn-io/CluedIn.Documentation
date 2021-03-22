---
category: Administration
title: Backup and Restore
---

# Backup and Restore of the Managed disks

If managed disks are being used to store CluedIn's databases data, the preferred way of backup and restore is conducted by taking a snapshot of disks with in-built Azure functions from the outside of the cluster.

In order to backup a disk and ensure the integrity of data, CluedIn workloads needs to be spun down. First workloads to be shutodwn are the pods that are accessing databases either by writing, or reading.

You can use the following `kubectl` commands:
 ```
    kubectl scale deployment -l role=processing --replicas=0
    kubectl scale deployment -l role=main --replicas=0
    kubectl scale deployment -l role=crawling --replicas=0
```

Once containers has finished terminating, we can spin down the databases itself for disks to detach from the nodes:
```
kubectl scale deployment -l app=sqlserver --replicas=0
kubectl scale deployment -l app=neo4j --replicas=0
kubectl scale statefulset -l chart=elasticsearch --replicas=0
kubectl scale deployment -l app=rabbitmq --replicas=0
kubectl scale deployment -l app=redis --replicas=0
kubectl scale deployment -l app=openrefine --replicas=0
```

Lastly, we can backup the disks using in-built Azure functions as instructed in Azure Disk's documentation: https://docs.microsoft.com/en-us/azure/backup/backup-managed-disks

Same documentation can be used to restore from managed disks:
https://docs.microsoft.com/en-us/azure/backup/restore-managed-disks

Upon a successful backup or restore operation, the workloads can be spun back up:

```
    kubectl scale deployment -l app=neo4j --replicas=1
    kubectl scale statefulset -l chart=elasticsearch --replicas=1
    kubectl scale deployment -l app=rabbitmq --replicas=1
    kubectl scale deployment -l app=redis --replicas=1
    kubectl scale deployment -l app=openrefine --replicas=1
    kubectl scale deployment -l role=processing --replicas=1
    kubectl scale deployment -l role=main --replicas=1
    kubectl scale deployment -l role=crawling --replicas=1
    kubectl scale deployment -l app=sqlserver --replicas=1
```

# Backup and Restore using Velero

If not using managed disks or looking into snapshotting disks from inside the cluster, you can use Velero.

Refer to the official Velero documentation to find guidance on installation: 
https://velero.io/docs/v1.5/basic-install/

### Pre-requisites

* Storage account
  * Blob Container

* Velero Service Principal

* Velero server installed

* Configuration:
  * Subscription Id
  * Resource Group Name
  * Storage Account Name
  * Blob Container Name
  * Backup location
  * Velero SP Account Name
  * AKS Resource Group Name

* RBAC assignments required: 
  * For apiGroup ‘velero.io’ access needs to be granted for all (*) resources in the cluster.

* Velero SP requires the following roles: o “Microsoft.Compute/disks/read” for managed disks
* Contributor role for Storage Account
* Contributor role for Storage Blob data

The following needs to be added to your values.yaml to configure Velero installation:

```
velero:
  image:
    repository: vmware-tanzu/velero
    tag: v2.12.17
    pullPolicy: IfNotPresent
    
  installCRDs: false

  initContainers: 
  - name: velero-plugin-for-microsoft-azure
    image: velero/velero-plugin-for-microsoft-azure:v1.0.0
    imagePullPolicy: IfNotPresent
    volumeMounts:
      - mountPath: /target
        name: plugins


  configuration:
    provider: azure

    backupStorageLocation:
      name: azure-bucket
      provider: azure
      bucket: <VELERO_BLOB_CONTAINER_NAME>
      config: 
        region: <VELERO_REGION>
        resourceGroup: <VELERO_RESOURCE_GROUP_NAME>
        subscriptionId: <SUBSCRIPTION_ID>
        storageAccount: <VELERO_STORAGE_ACCOUNT_NAME>
        serviceAccount: <VELERO_SP_NAME>

    volumeSnapshotLocation:
      name: velero
      config: 
        apitimeout: "5m"
        resourceGroup: <VELERO_RESOURCE_GROUP_NAME>
        subscriptionId: <SUBSCRIPTION_ID>

    credentials:
      useSecret: true
      existingSecret: 'cloud-credentials'
    
    schedules:
      daily-backup:
        schedule: "0 0 * * *"
        template:
          includeClusterResources: true
          includedNamespaces:
          - '*'
          includedResources:
          - '*'
          storageLocation: azure-bucket
          snapshotVolumes: true      
          ttl: 720h0m0s
```

### Backup

Backup procedure is scheduled to run every 24 hours at 01:00AM. Backup job time to live is set to 48 hours. Time to live for a backup is set to 72 hours. Schedule is configured via Helm chart at installation, or via Velero CLI. It snapshots & moves the backup automatically to the blob storage without any manual work required.

Whole cluster will be backed up as .json or .tar.gz files respectively, and moved to Blob Storage with a timestamp. Read more about how Velero compresses output files. To take a manual backup, execute:

`velero create backup <backup name>`

### Restore

When restoring from the backup, there are a couple of options.

* Restoring from schedule:

    This is a preferred way to restore. It means it will restore from the last successfully ran scheduled backup. Execute the following command to restore:

    `velero restore create --from-schedule daily`


* Restoring from manual backup

    Identify the backup you want to restore:

    `velero backup get`

    Restoring from the backup:

    `velero restore create --from-backup <backup name>`
