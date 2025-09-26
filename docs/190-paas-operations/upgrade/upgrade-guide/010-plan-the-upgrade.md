---
layout: cluedin
nav_order: 1
parent: CluedIn upgrade guide
grand_parent: Upgrade
permalink: /paas-operations/upgrade/guide/plan-the-upgrade
title: Plan the upgrade
tags: ["deployment", "ama", "marketplace", "azure", "aks", "kubernetes", "upgrade"]
last_modified: 2025-09-22
headerIcon: "paas"

---
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

Careful planning ensures that the upgrade process is efficient, minimizes downtime, and accounts for dependencies across your environment. This page covers stage 1 of the [CluedIn upgrade process](/paas-operations/upgrade/guide). It outlines the decisions and preparations you should make before executing the upgrade.

## Get familiar with the versioning scheme 

CluedIn releases version numbers follow this format: **`{year}.{month}.{patch}`**. For example, **`2025.05.02`**.

For details about the updates available in a specific release, see [Release notes](/release-notes).

## Perform pre-upgrade actions 

Before performing an upgrade, complete the following steps to ensure a smooth process and minimize risks:

1. **Schedule downtime** – Plan the upgrade during a period when the application is not in use. The application will be unavailable throughout the upgrade process. 

1. **Perform a full backup** – Back up all persistent disks and user values. This step is critical in case a rollback becomes necessary.

1. **Allocate sufficient time** – Ensure you have enough time for the full upgrade and, if required, disaster recovery.

1. **Inform the stakeholders** – Communicate at all stages of the upgrade:

    - Before the upgrade: Provide advance notice of the planned upgrade window, expected downtime, and potential business impact. 

    - During the upgrade: Provide updates if the upgrade takes longer than anticipated or if issues arise. 

    - After the upgrade: Confirm completion, communicate any changes affecting users, and explain how to report issues. 

## Review the upgrade documentation 

CluedIn publishes [upgrade documentation](/paas-operations/upgrade) with each new release. Be sure to review this documentation in full before beginning the upgrade process. While many upgrades follow common steps, not all are identical, and some may include specialized procedures. 

{:.important}
Pay particular attention to any infrastructure-related changes, as these may require additional preparation or configuration. 