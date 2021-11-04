---
layout: default
nav_order: 3
parent: Administration
permalink: /administration/authentication
title: Authentication
tags: ["administration", "authentication", "sso", "single-sign-on"]
last_modified: 2021-10-18
---

## Default Authentication Provider

By default CluedIn uses Microsoft Identity Server as its authentication provider. These means that users and roles are managed within the CluedIn application itself. It is recommended to enable SSO in staging and production environments, but for locally development, it is fine to use this authentication mechanism. 

CluedIn will also expire the authentication after 15 minutes of inactivity within the CluedIn user interface. 

## Single Sign On with Azure AD

**note:** you will need to respect the restrictions and limitations of the [Redirect URI](https://docs.microsoft.com/en-us/azure/active-directory/develop/reply-url)

**note:** you MUST implement HTTPS for all CluedIn URIs before setting up SSO.

## App Registration
* Redirect URIs:
  * https://app._hostname_/
  * https://_organization_._hostname_/
  * https://app._hostname_/auth/signin-oidc

* Logout Uri
  * <org account url>/logout


* API Permissions:
  * Microsoft Graph
    * Email
    * Offline_access
    * Openid
    * Profile
    * User.Read
 
* Implicit Grant:
  * id_token (This is a checkbox)

* Expose an API:
  * Scopes
    * Scope: https://www.cluedin.net/sso/user_impersonation
  * Who can consent: Admins and Users
    * Authorized client applications
  * Authorized Scopes
    * https://www.cluedin.net/sso/user_impersonation (scope created in the step above)
 
* Details required to enable SSO:
  * Application (client) ID
  * Client Secret

## Enabling SSO
The following SQL query will have to be executed against Authentication database:

This may require you to port-forward to the SQL instance running inside the kubernetes cluster using [kubectl port-forward](https://kubernetes.io/docs/tasks/access-application-cluster/port-forward-access-application-cluster/). 

Navigate to the Database called Authentication, and either run this command from a command line or using your SQL Management Client such as SQL Server Management studio.

( Fill out all values in the diamond operators in the command below)
```
INSERT [SingleSignOn] ([Id],[OrganizationId],[LoginUrl],[LogoutUrl],[Active],[ChangePasswordUrl],[SingleSignOnProviderId],[ExternalId],[IssuerUrl],[SamlVersion],[Certificate],[CustomErrorUrl],[ExternalSecret],[AuthenticationScheme],[AuthorityUrl])

SELECT '{a421253e-9086-4202-bfcc-c42eed712987}','<organization id>','<organization url>/ssocallback','<organization url>/logout',1,' ','{54118954-951f-41a9-b0a7-6de7d47e6c17}','<client id>',' ',0,' ',' ','<client secret>','aad','https://login.microsoftonline.com/common';
```

You will now need to update the OrganizationAccount tables ExternalAuthenticationId column for this organization you have created to be  `54118954-951f-41a9-b0a7-6de7d47e6c17`. This will signal to CluedIn that this particular account uses Azure Active Directory as its identity provider.

Restart CluedIn API Pod
```
kubectl delete pod -l role=main
```

*Dependent upon the version of kubectl you are using you may need to also append the namespace in the command above.

```
kubectl delete pod -l role=main -n cluedin
```

After doing this, visit the login page for your CluedIn account again and you will notice that it will redirect you to the office 365 login page to authenticate. By default, your user will be created as a "User" and not an Administrator. You can now manage this all within your Active Directory now.

### Azure AD Application Role to CluedIn Role

Once you have created your App Registration and attached that to your CluedIn instance, you have an option to create App Roles on AD side that would get translated into CluedIn Platform role and assigned to the user upon first sign in.

This can be achieved by going to your App Registration and navigating the left hand side menu to *"App Roles"*

//img 01

Once in App Roles section, you can begin creating roles that match your needs. *(You can find all CluedIn roles by navigating to [Administration -> Roles](//img) in the web user interface.)*

All the changes that are applied to App Registration will be live in your Azure subscription. We do not impose any hard requirements on how App Roles are setup, so adhere to your organization's internal requirements.

//img 02

Once App Role has been created, gain access to CluedIn's internal SQL _Authentication_ database and begin mapping CluedIn Roles to App Roles.

You can use the following SQL insert statement or populate the values manually by Editing the table:
```
USE [DataStore.Db.Authentication]

INSERT INTO [dbo].[SingleSignOnRoleMappings] (Id, SingleSignOnId, RoleId, MappedTo)

VALUES ('<single sign on id>', '<cluedin role id>', '<app role value field>')
```

The following values needs to be replaced:
* `<single sign on id>`  Corresponds to `Id` column in `SingleSignOn` table.
* `<cluedin role id>` Corresponds to `Id` column in `AspNetRoles` table.
* `<app role value field>` Corresponds to `Value` assigned in your App Role in App Registration.

See the example below of mapping `OrganizationAdmin` CluedIn role to `CluedIn App Admin` AD app role.

//img 03

### Azure AD User assignment to Azure AD App Role
### Cleaning up after you have switched to a SSO provider

After you have switched over to a Single Sign On provider you will still have your original user in the database. This user will not be able to login anymore so it is best to deactivate this user. To do this, you will also need to port-forward to the SQL database like above and switch the "Active column" on the AspNetUser table to false for this user. 

### NGINX Bad Request
If you are running NGINX as your Ingress Controller and upon redirect you have a 502 Bad Request, you are missing the following annotations to your Ingress definition:

```
    nginx.ingress.kubernetes.io/proxy-buffering: "on"
    nginx.ingress.kubernetes.io/proxy-buffer-size: "128k"
    nginx.ingress.kubernetes.io/proxy-buffers-number: "4"
```
