---
layout: cluedin
title: Backup runbook
parent: Automation
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

![backup-runbook.png](../../assets/images/paas-operations/backup-runbook.png)

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

![backup-runbook-process.png](../../assets/images/paas-operations/backup-runbook-process.png)

Scaling up or down deployments is optional. However, it is recommended to prevent data loss while capturing snapshots.