---
layout: cluedin
title: Foundry IQ
parent: Microsoft IQ
grand_parent: Solutions & integrations
nav_order: 20
permalink: /solutions/microsoft-iq/foundry-iq
content_type: how-to
---

## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

CluedIn publishes golden records into [Foundry IQ](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/what-is-foundry-iq) (Azure AI Search). Foundry agents, Copilot Studio agents and any app using the knowledge base retrieve API can then ground answers on your mastered data, with citations back to each golden record.

Each publish:

1. Creates or updates a search **index** that CluedIn owns. There's one document per golden record, with its name, business domain and description, and a `content` field that lists every vocabulary key and value as text. New vocabulary keys therefore never need an index schema change. The index has a semantic configuration, which agentic retrieval needs.
2. Uploads the golden records with `mergeOrUpload`, in batches of 500.
3. Creates or updates a **search index knowledge source** over the index.
4. Creates the **knowledge base** if it doesn't exist. It's model-free (minimal reasoning effort, extractive output), so it works without an LLM deployment, and you can add a model to it later in Microsoft Foundry. An existing knowledge base is never changed, because it can hold sources and model connections someone added in Foundry. If it doesn't use CluedIn's knowledge source yet, add the source to it in Foundry.

## Before you start

You need a Foundry IQ (Azure AI Search) service in a [region that supports agentic retrieval](https://learn.microsoft.com/en-us/azure/search/search-region-support), on the Basic tier or higher, with the **semantic ranker** turned on. Choose one way to authenticate:

- **An admin API key** for the search service, or
- **A Microsoft Entra ID app registration** with the **Search Service Contributor** and **Search Index Data Contributor** roles on the search service, and role-based access turned on for the service.

## Configure

| Field | Description |
|--|--|
| `searchEndpoint` | The search service endpoint, for example `https://my-service.search.windows.net`. Only Azure AI Search endpoints are accepted. |
| `searchApiKey` | An admin API key. Leave it out to authenticate with `tenantId`, `clientId` and `clientSecret` instead. |
| `indexName` | The index CluedIn creates and owns, for example `cluedin-golden-records`. |
| `knowledgeSourceName` | The knowledge source CluedIn creates over the index. |
| `knowledgeBaseName` | The knowledge base agents connect to. |
| `entityTypes`, `maxRecords` | What to publish. |

Index, knowledge source and knowledge base names use lowercase letters, digits and dashes.

```http
POST https://<your CluedIn host>/api/api/microsoft-iq/connections
Authorization: Bearer <token>
Content-Type: application/json

{
  "name": "Foundry IQ",
  "product": "FoundryIQ",
  "searchEndpoint": "https://my-service.search.windows.net",
  "searchApiKey": "<admin key>",
  "indexName": "cluedin-golden-records",
  "knowledgeSourceName": "cluedin-golden-records-ks",
  "knowledgeBaseName": "cluedin-kb",
  "entityTypes": ["/Organization"],
  "cronSchedule": "0 * * * *",
  "enabled": true
}
```

## Validate end to end

1. **Preview.** Send `POST /api/api/microsoft-iq/preview?sampleSize=1` with the body above, minus the secrets. *Expected:* the index, knowledge source and knowledge base definitions, and one sample document such as:

   ```json
   {
     "@search.action": "mergeOrUpload",
     "id": "fbe8fe8e7ff855d6b461b7cf78129207",
     "name": "Northwind Traders",
     "entityType": "/Organization",
     "content": "Northwind Traders\nBusiness domain: /Organization\norganization.industry: Wholesale\norganization.website: http://northwindtraders.com/about\n"
   }
   ```

2. **Create the connection.** *Expected:* `201 Created`. A `400` names what's wrong, for example `Foundry IQ: listing indexes failed with HTTP 403` when the key or roles are missing.
3. **Publish.** Send `POST /api/api/microsoft-iq/connections/{id}/publish`. *Expected:* `lastResult` reads `Uploaded <n> golden records to index 'cluedin-golden-records'; created knowledge base 'cluedin-kb' over knowledge source 'cluedin-golden-records-ks'.`
4. **Retrieve.** Query the knowledge base:

   ```http
   POST https://my-service.search.windows.net/knowledgebases('cluedin-kb')/retrieve?api-version=2026-10-01
   api-key: <query or admin key>
   Content-Type: application/json

   {
     "intents": [ { "type": "semantic", "search": "Which industry is Northwind Traders in?" } ],
     "retrievalReasoningEffort": { "kind": "minimal" },
     "outputMode": "extractiveData"
   }
   ```

   *Expected:* a reference to the Northwind Traders document whose content includes `organization.industry: Wholesale`.
5. **Connect an agent.** In Microsoft Foundry, add the `cluedin-kb` knowledge base to an agent and ask it the same question. *Expected:* the answer cites the CluedIn golden record.
