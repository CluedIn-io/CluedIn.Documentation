---
layout: default
nav_order: 1
parent: How tos
grand_parent: Deployment
permalink: /deployment/infra-how-tos/configure-sso
title: Configure SSO
tags: ["deployment", "ama", "marketplace", "azure"]
last_modified: 2023-06-20
---

In this article, you will learn how to configure single sign-on (SSO) for CluedIn using Azure Active Directory (AD) group-managed role membership.

# Overview of SSO for CluedIn

SSO is an authentication method that allows users to sign in to multiple independent software systems with a single set of credentials.

SSO for CluedIn can be enabled in one of the following modes:
- **SSO with local CluedIn role membership management** – all users from the directory can sign in to the CluedIn application. After the user signs in for the first time, CluedIn roles can be assigned in the usual way in the CluedIn UI.
- **SSO with Azure AD group-managed role membership** – Azure AD application roles are created within your Azure application registration and they can be mapped to your AD groups or users. This mode requires **Automatic Role Synchronization** to be enabled in the **Administration Settings** page in CluedIn.
![Automatic_role_synchronization.png](../../assets/images/ama/howtos/configure-sso-1.png)

Configuring SSO for CluedIn using Azure AD involves three main steps:

1. [Register an application in the Azure portal](https://dev.azure.com/CluedIn-io/CluedIn/_wiki/wikis/CluedIn.wiki/1211/Y-Configure-SSO?anchor=register-an-application-in-the-azure-portal)
1. [Create Kubernetes secret and enable SSO via Helm](https://dev.azure.com/CluedIn-io/CluedIn/_wiki/wikis/CluedIn.wiki/1211/Y-Configure-SSO?anchor=enable-sso-via-helm)
1. [(Optional) Create custom role mappings](https://dev.azure.com/CluedIn-io/CluedIn/_wiki/wikis/CluedIn.wiki/1211/Y-Configure-SSO?anchor=(optional)-create-custom-role-mapping)

**Important!** Before configuring SSO, make sure that you have configured [DNS](https://dev.azure.com/CluedIn-io/CluedIn/_wiki/wikis/CluedIn.wiki/1197/Configure-DNS) and [TLS](https://dev.azure.com/CluedIn-io/CluedIn/_wiki/wikis/CluedIn.wiki/1199/Configure-certificates).

# Register an application in the Azure portal

Registering your application establishes a trust relationship between your application and the Microsoft identity platform. The trust is unidirectional: your application trusts the Microsoft identity platform, and not the other way around. After you create the application, it cannot be moved between different tenants.

**To register an application in the Azure portal**

1. In the Azure portal, go to the tenant in which you want to register the application.
1. Search for and select **Azure Active Directory**.
1. Under **Manage**, select **App registrations** > **New registration**.
1. Enter a display **Name** for your application.
![Register_application_Name.png](../../assets/images/ama/howtos/configure-sso-2.png)
1. Select the account types that can use the application.
1. Select **Register**.
When the registration finishes, the Azure portal displays the **Overview** pane of the application registration. Here you can see the **Application (client) ID**. This value uniquely identifies your application. You'll need it for [enabling SSO via Helm](https://dev.azure.com/CluedIn-io/CluedIn/_wiki/wikis/CluedIn.wiki/1211/Y-Configure-SSO?anchor=enable-sso-via-helm).
![Register_application_Application_ID.png](../../assets/images/ama/howtos/configure-sso-3.png)

After you register the application, complete the the following steps:
1. [Create a client secret](https://dev.azure.com/CluedIn-io/CluedIn/_wiki/wikis/CluedIn.wiki/1211/SSO?anchor=create-a-client-secret)
1. [Add redirect URIs](https://dev.azure.com/CluedIn-io/CluedIn/_wiki/wikis/CluedIn.wiki/1211/SSO?anchor=add-redirect-uris)
1. [Add API permissions](https://dev.azure.com/CluedIn-io/CluedIn/_wiki/wikis/CluedIn.wiki/1211/SSO?anchor=add-api-permissions)
1. [Expose an API](https://dev.azure.com/CluedIn-io/CluedIn/_wiki/wikis/CluedIn.wiki/1211/SSO?anchor=expose-an-api)
1. [Map Azure AD application roles to CluedIn roles](https://dev.azure.com/CluedIn-io/CluedIn/_wiki/wikis/CluedIn.wiki/1211/SSO?anchor=map-azure-ad-application-roles-to-cluedin-roles)
 
## Create a client secret

A client secret is used to configure CluedIn to communicate with your Azure AD.

**To create the client secret**
1. In the Azure portal, in **App registrations**, select your application.
1. Select **Certificates & secrets** > **Client secrets** > **New client secret**.
1. Add a description for your client secret and an expiration date.
1. Select **Add**.
1. Copy and save **Value** and the **Secret ID** because they will be used later in your CluedIn Helm configuration.
![Create_client_secret_Value_ID.png](../../assets/images/ama/howtos/configure-sso-4.png)

For more information about the client secret, see [Microsoft documentation](https://learn.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app#add-a-client-secret).

## Add redirect URIs

Redirect URI is the location where the Microsoft identity platform redirects the user's client and sends security tokens after authentication.

**To add redirect URIs**

1. In the Azure portal, in **App registrations**, select your application.
1. Select **Authentication** > **Add a platform**.
1. In the right pane, select **Web**.
![Add_redirect_URIs_Configure_platforms.png](../../assets/images/ama/howtos/configure-sso-5.png)
1. In the **Configure Web** pane, specify the following:
   1. In **Redirect URIs**, add a redirect URI for your application (for example, https://app.yourdomain.com).
![Add_redirect_URIs_Redirect_URIs.png](../../assets/images/ama/howtos/configure-sso-6.png)
   1. In **Front channel logout URI**, add a logout URL for your application (for example, https://app.yourdomain.com/logout).
![Add_redirect_URIs_Logout_URL.png](../../assets/images/ama/howtos/configure-sso-7.png)
   1. In the **Implicit grant and hybrid flows** section, select the **ID tokens** checkbox, and then select **Configure**.
![Add_redirect_URIs_ID_tokens.png](../../assets/images/ama/howtos/configure-sso-8.png)
5. In the **Platform configurations** section, in **Web**, add additional URIs (for example, https://departmentX.yourdomain.com, https://app.yourdomain.com/auth/signin-oidc).
![Add_redirect_URIs_additional.png](../../assets/images/ama/howtos/configure-sso-9.png)
6. At the bottom of the page, select **Save**.

For more information about redirect URIs, see [Microsoft documentation](https://learn.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app#add-a-redirect-uri).

## Add API permissions for Microsoft Graph

When you register an application in the Azure portal, the Microsoft Graph API with the User.Read permission is added automatically. You need to add additional permissions for Microsoft Graph.

**To add API permissions for Microsoft Graph**

1. In the Azure portal, in **App registrations**, select your application.
2. Select **API permissions**.
3. In the **Configured permissions** section, select **Microsoft Graph**.
![Add_API_permissions_MS_Graph.png](../../assets/images/ama/howtos/configure-sso-10.png)
4. In the right pane, select the following permissions: **email**, **offline_access**, **openid**, and **profile**. At the bottom of the pane, select **Update permissions**.
The API permissions for Microsoft Graph are updated.
![Add_API_permissions_Updated.png](../../assets/images/ama/howtos/configure-sso-11.png)

For more information about API permissions, see [Microsoft documentation](https://learn.microsoft.com/en-us/azure/active-directory/develop/quickstart-configure-app-access-web-apis).

## Expose an API

You need to register a web API with the Microsoft identity platform and expose it to the client app by adding a scope. By registering your web API and exposing it through scope, you can provide permissions-based access to authorized users that access your API.

**To expose the API**

1. In the Azure portal, in **App registrations**, select your application.
2. Select **Expose an API**.
3. In the **Scopes defined by this API** section, select **Add a scope**.
4. Specify the following scope attributes:
- **Scope name** – https://www.cluedin.net/sso/user_impersonation
- **Who can consent** – Admins and Users
- **Authorized client applications** – https://www.cluedin.net/sso/user_impersonation
![authorized_client_applications.png](../../assets/images/ama/howtos/configure-sso-12.png)

For detailed instructions on how to configure an app to expose web API, see [Microsoft documentation](https://learn.microsoft.com/en-us/azure/active-directory/develop/quickstart-configure-app-expose-web-apis).
 
## Map Azure AD application roles to CluedIn roles

After you have created your application registration and attached it to your CluedIn instance, you can create the application roles on the Azure AD side. These roles will be translated into the CluedIn platform roles and assigned to the users after they sign in to the application for the first time.

**To map Azure AD application roles to CluedIn roles**

1. In the Azure portal, in **App registrations**, select your application.
1. Select **App roles**.
1. In the menu, select **Create app role**.
1. Enter the details of the role. See [CluedIn roles](https://dev.azure.com/CluedIn-io/CluedIn/_wiki/wikis/CluedIn.wiki/1211/SSO?anchor=cluedin-roles) for recommended values.
![Create_app_role.png](../../assets/images/ama/howtos/configure-sso-create-app-role-1.png)
1. Select **Apply** to save your changes. The role is added to the **App roles** list.
![App_role_added.png](../../assets/images/ama/howtos/configure-sso-create-app-role-2.png)
1. Repeat step 3-5 to add all roles.

In the CluedIn application, you can find all CluedIn roles by navigating to **Administration** -> **Roles**.

Any changes made in the application registration will live in your Azure subscription. We do not impose strict requirements on how app roles are set up, so you can follow your organization’s internal requirements.

## CluedIn roles 

The following is a list of the CluedIn application roles and recommended values to use when creating your Azure app roles with your application registration.

| Display name | Value | Description |
|--|--|--|
|Data Governance Administrator| DataGovernanceAdministrator |Role responsible for approving changes made by Data Governance users|
|Data Compliance | DataCompliance |Role responsible for daily operations around data compliance|
|Data Steward |DataSteward |Role dedicated to cleaning data using Clean and Prepare modules|
|Data Compliance Administrator |DataComplianceAdministrator |Role responsible for approving changes made by Data Compliance users|
|Admin |Admin | Administrator for the whole system, including multi-tenancy environment|
|Guest|	Guest| Guest User with minimal, read-only, permissions|
|User | User| User that can view all modules in a read-only manner, in a multi-tenancy environment|
|Data Architect | DataArchitect	| Role responsible for designing an Organizations enterprise data strategy|
|Deduplication Reviewer | DeduplicationReviewer |Role responsible for reviewing Deduplication Project results and approving the groupings|
|Organization User | OrganizationUser |User within an Organization that can view all modules in a read-only manner, in a multi-tenancy environment |
|Data Governance | DataGovernance | Role responsible for monitoring and maintaining data quality|
|Report Manager | ReportManager | User that can generate reports for compliance matters such as breach, subject request, and retention |
|Organization Admin | OrganizationAdmin | Administrator within an Organization in multi-tenancy environment |
|Deduplication | Administrator | DeduplicationAdministrator Role responsible for creating and maintaining Deduplication Projects and merging the results back into the system |
|Data Steward Administrator | DataStewardAdministrator | Role responsible for approving changes made by Data Stewards |
 
# Create Kubernetes secret and enable SSO via Helm

After you complete the Azure application registration and app roles configuration, you need to enable the SSO feature on the CluedIn platform to make SSO available to users when signing in to CluedIn.

**Prerequisites**

- You should be comfortable working in either PowerShell or bash terminal via Azure Cloud Shell.
- You should be connected to your AKS cluster.
See [Connect to CluedIn cluster](https://dev.azure.com/CluedIn-io/CluedIn/_wiki/wikis/CluedIn.wiki/1226/Connect-to-CluedIn-cluster) for detailed instructions.
- Your Helm repository is set up.
See [Helm](https://dev.azure.com/CluedIn-io/CluedIn/_wiki/wikis/CluedIn.wiki/1220/Helm) for detailed instructions on how to set up the repository.

If you have any questions, you can request CluedIn support by sending an email to support@cluedin.com (or reach out to your delivery manager if you have a committed deal).

<hr>

Once you have connected to your cluster and you are able to issue commands using kubectl and Helm, complete the following procedure to enable SSO for CluedIn.

**To create Kubernetes secret and enable SSO via Helm**

1. Create a new Kubernetes secret with your Azure app registration secret by running the following command: `kubectl create secret generic "myorg-sso-cs" -n cluedin --from-literal=clientSecret="1234-5678-9ABC"`
In the command, replace _1234-5678-9ABC_ with your Azure app registration secret.

2. In Azure Cloud Shell, run the following command to create a new empty file: `nano Cluedin-SSO-Config.yaml`

3. In the file, paste the following configuration:
```
apiVersion: api.cluedin.com/v1
kind: Feature
metadata:
  name: myorg-sso
spec:
  enableSso:
    clientId: "0cXXXX-XXXX-XXXX-XXX-XXXXXX575"
    organizationName: "myorg"
    clientSecretName: "myorg-sso-cs"
    clientSecretKey: "clientSecret"
```

4. Change the **name** and **organizationName** values to match your CluedIn organization/tenant name.

5. Change the **clientId** value to the client ID from you Azure app registration.

6. Save the file.

7. Apply your SSO configuration by running the following command in Azure Cloud Shell: `kubectl apply -n cluedin -f Cluedin-SSO-Config.yaml`

8. Verify that the SSO feature has been enabled successfully by running the following command in Azure Cloud Shell: `kubectl get features -n cluedin`

If your SSO feature has been successfully applied, you should see something similar to the screenshot below.

![SSO_enabled.png](../../assets/images/ama/howtos/configure-sso-success-terminal.png)

If the **Phase** is not in the **Active** state, wait 5 minutes and run the command again. If nothing changes, reach out to CluedIn support at support@cluedin.com for help in enabling your SSO.

# (Optional) Create custom role mapping

After the app roles have been created, gain access to CluedIn’s internal SQL Authentication database and begin mapping CluedIn roles to app roles.

**To create custom role mapping**

1. Gain access to the internal database using Kubernetes port forwarding capability. You need to complete this process on a PC/server where you have access to a SQL client application to query and execute SQL commands.

2. Use the following server address in your SQL client application: 127.0.0.1\mcr.microsoft.com/mssql/server,1433.
Alternatively, you can request CluedIn support by sending an email to support@cluedin.com or reach out to your delivery manager.

3. Use the following SQL insert statement (or populate the values manually by editing the table).
```
USE [DataStore.Db.Authentication]
INSERT INTO [dbo].[SingleSignOnRoleMappings] (Id, SingleSignOnId, RoleId, MappedTo)
VALUES ('<single sign on id>', '<cluedin role id>', '<app role value field>')
```
4. Replace the following values:
   - <single sign on id> – corresponds to the Id column in the SingleSignOn table.
   - <cluedin role id> – corresponds to the Id column in the AspNetRoles table.
   - <app role value field> – corresponds to the Value assigned in your app role in App Registration.

The following example shows the mapping of OrganizationAdmin CluedIn role to CluedIn App Admin AD app role.

![SSO_custom_roles.png](../../assets/images/ama/howtos/configure-sso-success-terminal-2.png)