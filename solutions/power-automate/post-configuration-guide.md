---
title: Power Automate post-configuration guide
url: https://documentation.cluedin.net/solutions/power-automate/post-configuration-guide
content_type: how-to
section: Solutions & integrations > Power Automate
---

# Power Automate post-configuration guide

> how-to: Steps to accomplish one task.

In this guide, you will learn how to verify that the CluedIn custom connector has been created successfully.

> **Important:** This guide is applicable to both public and private CluedIn instances.

Make sure that you have completed all of the actions described in [Power Automate configuration guide](https://documentation.cluedin.net/solutions/power-automate/configuration-guide.md).

**Prerequisites**

- You need to have the System Administrator security role in the Power Automate environment.

## Verify a custom connector

1. Open the Power Automate environment that you prepared during pre-configuration stage in [Configure an environment](https://documentation.cluedin.net/solutions/power-automate/pre-configuration-guide.md#configure-an-environment), and then select **Custom connectors**.

    Alternatively, you can use the following link, but make sure you provide your environment ID: `https://make.powerautomate.com/environments/<env-id>/connections/custom`.

    You should see a custom connector with CluedIn logo.

    ![The Custom connectors page in Power Automate, with the CluedIn connector highlighted](https://documentation.cluedin.net/assets/images/microsoft-integration/power-automate/custom-connector.png)

1. Open the custom connector and select **Edit**.

    ![The CluedIn custom connector Details tab, with Edit highlighted](https://documentation.cluedin.net/assets/images/microsoft-integration/power-automate/custom-connector-edit.png)

    Alternatively, hover over the custom connector and select **Edit**.

    ![The CluedIn connector row on the Custom connectors page, with the Edit pencil action highlighted](https://documentation.cluedin.net/assets/images/microsoft-integration/power-automate/custom-connector-edit-alt.png)

1. Go to the **Definition** tab.

1. Check the **Triggers** section. All items there should be marked with green checkboxes.

    ![The custom connector Definition tab, with all eight triggers in the Triggers section marked with green checkmarks](https://documentation.cluedin.net/assets/images/microsoft-integration/power-automate/custom-connector-definition.png)

    If you see green checkboxes for all items, it means that the custom connector has been configured successfully. Now, you can start [creating workflows](https://documentation.cluedin.net/govern/workflows/create-and-manage-workflows.md) in the **Workflow** module in CluedIn.

## Troubleshooting

This section includes the description of errors that might appear after configuring the custom connector as well as remediation steps.

### No custom connector

Place of error: Power Automate

If you do not see a custom CluedIn connector in your Power Automate environment, make sure you have the System Administrator security role in the Power Automate environment. If you have the required role and still see a blank page, do the following:

1. In CluedIn, go to **Administration** > **Settings**, and then scroll down to the **Workflows** section.

1. Select **Delete Custom Connector**.

1. Select **Register Custom Connector**.

1. Repeat the steps from the section [above](#verify-a-custom-connector) to verify that the connector has been created successfully.

1. If the issue has not been resolved, reach out to CluedIn support at [support@cluedin.com](mailto:support@cluedin.com).

### Failed triggers after registering a connector

Place of error: Power Automate

If some triggers on the **Definitions** tab do not have the green checkmark, register the connector again as described in the [previous](#no-custom-connector) section.

### Failed triggers after enabling a workflow

Place of error: CluedIn

After you [create](https://documentation.cluedin.net/govern/workflows/create-and-manage-workflows.md) a workflow in CluedIn, you need to enable it, and then check its **Properties** tab. If you see the following error, it means that the workflow is not running.

![The 28-day run history panel showing the error There is a problem with the flow trigger, with a Fix the trigger link](https://documentation.cluedin.net/assets/images/microsoft-integration/power-automate/failed-trigger.png)

To fix this error, register the connector again as described in the [previous](#no-custom-connector) section.

### Sign-in error: ID token not enabled

Place of error: CluedIn

In CluedIn, when you go to **Workflow** > **Workflow Builder** or **Workflow** > **Approvals** you may see an error similar to the following.

![A Microsoft Sign in pop-up over the CluedIn Approvals page, with error AADSTS700054: response_type id_token is not enabled for the application](https://documentation.cluedin.net/assets/images/microsoft-integration/power-automate/sign-in-error-no-id-token.png)

This error indicates that the service application that is used to authenticate the Power Automate widget in CluedIn does not have the platform configurated. To fix this, add a platform and a redirect URI as described in [Create a service application](https://documentation.cluedin.net/solutions/power-automate/pre-configuration-guide.md#create-a-service-application).

### Sign-in error: no reply address

Place of error: CluedIn

In CluedIn, when you go to **Workflow** > **Workflow Builder** or **Workflow** > **Approvals** you may see an error similar to the following.

![A Microsoft Sign in pop-up over the CluedIn Approvals page, reporting a sign-in error with troubleshooting details](https://documentation.cluedin.net/assets/images/microsoft-integration/power-automate/sign-in-error-redirect-uri.png)

This error indicates that the redirect URI in the service application that is used to authenticate the Power Automate widget in CluedIn is incorrect. To fix this, make sure the domain in the redirect URI matches your CluedIn application.

![The Configure single-page application pane in Azure, with the Redirect URI set to https://your-cluedin-domain/admin/workflow/workflow-builder](https://documentation.cluedin.net/assets/images/microsoft-integration/power-automate/configure-platforms-redirect-uri.png)

For more details, see [Create a service application](https://documentation.cluedin.net/solutions/power-automate/pre-configuration-guide.md#create-a-service-application).

## Next steps

Once you have verified that the CluedIn custom connector has been successfully configured, you can start [creating workflows](https://documentation.cluedin.net/govern/workflows/create-and-manage-workflows.md) in the **Workflow** module in CluedIn.

Up: [Power Automate](https://documentation.cluedin.net/solutions/power-automate.md)
