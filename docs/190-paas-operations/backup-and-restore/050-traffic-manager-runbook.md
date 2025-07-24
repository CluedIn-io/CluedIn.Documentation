---
layout: cluedin
title: Traffic manager runbook
parent: Backup and restore
grand_parent: PaaS operations
permalink: {{ site.baseurl }}/paas-operations/automation/traffic-manager-runbook
nav_order: 5
headerIcon: "paas"
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

The traffic manager runbook will swap the endpoints or the traffic manager following a disaster event. The runbook will switch from the active region to the passive region (and back again).

This runbook is a PowerShell script, which CluedIn will provide as needed. This runbook should be run manually following a disaster event.

**Prerequisites**

- An active CluedIn cluster with a valid license (and/or a passive CluedIn cluster)
- The runbook script
- An automation account
- A storage account
- Sufficient permissions

## Automation account

An automation account must be provided. The runbook will be installed into the automation account. Typically, the runbook should only be run following a disaster event and after discussions with relevant stakeholders.

![traffic-manager-runbook.png](../../assets/images/paas-operations/traffic-manager-runbook.png)

## Input parameters

| Parameter | Default | Description |
|--|--|--|
| Subscription | _required_ | ID of the Azure subscription where the traffic manager is located |
| ResourceGroupName | _required_ | Name of resource group where the traffic manager is located |
| FailToDRDR | `true` | Move to the DR endpoints; when `false` move back to original endpoints |

## Process

![traffic-manager-runbook-process.png](../../assets/images/paas-operations/traffic-manager-runbook-process.png)

Scaling down of the DR environment following a successful restore is optional.