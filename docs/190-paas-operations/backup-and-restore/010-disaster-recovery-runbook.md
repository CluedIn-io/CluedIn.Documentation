---
layout: cluedin
title: Disaster recovery runbook
parent: Backup and restore
grand_parent: PaaS operations
permalink: paas-operations/automation/disaster-recovery-runbook
nav_order: 1
headerIcon: "paas"
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

The disaster recovery runbook can be triggered manually or on a set schedule. It is responsible for orchestrating the backup > copy > restore process.

This runbook is a PowerShell script, which CluedIn will provide as needed.

**Prerequisites**

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

![disaster-recovery-runbook.png]({{ "/assets/images/paas-operations/disaster-recovery-runbook.png" | relative_url }})| relative_url }})

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

![disaster-recovery-runbook-process.png]({{ "/assets/images/paas-operations/disaster-recovery-runbook-process.png" | relative_url }})| relative_url }})

Scaling down of the DR environment following a successful restore is optional.