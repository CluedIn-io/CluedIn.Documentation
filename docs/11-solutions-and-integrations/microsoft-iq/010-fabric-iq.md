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

| CluedIn | Fabric IQ ontology |
|--|--|
| Business domain (entity type), for example `/Organization` | Entity type `Organization`, keyed on `CluedInId` |
| Vocabulary keys of the business domain | Properties, typed from the vocabulary key data type (`int64`, `double`, `boolean`, `dateTime` or `string`) |
| Global data model relationship, for example `/WorksFor` | Entity relationship `User_WorksFor_Organization` |

The ontology is written in the Fabric IQ generation 2 (TMDL) definition format. Entity types are *ontology-first*: they aren't bound to tables, so an ontology editor can later bind them to the Lakehouse tables CluedIn exports golden records to. Every element carries a stable lineage tag derived from its CluedIn key, so publishing again updates the ontology in place, even after a business domain is renamed.

{: .note }
Fabric IQ ontologies are in preview in Microsoft Fabric.

## Before you start

Fabric IQ reuses an existing **Microsoft Fabric connection** - the one Ingest uses to browse Lakehouses - and needs no credentials of its own. If you don't have one, create it first under **Administration** > **Azure Integration** > **Microsoft Fabric Connections**.

The connection's service principal needs:

- The **Contributor** role (or higher) on the workspace that holds the ontology.
- A workspace on a Fabric capacity that supports ontologies.
- The tenant setting **Service principals can use Fabric APIs** turned on.

## Configure

In **Administration** > **Azure Integration** > **Microsoft IQ**, select **Add connection** and choose the product. The fields below are the panel's fields, and also the request fields if you use the API.

| Field | Description |
|--|--|
| `fabricConnectionId` | The id of the Microsoft Fabric connection to reuse. |
| `workspaceId` | The id of the Fabric workspace for the ontology. It's the GUID in the workspace URL. |
| `ontologyName` | The ontology item name. It must start with a letter and contain only letters, numbers and underscores. |
| `entityTypes` | Optional: the business domains to include. Empty includes the whole global data model. |

```http
POST https://<your CluedIn host>/api/api/microsoft-iq/connections
Authorization: Bearer <token>
Content-Type: application/json

{
  "name": "Fabric IQ ontology",
  "product": "FabricIQ",
  "fabricConnectionId": "<Microsoft Fabric connection id>",
  "workspaceId": "<workspace id>",
  "ontologyName": "CluedIn_Model",
  "cronSchedule": "0 3 * * *",
  "enabled": true
}
```

The first publish creates the ontology. Later publishes update its definition.

## Validate end to end

1. **Preview the ontology.** Send `POST /api/api/microsoft-iq/preview` with `{"product": "FabricIQ", "ontologyName": "CluedIn_Model"}`.

   *Expected:* one `entities/<Name>.tmdl` part per business domain in the global data model, each with `keyProperty: CluedInId` and one property per vocabulary key, plus an `entityRelationships.tmdl` part with one `entityRelationship` per global data model relationship. For example:

   ```tmdl
   /// CluedIn business domain /Organization (Organization).
   entity Organization
   	lineageTag: 0d6b7f8e-...
   	keyProperty: CluedInId
   	annotation CluedInEntityType = /Organization

   	/// Website
   	property organization_website
   		dataType: string
   		lineageTag: 6c1a2f0b-...
   		annotation CluedInVocabularyKey = organization.website
   ```

2. **Create the connection** as shown above. *Expected:* `201 Created`. A `400` names what's wrong, for example a missing Microsoft Fabric connection or a workspace the service principal can't read.
3. **Publish.** Send `POST /api/api/microsoft-iq/connections/{id}/publish`. *Expected:* `lastResult` reads `Created ontology 'CluedIn_Model' (<item id>) with <n> entity types and relationships.`, and `ontologyId` is set.
4. **Check in Fabric.** Open the workspace. *Expected:* an ontology item named `CluedIn_Model` whose entity types and relationships match the CluedIn global data model.
5. **Publish again** after adding a vocabulary key to a business domain. *Expected:* `lastResult` reads `Updated ontology ...` and the new property appears on the existing entity type.
