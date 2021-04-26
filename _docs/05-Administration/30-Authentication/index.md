---
category: Administration
title: Authentication
--- 

## Single Sign On with Azure AD

## App Registration
* Redirect URIs:
  * https://app._hostname_/
  * https://_accountSubdomain_._hostname_/
  * https://app._hostname_/auth/signin-oidc

*Logout Uri
  *<org account url>/logout


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

After doing this, visit the login page for your CluedIn account again and you will notice that it will redirect you to the office 365 login page to authenticate. By default, your user will be created as a "User" and not an Administrator. You cna now manage this all within your Active Directory now.

### NGINX Bad Request
If you are running NGINX as your Ingress Controller and upon redirect you have a 502 Bad Request, you are missing the following annotations to your Ingress definition:

```
    nginx.ingress.kubernetes.io/proxy-buffering: "on"
    nginx.ingress.kubernetes.io/proxy-buffer-size: "128k"
    nginx.ingress.kubernetes.io/proxy-buffers-number: "4"
```