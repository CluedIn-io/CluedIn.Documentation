---
layout: cluedin
title: Sync certificates and secrets from AKV to AKS
permalink: /kb/sync-aks-to-akv
parent: PaaS operations
tags: ["kubernetes","azure","aks", "akv", "key-vault", "azure"]
last_modified: 2024-02-05
nav_order: 8
headerIcon: "paas"
nav_exclude: true
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

{:.important}
As of Q1 2024, synchronizing certificates and secrtes from AKV to AKS is not currently supported. However, beta versions are available, enabling you to set up and test this functionality before GA release.

In this article, we will guide you through connecting your CluedIn instance to use the existing Azure Key Vault (AKV) to synchronize secrets and certificates to your Kubernetes cluster.

The method described in this article uses the AKV provider for the secrets store CSI driver to facilitate this feature.

Useful links:

- [Azure Key Vault Provider for Secrets Store CSI Driver](https://azure.github.io/secrets-store-csi-driver-provider-azure/)

- [Use the Secrets Store CSI Driver for Kubernetes in an Azure Kubernetes Service (AKS) cluster (preview)](https://docs.microsoft.com/en-us/azure/aks/csi-secrets-store-driver)

Prerequisites

- Powershell Core

- Azure CLI

## Guide

1. Sign in to your tenant to enable the AKV add-on against the AKS.

1. Open up `pwsh` and sign in to your tenant with `az login`.

1. Set up your variables which will be used below.
    ```powershell
    $aks = az aks show --name $aksName --resource-group $aksResourceGroup
    $subscription = '00000000-0000-0000-0000-000000000000' # This will be different guid on your end
    $tenantId = '00000000-0000-0000-0000-000000000000' # This will be different guid on your end

    $keyVaultName = 'kv-012345' # Use your desired key vault name
    $keyVaultRG = 'rg-kv' # Use the resource group the above key vault resides in
    ```

1. Enable the add-on on the existing AKS Cluster.
    ```powershell
    $params = @(
        '--addons', 'azure-keyvault-secrets-provider'
        '--name', $aks.name
        '--resource-group', $aks.resourceGroup
    )
    az aks enable-addons --addons @params
    ```

    This will deploy some additional pods to each available node. Once the add-on has been deployed, it will create a key vault managed identity that is used to communicate back to the AKV from the Kubernetes cluster.

1. To get the managed identity, run the following.
    ```powershell
    $params = @(
        '--name', $aks.name
        '--resource-group', $aks.resourceGroup
        '--subscription', $subscription
        '--query', 'addonProfiles.azureKeyvaultSecretsProvider.identity.objectId'
        '--output', 'tsv'
    )
    $kvManagedIdentity = az aks show @params
    ```

    {:.important}
    Depending on if you're using RBAC or Key Vault access policy, you will need to update the appropriate area so the key vault managed identity can GET and LIST secrets and certificates.

1. Obtain the key vault details.
    ```powershell
    $kv = az keyvault show --name $keyVaultName --resource-group $keyVaultRG | ConvertFrom-Json
    ```

    {:.important}
    This guide assumes you'll use the pre-existing key vault deployed at install time. You may use an alternative key vault if preferred. In this case, update the values above to match your desired key vault.

1. Update access to your key vault.
    - RBAC
    ```powershell
    $params = @(
        '--assignee', $kvManagedIdentity
        '--role', 'Key Vault Secret User'
        '--role', 'Key Vault Certificate User'
        '--scope', $kv.id
    )
    az role assignment create @params
    ```

    - Policy
    ```powershell
    $params = @(
        '--name', $kv.name
        '--resource-group', $kv.resourceGroup
        '--certificate-permissions', 'get'
        '--secret-permissions', 'get'
        '--spn', $kvManagedIdentity
    )
    az keyvault set-policy @params
    ```

    With the above now set, it's time to start uploading your secrets and certificates.

1. Navigate to the Key Vault in the Azure Portal instance and begin adding secrets and certificates. Depending on what you are uploading, select either **Certificates** or **Secrets**.

    - For Certificates: Upload a PFX of your choice along with a password.

    - For Secrets: Create a secret key:value pair. These will be used for synchronization from AKV to Kubernetes secrets. As Kubernetes secrets are an oject that contain multiple key:value pairs, ensure that your naming convention in AKV makes sense.

    **Example**: In Kubernetes, we may have a secret `cluedin-login-details` which contains 2 key:value pairs: `Username`, and `Password`. In AKV, it would be best to have these two secrets as `cluedin-login-username` and `cluedin-login-password`. When we get later into the guide, we'll explain how to pair these back up into a single object.

1. With all your desired secrets and certificates now uploaded to AKV, it's time to configure the `Values.yaml` to begin synchronizing.

    In your values file, add the following block of code into the global values:

    ```yaml
    global:
      keyvault:
        enabled: true # When enabled, it will deploy the secret store manifest to Kubernetes
        #frontendCrt: cluedin-sample-pfx # This must match the certificate name on the AKV end. When mounted, it will appear as `cluedin-frontend-crt`
        userAssignedIdentityID: $kvManagedIdentity # This is the guid for the kv managed identity
        keyvaultName: $kv.name # This is your key vault name
        tenantId: $tenantId # This is the guid of your tenant
        secretProviderClasses:
          cluedin-server: # For every key under `secretProviderClasses`, a new secret provider class will be created with the same name and `-sync` appended
          - secretName: cluedin-login-details # This is how the secret will appear within Kubernetes Secrets once synchronized
            secretType: # [OPTIONAL] Defaults to Opaque. But you can specify any supported secretType
            secretKeys:
              password: cluedin-login-password # The left side (Key) is the name in the Kubernetes secret object. The right side (Value) is the AKV reference which will grab its value
              username: cluedin-login-username

    infrastructure:
      cert-manager:
        #enabled: false # Only set to false if using an uploaded frontend certificate
    ```

    {:.important}
    If you are using the certificate upload as part of your setup, you **must** disable cert-manager by setting `enabled: false`. You also must set `frontendCrt` to a value. It will be mounted as `cluedin-frontend-crt` on `cluedin-server`. This secret name cannot change.

1. With all the secrets and certificates now done, the last step is to mount, map, and synchronize the secrets to Kubernetes.

    For every key under `secretProviderClass`, a new secret provider will be created with the same name with `-sync` appended. This gives you the flexibility to have secrets to share the same life cycle as an application, or to use a singular pod to synchronize the secrets.

    `cluedin-server` is the only server that will automount if keys are specified under the `cluedin-server` secretProviderClasses section. For everything else, a specific mount point will be required along with preventing local password creation by using the appropriate key.

    We **highly recommend** having secrets share life cycles with the application. We will cover only this scenario below.

    Please see the mapping table below.

    | Application | Secret | Helm Path | Mount Point |
    | --- | --- | --- | --- |
    | cluedin-server | cluedin-admin-secret | `application.bootstrap.organization.existingSecret` | auto-mounts |
    | | cluedin-email | `application.email.secretRef` | |
    | | cluedin-frontend-crt | `global.keyvault.frontendCrt` | |
    | cluedin-sqlserver | cluedin-sqlserver-secret | `infrastructure.mssql.existingSecret` | `infrastructure.mssql.extraVolumes`<br/>`infrastructure.mssql.extraVolumeMounts` |
    | | cluedin-sqlserver-clientuser-secret | `application.sqlserver.users.clientUser.existingSecret` | |
    | cluedin-elasticsearch | elasticsearch-credentials | `infrastructure.elasticsearch.auth.existingSecret` | `infrastructure.elasticsearch.extraVolumes`<br/>`infrastructure.elasticsearch.extraVolumeMounts` |
    | cluedin-redis | cluedin-redis | `infrastructure.redis.auth.existingSecret` | `infrastructure.redis.master.extraVolumes`<br/>`infrastructure.redis.master.extraVolumeMounts` |
    | cluedin-neo4j | cluedin-neo4j-secrets | `infrastructure.neo4j.neo4j.passwordFromSecret` | `infrastructure.neo4j.additionalVolumes`<br/>`infrastructure.neo4j.additionalVolumeMounts` |
    | | cluedin-neo4j-auth | `!! shared from above !!` | |
    | cluedin-grafana | cluedin-grafana | `infrastructure.monitoring.grafana.admin.existingSecret` | `infrastructure.monitoring.grafana.extraContainerVolumes`<br/>`infrastructure.monitoring.grafana.sidecar.dashboards.extraMounts` |
    | cluedin-rabbitmq | cluedin-rabbitmq | `infrastructure.rabbitmq.auth.existingPasswordSecret` | `infrastructure.rabbitmq.extraVolumes`<br/>`infrastructure.rabbitmq.extraVolumeMounts` | 
    | | cluedin-rabbitmq-load-definition | `!! shared from above !!` | |

    Please find a sample yaml file <a href="../../assets/other/akv-sync-sample.yaml" download>here</a>, which can be used as a reference for a complete setup.

## Technical notes

This section will explain some of the more technical bits:

- The secret csi driver is deployed at the Kubernetes level. This deploys some additional pods to each node to facilitate this. However, if your max pods limit is the default `30`, you may run into an issue after deploying as the CluedIn application is on the borderline of this value. Please ensure this is checked before proceeding as it may cause the cluster to not function correctly. 

- The way the secrets are synchronized is by using the `cluedin-server` pod mounting the secret store or mapping and mounting on other pods. The sample file and table above explain how to achieve this. It's important to note that the secrets synchronize only when the pod is active. It doesn't need to be in a running state, but it must at least be pending. This is a limitation of the CSI driver itself rather than the solution provided by CluedIn.

- The secrets synchronized do not overwrite existing secrets that are created by the CluedIn Installer. If your secret matches the same name (front-end certificate is mandatory here), you must remove the existing secret for the synchronized secret to take over. 

- Please ensure that you have enough resources. For example, by default the Neo4j and Elasticsearch pods consume a majority of the nodes they have been assigned. Having the additional Key Vault pods on these nodes may potentially prevent these from starting up even though the Key Vault pods request very little resource.

## Known issues

This section will explain some of the known issues.

**Issue 1**

Problem: When doing a migration of RabbitMQ from local kubernetes password to a synced password, you must do a sequence of steps due to the RabbitMQ charts logic.

Solution:
  
  1. Do an initial deployment where the secret is mounted and mapped to RabbitMQ pod as well as the initial password being supplied in the User Supply Values for RabbitMQ. 

  1. Once deployed and you can see the secretProviderClass, delete the existing rabbitMQ secrets and then kill the RabbitMQ pod. A new pod should spawn and the secrets should then be mapped to the secretProviderClass.

  1. Update User Supply Values to remove the password and update it to use an existing one. Redeploy the config, and this time it should succeed as the sychronised secret will exist at deployment time.

  **Note**: This is only an issue with migration. Fresh installs do not have this issue.

**Issue 2**

Problem: Not all secrets work from a synced source.

Solution: Unfortunately, not all secrets will work from AKV. An example of this is the `acr-registry-credentials` secret. For a secret to be synchronized, it must first be mounted to a pod. However, you cannot pull the image for the pod if the secret does not exist. There are ways around this such as having a generic pod that is deployed pre-helm install, but this is not a scenario we support.