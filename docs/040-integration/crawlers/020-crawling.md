---
layout: cluedin
title: Crawling
parent: Crawlers
grand_parent: Ingestion
nav_order: 020
has_children: false
permalink: /integration/crawling
tags: ["integration","crawling"]
---
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

Crawling servers are stateful but also transactional in nature:

- If a crawl does not finish, its state will never be marked as complete.

- If you cancel a crawler midway through a job, you must restart the crawl from the beginning or from the data that changed state in the source system since the last successful crawl.

Crawlers are responsible for fetching data from a source system:

- They are self-hosted, and when they run, the CluedIn server provides everything needed to connect and pull the correct data.

- If a crawl is cancelled midway, CluedIn will still ingest whatever data has already been ingested.

{:.important}
It is not recommended to run a Crawling Server and a Processing Server on the same CluedIn host, as they operate in different environments (stateful vs. stateless).

Crawlers are provided out-of-the-box with CluedIn. If you build your own, remember:

- Crawlers should not contain business logic.

- Crawlers should not attempt to fix source data.

## Crawling complexities

Crawling data can be complex and error-prone. Issues may include:

 - Time-outs when calling sources

 - Network errors when calling sources

 - Source structure changes mid-crawl

 - Authentication changes mid-crawl

 - Source systems without obvious filtering mechanisms

Your crawlers must account for these complexities. Fortunately, the CluedIn crawler framework helps handle them, giving you full control over error handling (for example, retry logic, retry frequency).

## Checklist for custom crawlers

When extending CluedIn with custom crawlers, ensure the following areas are covered.

**Webhooks**

- [ ] Webhook support – Does this provider support Webhooks?

- [ ] Manual or automatic – Can CluedIn create webhooks programmatically, or must they be set up manually?

- [ ] Webhook lifecycle – Test if webhook creation, processing, and deletion works.

- [ ] Management endpoint – Is there a place in the UI where users can manage webhooks created by CluedIn?

**Configuration**

- [ ] Configuration filters (for example, folders, labels) – What configuration can the user set to filter what the crawler fetches? 

- [ ] Provider configuration – List, tree, setting, checkbox.

- [ ] Type of provider – Cloud or on-premises?

**Authentication & API handling**

- [ ] API tokens or credentials – Does the provider support developer tokens?

- [ ] API rate limiting – What rules are in place to limit what the crawler does?

- [ ] Status code handling – Does the crawler handle `429 Too Many Requests`?

- [ ] Authentication types (OAuth2, OAuth, Basic, API token, custom) – What types of authentication does this API support?

- [ ] OAuth2 flow endpoints – What are they?

- [ ] Refresh token – How does the provider refresh access tokens?

- [ ] Expired token – How is expiry handled? 

- [ ] ReAuth endpoint – Is there an endpoint in CluedIn for reauthentication?

**App requirements**

- [ ] App installation – Does CluedIn need to install an app before it can connect to it?

- [ ] App install URL – What is the install link?

- [ ] Permissions – Are read/write permissions required?

- [ ] Paid account – Does the provider require a premium/paid account?

**Crawling behavior**

- [ ] Auto-watching – Will CluedIn automatically sync new folders/channels? 

- [ ] Paging – How are results paged?

- [ ] Schedule – How often should a crawl run?

- [ ] Filtering to get only the latest data (delta/auto crawls) – By default, CluedIn runs a job every 4 hours for a new crawl. This should only pull changes since the last crawl. For details, see [Delta/Auto crawls – Change Data Capture](./delts-crawls).

- [ ] Dynamic templates – Does the provider support custom/dynamic objects (e.g., SharePoint, Podio, HubSpot)?

**Data handling**

- [ ] Entity statistics – Can the provider report how much data of each type exists?

- [ ] Cursor vs. date filters – Which is used, and in what format?

- [ ] Schema for connections – Does the crawler connect with the correct edge type and direction?

- [ ] Data formats – Is incoming data formatted correctly?

- [ ] Vocabulary key mappings – Is all data mapped to the relevant core vocabulary keys?

- [ ] Date formatting – Are dates stored in the correct format (`ToString("o")`)?

**Provider metadata**

- [ ] Logo – High-quality 400x400 provider icon.

- [ ] Description – A short description of the provider.

- [ ] Account details – How to get account ID and display name.
 
- [ ] Provider ID – What is the GUID of the provider?


 
