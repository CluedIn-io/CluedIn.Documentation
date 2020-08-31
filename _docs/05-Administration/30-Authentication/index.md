# TODO
* Hide this for v3.0

---
category: Administration
title: Authentication
--- 

## Single Sign On / LDAP Provider

CluedIn supports Open Id for Single Sign On and hence we support all providers listed here: https://openid.net/developers/certified/

You can choose your provider from the _Administration_ menu and then click on _Authentication_. After this, choose the _Change Authentication Type_ button and choose the provider you would like to use. 
![Screenshot](ChangeAuthenticationType.png)

Follow the instructions listed in the user interface to insert the configuration necessary to enable the Single Sign On provider of your choice. 

## Enable Email Domain

From this screen you can also enable the _Use Domain Sign Up_ feature. This is useful if you are not using the LDAP provider support of CluedIn and if you would like anyone in your organisation to sign up and access your CluedIn account.

## Setting up Azure Active Directory

If you want to use Azure Active Directory, just select it from the list.

![Screenshot](AzureAD.png)

You will be prompted to fill in 4 values that you can get from your Azure Portal. Click Save, once you have entered the data and click "Sign Out" in the top right hand corner. On the CluedIn login page, it will now automatically redirect to your Single Sign On provider to authorize and login with your Azure Active Directory credentials. 

# Open ID Connect Single Sign On

This document explains how to use `OpenID Connect` and `OAuth` as an external authentication provider for the application.

Some terminology:

> OpenID Connect (OIDC) is an authentication protocol, based on the OAuth 2.0 family of specifications. It uses simple JSON Web Tokens (JWT), which you can obtain using flows conforming to the OAuth 2.0 specifications.

## Background

### Authorization Code Flow

The steps involved in the [Authorization Code Flow](https://auth0.com/docs/flows/concepts/auth-code) are set out below:

1. The user clicks Login within the CluedIn web application.

1. Web application redirects the user to the OAuth Authorization Server.

1. The Authorization Server redirects the user to the login and authorization prompt.

1. The user authenticates using one of the configured login options and may see a consent page listing the permissions the authorization request will give to the CluedIn web application.

1. The Authorization Server redirects the user back to the application with an authorization code.
1. The authorization code is sent back to the Authorization Server along with the application's Client ID and Client Secret.

1. The Authorization Server verifies the code, Client ID, and Client Secret.

1. The Authorization Server responds with an ID Token and Access Token (and optionally, a Refresh Token).

1. The CluedIn application can use the Access Token to call the CluedIn APIs and to access information about the user.

1. The API responds with requested data.

See https://cdn2.auth0.com/docs/media/articles/flows/concepts/auth-sequence-auth-code.png

The steps performed by the CluedIn application to authenticate a User with Single Sign On are defined in this PlantUML Sequence diagram which shows the [Single Sign On Flow](../SSO-flow.plantuml).

## Getting started using Open ID Connect with the CluedIn application

There are three steps to be performed in order to user Open ID Connect for Single Sign On to the CluedIn application:

1. Registering CluedIn as an OpenID client application in your Identity Provider (IDP)
1. Add IDP configuration to the CluedIn deployment
1. Change the Authentication Provider in the CluedIn application

These steps are covered in the following sections.

### Registering CluedIn as an OpenID Client Application

In order to use an Identity Provider (IDP) as an external authentication provider you will need to create a registration for the CluedIn application.

In the IDP developer / administration portal you will need to create a registration entry, as follows:

* Create a new OAuth 2.0 client registration

  * Note the `client id` and generate a `client secret` for this application

  * You will be asked to specify a `redirect uri`

    This should be in the form of `https://<yourdomain>:<port>/sso/oidc/callback`

    For example `https://localhost:9001/sso/oidc/callback` would be used for local development.

### Add IDP configuration to the CluedIn Deployment

* Set the _OpenID Connect_ Provider configuration settings

  The Identity Provider Authorization and Token urls use the following `AppSettings` section within [container.config](../../../Code/Server.ConsoleHostV2/ServerComponent/container.config).

  * `SingleSignOn.OAuth.auth_uri`
  * `SingleSignOn.OAuth.token_uri`

  The [Authorization Code Flow](https://auth0.com/docs/flows/concepts/auth-code) for the Server exchanging an Authorization Code for a token. The configuration settings that support the Authorization Code Flow are:

  * `SingleSignOn.OAuth.client_id`
  * `SingleSignOn.OAuth.client_secret`

* Review and update, if needed, the _Security_ configuration settings

  * `Security.Token.AccessTokenExpireIn`

    To specify a __1 day__ expiry time for Access Tokens use the following configuration settings:

    ```Xml
    <add key="Security.Token.AccessTokenExpireIn" value="1.00:00:00" />
    ```

  * User Role mapping from configuration

    Roles returned from the IDP in tokens are mapped to built-in CluedIn Role types using configuration.

    The default configuration for this Role mapping is shown below:

    ```Xml
    <add key="Security.Roles.Mapping.User" value=".*User" />

    <add key="Security.Roles.Mapping.OrganizationAdmin" value=".*Organization.*Admin" />

    <add key="Security.Roles.Mapping.ReportManager" value=".*ReportManager" />
    ```

    The configuration key starts with the prefix `Security.Roles.Mapping.` followed by the CluedIn Role name. The supported CluedIn roles are `User`, `OrganizationAdmin` and `ReportManager`, these roles are defined in the `CluedIn.Core.Accounts.UserRoleType` enumeration.

    The value specified by the Role mapping setting is a regular expression to match incoming Role names against.

    Note: If the application finds Roles originating from the IDP that do not have a configuration mapping a warning will be issued to the application logs and the incoming Role will be ignored.

* Review and update, if needed, the _provider_id_ configuration settings

  * `SingleSignOn.provider_id`

     The external authentication provider identifier.

     To use OpenID Connect as an external authentication provider use the following configuration settings:

    ```Xml
    <add key="SingleSignOn.provider_id" value="b4297a43-6e13-46a1-84bd-580fa39d8b44" />
    ```

### Change the Authentication Provider in the CluedIn Application

To change the Authentication Provider in the application login as an Administrator and perform the steps outlined below.

The _idp_ value is used to set the OAuth2 paths for the Identity Provider (IDP) that your instance will use.

1. Client Application -> Administration -> Change Authentication Provider

   * `Provider Name` : OpenID Connect
   * `External Id` : b4297a43-6e13-46a1-84bd-580fa39d8b44
   * `Login Url` : <https://idp/oauth2/authorize>
   * `Logout Url` : <https://idp/oauth2/v2.0/logout>
   * `Change Password Url` : <https://idp/>

   Note: `Issuer Url` parameter in the UI is not required when changing the Authentication Provider to _OpenID Connect_.

1. Save and accept Authentication Provider change

1. Sign out User

1. Login using Single Sign On Authority

1. Browser redirected back to authenticated session in CluedIn Application

You have now enabled external authentication as the sole method of authenticating users of the CluedIn application.

#### Future Changes

The selection of Authentication Provider will become a deployment concern. The UI around this will be simplified and the selection of presenting a User credentials login page or a redirect to an IDP login page will be made by configuration.

The configuration settings that will control the enabling or disabling of external authentication providers is as follows:

```Xml
<add key="FeatureExternalAuthentication" value="true" />
```

Set the configuration flag to `true` to enable external authentication. Set it to `false` to disable external authentication and use local User credentials for authenticating with the CluedIn application.

### Sample OAuth Configurations for Identity Providers

* [CluedIn ApS Azure Active Directory](./samples/cluedin.md)

* [Google](./samples/google.md)

* [Local Active Directory Federation Services (ADFS)](./samples/adfs.md)

## References

* [OpenID Connect Protocol](https://auth0.com/docs/protocols/oidc)

* The Microsoft [OAuth 2.0 authorization flow](https://docs.microsoft.com/en-us/azure/active-directory/develop/v1-protocols-oauth-code#oauth-20-authorization-flow) documentation


