---
title: Private SaaS - Azure Market Place
url: https://documentation.cluedin.net/operate/azure-marketplace/installation-guide
content_type: how-to
section: Deploy & operate > Azure Marketplace
---

# Private SaaS - Azure Market Place

> how-to: Steps to accomplish one task.

## On this page

1. TOC
   {:toc}

In this article, you will learn how to subscribe to CluedIn Private SaaS (via Azure Azure Marketplace) in the Azure portal and how to configure your CluedIn account.

![Five steps to install CluedIn SaaS: submit a request, receive a license key by email, subscribe in the Azure Marketplace, configure your CluedIn account, and get started with the email link sent after 30 minutes](https://documentation.cluedin.net/assets/images/deployment/saas-install/saas-installation-diagram.gif)

> **Important:** CluedIn team performs installation activities on all business days **except Friday**. Deploying on a Friday carries higher risk because issues may not surface immediately and can escalate into weekend incidents with fewer people available to respond. As a best practice, it is recommended to schedule installations earlier in the week (Tuesday–Thursday) to allow time for monitoring, troubleshooting, and stabilization.

## Submit a request and receive a license key

CluedIn Private SaaS (via Azure Azure Marketplace) is currently available by invitation only. You can request an invitation [here](https://www.cluedin.com/saas-invitation-application).

![Submit your request form with First Name, Last Name, Business Email, Job Title, Preferred Azure Region, and a Submit button](https://documentation.cluedin.net/assets/images/deployment/saas-install/saas-form.png)

After you submit an application, you'll receive an email with the license key needed to complete the Private SaaS installation process.

The CluedIn Private SaaS (via Azure Azure Marketplace) installation process consists of 2 parts:

1. Subscribing to CluedIn Private SaaS (via Azure Azure Marketplace). All details provided in this step are required by Microsoft.

1. Configuring an account with CluedIn. All details provided in this step are required by CluedIn.

![Two-part SaaS installation: in Microsoft, find the app, start the subscription, provide project and SaaS details, review terms, and subscribe; in CluedIn, validate the license key, enter basic information, and complete configuration](https://documentation.cluedin.net/assets/images/deployment/saas-install/saas-diagram.gif)

## Subscribe to CluedIn Private SaaS (via Azure Azure Marketplace)

Before you start the CluedIn Private SaaS (via Azure Azure Marketplace) installation process, make sure you meet all [Azure requirements](https://documentation.cluedin.net/operate/azure-marketplace/requirements.md).

> **Important:** Make sure that you have enabled marketplace purchases and configured the required user permissions (at least **Contributor**) for the subscription where you want to store the CluedIn SaaS application. For more information, see [Enable marketplace purchases in Azure](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/enable-marketplace-purchases).

**To subscribe to CluedIn Private SaaS (via Azure Azure Marketplace)**

1. In the Azure Marketplace, find [CluedIn Master Data Management – MDM (SaaS)](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/cluedin.cluedin-saas?tab=Overview).

1. On the **CluedIn Master Data Management Private SaaS** page, select **Get It Now**.

   ![CluedIn Master Data Management - MDM (SaaS) page in the Azure Marketplace, with the Get It Now button below the CluedIn logo](https://documentation.cluedin.net/assets/images/deployment/saas-install/saas-1-additional.png)

1. On the page that opens, review basic information about CluedIn Private SaaS (via Azure Azure Marketplace). Then, select **Subscribe**.

   ![CluedIn MDM (SaaS) offer page with the Plan dropdown set to Pay as you Go and the Subscribe button](https://documentation.cluedin.net/assets/images/deployment/saas-install/saas-3-subscribe.png)

1. On the **Basics** tab, in the **Project details** section, do the following:

   1. Select a **Subscription** where you want to store CluedIn Private SaaS (via Azure Azure Marketplace) application in your Azure account.

      If you encounter an error stating that the subscription requires permission to make purchases, it means that you don't have the required permission for the subscription. Contact your IT team to get the required permissions. For more information, see [Enable marketplace purchases in Azure](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/enable-marketplace-purchases).

      ![Basics tab error under Subscription: This subscription requires permission to make purchases](https://documentation.cluedin.net/assets/images/deployment/saas-install/saas-4-error.png)

   1. Select or create a **Resource group** where the SaaS subscription will be stored. If you create a new resource group, you need to choose the location for that resource group.

      The location of the resource group is not the same as the Azure region where CluedIn will be installed, it is just the location where subscription will be stored. You'll select the Azure region when configuring your CluedIn account as described in the next section.

1. In the **SaaS details** section, enter a **Name** for the Private SaaS application.

   ![Basics tab with Subscription CluedIn, Resource group myResourceGroup, and the SaaS details Name cluedin-saas](https://documentation.cluedin.net/assets/images/deployment/saas-install/saas-2.png)

1. (Optional) Select **Next: Tags** On the **Tags** tab, you can define tags to help you find your Private SaaS resource later.

1. Select **Review + subscribe**.

1. On the **Review + subscribe** tab, review the terms of use, contact information, and billing details.

   Billing is handled exclusively by Microsoft.

1. Select **Subscribe**.

   You'll see the following message: _Your SaaS subscription is in progress_. This process takes a few minutes. Don't close the window until it's finished.

   ![Subscription progress page reading Your SaaS subscription is in progress, with the Configure account now button still disabled](https://documentation.cluedin.net/assets/images/deployment/saas-install/saas-3.png)

   After the subscription is completed, the **Configure account now** button becomes active, and you'll receive an email from Microsoft requesting you to activate the new subscription.

   ![Microsoft email asking you to configure your new CluedIn SaaS account, with a Configure account button](https://documentation.cluedin.net/assets/images/deployment/saas-install/saas-email-1.png)

1. Either in the email or in the Azure Marketplace, select the corresponding button to configure the account. If you selected the button in the Azure Marketplace, you can ignore the email.

   You'll be redirected to the CluedIn account configuration page.

## Configure an account with CluedIn

To configure an account with CluedIn, you need a valid license key. You can find a license key in an email from CluedIn if you have previously requested SaaS application. If you don't have a license key, request it [here](https://www.cluedin.com/saas-invitation-application).

**To configure a CluedIn account**

1. On the CluedIn account configuration page, enter a license key, and then select **Validate your license key**.

   ![Configure your account page with Yes selected for having a CluedIn SaaS license, a License Key field, and the Validate your license key button](https://documentation.cluedin.net/assets/images/deployment/saas-install/saas-6.png)

1. Provide basic information for setting up your CluedIn account:

   1. Enter your **Email**.

   1. Enter an **Organization Name** to create a link to your CluedIn instance.

   1. Enter a **Password** for signing in to your CluedIn instance.

   1. Select an **Azure Region** where you want CluedIn to be installed.

   1. Select **Complete configuration**.

      ![Configure your account form with Email, Organization Name, Password, and Azure Region fields and the Complete configuration button](https://documentation.cluedin.net/assets/images/deployment/saas-install/saas-4.png)

   After the configuration is completed, you'll receive an email from Microsoft notifying you that the configuration was successful.

   ![Microsoft email confirming the CluedIn SaaS subscription is now active, with a Review SaaS subscription button](https://documentation.cluedin.net/assets/images/deployment/saas-install/saas-email-2.png)

   Also, you can view your SaaS subscription in the Azure portal.

   ![SaaS subscription overview in the Azure portal showing it was configured successfully, with plan, billing term, recurring billing, and pricing details](https://documentation.cluedin.net/assets/images/deployment/saas-install/subscription-active.png)

Our automatic installer will start preparing your isolated environment. Once it is ready, you'll receive an email from CluedIn with instructions on how to get started. It can take up to 30 minutes to receive an email.

## Next steps

After configuring an account, you will receive an email with a link to your CluedIn instance. To sign in, enter the email and password that you provided when configuring your CluedIn account.

![CluedIn Sign in page with Email and Password fields and a Sign In button](https://documentation.cluedin.net/assets/images/deployment/saas-install/saas-5.png)

> **Important:** To enable SSO (Entra ID) in SaaS, please refer to our [SSO configuration guide](https://documentation.cluedin.net/operate/configuration/configure-sso.md).

Useful links:

- [Getting access](https://documentation.cluedin.net/getting-access#sign-in-by-email) – learn how to sign in to CluedIn.

- [Getting started](https://documentation.cluedin.net/getting-started) – get acquainted with the main CluedIn features.

- [Pricing](https://documentation.cluedin.net/operate/deployment-options/pricing.md) – learn about our pricing options (pay-as-you-go and committed deal).

Up: [Azure Marketplace](https://documentation.cluedin.net/operate/azure-marketplace.md)
