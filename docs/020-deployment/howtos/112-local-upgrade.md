---
layout: cluedin
nav_order: 14
parent: How-to guides for PaaS
grand_parent: Installation
permalink: /deployment/infra-how-tos/local-upgrade
title: Local upgrade
tags: ["deployment", "local"]
last_modified: 2023-10-06
---

In this article, you will learn how to upgrade your local instance of CluedIn to the new version.

**Important!** Before upgrading your local instance of CluedIn, consider whether it would be more convenient to create a new environment. Typically, you shouldn't store many records in your local instance, so re-ingesting the records should be fast.

**To upgrade the local instance of CluedIn**

1. Depending on the release that you need, do one of the following:

    - To get the latest release, run `git pull` on the master branch of [CluedIn Home](https://github.com/CluedIn-io/Home) repository.

    - To get a specific release, in [CluedIn Home](https://github.com/CluedIn-io/Home) repository, switch to the tag containing the needed release, and then check out the tag by running the following command: `$ git checkout tags/<tag> -b <branch>`.

        ![local-upgrade-1.png](../../assets/images/ama/howtos/local-upgrade-1.png)

1. Retrieve the SQL Init image by running the following command:  
`docker pull {acr url}/cluedin/sqlserver-init:[VERSION]`

    You should use the version to which you want to upgrade (e.g., 3.7.4).

1. Perform the database update by running the following command:  
`docker run --rm -it -e MSSQL_HOST=host.docker.internal {acr url}/cluedin/sqlserver-init:[VERSION]`

    You should use the version to which you want to upgrade (e.g., 3.7.4).

    {:.important}
    Your environment's SQL Server Docker image should be running for this image to run correctly.

1. In the **.env** file for your environment, change the tags to reference the version of CluedIn that you are upgrading to.

    ![local-upgrade-2.png](../../assets/images/ama/howtos/local-upgrade-2.png)

1. Using a diff tool, compare the **.env** file for your environment with the **default/.env** file. If some values are missing in the **.env** file for your environment, copy them from the **default/.env** file.

1. Run the following command to get container images:  
`pwsh ./cluedin pull -env [NAME OF ENV]`

1. Run the following command to start your instance of CluedIn:  
`pwsh ./cluedin up -env [NAME OF ENV]`
