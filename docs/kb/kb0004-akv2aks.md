---
layout: default
title: Sync certificates and secrets from Azure Key Vault to Azure Kubetnetes Service
permalink: /kb/sync-aks-to-akv
nav_exclude: true
tags: ["kubernetes","azure","aks", "akv", "key-vault", "azure"]
last_modified: 2024-02-05
is_kb: true
---
# Introduction

{:.important}
This is not currently supported as of Q1 2024. However, beta versions are available that allow users to set this up and test it before GA release.

In this walkthrough, we will guide you through connecting your CluedIn instance to use the existing Azure Key Vault to synchronize secrets and certificates to your Kubernetes cluster.

This method uses the Azure Key Vault (**AKV**) provider for secrets store CSI driver to facilitate this feature.

Useful links:
* [Azure Key Vault Provider for Secrets Store CSI Driver](https://azure.github.io/secrets-store-csi-driver-provider-azure/)
* [Use the Secrets Store CSI Driver for Kubernetes in an Azure Kubernetes Service (AKS) cluster (preview)](https://docs.microsoft.com/en-us/azure/aks/csi-secrets-store-driver)

# Prerequisites

- Powershell Core
- Azure CLI

# Guide

1. Sign in to your tenant to enable the Azure Key Vault add-on against the AKS.

1. Open up `pwsh` and sign in to your tenant with `az login`.

1. Set up your variables which will be used below:
    ```pwsh
    $aks = az aks show --name $aksName --resource-group $aksResourceGroup
    $subscription = '00000000-0000-0000-0000-000000000000' # This will be different guid on your end.
    $tenantId = '00000000-0000-0000-0000-000000000000' # This will be different guid on your end.

    $keyVaultName = 'kv-012345' # Please use your desired key vault name
    $keyVaultRG = 'rg-kv' # Please use the resource group the above key vault resides in
    ```

1. Enable the add-on on the existing AKS Cluster.
    ```pwsh
    $params = @(
        '--addons', 'azure-keyvault-secrets-provider'
        '--name', $aks.name
        '--resource-group', $aks.resourceGroup
    )
    az aks enable-addons --addons @params
    ```
    {:.important}
    Please note that this will deploy some additional pods to each available node.

    Once the add-on has been deployed, it will create a key vault managed identity that is used to communicate back to the Azure Key Vault from the Kubernetes cluster.

1. To get the managed identity, run the following:
    ```pwsh
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

1. Obtain the key vault details:
    ```pwsh
    $kv = az keyvault show --name $keyVaultName --resource-group $keyVaultRG | ConvertFrom-Json
    ```

    {:.important}
    This guide assumes you'll use the pre-existing key vault deployed at install time. You may use an alternative key vault if preferred. In this case, update the values above to match your desired key vault.

1. Update access to your key vault:
    - RBAC:
    ```pwsh
    $params = @(
        '--assignee', $kvManagedIdentity
        '--role', 'Key Vault Secret User'
        '--role', 'Key Vault Certificate User'
        '--scope', $kv.id
    )
    az role assignment create @params
    ```

    - Policy: 
    ```pwsh
    $params = @(
        '--name', $kv.name
        '--resource-group', $kv.resourceGroup
        '--certificate-permissions', 'get'
        '--secret-permissions', 'get'
        '--spn', $kvManagedIdentity
    )
    az keyvault set-policy @params
    ```

1. With the above now set, it's time to start uploading your secrets and certificates.

1. Navigate to the Key Vault in the Azure Portal instance and begin adding secrets and certificates.  
    Depending on what you are uploading, select either Certificates or Secrets.

    For Certificates:
    Upload a PFX of your choice along with a password

    For Secrets:
    Create a secret key:value pair. These will be used for synchronisation from Azure key vault to Kubernetes secrets.  
    As Kubernetes secrets are an oject that contain multiple key:value pairs, please ensure that your naming convention in AKV makes sense.

    **EXAMPLE**: In Kubernetes we may have a secret `cluedin-login-details` which contains 2 key:value pairs. `Username`, and `Password`.

    In AKV, it would be best to have these two secrets as `cluedin-login-username` and `cluedin-login-password`. 

    When we get later into the guide, we'll explain how to pair these back up into a single object.

1. With all your desired secrets and certificates now uploaded, it's time to configure the `Values.yaml` to begin synchronising.

    In your values file, add the following block of code into the global values:

    ```yaml
    global:
      keyvault:
        enabled: true # When enabled, it will deploy the secret store manifest to Kubernetes
        #frontendCrt: cluedin-sample-pfx # This must match the certificate name on the AKV end. When mounted, it will appear as `cluedin-frontend-crt`
        userAssignedIdentityID: $kvManagedIdentity # This is the guid for the kv managed identity
        keyvaultName: $kv.name # This is your key vault name
        tenantId: $tenantId # This is the guid of your tenant
        secretRanges:
        - secretName: cluedin-login-details # This is how the secret will appear within Kubernetes Secrets once synchronised
          secretType: Opaque # For most secrets, leave as Opaque
          secretKeys:
            password: cluedin-login-password # The left side (Key) is the name in the Kubernetes secret object. The right side (Value) is the AKV reference which will grab its value.
            username: cluedin-login-username

    infrastructure:
      cert-manager:
        #enabled: false # Only set to false if using an uploaded frontend certificate.
    ```
    **NOTE**: If you are using the certificate upload as part of your setup, you **must** disable cert-manager by setting `enabled: false`. You also must set `frontendCrt` to a value. It will be mounted as `cluedin-frontend-crt`. This secret name cannot change.

1. With all the secrets and certificates now done, the last step is to update and `secretRef`'s in your `Values.yaml` or chart to reference the new synchronized secrets.

# Technical Notes
This section will explain some of the more technical bits.

- The secret csi driver is deployed at the Kubernetes level. This deploys some additional pods to each node to facilitate this. However, if your max pods limit is the default `30`, you may run into an issue after deploying as the CluedIn application is on the borderline of this value.  

    Please ensure this is checked before proceeding as it may cause the cluster to not function correctly. 

- The way the secrets are synchronized is by the `cluedin-server` pod mounting the secret store and the secrets referenced above under `secretRanges`. It's important to note that the secrets synchronize only when the pod is active. It doesn't need to be in a running state, but it must at least be pending.  

    This is a limitation of the CSI driver itself rather than the solution provided by CluedIn.

- The secrets synchronized do not override existing secrets that are created by the CluedIn Installer. If your secret matches the same name (front-end certificate is mandatory here), you must remove the existing secret for the synchronized secret to appear.

- Please ensure that you have enough resources. For example, by default the Neo4j and Elasticsearch pods consume a majority of the nodes they have been assigned. Having the additional Key Vault pods on these nodes may potentially prevent these from starting up.