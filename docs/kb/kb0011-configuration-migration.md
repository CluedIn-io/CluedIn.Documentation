---
layout: cluedin
title: Configuration Migration
permalink: /kb/config-migrate
nav_exclude: true
tags: ["configuration", "migration"]
is_kb: true
---

## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

This document covers the process for migrating CluedIn configuration from one environment to another environment. This is especially useful when developing your foundation on one environment and want to promote it to production.

## Configuration migration

### Prerequisites
- PowerShell Core
- PowerShell 'CluedIn Product Toolkit' Module. Please reach out to CluedIn support to get this toolkit.
- Service or Admin account to do the export and import
- Access to the front end, whether it's public facing or private facing

### Guide
The product toolkit supports a number of methods of transferring configuration from one environment to another. The main two methods are running locally on your desktop, or alternatively using a pipeline platform such as Azure DevOps

Below will guide you through both local and Azure DevOps, but you can technically use other methods.

#### Locally

This guide will be using the `import` and `export` scripts only. The toolkit also supports running the functions on their own, but this will not be covered as part of this documentation.

To successfully run this, you will need the following information before proceeding:
- Full URL of your front end.
- A backup path locally to store the JSON files exported.
- IDs of the data you want to back up.

{:.important}
To get the Ids of specific parameters, you will need to use the frontend and navigate to the desired resource. In the url, you will then notice the id of a given object. This may be a guid or integer depending on what is viewed.

##### Exporting configuration (Source system)

1. Open up a `PowerShell`.
1. In the `PowerShell` window, run the following: 

    **Note**: We will be using the ficticious front end `https://cluedin-source.customer.com` in the example below.

    ```powershell
    $BaseURL = 'customer.com'
    $Organization = 'cluedin-source'
    $BackupPath = '/path/to/export-20240403'

    /path/to/CluedIn.Product.Toolkit/Scripts/Export-CluedInConfig.ps1 \
        -BaseURL ${BaseURL} \
        -Organization ${Organization} \
        -BackupPath ${$BackupPath}
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

1. The script will launch and prepare to connect. You will be prompted for a username and password which will obtain a JWToken if successful. Once connect, it will attempt to export all the desired configuration specified above.

    Depending on how much configuration there is to export, this may take up to 15 minutes to complete. Once export has completed, move onto the import phase.

##### Importing configuration (Destination system)

1. Open up a new `PowerShell` session to avoid any conflict with environmental variables
1. In the `PowerShell` window, run the following:

    **Note**: We will be using the ficticious front end `https://cluedin-destination.customer.com` in the example below.

    ```powershell
    $BaseURL = 'customer.com'
    $Organization = 'cluedin-destination'
    $RestorePath = '/path/to/export-20240403'

    /path/to/CluedIn.Product.Toolkit/Scripts/Import-CluedInConfig.ps1 \
        -BaseURL ${BaseURL} \
        -Organization ${Organization} \
        -RestorePath ${$RestorePath}
    ```

    **Note**: `/path/to/` will differ on your local system. Please update this to be the local respective path.

1. The script will launch and prepare to connect. When successful, it will iterate through the RestorePath and begin importing and/or correcting any configuration drift between the environments. 

    The console will output any relevant changes that may have occurred during the import phase so that you can keep track of what has happened.

    {:.important}
    A lot of the comparisons are based on `Display Name` lookup. If a display name matches and there is configuration drift, it will attempt to correct this during import time.
    It will not delete any configuration as that is not within scope.

    Depending on how much configuration there is to import, this may take up to 15 minutes to complete.

This concludes the general process of how to export and import configuration from one environment to another.

#### Azure DevOps (Pipeline)

This guide will be using the `import` and `export` scripts only. The toolkit also supports running the functions on their own, but this will not be covered as part of this documentation.

To successfully run this, you will need the following information before proceeding:
- Full url of your frontend
- Access to Azure DevOps with the pipelines setup (Please refer to the README within the `CluedIn Product Toolkit`). Failing to setup the pipelines correctly will result in failed configuration backups and restores.
- Id's of the data you want to backup

{:.important}
To get the Ids of specific parameters, you will need to use the frontend and navigate to the desired resource. In the url, you will then notice the id of a given object. This may be a guid or integer depending on what is viewed.

##### Transfer configuration

1. Navigate to the backup pipeline and click on [Run Pipeline]
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
1. When ready, click on [**Run**]

### Final Notes

This guide only covers how to run the toolkit to migrate configuration from one environment to another. The steps to setup the Azure DevOps pipeline specifically must be followed from the document within the toolkit.

If at any stage you have issues with trying to do a migration, don't hesitate to reach out to CluedIn support who will be happy to assist.