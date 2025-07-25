---
layout: cluedin
title: Restore runbook
parent: Backup and restore
grand_parent: PaaS operations
permalink: paas-operations/automation/restore-runbook
nav_order: 4
headerIcon: "paas"
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

The restore runbook can be triggered manually or on a predefined schedule. It handles the removal of all persistent disks and restores them from snapshots.

This runbook is a PowerShell script, which CluedIn will provide as needed.

**Prerequisites**

- An active or passive CluedIn cluster with a valid license
- The runbook script
- An automation account
- A storage account
- Sufficient permissions

## Typical persistent disks

CluedIn configurations may vary, but a typical instance includes the nine disks as shown below. All must be restore from snapshots.

## Automation account

An automation account must be provided. The runbook will be installed into the the automation account. Typically, the runbook should be triggered following a backup/copy event.

## Scaledown

The runbook will optionally scale down the target CluedIn instance after the restore.

![restore-runbook.png]({{ "/assets/images/paas-operations/restore-runbook.png" | relative_url }})

## Input parameters

| Parameter | Default | Description |
|--|--|--|
| LicenseKey | _required_ | License key tag on snapshot |
| Timestamp | _required_ | Timestamp on snapshot |
| HostResourceGroup | _required_ | Name of source resource group |
| Subscription | _required_ | ID of target Azure subscription |
| TargetResourceGroup | _required_ | Name of target resource group |
| TargetAKSClusterName | _required_ | Name of target AKS cluster |
| StorageAccountName | _required_ | Name of storage account |
| Scaledown | `false` | Option to scale down after a successful restore |

## Process

![restore-runbook-process.png]({{ "/assets/images/paas-operations/restore-runbook-process.png" | relative_url }})