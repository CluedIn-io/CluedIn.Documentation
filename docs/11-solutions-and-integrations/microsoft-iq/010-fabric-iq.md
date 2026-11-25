---
layout: cluedin
title: Fabric IQ
parent: Microsoft IQ
grand_parent: Solutions & integrations
nav_order: 10
permalink: /solutions/microsoft-iq/fabric-iq
content_type: how-to
---

## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

CluedIn publishes its [global data model](/model/global-data-model) as a [Fabric IQ ontology](https://learn.microsoft.com/en-us/fabric/iq/ontology/overview). Fabric data agents, the Fabric IQ ontology MCP server and Foundry IQ's Fabric ontology knowledge source can then reason over your mastered business domains and how they relate.

A Fabric IQ connection runs the same sync as **Sync with Microsoft Fabric Ontology** on the **Global Data Model** page. It writes to the same ontology item, `CluedIn_Global_Data_Model_Ontology`, and both places show the same sync status. Use whichever suits you: the Microsoft IQ connection keeps all of your Microsoft IQ targets in one list, with its own publish schedule.

| CluedIn | Fabric IQ ontology |
|--|--|
| Business domain (entity type), for example `/Organization` | Entity type, with its record count, icon, workflow involvement and data quality scores as custom attributes |
| Vocabulary keys of the business domain | Properties, typed from the vocabulary key data type |
| Global data model relationship, for example `/WorksFor` | Relationship type, with its relationship count |

The ontology always covers the whole global data model. Publishing again updates the existing ontology instead of creating another one.

{: .note }
Fabric IQ ontologies are in preview in Microsoft Fabric.

## Before you start

Fabric IQ reuses an existing **Microsoft Fabric connection** and needs no credentials of its own. If you don't have one, create it first under **Administration** > **Azure Integration** > **Microsoft Fabric Connections**.

The connection's service principal needs:

- The **Contributor** role (or higher) on the workspace that holds the ontology.
- A workspace on a Fabric capacity that supports ontologies.
- The tenant setting **Service principals can use Fabric APIs** turned on.

## Configure

In **Administration** > **Azure Integration** > **Microsoft IQ**, select **Add connection** and choose **Fabric IQ**. The fields below are the panel's fields, and also the request fields if you use the API.

| Field | Description |
|--|--|
| `fabricConnectionId` | The Microsoft Fabric connection to reuse. |
| `workspaceId` | The id of the Fabric workspace for the ontology. It's the GUID in the workspace URL. |

```http
POST https://<your CluedIn host>/api/api/microsoft-iq/connections
Authorization: Bearer <token>
Content-Type: application/json

{
  "name": "Fabric IQ ontology",
  "product": "FabricIQ",
  "fabricConnectionId": "<Microsoft Fabric connection id>",
  "workspaceId": "<workspace id>",
  "cronSchedule": "0 3 * * *",
  "enabled": true
}
```

## Validate end to end

1. **Preview the ontology.** In the connection panel select **Preview**, or send `POST /api/api/microsoft-iq/preview` with `{"product": "FabricIQ"}`. *Expected:* `ontologyName` is `CluedIn_Global_Data_Model_Ontology`, with one `EntityTypes/<id>/definition.json` part per business domain and one `RelationshipTypes/<id>/definition.json` part per relationship. For example:

   ```json
   {
     "namespace": "usertypes",
     "name": "Organization",
     "semanticEnrichment": {
       "customAttributes": { "RecordCount": "5", "Icon": "Organization", "DataQuality.accuracy": "100%" }
     }
   }
   ```

2. **Create the connection.** *Expected:* the connection appears in the list. If it's rejected, the reason appears next to the button, for example a missing Microsoft Fabric connection or a workspace the service principal can't read.
3. **Publish.** Select **Publish now** on the connection. *Expected:* **Last result** reads `Synced the global data model to Fabric ontology 'CluedIn_Global_Data_Model_Ontology' (<item id>): <n> entity types and <m> relationship types.`
4. **Check in Fabric.** Open the workspace. *Expected:* an ontology item named `CluedIn_Global_Data_Model_Ontology` whose entity types and relationships match the CluedIn global data model. The **Global Data Model** page shows the same last sync time.
5. **Publish again** after adding a vocabulary key to a business domain. *Expected:* the existing ontology is updated, and the new property appears on its entity type.
