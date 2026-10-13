---
title: Power Apps pre-configuration guide
url: https://documentation.cluedin.net/solutions/power-apps/pre-configuration-guide
content_type: how-to
section: Solutions & integrations > Power Apps
---

# Power Apps pre-configuration guide

> how-to: Steps to accomplish one task.

In this guide, you will learn how to prepare for configuring Power Apps integration in CluedIn. The instructions in this guide apply to both public and private CluedIn instances, as Power Apps is hosted in your environment.

## Set up a firewall policy

To enable CluedIn to call Power Apps, you need to add specific rules to your Azure Firewall as described in the [Firewall guide](https://documentation.cluedin.net/operate/configuration/configure-firewall.md#power-apps-and-power-automate).

Power Apps integration also involves Power Automate, which is used for data ingestion workflow to push data from Dataverse to CluedIn. That's why you need to add firewall rules both for Power Automate and Power Apps.

## Pre-configuration steps in Microsoft Entra ID

To manage all transactions between CluedIn and Dataverse, you need to register a new application in Microsoft Entra ID.  When you register a new application, a service principal is automatically created for the app registration. Following the steps in this section will provide you with the **Client ID**, **Tenant ID**, and **Client Secret** required to configure Power Apps integration in CluedIn.

For more information, see [Register an application in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app?tabs=certificate%2Cexpose-a-web-api).

### Register a new application

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com/) as at least an Application Developer role.

2. If you have access to multiple tenants, switch to the tenant in which you want to register the application.

3. Go to **Identity** > **Applications** > **App registrations**, and then select **New registration**.

    ![App registrations page in the Microsoft Entra admin center with the New registration button highlighted](https://documentation.cluedin.net/assets/images/microsoft-integration/power-apps/new-registration.png)

4.  Enter a **Name** for your application.

5.  Under **Supported account types**, specify who can use the application (**Accounts in this organizational directory only**).

    ![Register an application page with the name PowerApps_CluedIn and Accounts in this organizational directory only selected](https://documentation.cluedin.net/assets/images/microsoft-integration/power-apps/new-registration-name.png)

1. Select **Register**.

    On the application's **Overview** page, you can find the **Application (client) ID** and **Directory (tenant) ID** that you will need to configure Power Apps integration in CluedIn as described in [Power Apps configuration guide](https://documentation.cluedin.net/solutions/power-apps/configuration-guide.md).

    ![Overview page of the PowerApps_CluedIn app registration with the Application (client) ID and Directory (tenant) ID highlighted](https://documentation.cluedin.net/assets/images/microsoft-integration/power-apps/app-overview.png)

### Create a client secret

1. In the [Microsoft Entra admin center](https://entra.microsoft.com/), in **App registrations**, select your newly created application.

1. Go to **Certificates & secrets** > **Client secrets** > **New client secret**.

    ![Certificates and secrets page, Client secrets tab, with the New client secret button highlighted](https://documentation.cluedin.net/assets/images/microsoft-integration/power-apps/client-secret.png)

1. Add a description for your client secret. Select an expiration for the secret or specify a custom lifetime. Finally, select **Add**.

    ![Add a client secret pane with the description PowerAppsCluedInSecret and the recommended 180-day expiry, and the Add button](https://documentation.cluedin.net/assets/images/microsoft-integration/power-apps/add-a-client-secret.png)

1. Record the **Value** of the client secret. You will need it to configure Power Apps integration in CluedIn as described in [Power Apps configuration guide](https://documentation.cluedin.net/solutions/power-apps/configuration-guide.md). This secret value is never displayed again after you leave this page.

    ![Client secrets tab showing the new PowerAppsCluedInSecret with its Value highlighted and copied](https://documentation.cluedin.net/assets/images/microsoft-integration/power-apps/copy-client-secret.png)

## Pre-configuration steps in Power Apps

In order to manage your master data from CluedIn directly in Power Apps Dataverse tables, you need to prepare a Power Apps environment. This involves creating a new security role and a new application user. These will be used to grant access to the Power Apps environment to the application that you created in [Pre-configuration steps in Microsoft Entra ID](#pre-configuration-steps-in-microsoft-entra-id).

**Prerequisites**

- You need to have an environment in the [Power Platform admin center](https://admin.powerplatform.microsoft.com/) with Dataverse as a data store.

- You need to have the System Administrator access to the Power Platform of your organization.

### Find your environment ID

1. Sign in to the [Power Platform admin center](https://admin.powerplatform.microsoft.com/).

1. On the navigation pane, select **Environments**, and then select your intended environment.

1. Find the environment ID in the **Details** section.

    ![Power Platform environment Details section with the Environment ID highlighted](https://documentation.cluedin.net/assets/images/microsoft-integration/power-apps/env-id.png)

    The environment ID is needed to configure Power Apps integration in CluedIn as described in [Power Apps configuration guide](https://documentation.cluedin.net/solutions/power-apps/configuration-guide.md).

### Create a new security role

1. Sign in to the [Power Platform admin center](https://admin.powerplatform.microsoft.com/).

1. On the navigation pane, select **Environments**, and then select your intended environment.

1. Select **Settings** > **Users + permissions** > **Security roles**.

1. Select **+ New role**.

1. Enter the role name and then select the business unit.

1. In **Member's privilege inheritance**, select **Direct User (Basic) access level and Team privileges**.

    You must add the **System Customizer** role to Service Principal. This role is required for the Service Principal to automatically access tables created by the PowerApps component or the Dataverse connector.

    ![Create New Role pane with the role name PowerAppsCluedInRole, a business unit, member privilege inheritance, and the Save button](https://documentation.cluedin.net/assets/images/microsoft-integration/power-apps/create-security-role.png)

1. Select **Save**.

1. Grant your app's table privileges to the newly created security role according to the [reference table](#security-role-reference-table). To open the edit mode, select the three-dot button next to the table that you want to edit.

1. Once you’ve updated the security role’s privileges according to the reference table, select **Save**.

### Security role reference table

<table>
  <thead>
    <tr>
      <th>Table</th>
      <th>Create</th>
      <th>Read</th>
      <th>Write</th>
      <th>Delete</th>
      <th>Append to</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="6"><em>Customization</em></td>
    </tr>
    <tr>
      <td>Solution</td>
      <td>Organization</td>
      <td>Organization</td>
      <td>Organization</td>
      <td>Organization</td>
      <td></td>
    </tr>
    <tr>
      <td>Publisher</td>
      <td>Organization</td>
      <td>Organization</td>
      <td>Organization</td>
      <td>Organization</td>
      <td></td>
    </tr>
    <tr>
      <td>Entity</td>
      <td>Organization</td>
      <td>Organization</td>
      <td>Organization</td>
      <td>Organization</td>
      <td></td>
    </tr>
    <tr>
      <td>Entity Key</td>
      <td>Organization</td>
      <td>Organization</td>
      <td></td>
      <td>Organization</td>
      <td></td>
    </tr>
    <tr>
      <td>Attribute</td>
      <td>Organization</td>
      <td>Organization</td>
      <td>Organization</td>
      <td>Organization</td>
      <td></td>
    </tr>
    <tr>
      <td>System Form</td>
      <td>Organization</td>
      <td>Organization</td>
      <td>Organization</td>
      <td>Organization</td>
      <td></td>
    </tr>
    <tr>
      <td>View</td>
      <td>Organization</td>
      <td>Organization</td>
      <td>Organization</td>
      <td>Organization</td>
      <td></td>
    </tr>
    <tr>
      <td>Custom Control Default Config</td>
      <td>Organization</td>
      <td></td>
      <td>Organization</td>
      <td>Organization</td>
      <td></td>
    </tr>
    <tr>
      <td>Process</td>
      <td>Organization</td>
      <td>Organization</td>
      <td>Organization</td>
      <td>Organization</td>
      <td></td>
    </tr>
    <tr>
      <td>Relationship Entity</td>
      <td>Organization</td>
      <td>Organization</td>
      <td>Organization</td>
      <td>Organization</td>
      <td></td>
    </tr>
    <tr>
      <td colspan="6"><em>Custom tables</em></td>
    </tr>
    <tr>
      <td>Connection Reference</td>
      <td>Organization</td>
      <td>Organization</td>
      <td>Organization</td>
      <td>Organization</td>
      <td></td>
    </tr>
    <tr>
      <td>Connector</td>
      <td>Organization</td>
      <td>Organization</td>
      <td>Organization</td>
      <td>Organization</td>
      <td></td>
    </tr>
    <tr>
      <td>Dataflow</td>
      <td>Organization</td>
      <td>Organization</td>
      <td>Organization</td>
      <td>Organization</td>
      <td></td>
    </tr>
    <tr>
      <td>OptionSet</td>
      <td>Organization</td>
      <td>Organization</td>
      <td>Organization</td>
      <td>Organization</td>
      <td>Organization</td>
    </tr>
  </tbody>
</table>

### Create a new application user

1. Sign in to the [Power Platform admin center](https://admin.powerplatform.microsoft.com/).

1. On the navigation pane, select **Environments**, and then select your intended environment.

1. Select **Settings** > **Users + permissions** > **Application users**.

1. Select **+ New app user**.

1. In the **App** field, select **Add an app**, and then find and select the application that you created before in [Register a new application](#register-a-new-application).

    ![Add an app from Microsoft Entra ID pane with the PowerApps_CluedIn app selected, and the Add button](https://documentation.cluedin.net/assets/images/microsoft-integration/power-apps/create-new-app-user-add-app.png)

1. Enter the **Business unit**.

2. In the **Security roles** field, select the pencil icon, and then enter the security role that you created before in [Create a new security role](#create-a-new-security-role).

3. Select **Create**.

    ![Create a new app user pane with app PowerApps_CluedIn, a business unit, and the security role PowerAppsCluedInRole, and the Create button](https://documentation.cluedin.net/assets/images/microsoft-integration/power-apps/create-new-app-user.png)

### Create a Dataverse connection

To enable communication between Dataverse tables and CluedIn and to automate the creation of workflows for ingesting the data from Dataverse to CluedIn, you need to manually create a Dataverse connection and share it with the application user.

> **Important:** The workflows in Power Apps integration are different in terms of configuration from the **Workflows** module in CluedIn. For more information, see [Power Automate integration](https://documentation.cluedin.net/solutions/power-automate.md).

**To create a new connection**

1. Sign in to [make.powerapps.com](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).

1. On the left navigation pane, select **Connections**.

1. Select **+ New connection**.

1. Find the Dataverse connection and select the one with the green icon.

    ![New connection list with the Microsoft Dataverse connection that has the green icon highlighted](https://documentation.cluedin.net/assets/images/microsoft-integration/power-apps/dataverse-connection-select.png)

1. Select **Create**.

    ![Microsoft Dataverse connection dialog with the Create button highlighted](https://documentation.cluedin.net/assets/images/microsoft-integration/power-apps/data-verse-connection.png)

    The new connector appears under **Connections**.

1. Open the newly added Dataverse connection, and then select **Share**.

1. Find and select the application user that you created in [Create a new application user](#create-a-new-application-user). Grant the following permissions to the application user: **Can use** or **Can edit**. Then, select **Save**. 

    ![Share Dataverse dialog with the PowerApps_CluedIn application user given the Can edit permission](https://documentation.cluedin.net/assets/images/microsoft-integration/power-apps/share-dataverse.png)

You will need the ID of Dataverse connection to configure Power Apps integration in CluedIn as described in [Power Apps configuration guide](https://documentation.cluedin.net/solutions/power-apps/configuration-guide.md). To find the connection ID, open the connection and look for ID in the URL field.

![Dataverse connection details page in Power Apps, with the connection ID highlighted at the end of the browser URL](https://documentation.cluedin.net/assets/images/microsoft-integration/power-apps/dataverse-connector-id.png)

## Next steps

Now that you have completed all pre-configuration steps, start the configuration of Power Apps in CluedIn using our [Power Apps configuration guide](https://documentation.cluedin.net/solutions/power-apps/configuration-guide.md).

Up: [Power Apps](https://documentation.cluedin.net/solutions/power-apps.md)
