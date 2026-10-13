---
title: Delete CluedIn instance
url: https://documentation.cluedin.net/operate/deployment-options/delete-cluedin-instance
content_type: how-to
section: Deploy & operate > Deployment options
---

# Delete CluedIn instance

> how-to: Steps to accomplish one task.

This article outlines how to delete your CluedIn instance if you no longer want to use it. Note that all data that you have in CluedIn will be permanently deleted. Therefore, consider making [backups](https://documentation.cluedin.net/archive/historical-operations/backup-and-restore-draft) if needed.

## Delete CluedIn PaaS

If you no longer want to use CluedIn PaaS or if the installation of CluedIn PaaS failed, you can delete the instance. Deleting CluedIn PaaS instance will reset your CluedIn license. It means that you can [install](https://documentation.cluedin.net/operate/azure-marketplace/step-3.md) CluedIn again using the same license key.

There are two ways to delete the CluedIn PaaS instance:

- Delete the resource group where you installed CluedIn.

- Delete the managed application within the resource group where you installed CluedIn.

### Delete resource group

1. In the [Azure portal](https://portal.azure.com/), navigate to the resource group where you installed CluedIn.

1. At the top of the page, select **Delete resource group**.

    ![Azure resource group rg-mmc overview with the Delete resource group button highlighted](https://documentation.cluedin.net/assets/images/deployment/delete-cluedin-instance/delete-paas-delete-resource-group.png)

1. Confirm the deletion by typing the name of the resource group.

### Delete managed application

1. In the [Azure portal](https://portal.azure.com/), navigate to the resource group where you installed CluedIn, and then find the corresponding managed application.

    ![Resource group rg-mmc resources list with the cluedin managed application highlighted](https://documentation.cluedin.net/assets/images/deployment/delete-cluedin-instance/delete-paas-resource-group.png)

1. Open the managed application that you want to delete.

    ![Overview page of the cluedin managed application, with a Delete button at the top](https://documentation.cluedin.net/assets/images/deployment/delete-cluedin-instance/delete-paas-open-managed-application.png)

1. At the top of the page, select **Delete**, and then confirm your choice.

    ![Delete managed application confirmation asking whether to delete cluedin, with Yes and No buttons](https://documentation.cluedin.net/assets/images/deployment/delete-cluedin-instance/delete-paas-confirmation.png)

## Delete CluedIn SaaS

If you no longer want to use CluedIn SaaS, you can delete the instance in one of two ways:

- Cancel CluedIn SaaS subscription.

- Delete the resource group within the CluedIn SaaS subscription.

### Cancel CluedIn SaaS subscription

1. In the [Azure portal](https://portal.azure.com/), navigate to your CluedIn SaaS subscription. At the top of the subscription page, select **Cancel Subscription**.

    ![CluedIn SaaS subscription page in the Azure portal with the Cancel subscription button highlighted](https://documentation.cluedin.net/assets/images/deployment/delete-cluedin-instance/cancel-subscription-1.png)

1. Review the terms for cancelling the subscription and select the checkbox to confirm that you have read and understood the implications. Optionally, provide a reason for cancellation. Finally, select **Cancel subscription**.

    ![Cancel SaaS subscription pane with the confirmation checkbox selected, a cancellation reason chosen, and the Cancel subscription button](https://documentation.cluedin.net/assets/images/deployment/delete-cluedin-instance/cancel-subscription-2.png)

### Delete resource group within subscription

1. In the [Azure portal](https://portal.azure.com/), navigate to your CluedIn SaaS subscription. On the subscription page, in the **Product and plan details** section, select the resource group.

    ![CluedIn SaaS subscription page with the Resource group link highlighted in the billing info section](https://documentation.cluedin.net/assets/images/deployment/delete-cluedin-instance/delete-resource-group-within-subscription.png)

1. Select the checkbox next to the resource group. At the top of the page, select **Delete**.

1. Enter _delete_ to confirm your choice, and then select **Delete**.

    ![Resource group with the SaaS resource selected and the Delete Resources pane open, delete entered to confirm, and the Delete button](https://documentation.cluedin.net/assets/images/deployment/delete-cluedin-instance/delete-resource-group-within-subscription-2.png)

Up: [Deployment options](https://documentation.cluedin.net/operate/deployment-options.md)
