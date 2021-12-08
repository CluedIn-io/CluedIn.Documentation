# CONNECT TO AZURE
Write-Host "Connecting to Azure..." -ForegroundColor Yellow
az login
Write-Host "Successfully connected to Azure, please wait..."
Start-Sleep -Seconds 2

######################################## SET AZURE SUBSCRIPTION'S NAME OR ID #######################################
Clear-Host
Write-Host "Setting the values of variables needed later..." -ForegroundColor Yellow
Write-Host ""
Write-Host "------------------------------------Subscription--------------------------------------" -ForegroundColor Green
Write-Host ""
$subscription = Read-Host "Enter the Name or Id of the Azure subscription you will be using for your deployment"
While (($subscription -eq ""))
{
	Write-Host "Subscription cannot be empty, please enter a valid value: " -NoNewLine -ForegroundColor Red
	$subscription = Read-Host 
}
$subscriptionIsValid = (az account show --subscription $subscription)
while($null -eq $subscriptionIsValid){
	Write-Host "Please enter a valid Subscription Name or Id: " -NoNewLine -ForegroundColor Red
	$subscription = Read-Host
	if([System.String]::IsNullOrWhiteSpace($subscription)){
		Write-Host "Subscription cannot be empty or blank! " -NoNewLine -ForegroundColor Red
		$subscriptionIsValid = $null
	} else {
		$subscriptionIsValid = az account show --subscription $subscription
	}
}
# Set working subscription to current chosen subscription
az account set --subscription $subscription
#Clear unnecessary variable
$subscriptionIsValid = $null
########################################## END SUBSCRIPTION ########################################################

########################################## SET AZURE REGION ########################################################
Write-Host ""
Write-Host "-------------------------------------Region-------------------------------------------" -ForegroundColor Green
Write-Host ""
# Enter region and check it is a valid one:
$location = Read-Host "Enter the Azure Region"
While ([System.String]::IsNullOrWhiteSpace($location))
{
	$location = Read-Host "Region cannot be empty, please enter a valid value" -ForegroundColor Red
}
$location = $location.ToLower()
$availableLocationNames=(az account list-locations --query "[].{name:name}" --out tsv).Split("\t")
$availableLocationDisplayNames=(az account list-locations --query "[].{DisplayName:displayName}" --out tsv).Split("\t")
While((-not $availableLocationNames.Contains($location.ToLower())) -and (-not $availableLocationDisplayNames.Contains($location))){
	Write-Host "$location is not a valid location Name or DisplayName, please enter a valid value from the following: " -ForegroundColor Red -NoNewLine
	$commaSeparatedLocations = [System.String]::Join(", ",$availableLocationNames)
	Write-Host "$commaSeparatedLocations : " -ForegroundColor Yellow -NoNewLine
	$location = Read-Host
}
Write-Host ""
########################################## END AZURE REGION ########################################################


########################################## SET RG NAME #############################################################
Write-Host "-------------------------------Resource Group Name------------------------------------" -ForegroundColor Green
Write-Host ""
Write-Host "The default Resource Group Name is 'rg-cluedin-dev'. If you would like to override it, you can enter another value below"
Write-Host "Otherwise, please press Enter to use the default name (rg-cluedin-dev): " -NoNewLine -ForegroundColor Yellow
$rgName = Read-Host
if([System.String]::IsNullOrWhiteSpace($rgName)){
	$rgName = "rg-cluedin-dev"
}
Write-Host ""
########################################## END RG NAME #############################################################

########################################## SET AKS CLUSTER NAME ####################################################
Write-Host "--------------------------------AKS Cluster Name--------------------------------------" -ForegroundColor Green
Write-Host ""
Write-Host "The default AKS Cluster Name is 'aks-cluedin-dev'. If you would like to override it, you can enter another value below"
Write-Host "Otherwise, please press Enter to use the default name (aks-cluedin-dev): " -NoNewLine -ForegroundColor Yellow
$clusterName = Read-Host
if([System.String]::IsNullOrWhiteSpace($clusterName)){
	$clusterName = "aks-cluedin-dev"
}
Write-Host ""
########################################## END AKS CLUSTER NAME #####################################################

########################################## SET DEPLOYMENT NAME ######################################################
Write-Host ""
Write-Host "--------------------------------Deployment Name---------------------------------------" -ForegroundColor Green
Write-Host ""
$deploymentName = "aks-cluedin-dev-deployment"
Write-Host "The default AKS Deployment Name is 'aks-cluedin-dev-deployment'. If you would like to override it, you can enter another value below"
Write-Host "Otherwise, please press Enter to use the default name (aks-cluedin-dev-deployment): " -NoNewLine -ForegroundColor Yellow
$deploymentName = Read-Host
if([System.String]::IsNullOrWhiteSpace($deploymentName)){
	$deploymentName = "aks-cluedin-dev-deployment"
}
Write-Host ""
########################################## END DEPLOYMENT NAME ######################################################

########################################## BREAKDOWN OF VARIABLES ###################################################
Write-Host "------------------------------------- SUMMARY ----------------------------------------" -ForegroundColor Green
Write-Host ""
Write-Host "Your user name is " -NoNewLine
Write-Host "$env:username" -ForegroundColor Green
Write-Host "You chose the following values for your variables: " -ForegroundColor Yellow
Write-Host " 1) Azure Subscription's Id or Name: " -NoNewLine
Write-Host "$subscription" -ForegroundColor Green
Write-Host " 2) Deployment Region: " -NoNewLine
Write-Host "$location" -ForegroundColor Green
Write-Host " 3) Resource Group Name: " -NoNewLine
Write-Host "$rgName" -ForegroundColor Green
Write-Host " 4) Name of the AKS Cluster: " -NoNewLine
Write-Host "$clusterName" -ForegroundColor Green
Write-Host " 5) Name of the AKS Deployment: " -NoNewLine
Write-Host "$deploymentName" -ForegroundColor Green
Write-Host ""
Write-Host "--------------------------------------------------------------------------------------" -ForegroundColor Green
Write-Host ""
Write-Host "Press press Enter to move to the next step..." -NoNewline -ForegroundColor Yellow
Read-Host