---
layout: default
title: Sync certificates and secrets from Azure Key Vault to Azure Kubetnetes Service
permalink: /kb/sync-aks-to-akv
nav_exclude: true
tags: ["kubernetes","azure","aks", "akv", "key-vault", "azure"]
last_modified: 2021-11-02
---

In this walkthrough, we will create a new Azure Key Vault, and then create a new Azure Kubernetes Service, and then we will synchronize the certificates and secrets from the Azure Key Vault to the Azure Kubernetes Service.

Useful links:
* [Azure Key Vault Provider for Secrets Store CSI Driver](https://azure.github.io/secrets-store-csi-driver-provider-azure/)
* [Use the Secrets Store CSI Driver for Kubernetes in an Azure Kubernetes Service (AKS) cluster (preview)](https://docs.microsoft.com/en-us/azure/aks/csi-secrets-store-driver)


We will use Powershell 7 and assume that all commands run in the same session. So we can start with defining the necessary variables:

```powershell
$SUBSCRIPTION_ID = '...'
$LOCATION = '...'
$RG_NAME = '...'
$AKS_NAME = '...'
$AKV_NAME = '...' # must be globally unique
```

Ensure that we run the commands under the right Subscription:

```powershell
az login
az account set --subscription $SUBSCRIPTION_ID
```

Enable the Secrets Store CSI Driver feature:

```powershell
az feature register --namespace "Microsoft.ContainerService" --name "AKS-AzureKeyVaultSecretsProvider"
```

It will take a while for the feature to be enabled. We can check the status of the feature by running this command:

```powershell
az feature list -o table --query "[?contains(name, 'Microsoft.ContainerService/AKS-AzureKeyVaultSecretsProvider')].{Name:name,State:properties.state}"

# Eventually, it must return "Registered":

# Name                                                         State
# -----------------------------------------------------------  ----------
# Microsoft.ContainerService/AKS-AzureKeyVaultSecretsProvider  Registered
```

Now, re-register the Container Service extension and ensure it is up-to-date:

```powershell
az provider register --namespace Microsoft.ContainerService
az extension add --name aks-preview
az extension update --name aks-preview
```

Create a resource group:

```powershell
az group create --name $RG_NAME --location $LOCATION
```

Create an Azure Key Vault with one secret and one certificate:

```powershell

az keyvault create --name $AKV_NAME --resource-group $RG_NAME --location $LOCATION

az keyvault certificate get-default-policy > policy.json # get the default policy

az keyvault certificate create --name cert-demo --vault-name $AKV_NAME -p "@policy.json"
az keyvault secret set --vault-name $AKV_NAME --name "foo" --value "bar"
```

Next, let's create an Azure Kubernetes Service:

```powershell
az aks create `
  --resource-group $RG_NAME `
  --name $AKS_NAME `
  --node-vm-size Standard_B8ms `
  --node-count 1 ` # AKS creates 3 nodes by default, but for the demo we need only one
  --generate-ssh-keys `
  --network-plugin azure `
  --enable-addons azure-keyvault-secrets-provider ` # enable the Secrets Store CSI Driver
  --enable-managed-identity ;

  # Expected output:

  # {
  #   "aadProfile": null,
  #   "addonProfiles": {
  #     "azureKeyvaultSecretsProvider": {
  #       "config": {
  #         "enableSecretRotation": "false",
  #         "rotationPollInterval": "2m"
  #       },
  #       "enabled": true,
  #       "identity": {
  #         "clientId": "...",
  #         "objectId": "...",
  #         "resourceId": "/subscriptions/.../resourcegroups/MC_resourse-group-name_region/providers/Microsoft.ManagedIdentity/userAssignedIdentities/azurekeyvaultsecretsprovider-aks-name"
  #       }
  #     }
  #   },
```

Pay attention to the `addonProfiles.identity` - a managed identity automatically created in the `MC_` resource group. We will use this identity to connect to the Azure Key Vault.

Let's save the `addonProfiles.identity.cliendId` into a variable:

```powershell
$SERVICE_PRINCIPAL_CLIENT_ID = 'a819baaa-4aeb-43fc-92ce-b367176d5b88'
```

If you update the existing AKS cluster, you will need to run this command in this way:

```powershell
az aks enable-addons --addons azure-keyvault-secrets-provider --name $AKS_NAME --resource-group $RG_NAME
```

While we are here, let's connect to the AKS cluster and enable the secrets auto-rotation:

```powershell
az aks get-credentials --resource-group $RG_NAME --name $AKS_NAME
# check the CSI driver and the store provider statuses
kubectl get pods -n kube-system -l 'app in (secrets-store-csi-driver, secrets-store-provider-azure)'

# Expected output:
# NAME                                     READY   STATUS    RESTARTS   AGE
# aks-secrets-store-csi-driver-h52sr       3/3     Running   0          0h17m
# aks-secrets-store-provider-azure-7qlgd   1/1     Running   0          0h30m

az aks update -g $RG_NAME -n $AKS_NAME --enable-secret-rotation
```

Now, let's allow our managed identity to access the Azure Key Vault:

```powershell
az keyvault set-policy -n $AKV_NAME --secret-permissions get --spn $SERVICE_PRINCIPAL_CLIENT_ID
az keyvault set-policy -n $AKV_NAME --certificate-permissions get --spn $SERVICE_PRINCIPAL_CLIENT_ID
```

These commands let the managed identity read secrets and certificates from the Azure Key Vault.


Our next step is to create a SecretProviderClass - a custom Kubernetes resource that will be used to connect to the Azure Key Vault:

```yaml
# secretproviderclass.yml
apiVersion: secrets-store.csi.x-k8s.io/v1alpha1
kind: SecretProviderClass
metadata:
  name: azure-keyvault-name # use the name of your Azure Key Vault
spec:
  provider: azure
  secretObjects:
  # The following section describes how AKV secret is mapped to the Kubernetes secret:
  - secretName: foo
    type: Opaque
    data:
    - objectName: foo
      key: foo
  # If we store a certificate as a Kubernetes secret, the secret type must be kubernetes.io/tls
  - secretName: cert-demo
    type: "kubernetes.io/tls"
    data:
    - objectName: cert-demo
      key: tls.key
    - objectName: cert-demo
      key: tls.crt
  parameters:
    keyvaultName: "azure-keyvault-name" # The name of the Azure Key Vault
    useVMManagedIdentity: "true"         
    userAssignedIdentityID: "..." # The clientId of the addon-created managed identity
    # this section describes the objects pulled from Azure Key Vault
    objects:  |
      array:
        - |
          objectName: foo
          objectType: secret
        - |
          objectName: cert-demo
          objectType: secret
    # the tenant ID containing the Azure Key Vault instance, you can find it in Azure Portal
    tenantId: "..." 
```

Apply the SecretProviderClass:

```powershell
kubectl apply -f ./secretproviderclass.yml
```

Finally, let's test it:

Create a `test-pod.yml` with the following content:

```yaml
kind: Pod
apiVersion: v1
metadata:
  name: busybox-secrets-store-inline
spec:
  containers:
  - name: busybox
    image: k8s.gcr.io/e2e-test-images/busybox:1.29
    command:
      - "/bin/sleep"
      - "10000"
    volumeMounts:
    - name: secrets-store-inline
      mountPath: "/mnt/secrets-store"
      readOnly: true
  volumes:
    - name: secrets-store-inline
      csi:
        driver: secrets-store.csi.k8s.io
        readOnly: true
        volumeAttributes:
          secretProviderClass: "azure-key-vault-name" # the name of your key vault
```

```powershell
kubectl apply -f ./test-pod.yml

kubectl exec busybox-secrets-store-inline -- ls /mnt/secrets-store/
# Expected output:
# cert-demo
# foo

kubectl exec busybox-secrets-store-inline -- cat /mnt/secrets-store/foo
# Expected output:
# bar

kubectl exec busybox-secrets-store-inline -- cat /mnt/secrets-store/cert-demo
# Expected output:
-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDVYhtyud6rbRJT
...
3fic6VM3cQR9FJxBxAq4vro=
-----END PRIVATE KEY-----
-----BEGIN CERTIFICATE-----
MIIDQjCCAiqgAwIBAgIQSRZYP7ncTSGCw6IEOxTIhjANBgkqhkiG9w0BAQsFADAe
...
5STNJyO/kEBkBMjlzZKlDkhuf4Tr1g==
-----END CERTIFICATE-----
```

```powershell
kubectl get secrets
# Expected output:
# NAME                                    TYPE                                  DATA   AGE
# cert-demo                               kubernetes.io/tls                     2      9h
# foo                                     Opaque                                1      9h
```
