# CLEAR SCREEN FOR BETTER USER EXPERIENCE
Clear-Host
Write-Host "Preparing the creation of the AKS Cluster..." -ForegroundColor Yellow
Write-Host "For this step, an ARM Template and its associated set of parameters will be used, you will be entering the required information shortly..." -ForegroundColor Yellow
############################################# DOWNLOAD ARM TEMPLATE #####################################################

$armTemplatePath = "$($cluedinInstallFolder)$($sep)create-cluster-template.json"
$paramsPath = "$($cluedinInstallFolder)$($sep)create-cluster-params.json"

if([System.IO.File]::Exists($armTemplatePath)){
	[System.IO.File]::Delete($armTemplatePath)
}
$ProgressPreference = 'SilentlyContinue'
Invoke-WebRequest -Uri "$cluedinDocUrl/assets/js/create-cluster-template.json" -OutFile "$armTemplatePath"

############################################# DOWNLOAD ARM PARAMETERS ###################################################
if([System.IO.File]::Exists($paramsPath)){
	[System.IO.File]::Delete($paramsPath)
}
Invoke-WebRequest -Uri "$cluedinDocUrl/assets/js/create-cluster-params.json" -OutFile "$paramsPath"
$ProgressPreference = 'Continue'

Write-Host "The ARM Template and the Parameters files used for the creation of the AKS Cluster have been loaded successfully." -ForegroundColor Green
Write-Host "Proceeding with the setting of required parameters for the cluster creation..."

$paramsJson = Get-Content $paramsPath | ConvertFrom-Json
$paramsJson.parameters.resourceName.value = $clusterName
$paramsJson.parameters.location.value = $location
$paramsJson.parameters.dnsPrefix.value = "$clusterName-dns"
Write-Host "Please enter the version of Kubernetes you want to use, or press enter to use the default (1.20.9): " -NoNewLine -ForegroundColor Yellow
$kubernetesVersion = Read-Host
If(-not [System.String]::IsNullOrWhiteSpace($kubernetesVersion)){
		$paramsJson.parameters.kubernetesVersion.value = $kubernetesVersion
}

# Now write the content to the Params Json file:
($paramsJson | ConvertTo-Json) | Out-File -FilePath $paramsPath
Write-Host "ARM Template and Parameters are ready. " -ForegroundColor Yellow
Write-Host "-------------------------------------------------------------------------------------------------------" -ForegroundColor Green
Write-Host "Next step will start in 3 seconds..." -ForegroundColor Yellow
Start-Sleep -Seconds 3

############################################# CREATE RESOURCE GROUP AND AKS CLUSTER  #####################################################
Clear-Host
Write-Host "Preparing the creation of the AKS Cluster..." -ForegroundColor Yellow
Write-Host "Checking if a resource group named $rgName already exists..."
if((az group exists -n $rgName).ToLower() -eq 'true') { 
	Write-Host "Resource Group $rgName exists already, it will be used for this deployment." -ForegroundColor Yellow
} else {
	Write-Host "Resource Group $rgName does not exist, creating it..." -ForegroundColor Green
	az group create --name $rgName --subscription $subscription --location $location
}
#az deployment group create --name $deploymentName --resource-group $rgName --template-file $armTemplatePath --parameters $paramsPath
$subscriptionId = (az account show --subscription $subscription --query 'id').Replace('"','')
$upn = (az ad signed-in-user show --query 'userPrincipalName')
$userDomain = $upn.Replace('"','').Substring($upn.IndexOf('@'))
$startTime = $(Get-Date)
Write-Host "Creation of the AKS Cluster will start now ($($startTime)), this can take up to 15 minutes..." -ForegroundColor Yellow
Write-Host "You can check the status in real-time on https://portal.azure.com/#@$($userDomain)/resource/subscriptions/$($subscriptionId)/resourceGroups/$($rgName)/deployments" -ForegroundColor Yellow
Write-Host ""
$creationResult = az deployment group create --name $deploymentName --resource-group $rgName --template-file $armTemplatePath --parameters $paramsPath
if($null -eq $creationResult) {
	Write-Host "Cluster creation failed, please check output, address issues and start over." -ForegroundColor Red
} elseif(($creationResult | ConvertFrom-Json).properties.provisioningState.ToLower() -eq "succeeded"){
	$elapsedTime = $(Get-Date) - $startTime
	$duration = "{0:HH:mm:ss}" -f ([datetime]$elapsedTime.Ticks)
	Write-Host "Cluster $clusterName was created successfully, process duration was $($duration)" -ForegroundColor Green
}
Write-Host "-------------------------------------------------------------------------------------------------------" -ForegroundColor Green
Write-Host "Press press Enter to move to the next step..." -NoNewline -ForegroundColor Yellow
Read-Host