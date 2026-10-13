---
title: Upgrade guide
url: https://documentation.cluedin.net/operate/upgrade/guide
content_type: how-to
section: Deploy & operate > Upgrade
---

# Upgrade guide

> how-to: Steps to accomplish one task.

This guide provides instructions for upgrading CluedIn after the initial [installation](https://documentation.cluedin.net/operate.md). Regular upgrades are recommended to ensure you benefit from the latest features, improvements, and fixes. For details about the updates available in a specific release, see [Release notes](https://documentation.cluedin.net/release-notes.md).

The upgrade process typically involves the steps outlined below.

> **Important:** If issues occur during the upgrade, see [Resolve common upgrade issues](https://documentation.cluedin.net/operate/upgrade/resolve-common-upgrade-issues.md) for troubleshooting instructions.

![Upgrade process in four stages: 0 prepare the prerequisites, 1 plan the upgrade, 2 prepare for the upgrade, 3 perform the upgrade, each with its sequence of tasks](https://documentation.cluedin.net/assets/images/paas-operations/upgrade/upgrade_process_6.png)

**Prerequisites for upgrade**

Before starting an upgrade, make sure you have the following in place: 

1. Access to live CluedIn application.
1. Access to [Azure Kubernetes Service (AKS)](https://documentation.cluedin.net/operate/upgrade/required-tools.md#azure-kubernetes-service) cluster.
1. Access to the [kubeconfig file](https://documentation.cluedin.net/operate/upgrade/required-tools.md#kubeconfig-file) – this must be provided by your Azure administrator.
1. A machine or a virtual machine (VM).
1. All the [required tools](https://documentation.cluedin.net/operate/upgrade/required-tools.md) installed on the machine/VM.
1. Valid and trusted SSL certificates for the environment.

**Stage 1 – Plan your upgrade**
1. Get familiar with the versioning scheme. See [instructions](https://documentation.cluedin.net/operate/upgrade/plan-the-upgrade.md#get-familiar-with-the-versioning-scheme).
1. Review upgrade-related documentation. See [instructions](https://documentation.cluedin.net/operate/upgrade/plan-the-upgrade.md#review-upgrade-related-documentation).
1. Schedule the upgrade window. See [instructions](https://documentation.cluedin.net/operate/upgrade/plan-the-upgrade.md#schedule-the-upgrade-window).
1. Inform the stakeholders. See [instructions](https://documentation.cluedin.net/operate/upgrade/plan-the-upgrade.md#inform-the-stakeholders).
1. Perform a full backup. See [instructions](https://documentation.cluedin.net/operate/upgrade/plan-the-upgrade.md#perform-a-full-backup).
1. Prepare and test custom packages. See [instructions](https://documentation.cluedin.net/operate/upgrade/plan-the-upgrade.md#prepare-and-test-custom-packages).

**Stage 2 – Prepare for the upgrade**
1. Get access to CluedIn application. See [instructions](https://documentation.cluedin.net/operate/upgrade/prepare-for-the-upgrade.md#get-access-to-cluedin-application).
1. Prepare the kubeconfig file. See [instructions](https://documentation.cluedin.net/operate/upgrade/prepare-for-the-upgrade.md#prepare-the-kubeconfig-file).
1. Configure [kubectl](https://documentation.cluedin.net/operate/upgrade/required-tools.md#kubectl). See [instructions](https://documentation.cluedin.net/operate/upgrade/prepare-for-the-upgrade.md#configure-kubectl).
1. Configure [Helm](https://documentation.cluedin.net/operate/upgrade/required-tools.md#helm). See [instructions](https://documentation.cluedin.net/operate/upgrade/prepare-for-the-upgrade.md#configure-helm).
1. (Optional) Connect [Lens or Freelens](https://documentation.cluedin.net/operate/upgrade/required-tools.md#lens-or-freelens) to your cluster. See [instructions](https://documentation.cluedin.net/operate/upgrade/prepare-for-the-upgrade.md#connect-lens-or-freelens-to-your-cluedin-cluster).

**Stage 3 – Perform the upgrade**
1. Get current Helm user values. See [instructions](https://documentation.cluedin.net/operate/upgrade/perform-the-upgrade.md#get-current-helm-user-values).
1. Prepare new Helm user values. See [instructions](https://documentation.cluedin.net/operate/upgrade/perform-the-upgrade.md#prepare-new-helm-user-values).
1. Perform system pre-checks. See [instructions](https://documentation.cluedin.net/operate/upgrade/perform-the-upgrade.md#perform-system-pre-checks).
1. Perform Helm upgrade. See [instructions](https://documentation.cluedin.net/operate/upgrade/perform-the-upgrade.md#perform-helm-upgrade).
1. Verify the upgrade. See [instructions](https://documentation.cluedin.net/operate/upgrade/perform-the-upgrade.md#verify-the-upgrade).
1. Notify about upgrade completion. See [instructions](https://documentation.cluedin.net/operate/upgrade/perform-the-upgrade.md#notify-about-upgrade-completion).

**Useful resources**
- [Resolve common upgrade issues](https://documentation.cluedin.net/operate/upgrade/resolve-common-upgrade-issues.md)
- [Common upgrade operations](https://documentation.cluedin.net/operate/upgrade/common-upgrade-operations.md)
- [Release notes](https://documentation.cluedin.net/release-notes.md)

Up: [Upgrade](https://documentation.cluedin.net/operate/upgrade.md)
