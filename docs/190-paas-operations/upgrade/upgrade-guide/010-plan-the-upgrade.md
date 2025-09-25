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

## Prepare the prerequisites 

Before starting an upgrade, make sure you have the following in place: 

  1. Access to the live CluedIn application 
  1. Access to the kubeconfig file this must be provided by your azure administrator 
  1. A machine or VM with the following tools installed: 

      - Kubectl 1.30 (min) 
      - Helm 3.x.x 
      - Visual Studio Code (optional) 
      - Lens (or FreeLens) (optional) 

## Perform pre-upgrade actions 

Before performing an upgrade, complete the following steps to ensure a smooth process and minimize risks: 

  1. Schedule Downtime 
    Plan the upgrade during a period when the application is not in use. The application will be unavailable throughout the upgrade process. 

  1. Perform a Full Backup 
    Back up all persistent disks and user values. This step is critical in case a rollback is required. 

  1. Allocate Sufficient Time 
    Allow enough time to run the full upgrade and to manage potential disaster recovery scenarios if needed. 

  1. Inform Stakeholders 
    Keep all relevant stakeholders informed before, during, and after the upgrade: 

      - Before the upgrade: Provide advance notice of the planned upgrade window, expected downtime, and potential business impact. 
      - During the upgrade: Share progress updates if the process takes longer than anticipated or if issues arise. 
      - After the upgrade: Confirm completion, communicate any changes that may affect users, and provide guidance on reporting unexpected issues. 

## Review the upgrade documentation 

CluedIn publishes upgrade documentation with each new release. Please ensure you read the documentation in full before beginning the upgrade process. While many upgrades share common steps, not all are identical, and some may include specialized procedures. 

{:.important}
Pay particular attention to any infrastructure-related changes, as these may require additional preparation or configuration. 