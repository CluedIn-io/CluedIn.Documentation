---
layout: cluedin
title: Work IQ
parent: Microsoft IQ
grand_parent: Solutions & integrations
nav_order: 30
permalink: /solutions/microsoft-iq/work-iq
content_type: how-to
---

## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

CluedIn publishes golden records into [Work IQ](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/work-iq) through a [Microsoft 365 Copilot connector](https://learn.microsoft.com/en-us/microsoft-365/copilot/connectors/overview). Microsoft 365 Copilot, Work IQ agents and Microsoft Search can then answer questions such as "What industry is Contoso in?" from your mastered data, alongside email, chats and documents.

Each golden record becomes one connector item. It has a title, a business domain, a description, a URL, a last-modified date and the CluedIn id, and its text content lists every vocabulary key and value.

## How publishing works

Microsoft takes 5 to 15 minutes to register a new connector's schema, so the first publish happens over two runs:

1. **First run:** creates the connector and starts registering its schema. The run reports that it's pending, and `isSchemaRegistrationPending` is `true`.
2. **Later run:** once Microsoft has finished, pushes the golden records. If registration is still in progress, the run reports that again and pushes nothing.

With a schedule enabled, this happens without you doing anything. Without one, publish again after about 15 minutes.

{: .important }
By default, everyone in your Microsoft 365 tenant can see the published items. CluedIn's access control policies are not carried over. To limit who can see them, set `aclGroupId` to a Microsoft Entra group.

## Before you start

Register an app in Microsoft Entra ID, create a client secret, and grant these **application** permissions on Microsoft Graph, with admin consent:

- `ExternalConnection.ReadWrite.OwnedBy`
- `ExternalItem.ReadWrite.OwnedBy`

Copilot connectors need Microsoft 365 Copilot or Microsoft Search licensing in the tenant.

## Configure

In **Administration** > **Azure Integration** > **Microsoft IQ**, select **Add connection** and choose the product. The fields below are the panel's fields, and also the request fields if you use the API.

| Field | Description |
|--|--|
| `tenantId`, `clientId`, `clientSecret` | The app registration. |
| `externalConnectionId` | The connector id: 3 to 32 letters and numbers, for example `cluedin`. |
| `externalConnectionName` | The connector's display name in Microsoft 365, for example `CluedIn golden records`. |
| `aclGroupId` | Optional: the object id of the Microsoft Entra group allowed to see the items. |
| `entityTypes`, `maxRecords` | What to publish. |

```http
POST https://<your CluedIn host>/api/api/microsoft-iq/connections
Authorization: Bearer <token>
Content-Type: application/json

{
  "name": "Work IQ",
  "product": "WorkIQ",
  "tenantId": "<tenant id>",
  "clientId": "<client id>",
  "clientSecret": "<client secret>",
  "externalConnectionId": "cluedin",
  "externalConnectionName": "CluedIn golden records",
  "entityTypes": ["/Organization"],
  "cronSchedule": "*/30 * * * *",
  "enabled": true
}
```

## Validate end to end

1. **Preview.** Send `POST /api/api/microsoft-iq/preview?sampleSize=1` with the body above, minus the secret. *Expected:* the connector, its schema and a sample item, for example:

   ```json
   {
     "id": "fbe8fe8e7ff855d6b461b7cf78129207",
     "acl": [ { "type": "everyone", "value": "<tenant id>", "accessType": "grant" } ],
     "properties": { "title": "Northwind Traders", "entityType": "/Organization", "cluedInId": "fbe8fe8e-7ff8-55d6-b461-b7cf78129207" },
     "content": { "value": "Northwind Traders\nBusiness domain: /Organization\norganization.industry: Wholesale\n...", "type": "text" }
   }
   ```

2. **Create the connection.** *Expected:* `201 Created`. A `400` names what's wrong: `Microsoft Entra ID rejected the service principal` for wrong credentials, or `listing Microsoft 365 Copilot connectors ... failed with HTTP 403` when the Graph permissions are missing.
3. **Publish.** Send `POST /api/api/microsoft-iq/connections/{id}/publish`. *Expected:* `lastResult` reads `Created connector 'cluedin' and started registering its schema; ...`.
4. **Publish again** after about 15 minutes. *Expected:* `lastResult` reads `Pushed <n> golden records to Microsoft 365 Copilot connector 'cluedin'.`
5. **Check in Microsoft 365.** In the Microsoft 365 admin center, go to **Copilot** > **Connectors**. *Expected:* the `CluedIn golden records` connector, with an item count. In Microsoft 365 Copilot, ask "What industry is Northwind Traders in, according to CluedIn?". *Expected:* an answer citing the CluedIn item. Microsoft can take a while to index new items.
