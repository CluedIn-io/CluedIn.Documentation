---
layout: cluedin
title: Delete CluedIn instance
parent: Installation
permalink: /deployment/delete-cluedin-instance
nav_order: 5
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

This article outlines how to delete your CluedIn instance if you no longer want to use it. Note that all data that you have in CluedIn will be permanently deleted. Therefore, consider making [backups](/deployment/infra-how-tos/ama-backup) if needed.

## Delete CluedIn PaaS

If you no longer want to use CluedIn PaaS or if the installation of CluedIn PaaS failed, you can delete the instance. Deleting CluedIn PaaS instance will reset your CluedIn license. It means that you can [install](/deployment/azure-marketplace/step-3) CluedIn again using the same license key.

There are two ways to delete the CluedIn PaaS instance:

- Delete the resource group where you installed CluedIn.

- Delete the managed application within the resource group where you installed CluedIn.

### Delete resource group

1. In the [Azure portal](https://portal.azure.com/), navigate to the resource group where you installed CluedIn.

1. At the top of the page, select **Delete resource group**.

    ![delete-paas-delete-resource-group.png]({{ "/assets/images/deployment/delete-cluedin-instance/delete-paas-delete-resource-group.png" | relative_url }})

1. Confirm the deletion by typing the name of the resource group.

### Delete managed application

1. In the [Azure portal](https://portal.azure.com/), navigate to the resource group where you installed CluedIn, and then find the corresponding managed application.

    ![delete-paas-resource-group.png]({{ "/assets/images/deployment/delete-cluedin-instance/delete-paas-resource-group.png" | relative_url }})

1. Open the managed application that you want to delete.

    ![delete-paas-open-managed-application.png]({{ "/assets/images/deployment/delete-cluedin-instance/delete-paas-open-managed-application.png" | relative_url }})

1. At the top of the page, select **Delete**, and then confirm your choice.

    ![delete-paas-confirmation.png]({{ "/assets/images/deployment/delete-cluedin-instance/delete-paas-confirmation.png" | relative_url }})

## Delete CluedIn SaaS

If you no longer want to use CluedIn SaaS, you can delete the instance in one of two ways:

- Cancel CluedIn SaaS subscription.

- Delete the resource group within the CluedIn SaaS subscription.

### Cancel CluedIn SaaS subscription

1. In the [Azure portal](https://portal.azure.com/), navigate to your CluedIn SaaS subscription. At the top of the subscription page, select **Cancel Subscription**.

    ![cancel-subscription-1.png]({{ "/assets/images/deployment/delete-cluedin-instance/cancel-subscription-1.png" | relative_url }})

1. Review the terms for cancelling the subscription and select the checkbox to confirm that you have read and understood the implications. Optionally, provide a reason for cancellation. Finally, select **Cancel subscription**.

    ![cancel-subscription-2.png]({{ "/assets/images/deployment/delete-cluedin-instance/cancel-subscription-2.png" | relative_url }})

### Delete resource group within subscription

1. In the [Azure portal](https://portal.azure.com/), navigate to your CluedIn SaaS subscription. On the subscription page, in the **Product and plan details** section, select the resource group.

    ![delete-resource-group-within-subscription.png]({{ "/assets/images/deployment/delete-cluedin-instance/delete-resource-group-within-subscription.png" | relative_url }})

1. Select the checkbox next to the resource group. At the top of the page, select **Delete**.

1. Enter _delete_ to confirm your choice, and then select **Delete**.

    ![delete-resource-group-within-subscription-2.png]({{ "/assets/images/deployment/delete-cluedin-instance/delete-resource-group-within-subscription-2.png" | relative_url }})