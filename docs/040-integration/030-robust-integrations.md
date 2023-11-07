---
layout: default
title: Help with building robust integrations
parent: Crawlers and enrichers
grand_parent: Integration
nav_order: 030
has_children: false
permalink: /integration/robust-ntegrations
tags: ["integration"]
---


With the CluedIn team building just over 220 integrations to date, we have learnt quite a lot of tips and tricks in guiding developers to build good and robust integrations. 

Here is an exhaustive list of advice from the team to help you also build robust integrations.

 - Make sure you attend the 3 day developer training given by the CluedIn team. You will be given first hand advice and labs on building solid integrations. 
 - Your integrations are responsible for fetching data, not cleaning it, not access control, not joining or blending data. In an ETL world, CluedIn wants your integrations to be more like ELT i.e. just extract and load. The CluedIn server will do the "T" or the Transform. 
 - Build your crawlers with a mindset that the structure can and will change on a regular basis (even if it does not).
 - Many source systems will contain "Discovery Endpoints" in which you can "sniff" what types of data is possible for you to fetch. These are great to use, because they make your integration more dynamic than static. In this way you can build integrations that are very flexible and can use the source system to discover what objects or data is available and then "iterate" over all objects to fetch all the rows or instances of those objects. It is quite typical that these types of sources will also describe the data in forms of "type", "constraints" and more. 
 - Use the inbuilt Crawler Validation Framework within the Crawler Templates to help validate if you are building your crawler with best practices. 
 - Your crawlers may be responsible for fetching billions of rows of data and hence this should be designed into your crawler as well. This means that practices like paging, filtering and more is recommended. 
 - You might find that many CluedIn integrations will use "Service Accounts" to access data. This means that CluedIn will need to "iterate" all the individual accounts that this "Service Account" has access to. 
 - There is a default timeout on crawlers in that if they have not fetched data within a 10 minute window, the CluedIn server assumes that something has gone wrong and will terminate the job. You can sometimes cause this accidentally or it might be that sometimes you will need to increase this timeout. For example, if your integration was built in a way to sort a table of data before ingesting it (because of a performance reason) then you might find that your table takes longer than 10 minutes to sort before it can start iterating and ingesting data from the platform. Increasing the timeout is fine and supported. You can change this in your container.config file.

 The best way to learn how to build a new integration is typically to view the over 220 prebuilt integrations as to see what the final solution looks like. You will notice that CluedIn is using the advice above in its integrations as to also abide by best practices. 

 You can probably imagine that an integration that we build and deploy today, may change requirements tomorrow. Due to the nature of the integrations being very simple in nature and just tasked with fetching data, you will often find that the common failures are due to the underlying system changing in some way. The typical issues are:

  - The location of the source has changed e.g. a connection string or physical location.
  - The data itself has changed structure and can no longer be properly reserialized into the JSON or XML format that CluedIn is asking for. 

  There are some of these changes that are more drastic than others and CluedIn integrations can be setup in a way to "survive" some changes without the need for new deployments and changes to integration code. For example, if your underlying data has simply added a new column or property, CluedIn can "survive" this change, but eventually you should map that new property into its rightful Entity Code, Edge, Vocabulary Key or other. At least data will continue to flow from source to CluedIn. If the object structure changes dramatically, you will notice that CluedIn will throw notifications and alerts that we detect that a change is dramatic enough to stop the flow of data suffering from this issue until it is addressed. Making the changes in your code and redeploying will address this issue and data will continue to flow. 

  You might also find that endpoints (REST) change, but we do find that most providers are quite good at versioning their endpoints so that data will continue to flow. However, in this case you might find that changing to the new endpoints will require to to run a complete re-crawl as you might be getting more rich data from the new endpoints. Therefor some sources might be sophisticated enough that we don't require to fetch all data, but only the new fields that we are interested in. This complicates the crawler too much and it should potentially be avoided. It really depends on the source itself and if you find that you are charged a lot of money for pulling data. There are many integration sources that can be like this and it means that you may have to control this in your integration code. 

  The CluedIn Crawler framework ships with a validation framework in which this can be extended as well. To add new Rules, all you need to do is implement the IClueValidationRule interface and then compile and drop this into your CluedIn directory to reboot. The Framework currently watches for:

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