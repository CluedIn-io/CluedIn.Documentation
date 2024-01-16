---
layout: default
title: Entity Page
parent: User Interface
nav_order: 10
permalink: /user-interface/entity-page
tags: ["ui"]
published: false
---

The entity page will show you a single view of the record, all metadata associated to this record and all records that have a connection to this record. 

![Diagram](../assets/images/user-interface/unified-view.png)

The entity page is composed of many "tabs". The Overview tab is a view of the consolidated view of the record where it shows the most statistically accurate values of properties from across the different systems that ingested this data. 

The "All Properties" tab will show you a meta data view of the record where you can filter and view the history of records by a property level. 

The "History" tab will show you a list of all the Clue objects that composed this record. This could be a combination of internal data sources as well as external data sources that have been enabled. 

The "Pending Changes" window will show Mesh Commands that are ready to run for this particular entity. 

The entity page allows you to show the "Suggested Searches" feature of CluedIn so that you can show widgets on the page that show related data. This data may be direction relations or very sophisticated queries.

You will also note that your "entity-level" data quality scores are shown. 

There are many actions that you can run from the entity page. These actions are located under the "More" dropdown. These actions include:

 - Select records to merge
 - Mark this record as sensitive
 - Minimize this record to only have the metadata that you have consent for
 - Anonymise this entire record and all places where it is referenced. 
 - Remove this record from any automated processing in CluedIn or other third party systems. 
 - Manually reprocess this record through all the external data providers enabled in your account (e.g. Google Places)
 - Manually reprocess this record through the processing pipeline of CluedIn.

You can also see all of the "child" entities of this record in the "Parent Aggregation" component.

![Diagram](../assets/images/user-interface/parent-aggregation-view.png)

On the Entity Page you will be able to see your visual view of a Record. CluedIn will automatically choose which properties from which systems are the most accuract and hence are the ones that we will natively display in the user interface as the "Golden Value".

CluedIn has 3 possible mechanisms to choose the "Golden Value".

1. Latest Modified Date
2. Highest mean value across metrics
3. Highest mean value across metrics combined with the trust level set at the integration level.