---
layout: cluedin
title: Entity type
parent: Key terms and features
nav_order: 9
has_children: false
permalink: /key-terms-and-features/entity-type
tags: ["development","entities","entity-types"]
---


An Entity Type is your way to tell a Clue its base object type. This could be any of the inbuilt Entity Types from CluedIn, or it could be custom types as well. A Clue can only have one type, but an entity may have decided its type based off different entity types from many Clues. For example, if one Clue was of type "/Infrastructure/Contact" and one was "Person", then the final Entity will choose one of these types - you cannot have more than one Entity Type. 

Why do Entity Types have a "/" in them? CluedIn has a nested hierarchy of Entity Types that will separate the types by a forward slash. This hierarchy could be something such as "/Sales/Deal", indicating that the "Deal" type is a child of the "Sale" entity type. We sometimes refer to these as "Namespaces".

By choosing certain Entity Types, CluedIn will do some automatic processing on that data. For example, if you add a custom Entity Type of "/Car", then by default, CluedIn will most likely do absolutely no "smarts" on this entity. This is simply due to the fact that the CluedIn processing server will only listen to certain Entity Types and run extra processing on it. Your custom data will be persisted and made available - there is no issues with adding new types. If you would like to add "smarts" into the CluedIn processing server to handle your new Entity Type and either clean, validate, enrich or other - then you will need to add new Processors, based off the IProcessing interface.

You can access all the default Entity Types using the Static EntityType class. Think of Entity Types like Domain Objects. 