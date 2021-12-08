Clear-Host
$env:AzureTools = "C:\users\$env:username\AzureTools"
Set-Location $env:AzureTools

Write-Host "Loading values.yml from CluedIn repo, please wait..." -ForegroundColor Yellow
helm inspect values cluedin/cluedin > values.yml

# Installing Powershell-Yaml module needed to change the content of the values.yml file
Set-PSRepository -Name "PSGallery" -InstallationPolicy Trusted
# Write-Host "The PowerShell-Yaml module is needed to change the content of the values.yml file, installing the module now, it will be uninstalled once we are done." -ForegroundColor Yellow
Install-Module powershell-yaml
Import-Module powershell-yaml

$yaml = Get-Content "$env:AzureTools\values.yml" | ConvertFrom-Yaml
Write-Host "Content of values.yml was loaded successfully" -ForegroundColor Green
Write-Host "Setting up your default organization and admin credentials" -ForegroundColor Yellow
Write-Host "Please enter the name of the organization you would like to use, please use only letters and numbers: " -NoNewLine
$orgName = Read-Host
$orgRegex = New-Object -TypeName System.Text.RegularExpressions.Regex -ArgumentList '^[a-zA-Z][a-zA-Z0-9]*$'
while(-not ($orgRegex.IsMatch($orgName))){
	Write-Host "Organization Name is invalid, you can only use letters and numbers with no spaces, hyphens or underscores. " -ForegroundColor Red
	Write-Host "Please enter a valid Organization Name: " -ForegroundColor Yellow
	$orgName = Read-Host
}
Write-Host "If you would like to use the same Organization Name as prefix, press Enter. Otherwise, please enter a different prefix: " -NoNewLine -ForegroundColor Yellow
$orgPrefixRegex = New-Object -TypeName System.Text.RegularExpressions.Regex -ArgumentList '^[a-zA-Z][a-zA-Z0-9-]*$'
$orgPrefix = Read-Host
if([System.String]::IsNullOrWhiteSpace($orgPrefix)){
	$orgPrefix = $orgName
} else {
	while($orgPrefix.EndsWith('-') -or (-not $orgPrefixRegex.IsMatch($orgPrefix))){
		Write-Host "Organization Prefix is invalid, please use only letters, numbers or hyphens with no spaces." -ForegroundColor Red
		Write-Host "Please enter an Organization Prefix, or press Enter if you want to use the Organization Name as prefix too: " -NoNewLine Yellow
		$orgPrefix = Read-Host
		if([System.String]::IsNullOrWhiteSpace($orgPrefix)){
			$orgPrefix = $orgName
			break
		}
	}
}

Write-Host "Please enter the email of CluedIn's admin: " -NoNewLine -ForegroundColor Yellow
$emailRegex = New-Object -TypeName System.Text.RegularExpressions.Regex -ArgumentList '^[^@\s]+@[^@\s]+\.[^@\s]+$'
$adminEmail = Read-Host
while(-not $emailRegex.IsMatch($adminEmail)){
	Write-Host "Email is not in a valid format, please enter a valid email: " -NoNewLine -ForegroundColor Red
	$adminEmail = Read-Host
}
Write-Host "Please enter a strong password for the CluedIn's admin, no spaces are allowed: " -NoNewLine -ForegroundColor Yellow
$adminPassword = Read-Host
while ($adminPassword.Contains(' ')) {
	Write-Host "Password cannot contain spaces, please enter a valid password: " -NoNewLine -ForegroundColor Red
	$adminPassword = Read-Host
} 
$emailDomain = $adminEmail.Substring($adminEmail.IndexOf('@') + 1)
Write-Host "Based on provided admin email, email domain is " -NoNewLine -ForegroundColor Yellow
Write-Host $emailDomain -ForegroundColor Green
$adminUsername = $adminEmail

$yaml.bootstrap.organization.name = $orgName
$yaml.bootstrap.organization.prefix = $orgPrefix
$yaml.bootstrap.organization.email = $adminEmail
$yaml.bootstrap.organization.username = $adminUsername
$yaml.bootstrap.organization.password = $adminPassword
$yaml.bootstrap.organization.emailDomain = $emailDomain

Write-Host "Organization & Admin settings complete..." -ForegroundColor Green

Write-Host ""
Write-Host "Setting DNS configuration" -ForegroundColor Yellow
Write-Host "Would you like to add DNS configuration for your installation? (Y/N)" -ForegroundColor Yellow
$choice = Read-Host
if((-not [System.String]::IsNullOrWhiteSpace($choice)) -and ($choice.ToLower().Equals('y'))){
	Write-Host "Please enter the hostname you are assigning to the CluedIn application (for example cluedin-dev.companyName.com, or companyName.com if you are using no prefix): " -ForegroundColor Yellow
	$hostname = Read-Host
	$yaml.global.dns.hostname = $hostname
}else{
	Write-Host "Setting External IP for hostname..."
	$hostname = "$externalIP.nip.io"
	$yaml.global.dns.hostname = $hostname
}

Write-Host "Do you want to override the default subdomains (app, clean, grafana, promotheus, alertmanager & seq)? (Y/N) " -NoNewLine -ForegroundColor Yellow
$choice = Read-Host
if((-not [System.String]::IsNullOrWhiteSpace($choice)) -and ($choice.ToLower().Equals('y'))){
	Write-Host "Please enter the custom prefix for the App URL, <appPrefix>.$hostname (Only alphanumeric and '-' are allowed): " -NoNewLine -ForegroundColor Yellow
	$appPrefix = Read-Host
	$yaml.global.dns.subdomains.application = $appPrefix
	
	Write-Host "Please enter the custom prefix for the Clean URL, <cleanPrefix>.$hostname (Only alphanumeric and '-' are allowed): " -NoNewLine -ForegroundColor Yellow
	$cleanPrefix = Read-Host
	$yaml.global.dns.subdomains.openrefine = $cleanPrefix
	
	Write-Host "Please enter the custom prefix for the Grafana URL, <grafanaPrefix>.$hostname (Only alphanumeric and '-' are allowed): " -NoNewLine -ForegroundColor Yellow
	$grafanaPrefix = Read-Host
	$yaml.global.dns.subdomains.grafanaAdmin = $grafanaPrefix
	
	Write-Host "Please enter the custom prefix for the Promotheus URL, <promotheusPrefix>.$hostname  (Only alphanumeric and '-' are allowed): " -NoNewLine -ForegroundColor Yellow
	$promotheusPrefix = Read-Host
	$yaml.global.dns.subdomains.prometheusAdmin = $promotheusPrefix
	
	Write-Host "Please enter the custom prefix for the Alert Manager URL, <alertManagerPrefix>.$hostname  (Only alphanumeric and '-' are allowed): " -NoNewLine -ForegroundColor Yellow
	$alertMgrPrefix = Read-Host
	$yaml.global.dns.subdomains.alertManagerAdmin = $alertMgrPrefix
	
	Write-Host "Please enter the custom prefix for the Seq URL, <seqPrefix>.$hostname  (Only alphanumeric and '-' are allowed): " -NoNewLine -ForegroundColor Yellow
	$seqPrefix = Read-Host
	$yaml.global.dns.subdomains.seq = $seqPrefix
} else {
	Write-Host "Default prefixes will be used for your URLs:" -ForegroundColor Yellow
	Write-Host " " $yaml.global.dns.subdomains.application -NoNewLine -ForegroundColor Green
	Write-Host $hostname -ForegroundColor Yellow
	Write-Host " " $yaml.global.dns.subdomains.openrefine -NoNewLine -ForegroundColor Green
	Write-Host $hostname -ForegroundColor Yellow
	Write-Host " " $yaml.global.dns.subdomains.grafanaAdmin -NoNewLine -ForegroundColor Green
	Write-Host $hostname -ForegroundColor Yellow
	Write-Host " " $yaml.global.dns.subdomains.prometheusAdmin -NoNewLine -ForegroundColor Green
	Write-Host $hostname -ForegroundColor Yellow
	Write-Host " " $yaml.global.dns.subdomains.alertManagerAdmin -NoNewLine -ForegroundColor Green
	Write-Host $hostname -ForegroundColor Yellow
	Write-Host " " $yaml.global.dns.subdomains.seq -NoNewLine -ForegroundColor Green
	Write-Host $hostname -ForegroundColor Yellow
}

Write-Host ""
Write-Host "DNS Configuration done, proceeding with SSL/HTTPS configuration..." -ForegroundColor Yellow
Write-Host "Do you wish to configure SSL/HTTPS for your CluedIn instance? (Y/N)"
$choice = Read-Host
if((-not [System.String]::IsNullOrWhiteSpace($choice)) -and ($choice.ToLower().Equals('y'))){
	$yaml.global.ingress.forceHttps = true
	Write-Host "Configuring hosts in your SSL certificate: " -NoNewLine -ForegroundColor Yellow
	Write-Host "  Does your certificate have:" -ForegroundColor Yellow
	Write-Host "   1- Wildcard host *.$hostname (Enter 1)" -ForegroundColor Yellow
	Write-Host "   2- Specific named hosts: $appPrefix.$hostname, $cleanPrefix.$hostname, $orgPrefix.$hostname etc..." -ForegroundColor Yellow
	Write-Host "Please enter 1 or 2: " -NoNewLine -ForegroundColor Yellow
	$choice = Read-Host
	while(([System.String]::IsNullOrWhiteSpace($choice)) -or ((-not $choice.Equals("1")) -and (-not $choice.Equals("1")))) {
		Write-Host "Only 1 or 2 are valid options, please enter a value: " -NoNewLine -ForegroundColor Red
		$choice = Read-Host
	}
	if($choice.Equals("1")){
		$yaml.global.ingress.tls.hosts.Add("*.$hostname")
	} elseif($choice.Equals("2")){
		$yaml.global.ingress.tls.hosts.Add("$appPrefix.$hostname")
		$yaml.global.ingress.tls.hosts.Add("$orgPrefix.$hostname")
		Write-Host " $appPrefix.$hostname and $orgPrefix.$hostname were added to hosts" -ForegroundColor Green
		$secondarySubdomains = New-Object System.Collections.Generic.List[System.String]
		[string[]] $a = "$cleanPrefix.$hostname","$grafanaPrefix.$hostname","$promotheusPrefix.$hostname","$alertMgrPrefix.$hostname","$seqPrefix.$hostname"
		$secondarySubdomains.AddRange($a)
		foreach($sd in $secondarySubdomains){
			Write-Host " Add $sd to hosts? (Y/N)" -ForegroundColor Yellow
			$decision = Read-Host
			if((-not [System.String]::IsNullOrWhiteSpace($decision)) -and ($decision.ToLower().Equals('y'))){
				$yaml.global.ingress.tls.hosts.Add($sd)
				Write-Host " $sd was added to hosts" -ForegroundColor Green
			}
		}
	}
	
	# CREATE SSL SECRET AND ADD IT TO VALUES.YAML
	Write-Host ""
	Write-Host "Now you need to create a secret with the Certificate's tls.crt and tls.key files, please ensure you have the files saved locally on your machine before proceeding..." -ForegroundColor Yellow
	Write-Host "  Enter the name of the secret (only letters and hyphens), or press Enter to use the default (ssl-cert-secret): " -ForegroundColor Yellow
	$sslSecretName = Read-Host
	if([System.String]::IsNullOrWhiteSpace($sslSecretName)){
		$sslSecretName = "ssl-cert-secret"
	}
	Write-Host " Enter the path to the tls.key file (private key): " -ForegroundColor Yellow
	$privateKeyPath = Read-Host
	while((-not [System.IO.File]::Exists($privateKeyPath)) -or ([System.String]::IsNullOrWhiteSpace($privateKeyPath)) -or (-not $privateKeyPath.EndsWith("tls.key"))){
		Write-Host " Please enter a valid path to tls.key: " -NoNewLine -ForegroundColor Red
		$privateKeyPath = Read-Host
	}
	Write-Host " Enter the path to the tls.crt file (public certificate): " -ForegroundColor Yellow
	$publicCertPath = Read-Host
	while((-not [System.IO.File]::Exists($publicCertPath)) -or ([System.String]::IsNullOrWhiteSpace($publicCertPath)) -or (-not $publicCertPath.EndsWith("tls.crt"))){
		Write-Host " Please enter a valid path to tls.crt: " -NoNewLine -ForegroundColor Red
		$publicCertPath = Read-Host
	}
	$res = kubectl create secret tls $sslSecretName --key $privateKeyPath --cert $publicCertPath
	Write-Host $res -ForegroundColor Yellow
}
# Save changes to values.yml
Write-Host ""
Write-Host "Saving changes to values.yml" -ForegroundColor Yellow
($yaml | ConvertTo-Yaml) | Out-File -FilePath "$env:AzureTools\values.yml"

Write-Host "-------------------------------------------------------------------------------------------------------" -ForegroundColor Green
Write-Host "Press press Enter to move to the next step..." -NoNewline -ForegroundColor Yellow
Read-Host