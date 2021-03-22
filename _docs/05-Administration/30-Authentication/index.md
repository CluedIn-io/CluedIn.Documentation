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

* API Permissions:
  * Microsoft Graph
  * Email
  * Offline_access
  * Openid
  * Profile
  * User.Read
 
* Implicit Grant:
  * id_token

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

( Fill out values in the diamond operators )
```
INSERT [SingleSignOn] ([Id],[OrganizationId],[LoginUrl],[LogoutUrl],[Active],[ChangePasswordUrl],[SingleSignOnProviderId],[ExternalId],[IssuerUrl],[SamlVersion],[Certificate],[CustomErrorUrl],[ExternalSecret],[AuthenticationScheme],[AuthorityUrl])

SELECT '{a421253e-9086-4202-bfcc-c42eed712987}','<organization id>','<org account url>/ssocallback','<org account url>/logout',1,' ','{54118954-951f-41a9-b0a7-6de7d47e6c17}','<client id>',' ',0,' ',' ','<client secret>','aad','https://login.microsoftonline.com/common';
```

Add `54118954-951f-41a9-b0a7-6de7d47e6c17` as OrganizationProfile -> SingleSignOnProvider value for your Organization account.

Restart CluedIn API Pod
```
kubectl delete pod -l role=main
```

### NGINX Bad Request
If you are running NGINX as your Ingress Controller and upon redirect you have a 502 Bad Request, you are missing the following annotations to your Ingress definition:

```
    nginx.ingress.kubernetes.io/proxy-buffering: "on"
    nginx.ingress.kubernetes.io/proxy-buffer-size: "128k"
    nginx.ingress.kubernetes.io/proxy-buffers-number: "4"
```