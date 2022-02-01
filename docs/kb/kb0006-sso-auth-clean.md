---
layout: default
title: Restricting access to CluedIn Clean via SSO Authentication
permalink: /kb/sso-auth-cluedin-clean
nav_exclude: true
tags: ["security","cluedin-clean","authentication","kubernetes", "sso"]
last_modified: 2022-02-01
---

# SSO Authentication for Clean

When using CluedIn with an SSO provider, you can configure the CluedIn Clean address `clean.*` to utilise the same SSO provider
that use to authenticate with the CluedIn platform.

## Configuration of OAuth2

1. Generate a cookie secret based on a known password. E.g. Run the following in PowerShell
    ```PowerShell
    $myPassword = 'mySuperStrong(!)Password'
    [Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes($myPassword)).Replace("+","-").Replace("/","_")
    ```
1. Prior to deployment of CluedIn, create a new secret using `kubectl`
    ```PowerShell
    $secretName = 'oauth2-proxy-config'
    $clientIdFromSsoProvider = '12345...'
    $clientSecretFromSsoProvider = '12345...'
    $cookieSecretFromStep1 = '12345...'
    $cluedinNamespace = 'cluedin'
    kubectl create secret generic $secretName --from-literal=OAUTH2_PROXY_CLIENT_ID=$clientIdFromSsoProvider --from-literal=OAUTH2_PROXY_CLIENT_SECRET=$clientSecretFromSsoProvider --from-literal=OAUTH2_PROXY_COOKIE_SECRET=$cookieSecretFromStep1 -n $cluedinNamespace
    ```
1. In the `values.yaml` for your deployment, configure the `oauth2` section
    ```yaml
    oauth2:
    enabled: true
    environment:
        OAUTH2_PROXY_EMAIL_DOMAIN: example.com # Match to your SSO provider domain
    secretRefName: oauth2-proxy-config # Match to the secret name in step 2
    ```

For additonal configuration options, see: https://oauth2-proxy.github.io/oauth2-proxy/docs/configuration/overview/