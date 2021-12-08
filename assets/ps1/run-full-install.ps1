######################################## INTRO #####################################################################
Clear-Host
Write-Host "-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------" -ForegroundColor Green
Write-Host "-------------------------------------------------- CLUEDIN INSTALLATION IN AZURE KUBERNETES SERVICES ------------------------------------------------------------------------------" -ForegroundColor Green
Write-Host "-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------" -ForegroundColor Green
Write-Host ""
Write-Host "Loading required tools for installation..." -ForegroundColor Yellow


# CREATE OR GET AZURETOOLS FOLDER
$env:AzureTools = $pwd.drive.name
$env:AzureTools += ":\Users\$env:UserName\AzureTools"
if(-not [System.IO.Directory]::Exists($env:AzureTools)){
	mkdir $env:AzureTools
}

# Set-Location $env:AzureTools

# SET CLUEDIN DOCUMENTATION URL FOR DOWNLOADS NEEDED IN THIS SCRIPT
$cluedinDocUrl = "https://documentation.cluedin.net"
# $cluedinDocUrl = "http://127.0.0.1:4000/"


$scriptsFolder = "$env:AzureTools\scripts"
if(-not [System.IO.Directory]::Exists("$scriptsFolder")){
	mkdir "$scriptsFolder"
}

$ProgressPreference = 'SilentlyContinue'
Invoke-WebRequest -Uri "$cluedinDocUrl/assets/ps1/install-steps/1-set-variables.ps1" -OutFile "$scriptsFolder\1-set-variables.ps1"
Invoke-WebRequest -Uri "$cluedinDocUrl/assets/ps1/install-steps/2-create-aks-cluster.ps1" -OutFile "$scriptsFolder\2-create-aks-cluster.ps1"
Invoke-WebRequest -Uri "$cluedinDocUrl/assets/ps1/install-steps/3-prepare-cluedin.ps1" -OutFile "$scriptsFolder\3-prepare-cluedin.ps1"
Invoke-WebRequest -Uri "$cluedinDocUrl/assets/ps1/install-steps/4-configure-values-yaml.ps1" -OutFile "$scriptsFolder\4-configure-values-yaml.ps1"
Invoke-WebRequest -Uri "$cluedinDocUrl/assets/ps1/install-steps/5-install-cluedin.ps1" -OutFile "$scriptsFolder\5-install-cluedin.ps1"

# 1- SET VARIABLES FOR CLUSTER CREATION
. $scriptsFolder\1-set-variables.ps1

# 2- CREATE AKS CLUSTER
. $scriptsFolder\2-create-aks-cluster.ps1

# 3- PREPARE CLUEDIN
. $scriptsFolder\3-prepare-cluedin.ps1

# 4- CONFIGURE VALUES.YML
. $scriptsFolder\4-configure-values-yaml.ps1

# 5- INSTALL CLUEDIN
. $scriptsFolder\5-install-cluedin.ps1