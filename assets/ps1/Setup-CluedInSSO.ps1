# End-to-end full deployment of Single Sign-On
[CmdletBinding()]
param(
    [Parameter(Mandatory)][string]$AKSCluster,
    [string]$AADApplicationName = 'cluedin-sso-app'
)

# Validation
Try{ Get-Command -Name 'az' }
Catch { throw "az cli must be installed for this script to work" }

$resource = az resource list --name $AKSCluster | ConvertFrom-Json
if ($resource.count -ne 1) { throw "Issue with returned AKS Cluster '$AKSCluster'" }

$aks = az aks show --name $resource.name --resource-group $resource.resourceGroup | ConvertFrom-Json
if (!$?) { throw "Issue getting aks details" }

$appExists = az ad app list --display-name $AADApplicationName | ConvertFrom-Json
if ($appExists) { throw "AD App already exists" }

# Setup
Write-Host "Registering '$AADApplicationName'"
$appObject = az ad app create --display-name $AADApplicationName | ConvertFrom-Json
if (!$?) { throw "There was an issue creating the az ad app" }

$clientId = $appObject.appId
$appId = $appObject.id

Write-Host "Creating secret" -ForegroundColor 'Green'
$secretName = 'cluedin-sso'
$secretParams = @(
    '--id', $clientId
    '--display-name', $secretName
    '--years', 5
    '--query', 'password'
    '--output', 'tsv'
)
$secretPassword = az ad app credential reset @secretParams
if (!$?) { throw "Issue with generating a secret" }

$aksSecretName = 'cluedin-sso-cs'
Write-Host "Uploading secret '$aksSecretName' to AKS" -ForegroundColor 'Cyan'
$command = "kubectl create secret generic $aksSecretName --namespace 'cluedin' --from-literal=clientSecret=$secretPassword"
$result = az aks command invoke --name $aks.name --resource-group $aks.resourceGroup --command $command --output 'json'
$resultObject = $result | ConvertFrom-Json
if ($resultObject.provisioningState -ne 'Succeeded') { Write-Warning "Issue with uploading password. Please manually reset and upload to AKS" }

Write-Host "Getting current helm details" -ForegroundColor 'Green'
$command = "helm get values cluedin-platform --namespace cluedin --output json"
$result = az aks command invoke --name $aks.name --resource-group $aks.resourceGroup --command $command --output 'json'
$helm = ($result | ConvertFrom-Json).logs | ConvertFrom-Json

$organisation = $helm.application.bootstrap.organization.name
$hostname = $helm.global.dns.hostname
$baseUri = 'https://{0}.{1}' -f $organisation, $hostname

# detect if subdomains or host alias
$default = ($helm.global.ingress.tls.hosts) ? $true : $false
switch ($default) {
    $true { $appBaseUri = 'https://app.{0}' -f $hostname }
    $false {
        if (!$helm.global.dns.subdomains.application) {
            Write-Warning "Issue detecting application uri. Please manually update post-deployment"
            $appBaseUri = 'https://APP.REPLACEME'
        }
        else { $appBaseUri = 'https://{0}.{1}' -f $helm.global.dns.subdomains.application, $hostname }
    }
}

$redirectUris = @(
    $baseUri
    $appBaseUri
    '{0}/auth/signin-oidc' -f $appBaseUri
)

Write-Host "Setting Authentication" -ForegroundColor 'Green'
Write-Host "Adding redirect URIs" -ForegroundColor 'Cyan'
$graphUri = 'https://graph.microsoft.com/v1.0/applications/{0}' -f $appId
az ad app update --id $clientId --web-redirect-uris @redirectUris
if (!$?) { Write-Warning "Issue adding redirect uris, please check this manually post-deployment" }

Write-Host "Adding logout URL" -ForegroundColor 'Cyan'
$logoutUrl = '{0}/logout' -f $appBaseUri
$body = ( (@{ web = @{ logoutUrl = $logoutUrl } } | ConvertTo-Json -Compress) -Replace '"', '\"' )
$params = @(
    '--method', 'PATCH'
    '--uri', $graphUri
    '--headers', 'Content-Type=application/json'
    '--body', $body
)
az rest @params

Write-Host "Setting Implicit Grants" -ForegroundColor 'Cyan'
az ad app update --id $clientId --enable-id-token-issuance

Write-Host "Adding API permissions for MS Graph" -ForegroundColor 'Green'
$msGraphGuid = '00000003-0000-0000-c000-000000000000' # Microsoft Graph
$params = @(
    '--id', $appId
    '--api', $msGraphGuid
    '--api-permissions',
        'e1fe6dd8-ba31-4d61-89e7-88639da4683d=Scope' # User.Read
        '64a6cdd6-aab1-4aaf-94b8-3cc8405e90d0=Scope' # email
        '7427e0e9-2fba-42fe-b0c0-848c9e6a8182=Scope' # offline_access
        '37f7f235-527c-4136-accd-4a02d197296e=Scope' # openid
        '14dad69e-099b-42c9-810b-d002981feec1=Scope' # profile
        # Ref: https://learn.microsoft.com/en-us/graph/permissions-reference
)
az ad app permission add @params 2>nul
Write-Host "NOTE: You may need to manually grant consent if it does not work" -ForegroundColor 'Yellow'

Write-Host "Exposing API" -ForegroundColor 'Green'
Write-Host "Setting Application ID Uri" -ForegroundColor 'Cyan'
$appHttpsLess = $appBaseUri.Replace('https://', '')
$body = (( @{identifierUris=@("api://$appHttpsLess/sso")} | ConvertTo-Json -Compress) -Replace '"', '\"' )
$params = @(
    '--method', 'PATCH'
    '--uri', $graphUri
    '--headers', 'Content-Type=application/json'
    '--body', $body
)
az rest @params

Write-Host "Setting Scope" -ForegroundColor 'Cyan'
$scopeGuid = New-Guid
$scopeJsonHash = @{
    adminConsentDescription = 'CluedIn'
    adminConsentDisplayName = 'CluedIn'
    id = $scopeGuid.Guid
    isEnabled = $true
    type = 'User'
    userConsentDescription = 'CluedIn'
    userConsentDisplayName = 'CluedIn'
    value = 'testscopename.com'
}
$body = ( @{api = @{ oauth2PermissionScopes = @($scopeJsonHash) }} | ConvertTo-Json -Compress -Depth 3 ) -Replace '"', '\"'

$params = @(
    '--method', 'PATCH'
    '--uri', $graphUri
    '--headers', 'Content-Type=application/json'
    '--body', $body
)
az rest @params

Write-Host "Enabling SSO on the environment" -ForegroundColor 'Green'

$tempFile = New-TemporaryFile
$enableSSOYaml = @'
apiVersion: api.cluedin.com/v1
kind: Feature
metadata:
  name: cluedin-sso
spec:
  enableSso:
    clientId: "{0}"
    organizationName: "{1}"
    clientSecretName: "{2}"
    clientSecretKey: "clientSecret"
'@ -f $clientId, $organisation, $aksSecretName
$enableSSOYaml | Out-File -FilePath $tempFile.FullName

$command = "kubectl apply --namespace 'cluedin' -f ./$($tempFile.name)"
$params = @(
    '--name', $aks.name
    '--resource-group', $aks.resourceGroup
    '--command', $command
    '--file', $tempFile.FullName
    '--output', 'json'
)
$result = az aks command invoke @params
$resultObject = $result | ConvertFrom-Json
if ($resultObject.logs -notmatch 'created') {
    Write-Error "Potential issue with enabling SSO"
    $resultObject.logs
}

Write-Host "Single Sign On process now complete" -ForegroundColor 'Green'
Write-Host "Reference Document: https://documentation.cluedin.net/deployment/infra-how-tos/configure-sso"