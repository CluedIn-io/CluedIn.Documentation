---
layout: cluedin
nav_order: 1
parent: Upgrade
grand_parent: PaaS operations
permalink: /paas-operations/upgrade/guide
title: Upgrade guide
tags: ["deployment", "ama", "marketplace", "azure", "aks", "kubernetes", "upgrade"]
last_modified: 2025-09-22
headerIcon: "paas"

---

This guide provides instructions for upgrading CluedIn after the initial [installation](/deployment). Regular upgrades are recommended to ensure you benefit from the latest features, improvements, and fixes. For details about the updates available in a specific release, see [Release notes](/release-notes).

The upgrade process typically involves the steps outlined below.

{:.important}
If issues occur during the upgrade, see [Resolve common upgrade issues](/paas-operations/upgrade/guide/resolve-common-upgrade-issues) for troubleshooting instructions.

![upgrade_process.png]({{ "/assets/images/paas-operations/upgrade/upgrade_process_2.png" | relative_url }})

**Prerequisites for upgrade**

Before starting an upgrade, make sure you have the following in place: 

1. Access to live CluedIn application.
1. Access to AKS cluster.
1. Access to the kubeconfig file – this must be provided by your Azure administrator.
1. A machine or a virtual machine (VM).
1. All the [required tools](/paas-operations/upgrade/guide/required-tools) installed on the machine/VM.

**Stage 1 – Plan your upgrade**
1. Get familiar with the versioning scheme. See [instructions](/paas-operations/upgrade/guide/plan-the-upgrade#get-familiar-with-the-versioning-scheme).
1. Perform pre-upgrade actions. See [instructions](/paas-operations/upgrade/guide/plan-the-upgrade#perform-pre-upgrade-actions).
1. Review the upgrade documentation. See [instructions](/paas-operations/upgrade/guide/plan-the-upgrade#review-the-upgrade-documentation).

**Stage 2 – Prepare for the upgrade**
1. Get access to CluedIn application. See [instructions](/paas-operations/upgrade/guide/prepare-for-the-upgrade#get-access-to-cluedin-application).
1. Connect [Helm](/paas-operations/upgrade/guide/required-tools#helm) and [kubectl](/paas-operations/upgrade/guide/required-tools#kubectl) to the CluedIn AKS cluster. See [instructions](/paas-operations/upgrade/guide/prepare-for-the-upgrade#connect-helm-and-kubectl-to-the-cluedin-aks-cluster).
1. Configure [kubectl](/paas-operations/upgrade/guide/required-tools#kubectl). See [instructions](/paas-operations/upgrade/guide/prepare-for-the-upgrade#configure-kubectl).
1. Configure [Helm](/paas-operations/upgrade/guide/required-tools#helm). See [instructions](/paas-operations/upgrade/guide/prepare-for-the-upgrade#configure-helm).
1. (Optional) Connect [Lens or Freelens](/paas-operations/upgrade/guide/required-tools#lens-or-freelens) to your cluster. See [instructions](/paas-operations/upgrade/guide/prepare-for-the-upgrade#connect-lens-to-your-cluedin-cluster).

**Stage 3 – Perform the upgrade**
1. Get current [Helm](/paas-operations/upgrade/guide/required-tools#helm) user values. See [instructions](/paas-operations/upgrade/guide/perform-the-upgrade#get-current-helm-user-values).
1. Prepare new [Helm](/paas-operations/upgrade/guide/required-tools#helm) user values. See [instructions](/paas-operations/upgrade/guide/perform-the-upgrade#prepare-new-helm-user-values).
1. Perform system pre-checks. See [instructions](/paas-operations/upgrade/guide/perform-the-upgrade#perform-system-pre-checks).
1. Perform [Helm](/paas-operations/upgrade/guide/required-tools#helm) upgrade. See [instructions](/paas-operations/upgrade/guide/perform-the-upgrade#perform-helm-upgrade).
1. Verify the upgrade. See [instructions](/paas-operations/upgrade/guide/perform-the-upgrade#verify-the-upgrade).
1. Notify about upgrade completion. See [instructions](/paas-operations/upgrade/guide/perform-the-upgrade#notify-about-upgrade-completion).


