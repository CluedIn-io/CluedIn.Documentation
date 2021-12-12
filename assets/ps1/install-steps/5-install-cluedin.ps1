# Install CluedIn
Clear-Host
Write-Host "Installation of CluedIn will start now" -ForegroundColor Yellow
Write-Host " Enter a release name for the installation, or press Enter to keep the default value (cluedin-dev): " -NoNewLine -ForegroundColor Yellow
$releaseName = Read-Host
if ([System.String]::IsNullOrWhiteSpace($releaseName)){
	$releaseName = "cluedin-dev"
}
$pathToValues = "$($cluedinInstallFolder)$($sep)values.yml"
helm upgrade $releaseName cluedin/cluedin -n $cluedinNamespace --install --values $pathToValues --debug

Write-Host "CluedIn resources are currently being spun-up..." -ForegroundColor Yellow
Write-Host "If you wish to close this PowerShell session and check the statuses of the CluedIn pods later manually by running `kubectl get pods -n $cluedinNamespace`, you can press CTRL+C now. "
Write-Host "Otherwise, if you leave this session alive, the statuses of the CluedIn pods will be refreshed every 20 seconds..." -ForegroundColor Yellow
while($true){
    kubectl get pods -n $cluedinNamespace
    Write-Host ""
    Write-Host "Pods' Statuses will be refreshed in 20 seconds..." -ForegroundColor Yellow
    Start-Sleep -Seconds 20
}