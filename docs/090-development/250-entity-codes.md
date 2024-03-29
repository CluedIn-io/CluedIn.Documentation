---
layout: cluedin
title: Entity Codes
parent: Development
nav_order: 250
has_children: false
permalink: /development/entity-codes
tags: ["development","entities","entity-codes"]
---

An Entity Code is a way to instruct CluedIn to know what a completey unique reference to a Clue is. It is important to establish that an Entity Code will cause two Clue objects to merge with 100% confidence. 

An Entity Code is made up from 5 different pieces:

 - Entity Type
 - Provider Definition Id
 - Id
 - Origin
 - Organization Id

This combination will allow us to achieve absolute uniqueness across any datasource that we interact with. 

Entity Codes will often be unique to the source system only, this is fine. Every now and then you will ingest a property that allows you to bridge different sources. It is not recommended to build Entity Codes where you force the Origin to be that of a common Origin e.g. "CluedIn". The role of the Vocabulary mappings is to handle this type of operation on the processing server. 

There are many times where Identifiers for Entity Codes are dirty, or not ready to be made into a unique Entity Code. Examples include data where you have default or fallback values where a real value is not present. Imagine that you had an EmployeeId property or column in your data and when a value was not present, someone would place "NONE", "", "N/A" or other values. These are obviously not valid Entity Codes pertaining to the EmployeeId. This is completely fine in CluedIn, in fact we expect this to happen all the time. The important aspect is that you will not be able to upfront handle all permutations of this "placeholder" and hence you should still create Entity Codes with the intention that these values are unique. We will fix and clean this up later. 

There are many aspects of an Entity Code that will lead to slower processing time. If you find that you have a large amount of duplicate data that would cause you to have Entities with 1000's of EntityCodes, then processing this record will take significant time. Be careful of using Entity Codes that would cause this type of behavior. It doesn't mean that you should not, it just means that you will pay a processing penalty. 

There are also CluedIn specific Entity Codes. These are codes that use the Origin of "CluedIn" and then have a parameter in brackets that specifies a type of Origin e.g. CluedIn(cvr). This Origin shows that CluedIn has a generic, non-source specific Id from a record. 

## How do I make sure Entity Codes will blend across different data sources?

Now that we know that an Entity Code will only merge with another Entity Code if they are 100% the same, we have to talk about how you would be able to merge records across different systems if the Origin will be different. There are many ways to achieve this, but one of the interesting ways is the "GUID trick".

If a record has an Identifier that is a GUID/UUID, you can set the Origin as CluedIn as no matter the system, this should be unique. (Unless you are using deterministic GUIDS). We would recommend to do this and run tests to find out if this is the case. If you are wondering if you do use deterministic GUIDs, doing some pre analysis on the data will help you but figuring our if many GUIDS overlap in a certain sequence of the GUID e.g. you might mind the first chunk of the GUID is replicated many times. This is a strong indicator you are using deterministic IDs. 

GUIDs (random ones) are so unique that the chance of them being the same is close to impossible. Here is the other interesting part of this "trick". You could even determine that the EntityType can be generic as well due to its ability to be unique. You will have to craft these special entity codes in you Clues to e.g. look something like /Generic#CluedIn:<GUID>. You will need to make sure your edges support the same mechanism. In doing this, your are instructing CluedIn that no matter the Entity Type, no matter the origin of the data, this record can be uniquely identified by JUST the GUID.


## What if your record doesn't have a unique reference to construct an Entity Code? 

This happens all the time. Often you will find that you need to merge or link records across systems that don't have Id's but rather require a more rules based or fuzzy merging to be able to link records. In this case, we will often suggest to create a composite Entity Code i.e. an Entity Code that you have constructed from a combination of column or property values that guarantee uniqueness. For example, if you have a Transaction record, you might find that a combination of the Transaction Date, Product, Location and Store will guarantee uniqueness. It is best to calculate a "Hash" of these values combined which means that we can calculate an Entity Code from this. 

