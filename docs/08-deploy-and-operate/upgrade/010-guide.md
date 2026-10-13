---
layout: cluedin
title: Upgrade guide
parent: Upgrade
grand_parent: Deploy & operate
nav_order: 10
permalink: /operate/upgrade/guide
content_type: how-to
redirect_from: ["/paas-operations/upgrade/guide"]
source_path: docs/190-paas-operations/upgrade/100-cluedin-upgrade-guide.md
tags: ["deployment", "ama", "marketplace", "azure", "aks", "kubernetes", "upgrade"]
last_modified: 2025-09-22
headerIcon: "paas"
---

This guide provides instructions for upgrading CluedIn after the initial [installation](/operate). Regular upgrades are recommended to ensure you benefit from the latest features, improvements, and fixes. For details about the updates available in a specific release, see [Release notes](/release-notes).

The upgrade process typically involves the steps outlined below.

{:.important}
If issues occur during the upgrade, see [Resolve common upgrade issues](/operate/upgrade/resolve-common-upgrade-issues) for troubleshooting instructions.

![upgrade_process.png]({{ "/assets/images/paas-operations/upgrade/upgrade_process_6.png" | relative_url }})

**Prerequisites for upgrade**

Before starting an upgrade, make sure you have the following in place: 

1. Access to live CluedIn application.
1. Access to [Azure Kubernetes Service (AKS)](/operate/upgrade/required-tools#azure-kubernetes-service) cluster.
1. Access to the [kubeconfig file](/operate/upgrade/required-tools#kubeconfig-file) – this must be provided by your Azure administrator.
1. A machine or a virtual machine (VM).
1. All the [required tools](/operate/upgrade/required-tools) installed on the machine/VM.
1. Valid and trusted SSL certificates for the environment.

**Stage 1 – Plan your upgrade**
1. Get familiar with the versioning scheme. See [instructions](/operate/upgrade/plan-the-upgrade#get-familiar-with-the-versioning-scheme).
1. Review upgrade-related documentation. See [instructions](/operate/upgrade/plan-the-upgrade#review-upgrade-related-documentation).
1. Schedule the upgrade window. See [instructions](/operate/upgrade/plan-the-upgrade#schedule-the-upgrade-window).
1. Inform the stakeholders. See [instructions](/operate/upgrade/plan-the-upgrade#inform-the-stakeholders).
1. Perform a full backup. See [instructions](/operate/upgrade/plan-the-upgrade#perform-a-full-backup).
1. Prepare and test custom packages. See [instructions](/operate/upgrade/plan-the-upgrade#prepare-and-test-custom-packages).

**Stage 2 – Prepare for the upgrade**
1. Get access to CluedIn application. See [instructions](/operate/upgrade/prepare-for-the-upgrade#get-access-to-cluedin-application).
1. Prepare the kubeconfig file. See [instructions](/operate/upgrade/prepare-for-the-upgrade#prepare-the-kubeconfig-file).
1. Configure [kubectl](/operate/upgrade/required-tools#kubectl). See [instructions](/operate/upgrade/prepare-for-the-upgrade#configure-kubectl).
1. Configure [Helm](/operate/upgrade/required-tools#helm). See [instructions](/operate/upgrade/prepare-for-the-upgrade#configure-helm).
1. (Optional) Connect [Lens or Freelens](/operate/upgrade/required-tools#lens-or-freelens) to your cluster. See [instructions](/operate/upgrade/prepare-for-the-upgrade#connect-lens-or-freelens-to-your-cluedin-cluster).

**Stage 3 – Perform the upgrade**
1. Get current Helm user values. See [instructions](/operate/upgrade/perform-the-upgrade#get-current-helm-user-values).
1. Prepare new Helm user values. See [instructions](/operate/upgrade/perform-the-upgrade#prepare-new-helm-user-values).
1. Perform system pre-checks. See [instructions](/operate/upgrade/perform-the-upgrade#perform-system-pre-checks).
1. Perform Helm upgrade. See [instructions](/operate/upgrade/perform-the-upgrade#perform-helm-upgrade).
1. Verify the upgrade. See [instructions](/operate/upgrade/perform-the-upgrade#verify-the-upgrade).
1. Notify about upgrade completion. See [instructions](/operate/upgrade/perform-the-upgrade#notify-about-upgrade-completion).

**Useful resources**
- [Resolve common upgrade issues](/operate/upgrade/resolve-common-upgrade-issues)
- [Common upgrade operations](/operate/upgrade/common-upgrade-operations)
- [Release notes](/release-notes)


