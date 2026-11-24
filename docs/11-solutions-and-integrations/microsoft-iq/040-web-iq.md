---
layout: cluedin
title: Web IQ
parent: Microsoft IQ
grand_parent: Solutions & integrations
nav_order: 40
permalink: /solutions/microsoft-iq/web-iq
content_type: how-to
---

## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

[Web IQ](https://learn.microsoft.com/en-us/web-iq/) grounds AI agents on fresh information from the public web. You can't push private data into the public web, so CluedIn integrates with Web IQ in two ways:

- **Scopes:** CluedIn publishes the websites held on golden records as a named Web IQ [scope](https://learn.microsoft.com/en-us/web-iq/guides/create-scopes). For example, publish every mastered supplier's website as `CluedIn.Suppliers`. Then a Web IQ search, an Auto request or a Web IQ MCP tool call that passes `scopeName: "CluedIn.Suppliers"` grounds only on your suppliers' own sites, and the list follows your master data as suppliers are added or removed.
- **Copilot web search:** CluedIn Copilot and AI agents search the web through Web IQ. See [Copilot web search through Web IQ](/solutions/microsoft-iq#copilot-web-search-through-web-iq).

## How the scope is built

For each golden record, CluedIn reads the vocabulary keys you name in `siteVocabularyKeys` and turns each website into a domain selector:

| Golden record value | Scope selector |
|--|--|
| `https://www.contoso.com` | `contoso.com` (covers `contoso.com` and all of its subdomains) |
| `http://northwindtraders.com/about` | `northwindtraders.com` |
| `adventure-works.com; adventureworks.co.uk` | `adventure-works.com` and `adventureworks.co.uk` |
| `n/a`, `localhost`, a URL with a port | Skipped, and counted in `rejectedValues` |

Each publish replaces the scope's include list. An exclude list added in the Web IQ portal is kept. CluedIn refuses to publish an empty include list, because Web IQ treats an empty list as "every site". A scope holds at most 10,000 sites.

{: .note }
Web IQ takes 10 to 30 minutes to apply a new or changed scope to searches.

## Before you start

- A Web IQ billing account. In the Web IQ portal, go to **Account settings** > **Management API access** and grant a Microsoft Entra app registration access to the account (the `CustomerApiAccess` role). This grant is separate from search API keys.
- Optional, to verify the scope with a real search: a Web IQ API key from [Profile Management](https://webiq.microsoft.ai/profiles).

## Configure

| Field | Description |
|--|--|
| `tenantId`, `clientId`, `clientSecret` | The app registration that has management access. |
| `billingAccountId` | The Web IQ billing account that owns the scope. |
| `scopeName` | The scope name: up to 128 ASCII letters, digits, `.`, `_` or `-`. |
| `siteVocabularyKeys` | The vocabulary keys holding websites, for example `["organization.website"]`. |
| `webIqApiKey` | Optional: a Web IQ runtime API key, used only by the verification search. |
| `entityTypes`, `maxRecords` | Which golden records to read websites from. |

```http
POST https://<your CluedIn host>/api/api/microsoft-iq/connections
Authorization: Bearer <token>
Content-Type: application/json

{
  "name": "Web IQ supplier sites",
  "product": "WebIQ",
  "tenantId": "<tenant id>",
  "clientId": "<client id>",
  "clientSecret": "<client secret>",
  "billingAccountId": "<billing account id>",
  "scopeName": "CluedIn.Suppliers",
  "entityTypes": ["/Organization"],
  "siteVocabularyKeys": ["organization.website"],
  "webIqApiKey": "<runtime api key>",
  "cronSchedule": "0 4 * * *",
  "enabled": true
}
```

## Validate end to end

1. **Preview.** Send `POST /api/api/microsoft-iq/preview?sampleSize=50` with `{"product": "WebIQ", "scopeName": "CluedIn.Suppliers", "entityTypes": ["/Organization"], "siteVocabularyKeys": ["organization.website"]}`. *Expected:* the sites the scope would include, for example:

   ```json
   {
     "scopeName": "CluedIn.Suppliers",
     "includeSites": [ "adventure-works.com", "adventureworks.co.uk", "contoso.com", "fabrikam.com", "northwindtraders.com" ],
     "includedSiteCount": 5,
     "rejectedValues": 1,
     "isTruncated": false
   }
   ```

2. **Create the connection.** *Expected:* `201 Created`. A `400` names what's wrong, for example `the service principal has no management access to billing account ...`.
3. **Publish.** Send `POST /api/api/microsoft-iq/connections/{id}/publish`. *Expected:* `lastResult` reads `Created Web IQ scope 'CluedIn.Suppliers' with 5 sites (1 values weren't usable websites). ...`.
4. **Check in the Web IQ portal.** Open [Scopes](https://webiq.microsoft.ai/scopes). *Expected:* the `CluedIn.Suppliers` scope, with the published sites on the **Included** tab.
5. **Search with the scope** after 10 to 30 minutes. Send `POST /api/api/microsoft-iq/connections/{id}/web-iq-search` with `{"query": "annual report"}`. *Expected:* `scopeApplied: true`, and only results from the included sites.
