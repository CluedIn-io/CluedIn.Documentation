param(
    [Parameter(Mandatory)]
    [string]$SubscriptionId,
    [Parameter(Mandatory)]
    [string]$Location,
    [string]$WorkingDirectory = $PSScriptRoot,
    [switch]$SkipLogin
)

$ErrorActionPreference = 'Stop'
$configuration = Get-Content (Join-Path $WorkingDirectory 'config.json') | ConvertFrom-Json

function GetAz {
    # Test for Az install via winget
    if(!(Get-Command 'az' -ErrorAction Ignore)){
        Write-Host "The Azure CLI must be installed to run this script" -ForegroundColor Red
        Write-Host "Please install using one of the following options" -ForegroundColor Yellow
        Write-Host " - Running ``winget install -e --id Microsoft.AzureCLI`` " -ForegroundColor Yellow
        Write-Host " - Dowloading and running the msi: https://aka.ms/installazurecliwindows " -ForegroundColor Yellow
        Write-Host "Once installation is complete, please restart your terminal and run this script again" -ForegroundColor Green
    } else {
        Write-Host "Found Azure CLI"
        return $true
    }

    return $false
}

function Login {

    function AzLogin { az login -o none }

    $current = az account show --query 'id' -o tsv

    if(!!$LASTEXITCODE) {
        Write-Host "Please login with the user account that would conduct the install" -ForegroundColor Yellow
        AzLogin
    }
    if($current -ne $SubscriptionId)
    {
        $subscriptions = az account list --query '[].{Id: id, Name: name}' | ConvertFrom-Json
        $found = $subscriptions.Where({ $_.id -eq $SubscriptionId})
        if($found) {
            Write-Host "Setting subscription to $($found.Name)"
            az account set --subscription $SubscriptionId
        } else {
            Write-Host "Please ensure you login to Azure as the correct user" -ForegroundColor Red
            Write-Error "Could not login to subscription ${SubscriptionId}"
        }
    }
}

function ValidateLocation {
    $locations = az account list-locations --query "[].{ Name: name, DisplayName: displayName}" -o json | ConvertFrom-Json
    $foundLocation = $locations.Where({ $_.Name -eq $Location })
    if($foundLocation){
        Write-Host "Using location: $($foundLocation.DisplayName)"
        return
    } else {
        Write-Host "Could not find location '${Location}'" -ForegroundColor Red
        Write-Host "Possible locations are:" -ForegroundColor Yellow
        $locations.Name | ForEach-Object {
            Write-Host "- ${_}" -ForegroundColor Yellow
        }
    }

    Write-Error "Could not validate location"
}

function GetRegisteredProviders {

    Write-Host "Fetching Providers"
    $requiredProviders = $configuration.providers

    az provider list --query '[].{ Name: namespace, Registered: registrationState}' |
        ConvertFrom-Json |
        Where-Object { $requiredProviders -contains $_.Name } |
        Sort-Object Name
}

function CheckQuotas {
    Write-Host "Checking Quotas"

    $collected = @()
    $configuration.quotas.psobject.Properties.name | ForEach-Object {
        $group = $_
        $configuration.quotas.$group.psobject.properties.name | ForEach-Object {
            #$quota = az rest --uri "/subscriptions/{subscriptionId}/providers/Microsoft.Capacity/resourceProviders/Microsoft.Compute/locations/${Location}/serviceLimits/${_}?api-version=2020-10-25" | ConvertFrom-Json
            $quota = az vm list-usage --location westeurope --query "[?contains(name.value, '${_}')].{Name: localName, Limit: limit, CurrentValue: currentValue, Unit: unit}" --output json | ConvertFrom-Json
            $available = $quota.limit - $quota.currentValue
            $required = $configuration.quotas.$group.$_
            $collected += [PSCustomObject]@{
                Name = $quota.Name
                Plan = $group
                Required = $required
                Available = $available
                IncreaseRequired = ($available - $required) -lt 0
            }
        }
    }

    $collected
}

if(GetAz){
    Login
    ValidateLocation
    $providers = GetRegisteredProviders
    $quotas = CheckQuotas

    $output = @{
        Location = $Location
        Providers = $providers
        Quotas = $quotas
    } | ConvertTo-Json -Depth 100

    Set-Content (Join-Path $WorkingDirectory "results_${Location}.json") -Value $output
}