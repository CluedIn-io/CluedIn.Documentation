---
layout: cluedin
nav_order: 2
parent: CluedIn SaaS
grand_parent: Installation
permalink: {{ site.baseurl }}/deployment/saas/installation-guide
title: SaaS installation guide
last_modified: 2024-04-08
headerIcon: "saas"
---
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

In this article, you will learn how to subscribe to CluedIn SaaS in the Azure portal and how to configure your CluedIn account.

![saas-installation-diagram.gif](../../assets/images/deployment/saas-install/saas-installation-diagram.gif)

## Submit a request and receive a license key

CluedIn SaaS is currently available by invitation only. You can request an invitation [here](https://www.cluedin.com/saas-invitation-application).

![saas-form.png](../../assets/images/deployment/saas-install/saas-form.png)

After you submit an application, you'll receive an email with the license key needed to complete the SaaS installation process.

The CluedIn SaaS installation process consists of 2 parts: 

1. Subscribing to CluedIn SaaS in the Azure Marketplace. All details provided in this step are required by Microsoft.

1. Configuring an account with CluedIn. All details provided in this step are required by CluedIn.

![saas-diagram.gif](../../assets/images/deployment/saas-install/saas-diagram.gif)

## Subscribe to CluedIn SaaS in Azure Marketplace

Before you start the CluedIn SaaS installation process, make sure you meet all [Azure requirements](/deployment/saas/requirements).

{:.important}
Make sure that you have enabled marketplace purchases and configured the required user permissions (at least **Contributor**) for the subscription where you want to store the CluedIn SaaS application. For more information, see [Enable marketplace purchases in Azure](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/enable-marketplace-purchases).

**To subscribe to CluedIn SaaS**

1. In the Azure Marketplace, find [CluedIn Master Data Management – MDM (SaaS)](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/cluedin.cluedin-saas?tab=Overview).

1. On the **CluedIn Master Data Management SaaS** page, select **Get It Now**.

    ![saas-1-additional.png](../../assets/images/deployment/saas-install/saas-1-additional.png)

1. On the page that opens, review basic information about CluedIn SaaS. Then, select **Subscribe**.

    ![saas-3-subscribe.png](../../assets/images/deployment/saas-install/saas-3-subscribe.png)

1. On the **Basics** tab, in the **Project details** section, do the following:

    1. Select a **Subscription** where you want to store CluedIn SaaS application in your Azure account.

        If you encounter an error stating that the subscription requires permission to make purchases, it means that you don't have the required permission for the subscription. Contact your IT team to get the required permissions. For more information, see [Enable marketplace purchases in Azure](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/enable-marketplace-purchases).
        
        ![saas-4-error.png](../../assets/images/deployment/saas-install/saas-4-error.png)

    1. Select or create a **Resource group** where the SaaS subscription will be stored. If you create a new resource group, you need to choose the location for that resource group.
    
        {:.important}
        The location of the resource group is not the same as the Azure region where CluedIn will be installed, it is just the location where subscription will be stored. You'll select the Azure region when configuring your CluedIn account as described in the next section.

1. In the **SaaS details** section, enter a **Name** for the SaaS application.

    ![saas-2.png](../../assets/images/deployment/saas-install/saas-2.png)

1. (Optional) Select **Next: Tags** On the **Tags** tab, you can define tags to help you find your SaaS resource later.

1. Select **Review + subscribe**.

1. On the **Review + subscribe** tab, review the terms of use, contact information, and billing details.

    {:.important}
    Billing is handled exclusively by Microsoft.

1. Select **Subscribe**.

    You'll see the following message: _Your SaaS subscription is in progress_. This process takes a few minutes. Don't close the window until it's finished.

    ![saas-3.png](../../assets/images/deployment/saas-install/saas-3.png)

    After the subscription is completed, the **Configure account now** button becomes active, and you'll receive an email from Microsoft requesting you to activate the new subscription.

    ![saas-email-1.png](../../assets/images/deployment/saas-install/saas-email-1.png)

1. Either in the email or in the Azure Marketplace, select the corresponding button to configure the account. If you selected the button in the Azure Marketplace, you can ignore the email.

    You'll be redirected to the CluedIn account configuration page.

## Configure an account with CluedIn

To configure an account with CluedIn, you need a valid license key. You can find a license key in an email from CluedIn if you have previously requested SaaS application. If you don't have a license key, request it [here](https://www.cluedin.com/saas-invitation-application).

**To configure a CluedIn account**

1. On the CluedIn account configuration page, enter a license key, and then select **Validate your license key**.

    ![saas-6.png](../../assets/images/deployment/saas-install/saas-6.png)

1. Provide basic information for setting up your CluedIn account:

    1. Enter your **Email**.

    1. Enter an **Organization Name** to create a link to your CluedIn instance.

    1. Enter a **Password** for signing in to your CluedIn instance.

    1. Select an **Azure Region** where you want CluedIn to be installed.

    1. Select **Complete configuration**.

        ![saas-4.png](../../assets/images/deployment/saas-install/saas-4.png)

    After the configuration is completed, you'll receive an email from Microsoft notifying you that the configuration was successful.

    ![saas-email-2.png](../../assets/images/deployment/saas-install/saas-email-2.png)

    Also, you can view your SaaS subscription in the Azure portal.

    ![subscription-active.png](../../assets/images/deployment/saas-install/subscription-active.png)
    
Our automatic installer will start preparing your isolated environment. Once it is ready, you'll receive an email from CluedIn with instructions on how to get started. It can take up to 30 minutes to receive an email.

## Next steps

After configuring an account, you will receive an email with a link to your CluedIn instance. To sign in, enter the email and password that you provided when configuring your CluedIn account.

![saas-5.png](../../assets/images/deployment/saas-install/saas-5.png)

{:.important}
To enable SSO (Entra ID) in SaaS, please refer to our [SSO configuration guide](/deployment/infra-how-tos/configure-sso).

Useful links:

- [Getting access](https://documentation.cluedin.net/getting-access#sign-in-by-email) – learn how to sign in to CluedIn.

- [Geeting started](https://documentation.cluedin.net/getting-started) – get acquainted with the main CluedIn features.

- [Pricing](/deployment/pricing) – learn about our pricing options (pay-as-you-go and committed deal).