---
layout: cluedin
title: Azure Managed Redis
parent: Day-to-day operations
grand_parent: Deploy & operate
nav_order: 50
permalink: /operate/operations/azure-managed-redis
content_type: how-to
tags: ["azure", "redis", "deployment"]
headerIcon: "paas"
---

## On this page
{: .no_toc .text-delta }

1. TOC
{:toc}

This document outlines the process of provisioning Azure Managed Redis with a private endpoint and configure CluedIn to use it in place of the in-cluster Redis service. You can store the Redis access key in Azure Key Vault or manage it through Helm secrets.

The process is split into two stages:
1. **Azure Redis Creation**
2. **Update Redis Connection String on Helm**

## Stage 1: Azure Redis creation

### Prerequisites

**Before running this deployment, please ensure that your CluedIn application is already on version 5.0 ([2026.03.00](/operate/upgrade/2026-03-00)).** Should you require any assistance or have any inquiries, please contact CluedIn support.

The Automation Account managed identity requires the following permissions:

| Scope | Role | Purpose |
|---|---|---|
| AKS Resource Group | Contributor | Retrieve AKS details and deploy Redis resources. |
| AKS Virtual Network | Network Contributor | Create the Redis Private Endpoint. |
| AKS Resource Group | Private DNS Zone Contributor | Create and configure the Private DNS Zone. |
| Storage Account | Appropriate Storage permissions | Download the Bicep template. |

**Azure Key Vault is optional**. To store the Redis primary access key automatically in Key Vault, the Automation Account managed identity also requires **Key Vault Secrets Officer** on the specified vault.

### Step 1: Upload the Bicep template

Upload the following Bicep template to a Storage Account that the Automation Account can access:

- Container: `azureredis`
- Blob: `azureredis.bicep`

```bicep
@description('Name of the Azure Managed Redis instance')
param redisName string

@description('Azure region')
param location string = resourceGroup().location

@description('Redis SKU name, for example Balanced_B0 or Balanced_B1')
param skuName string = 'Balanced_B0'

@description('Subnet resource ID for the Private Endpoint')
param subnetId string

@description('Virtual Network resource ID for the Private DNS Zone link')
param virtualNetworkId string

@description('Whether to create and associate the Private DNS Zone')
param enablePrivateDnsZone bool = true

@description('Name of the Private DNS Zone')
param privateDnsZoneName string = 'privatelink.redis.azure.net'

@description('Resource tags')
param tags object = {}

resource redis 'Microsoft.Cache/redisEnterprise@2025-04-01' = {
  name: redisName
  location: location
  sku: {
    name: skuName
  }
  properties: {
    encryption: {}
    highAvailability: 'Enabled'
    minimumTlsVersion: '1.2'
  }
}

resource defaultDatabase 'Microsoft.Cache/redisEnterprise/databases@2025-04-01' = {
  name: 'default'
  parent: redis
	properties: {
    clientProtocol: 'Encrypted'
    clusteringPolicy: 'OSSCluster'
    evictionPolicy: 'VolatileLRU'
    modules: []
    port: 10000
  }
}

resource redisDnsZone 'Microsoft.Network/privateDnsZones@2024-06-01' = if (enablePrivateDnsZone) {
  name: privateDnsZoneName
  location: 'global'
  tags: tags
}

resource redisPrivateEndpoint 'Microsoft.Network/privateEndpoints@2024-07-01' = {
  name: 'azureredis-private-endpoint'
  location: location
  tags: tags
  properties: {
    subnet: {
      id: subnetId
    }
    privateLinkServiceConnections: [
      {
        name: 'azureredisPrivateLink'
        properties: {
          privateLinkServiceId: redis.id
          groupIds: [
            'redisEnterprise'
          ]
        }
      }
    ]
  }
}

resource redisPrivateDnsZoneGroup 'Microsoft.Network/privateEndpoints/privateDnsZoneGroups@2024-07-01' = if (enablePrivateDnsZone) {
  parent: redisPrivateEndpoint
  name: 'default'
  properties: {
    privateDnsZoneConfigs: [
      {
        name: 'redis-private-dns'
        properties: {
          privateDnsZoneId: redisDnsZone.id
        }
      }
    ]
  }
}

resource redisDnsLink 'Microsoft.Network/privateDnsZones/virtualNetworkLinks@2024-06-01' = if (enablePrivateDnsZone) {
  parent: redisDnsZone
  name: 'azure-redis-link'
  location: 'global'
  properties: {
    virtualNetwork: {
      id: virtualNetworkId
    }
    registrationEnabled: false
  }
}

output redisFqdn string = redis.properties.hostName

output redisPort int = 10000

output redisSslPort int = 10000

```

1. Review the SKU, availability, clustering, and eviction settings for your environment. The template uses `Balanced_B0`, `OSSCluster`, and `VolatileLRU` as in the deployment procedure. Confirm that these settings are supported for your intended CluedIn deployment.

  {:.important}
  If a private DNS zone already exists in a shared networking resource group, use `EnablePrivateDnsZone=false` and arrange the zone association, DNS records, and AKS virtual network DNS resolution separately. That setting skips all DNS resources in this template.

### Step 2: Create the Automation runbook

Create a PowerShell runbook named `Deploy-AzureRedis` in the Automation Account and add the script below. Select a runtime compatible with the imported Az modules and the Windows executable used by the script.

The runbook will:
1. Authenticate using the Automation Account managed identity.
1. Retrieve the AKS cluster location.
1. Generate the Redis name based on the AKS name.
1. Download the Bicep template from the Storage Account.
1. Deploy Azure Managed Redis.
1. Retrieve the Redis FQDN, port and primary access key.
1. Optionally store the primary access key in Azure Key Vault.

```powershell
param(

    [string]$StorageAccountRG="",
    [string]$StorageAccountName="",
    [string]$ResourceGroupName="",
    [string]$aksName="",
    [string]$VirtualNetworkId="",
    [string]$SubnetId="",

    [Parameter(Mandatory = $false)]
    [string]$KeyVaultName = "",

    [Parameter(Mandatory = $false)]
    [string]$RedisPasswordSecretName = "redis-password",

    [Parameter(Mandatory = $false)]
    [bool]$EnablePrivateDnsZone = $true,

    [Parameter(Mandatory = $false)]
    [hashtable]$Tags = @{}

)

$ErrorActionPreference = "Stop"
# ------------------------------------------------------------
# 1. Install Bicep
# ------------------------------------------------------------
$installPath = "$env:USERPROFILE\.bicep"
if (-not (Test-Path $installPath)) {
    New-Item -ItemType Directory -Path $installPath -Force | Out-Null
}
$bicepPath = "$installPath\bicep.exe"
if (-not (Test-Path $bicepPath)) {
    Write-Output "Downloading latest Bicep CLI..."
    (New-Object Net.WebClient).DownloadFile(
        "https://github.com/Azure/bicep/releases/latest/download/bicep-win-x64.exe",
        $bicepPath
    )
}
if (-not $env:PATH.Contains($installPath)) {
    $env:PATH += ";$installPath"
}
Write-Output "Bicep version:"
bicep --version
# ------------------------------------------------------------
# 2. Authenticate using Automation Account Managed Identity
# ------------------------------------------------------------
Write-Output "Logging in with Automation Account Managed Identity..."
Connect-AzAccount -Identity
Write-Output "Azure authentication successful."
# ------------------------------------------------------------
# 3. Get AKS location
# ------------------------------------------------------------
Write-Output "Getting AKS cluster details..."
$aks = Get-AzAksCluster `
    -ResourceGroupName $ResourceGroupName `
    -Name $aksName
$Location = $aks.Location
Write-Output "AKS Name: $aksName"
Write-Output "AKS Location: $Location"
# ------------------------------------------------------------
# 4. Generate Redis name
# ------------------------------------------------------------
$RedisSuffix = $aksName -replace '^aks-', ''
$RedisName = "redis-$RedisSuffix"
Write-Output "Redis Name: $RedisName"
# ------------------------------------------------------------
# 5. Download Bicep template
# ------------------------------------------------------------
$storageContainerName = "azureredis"
$blobName = "azureredis.bicep"
$tempFile = Join-Path $env:TEMP $blobName
Write-Output "Getting Storage Account key..."
$storageAccountKey = (
    Get-AzStorageAccountKey `
        -ResourceGroupName $StorageAccountRG `
        -Name $StorageAccountName
).Value[0]
$storageContext = New-AzStorageContext `
    -StorageAccountName $StorageAccountName `
    -StorageAccountKey $storageAccountKey
Write-Output "Downloading Bicep template..."
Get-AzStorageBlobContent `
    -Container $storageContainerName `
    -Blob $blobName `
    -Destination $tempFile `
    -Context $storageContext `
    -Force
Write-Output "Downloaded Bicep template to:"
Write-Output $tempFile
# ------------------------------------------------------------
# 6. Prepare Bicep parameters
# ------------------------------------------------------------
$params = @{
    redisName            = $RedisName
    location             = $Location
    subnetId             = $SubnetId
    virtualNetworkId     = $VirtualNetworkId
    enablePrivateDnsZone = $EnablePrivateDnsZone
    tags                 = $Tags
}
Write-Output "Deployment parameters:"
$params | ConvertTo-Json -Depth 10
# ------------------------------------------------------------
# 7. Deploy Azure Managed Redis
# ------------------------------------------------------------
Write-Output "Starting Azure Managed Redis deployment..."
$deployment = New-AzResourceGroupDeployment `
    -Name "redis-deployment" `
    -ResourceGroupName $ResourceGroupName `
    -TemplateFile $tempFile `
    -TemplateParameterObject $params `
    -Verbose
Write-Output "Azure Managed Redis deployment completed successfully."
# ------------------------------------------------------------
# 9. Retrieve Redis deployment outputs
# ------------------------------------------------------------
$redisFqdn = $deployment.Outputs.redisFqdn.Value
$redisPort = $deployment.Outputs.redisSslPort.Value
Write-Output "Redis FQDN: $redisFqdn"
Write-Output "Redis SSL Port: $redisPort"
# ------------------------------------------------------------
# 10. Retrieve Redis access key
# ------------------------------------------------------------
Write-Output "Retrieving Azure Managed Redis primary access key..."
$redisKeys = Get-AzRedisEnterpriseCacheKey `
    -ResourceGroupName $ResourceGroupName `
    -ClusterName $RedisName `
    -ErrorAction Stop
$redisPassword = $redisKeys.PrimaryKey
if ([string]::IsNullOrWhiteSpace($redisPassword)) {
    throw "Failed to retrieve the Azure Managed Redis primary access key."
}
Write-Output "Redis primary access key retrieved successfully."
# ------------------------------------------------------------
# 9. Optional: Store Redis password in Azure Key Vault
# ------------------------------------------------------------
if (-not [string]::IsNullOrWhiteSpace($KeyVaultName)) {
    Write-Output "Key Vault configured."
    Write-Output "Storing Redis primary access key in Key Vault..."
    $secureRedisPassword = ConvertTo-SecureString `
        $redisPassword `
        -AsPlainText `
        -Force
    Set-AzKeyVaultSecret `
        -VaultName $KeyVaultName `
        -Name $RedisPasswordSecretName `
        -SecretValue $secureRedisPassword `
        -ContentType "Azure Managed Redis primary access key" `
        -Tag @{
            RedisName = $RedisName
            ManagedBy = "Deploy-AzureRedis"
        }
    Write-Output "Redis password successfully stored in Key Vault."
    Write-Output "Key Vault: $KeyVaultName"
    Write-Output "Secret Name: $RedisPasswordSecretName"
}
else {
    Write-Output "Key Vault was not provided."
    Write-Output "Skipping Key Vault secret creation."
}
# ------------------------------------------------------------
# 10. Deployment summary
# ------------------------------------------------------------
Write-Output ""
Write-Output "=============================================="
Write-Output "Azure Managed Redis Deployment Completed"
Write-Output "=============================================="
Write-Output "AKS Name:        $aksName"
Write-Output "Redis Name:      $RedisName"
Write-Output "Redis FQDN:      $redisFqdn"
Write-Output "Redis SSL Port:  $redisPort"
Write-Output "Redis Key:       $redisPassword"
if (-not [string]::IsNullOrWhiteSpace($KeyVaultName)) {
    Write-Output "Key Vault:       $KeyVaultName"
    Write-Output "Secret Name:     $RedisPasswordSecretName"
}
else {
    Write-Output "Key Vault:       Not configured"
}
Write-Output "=============================================="
```

### Runbook parameters

| Parameter | Description | Required |
|---|---|---|
| `StorageAccountRG` | Resource group containing the Bicep Storage Account. | Yes |
| `StorageAccountName` | Storage Account containing `azureredis.bicep`. | Yes |
| `ResourceGroupName` | AKS/Redis resource group. | Yes |
| `aksName` | AKS cluster name. | Yes |
| `VirtualNetworkId` | AKS VNet resource ID. | Yes |
| `SubnetId` | Subnet used by the Redis Private Endpoint. | Yes |
| `KeyVaultName` | Key Vault for storing the Redis password. | No |
| `RedisPasswordSecretName` | Key Vault secret name. | No |
| `EnablePrivateDnsZone` | Create the Private DNS Zone. | No |
| `Tags` | Azure resource tags. | No |

If you are not using Key Vault, leave `KeyVaultName` empty:

```text
KeyVaultName = ""
```

If Key Vault was setup and used, provide:

```text
KeyVaultName = <customer-key-vault-name>
RedisPasswordSecretName = redis-password
```

The runbook creates or updates the primary access key in the specified Key Vault.

1. Wait for the runbook to complete. Record the Redis FQDN and TLS port from the output. If you did not use Key Vault, retrieve the primary access key through the Azure portal using your approved secret-management process. The runbook does not print it.

1. In Azure, confirm that Redis and its database are provisioned, the private endpoint connection is approved, and DNS resolves the Redis hostname to the private endpoint from the AKS network. Use the Redis hostname in application settings rather than the private IP address.

## Stage 2: Update Redis connection settings in Helm

After deployment, configure CluedIn to use the new Redis instance.

The following information is required:
- Redis FQDN
- Redis SSL port
- Redis primary access key

### Step 1: Back up the existing Redis Secret
```bash
kubectl get secret cluedin-redis -n cluedin -o yaml > redis-secret-backup.yaml
```

Store the backup securely.

### Step 2: Back up the current Helm values
```bash
helm get values cluedin-platform -n cluedin -o yaml > values-backup.yaml
```

Create a new `values.yaml` based on the existing configuration. Preserve the original in-cluster Redis PVCs and data until the switch is validated.

### Step 3: Update the Redis configuration
Scale down CluedIn:

```bash
kubectl scale deploy cluedin-server cluedin-server-processing cluedin-datasource-processing cluedin-datasource-submitter cluedin-gql cluedin-ui -n cluedin --replicas=0 --timeout 5m

kubectl scale statefulset/cluedin-redis-master -n cluedin --replicas 0
```

Delete the current Redis Secret:

```bash
kubectl delete secret cluedin-redis -n cluedin 
```

**If using Key Vault**, delete the SecretProviderClass:

```bash
kubectl get secretproviderclass cluedin-redis-sync -n cluedin -o yaml > redis-spc-backup.yaml
kubectl delete secretproviderclass/cluedin-redis-sync -n cluedin
```

Update the Redis configuration in your values file:

```yaml
application:
  redis:
    connectionOptions:
      encrypt: true
    host: <AZURE_REDIS_FQDN>
    isExternal: true
    port: 10000

infrastructure:
  redis:
    enabled: false
```

Replace `<AZURE_REDIS_FQDN>` with the FQDN returned by the deployment.

#### Option A: Without Azure Key Vault

Add the Redis primary access key directly through `platform.extraSecrets`:

```yaml
platform:
  extraSecrets:
    cluedin-redis:
      redis-password: '<AZURE_REDIS_PRIMARY_ACCESS_KEY>'
```

Replace `<AZURE_REDIS_PRIMARY_ACCESS_KEY>` with the primary access key returned by the Azure Redis deployment. 

  {:.important}
  Do not commit the Redis primary access key to source control. Store the value using your approved secret-management process.

#### Option B: With Azure Key Vault

If you are using Azure Key Vault, do not add the Redis password under `platform.extraSecrets`.

Instead, configure the CluedIn SecretProviderClass to retrieve the password from Key Vault:

```yaml
global:
  keyvault:
    secretProviderClasses:
      cluedin-server:
        - secretKeys:
            redis-password: cluedin-redis-password
          secretName: cluedin-redis
```

In this configuration:

- `redis-password` is the key expected by CluedIn.
- `cluedin-redis-password` is the Azure Key Vault secret name.
- `cluedin-redis` is the Kubernetes Secret created by the SecretProviderClass.
- The primary access key should be stored in Key Vault as `cluedin-redis-password`.

  {:.important}
  Use either `platform.extraSecrets` or the Key Vault SecretProviderClass configuration. Do not configure the password in both locations.

### Step 4: Run Helm upgrade

Remove any obsolete `cluedin-redis` entry from `global.keyvault.secretProviderClasses` that would recreate the old dedicated Redis synchronization resource. Preserve the new mapping under `cluedin-server`. Confirm no remaining controller is configured to restore the previous password.

1. Apply the updated values:

   ```bash
   helm upgrade cluedin-platform -n cluedin cluedin/cluedin-platform \
       --version 3.0.0 \
       --values values.yaml
   ```

## Post-deployment checks

### Verify pod status

Confirm that all CluedIn pods are `Running`:

```bash
kubectl get pods -n cluedin
```
### Verify Redis configuration

Confirm that the Redis Secret exists:

```bash
kubectl get secret cluedin-redis -n cluedin
```

Review deployed Helm configuration:

```bash
helm get values cluedin-platform -n cluedin
```

Verify that:
- External Redis is enabled.
- Azure Redis FQDN is configured.
- Redis port is `10000`.
- Redis encryption is enabled.
- The in-cluster Redis deployment is disabled.

Check logs if required:

```bash
kubectl logs -n cluedin <pod-name>
```

Search for Redis-related errors:

```bash
kubectl logs -n cluedin <pod-name> | grep -i redis
```

### Verify application health

Verify that:
- CluedIn UI is accessible.
- CluedIn services are healthy.
- No Redis connection errors are present in the application logs.
- Standard CluedIn sanity tests complete successfully.

## Roll back *(if required)*

1. Stop Redis-consuming workloads before restoring the old credentials and connection settings. Confirm the original Redis PVCs are available and the previous chart version is accessible.

1. When using Key Vault, restore the previous Redis password in its original Key Vault secret before restarting synchronization. Restore the previous SecretProviderClass configuration as needed. Remove the new external-Redis mapping so that it does not overwrite the restored Kubernetes Secret.

1. Restore the original Redis Secret from your backup. If you backed up the old SecretProviderClass, restore that as well:

```bash
kubectl apply -f redis-secret-backup.yaml

# Only when this backup was created:
kubectl apply -f redis-spc-backup.yaml
```

Restore the previous Helm configuration:

```bash
helm upgrade cluedin-platform -n cluedin cluedin/cluedin-platform \
    --version 3.0.0 \
    --values values-backup.yaml \
    --wait \
    --timeout 15m0s
```

Monitor the pods:

```bash
kubectl get pods -n cluedin -w
```

1. Restore any remaining manually scaled workloads to their recorded replica counts. Confirm that the original Redis instance and CluedIn pods are healthy and that the original connection settings are active.

{:.important}
Restoring connection settings does not transfer data written to Azure Managed Redis back to the original instance. Follow the agreed data recovery procedure if Redis data must be preserved across the rollback.

If deployment or application validation fails, contact CluedIn support before proceeding.