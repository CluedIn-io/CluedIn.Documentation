---
layout: cluedin
title: Tips on building robust integrations
parent: Crawlers
grand_parent: Ingestion
nav_order: 030
has_children: false
permalink: /integration/robust-ntegrations
tags: ["integration"]
---
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

With the CluedIn team building over 220 integrations to date, we’ve collected many tips and tricks to guide developers in building solid and reliable integrations.

This section provides an exhaustive list of advice from the team to help you build robust integrations.

## Best practices for building integrations

 - Attend the 3-day developer training provided by the CluedIn team. It includes first-hand advice and labs on building integrations.
 
 - Keep integrations focused on fetching data only – not cleaning, access control, or joining/blending data.

    In ETL terms, CluedIn follows an ELT model: Extract + Load are handled by integrations; Transform is handled by the CluedIn server.
 
 - Build crawlers assuming the data structure will change regularly (even if it does not).

 - Many source systems provide "Discovery Endpoints", which let you detect what types of data are available to fetch. Using these makes your integration more dynamic and flexible rather than static. With Discovery Endpoints, your integration can identify available objects or datasets and then iterate through them to fetch all rows or instances.

    These sources often also describe the data in terms of types, constraints, and other metadata, which can further guide your integration logic.

 - Leverage the inbuilt Crawler Validation Framework within the Crawler Template to ensure your crawler follows best practices.

 - Design crawlers to handle large datasets (billions of rows). Implement paging, filtering, and retry mechanisms.

 - Expect to use "Service Accounts" – your crawler may need to iterate across all accounts accessible to that service account.
 
 - Be mindful of the default crawler timeout (10 minutes). If a crawler does not fetch data in that window, CluedIn will terminate the job. You can increase this timeout in `container.config` if needed (for example, for pre-sorting large tables).

## Learning from prebuilt integrations

The best way to learn how to build integrations is by reviewing the 220+ prebuilt integrations. You will see that they consistently apply the best practices listed above.

## Handling changing requirements

Integrations must adapt to changes in source systems.

Typical issues include:

- The location of the source changes (for example, connection string, physical location).

- The data structure changes, breaking JSON/XML serialization.

CluedIn’s resilience to changes:

- If a new column/property is added, CluedIn can continue processing until you map it properly (entity code, edge, vocabulary key, and so on).

- If the structure changes dramatically, CluedIn will generate notifications and alerts, stopping the data flow until you update and redeploy the integration.

Endpoint changes:

- REST endpoints may change, but most providers handle this through versioning.

- Switching to a new endpoint may require a full re-crawl, especially if richer data is returned.

- Some sources charge for data pulls – avoid overly complex crawlers that attempt to minimize costs by selectively fetching only certain fields unless necessary.

## Crawler validation framework

CluedIn’s crawler framework ships with a [validation framework](/crawling/crawler-validation-framework), which you can extend.

- To add new rules, implement the `IClueValidationRule` interface.

- Compile your changes, drop them into the CluedIn directory, and restart the system.

The framework currently watches for:

```csharp
DATA_001_File_MustBeIndexed
ENTITYTYPE_001_Person_MustNotBeUsedDirectly
ENTITYTYPE_002_Document_MustNotBeUsedDirectly
METADATA_001_Name_MustBeSet
METADATA_002_Uri_MustBeSet
METADATA_003_Author_Name_MustBeSet
METADATA_004_Invalid_EntityType
METADATA_005_PreviewImage_RawData_MustBeSet
METADATA_006_Created_Modified_Date_InFuture
METADATA_007_Created_Modified_Date_InPast
METADATA_008_Created_Modified_Date_UnixEpoch
METADATA_009_Created_Modified_Date_MinDate
METADATA_010_Created_Modified_Date_MaxDate
EDGES_001_Outgoing_Edge_MustExist
EDGES_002_Incoming_Edge_ShouldNotExist
PROPERTIES_001_MustExist
PROPERTIES_002_Unknown_VocabularyKey_Used
PROPERTIES_003_Value_ShouldNotBeQuoted
```