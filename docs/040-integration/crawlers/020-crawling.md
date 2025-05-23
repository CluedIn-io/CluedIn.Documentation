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


Crawling servers are stateful but are also transactional in nature i.e. if a complete crawl does not finish, then it will never have a state of “complete”. This also means that if you were to cancel a crawler half way through a job, that you will need to start the crawl from the start again or potentially from the data that had changed state in the source system since the last successful crawl time. Crawlers are responsible for fetching data from a source system. Crawlers are self hosted and when they are run, the CluedIn server is responsible for giving it everything that is necessary to successfully connect and pull the right data from a source system. If you were to cancel a crawl half way through, CluedIn will ingest the data that has been ingested. 

It is not recommended to run a Crawling server and a Processing Server in this same CluedIn host, due to the change in nature of stateless and stateful environments. 

There are many crawlers that are provided for you in CluedIn, but if you are building your own, it is important to remember that the crawlers should not contain business logic and should not attempt to fix the data from the source. 

Crawling data can be complex and error-prone and many things can go wrong such as:

 - Time-outs when calling sources
 - Network errors when calling sources
 - The source changes structure mid crawl
 - Authentication can change mid crawl
 - Source systems don't have an obvious way to filter the data

Your crawlers will need to cater for all of the complexities mentioned above and more. Fortunately, the CluedIn crawler framework helps with all of the above mentioned complexities. You have full control over the granularity of error handling that you would like in your crawlers e.g. managing how often to retry or how many times.

Here is a list of things you should be covering with any custom crawlers that you extend CluedIn with: 


* Supports Webhooks - Does this provider support Webhooks? 
* Are Webhooks Manual or Automatic  - Does the provider support programmatic webhook creation or does the user need to manually set this up? 
* Test Webhook processing, creation, deletion. - Does the webhook creation process and deletion process work?
* Management Endpoint for Webhooks - Is there a link in the User Interface where the user can manage any webhooks that CluedIn creates?

* Test that you are handling for configuration filters e.g. Folders, Labels. - What configuration can the user set to filter what the crawler goes out and gets? 
* Configuration of Providers -> List, Tree, Setting, Checkbox? 
* Type of Provider - Is it Cloud? Is it On-Premise? 

* Test API Token or Credentials - Does the provider support Developer API tokens. 
* API Rate Limiting  - What rules are in place to limit what the crawler does?
* Test 429 Status Code Handling - Does the crawler handle limiting requests?
* OAuth2, OAuth, Basic, ApiToken, Custom - What type of authentication can this API support? Remember that you can support many different types of Authentication.
* OAuth 2 flow endpoints. - What are the OAuth2 flow endpoints?
* Refresh Token - How does a provider refresh an access token?
* Expired Token - When does an access token expire? 
* ReAuth Endpoint - Endpoint in CluedIn to run the ReAuth Process. 

* Requirements and APP to be installed - Does CluedIn need to install an APP before it can talk to it?
* App Install URL - What is the Install URL of an App if it requires an App to be installed first?
* Get Permissions - Are there any permissions set in the provider for read/write access?
* Requires a Paid Account / Premium Account - Will CluedIn only work if the provider is a paid account?

* Configuration for AutoWatching new things in providers - Will CluedIn automatically sync NEW folders and channels that are added into the provider. 
* Paging - How to page results in a reasonable amount of data at a time? 
* Schedule of how often it runs - How often should a crawl run?
* Filtering on only getting the latest data (delta/auto crawls) - By default, CluedIn runs a job every 4 hours for a new crawl. This should only pull the latest data since the previous crawl. Please refer to [Delta/Auto crawls - Change Data Capture](./delts-crawls)
* Has a Dynamic Template - Does the provider support custom and dynamic objects e.g. SharePoint/Podio/HubSpot etc. 

* Getting the Entity Statistics - Does the provider support a way to figure out how much data of different types they have? 
* Does the source use a cursor to get latest or a date filter (what format) - If the provider uses a cursor instead of a date filter. 

* Logo - Does the provider have a good high quality 400x400 image icon of the provider?
* Description of Provider - Small description of the provider. 

* How to Get Account Id and Account Display - What is the unique ID of the provider per user and what is the friendly name to display in the UI. 
* Id - What is the GUID of the provider? 

* Schema for Connections - Does the crawler connect properly with the right edge type, edge direction. 
* Data formats - Is the data in the format you mapped it to be?
* Vocabulary Key mappings - Is all the data mapped to relevant Core Vocabulary Key?
* Test that Dates are in the right format. - If we are using dates in the Vocabulary, do they format to ToString("o")?


 
