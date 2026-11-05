---
title: Connect CluedIn to OneLake Catalog
url: https://documentation.cluedin.net/solutions/fabric/connect-to-onelake-catalog
content_type: how-to
section: Solutions & integrations > Microsoft Fabric
---

# Connect CluedIn to OneLake Catalog

> how-to: Steps to accomplish one task.

This guide describes the information you need to connect CluedIn to the OneLake Catalog in Microsoft Fabric. OneLake Catalog is the Fabric experience for discovering and governing Fabric items. The connection pattern is similar to CluedIn's Microsoft Purview integration: CluedIn authenticates as an application and uses the granted permissions to access catalog metadata.

> **Implementation note:** Confirm that your CluedIn release exposes a OneLake Catalog integration and the settings described below before configuring the connection. Do not reuse the Purview endpoint or credentials unless the CluedIn integration specifically requests them.

## Prerequisites

Before you begin, ensure that you have:

- A Microsoft Fabric tenant with OneLake Catalog enabled and at least one workspace and item available.
- Administrator access to the CluedIn organization settings.
- Permission to create or configure a Microsoft Entra ID app registration, or an existing app registration dedicated to CluedIn.
- A Fabric administrator who can enable service-principal access for the tenant and grant the app access to the target workspace or items.
- A documented list of workspaces and catalog metadata that CluedIn should be able to discover.

## Configure Microsoft Entra ID access

Use a dedicated service principal for the integration. This follows the same identity model as the Purview connection, while Fabric access is granted through Fabric tenant and workspace permissions.

1. In Microsoft Entra admin center, create an app registration (or select the approved CluedIn integration app).
2. Record the **Application (client) ID** and **Directory (tenant) ID**.
3. Create a client secret or certificate and securely record its value. If you use a secret, note its expiry and rotation owner.
4. Ask a Fabric administrator to enable service-principal API access for the app's security group in Fabric tenant settings, if required by your tenant policy.
5. Add the service principal to each target Fabric workspace and grant the least-privileged role that supports the catalog operations required by your CluedIn integration. Use **Contributor** only if the integration needs to create or modify workspace items; read-only discovery should use a read role where supported.
6. Confirm that the service principal can see the intended workspaces and items in Fabric.

For details about registering an application, see [Microsoft Entra app registration documentation](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app). For service-principal tenant settings, see [Fabric developer settings](https://learn.microsoft.com/en-us/fabric/admin/service-principal-tenant-setting). For workspace access, see [Fabric roles](https://learn.microsoft.com/en-us/fabric/get-started/roles-workspaces).

## Configure the connection in CluedIn

When the OneLake Catalog integration is available in your CluedIn deployment:

1. In CluedIn, open **Administration** > **Azure Integration** and select the OneLake Catalog or Microsoft Fabric integration.
2. Enter the values requested by the integration. These commonly include:
   - **Tenant ID** – the Entra directory ID.
   - **Client ID** – the app registration's application ID.
   - **Client Secret** or certificate – the credential created for the app registration.
   - **Workspace scope** – the workspace ID or IDs to include, if the integration supports scoping.
   - **Catalog endpoint or base URL** – use the value shown in the CluedIn integration settings or supplied by CluedIn support. Do not substitute a Purview URL.
3. Save the settings and use the integration's connection or validation action, if available.
4. Select the catalog synchronization options that match your use case. Start with read-only discovery and metadata synchronization; enable write-back only when your CluedIn version explicitly supports it and the business owner has approved it.

The exact fields, endpoint, synchronization features, and minimum Fabric role can vary by CluedIn release. Use the fields displayed in your deployment as authoritative.

## Validate the connection

1. In Fabric, confirm that the app registration has access to a target workspace and its items.
2. In CluedIn, run the connection test or start a catalog refresh, if those actions are available.
3. Confirm that the expected workspaces, Lakehouses, Warehouses, and other supported items appear in CluedIn.
4. Compare item names and workspace ownership with Fabric. Verify that the integration has not included workspaces outside the approved scope.
5. If synchronization is supported, update a non-production test item and confirm the expected metadata change appears in the other system.

## Troubleshooting

- **Authentication fails:** Check that the tenant ID and client ID belong to the same app registration, the secret is the secret *value* (not its identifier), and the credential has not expired.
- **No workspaces or items appear:** Verify that the Fabric tenant setting allows the service principal and that it has access to the target workspace.
- **Only some items appear:** Check workspace membership, item-level access, and the integration's configured workspace scope.
- **Access denied:** Review Fabric tenant settings and workspace roles with a Fabric administrator. Avoid granting broad tenant permissions as a diagnostic shortcut.
- **Connection fields differ from this guide:** Follow the fields shown by your CluedIn release and confirm endpoint and permission requirements with CluedIn support before entering credentials.

## Security recommendations

- Use a dedicated application identity and limit it to approved Fabric workspaces.
- Store and rotate credentials according to your organization's secrets policy.
- Grant only the access required for the configured operations.
- Review the integration's workspace scope and audit access periodically.

Up: [Microsoft Fabric](https://documentation.cluedin.net/solutions/fabric.md)
