---
title: Traffic manager runbook
url: https://documentation.cluedin.net/operate/backup-and-restore/traffic-manager-runbook
content_type: how-to
section: Deploy & operate > Backup and restore
---

# Traffic manager runbook

> how-to: Steps to accomplish one task.

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

![Diagram: DNS points to Traffic Manager, which routes to root-prod, app-prod and clean-prod endpoints for CluedIn AKS in the active region (North Europe), with standby root-dr-prod, app-dr-prod and clean-dr-prod endpoints for CluedIn AKS in the passive region (West Europe)](https://documentation.cluedin.net/assets/images/paas-operations/traffic-manager-runbook.png)

## Input parameters

| Parameter | Default | Description |
|--|--|--|
| Subscription | _required_ | ID of the Azure subscription where the traffic manager is located |
| ResourceGroupName | _required_ | Name of resource group where the traffic manager is located |
| FailToDRDR | `true` | Move to the DR endpoints; when `false` move back to original endpoints |

## Process

![Flowchart: Start, trigger runbook, switch endpoints, Stop](https://documentation.cluedin.net/assets/images/paas-operations/traffic-manager-runbook-process.png)

Scaling down of the DR environment following a successful restore is optional.

Up: [Backup and restore](https://documentation.cluedin.net/operate/backup-and-restore.md)
