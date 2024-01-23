---
layout: cluedin
nav_order: 2
parent: Local
grand_parent: Installation
permalink: /deployment/local/step-2
title: Local installation guide
tags: ["deployment", "local"]
last_modified: 2023-06-30
---
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

In this article, you will learn how to install CluedIn locally.

![local-installation.png](../../assets/images/local-install/local-installation.png)

## Clone CluedIn repository

The first step for the local installation of CluedIn is to clone the CluedIn public repository named **Home** [https://github.com/CluedIn-io/Home](https://github.com/CluedIn-io/Home).

**To clone the CluedIn repository**

- At the command prompt, run the following command:
```
git clone https://github.com/CluedIn-io/Home
```

    You will get an output similar to the following.

    ![git-clone.png](../../assets/images/local-install/git-clone.png)

    **Note:** Alternatively, you can clone the repository using your preferred Git client.

## Authenticate to CluedIn ACR

**Prerequisites**

- For Windows environments: Modify the PowerShell execution policy to enable running local scripts. To do that, use the `Set-ExecutionPolicy RemoteSigned` command.

    ![pwsh-policy.png](../../assets/images/local-install/pwsh-policy.png)

- For Windows environments: Run your terminal session as an administrator.
- For non-Windows environments: Use the `sudo` command.

<hr>

CluedIn uses two ACRs:

- **Production** – the registry name is **cluedinprod**. This registry is used to store all official images from CluedIn.
- **Early Access** – the registry name is **cluedindev**. This registry is used internally by CluedIn to develop the software. Occasionally, this registry can be used by partners and customers to test new functionality before it is officially released.

You can find the ACR to which you have been granted access in the <a href="/deployment/local/step-1#get-access-to-CluedIn-container-registry">email from CluedIn</a>.

**To authenticate to CluedIn ACR**

1. Open to the checkout directory by running the following command:
 ```
    cd Home
 ```

1. Sign in to Docker. Depending on the registry to which you have been granted access, do one of the following:

    - For **Production**, run the following command:
    ```
    docker login cluedinprod.azurecr.io
    ```

    - For **Early Access**, run the following command:
    ```
    docker login cluedindev.azurecr.io
    ```

1. Enter the username and password that you received in the email from CluedIn.

1. To verify your access, pull images from the ACR by running the following command:
 ```
 pwsh .\cluedin.ps1 pull
 ```
    This process takes some time.

    ![pull_images_process.gif](../../assets/images/local-install/pull_images_process.gif)

    You will get an output similar to the following.

    ![pull-images-result.png](../../assets/images/local-install/pull-images-result.png)

1. Create an environment. In the following command, we use `202304` as the name of the environment and `2023.04` as the release number. To create an environment, run the following command:
```
 pwsh .\cluedin.ps1 env 202304 -tag 2023.04
 ```

    **Important!** You should use the most recent release number. Find the list of releases [here](https://cluedin-io.github.io/Releases/).
    
    You will get an output similar to the following.

    ![create-env.png](../../assets/images/local-install/create-env.png)

    **Note:** Environment is used for having scripts that can start CluedIn of different versions. Docker does not support multiple CluedIn versions running in parallel.

## Start CluedIn

As Docker is not an orchestration tool like Kubernetes, starting up Docker containers may require some manual configuration steps to ensure proper initialization.

**To start CluedIn**

1. Run the following command:
```
pwsh .\cluedin.ps1 up 202304 -disable server
```

    where `202304` is the name of the environment.

    You will get an output similar to the following.

    ![disable-server.png](../../assets/images/local-install/disable-server.png)

1. In Docker Desktop, check if SQL Server is ready. To do that, select the SQL Server container and look for a similar section in logs.

    ![sql-server-logs.png](../../assets/images/local-install/sql-server-logs.png)

1. Run the following command:
```
pwsh .\cluedin.ps1 up 202304
```

    where `202304` is the name of the environment.

    You will get an output similar to the following.

    ![start-cluedin.png](../../assets/images/local-install/start-cluedin.png)

## Create your sign-in credentials

The last step of the local installation of CluedIn is to create an organization and credentials for signing in to CluedIn.

**Prerequisites**

Make sure that the server has started correctly. To do that, in Docker Desktop, select the server and look for a similar section in logs.

![cluedin-server-logs.png](../../assets/images/local-install/cluedin-server-logs.png)

<hr>

**Important!** In the following procedure, we’ll use `202304` as an environment, `example` as an organization name, and `Example123!` as a password for signing in to CluedIn.

**To create organization and sign-in credentials**

1. Run the following command:
```
pwsh .\cluedin.ps1 createorg 202304 -Name example -Pass Example123!
```

    You'll get the credentials for signing in to CluedIn.

    ![create-org.png](../../assets/images/local-install/create-org.png)

1. Open the CluedIn sign-in page by running the following command:
```
pwsh .\cluedin.ps1 open 202304 -Org example
```

    ![open-cluedin.png](../../assets/images/local-install/open-cluedin.png)

    As a result, CluedIn opens in your default browser.   

    By default, CluedIn uses the following address: `http://app.127.0.0.1.nip.io:9080`

1. Sign in to CluedIn using the credentials that you received in step 1.

    ![sign-in-page.png](../../assets/images/local-install/sign-in-page.png)

## Results

You have installed CluedIn locally.

## Next steps

Add more features to CluedIn with the help of extension packages. Learn how to do that in [Extension packages](/deployment/local/step-3).