---
category: Get Started
title: Securing components with OAuth2
hideMenu: true
---

With the default values of the chart, OAuth2 authentication will be enabled to access the clean feature (URL `https://<clean-segment>.<prefix>.<hostname>`) and the `Seq` log monitoring tool.

Internally it uses an Oauth2 proxy, which supports all the most common providers (Azure, Google, etc.). Read their [documentation](https://pusher.github.io/oauth2_proxy/auth-configuration) for further information.

The chart assumes the usage of Azure, however it is possible to use other providers:
1. Create a new Application registration in Azure AD.

1. Allow the following endpoints for redirection in the Azure AD application
    - `https://<clean-segment>.<prefix>.<hostname>/oauth2/callback`
    - `https://<app-segment>.<prefix>.<hostname>/oauth2/callback`
    (refer to the [DNS](/docs/0-gettingStarted/dns-hostnames.html) section).

1. Create a new _client secret_ (under Certificates and Secrets).

1. Create a secret with the keys 
    - `OAUTH2_PROXY_CLIENT_ID`: this is the _Application (client) ID_ from Azure AD
    - `OAUTH2_PROXY_CLIENT_SECRET`: A client secret generated in Azure AD
    - `OAUTH2_PROXY_COOKIE_SECRET`: A random string

1. Set the following in your `values.yml` file override.
    ```yaml
    oauth2:
        environment:
            OAUTH2_PROXY_EMAIL_DOMAIN: <email-domain-for-authentication>
        secretRefName: <name-of-secret-created above>
    ```

### Disabling OAuth2

You can disable it entirely by setting:
```yaml
oauth2:
    enabled: false
```

You can also disable it for individual components by only adding to the `for` key those elements you want to have OAuth2 enabled for:
```yaml
oauth2:
    for:
    - seq
    - openrefine
```