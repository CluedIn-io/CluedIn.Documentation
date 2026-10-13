---
title: Plan the upgrade
url: https://documentation.cluedin.net/operate/upgrade/plan-the-upgrade
content_type: how-to
section: Deploy & operate > Upgrade
---

# Plan the upgrade

> how-to: Steps to accomplish one task.

Careful planning ensures that the upgrade process is efficient, minimizes downtime, and accounts for dependencies across your environment. This page covers stage 1 of the [CluedIn upgrade process](https://documentation.cluedin.net/operate/upgrade/guide.md). It outlines the decisions and preparations you should make before executing the upgrade.

## Get familiar with the versioning scheme 

CluedIn releases version numbers follow this format: **`{year}.{month}.{patch}`**. For example, **`2025.05.02`**.

## Review upgrade-related documentation

When planning the upgrade, consult the following documentation:

- [Release notes](https://documentation.cluedin.net/release-notes.md) – Provide an overview of the updates available in a specific release.

- [Upgrade documentation](https://documentation.cluedin.net/operate/upgrade.md) – CluedIn publishes upgrade documentation with each new release. Be sure to review this documentation in full before beginning the upgrade process. While many upgrades follow common steps, not all are identical, and some may include specialized procedures. 

    Pay particular attention to any infrastructure-related changes, as these may require additional preparation or configuration.

## Schedule the upgrade window

- Schedule downtime – Plan the upgrade during a period when the application is not in use. The application will be unavailable throughout the upgrade process. 

- Allocate sufficient time – Ensure you have enough time for the full upgrade and, if required, disaster recovery.

## Inform the stakeholders
It is essential to keep stakeholders informed at every stage of the upgrade process:

- Before the upgrade – Provide advance notice of the planned upgrade window, expected downtime, and potential business impact. 

- During the upgrade – Provide updates if the upgrade takes longer than anticipated or if issues arise. 

- After the upgrade – Confirm completion, communicate any changes affecting users, and explain how to report issues. 

## Perform a full backup

Back up the following:

- All persistent disks

- All user values

This step is critical in case a rollback becomes necessary.

## Prepare and test custom packages
If you use custom packages, verify that the following steps are completed before upgrading:

- The package developer reviews the [Release notes](https://documentation.cluedin.net/release-notes.md#release-notes) to identify any breaking changes in the new CluedIn version and adapts the code if necessary.

- The packages are compiled and deployed against the new version you plan to upgrade to.

- Package developer tests the packages locally with the new version.

- The packages are available in the feed accessible by the cluster. If the packages are not deployed towards the standard CluedIn feed, add a custom feed.

Up: [Upgrade](https://documentation.cluedin.net/operate/upgrade.md)
