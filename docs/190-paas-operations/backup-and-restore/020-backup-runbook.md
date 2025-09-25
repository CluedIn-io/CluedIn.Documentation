---
layout: cluedin
title: Backup runbook
parent: Backup and restore
grand_parent: PaaS operations
permalink: /paas-operations/automation/backup-runbook
nav_order: 2
headerIcon: "paas"
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

The backup runbook can be triggered manually or on a set schedule. It is responsible for capturing snapshots of all persistent disks used by CluedIn.

This runbook is a PowerShell script, which CluedIn will provide as needed.

**Prerequisites**

- An active CluedIn cluster with a valid license
- The runbook script
- An automation account
- A storage account
- Sufficient permissions

## Typical persistent disks

CluedIn configurations may vary, but a typical instance includes the nine disks as shown below.

## Automation account

An automation account must be provided. The runbook will be installed into the the automation account. Typically, the runbook should be scheduled to run once a day outside of office hours.

## Snapshots

Upon a successful run, the runbook generates nine snapshots and stores them in a resource group for seven days.

![backup-runbook.png]({{ "/assets/images/paas-operations/backup-runbook.png" | relative_url }})

## Input parameters

| Parameter | Default | Description |
|--|--|--|
| ClusterName | _required_ | Name of the target AKS cluster |
| CustomerName | _required_ | Name of customer |
| Subscription | _required_ | ID of the azure subscription |
| SnapshotType | `Incremental` | Incremental or Full |
| BackupResourceGroup | _required_ | Name of resource group where the snapshots will be saved to |
| RetentionCount | `7` | Number of days to retain the snapshots |
| EnableScaling | `true` | Scale down the cluster during restore |

## Process

![backup-runbook-process.png]({{ "/assets/images/paas-operations/backup-runbook-process.png" | relative_url }})

Scaling up or down deployments is optional. However, it is recommended to prevent data loss while capturing snapshots.

## Permissions

The runbook must be granted the following permissions:

| Resource                     | Assigned Role(s)                                             | Why This Role is Needed                                                                 |
|------------------------------|--------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| AKS Resource Group           | Reader                                                       | Required to read AKS configurations and metadata.                                        |
| AKS Instance                 | Contributor                                                  | Required to scale AKS Instance and send aks command.                                     |
| Snapshot Resource Group      | Reader, Disk Snapshot Contributor                           | Required to read snapshots and creating/managing disk snapshots in the resource group.   |
| AKS Node Resource Group      | Reader, Disk Snapshot Contributor, VM Restore Contributor    | Required to read list of disk, delete old disk, and restore new Disk from snapshot.      |
| Storage Account Resource Group | Reader                                                     | Required to read Storage account configurations and metadata.                            |
| Storage Account              | Storage Blob Data Contributor, Storage Account Key Operator Service Role | Required to store pod replica configuration during scaling down. |
