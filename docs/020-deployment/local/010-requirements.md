---
layout: default
nav_order: 1
parent: Local
grand_parent: Installation
permalink: /deployment/local/step-1
title: Local installation requirements
tags: ["deployment", "local"]
last_modified: 2023-06-30
---
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

In this article, you will learn about the pre-installation processes that you must perform to ensure successful local installation of CluedIn.

![local-installation-checklist.png](../../assets/images/local-install/local-installation-checklist.png)

# Get access to CluedIn container registry

The first to do to be able to run CluedIn locally is to get access to CluedIn Azure Container Registry (ACR).

**Important!** Only our partners and customers can get access to CluedIn ACR. If you are not our partner or customer, consider becoming one. Discover the benefits and advantages of being our partner [here](https://www.cluedin.com/become-a-partner).

**To get access to CluedIn ACR**

1. Fill in and submit the [form](https://forms.office.com/pages/responsepage.aspx?id=YSiu9fyznUSp50nBTQEawIEsLHex0dtAnRBIgXFdeu5UQ0ZFWU0wUFI4N1lDMkRRSFpPSUg2QjdSWCQlQCN0PWcu).

    In the form, you need to specify the type of access that you need: **Production** (access to release, support, and occasional beta builds) and/or **Early Access** (access to early release builds that are not supported for production).

    After you submit the form, you'll receive an email with instructions to verify your email address.
    
    ![email-sample.png](../../assets/images/local-install/email-sample.png)

1. In the email, select **Verify**.

    A new page opens in your default browser.

1. Select **Confirm 'Verify'**.

    ![confirm-email-verification.png](../../assets/images/local-install/confirm-email-verification.png)
    
    After you verify your email address, you'll receive an email with credentials. You'll need these credentials for authenticating to ACR.

    ![email-access.png](../../assets/images/local-install/email-access.png)

# Check hardware requirements

Running clusters locally requires a substantial amount of computational power in terms of both CPU and memory resources.

Make sure that your computer meets the following hardware requirements:

- **Modern CPU** (Intel or AMD). We do not support ARM CPU.
- **16 GB** of free memory. We recommend having 32 GB of free memory.

# Check software requirements

Make sure that you have installed the following software:

- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Git](https://gitforwindows.org/)
- [PowerShell](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell?view=powershell-7.3) 7 or higher

In addition, make sure that you have access to [CluedIn container registry](#get-access-to-cluedin-container-registry).

# Results

- You have access to CluedIn container registry.
- Your computer meets hardware and software requirements for local installation of CluedIn.

# Next steps

Start the local installation of CluedIn as described in our [Local installation guide](/deployment/local/step-2).