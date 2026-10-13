---
title: Install CluedIn using PowerShell
url: https://documentation.cluedin.net/operate/azure/powershell
content_type: how-to
section: Deploy & operate > Azure deployment
---

# Install CluedIn using PowerShell

> how-to: Steps to accomplish one task.

---
### Introduction

This installation process is done through command lines using [PowerShell 7](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell?view=powershell-7), [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli), [Kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/#install-kubectl) and [Helm](https://helm.sh/).

The purpose of the chart is to install the CluedIn application. This includes the actual CluedIn server, website, and other [services required](../../getting-started) (storage, queues, etc.)

**Note**: Before proceeding with the installation, you must ensure that all [pre-requisites](https://documentation.cluedin.net/operate/azure/setup.md#pre-requisites--preparation) are met.

### Download the Installation script and run it

- Save this [Installation Script](https://documentation.cluedin.net/assets/ps1/run-full-install.ps1) to a folder of your choice on your computer. *In this example, the script is saved to* `C:\Users\$env:UserName`

- Open a PowerShell 7 session **as administrator** on your computer and run the following command, this will enable local scripts to run:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```
- Run the `run-full-install.ps1` script and let it guide you through the whole installation process

![Administrator PowerShell 7 window running Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass followed by .\run-full-install.ps1](https://documentation.cluedin.net/assets/images/deployment/step-by-step-install/70-run-full-install-script.png)

### Next Steps

After logging in to the platform, you can proceed with enabling single sign on for your users to access the platform, as well as start loading data in via Data Sources or installing some crawlers. 
Below you will find some useful links on achieving the above:
- [Enabling Single Sign On](https://documentation.cluedin.net/administration/authentication)
- [Restricting access to CluedIn Clean via Basic Authentication](https://documentation.cluedin.net/operate/security/basic-auth-cluedin-clean)
- [Install a crawler/custom component](https://documentation.cluedin.net/ingest/connectors/install-integrations.md)

Optionally, you can also adjust other settings to cater for more complex scenarios:
- [Persistence/Using Managed Disks](https://documentation.cluedin.net/operate/configuration/persistence.md)
- [Azure SQL Server](https://documentation.cluedin.net/operate/configuration/sql.md)
- [Scaling](https://documentation.cluedin.net/deployment/kubernetes/scaling)

Up: [Azure deployment](https://documentation.cluedin.net/operate/azure.md)
