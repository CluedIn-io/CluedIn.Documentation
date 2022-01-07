---
layout: default
nav_order: 9
parent: Administration
permalink: /administration/backup-restore
title: Backup and Restore
tags: ["administration", "backup"]
last_modified: 2022-01-05
---

## Backup and Restore of the Managed disks

If managed disks are being used to store CluedIn's databases data, the preferred way of backup and restore is conducted by taking a snapshot of disks with in-built Azure functions from the outside of the cluster.

In order to backup a disk and ensure the integrity of data, CluedIn workloads need to be spun down first. The first workloads to be shutdown are the pods that are accessing databases either by writing, or reading.

You can use the following `kubectl` commands:
 ```shell
kubectl scale deployment -l role=processing --replicas=0
kubectl scale deployment -l role=main --replicas=0
kubectl scale deployment -l role=crawling --replicas=0
```

Once containers have finished terminating, we can spin down the databases to ensure the disks have detached from the nodes:
```shell
kubectl scale deployment -l app=sqlserver --replicas=0
kubectl scale deployment -l app=neo4j --replicas=0
kubectl scale statefulset -l chart=elasticsearch --replicas=0
kubectl scale statefulset -l app.kubernetes.io/name=rabbitmq --replicas=0
kubectl scale deployment -l app=redis --replicas=0
kubectl scale deployment -l app=openrefine --replicas=0
```

Lastly, we can backup the disks using in-built Azure functions as directed in [Azure Disk's documentation](https://docs.microsoft.com/en-us/azure/backup/backup-managed-disks).

Same documentation can be used to [restore from managed disks](https://docs.microsoft.com/en-us/azure/backup/restore-managed-disks).

Upon a successful backup or restore operation, the workloads can be spun back up:

```shell
kubectl scale deployment -l app=neo4j --replicas=1
kubectl scale statefulset -l chart=elasticsearch --replicas=1
kubectl scale statefulset -l app.kubernetes.io/name=rabbitmq --replicas=1
kubectl scale deployment -l app=redis --replicas=1
kubectl scale deployment -l app=openrefine --replicas=1
kubectl scale deployment -l app=sqlserver --replicas=1

kubectl scale deployment -l role=processing --replicas=1
kubectl scale deployment -l role=main --replicas=1
kubectl scale deployment -l role=crawling --replicas=1
```

# Backup and Restore using Velero

If not using managed disks or looking into snapshotting disks from inside the cluster, you can use Velero.

Please refer to the "Basic Install" section of the [Velero documentation](https://velero.io/docs).

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

The following is an example of what needs to be added to your values.yaml to configure Velero installation (check version information and latest Velero documentation):

```yml
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

**note**: please compare and update based on the version you are installing; example commands for acquiring the default yaml are:
```yml
helm repo add vmware-tanzu https://vmware-tanzu.github.io/helm-charts
helm repo update
helm install velero vmware-tanzu/velero --dry-run -o yaml
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


### Examples

A simple PowerShell script to install kubectl on Linux, and spin down the workloads and databases:

```powershell
Param ([Parameter(Mandatory)]$namespace)
Write-Host $namespace 

function Install-Kubectl {
    # This code is for Linux.
    # Please, check the official documentation for other options to install kubectl: https://kubernetes.io/docs/tasks/tools/#kubectl
    Write-Host "Installing kubectl.`n" -ForegroundColor Yellow
    curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
    mkdir -p ~/.local/bin/kubectl
    mv ./kubectl ~/.local/bin/kubectl
    export PATH="$HOME/local/bin:$PATH"
}

function Stop-Deployment {
    param (
        [Parameter(Mandatory=$true)]
        [string]$namespace,
        [Parameter(Mandatory=$true)]
        [string]$name
    )
    Write-Host "  Stopping deployment '$name' in namespace '$namespace'."
    kubectl scale deployment --namespace $namespace -l role=$name --replicas=0
}

function Stop-StatefulSet {
    param (
        [Parameter(Mandatory=$true)]
        [string]$namespace,
        [Parameter(Mandatory=$true)]
        [string]$name
    )
    Write-Host "  Stopping stateful set '$name' in namespace '$namespace'."
    kubectl scale statefulset --namespace $namespace -l $name --replicas=0
}

Install-Kubectl

Write-Host "Shutting down the workloads." -ForegroundColor Cyan

Stop-Deployment $namespace "processing"
Stop-Deployment $namespace "main"
Stop-Deployment $namespace "crawling"

# Wait for the pods to shut down
$secondsToWait = 60
Write-Host "`nWaiting $secondsToWait seconds for the workloads to stop.`n"  -ForegroundColor Yellow
Start-Sleep $secondsToWait

Write-Host "Stopping the databases:" -ForegroundColor Cyan

Stop-Deployment $namespace "sqlserver"
Stop-Deployment $namespace "neo4j"
Stop-StatefulSet $namespace "chart=elasticsearch"
Stop-StatefulSet $namespace "app.kubernetes.io/name=rabbitmq"
Stop-Deployment $namespace "redis"
Stop-Deployment $namespace "openrefine"
```

After the backup is completed, spin up the pods with a script like this:

```powershell
Param ([Parameter(Mandatory)]$namespace)
Write-Host $namespace 

function Start-Deployment {
    param (
        [Parameter(Mandatory=$true)]
        [string]$namespace,
        [Parameter(Mandatory=$true)]
        [string]$name
    )
    Write-Host "  Starting deployment '$name' in namespace '$namespace'."
    kubectl scale deployment  --namespace $namespace -l app=neo4j --replicas=1
}

function Start-StatefulSet {
    param (
        [Parameter(Mandatory=$true)]
        [string]$namespace,
        [Parameter(Mandatory=$true)]
        [string]$name
    )
    Write-Host "  Starting stateful set '$name' in namespace '$namespace'."
    kubectl scale statefulset --namespace $namespace -l $name --replicas=1
}

Write-Host "Starting the databases:" -ForegroundColor Cyan

Start-Deployment $namespace "sqlserver"
Start-Deployment $namespace "neo4j"
Start-StatefulSet $namespace "chart=elasticsearch"
Start-StatefulSet $namespace "app.kubernetes.io/name=rabbitmq"
Start-Deployment $namespace "redis"
Start-Deployment $namespace "openrefine"

# Wait for the pods to start up
$secondsToWait = 60
Write-Host "`nWaiting $secondsToWait seconds for the workloads to start.`n"  -ForegroundColor Yellow
Start-Sleep $secondsToWait

Write-Host "Starting the workloads." -ForegroundColor Cyan

Start-Deployment $namespace "processing"
Start-Deployment $namespace "main"
Start-Deployment $namespace "crawling"
```
