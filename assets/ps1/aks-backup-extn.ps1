param (
    [string]$aksclustername,
    [string]$aksclusterrg,
    [string]$storageaccountname,
    [string]$containername,
    [string]$stroragerg
)

function Read-HostIfEmpty {
  param (
      [string]$value,
      [string]$prompt
  )
  
  if (-not $value) {
      $value = Read-Host $prompt
  }
  
  return $value
}

# Prompt for missing parameters
$aksclustername = Read-HostIfEmpty $aksclustername "Enter AKS Cluster Name"
$aksclusterrg = Read-HostIfEmpty $aksclusterrg "Enter AKS Cluster Resource Group"
$storageaccountname = Read-HostIfEmpty $storageaccountname "Enter Storage Account Name"
$containername = Read-HostIfEmpty $containername "Enter Blob Container Name"
$stroragerg = Read-HostIfEmpty $stroragerg "Enter Storage Resource Group"




# Variable assignment
$installExtensions = 1


# Get subscription id, subscription name, and tenant id of the current subscription
$subscriptionInfo = az account show --query "[id, name, tenantId]" --output tsv
$subscriptionId = $subscriptionInfo[0]
#$subscriptionName = $subscriptionInfo[1]
$tenantId = $subscriptionInfo[2]

# Function to check command success
function checkSuccess {
    param (
        [string]$msg
    )
    if ($LASTEXITCODE -ne 0) {
        Write-Host $msg
        exit 1
    }
}

function providerRegistration {
    # Check and install Microsoft.KubernetesConfiguration provider
    $providerstatus = az provider show --namespace Microsoft.KubernetesConfiguration --query "registrationState" --output tsv

    if ($providerstatus -ne "Registered") {
        Write-Host "Registering Microsoft.KubernetesConfiguration Provider..."

        az provider register --namespace Microsoft.KubernetesConfiguration --accept-terms --wait

        if ($LASTEXITCODE -eq 0) {
            Write-Host "[Microsoft.KubernetesConfiguration] provider successfully installed"
        }
        else {
            Write-Host "Failed to install [Microsoft.KubernetesConfiguration] provider"
        }
    }

    # Install aks-preview Azure extension
    if ($installExtensions -eq 1) {
        Write-Host "Checking if [aks-preview] extension is already installed..."
        az extension show --name aks-preview | Out-Null
        if ($LASTEXITCODE -eq 0) {
            Write-Host "[aks-preview] extension is already installed"
            Write-Host "Updating [aks-preview] extension..."
            az extension update --name aks-preview | Out-Null # Update the extension to make sure you have the latest version installed
        }
        else {
            Write-Host "[aks-preview] extension is not installed. Installing..."
            # Install aks-preview extension
            az config set extension.use_dynamic_install=yes_without_prompt
            az extension add --name aks-preview | Out-Null
            if ($LASTEXITCODE -eq 0) {
                Write-Host "[aks-preview] extension successfully installed"
            }
            else {
                Write-Host "Failed to install [aks-preview] extension"
                exit
            }
        }

        # Registering AKS feature extensions
        $aksExtensions = @("TrustedAccessPreview")
        $ok = 0
        $registeringExtensions = @()
        foreach ($aksExtension in $aksExtensions) {
            Write-Host "Checking if [$aksExtension] extension is already registered..."
            $extension = az feature list --query "[?contains(name, 'Microsoft.ContainerService/$aksExtension') && @.properties.state == 'Registered'].{Name:name}" --output tsv
            if (-not $extension) {
                Write-Host "[$aksExtension] extension is not registered."
                Write-Host "Registering [$aksExtension] extension..."
                az feature register --name $aksExtension --namespace Microsoft.ContainerService
                $registeringExtensions += $aksExtension
                $ok = 1
            }
            else {
                Write-Host "[$aksExtension] extension is already registered."
            }
        }
        Write-Host $registeringExtensions
        $delay = 1
        foreach ($aksExtension in $registeringExtensions) {
            Write-Host -NoNewline "Checking if [$aksExtension] extension is already registered..."
            while ($true) {
                $extension = az feature list --query "[?contains(name, 'Microsoft.ContainerService/$aksExtension') && @.properties.state == 'Registered'].{Name:name}" --output tsv
                if (-not $extension) {
                    Write-Host -NoNewline "."
                    Start-Sleep -Seconds $delay
                }
                else {
                    Write-Host "."
                    break
                }
            }
        }

        if ($ok -eq 1) {
            Write-Host "Refreshing the registration of the Microsoft.ContainerService resource provider..."
            az provider register --namespace Microsoft.ContainerService
            Write-Host "Microsoft.ContainerService resource provider registration successfully refreshed"
        }
    }
}

function Install-AksExtension {
    # Install AKS backup extension
    $command = "az k8s-extension create --name azure-aks-backup --extension-type microsoft.dataprotection.kubernetes --scope cluster --cluster-type managedClusters --cluster-name  ""$aksclustername"" --resource-group ""$aksclusterrg"" --release-train stable --configuration-settings blobContainer=""$containername"" storageAccount=""$storageaccountname""   storageAccountResourceGroup=""$stroragerg"" storageAccountSubscriptionId=""$subscriptionId"""
    Write-Host "ℹ️ - Installing AKS Backup Extension" 
    Invoke-Expression $command
    checkSuccess "🛑 - AKS Backup extension installation failed" 

    $aksExtensionInfo = az k8s-extension show --name azure-aks-backup --cluster-type managedClusters --cluster-name $aksclustername --resource-group $aksclusterrg --query "aksAssignedIdentity.principalId" --output tsv
    checkSuccess

    $principalId = $aksExtensionInfo
    az role assignment create --assignee-object-id $principalId --role 'Storage Account Contributor' --scope "/subscriptions/$subscriptionId/resourceGroups/$stroragerg/providers/Microsoft.Storage/storageAccounts/$storageaccountname"
}

function Backup-Schedule {
    Write-Host =======================
    Write-Host "ℹ️ - Backup configuration " 
    Write-Host =======================

    $servicePrincipal = az ad sp create-for-rbac -n cluedin-backup --role Owner --scopes /subscriptions/$subscriptionId/resourceGroups/$stroragerg /subscriptions/$subscriptionId/resourceGroups/$aksclusterrg

    $clientId = ($servicePrincipal | ConvertFrom-Json).appId
    $PrincipalId = (az ad sp show --id $clientId |ConvertFrom-Json).id

    az role assignment create --assignee-object-id $PrincipalId --assignee-principal-type ServicePrincipal --role Reader --scope /subscriptions/$subscriptionId | Out-Null


    $clientId = ($servicePrincipal | ConvertFrom-Json).appId
    $encodedClientId = [System.Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes($clientId))


    $clientPassword = ($servicePrincipal | ConvertFrom-Json).password
    $encodedClientPassword = [System.Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes($clientPassword))


    $encodedTenantId = [System.Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes($tenantId))

    $backupinstanceid = (az dataprotection backup-instance list-from-resourcegraph --datasource-type AzureKubernetesService --datasource-id /subscriptions/$subscriptionId/resourceGroups/$aksclusterrg/providers/Microsoft.ContainerService/managedClusters/$aksclustername | ConvertFrom-Json).id

    $env:KUBECONFIG = az aks get-credentials --resource-group $aksclusterrg --name $aksclustername --overwrite-existing

    $content = @"
apiVersion: v1
kind: ServiceAccount
metadata:
  name: scaler-sa
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: deployment-scaler-up
rules:
- apiGroups: ["apps"]
  resources: ["deployments", "deployments/scale", "statefulsets", "statefulsets/scale", "services", "endpoints", "configmaps"]
  verbs: ["*"]
- apiGroups: ["extensions", "networking.k8s.io"]
  resources: ["ingresses"]
  verbs: ["*"]

---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: scaler-up-rolebinding
roleRef:
  kind: ClusterRole
  name: deployment-scaler-up
  apiGroup: rbac.authorization.k8s.io
subjects:
- kind: ServiceAccount
  name: scaler-sa
  namespace: cluedin

---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: maintenance-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: maintenance
  template:
    metadata:
      labels:
        app: maintenance
    spec:
      containers:
        - name: nginx
          image: cluedindev.azurecr.io/cluedin/nginx:latest
          ports:
          - containerPort: 80
          volumeMounts:
          - name: maintenance-page
            mountPath: /usr/share/nginx/html
          resources:
            limits:
              cpu: 25m
              memory: 64Mi
            requests:
              cpu: 10m
              memory: 64Mi
      volumes:
        - name: maintenance-page
          configMap:
            name: maintenance-page-config
      serviceAccountName: scaler-sa
      imagePullSecrets:
        - name: acr-registry-key
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: maintenance-page-config
data:
  index.html: |
    <!DOCTYPE html>
    <html>
    <head>
      <title>Site Maintenance</title>
    </head>
    <body>
      <h1>Our site is currently undergoing maintenance.</h1>
      <p>We apologize for any inconvenience. Please check back later.</p>
    </body>
    </html>
---
apiVersion: v1
kind: Service
metadata:
  name: maintenance-service
spec:
  selector:
    app: maintenance
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
---
apiVersion: v1
kind: Secret
metadata:
  name: backup-credentials
type: Opaque
data:
  client-id: $encodedclientId
  client-secret: $encodedclientPassword
  tenantId: $encodedtenantId
---
apiVersion: batch/v1
kind: CronJob
metadata:
  name: backup-and-scale
spec:
  schedule: "0 16 * * *"
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: backup-and-scale
            image: cluedindev.azurecr.io/azure/cli:2.51.0   # Replace with your own container image that includes Azure CLI
            env:
            - name: AZURE_CLIENT_ID
              valueFrom:
                secretKeyRef:
                  name: backup-credentials
                  key: client-id
            - name: AZURE_CLIENT_SECRET
              valueFrom:
                secretKeyRef:
                  name: backup-credentials
                  key: client-secret
            - name: AZURE_TENANT
              valueFrom:
                secretKeyRef:
                  name: backup-credentials
                  key: tenantId
            command: ["/bin/sh", "-c"]
            args:
              - |
                # Step 1: repoint the Ingress to maintenance page
                kubectl get ing/cluedin-ui -n cluedin -o json | jq '(.spec.rules[].http.paths[].backend.service.name | select(. == "cluedin-ui")) |= "maintenance-service"' | kubectl apply -f -
                # Step 2: Scale down deployments
                kubectl scale deployments -n cluedin --replicas=0 --all
                kubectl scale deployment/maintenance-deployment deployment/cluedin-haproxy-ingress -n cluedin --replicas=1
                sleep 60
                kubectl scale statefulsets -n cluedin --replicas=0 --all
                sleep 240
                # Step 3: Run on-demand backup
                az login --service-principal -u `$AZURE_CLIENT_ID -p `$AZURE_CLIENT_SECRET --tenant `$AZURE_TENANT >/dev/null 2>&1
                job_trigger=`$(az dataprotection backup-instance adhoc-backup --rule-name "BackupHourly" --ids $backupinstanceid) >/dev/null 2>&1
                job_id=`$(echo "`$job_trigger" | jq -r '.jobId')
                # Function to check job status
                check_job_status() {
                    status=`$(az dataprotection job show --ids `$job_id  | jq -r '.properties.status') >/dev/null 2>&1
                    echo "`$status"
                }
                # Loop until the status changes from InProgress
                while true; do
                    job_status=`$(check_job_status)

                    if [ "`$job_status" != "InProgress" ]; then
                        echo "Backup job completed"
                        echo "Scaling up deployments"
                        kubectl scale statefulsets -n cluedin --replicas=1 --all
                        sleep 60
                        kubectl scale deployments -n cluedin --replicas=1 --all
                        while true; do
                          response=`$(curl -s -o /dev/null -w "%{http_code}" "http://cluedin-server:9000/api/status")
                          if [ "`$response" -eq 200 ]; then
                            echo "Repointing ingress from maintenance-service"
                            kubectl get ing/cluedin-ui -n cluedin -o json | jq '(.spec.rules[].http.paths[].backend.service.name | select(. == "maintenance-service")) |= "cluedin-ui"' | kubectl apply -f -
                            kubectl scale deployment/maintenance-deployment -n cluedin --replicas=0
                            break
                          else
                            echo "waiting for the system back on-line"
                            sleep 30
                          fi
                        done
                        break  # Exit the loop when status changes
                    else
                        echo "Backup job status is InProgress. Waiting for backup job to complete."
                        sleep 300  # Sleep for a minute before checking again
                    fi
                done

          restartPolicy: Never
          serviceAccountName: scaler-sa
          imagePullSecrets:
            - name: acr-registry-key
"@

    $dir = New-Item (Join-Path . 'backup') -ItemType Directory -Force
    Set-Content (Join-Path $dir cluedin-backup.yaml)  -Value $content

    #
    kubectl apply -f backup/cluedin-backup.yaml -n cluedin

}
providerRegistration
Install-AksExtension
Backup-Schedule