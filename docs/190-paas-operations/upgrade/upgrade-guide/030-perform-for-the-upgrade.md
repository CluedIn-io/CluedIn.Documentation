---
layout: cluedin
nav_order: 3
parent: CluedIn upgrade guide
grand_parent: Upgrade
permalink: /paas-operations/upgrade/guide/perform-the-upgrade
title: Perform the upgrade
tags: ["deployment", "ama", "marketplace", "azure", "aks", "kubernetes", "upgrade"]
last_modified: 2025-09-22
headerIcon: "paas"
---
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

This page covers stage 3 of the [CluedIn upgrade process](/paas-operations/upgrade/guide). It provides step-by-step instructions to apply the new version of CluedIn safely and verify that the upgrade completes successfully.

{:.important}
Before you begin, make sure that you have completed all actions outlined in [Plan the upgrade](/paas-operations/upgrade/guide/plan-the-upgrade) and [Prepare for the upgrade](/paas-operations/upgrade/guide/prepare-for-the-upgrade).

Keep in mind that upgrade steps may vary depending on the release. The following sequence outlines a typical upgrade process:

1. [Get current Helm user values](#get-current-helm-user-values)

1. [Prepare new Helm user values](#prepare-new-helm-user-values)

1. [Perform system pre-checks](#perform-system-pre-checks)

1. [Perform Helm upgrade](#perform-helm-upgrade)

1. [Verify the upgrade](#verify-the-upgrade)

1. [Notify about upgrade completion](#notify-about-upgrade-completion)

-----------

## Get current Helm user values

The [Helm](/paas-operations/upgrade/guide/required-tools#helm) user values file is a YAML file that defines the configuration values to be applied when upgrading a Kubernetes cluster. The file will look similar to the following:

  ```yaml
    global: 
      image: 
        tag: "2024.12.02" 
      strategy: 
        type: Recreate 

    application: 
      cluedin: 
        image: 
          tag: "2024.12.02" 
        components: 
          packages: 
          - name: "CluedIn.Connector.AzureEventHub" 
            version: "4.0.1" 
          - name: "CluedIn.Connector.Dataverse" 
            version: "4.4.0" 
          - name: "CluedIn.Connector.Http" 
            version: "4.0.0" 
  ```

We recommend the following format for naming your user values files: `values-<environment>-<release-version>.yml`, where:

  - `<environment>` – The target environment (for example, dev, staging, or prod).

  - `<release-version>` – The release identifier, written as a hyphen-separated date or version number. 

For example, for release 2024.12.02 on the dev environment, the file should be named `values-dev-2024-12-02.yml`.

1. To get your Helm user values, run the following command in PowerShell (replace `<environment>` and `<release-version>` with your values): 
 
    ```powershell
    helm get values cluedin-platform -n cluedin -o yaml > ./ values-<environment>-<release-version>.yml 
    ```

1. YAML file is created in your working directory. Open the file in your preferred IDE (we typically use [Visual Studio Code](/paas-operations/upgrade/guide/required-tools#visual-studio-code)). 

1. Check the contents of the file. It should look similar to the example above. If it appears empty, this usually means you are not connected to the cluster correctly. In that case, revisit the earlier steps to verify your connection. 

-----------

## Prepare new Helm user values 

1. The required values for the target release are published in [CluedIn documentation](/paas-operations/upgrade). Before proceeding, carefully verify that your current release is compatible with the target release. Once verified, duplicate the values file created in the previous step and rename it to match the target release. 

    For example, to go to release 2025.05.00 on the dev environment, the file should be named `values-dev-2025-05-00.yml`.

1. Carefully compare your existing values file with the new release’s required values. Update any outdated entries and add newly introduced values:

    - In most cases, you will update container image tags and package versions, but additional configuration keys may also be required.

    - Platform version (specified in `tag`) must align with the specified package versions.

    - To learn which package `version` must be used, see the [Release notes](/release-notes#release-notes) section. The **Release notes** column points to the release details.

        ![release_overview_page]({{ "/assets/images/paas-operations/upgrade/release_overview_page.png" | relative_url }})

        Package versions are listed in the **Packages** section of the release details page.

        ![package_versions]({{ "/assets/images/paas-operations/upgrade/package_versions.png" | relative_url }})

        {:.important}
        If the release includes customer-specific packages, ensure they are compiled against the version of the platform you are deploying. Be aware that breaking API changes may exist and should be addressed in advance.

    - An IDE such as [Visual Studio Code](/paas-operations/upgrade/guide/required-tools#visual-studio-code) will highlight any formatting or indentation issues as you edit the YAML file.

        {:.important}
        YAML is whitespace-sensitive—use spaces (not tabs) and ensure correct indentation, or the deployment will fail.

1. Once everything looks correct, save the file. 

    Based on the [earlier example](#get-current-helm-user-values), your YAML file should now look like this: 
 
      ```yaml
        global: 
          image: 
            tag: "2025.05.00" 
          strategy: 
            type: Recreate 
     
        application: 
          cluedin: 
            components: 
              packages: 
              - name: "CluedIn.Connector.AzureEventHub" 
                version: "4.5.0" 
              - name: "CluedIn.Connector.Dataverse" 
                version: "4.5.0" 
              - name: "CluedIn.Connector.Http" 
                version: "4.5.0" 
      ```

-----------

## Perform system pre-checks

1. Complete the following checks:

    - [Verify](/paas-operations/upgrade/guide/common-upgrade-operations#check-cluedin-ui) that CluedIn UI is running correctly.

    - [Confirm](/paas-operations/upgrade/guide/common-upgrade-operations#check-cluedin-pods) that all pods are in a healthy (green) state.

    - [Review](/paas-operations/upgrade/guide/common-upgrade-operations#check-cluedin-logs) the server logs and ensure they are free of errors.

    If any issues are detected, it is recommended to resolve them before proceeding with the upgrade. In some cases, the upgrade itself may address certain problems, but if you're uncertain, it’s best to consult CluedIn support team for guidance.

1. Check CluedIn workload. Determine whether CluedIn is currently processing a high volume of data. If the system is under heavy load, it is best to allow all data to finish processing before performing the upgrade.

    Although any data still in the queues should remain forward-compatible, reducing the workload helps minimize risk during the upgrade.

1. [Check](/paas-operations/upgrade/guide/common-upgrade-operations#check-cluedin-queues) internal CluedIn queues.

## Perform Helm upgrade

There are several methods to upgrade [Helm](/paas-operations/upgrade/guide/required-tools#helm):

- [Basic Helm upgrade](#basic-helm-upgrade) – This is the default method. Use it unless you are explicitly instructed otherwise.

- [Helm upgrade with data upgrade](#helm-upgrade-with-data-upgrade) – Use this method only when specifically instructed to do so.

### Basic Helm upgrade

During a [Helm](/paas-operations/upgrade/guide/required-tools#helm) upgrade, the UI will be temporarily unavailable. Make sure to notify all users in advance so that they are aware of the downtime. 

A standard CluedIn upgrade typically results in 20–30 minutes of downtime. If the upgrade includes data migrations or additional updates, the outage may take longer. 

1. Check the current CluedIn Helm chart version. To do this, run the following command to list all Helm releases in the `cluedin` namespace: 

    ```powershell
    helm list -a -n cluedin 
    ```

    The output will display the currently installed chart version. For example: 

    ```powershell
    cluedin-platform-2.5.1 
    ```

    This sample output indicates that the current Helm chart version in use is **2.5.1**. 
 
1. Prepare the Helm command. The exact Helm command for the current update will be provided in the target documentation. In general, the command follows this structure: 

    ```powershell
    # ${CustomValues} refers to the values file you have amended with the above changes. Please type the full path here. 
    
    helm upgrade cluedin-platform -n cluedin cluedin/cluedin-platform \ 
        --version {CluedInChartVersion} \ 
        --values ${CustomValues} \ 
        --set application.system.runDatabaseJobsOnUpgrade=true \ 
        --set application.system.runNugetFullRestore=true \ 
        --wait \ 
        --timeout 10m0s 
    ```

    Parameter details: 
    - `{CluedInChartVersion}` – The target chart version specified in the documentation.

    - `${CustomValues}` – The full path to the user values file you created in the previous step. 
 
    - `runDatabaseJobsOnUpgrade=true` – Ensures that the database is refreshed during the upgrade.

    - `runNugetFullRestore=true` – Ensures that all packages are fully restored. 

    - `--timeout 10m0s` – A best practice is to allow a 10-minute timeout. If the upgrade fails due to a timeout, follow the documented mitigation steps. 

1. When you are ready, execute the Helm command in PowerShell. 

    - The PowerShell prompt will remain active for several minutes—this is expected. Please be patient while the process runs.

    - During the upgrade, the Helm release status will progress through the following states: Active → Pending Upgrade → Upgrading. 

1. Allow the process to complete without interruption.

    - After about **10 minutes**, the Helm command in PowerShell should complete and display a confirmation message. This indicates that the Helm command executed successfully. 

    - However, while the Helm upgrade itself will be finished, some pods may still be starting up. It can take an additional **10–15** minutes for all pods to become fully healthy (green). 

1. Verify that CluedIn Helm chart version matches the target version. Run the following command:

    ```powershell
    helm list -a -n cluedin 
    ```

    The output should display the newly installed chart version. For example: 

    ```powershell
    cluedin-platform-2.5.2 
    ```

### Helm upgrade with data upgrade

In some cases, an upgrade also requires changes to the underlying data. When this occurs, CluedIn must be placed into the Upgrade Mode during installation. Upgrade Mode ensures that no data is ingested or processed while the upgrade is in progress, preventing inconsistencies and maintaining data integrity.

During a [Helm](/paas-operations/upgrade/guide/required-tools#helm) upgrade, the UI will be temporarily unavailable. Make sure to notify all users in advance so that they are aware of the downtime. 

A standard CluedIn upgrade typically results in 20–30 minutes of downtime. If the upgrade includes data migrations or additional updates, the outage may take longer.

{:.important}
Use this method of upgrading Helm only if you are explicitly instructed to do so. It replaces the steps provided in [Basic Helm upgrade](#basic-helm-upgrade).

1. Verify the current CluedIn Helm chart version. Run the following command to list all Helm releases in the `cluedin` namespace: 

    ```powershell
    helm list -a -n cluedin 
    ```

    The output will display the currently installed chart version. For example: 

    ```powershell
    cluedin-platform-2.5.1 
    ```

    This sample output indicates that the current Helm chart version in use is **2.5.1**. 

1. Prepare the Helm command:
    ```powershell
    # ${CustomValues} refers to the values file you have amended above. Enter the full path here. 
    
    helm upgrade cluedin-platform -n cluedin cluedin/cluedin-platform \
         --version {CluedInChartVersion} \ 
         --values ${CustomValues} \ 
         --set application.system.upgradeMode=true \
         --set application.system.runDatabaseJobsOnUpgrade=true \
         --set application.system.runNugetFullRestore=true \
         --wait \
         --timeout 10m0s
    ```

    Parameter details:

    - `{CluedInChartVersion}` – The target chart version specified in the documentation.

    - `${CustomValues}` – The full path to the user values file created in the [previous step](#prepare-new-helm-user-values ).

    - `upgradeMode=true` – Ensures no data is ingested or processed during the upgrade.

    - `runDatabaseJobsOnUpgrade=true` – Ensures the database is refreshed as part of the upgrade.

    - `runNugetFullRestore=true` – Ensures all packages are fully restored. 

    - `--timeout 10m0s` – Allows a 10-minute timeout (recommended). If the upgrade fails due to a timeout, follow the documented mitigation steps. 

1. Run the command. After a few minutes, it should successfully complete.

1. Wait until the deployment finishes. Make sure that all pods are healthy and all jobs are completed.

    {:.important}
    Do not proceed further if any of the pods have health issues. 

1. Run the data upgrade. The data upgrade requires a trigger which is applied by running the following command:

    ```yaml
    kubectl apply -f - <<EOF
    apiVersion: api.cluedin.com/v1
    kind: DataUpgrade
    metadata:
      annotations:
        meta.helm.sh/release-name: cluedin-platform
        meta.helm.sh/release-namespace: cluedin
      labels:
        app: cluedin
        app.kubernetes.io/instance: cluedin-platform
        app.kubernetes.io/managed-by: Helm
        app.kubernetes.io/name: application
        helm.sh/chart: application-2.5.1
        release: cluedin-platform
      name: data-upgrade-450
      namespace: cluedin
    spec:
      toVersion: Version450
    EOF
    ```

1. Check the CluedIn server pod logs. The logs should display the following (the `Version450` label will vary):

    ```powershell
    [#098 05:57:02 INF] Performing Upgrade Scenario Apply DataSource and Manual Data Entry Project Owners Upgrade for version Version450
    [#090 05:57:03 INF] Completed Upgrade Scenario Apply DataSource and Manual Data Entry Project Owners Upgrade for version Version450
    [#090 05:57:03 INF] Performing Upgrade Scenario Elastic search upgrade mapping for version Version450
    [#095 05:57:04 INF] Completed Upgrade Scenario Elastic search upgrade mapping for version Version450
    [#095 05:57:04 INF] HTTP POST /api/upgradeto/Version450 responded 200 in 1857.3003 ms
    ```

    The `responded 200` part indicates a successful upgrade.

1. Finalise the upgrade. CluedIn must now be taken back out of the Upgrade Mode. To bring CluedIn back online, run the following command:

    ```powershell
     # ${CustomValues} refers to the values file you have amended above. Enter the full path here.
    
     helm upgrade cluedin-platform -n cluedin cluedin/cluedin-platform \
       --version {CluedInChartVersion} \ 
       --values ${CustomValues} \ 
       --set application.system.upgradeMode=false \
       --set application.system.runDatabaseJobsOnUpgrade=false \
       --set application.system.runNugetFullRestore=false
    ```

    After a few minutes, the command should complete.

## Verify the upgrade

1. To monitor the upgrade progress, check the following: 

    - [CluedIn pods](/paas-operations/upgrade/guide/common-upgrade-operations#check-cluedin-pods)
    - [CluedIn server logs](/paas-operations/upgrade/guide/common-upgrade-operations#check-cluedin-logs)

        When checking the server logs, look for the following message: 

        ```
        Application started
        ``` 

        This indicates a successful startup.

1. Check [CluedIn UI](/paas-operations/upgrade/guide/common-upgrade-operations#check-cluedin-ui) and ensure everything is running smoothly.

## Notify about upgrade completion

Once the upgrade completes and the cluster is back online, send a notification to all relevant teams and stakeholders to inform them that the cluster is ready for use.