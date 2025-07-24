---
layout: cluedin
title: Restricting access to CluedIn Clean via SSO Authentication
permalink: kb/sso-auth-cluedin-clean
parent: Knowledge base
tags: ["security","cluedin-clean","authentication","kubernetes", "sso"]
last_modified: 2022-03-23
nav_order: 6
published: false
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

This article describes how to enable your selected SSO provider to restrict access to the CluedIn Clean page.

Please note that the setup of CluedIn on AKS is not in the scope of this article.

## Prerequisites

Before you start, make sure you have the following :

- A working instance of CluedIn on AKS
- Preferably Azure CLI and Kubectl on your local machine. Otherwise, you can also use Cloud Shell on Azure Portal. **The steps described below suppose you are using PowerShell locally.**

## Configure your SSO provider
You must register the appropriate redirect uris for your SSO provider.
When using Azure App registrations you can do this under the `Authentication` section:
![App Registration](../assets/images/kb/0006/app_registration.png)

> Provide the _full_ url of the address to be protected followed by `/oauth2/callback` e.g. https://clean.example.com/oauth2/callback

## Connect to the AKS cluster

Open PowerShell, then connect to your Azure tenant using the following command (replace values of variables were needed):
First, connect to Azure [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli):

{:.important}
For directions on how to get Azure Tenant Id, visit [How to find Azure AD tenant ID](https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-how-to-find-tenant).

```powershell
$tenant_id = 'replace with your tenant Id' # your tenant ID
az login --tenant $tenant_id # this line will open the Azure Login page in your browser
```

## Configuration of OAuth2

1. Generate a cookie secret based on a known password. E.g. Run the following in PowerShell
    ```PowerShell
    $myPassword = 'mySuperStrong(!)Password'
    [Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes($myPassword)).Replace("+","-").Replace("/","_")
    ```
1. Push the secret to the cluster using `kubectl`
    ```PowerShell
    $secretName = 'oauth2-proxy-config'
    $clientIdFromSsoProvider = '12345...'
    $clientSecretFromSsoProvider = '12345...'
    $cluedinNamespace = 'cluedin'
    kubectl create secret generic $secretName --from-literal=OAUTH2_PROXY_CLIENT_ID=$clientIdFromSsoProvider --from-literal=OAUTH2_PROXY_CLIENT_SECRET=$clientSecretFromSsoProvider --from-literal=OAUTH2_PROXY_COOKIE_SECRET=$myPassword -n $cluedinNamespace
    ```

## Apply values for Helm chart

Prior to CluedIn 3.3.0 all versions of CluedIn were installed using the helm chart `cluedin/cluedin`.

From 3.3.0 a new chart `cluedin/cluedin-platform` is used to support improved flexiblity and control of an install.

### Using chart `cluedin/cluedin` (All CluedIn releases until 3.2.5)
1. In the `values.yaml` for your deployment, configure the `oauth2` section
    ```yaml
    oauth2:
        enabled: true
          for:
          - clean # Include the clean service and any others you want to configure
          - seq
          - openrefine
          - grafana-admin
          - prometheus-admin
        environment:
            OAUTH2_PROXY_EMAIL_DOMAIN: example.com # Match to your SSO provider domain
        secretRefName: oauth2-proxy-config # Match to the secret name in step 2
    ```
1. Apply the changes using `helm`
    ```PowerShell
    # For new installs
    helm install -f values.yaml cluedin cluedin/cluedin

    # To upgrade an existing install
    helm upgrade -f values.yaml cluedin cluedin/cluedin
    ```

### Using chart `cluedin/cluedin-platform` (All CluedIn releases 3.3.0 and up)
1. In the `values.yaml` for your deployment, configure the `oauth2` section
    ```yaml
    application:
        oauth2:
            enabled: true
            for:
            - clean # Include the clean service and any others you want to configure
            - seq
            - openrefine
            - grafana-admin
            - prometheus-admin
            extraConfiguration:
                OAUTH2_PROXY_EMAIL_DOMAIN: example.com # Match to your SSO provider domain
            secretRefName: oauth2-proxy-config # Match to the secret name in step 2
    ```
1. Apply the changes using `helm`
    ```PowerShell
    # For new installs
    helm install -f values.yaml cluedin cluedin/cluedin-platform

    # To upgrade an existing install
    helm upgrade -f values.yaml cluedin cluedin/cluedin-platform
    ```

For additional configuration options, see: https://oauth2-proxy.github.io/oauth2-proxy/docs/configuration/overview/
