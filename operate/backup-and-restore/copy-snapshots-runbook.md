---
title: Copy snapshots runbook
url: https://documentation.cluedin.net/operate/backup-and-restore/copy-snapshots-runbook
content_type: how-to
section: Deploy & operate > Backup and restore
---

# Copy snapshots runbook

> how-to: Steps to accomplish one task.

The copy snapshots runbook can be triggered manually or on a set schedule. It copies snapshots from one Azure location to another. However, if your source and target CluedIn instances are the same or reside in the same Azure location, this runbook is not required.

This runbook is a PowerShell script that CluedIn will provide as needed.

**Prerequisites**

- At least one active CluedIn cluster with a valid license
- The runbook script
- An automation account
- A storage account
- Sufficient permissions

## Typical snapshots

Typically, Cluedin requires nine snapshots, which will be attached to the disks during a restore process. The snapshot type is incremental.

## Automation account

An automation account must be provided, the runbook will be installed into the the automation account. Typically, the runbook should be triggered once the snapshots have been created successfully.

## Transfer of snapshots

Snapshot transfers occur over the Microsoft backbone and can take anywhere from 20 minutes for small datasets to several hours for larger ones. Additionally, Azure inter-region transfer costs will apply.

![Diagram: disk snapshots in the source resource group of Instance A (CluedIn AKS, Vnet North Europe) are transferred, if required, to the target resource group of Instance B in a secondary region (Vnet West Europe)](https://documentation.cluedin.net/assets/images/paas-operations/copy-snapshots-runbook.png)

## Input parameters

| Parameter | Default | Description |
|--|--|--|
| LicenseKey | _required_ | License key tag on snapshot |
| Timestamp | _required_ | Timestamp on snapshot |
| SourceResourceGroup | _required_ | Name of source resource group |
| TargetSubscriptionId | _required_ | ID of target Azure subscription |
| TargetResourceGroup | _required_ | Name of target resource group |
| TargetRegion | _required_ | Target Azure location |

## Process

![Flowchart of the runbook: start, retrieve all snapshots by license key and timestamp, loop through all snapshots, transfer to new location, stop](https://documentation.cluedin.net/assets/images/paas-operations/copy-snapshots-runbook-process.png)

When the source and target resource groups are in the same location, the snapshot copy is not neccessary.

Up: [Backup and restore](https://documentation.cluedin.net/operate/backup-and-restore.md)
