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

This section provides step-by-step instructions to apply the new version of CluedIn safely and verify that the upgrade completes successfully.

{:.important}
Before you begin, make sure that you have completed all actions outlined in [Plan the upgrade](/paas-operations/upgrade/guide/plan-the-upgrade) and [Prepare for the upgrade](/paas-operations/upgrade/guide/prepare-for-the-upgrade).

The upgrade steps may vary depending on the release. The following steps are part of the typical process: 

  1. Get current values 
  1. Setup new values 
  1. System Pre-Checks
  1. Helm upgrade (Basic)
  1. Helm upgrade with Data Upgrade
  1. Verify upgrade 

-----------

## Get current Helm user values

The Helm user values file is a YAML file which defines the configuration values to be apply when upgrading a Kubernetes cluster. The user value file will look something like this: 

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

{:.important}
We recommend using the following format for naming your user values files: 
values-{environment}-{release-version}.yml 

  - {environment} = the target environment (e.g., dev, staging, prod). 
  - {release-version} = the release identifier, written as a hyphen-separated date or version number. 

Example: 
For release 2024.12.02 on the dev environment, the file should be named: 
 
```
values-dev-2024-12-02.yml 
```

To get your helm user values run the following command in powershell (substitute your environment and release number): 
 
```powershell
helm get values cluedin-platform -n cluedin -o yaml > ./ values-<environment>-<release-version>.yml 
```

  - The YAML file will be created in your working directory. Open it in your preferred IDE (we typically use Visual Studio Code). 
  - The file should resemble the provided example. If it appears empty, this usually means you are not connected to the cluster correctly. In that case, revisit the earlier steps to confirm your connection. 

-----------

## Prepare new Helm user values 

The required values for the target release are published in the CluedIn documentation. Before proceeding, carefully confirm that your current release is compatible with the target release. Once verified, duplicate the values file created in the previous step and rename it to match the target release. 

Example: 
To go to release 2025.05.00 on the dev environment, the file should be named: 
 
```
values-dev-2025-05-00.yml 
```

Carefully review your existing values file against the new release values. Replace any outdated entries with the updated ones, and add any values that are newly introduced. In most cases, you will be updating image tags and package versions, but additional configuration keys may also be required. Be especially mindful of YAML indentation, as incorrect spacing will cause errors during deployment. 

An IDE such as Visual Studio Code will highlight any formatting or indentation issues as you edit the YAML file. Once everything looks correct, save the file. 

Based on the earlier example, your YAML file should now look like this: 
 
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

Before starting an upgrade, ensure the following checks are completed:

  - [Verify that the UI](/paas-operations/upgrade/guide/common-upgrade-operations#check-cluedin-ui) is running correctly.
  - Confirm that [all pods](/paas-operations/upgrade/guide/common-upgrade-operations#check-cluedin-pods) are in a healthy (green) state.
  - Review the [server logs](/paas-operations/upgrade/guide/common-upgrade-operations#check-cluedin-logs) and ensure they are free of errors.

If any issues are detected, it is recommended to resolve them before proceeding with the upgrade. In some cases, the upgrade itself may address certain problems, but when uncertain, seek advice from CluedIn Support.

**Check CluedIn Workload**
Determine whether CluedIn is currently processing a high volume of data. If the system is under heavy load, it is generally advisable to allow all data to finish processing before performing the upgrade.

Any data still in the queues should remain forward-compatible, but minimizing workload reduces risk during the upgrade process.

Check the internal [CluedIn queues](/paas-operations/upgrade/guide/common-upgrade-operations#check-cluedin-queues).

## Perform Helm upgrade

### Basic Helm upgrade

During a Helm upgrade, the UI will be temporarily unavailable. Please notify all users in advance so they are aware of the downtime. 

A standard CluedIn upgrade typically results in 20–30 minutes of downtime. If the upgrade includes data migrations or additional updates, the outage may take longer. 

**Verify the Current CluedIn Helm Chart Version** 
Run the following command to list all Helm releases in the cluedin namespace: 

```powershell
helm list -a -n cluedin 
```

The output will display the currently installed chart version. For example: 

```powershell
cluedin-platform-2.5.1 
```

This indicates that the current Helm chart version in use is **2.5.1**. 
 
**Prepare the Helm Command** 
The exact Helm command for the current update will be provided in the target documentation. In general, the command follows this structure: 

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

**Parameter details:** 
  - {CluedInChartVersion} – The target chart version specified in the documentation. 
  - ${CustomValues} – The full path to the user values file you created in the previous step. 
  - runDatabaseJobsOnUpgrade=true – Ensures the database is refreshed during the upgrade. 
  - runNugetFullRestore=true – Ensures all packages are fully restored. 
  - --timeout 10m0s – A best practice is to allow a 10-minute timeout. If the upgrade fails due to a timeout, please follow the documented mitigation steps. 

**Run the Helm Command** 
When you are ready, execute the Helm command in PowerShell. 

The PowerShell prompt will remain active for several minutes—this is expected. Please be patient while the process runs. 

During the upgrade, the Helm release status will progress through the following states: 

 - Active → Pending Upgrade → Upgrading 

Allow the process to complete without interruption. 

**Helm Command Completed**
After about **10 minutes**, the Helm command in PowerShell should complete and display a confirmation message. This indicates that the Helm command executed successfully. 

However, while the Helm upgrade itself will be finished, some pods may still be starting up. It can take an additional **10–15** minutes for all pods to become fully healthy (green). 

**Finally**
Check the cluedin helm chart version has matches the target version.

```powershell
helm list -a -n cluedin 
```

The output should display the new installed chart version. For example: 

```powershell
cluedin-platform-2.5.2 
```

The following sections outline common operational tasks, along with typical failure scenarios and their mitigations.

### Helm upgrade with data upgrade
This step should only be executed if explicitly directed, and it replaces the step above titled “Helm Upgrade (Basic).”

In some cases, an upgrade also requires changes to the underlying data. When this occurs, CluedIn must be placed into Upgrade Mode during installation.

{:.important}
**Upgrade Mode** Upgrade Mode ensures that no data is ingested or processed while the upgrade is in progress, preventing inconsistencies and maintaining data integrity.

During this upgrade, the UI will be disabled. Please notify all users in advance so they are aware of the downtime. 

A standard CluedIn upgrade typically results in 20–30 minutes of downtime. If the upgrade includes data migrations or additional updates or large volumes of data, the outage may take longer. 

**Verify the Current CluedIn Helm Chart Version** 
Run the following command to list all Helm releases in the cluedin namespace: 

```powershell
helm list -a -n cluedin 
```

The output will display the currently installed chart version. For example: 

```powershell
cluedin-platform-2.5.1 
```

This indicates that the current Helm chart version in use is **2.5.1**. 

```powershell
# ${CustomValues} refers to the values file you have amended with the above changes. Please type the full path here. 

helm upgrade cluedin-platform -n cluedin cluedin/cluedin-platform \
     --version {CluedInChartVersion} \ 
     --values ${CustomValues} \ 
     --set application.system.upgradeMode=true \
     --set application.system.runDatabaseJobsOnUpgrade=true \
     --set application.system.runNugetFullRestore=true \
     --wait \
     --timeout 10m0s
```

**Parameter details:** 
  - {CluedInChartVersion} – The target chart version specified in the documentation. 
  - ${CustomValues} – The full path to the user values file you created in the previous step.
  - upgradeMode=true - Ensures no data is ingested or processed 
  - runDatabaseJobsOnUpgrade=true – Ensures the database is refreshed during the upgrade. 
  - runNugetFullRestore=true – Ensures all packages are fully restored. 
  - --timeout 10m0s – A best practice is to allow a 10-minute timeout. If the upgrade fails due to a timeout, please follow the documented mitigation steps. 

After a few minutes, it should successfully complete.

**Validation**
  - Wait until deployment finishes. Make sure that all pods are healthy and all jobs are completed.
  - Don’t proceed further if any of the pods have health issues. 

**Run Data Upgrade**
The data upgrade requires a trigger which is applied by running the following command:

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

**Validation**
Check the CluedIn server pod logs. The logs should display the following (Version450 label will vary):

```powershell
[#098 05:57:02 INF] Performing Upgrade Scenario Apply DataSource and Manual Data Entry Project Owners Upgrade for version Version450
[#090 05:57:03 INF] Completed Upgrade Scenario Apply DataSource and Manual Data Entry Project Owners Upgrade for version Version450
[#090 05:57:03 INF] Performing Upgrade Scenario Elastic search upgrade mapping for version Version450
[#095 05:57:04 INF] Completed Upgrade Scenario Elastic search upgrade mapping for version Version450
[#095 05:57:04 INF] HTTP POST /api/upgradeto/Version450 responded 200 in 1857.3003 ms
```

**responded 200** indicates a successful upgrade.

**Finalise Upgrade**
CluedIn must now be taken back out of *Upgrade Mode* to bring CluedIn back online. Run the following command:

```powershell
 # ${CustomValues} refers to the values file you have amended with the above changes. Please type the full path here.

 helm upgrade cluedin-platform -n cluedin cluedin/cluedin-platform \
   --version {CluedInChartVersion} \ 
   --values ${CustomValues} \ 
   --set application.system.upgradeMode=false \
   --set application.system.runDatabaseJobsOnUpgrade=false \
   --set application.system.runNugetFullRestore=false
```

After a few minutes the command should complete.

## Verify the upgrade
You can monitor progress by checking: 

  - [CluedIn pods](/paas-operations/upgrade/guide/common-upgrade-operations#check-cluedin-pods)
  - [CluedIn server logs](/paas-operations/upgrade/guide/common-upgrade-operations#check-cluedin-logs)

When checking the server logs, look for the following message: 

```
Application started
``` 

This indicates a successful startup, finally check the [CluedIn UI](/paas-operations/upgrade/guide/common-upgrade-operations#check-cluedin-ui) and ensure everything is running smoothly.

## Notify about upgrade completion
[TBD]