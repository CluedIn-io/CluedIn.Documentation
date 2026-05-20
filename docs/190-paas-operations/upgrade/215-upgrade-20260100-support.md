---
layout: cluedin
nav_order: 1
parent: "2026.01.00"
grand_parent: Upgrade
permalink: /paas-operations/upgrade/2026-01-00/support
title: "2026.01.00 Support"
tags: ["upgrade", "software", "2026.01.00 support", "2.7.0", "4.7.0"]
headerIcon: "paas"
---
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

This document covers the upgrade process for 2026.01.00 to its support update.

{:.important}
We do not support upgrading directly to this version from prior to 2026.01.00.

## Prerequisites
- Access to the Helm chart version `2.7.0`. You may need to run `helm repo update` to grab the latest version.
- [kubectl](/paas-operations/upgrade/guide/required-tools#kubectl)
- [Helm](/paas-operations/upgrade/guide/required-tools#helm)

## Guide

{:.important}
Before any upgrade takes place, ensure you have taken a snapshot or **backup of all your running PVCs** in your AKS cluster. This is very important as databases may be upgraded during this process.

### Stage 1: Prepare for upgrade

  1. Connect to your cluster using the kubeconfig.

  1. Export your current Helm values file. Keep one copy for the upgrade process and another as a backup.

  1. In the values file, update the following properties:

      ```yaml
      application:
        datasourceProcessing:
          image:
            tag: 4.7.0-update.118

        datasource:
          image:
            tag: 4.7.0-update.118

        submitter:
          image:
            tag: 4.7.0-update.118

        gql:
          image:
            tag: 4.7.0-update.32

        ui:
          image:
            tag: 4.7.0-update.98

      infrastructure:
        neo4J:
          image:
            tag: 4.7.0-update.3

      global:
        containerImages:
          initSql:
            image:
              tag: 4.7.0-update.3
          initNeo4J:
            image:
              tag: 4.7.0-update.3

      ```
  1. Apply the values file from your shell by running the following:

      ```bash
      # ${CustomValues} refers to the values file you have amended with the above changes. Please type the full path here.

      helm upgrade cluedin-platform -n cluedin cluedin/cluedin-platform \
          --version 2.7.0 \
          --values ${CustomValues} \
          --set application.system.runDatabaseJobsOnUpgrade=true \
          --set application.system.runNugetFullRestore=true \
          --wait \
          --timeout 10m0s
      ```
      After a few minutes, it should complete successfully.

1. Wait until the deployment finishes.

1. Perform the validation:

    - Make sure that all pods are healthy and all jobs are completed.
    
    - Ensure that there are no errors in the pod logs.

If there are any issues during the upgrade process, please do not hesitate to reach out to CluedIn support.