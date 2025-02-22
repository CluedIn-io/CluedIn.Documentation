---
layout: cluedin
title: Sync configuration between environments
parent: PaaS operations
permalink: /kb/config-migrate
tags: ["configuration", "migration"]
nav_order: 9
headerIcon: "paas"
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

This document covers the process for migrating CluedIn configuration from one environment to another environment. This is especially useful when you are developing your foundation on one environment and want to promote it to production.

**Prerequisites**

- [PowerShell Core / 7+](https://github.com/PowerShell/PowerShell).
- PowerShell `CluedIn product toolkit` module, which you can download it in the following section.
- Service account to do the export and import (the script is provided in above toolkit).
- Access to the front end, whether it's public facing or private facing.
- The user running the script must have full admin permissions with **Accountable** access level for every claim in CluedIn.

{:.important}
PowerShell Core does not work with PowerShell ISE. To replicate the ISE experience, please use Visual Studio Code.

## CluedIn product toolkit

Please find the latest releases on our [GitHub repository](https://github.com/CluedIn-io/CluedIn.Product.Toolkit/releases)

All future versions will be published on the [CluedIn.Product.Toolkit](https://github.com/CluedIn-io/CluedIn.Product.Toolkit) repository. Make sure that you retrieve the version that relates to the version of CluedIn that you are running.

| Version | Technical Version | Source Code  | Link |
| -- | -- | -- |
| 2024.12.00 | 4.4.0 | [Source Code](https://github.com/CluedIn-io/CluedIn.Product.Toolkit/tree/release/4.4.0) | <a href="/assets/other/CluedIn.Product.Toolkit_4.4.0.zip" download>Download</a> |
| 2024.07 | 4.3.0 | [Source Code](https://github.com/CluedIn-io/CluedIn.Product.Toolkit/tree/release/4.3.0) | <a href="/assets/other/CluedIn.Product.Toolkit_0.9.35.zip" download>Download</a> |

The product toolkit supports a number of methods of transferring configuration from one environment to another. The main two methods are running locally on your desktop or using a pipeline platform such as Azure DevOps. Below will guide you through both local and Azure DevOps, but you can technically use other methods.

{:.important}
Please note that the product toolkit is not included in the CluedIn license. This is an open-source toolkit provided by the CluedIn team to help you migrate your configuration between environments if you need to do that.

## Local configuration migration

This guide will be using the `import` and `export` scripts only. The toolkit also supports running the functions on their own, but this will not be covered as part of this documentation.

To successfully run this, you will need the following information before proceeding:
- Full URL of your front end.
- A backup path locally to store the JSON files exported.
- IDs of the data you want to back up.

{:.important}
To get the IDs of specific parameters, you will need to use the front end and navigate to the desired resource. In the URL, you will then notice the ID of a given object. This may be a GUID or integer depending on what is viewed.

### Exporting configuration (Source system)

1. Open up a `PowerShell`.
1. In the `PowerShell` window, run the following:

    **Note**: We will be using the ficticious front end `https://cluedin-source.customer.com` in the example below.

    ```powershell
    $params = @{
        BaseURL = 'customer.com'
        Organization = 'cluedin-source'
        BackupPath = '/path/to/export-20240403'
    }

    /path/to/CluedIn.Product.Toolkit/Scripts/Export-CluedInConfig.ps1 @params
        # The below are all optional. Please see what values are accepted below. If running without any of the below.
        # It will not export anything as everything defaults to export nothing.
        #
        # -BackupAdminSettings      [switch] true | false (Default)
        # -SelectVocabularies       [string] csv guids | None (Default)
        # -SelectDataSets           [string] csv ints | All | None (Default)
        # -SelectRules              [string] csv guids | All | None (Default)
        # -SelectExportTargets      [string] csv guids | All | None (Default)
        # -SelectStreams            [string] csv guids | All | None (Default)
        # -SelectGlossaries         [string] csv guids | All | None (Default)
        # -SelectCleanProjects      [string] csv guids | All | None (Default)
    ```

    **Note**: `/path/to/` will differ on your local system. Please update this to be the local respective path.

1. The script will launch and prepare to connect. You will be prompted for a username and password which will obtain a JWToken if successful. Once connected, it will attempt to export all the desired configuration specified above.

    Depending on how much configuration there is to export, this may take up to 15 minutes to complete. Once export has completed, move onto the import phase.

### Importing configuration (Destination system)

1. Open up a new `PowerShell` session to avoid any conflict with environmental variables.
1. In the `PowerShell` window, run the following:

    **Note**: We will be using the ficticious front end `https://cluedin-destination.customer.com` in the example below.

    ```powershell
    $params = @{
        BaseURL = 'customer.com'
        Organization = 'cluedin-destination'
        RestorePath = '/path/to/export-20240403'
    }

    /path/to/CluedIn.Product.Toolkit/Scripts/Import-CluedInConfig.ps1 @params
    ```

    **Note**: `/path/to/` will differ on your local system. Please update this to be the local respective path.

1. The script will launch and prepare to connect. When successful, it will iterate through the RestorePath and begin importing and/or correcting any configuration drift between the environments.

    The console will output any relevant changes that may have occurred during the import phase so that you can keep track of what has happened.

    {:.important}
    A lot of the comparisons are based on `Display Name` lookup. If a display name matches and there is configuration drift, it will attempt to correct this during import time.
    It will not delete any configuration as that is not within scope.

    Depending on how much configuration there is to import, this may take up to 15 minutes to complete.

This concludes the general process of how to export and import configuration locally from one environment to another.

## Configuration migration using Azure DevOps (pipeline)

This guide will be using the `import` and `export` scripts only. The toolkit also supports running the functions on their own, but this will not be covered as part of this documentation.

To successfully run this, you will need the following information before proceeding:

- Full URL of your front end.

- Access to Azure DevOps with the pipelines setup. Please refer to the README within the `CluedIn Product Toolkit`. Failing to set up the pipelines correctly will result in failed configuration backups and restores.

- IDs of the data you want to back up.

{:.important}
To get the IDs of specific parameters, you will need to use the front end and navigate to the desired resource. In the URL, you will then notice the ID of a given object. This may be a GUID or integer depending on what is viewed.

**To transfer configuration**

1. Navigate to the backup pipeline and click on [Run Pipeline].
1. Fill in parameters:

    **Note**: We will be using the ficticious front end `https://cluedin-source.customer.com` and `https://cluedin-destination.customer.com` in the example below.

    - **CluedIn Base URL (Source)**: This is in the format of customer.com without http(s)://.
    e.g. `customer.com`
    - **CluedIn Organization (Source)**: This is the first part of your cluedin environment.
    e.g. `cluedin-source`
    - **CluedIn Base URL (Destination)**: This is in the format of customer.com without http(s)://
    e.g. `customer.com`
    - **CluedIn Organization (Destination)**: This is the first part of your cluedin environment.
    e.g. `cluedin-destination`
    - **Admin Settings**: Checkbox determines 'True' or 'False'
    - **Vocabularies (guid, csv)**: Accepted values are 'None', or the guids seperated by a comma (,). All will not work for this one.
    - **Data Sets (guid, csv)**: Accepted values are 'All', 'None', or guids seperated by a comma (,).
    - **Rules (guid, csv)**: Accepted values are 'All', 'None', or guids seperated by a comma (,).
    - **Export Targets (guid, csv)**: Accepted values are 'All', 'None', or guids seperated by a comma (,).
    - **Streams (guid, csv)**: Accepted values are 'All', 'None', or guids seperated by a comma (,).
    - **Glossaries (guid, csv)**: Accepted values are 'All', 'None', or guids seperated by a comma (,).
    - **Clean Projects (guid, csv)**: Accepted values are 'All', 'None', or guids seperated by a comma (,).
    - **Push to repo**: If set to true, it will push your configuration json files to the specified git  repository in the pipeline.
1. When ready, click on [**Run**].

## Final notes

This guide only covers how to run the toolkit to migrate configuration from one environment to another. The steps to setup the Azure DevOps pipeline specifically must be followed from the document within the toolkit.

If at any stage you have issues with trying to do a migration, don't hesitate to reach out to CluedIn support who will be happy to assist.