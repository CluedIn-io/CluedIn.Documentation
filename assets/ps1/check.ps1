[CmdletBinding()]
param(
    [Parameter(Mandatory)][string]$SubscriptionId,
    [Parameter(Mandatory)][string]$Location
)

$Configuration = @{
    providers = @(
        "Microsoft.ManagedIdentity"
        "Microsoft.Authorization"
        "Microsoft.KeyVault"
        "Microsoft.Network"
        "Microsoft.ContainerService"
        "Microsoft.OperationalInsights"
        "Microsoft.Insights"
        "Microsoft.Sql"
        "Microsoft.EventHub"
        "Microsoft.Cache"
        "Microsoft.Compute"
        "Microsoft.OperationsManagement"
        "Microsoft.Storage"
    )
    quotas = @{
        All = @{ # All will be combined with the licenses below during runtime
            standardDv4Family = 16 # Data 2x8, General 2x8, Neo 1x8
            standardDASv5Family = 24 # Data 2x8, Neo 1x8
            standardDv2Family = 2 # System
        }
        Essential = @{ standardDASv5Family = 8 }
        Professional = @{ standardDASv5Family = 16 }
        Elite = @{ standardDASv5Family = 32 }
    }
}

function Get-Az {
    if (!(Get-Command 'az' -ErrorAction Ignore)) {
        Write-Host "INFO - Az CLI needs to be installed before proceeding"
        while ($confirm -notmatch "^[yY]$|^[nN]$") {
            $confirm = Read-Host "Install Az CLI now? [Y/n]"
        }
        switch ($confirm) {
            'y' { Install-Az }
            'n' { 
                Write-Host "The Azure CLI must be installed to run this script" -ForegroundColor Red
                Write-Host "Please install using one of the following options" -ForegroundColor Yellow
                Write-Host " - Running ``winget install -e --id Microsoft.AzureCLI`` " -ForegroundColor Yellow
                Write-Host " - Dowloading and running the msi: https://aka.ms/installazurecliwindows " -ForegroundColor Yellow
                Write-Host "Once installation is complete, please restart your terminal and run this script again" -ForegroundColor Green
                return
            }
        }
    }

    Write-Verbose "Az CLI Found"
    return $true
}

function Install-Az {
    Try {
        winget install -e --id Microsoft.AzureCLI
    }
    Catch {
        throw "There was an issue attempting to install Azure CLI. Please install this manually"
    }
}

function Connect-Az {
    $current = az account show --query '{Id: id, LoginUser: user.name}' | ConvertFrom-Json
    Write-Host "INFO - You are currently logged in as: $($current.LoginUser) [$($current.Id)]"
    
    if ($current.Id -ne $SubscriptionId) {
        Write-Warning "Setting subscription to: $SubscriptionId"
        az account set --subscription $SubscriptionId
        if (!$?) { throw "Please check that you have appropriate access" }
    }
}

function Get-RegisteredProviders {
    Write-Host "INFO - Checking Providers"
    $requiredProviders = $configuration.providers

    $providers = az provider list --query '[].{ Name: namespace, Registered: registrationState}' |
        ConvertFrom-Json |
        Where-Object { $requiredProviders -contains $_.Name } |
        Sort-Object Name

    if ($providers.Registered -ne 'Registered') {
        Write-Warning "Please ensure the following providers are registered"
        $providers | Where-Object {$_.Registered -ne 'Registered'}
    }
    else { Write-Host "  All required providers are registered" -ForegroundColor Green }
}

function Get-Quotas {
    Write-Verbose "Getting CPU Usage"

    $query = "[].{Name: name.value, Current: currentValue, Limit: limit}"
    $regionQuotas = az vm list-usage --location $Location --query $query | ConvertFrom-Json
    if ($regionQuotas.count -eq 0) { throw "No quotas were returned for the region '$location'" }

    Write-Verbose "Filtering results"
    $uniqueFamilies = $Configuration.quotas.values.keys | Select-Object -Unique
    $filtered = $regionQuotas | Where-Object {$uniqueFamilies -contains $_.Name}

    Write-Verbose "Processing Remaining Cores"
    $remainingCores = @{}
    $filtered.ForEach({
        $remainingCores += @{
            $_.Name = $_.Limit - $_.Current
        }
    })

    Write-Debug $remainingCores

    Write-Verbose "Cloning and Cleansing quotas"
    $licenseTable = $Configuration.quotas.Clone()
    $licenseTable.Remove('All')

    foreach ($key in ($Configuration.quotas['All'].keys)) {
        Write-Debug "key: $key"
        foreach ($license in ($licenseTable.keys)) {
            $cpuAddition = $licenseTable[$license][$key] + $Configuration.quotas['All'][$key] # Adds all and current license values together
            $licenseTable[$license][$key] = $cpuAddition
        }
    }

    Write-Host "INFO - Checking CPU Family Quotas for All licenses"
    foreach ($key in $licenseTable.keys) {
        Write-Debug "key: $key"
        Write-Host "[$key]:"
        $licenseTable[$key].keys.ForEach({
            $requiredQuotas = $licenseTable[$key][$_]
            $result = $remainingCores[$_] - $requiredQuotas
            if ($result -lt 0) { $cpuFamilyFail = $true }

            $colour = ($result -gt 0) ? "Green" : "Red"
            Write-Host "  ${_}: $result vCPU remaining" -ForegroundColor $colour
        })
    }

    if ($cpuFamilyFail) { 
        Write-Warning "At least one vCPU family has insufficient quota for the license family it falls under. If this is the license you require, please request additional quota." 
    }
    # TODO: Check Region Total vCPU
}

Write-Host "INFO - Checking Pre-Requisites"
if (Get-Az) {
    Connect-Az

    Get-Quotas
    Get-RegisteredProviders
}