# CLEAR SCREEN FOR BETTER USER EXPERIENCE
Clear-Host
Write-Host "Preparing the creation of the AKS Cluster..." -ForegroundColor Yellow
Write-Host "For this step, an ARM Template and its associated set of parameters will be used, you will be entering the required information shortly..." -ForegroundColor Yellow
############################################# DOWNLOAD ARM TEMPLATE #####################################################

$armTemplatePath = "$env:AzureTools\create-cluster-template.json"
$paramsPath = "$env:AzureTools\create-cluster-params.json"

if([System.IO.File]::Exists($armTemplatePath)){
	[System.IO.File]::Delete($armTemplatePath)
}
Invoke-WebRequest -Uri "$cluedinDocUrl/assets/js/create-cluster-template.json" -OutFile "$armTemplatePath"

############################################# DOWNLOAD ARM PARAMETERS ###################################################
if([System.IO.File]::Exists($paramsPath)){
	[System.IO.File]::Delete($paramsPath)
}
Invoke-WebRequest -Uri "$cluedinDocUrl/assets/js/create-cluster-params.json" -OutFile "$paramsPath"

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
Write-Host "Creation of the AKS Cluster will start now, this can take a few minutes..." -ForegroundColor Yellow
$creationResult = az deployment group create --name $deploymentName --resource-group $rgName --template-file $armTemplatePath --parameters $paramsPath
if($null -eq $creationResult) {
	Write-Host "Cluster creation failed, please check output, address issues and start over." -ForegroundColor Red
} elseif(($creationResult | ConvertFrom-Json).properties.provisioningState.ToLower() -eq "succeeded"){
	Write-Host "Cluster $clusterName was created successfully!" -ForegroundColor Green
}
Write-Host "-------------------------------------------------------------------------------------------------------" -ForegroundColor Green
Write-Host "Press press Enter to move to the next step..." -NoNewline -ForegroundColor Yellow
Read-Host