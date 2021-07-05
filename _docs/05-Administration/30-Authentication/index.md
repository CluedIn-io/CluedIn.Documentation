---
category: Administration
title: Authentication
--- 

## Default Authentication Provider

By default CluedIn uses Microsoft Identity Server as its authentication provider. These means that users and roles are managed within the CluedIn application itself. It is recommended to enable SSO in staging and production environments, but for locally development, it is fine to use this authentication mechanism. 

CluedIn will also expire the authentication after 15 minutes of inactivity within the CluedIn user interface. 

## Single Sign On with Azure AD

## App Registration
* Redirect URIs:
  * https://app._hostname_/
  * https://_accountSubdomain_._hostname_/
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

SELECT '{a421253e-9086-4202-bfcc-c42eed712987}','<organization id>','<org account url>/ssocallback','<org account url>/logout',1,' ','{54118954-951f-41a9-b0a7-6de7d47e6c17}','<client id>',' ',0,' ',' ','<client secret>','aad','https://login.microsoftonline.com/common';
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

### Cleaning up after you have switched to a SSO provider

After you have switched over to a Single Sign On provider you will still have your original user in the database. This user will not be able to login anymore so it is best to deactivate this user. To do this, you will also need to port-forward to the SQL database like above and switch the "Active column" on the AspNetUser table to false for this user. 

### Mapping Active Directory Groups to Roles within CluedIn

If you have switched to an SSO provider then you will need to map Groups in Active Directory to Roles within CluedIn. This is done using configuration files within CluedIn. 

User Role mapping from configuration

Roles returned from the IDP in tokens are mapped to built-in CluedIn Role types using configuration.

The default configuration for this Role mapping is shown below:

<add key="Security.Roles.Mapping.User" value=".*User" />

<add key="Security.Roles.Mapping.OrganizationAdmin" value=".*Organization.*Admin" />

<add key="Security.Roles.Mapping.ReportManager" value=".*ReportManager" />

The configuration key starts with the prefix Security.Roles.Mapping. followed by the CluedIn Role name. The supported CluedIn roles are User, OrganizationAdmin and ReportManager, these roles are defined in the CluedIn.Core.Accounts.UserRoleType enumeration.

The value specified by the Role mapping setting is a regular expression to match incoming Role names against.

### Delegating access to CluedIn from Active Directory

Now that you have moved to using a SSO provider, then all access to users and groups is now done through Active Directory. Here is an example of a guide in Azure Active Directory that guides you through doing this against the Enterprise Application that you setup above. 

![Diagram](ChangeAuthenticationType.png)

### NGINX Bad Request
If you are running NGINX as your Ingress Controller and upon redirect you have a 502 Bad Request, you are missing the following annotations to your Ingress definition:

```
    nginx.ingress.kubernetes.io/proxy-buffering: "on"
    nginx.ingress.kubernetes.io/proxy-buffer-size: "128k"
    nginx.ingress.kubernetes.io/proxy-buffers-number: "4"
```
