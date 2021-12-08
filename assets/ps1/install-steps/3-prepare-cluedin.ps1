############################################# PREPARE CLUEDIN INSTALLATION ###############################################################
Clear-Host
Write-Host "Preparing CluedIn Installations..." -ForegroundColor Green
Write-Host "Merging current context to Cluster $clusterName" -ForegroundColor Yellow
az aks get-credentials --resource-group $rgName --name $clusterName

Write-Host "Proceeding with the creation of the cluedin namespace" -ForegroundColor Yellow
Write-Host "Please press Enter if you would like to use the default namespace for CluedIn (cluedin). Otherwise, please enter a value of your choice (only lower case letters and hyphens are allowed): " -NoNewLine -ForegroundColor Yellow
$cluedinNamespace = Read-Host
$regex = New-Object -TypeName System.Text.RegularExpressions.Regex -ArgumentList "^[a-z-]+$"
if(([System.String]::IsNullOrWhiteSpace($cluedinNamespace))){
	$cluedinNamespace = "cluedin"
} else {
	while(-not ($regex.IsMatch($cluedinNamespace)) -or $cluedinNamespace.EndsWith("-") -or $cluedinNamespace.StartsWith("-")) {
		Write-Host "namespace can only contain lower case letters and hyphens, please enter a valid value... " -NoNewLine -ForegroundColor Red
		$cluedinNamespace = Read-Host
	}
}
kubectl create namespace $cluedinNamespace

Write-Host "Proceeding with the installation of HAProxy Ingress Controller" -ForegroundColor Yellow
Write-Host "Adding HAProxy Helm Repo and installing the chart" -ForegroundColor Yellow
$haproxyRepoAdded = helm repo add haproxy-ingress https://haproxy-ingress.github.io/charts
if($haproxyRepoAdded.Equals('"haproxy-ingress" has been added to your repositories')){
	Write-Host $haproxyRepoAdded
	helm repo update haproxy-ingress
} elseif($haproxyRepoAdded.Equals('"haproxy-ingress" already exists with the same configuration, skipping')){
	helm repo update haproxy-ingress
}
Write-Host "Installing HAPRoxy Ingress Controller..." -ForegroundColor Yellow
helm install haproxy-ingress haproxy-ingress/haproxy-ingress --namespace=$cluedinNamespace

Write-Host ""
$res = (kubectl --namespace $cluedinNamespace get services haproxy-ingress)[1]
while ($res.ToLower().Contains('pending')) {
	Write-Host "External IP pending, trying again in 3 seconds..." -ForegroundColor Yellow
	Start-Sleep -Seconds 3
	$res = (kubectl --namespace cluedin get services haproxy-ingress)[1]
}
do {
	$res = $res.Replace("  ", " ")
} while ($res.IndexOf("  ") -gt 0)
$externalIP = $res.Split(' ')[3]
Write-Host "HAProxy Ingress Controller's External IP is $externalIP" -ForegroundColor Green
Write-Host ""
Write-Host "Now we will be proceeding with addition of CluedIn's Helm repo"
$cluedinRepoAdded = helm repo add cluedin https://cluedin-io.github.io/Charts/
if($cluedinRepoAdded.Equals('"cluedin" has been added to your repositories')){
	Write-Host $cluedinRepoAdded -ForegroundColor Green
	helm repo update cluedin
} elseif($cluedinRepoAdded.Equals('"cluedin" already exists with the same configuration, skipping')){
	helm repo update cluedin
}

Write-Host ""
Write-Host "Please have your Docker.io credentials ready..." -ForegroundColor Yellow
Start-Sleep -Seconds 3
Write-Host "Please enter your Docker username: " -NoNewLine -ForegroundColor Yellow
$dockerUserName = Read-Host
Write-Host "Please enter your Docker password: " -NoNewLine -ForegroundColor Yellow
$dockerPassword = Read-Host
Write-Host "Please enter your Docker email: " -NoNewLine -ForegroundColor Yellow
$dockerEmail = Read-Host
Write-Host "Creating Docker registry key secret with your credentials..." -ForegroundColor Yellow
kubectl create secret docker-registry docker-registry-key --namespace $cluedinNamespace --docker-server='docker.io' --docker-username=$dockerUserName --docker-password=$dockerPassword --docker-email=$dockerEmail

Write-Host "-------------------------------------------------------------------------------------------------------" -ForegroundColor Green
Write-Host "Press press Enter to move to the next step..." -NoNewline -ForegroundColor Yellow
Read-Host