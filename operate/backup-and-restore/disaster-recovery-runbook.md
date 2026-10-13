---
title: Disaster recovery runbook
url: https://documentation.cluedin.net/operate/backup-and-restore/disaster-recovery-runbook
content_type: how-to
section: Deploy & operate > Backup and restore
---

# Disaster recovery runbook

> how-to: Steps to accomplish one task.

The disaster recovery runbook can be triggered manually or on a set schedule. It is responsible for orchestrating the backup > copy > restore process.

This runbook is a PowerShell script, which CluedIn will provide as needed.

> **Important:** This runbook is recommended for instances with less than 1M records.

**Prerequisites**

- This runbook is for CluedIn versions 2025.09.00 and onwards
- Pre 2025.09.00 use [Disaster recovery runbook - legacy](https://documentation.cluedin.net/archive/historical-operations/disaster-recovery-runbook-pre-2025-09.md)
- An active CluedIn cluster with a valid license (and/or a passive CluedIn cluster)
- The runbook script
- An automation account
- The backup runbook
- The copy runbook
- The restore runbook
- A storage account
- Sufficient permissions

## Automation account

An automation account must be provided. The runbook will be installed into the the automation account. The three dependent runbooks must already be installed. Typically, the runbook should be scheduled to run once a day outside of office hours.

![Architecture: in an automation account, the orchestrate runbook triggers the backup runbook, which snapshots production AKS and Azure SQL; the transfer runbook copies snapshots to the DR region, and the restore runbook restores them to DR AKS and SQL](https://documentation.cluedin.net/assets/images/paas-operations/disaster-recovery-runbook-2026.png)

## Input parameters

| Parameter | Default | Description |
|--|--|--|
| CustomerName | _required_ | Name of customer |
| Subscription | _required_ | ID of the Azure subscription |
| SourceResourceGroup | _required_ | Name of resource group where source AKS cluster is located |
| TargetResourceGroup | _required_` | Name of resource group where target AKS cluster is located |
| TargetStorageAccount | _required_ | Name of target storage account |
| SourceSnapshotResourceGroup | _required_ | Name of resource group containing source snapshots |
| TargetSnapshotResourceGroup | _required_ | Name of resource group containing copied snapshots |
| ScaledownDR | `true` | Scales down a DR cluster after a successful restoer |

## Process

### 1. Backup of the Primary CluedIn Instance

The backup runbook performs the following actions:

- Takes snapshots of the virtual machine disks and stores them in a designated resource group.
- Exports the Azure SQL databases as BACPAC files.
- Stores the BACPAC files in a designated storage account.

---

### 2. Transfer of Snapshots and BACPAC Files

Upon successful completion of the backups:

- Disk snapshots and BACPAC files are transferred from the primary region to the secondary region via the Microsoft backbone.
- Transfer completion and data integrity should be validated before proceeding.

---

### 3. Disaster Recovery Environment Validation

The idle CluedIn DR instance in the secondary region is prepared and validated as follows:

1. Restart the DR environment.
2. Scale down all Kubernetes deployments and stateful sets.
3. Restore the disks from the replicated snapshots.
4. Restore the Azure SQL databases from the transferred BACPAC files.
5. Scale the stateful sets and deployments back up.
6. Verify that all services start successfully and the system operates without errors.
7. After validation, scale the CluedIn environment back down to its idle state to optimize cost.

![Flow: start, trigger backup, wait for backups to complete, copy snapshots to target, wait for transfer, restore CluedIn, wait for restore to complete, stop](https://documentation.cluedin.net/assets/images/paas-operations/disaster-recovery-runbook-process.png)

Scaling down of the DR environment following a successful restore is optional.

Up: [Backup and restore](https://documentation.cluedin.net/operate/backup-and-restore.md)
