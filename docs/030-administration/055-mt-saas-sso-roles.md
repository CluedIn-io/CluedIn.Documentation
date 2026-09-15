---
layout: cluedin
nav_order: 4
parent: Roles
grand_parent: Administration
permalink: /administration/roles/mt-saas-sso-roles
title: Configure Microsoft Entra roles for multi-tenant SaaS SSO
tags: ["administration", "roles", "sso", "saas", "entra"]
last_modified: 2026-09-15
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

This article explains how to configure Microsoft Entra application roles for **CluedIn multi-tenant (MT) SaaS** when using Microsoft Entra ID single sign-on (SSO) with automatic role synchronization.

{:.important}
This article applies to **CluedIn multi-tenant SaaS**. It does not describe the application-registration flow used by CluedIn PaaS or Private SaaS deployments.

## How SSO works in multi-tenant SaaS

CluedIn multi-tenant SaaS uses a CluedIn-managed, multi-tenant Microsoft Entra application registration. The application registration is owned by CluedIn and is not created in the customer tenant.

When a customer enables Microsoft Entra SSO, Microsoft Entra creates or uses a local **Enterprise application** in the customer tenant. In Microsoft Entra terminology, this Enterprise application is the **service principal**: the local representation of the CluedIn multi-tenant application in that tenant.

Because the customer does not own the CluedIn application registration, the customer cannot add app roles through **App registrations > App roles**. Instead, tenant-specific app roles are added to the customer tenant's CluedIn **service principal** by using Microsoft Graph.

Microsoft supports this scenario explicitly: app roles that should exist only in one tenant for a multi-tenant application can be added to the `appRoles` collection of the service principal.

The role flow is:

1. Create the CluedIn app roles on the CluedIn Enterprise application (service principal) in the customer tenant.
2. Assign users or Microsoft Entra groups to those roles.
3. Microsoft Entra emits the assigned role values in the `roles` claim when the user signs in.
4. CluedIn reads the role claim and maps the values to CluedIn roles when **Automatic Role Synchronization** is enabled.

{:.important}
The **Value** of the Microsoft Entra app role is the value sent in the `roles` claim. Use the CluedIn role values shown in this article exactly. The display name can be more descriptive, but the value should remain stable.

## Prerequisites

Before configuring roles, make sure that:

- Microsoft Entra SSO has already been enabled for the CluedIn organization.
- The CluedIn Enterprise application exists in the customer Microsoft Entra tenant.
- You can access **Microsoft Entra admin center > Enterprise applications**.
- You have sufficient Microsoft Entra administrative rights. Microsoft specifically documents **Privileged Role Administrator** for the Graph Explorer role-management procedure. A **Global Administrator** also has sufficient administrative rights.
- If you use Microsoft Graph Explorer, Graph Explorer can receive the required delegated Microsoft Graph permissions in the tenant.
- **Automatic Role Synchronization** is enabled in CluedIn before testing role synchronization.

## CluedIn role values

The following role values can be used for the standard CluedIn roles.

| Display name | Value | Description |
|--|--|--|
| Data Governance Administrator | `DataGovernanceAdministrator` | Role responsible for approving changes made by Data Governance users. |
| Data Compliance | `DataCompliance` | Role responsible for daily operations around data compliance. |
| Data Steward | `DataSteward` | Role dedicated to cleaning data using Clean and Prepare modules. |
| Data Compliance Administrator | `DataComplianceAdministrator` | Role responsible for approving changes made by Data Compliance users. |
| Guest | `Guest` | Guest user with minimal, read-only permissions. |
| User | `User` | User who can view all modules as read-only. |
| Data Architect | `DataArchitect` | Role responsible for designing an organization's enterprise data strategy. |
| Deduplication Reviewer | `DeduplicationReviewer` | Role responsible for reviewing deduplication project results and approving groupings. |
| Organization User | `OrganizationUser` | User within an organization who can view all modules as read-only. |
| Data Governance | `DataGovernance` | Role responsible for monitoring and maintaining data quality. |
| Report Manager | `ReportManager` | User who can generate reports for compliance matters such as breach, subject request, and retention. |
| Organization Admin | `OrganizationAdmin` | Administrator within the organization. |
| Deduplication Administrator | `DeduplicationAdministrator` | Role responsible for creating and maintaining deduplication projects and merging the results back into the system. |
| Data Steward Administrator | `DataStewardAdministrator` | Role responsible for approving changes made by Data Stewards. |

## Method 1: Configure roles with Microsoft Graph Explorer

Graph Explorer is useful for a one-off configuration or for inspecting the service principal before automation.

### Find the CluedIn service principal Object ID

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com/).
2. Go to **Entra ID > Enterprise applications > All applications**.
3. Open the CluedIn application used for SSO.
4. On **Overview**, copy the **Object ID**.

{:.important}
Use the **Object ID** of the Enterprise application, not the Application (client) ID. Microsoft Graph addresses this local service principal by its Object ID.

### Grant Graph Explorer permissions

Open [Microsoft Graph Explorer](https://developer.microsoft.com/graph/graph-explorer), sign in to the customer tenant, and verify the tenant shown in the Graph Explorer header.

Microsoft's dedicated Enterprise application role-management guidance instructs administrators to use **Privileged Role Administrator** and consent to:

- `Application.ReadWrite.All`
- `Directory.ReadWrite.All`

The current Microsoft Graph `PATCH /servicePrincipals/{id}` reference lists `Application.ReadWrite.All` as the least-privileged delegated permission and `Directory.ReadWrite.All` as a higher-privileged alternative. If your organization follows least privilege strictly, `Application.ReadWrite.All` is sufficient for the service-principal update API; the dedicated Microsoft role-management walkthrough currently requests both permissions.

In Graph Explorer, select your profile avatar and choose **Consent to permissions**. Search for the permissions and grant consent.

#### If the Consent to permissions list is empty

An empty permissions list is not expected. Before trying to change the CluedIn Enterprise application, verify Graph Explorer itself is correctly consented in the tenant:

1. In Microsoft Entra admin center, go to **Enterprise applications**.
2. Search for **Graph explorer**.
3. Open the Graph Explorer Enterprise application.
4. Open **Permissions**.
5. Select **Grant admin consent** for the tenant if required.
6. Sign out of Graph Explorer, sign in again, and verify the correct tenant.

If the permissions list remains empty, use the PowerShell method later in this article. The PowerShell method does not depend on the Graph Explorer permissions UI.

### Read the existing app roles

In Graph Explorer, select `GET` and run:

```http
https://graph.microsoft.com/v1.0/servicePrincipals/<SERVICE-PRINCIPAL-OBJECT-ID>?$select=id,appId,displayName,appRoles
```

Save the returned `appRoles` collection before making any changes.

{:.warning}
A PATCH of `appRoles` replaces the collection. **Do not send only the new CluedIn roles.** Existing roles must also be included or they can be removed from the service principal.

A service principal can contain an existing role such as `msiam_access`. Preserve it.

Microsoft Graph returns the read-only `origin` property on app roles. The `appRole` API documentation states that `origin` must not be included in POST or PATCH requests, so remove `origin` from each role object before sending the PATCH.

### Add a role

Each role requires a unique GUID in its `id` property. For example, to add the `OrganizationAdmin` role, append an object like this to the existing `appRoles` array:

```json
{
  "allowedMemberTypes": [
    "User"
  ],
  "description": "Administrator within the organization.",
  "displayName": "Organization Admin",
  "id": "<NEW-GUID>",
  "isEnabled": true,
  "value": "OrganizationAdmin"
}
```

Generate a new GUID for each new role. For example, in PowerShell:

```powershell
[guid]::NewGuid().Guid
```

After adding all required roles, change Graph Explorer to `PATCH` and use:

```http
https://graph.microsoft.com/v1.0/servicePrincipals/<SERVICE-PRINCIPAL-OBJECT-ID>
```

The request body must contain the complete role collection:

```json
{
  "appRoles": [
    {
      "allowedMemberTypes": ["User"],
      "description": "<EXISTING-ROLE-DESCRIPTION>",
      "displayName": "<EXISTING-ROLE-DISPLAY-NAME>",
      "id": "<EXISTING-ROLE-ID>",
      "isEnabled": true,
      "value": null
    },
    {
      "allowedMemberTypes": ["User"],
      "description": "Administrator within the organization.",
      "displayName": "Organization Admin",
      "id": "<NEW-GUID>",
      "isEnabled": true,
      "value": "OrganizationAdmin"
    }
  ]
}
```

A successful update normally returns `204 No Content`.

Run the GET request again and verify that all expected roles are present.

## Method 2: Configure all roles with Microsoft Graph PowerShell

For repeatable deployments, PowerShell is safer than manually editing the `appRoles` collection. The script in this section:

- connects to a specific tenant;
- reads and preserves all existing app roles;
- creates any missing standard CluedIn roles;
- updates the metadata of matching CluedIn roles while preserving their existing role IDs;
- removes the read-only `origin` property from the PATCH payload;
- creates a timestamped JSON backup before changing anything;
- supports `-WhatIf`;
- can export the exact PATCH body for review or use in Graph Explorer;
- verifies the roles after the PATCH;
- optionally assigns Microsoft Entra groups to roles from a CSV file.

### Install Microsoft Graph PowerShell

PowerShell 7 is recommended.

```powershell
Install-Module Microsoft.Graph.Authentication -Scope CurrentUser
```

The script uses `Invoke-MgGraphRequest`, so the Authentication module is sufficient for the Graph calls.

### PowerShell script

Save the following as `Set-CluedInMtSaasAppRoles.ps1`.

```powershell
[CmdletBinding(SupportsShouldProcess = $true, ConfirmImpact = 'High')]
param(
    [Parameter(Mandatory = $true)]
    [Guid]$TenantId,

    [Parameter(Mandatory = $true)]
    [Guid]$ServicePrincipalObjectId,

    [switch]$UseDeviceCode,

    [ValidateNotNullOrEmpty()]
    [string]$BackupDirectory = '.',

    [string]$ExportPatchPath,

    # Optional CSV with columns: GroupObjectId,RoleValue
    [string]$GroupRoleMappingCsv
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Assert-MicrosoftGraphAuthenticationModule {
    if (-not (Get-Module -ListAvailable -Name Microsoft.Graph.Authentication)) {
        throw @'
Microsoft.Graph.Authentication is not installed.
Install it with:
  Install-Module Microsoft.Graph.Authentication -Scope CurrentUser
'@
    }

    Import-Module Microsoft.Graph.Authentication -ErrorAction Stop
}

function Connect-CluedInGraph {
    param(
        [Parameter(Mandatory = $true)]
        [Guid]$Tenant,

        [switch]$DeviceCode,

        [switch]$EnableGroupAssignments
    )

    $scopes = @('Application.ReadWrite.All')

    if ($EnableGroupAssignments) {
        $scopes += @(
            'AppRoleAssignment.ReadWrite.All',
            'Group.Read.All'
        )
    }

    $connectParameters = @{
        TenantId     = $Tenant.Guid
        Scopes       = $scopes
        ContextScope = 'Process'
        NoWelcome    = $true
    }

    if ($DeviceCode) {
        $connectParameters['UseDeviceCode'] = $true
    }

    Connect-MgGraph @connectParameters

    $context = Get-MgContext
    if (-not $context) {
        throw 'Microsoft Graph authentication did not return a context.'
    }

    if ($context.TenantId -ne $Tenant.Guid) {
        throw "Connected to tenant '$($context.TenantId)' instead of '$($Tenant.Guid)'."
    }

    $missingScopes = @(
        $scopes | Where-Object { $context.Scopes -notcontains $_ }
    )

    if ($missingScopes.Count -gt 0) {
        throw "The access token is missing required scopes: $($missingScopes -join ', ')"
    }

    Write-Host "Connected account : $($context.Account)"
    Write-Host "Connected tenant  : $($context.TenantId)"
    Write-Host "Granted scopes    : $($context.Scopes -join ', ')"
}

function Get-CluedInRoleDefinitions {
    @(
        [pscustomobject]@{
            DisplayName = 'Data Governance Administrator'
            Value       = 'DataGovernanceAdministrator'
            Description = 'Role responsible for approving changes made by Data Governance users.'
        }
        [pscustomobject]@{
            DisplayName = 'Data Compliance'
            Value       = 'DataCompliance'
            Description = 'Role responsible for daily operations around data compliance.'
        }
        [pscustomobject]@{
            DisplayName = 'Data Steward'
            Value       = 'DataSteward'
            Description = 'Role dedicated to cleaning data using Clean and Prepare modules.'
        }
        [pscustomobject]@{
            DisplayName = 'Data Compliance Administrator'
            Value       = 'DataComplianceAdministrator'
            Description = 'Role responsible for approving changes made by Data Compliance users.'
        }
        [pscustomobject]@{
            DisplayName = 'Guest'
            Value       = 'Guest'
            Description = 'Guest user with minimal, read-only permissions.'
        }
        [pscustomobject]@{
            DisplayName = 'User'
            Value       = 'User'
            Description = 'User who can view all modules as read-only.'
        }
        [pscustomobject]@{
            DisplayName = 'Data Architect'
            Value       = 'DataArchitect'
            Description = "Role responsible for designing an organization's enterprise data strategy."
        }
        [pscustomobject]@{
            DisplayName = 'Deduplication Reviewer'
            Value       = 'DeduplicationReviewer'
            Description = 'Role responsible for reviewing deduplication project results and approving groupings.'
        }
        [pscustomobject]@{
            DisplayName = 'Organization User'
            Value       = 'OrganizationUser'
            Description = 'User within an organization who can view all modules as read-only.'
        }
        [pscustomobject]@{
            DisplayName = 'Data Governance'
            Value       = 'DataGovernance'
            Description = 'Role responsible for monitoring and maintaining data quality.'
        }
        [pscustomobject]@{
            DisplayName = 'Report Manager'
            Value       = 'ReportManager'
            Description = 'User who can generate reports for compliance matters such as breach, subject request, and retention.'
        }
        [pscustomobject]@{
            DisplayName = 'Organization Admin'
            Value       = 'OrganizationAdmin'
            Description = 'Administrator within the organization.'
        }
        [pscustomobject]@{
            DisplayName = 'Deduplication Administrator'
            Value       = 'DeduplicationAdministrator'
            Description = 'Role responsible for creating and maintaining deduplication projects and merging the results back into the system.'
        }
        [pscustomobject]@{
            DisplayName = 'Data Steward Administrator'
            Value       = 'DataStewardAdministrator'
            Description = 'Role responsible for approving changes made by Data Stewards.'
        }
    )
}

function Get-ServicePrincipalWithAppRoles {
    param(
        [Parameter(Mandatory = $true)]
        [Guid]$ObjectId
    )

    $uri = "https://graph.microsoft.com/v1.0/servicePrincipals/$($ObjectId.Guid)?`$select=id,appId,displayName,appRoleAssignmentRequired,appRoles"

    $servicePrincipal = Invoke-MgGraphRequest `
        -Method GET `
        -Uri $uri `
        -OutputType PSObject

    if (-not $servicePrincipal.id) {
        throw "Service principal '$($ObjectId.Guid)' was not found."
    }

    return $servicePrincipal
}

function ConvertTo-PatchableAppRole {
    param(
        [Parameter(Mandatory = $true)]
        $Role
    )

    # Do not include origin. Microsoft Graph documents origin as read-only.
    [ordered]@{
        allowedMemberTypes = @($Role.allowedMemberTypes)
        description        = [string]$Role.description
        displayName        = [string]$Role.displayName
        id                 = [string]$Role.id
        isEnabled          = [bool]$Role.isEnabled
        value              = $Role.value
    }
}

function Merge-CluedInAppRoles {
    param(
        [Parameter(Mandatory = $true)]
        $ExistingRoles,

        [Parameter(Mandatory = $true)]
        $Definitions
    )

    $existing = @($ExistingRoles)
    $merged = [System.Collections.Generic.List[object]]::new()
    $changes = [System.Collections.Generic.List[object]]::new()

    $duplicateValues = @(
        $existing |
            Where-Object { $null -ne $_.value -and -not [string]::IsNullOrWhiteSpace([string]$_.value) } |
            Group-Object -Property value |
            Where-Object Count -gt 1
    )

    if ($duplicateValues.Count -gt 0) {
        $values = $duplicateValues.Name -join ', '
        throw "The service principal contains duplicate app role values: $values"
    }

    # Start by preserving every existing role, including non-CluedIn roles.
    foreach ($role in $existing) {
        $merged.Add((ConvertTo-PatchableAppRole -Role $role))
    }

    foreach ($definition in $Definitions) {
        $matchingIndex = -1

        for ($i = 0; $i -lt $merged.Count; $i++) {
            if ($null -ne $merged[$i].value -and
                ([string]$merged[$i].value -ceq [string]$definition.Value)) {
                $matchingIndex = $i
                break
            }
        }

        if ($matchingIndex -ge 0) {
            $existingRole = $merged[$matchingIndex]
            $changed = $false

            if ([string]$existingRole.displayName -cne [string]$definition.DisplayName) {
                $existingRole.displayName = $definition.DisplayName
                $changed = $true
            }

            if ([string]$existingRole.description -cne [string]$definition.Description) {
                $existingRole.description = $definition.Description
                $changed = $true
            }

            if (-not $existingRole.isEnabled) {
                $existingRole.isEnabled = $true
                $changed = $true
            }

            if (@($existingRole.allowedMemberTypes).Count -ne 1 -or
                @($existingRole.allowedMemberTypes)[0] -cne 'User') {
                $existingRole.allowedMemberTypes = @('User')
                $changed = $true
            }

            $changes.Add([pscustomobject]@{
                Action = if ($changed) { 'Update' } else { 'Keep' }
                Value  = $definition.Value
                Id     = $existingRole.id
            })
        }
        else {
            $newRole = [ordered]@{
                allowedMemberTypes = @('User')
                description        = $definition.Description
                displayName        = $definition.DisplayName
                id                 = (New-Guid).Guid
                isEnabled          = $true
                value              = $definition.Value
            }

            $merged.Add($newRole)
            $changes.Add([pscustomobject]@{
                Action = 'Create'
                Value  = $definition.Value
                Id     = $newRole.id
            })
        }
    }

    [pscustomobject]@{
        Roles   = @($merged)
        Changes = @($changes)
    }
}

function Save-AppRoleBackup {
    param(
        [Parameter(Mandatory = $true)]
        $ServicePrincipal,

        [Parameter(Mandatory = $true)]
        [string]$Directory
    )

    if (-not (Test-Path -LiteralPath $Directory)) {
        New-Item -ItemType Directory -Path $Directory -Force | Out-Null
    }

    $timestamp = (Get-Date).ToUniversalTime().ToString('yyyyMMdd-HHmmss')
    $path = Join-Path $Directory "cluedin-appRoles-$timestamp.json"

    $backup = [ordered]@{
        capturedUtc               = (Get-Date).ToUniversalTime().ToString('o')
        servicePrincipalId        = [string]$ServicePrincipal.id
        servicePrincipalAppId     = [string]$ServicePrincipal.appId
        servicePrincipalName      = [string]$ServicePrincipal.displayName
        appRoleAssignmentRequired = [bool]$ServicePrincipal.appRoleAssignmentRequired
        appRoles                  = @($ServicePrincipal.appRoles)
    }

    $backup |
        ConvertTo-Json -Depth 20 |
        Set-Content -LiteralPath $path -Encoding utf8

    return (Resolve-Path -LiteralPath $path).Path
}

function Get-AllGraphCollectionItems {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Uri
    )

    $items = [System.Collections.Generic.List[object]]::new()
    $next = $Uri

    while ($next) {
        $response = Invoke-MgGraphRequest -Method GET -Uri $next -OutputType PSObject

        foreach ($item in @($response.value)) {
            $items.Add($item)
        }

        $nextProperty = $response.PSObject.Properties['@odata.nextLink']
        if ($nextProperty) {
            $next = [string]$nextProperty.Value
        }
        else {
            $next = $null
        }
    }

    return @($items)
}

function Add-CluedInGroupRoleAssignments {
    param(
        [Parameter(Mandatory = $true)]
        $ServicePrincipal,

        [Parameter(Mandatory = $true)]
        [string]$CsvPath
    )

    if (-not (Test-Path -LiteralPath $CsvPath)) {
        throw "Group-role mapping CSV '$CsvPath' does not exist."
    }

    $rows = @(Import-Csv -LiteralPath $CsvPath)
    if ($rows.Count -eq 0) {
        Write-Host 'The group-role mapping CSV is empty. No assignments to create.'
        return
    }

    $roleByValue = @{}
    foreach ($role in @($ServicePrincipal.appRoles)) {
        if ($null -ne $role.value -and -not [string]::IsNullOrWhiteSpace([string]$role.value)) {
            $roleByValue[[string]$role.value] = $role
        }
    }

    $assignmentUri = "https://graph.microsoft.com/v1.0/servicePrincipals/$($ServicePrincipal.id)/appRoleAssignedTo?`$select=id,principalId,principalDisplayName,principalType,appRoleId"
    $existingAssignments = @(Get-AllGraphCollectionItems -Uri $assignmentUri)

    foreach ($row in $rows) {
        if (-not $row.GroupObjectId -or -not $row.RoleValue) {
            throw 'Each CSV row must contain GroupObjectId and RoleValue.'
        }

        $groupId = [Guid]$row.GroupObjectId
        $roleValue = [string]$row.RoleValue

        if (-not $roleByValue.ContainsKey($roleValue)) {
            throw "Role value '$roleValue' does not exist on the CluedIn service principal."
        }

        $role = $roleByValue[$roleValue]

        $groupUri = "https://graph.microsoft.com/v1.0/groups/$($groupId.Guid)?`$select=id,displayName"
        $group = Invoke-MgGraphRequest -Method GET -Uri $groupUri -OutputType PSObject

        $alreadyAssigned = @(
            $existingAssignments | Where-Object {
                ([string]$_.principalId -eq [string]$group.id) -and
                ([string]$_.appRoleId -eq [string]$role.id)
            }
        ).Count -gt 0

        if ($alreadyAssigned) {
            Write-Host "Already assigned: '$($group.displayName)' -> '$roleValue'"
            continue
        }

        $body = @{
            principalId = [string]$group.id
            resourceId  = [string]$ServicePrincipal.id
            appRoleId   = [string]$role.id
        } | ConvertTo-Json

        Invoke-MgGraphRequest `
            -Method POST `
            -Uri "https://graph.microsoft.com/v1.0/servicePrincipals/$($ServicePrincipal.id)/appRoleAssignedTo" `
            -Body $body `
            -ContentType 'application/json' | Out-Null

        Write-Host "Assigned: '$($group.displayName)' -> '$roleValue'"
    }
}

# ----- Main -----

Assert-MicrosoftGraphAuthenticationModule

Connect-CluedInGraph `
    -Tenant $TenantId `
    -DeviceCode:$UseDeviceCode `
    -EnableGroupAssignments:([bool]$GroupRoleMappingCsv)

$servicePrincipal = Get-ServicePrincipalWithAppRoles -ObjectId $ServicePrincipalObjectId

Write-Host "Service principal : $($servicePrincipal.displayName)"
Write-Host "Object ID         : $($servicePrincipal.id)"
Write-Host "Application ID    : $($servicePrincipal.appId)"

$backupPath = Save-AppRoleBackup `
    -ServicePrincipal $servicePrincipal `
    -Directory $BackupDirectory

Write-Host "Backup            : $backupPath"

$definitions = Get-CluedInRoleDefinitions
$mergeResult = Merge-CluedInAppRoles `
    -ExistingRoles @($servicePrincipal.appRoles) `
    -Definitions $definitions

$mergeResult.Changes |
    Sort-Object Action, Value |
    Format-Table Action, Value, Id -AutoSize

$patchBody = @{
    appRoles = @($mergeResult.Roles)
} | ConvertTo-Json -Depth 20

if ($ExportPatchPath) {
    $patchBody | Set-Content -LiteralPath $ExportPatchPath -Encoding utf8
    Write-Host "PATCH body exported: $ExportPatchPath"
}

$patchUri = "https://graph.microsoft.com/v1.0/servicePrincipals/$($ServicePrincipalObjectId.Guid)"

if ($PSCmdlet.ShouldProcess(
        "$($servicePrincipal.displayName) [$($servicePrincipal.id)]",
        'Replace appRoles with the preserved and merged role collection')) {

    Invoke-MgGraphRequest `
        -Method PATCH `
        -Uri $patchUri `
        -Body $patchBody `
        -ContentType 'application/json' | Out-Null

    $updated = Get-ServicePrincipalWithAppRoles -ObjectId $ServicePrincipalObjectId

    $missing = @(
        $definitions | Where-Object {
            $definition = $_
            -not (@($updated.appRoles) | Where-Object {
                $null -ne $_.value -and
                ([string]$_.value -ceq [string]$definition.Value)
            })
        }
    )

    if ($missing.Count -gt 0) {
        throw "Verification failed. Missing role values: $($missing.Value -join ', ')"
    }

    Write-Host 'Role verification succeeded.'

    @($updated.appRoles) |
        Where-Object { $null -ne $_.value } |
        Sort-Object value |
        Select-Object displayName, value, id, isEnabled |
        Format-Table -AutoSize

    if ($GroupRoleMappingCsv) {
        Add-CluedInGroupRoleAssignments `
            -ServicePrincipal $updated `
            -CsvPath $GroupRoleMappingCsv
    }
}
```

### Run the script safely

First use `-WhatIf`. This authenticates, reads the current Enterprise application, creates a backup, calculates the merged role collection, and shows the intended changes without sending the PATCH.

```powershell
.\Set-CluedInMtSaasAppRoles.ps1 `
    -TenantId '<CUSTOMER-TENANT-ID>' `
    -ServicePrincipalObjectId '<CLUEDIN-ENTERPRISE-APP-OBJECT-ID>' `
    -UseDeviceCode `
    -BackupDirectory '.\backup' `
    -ExportPatchPath '.\cluedin-appRoles-patch.json' `
    -WhatIf
```

Review the output and the exported JSON. Then run again without `-WhatIf`:

```powershell
.\Set-CluedInMtSaasAppRoles.ps1 `
    -TenantId '<CUSTOMER-TENANT-ID>' `
    -ServicePrincipalObjectId '<CLUEDIN-ENTERPRISE-APP-OBJECT-ID>' `
    -UseDeviceCode `
    -BackupDirectory '.\backup' `
    -ExportPatchPath '.\cluedin-appRoles-patch.json'
```

The `-UseDeviceCode` option is particularly useful when interactive authentication through Windows Web Account Manager (WAM) fails or cannot open a browser window.

For example, if `Connect-MgGraph` returns an error similar to:

```text
InteractiveBrowserCredential authentication failed: A window handle must be configured.
```

run the script with `-UseDeviceCode`.

## Optional: assign Microsoft Entra groups with the script

You can assign groups after the roles have been created. Create a CSV such as `cluedin-role-groups.csv`:

```csv
GroupObjectId,RoleValue
11111111-1111-1111-1111-111111111111,OrganizationAdmin
22222222-2222-2222-2222-222222222222,DataSteward
33333333-3333-3333-3333-333333333333,DataGovernance
```

Use the Microsoft Entra **Object ID** of each group.

Then run:

```powershell
.\Set-CluedInMtSaasAppRoles.ps1 `
    -TenantId '<CUSTOMER-TENANT-ID>' `
    -ServicePrincipalObjectId '<CLUEDIN-ENTERPRISE-APP-OBJECT-ID>' `
    -UseDeviceCode `
    -BackupDirectory '.\backup' `
    -GroupRoleMappingCsv '.\cluedin-role-groups.csv'
```

When group assignment is enabled, the script additionally requests:

- `AppRoleAssignment.ReadWrite.All`
- `Group.Read.All`

`Application.ReadWrite.All` is already requested for managing the service principal. Microsoft documents `AppRoleAssignment.ReadWrite.All` together with application read permissions for creating app-role assignments.

If you do not want the script to manage group assignments, omit `-GroupRoleMappingCsv` and assign users or groups through the Microsoft Entra admin center instead.

## Assign users or groups in Microsoft Entra admin center

After the roles exist on the Enterprise application:

1. Go to **Microsoft Entra admin center > Enterprise applications**.
2. Open the CluedIn Enterprise application.
3. Select **Users and groups**.
4. Select **Add user/group**.
5. Select the user or group.
6. Select the CluedIn role.
7. Select **Assign**.

Repeat this for the required role assignments.

### Optional: require explicit assignment

The Enterprise application has an **Assignment required?** setting. When enabled, users generally need to be explicitly assigned to the application before Microsoft Entra allows access.

{:.warning}
Do not enable **Assignment required?** until you have confirmed that all required administrators and user groups have assignments. Enabling it too early can prevent users from signing in.

## Enable Automatic Role Synchronization in CluedIn

For Microsoft Entra-managed roles to control CluedIn membership, **Automatic Role Synchronization** must be enabled for the organization.

After changing a role assignment in Microsoft Entra, the user should sign out of CluedIn and sign in again so that Microsoft Entra issues a new token containing the current `roles` claim.

## Verify the configuration

After configuring the roles and assignments:

1. Run the service-principal GET request again and verify that the required app roles are present.
2. In Microsoft Entra admin center, confirm the user or group assignment under **Enterprise applications > CluedIn > Users and groups**.
3. Confirm **Automatic Role Synchronization** is enabled in CluedIn.
4. Sign out of CluedIn completely and sign back in.
5. In CluedIn, verify that the expected role is assigned to the user.

If the Microsoft Entra assignment is correct but the CluedIn role is not updated, verify the exact app-role **Value** first. For example, use `OrganizationAdmin`, not `Organization Admin`.

## Roll back app-role changes

The PowerShell script saves the original service-principal state before changing it. To restore a backup, use the `appRoles` from the backup file, but remove the read-only `origin` property before PATCHing.

The following example converts a backup into a valid rollback body:

```powershell
$backup = Get-Content '.\backup\cluedin-appRoles-YYYYMMDD-HHMMSS.json' -Raw |
    ConvertFrom-Json

$roles = foreach ($role in @($backup.appRoles)) {
    [ordered]@{
        allowedMemberTypes = @($role.allowedMemberTypes)
        description        = $role.description
        displayName        = $role.displayName
        id                 = $role.id
        isEnabled          = $role.isEnabled
        value              = $role.value
    }
}

$body = @{ appRoles = @($roles) } | ConvertTo-Json -Depth 20

Invoke-MgGraphRequest `
    -Method PATCH `
    -Uri 'https://graph.microsoft.com/v1.0/servicePrincipals/<SERVICE-PRINCIPAL-OBJECT-ID>' `
    -Body $body `
    -ContentType 'application/json'
```

{:.warning}
Restoring an old app-role collection can remove roles created after the backup. Review the rollback JSON before applying it.

## Troubleshooting

### Graph Explorer Consent to permissions is empty

Verify that Graph Explorer is signed into the correct customer tenant. Then check the **Graph explorer** Enterprise application in Microsoft Entra and grant admin consent if required. If the list remains empty, use Microsoft Graph PowerShell with `-UseDeviceCode`.

### `Connect-MgGraph` reports a WAM window-handle error

Use device-code authentication:

```powershell
Connect-MgGraph `
    -TenantId '<CUSTOMER-TENANT-ID>' `
    -Scopes 'Application.ReadWrite.All' `
    -UseDeviceCode `
    -ContextScope Process `
    -NoWelcome
```

### Graph returns `403 Authorization_RequestDenied`

Check both parts of authorization:

- the signed-in administrator has a suitable Microsoft Entra directory role;
- the Graph access token contains the required delegated scope.

For Graph Explorer role management, use Privileged Role Administrator or Global Administrator. For the PowerShell role-creation script, verify `Application.ReadWrite.All` appears in:

```powershell
Get-MgContext | Format-List Account,TenantId,Scopes
```

### PATCH removes an existing role

The `appRoles` property is a collection. A PATCH that contains an incomplete collection can remove entries that were omitted. Restore the collection from a backup, then re-run the merge using the full existing collection.

### Graph rejects `origin`

Remove `origin` from the request body. Microsoft Graph returns it when reading app roles, but documents it as read-only and not valid in POST or PATCH requests.

### The role exists but CluedIn does not receive it

Check the following:

- the user or group is actually assigned to that role on the CluedIn Enterprise application;
- the role `value` matches the intended CluedIn role value;
- Automatic Role Synchronization is enabled;
- the user signed out and signed back in after the assignment changed.

## Microsoft references

- [Configure the role claim - Microsoft identity platform](https://learn.microsoft.com/en-us/entra/identity-platform/enterprise-app-role-management)
- [appRole resource type - Microsoft Graph](https://learn.microsoft.com/en-us/graph/api/resources/approle?view=graph-rest-1.0)
- [Update servicePrincipal - Microsoft Graph](https://learn.microsoft.com/en-us/graph/api/serviceprincipal-update?view=graph-rest-1.0)
- [Create an enterprise application from a multitenant application](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/create-service-principal-cross-tenant)
- [Work with Graph Explorer](https://learn.microsoft.com/en-us/graph/graph-explorer/graph-explorer-features)
- [Prerequisites to use PowerShell or Graph Explorer for Microsoft Entra roles](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/prerequisites)
- [Grant an appRoleAssignment for a service principal](https://learn.microsoft.com/en-us/graph/api/serviceprincipal-post-approleassignedto?view=graph-rest-1.0)
