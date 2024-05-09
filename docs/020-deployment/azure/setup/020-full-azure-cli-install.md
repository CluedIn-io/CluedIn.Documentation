---
layout: cluedin
nav_order: 20
parent: CluedIn Setup
grand_parent: Azure
permalink: /deployment/azure/setup/powershell
title: "Install CluedIn using PowerShell"
tags: ["deployment", "cluedin", "installation", "setup", "cli", "powershell"]
# last_modified: 2021-12-07
headerIcon: "paas"
---

{: .no_toc }
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

---
### Introduction

This installation process is done through command lines using [PowerShell 7](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell?view=powershell-7), [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli), [Kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/#install-kubectl) and [Helm](https://helm.sh/).

The purpose of the chart is to install the CluedIn application. This includes the actual CluedIn server, website, and other [services required](../../getting-started) (storage, queues, etc.)

**Note**: Before proceeding with the installation, you must ensure that all [pre-requisites](../setup#pre-requisites--preparation) are met.

### Download the Installation script and run it

- Save this <a href="../../../assets/ps1/run-full-install.ps1" download>Installation Script</a> to a folder of your choice on your computer. *In this example, the script is saved to* `C:\Users\$env:UserName`

- Open a PowerShell 7 session **as administrator** on your computer and run the following command, this will enable local scripts to run:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```
- Run the `run-full-install.ps1` script and let it guide you through the whole installation process

![PowerShell](../../../assets/images/deployment/step-by-step-install/70-run-full-install-script.png)

### Next Steps

After logging in to the platform, you can proceed with enabling single sign on for your users to access the platform, as well as start loading data in via Data Sources or installing some crawlers. 
Below you will find some useful links on achieving the above:
- [Enabling Single Sign On](/administration/authentication)
- [Restricting access to CluedIn Clean via Basic Authentication](../../../kb/basic-auth-cluedin-clean)
- [Install a crawler/custom component](/integration/install-integrations)

Optionally, you can also adjust other settings to cater for more complex scenarios:
- [Persistence/Using Managed Disks](/paas-operations/configuration/pvc)
- [Azure SQL Server](/deployment/kubernetes/sql)
- [Scaling](/deployment/kubernetes/scaling)
