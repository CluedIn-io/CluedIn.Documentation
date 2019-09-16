Entity Codes

An Entity Code is a way to instruct CluedIn to know what a completey unique reference to a Clue is. It is important to establish that an Entity Code will cause two Clue objects to merge with 100% confidence. 

Entity Codes will often be unique to the source system only, this is fine. Every now and then you will ingest a property that allows you to bridge different sources. It is not recommended to build Entity Codes where you force the Origin to be that of a common Origin e.g. "CluedIn". The role of the Vocabulary mappings is to handle this type of operation on the processing server. 

There are many times where Identifiers for Entity Codes are dirty, or not ready to be made into a unique Entity Code. Examples include data where you have default or fallback values where a real value is not present. Imagine that you had an EmployeeId property or column in your data and when a value was not present, someone would place "NONE", "", "N/A" or other values. These are obviously not valid Entity Codes pertaining to the EmployeeId. This is completely fine in CluedIn, in fact we expect this to happen all the time. THe important aspect is that you will not be able to upfront handle all permutations of this "placeholder" and hence you should still create Entity Codes with the intention that these values are unique. We will fix and clean this up later. 

There are many aspects of an Entity Code that will lead to slower processing time. If you find that you have a large amount of duplicate data that would cause you to have Entities with 1000's of EntityCodes, then processing this record will take significant time. Be careful of using Entity Codes that would cause this type of behaviour. 

