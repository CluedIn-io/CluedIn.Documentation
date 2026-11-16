---
layout: cluedin
title: Connect CluedIn to OneLake Catalog
parent: Microsoft Fabric
grand_parent: Solutions & integrations
nav_order: 50
permalink: /solutions/fabric/connect-onelake-catalog-to-cluedin
content_type: how-to
---

## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

In this article, you will learn how to connect CluedIn to Microsoft Fabric's OneLake Catalog, so you can search and browse Workspaces and Items across your Fabric tenant - including each item's connections, shortcuts and tags - through CluedIn's REST API.

## Prerequisites

To connect CluedIn to OneLake Catalog, you need:

- A Microsoft Entra ID app registration (service principal) with a client secret, added as a member or contributor on the Fabric workspace(s) you want to search or browse.
- An active CluedIn API token. You can create one in CluedIn in **Administration** > **API tokens**.

## Inputs

| Field | Required | Description |
|---|---|---|
| `Name` | No | A friendly name for the connection. Defaults to `OneLake Catalog (<tenant ID>)`. |
| `TenantId` | Yes | The Microsoft Entra ID tenant ID. |
| `ClientId` | Yes | The app registration's (service principal's) client ID. |
| `ClientSecret` | Yes | The app registration's client secret. Never returned back by the API once saved. |

## Create a OneLake Catalog connection

**To create a OneLake Catalog connection**

1. Call the create-connection endpoint with your service principal's credentials.

    ```
    POST /api/onelakecatalog/connections
    Authorization: Bearer <your CluedIn API token>
    Content-Type: application/json

    {
      "name": "My OneLake Catalog connection",
      "tenantId": "<tenant ID>",
      "clientId": "<client ID>",
      "clientSecret": "<client secret>"
    }
    ```

    CluedIn validates the credentials against OneLake Catalog before saving them. If they can't authenticate, or the service principal has no accessible workspace, the request fails with `400 Bad Request` and the connection is not saved.

1. On success, CluedIn returns `201 Created` with the connection's ID, which you use in the operations below.

    ```json
    {
      "id": "<connection ID>",
      "name": "My OneLake Catalog connection",
      "tenantId": "<tenant ID>",
      "clientId": "<client ID>"
    }
    ```

## Verify the result

Call the search endpoint to confirm the connection works end to end:

```
POST /api/onelakecatalog/connections/<connection ID>/search
Authorization: Bearer <your CluedIn API token>
Content-Type: application/json

{
  "search": "sales",
  "pageSize": 10
}
```

A successful call returns `200 OK` with the matching catalog entries (items and workspaces) your service principal can see.

## Supported operations

Once a connection exists, CluedIn exposes every currently-documented [OneLake Catalog REST API](https://learn.microsoft.com/en-us/rest/api/fabric/articles/onelakecatalog/overview) operation through it:

| Operation | Endpoint |
|---|---|
| Search the catalog | `POST /api/onelakecatalog/connections/{id}/search` |
| Browse Workspaces and Items | `GET /api/onelakecatalog/connections/{id}/browse` |
| Get an item's metadata and tags | `GET /api/onelakecatalog/connections/{id}/workspaces/{workspaceId}/items/{itemId}` |
| List an item's connections | `GET /api/onelakecatalog/connections/{id}/workspaces/{workspaceId}/items/{itemId}/connections` |
| List an item's shortcuts | `GET /api/onelakecatalog/connections/{id}/workspaces/{workspaceId}/items/{itemId}/shortcuts` |
| List the tenant's tags | `GET /api/onelakecatalog/connections/{id}/tags` |
| Apply tags to an item | `POST /api/onelakecatalog/connections/{id}/workspaces/{workspaceId}/items/{itemId}/tags` |
| Remove tags from an item | `DELETE /api/onelakecatalog/connections/{id}/workspaces/{workspaceId}/items/{itemId}/tags` |

{: .note }
OneLake Catalog is a metadata-discovery API: these operations find and describe Fabric items, but don't move their underlying data. To bring Fabric table data into CluedIn, use the [Microsoft Fabric](/solutions/fabric/connect-fabric-to-cluedin) connection instead.

## What this changes

Creating a connection only stores its credentials in CluedIn; it doesn't change any data in Fabric or CluedIn by itself. Calling an operation above reads live from OneLake Catalog - nothing is cached, and none of these operations write to Fabric, except Apply tags and Remove tags, which add or remove tags on the Fabric item you target.

## If something goes wrong

| Problem | What to do |
|---|---|
| `400 Bad Request` when creating or updating a connection | The tenant ID, client ID or client secret are incorrect, or the service principal has no workspace it can access. Double-check the app registration and its workspace role assignments. |
| `404 Not Found` on any operation | The connection ID doesn't exist for your organization, or (for item-level operations) the workspace or item ID is wrong. |
| `403`-style authentication errors in the response body | The service principal's credentials are valid, but it lacks permission for that specific workspace or item. Grant it the Fabric role the operation needs - see the [OneLake Catalog REST API](https://learn.microsoft.com/en-us/rest/api/fabric/articles/onelakecatalog/overview) for required scopes. |
