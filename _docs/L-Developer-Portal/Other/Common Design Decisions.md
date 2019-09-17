Common Design Decisions

Multiple Email Addresses

There is a special Core Vocaulary for mapping multiple Email Addresses instead of having to map just one. 

Integrating Databases with Seed Identity

It is quite normal for Databases to generate Identifiers for records starting from the Id of 0 and then incrementing this Id for every new record by 1. This might lead you to think that this will not be a unique reference to a record, but rest assured that it can be. If you need to create an Entity Code out of this record, you have to remember that this Entity Code will also contain a Entity Type, Code Origin and an Identifier. 

Flattening Records

Without a doubt, if two clues or entities have the same Entity Code then they will be flattened into the same record and will have the history of both clues contained within it. It can sometimes be hard to determine if records should flatten or not, but this is more a business based decision than a technical one. 

Build Hierarchies or not?

There are many times where you will have data that has a hierachy to it. For example, imagine a company that has a parent or mother company. If we had the same Entity Codes for these 2 records then CluedIn will treat these as the same company. This is not always the intention of your data project. The other option is to create hierarchies where if these two company objects need to be linked, instead of merged - you will often need to look at creating edges between these objects instead of entity codes. 