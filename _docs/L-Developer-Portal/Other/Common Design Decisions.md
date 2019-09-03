Common Design Decisions

Multiple Email Addresses

There is a special Core Vocaulary more mapping multiple Email Addresses instead of having to map just one. 

Integrating Databases with Seed Identity

It is quite normal for Databases to generate Identifiers for records starting from the Id of 0 and then incrementing this Id for every new record by 1. This might lead you to think that this will not be a unique reference to a record, but rest assured that it can be. If you need to create an Entity Code out of this record, you have to remember that this Entity Code will also contain a Entity Type, Code Origin and an Identifier. 