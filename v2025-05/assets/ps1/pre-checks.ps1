param(
    [Parameter(Mandatory)]
    [string]$SubscriptionId,
    [switch]$Register,
    [switch]$Wait
)

$ErrorActionPreference = 'Stop'

if(!(Get-Command az)) {
    Write-Error "You must install the azure CLI to continue"
}

# Login
function GetCurrentSubscription { az account show --query 'id' -o tsv }
$currentSubscription = GetCurrentSubscription
if(!$currentSubscription) { az login -o none }

if($currentSubscription -ne $SubscriptionId){
    az account set --subscription $SubscriptionId
    $currentSubscription = GetCurrentSubscription
    if($currentSubscription -ne $SubscriptionId){
        Write-Error "Could not login to subscription ${SubscriptionId}"
    }
}

function FetchProviders {
    $requiredProviders = @(
        "Microsoft.Cache",
        "Microsoft.Capacity",
        "Microsoft.Compute",
        "Microsoft.ContainerService",
        "Microsoft.EventHub",
        "Microsoft.KeyVault",
        "Microsoft.ManagedIdentity",
        "Microsoft.Network",
        "Microsoft.OperationalInsights",
        "Microsoft.OperationsManagement",
        "Microsoft.Resources",
        "Microsoft.Storage",
        "Microsoft.Sql"
    )

    az provider list --query '[].{ Name: namespace, Registered: registrationState}' |
        ConvertFrom-Json |
        Where-Object { $requiredProviders -contains $_.Name } |
        ForEach-Object {
            $required = $requiredProviders -contains $_.Name
            Add-Member -InputObject $_ -NotePropertyName Required -NotePropertyValue $required -PassThru
        } |
        Sort-Object Required,Name,Registered
}

$providers = FetchProviders

if($Register) {
    $toRegister = $providers.Where({ $_.Required -and $_.Registered -ne 'Registered'})
    if($toRegister) {
        Write-Host "Registering missing providers"
        $toRegister | ForEach-Object {
            az provider register --namespace $_.Name --accept-terms --wait
        }

        $providers = FetchProviders
    } else {
        Write-Host "All required providers registered" -ForegroundColor Green
    }
}

$providers