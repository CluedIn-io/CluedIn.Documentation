---
layout: default
title: Restricting access to CluedIn Clean via Basic Authentication
permalink: /kb/basic-auth-cluedin-clean
nav_exclude: true
tags: ["security","cluedin-clean","authentication","kubernetes"]
last_modified: 2021-09-13
---

This article describes how to enable [HAProxy Basic Authentication](https://github.com/jcmoraisjr/haproxy-ingress/tree/master/examples/auth/basic) to restrict access to CluedIn Clean page.

Please note that the setup of CluedIn on AKS is not in the scope of this article.

<hr>

<h2 class="text-delta">Table of contents</h2>
1. TOC
{:toc}

## Prerequisites

Before you start, make sure you have the following :

- A working instance of CluedIn on AKS
- Preferably Azure CLI and Kubectl on your local machine. Otherwise, you can also use Cloud Shell on Azure Portal. **The steps described below suppose you are using PowerShell locally.**

## Create a text file with credentials

Create a text file on your machine, name it **auth** (with no extension), and put the credentials you want to use for the Clean page. The format should be **username::password** 

You can add multiple users if you wish. The following sample contains two users:

```text
cln_user1::JAehdjyaeg0KAxJZDGJ
cln_user2::zefgyizjehgfaje8U6T
```

## Connect to the AKS cluster

Open PowerShell, then connect to your Azure tenant using the following command (replace values of variables were needed):
First, connect to Azure [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli):

**Note:** For directions on how to get Azure Tenant Id, visit [How to find Azure AD tenant ID](https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-how-to-find-tenant).
```powershell
$tenant_id = 'replace with your tenant Id' # your tenant ID
az login --tenant $tenant_id # this line will open the Azure Login page in your browser
```

## Create a secret in AKS

In PowerShell, run the following command:

**Note:** If you use a specific namespace for the CluedIn cluster, you need to add it to the command. In the following example, we use **cluedin**. If you are in the default namespace, you don't need to add the **-n $namesapce** to the command.

```powershell
$secret_name = 'cluedin-clean-credentials' # a name of your choice for the secret
$auth_file_path = 'C:\Users\MyUser\AzureResources\auth' # Local path of the auth file created in Step 1
$namespace = 'cluedin' # Namespace of the CluedIn install
kubectl create secret generic $secret_name --from-file $auth_file_path -n $namespace
```

## Add Ingress annotations

Run the following command to add required annotations to the Clean Ingress controller:

```powershell
$secret_name = 'cluedin-clean-credentials' # secret name created in Step 3
$ingress_name = 'cluedin-clean' # Name of the Clean ingress
$namespace = 'cluedin' # name of the 
kubectl annotate $ingress_name \
        ingress.kubernetes.io/auth-type=basic \
        ingress.kubernetes.io/auth-secret=$secret_name -n $namesepace
```

## Restart Clean Deployment

Run the following command to restart the Clean deployment:

```powershell
$deployment_name = 'clean-cluedin' # name of the Clean deployment
    kubectl scale deployment $deployment_name --replicas=0
    kubectl scale deployment $deployment_name --replicas=1
```
