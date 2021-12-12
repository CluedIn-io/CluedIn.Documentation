######################################## INTRO #####################################################################
Clear-Host
Write-Host "-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------" -ForegroundColor Green
Write-Host "-------------------------------------------------- CLUEDIN INSTALLATION IN AZURE KUBERNETES SERVICES ------------------------------------------------------------------------------" -ForegroundColor Green
Write-Host "-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------" -ForegroundColor Green
Write-Host ""
Write-Host "Loading required tools for installation..." -ForegroundColor Yellow

# DETERMINE OS TYPE AND PREPARE AzureTools Folder
if($IsMacOS -or $IsLinux) {
	$sep = "/"
	$cluedinInstallFolder = "$($pwd.drive.name)"
	$currentUser = (id -un)
} elseif ($IsWindows) {
	$sep = "\"
	$cluedinInstallFolder = "$($pwd.drive.name):$($sep)"
	$currentUser = $env:UserName
}

$archiveNeeded = $false
$cluedinInstallFolder += "Users$($sep)$($currentUser)$($sep)CluedinInstall"
if(-not [System.IO.Directory]::Exists($cluedinInstallFolder)){
	mkdir $cluedinInstallFolder
} else {
	$archiveNeeded = ((Get-ChildItem "$($cluedinInstallFolder)$($sep)*.*" | Measure-Object).count -gt 0)
}
# ARCHIVE OLD FILES
if($archiveNeeded){
	$archiveFolder="$($cluedinInstallFolder)$($sep)Archive-$(Get-Date -Format "yyyyddMMHHmmss")"
	mkdir $archiveFolder
	Get-ChildItem -Path $cluedinInstallFolder -File | Move-Item -Destination $archiveFolder -Exclude "$($cluedinInstallFolder)$($sep)Archive*"
}

# Set-Location $cluedinInstallFolder

# SET CLUEDIN DOCUMENTATION URL FOR DOWNLOADS NEEDED IN THIS SCRIPT
# $cluedinDocUrl = "https://documentation.cluedin.net"
$cluedinDocUrl = "http://127.0.0.1:4000/"

$scriptsFolder = "$($cluedinInstallFolder)$($sep)scripts"
if(-not [System.IO.Directory]::Exists("$scriptsFolder")){
	mkdir "$scriptsFolder"
} else {
	# CLEAR CONTENT
	Get-ChildItem -Path $scriptsFolder -Include * -File -Recurse | ForEach-Object { $_.Delete()}
}

$ProgressPreference = 'SilentlyContinue'
Invoke-WebRequest -Uri "$cluedinDocUrl/assets/ps1/install-steps/1-set-variables.ps1" -OutFile "$($scriptsFolder)$($sep)1-set-variables.ps1"
Invoke-WebRequest -Uri "$cluedinDocUrl/assets/ps1/install-steps/2-create-aks-cluster.ps1" -OutFile "$($scriptsFolder)$($sep)2-create-aks-cluster.ps1"
Invoke-WebRequest -Uri "$cluedinDocUrl/assets/ps1/install-steps/3-prepare-cluedin.ps1" -OutFile "$($scriptsFolder)$($sep)3-prepare-cluedin.ps1"
Invoke-WebRequest -Uri "$cluedinDocUrl/assets/ps1/install-steps/4-configure-values-yaml.ps1" -OutFile "$($scriptsFolder)$($sep)4-configure-values-yaml.ps1"
Invoke-WebRequest -Uri "$cluedinDocUrl/assets/ps1/install-steps/5-install-cluedin.ps1" -OutFile "$($scriptsFolder)$($sep)5-install-cluedin.ps1"
$ProgressPreference = 'Continue'

# 1- SET VARIABLES FOR CLUSTER CREATION
. "$($scriptsFolder)$($sep)1-set-variables.ps1"

# 2- CREATE AKS CLUSTER
. "$($scriptsFolder)$($sep)2-create-aks-cluster.ps1"

# 3- PREPARE CLUEDIN
. "$($scriptsFolder)$($sep)3-prepare-cluedin.ps1"

# 4- CONFIGURE VALUES.YML
. "$($scriptsFolder)$($sep)4-configure-values-yaml.ps1"

# 5- INSTALL CLUEDIN
. "$($scriptsFolder)$($sep)5-install-cluedin.ps1"