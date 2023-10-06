---
layout: default
nav_order: 1
parent: How-to guides
grand_parent: Installation
permalink: /deployment/infra-how-tos/ama-upgrade
title: AMA upgrade
tags: ["deployment", "ama", "marketplace", "azure"]
last_modified: 2023-10-06
---

In this article, you will learn how to upgrade CluedIn AMA to the new version. You can find the latest chart version [here](https://github.com/CluedIn-io/Charts/releases) and the latest app version [here](https://cluedin-io.github.io/Releases/).

**Important!** Before starting the AMA upgrade, make sure that you have backed up all data and that no processing or export tasks are running.

## Check dependencies

CluedIn is shipped with predefined connectors. They are listed in the **Packages** section in the [release notes](https://cluedin-io.github.io/Releases/) for the needed version. If you are using connectors, check their versions and make sure they match the versions from the needed release.

**To upgrade the package versions**

1. In Lens, go to the needed cluster. Then, go to **Config** > **ConfigMaps** > **cluedin-server-packages**.

1. In the **packages.txt** file, edit the versions so that they are the same as in the release notes. Then, save your changes.

1. Go to **Deployments** > **cluedin-server**, and then restart the server.

    You upgraded the package versions. Now, you can proceed with CluedIn upgrade.

## Check environment configuration

After you upgraded the package versions, check your current environment configuration and get the latest app version.

**To check environment configuration**

1. Make sure that your KUBECONFIG file is set in your current path by running the following command:

    `export KUBECONFIG=~/.kube/mycluster.config`

1. Check if you can connect to the cluster you are upgrading by running the following command:

    `kubectl get no`

    You will get an output similar to the following:
    
    ```
    kubectl get no

    NAME                              STATUS   ROLES   AGE   VERSION
    aks-default-18391074-vmss000000   Ready    agent   79d   v1.23.8
    aks-user-96238571-vmss000009      Ready    agent   29d   v1.23.8
    aks-user-96238571-vmss00000a      Ready    agent   29d   v1.23.8
    ```

    Then, compare the node names with the names in the Azure portal or Lens.

1. Make sure that you can see the current installation by running the following Helm command:

    `helm ls -a -n cluedin`

    You will get an output similar to the following:
    
    ```
    NAME                NAMESPACE   REVISION    UPDATED                                 STATUS      CHART                   APP VERSION
    cluedin-platform    cluedin     1           2023-07-18 14:08:21.6187923 +0100 BST   deployed    cluedin-platform-1.5.0  2023.04
    ```

1. Update your Helm repositories to the latest version by running the following command:

    ```
    helm repo update
    helm search repo cluedin-platform 
    ```

    You will get an output similar to the following:
    
    ```
    NAME                                    CHART VERSION   APP VERSION   DESCRIPTION
    cluedin/cluedin-platform                1.6.0           2023.07       Deploys all parts of the CluedIn platform 
    ```

    **Note:** You will need the `chart version` and `app version` for running the upgrade in the following [procedure](#run-upgrade).

1. If you do not have the previous values, get them by running the following command:

    `helm get values cluedin-platform -n cluedin -o yaml > default-values.yaml` 

    **Note:** If you are pulling the values using Lens, make sure that the **User-Supplied values only** checkbox is selected. Otherwise, you will get more values than you need and may encounter issues when upgrading.
    
## Run upgrade

Now that you have checked the environment configuration and received the latest chart and app versions, run the upgrade.

**Warning!** Upgrading on Azure SQL is a bit different as you must provision an empty DataStore.Db.CleanCache database before proceeding. If this is not there, then the DACPAC install will not create the tables correctly.

**To run the upgrade**

1. Create a patch file (**upgrade-values.yaml**) to update the global image tag to the latest one and set the strategy type to **Recreate**.

    ```
    global:
    image:
    tag: "[XXXX.XX]"
    strategy:
    type: Recreate
    ```
    Normally, this should be the only tag you need to update unless there have been custom image tag overrides in the past. Check your **default-values.yaml** file for any tag customizations.

    **Note:** Depending on the tag you use, you can enable auto-upgrade for CluedIn. If you use the major and minor versions only (e.g., 2023.07), you will get the latest available patch by default, thus enabling the auto-upgrade. If you specify a particular patch (e.g., 2023.07.02), you will get that specific patch, whether it is the latest or not. For the production environment, we recommend that you specify a patch. For the development environment, we recommended that you use the major and minor versions, and thus get the latest patch.

1. Run the `helm upgrade` command as follows:
    
    ```
    helm upgrade -i cluedin-platform -n cluedin cluedin/cluedin-platform 
        --set application.system.runDatabaseJobsOnUpgrade=true
        --version [X.X.X]
        --values default-values.yaml 
        --values upgrade-values.yaml
        --values production-resources.yaml
    ```

    This command runs the database jobs as part of the upgrade (normally these are skipped because they can take a long time to run.)

    **Note:** The order of the --values files matters as the last file will win any override priority so we need the **upgrade-values.yaml** file to follow the **default-values.yaml** file.

    You can find the `version` number in step 4 of [Check environment configuration](#check-environment-configuration) (look for the chart version number).

## Validate upgrade

To validate the upgrade, check the `init-sqlserver` job. This will be running the database upgrades needed for the new version. Then, get the logs of the completed job by running the following command:

`kubectl logs --tail=1000 --selector=job-name=init-sqlserver-job -n cluedin`

This will produce an output similar to the following.

```
🔍 - Checking DB : DataStore.Db.AuditLog .. ✅ - FOUND!
🔍 - Checking DB : DataStore.Db.Authentication .. ✅ - FOUND!
🔍 - Checking DB : DataStore.Db.BlobStorage .. ✅ - FOUND!
🔍 - Checking DB : DataStore.Db.CleanCache .. ✅ - FOUND!
🔍 - Checking DB : DataStore.Db.Configuration .. ✅ - FOUND!
🔍 - Checking DB : DataStore.Db.ExternalSearch .. ✅ - FOUND!
🔍 - Checking DB : DataStore.Db.Metrics .. ✅ - FOUND!
🔍 - Checking DB : DataStore.Db.MicroServices .. ✅ - FOUND!
🔍 - Checking DB : DataStore.Db.OpenCommunication .. ✅ - FOUND!
🔍 - Checking DB : DataStore.Db.TokenStore .. ✅ - FOUND!
🔍 - Checking DB : DataStore.Db.Training .. ✅ - FOUND!
🔍 - Checking DB : DataStore.Db.WebApp .. ✅ - FOUND!

🏃‍ - Running POST-INSTALL script : [340_1_MultiTenantRoleUpdate.sql] on [DataStore.Db.Authentication]
(0 rows affected) (0 rows affected) (0 rows affected) (0 rows affected) (0 rows affected) (0 rows affected) (0 rows affected) (0 rows affected) (0 rows affected) (0 rows affected) (0 rows affected) (0 rows affected)

🏃‍ - Running POST-INSTALL script : [350_1_PageTemplateMigration.sql] on [DataStore.Db.OpenCommunication]
(4 rows affected) (5 rows affected) (0 rows affected) (0 rows affected)

🏃‍ - Running POST-INSTALL script : [350_2_EntityTypeRouteFix.sql] on [DataStore.Db.OpenCommunication]
(0 rows affected) (0 rows affected)


🥇 - MS SQL Ready for visitors..
👋 - All done. Bye !
```

**What to check after upgrade?**

- PRE-INSTALL scripts have ran without error.

- DACPAC installs have ran without error.

- POST-INSTALL scripts have ran without error.