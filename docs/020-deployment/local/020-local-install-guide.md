---
layout: cluedin
nav_order: 2
parent: Local
grand_parent: Installation
permalink: /deployment/local/step-2
title: Local installation guide
tags: ["deployment", "local"]
last_modified: 2023-06-30
headerIcon: "local"
---
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

In this article, you will learn how to install CluedIn locally.

![local-installation-guide.gif](../../assets/images/deployment/local-installation-guide.gif)

## Clone CluedIn repository

The first step for the local installation of CluedIn is to clone the CluedIn public repository named **Home** [https://github.com/CluedIn-io/Home](https://github.com/CluedIn-io/Home).

**To clone the CluedIn repository**

- At the command prompt, run the following command.

    ```
    git clone https://github.com/CluedIn-io/Home
    ```

    You will get an output similar to the following.

    ![git-clone.png](../../assets/images/local-install/git-clone.png)

    Alternatively, you can clone the repository using your preferred Git client.

## Authenticate to CluedIn ACR

**Prerequisites**

- For Windows environments: Modify the PowerShell execution policy to enable running local scripts. To do that, use the `Set-ExecutionPolicy RemoteSigned` command.

    ![pwsh-policy.png](../../assets/images/local-install/pwsh-policy.png)

- For Windows environments: Run your terminal session as an administrator.

- For non-Windows environments: Use the `sudo` command.

CluedIn uses two ACRs:

- **Production** – the registry name is **cluedinprod**. This registry is used to store all official images from CluedIn.

- **Testing & development** – the registry name is **cluedindev**. This registry is used internally by CluedIn to develop the software. Occasionally, this registry can be used by partners and customers to test new functionality before it is officially released.

You can find the ACR to which you have been granted access in the <a href="/deployment/local/step-1#get-access-to-CluedIn-container-registry">email from CluedIn</a>.

{:.important}
In the following instructions, we use `2024.01` as the release number. You should always use the latest release number. You can find the list of releases [here](https://cluedin-io.github.io/Releases/).

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

    This process might take some time.

    ![pull_images_process.gif](../../assets/images/local-install/pull_images_process.gif)

    You will get an output similar to the following.

    ![pull-images-result.png](../../assets/images/local-install/pull-images-result.png)

1. Create an environment. In the following command, we use `202401` as the name of the environment and `2024.01` as the release number. Keep in mind that the environment name is the same as the release number, but without the dot (.). Defining the environment does not support the dot (.), but you can use the dot for the release number in the `tag`.

    To create an environment, run the following command:

    ```
    pwsh .\cluedin.ps1 env 202401 -tag 2024.01
    ```

    {:.important}
    You should always use the latest release number. You can find the list of releases [here](https://cluedin-io.github.io/Releases/).
    
    You will get an output similar to the following.

    ![create-env.png](../../assets/images/local-install/create-env.png)

    {:.important}
    Environment is used for having scripts that can start CluedIn of different versions. Docker does not support multiple CluedIn versions running in parallel.

## Start CluedIn

To start CluedIn, run the following command:

```
pwsh .\cluedin.ps1 up 202401
```

where `202401` is the name of the environment.

You will get an output similar to the following.

![start-cluedin.png](../../assets/images/local-install/start-cluedin.png)

## Create your sign-in credentials

The last step of the local installation of CluedIn is to create an organization and credentials for signing in to CluedIn.

**Prerequisites**

Make sure that the server has started correctly. To do that, in Docker Desktop, select the server and look for a similar section in logs.

![cluedin-server-logs.png](../../assets/images/local-install/cluedin-server-logs.png)

{:.important}
In the following procedure, we’ll use `202401` as an environment, `example` as an organization name, and `Example123!` as a password for signing in to CluedIn.

**To create organization and sign-in credentials**

1. Run the following command:

    ```
    pwsh .\cluedin.ps1 createorg 202401 -Name example -Pass Example123!
    ```

    You'll get the credentials for signing in to CluedIn.

    ![create-org.png](../../assets/images/local-install/create-org.png)

1. Open the CluedIn sign-in page by running the following command:

    ```
    pwsh .\cluedin.ps1 open 202401 -Org example
    ```

    ![open-cluedin.png](../../assets/images/local-install/open-cluedin.png)

    As a result, CluedIn opens in your default browser.   

    By default, CluedIn uses the following address: `http://app.127.0.0.1.nip.io:9080`. If the nip.io domain does not work, refer to the [Troubleshooting](#troubleshooting) section.

1. Sign in to CluedIn using the credentials that you received in step 1.

    ![sign-in-page.png](../../assets/images/local-install/sign-in-page.png)

## Troubleshooting

When the nip.io domain does not work, do the following:

1. In the **hosts** file (`C:\Windows\System32\drivers\etc\hosts`), add the following lines:

    ```
    127.0.0.1 cluedin.local
    127.0.0.1 app.cluedin.local
    127.0.0.1 foobar.cluedin.local
    ```

1. In the **.env** file, find the following line:

    ```
    CLUEDIN_DOMAIN=127.0.0.1.nip.io
    ```

1. Replace the line that you found in step 2 with the following line:

    ```
    CLUEDIN_DOMAIN=clueidn.local
    ```

## Results

You have installed CluedIn locally.

## Next steps

Add more features to CluedIn with the help of extension packages. Learn how to do that in [Extension packages](/deployment/local/step-3).