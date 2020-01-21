Entity

An Entity is the object model that CluedIn builds based off one or many Clue objects. An Entity will contain a history of every single Clue that was merged into, connected to or enriched a particular record. An Entity will store an object, referred to as the ProcessedMetaData which is a collection of data that CluedIn has decided is the “instance” or “version” of this record that it deemed to be the highest fidelity, most accurate and most statically confident permutation of the data for this record. Hence in the many different datastores for CluedIn, some of the database providers will only store a single permutation of an Entity, where others will store the full history. 

Graph Store: Will only store the Processed Golden Version of a record.
Search Store: Will store all versions of the record.
Blob Store: Will store every single piece of data on the record and all history.

When an Entity is made from multiple Clue objects, CluedIn will store the history of this record. You can see this history in the "History" tab of our Entity record. An Entity can be seen as the end goal of data within CluedIn. When accessing the data within your CluedIn account, you will always be accessing Entities, never Clues. The reason for this is that an Entity is one many Clues that have passed all the checks that tell CluedIn that a Clue is valuable, valid and has enough data in it to be useful. 

An Entity has a special property called the ProcessedEntityMetaData. This contains an amalgamation of the properties that have come from the different respective Clues or "Data Parts". CluedIn will decide which properties from which Data Parts are elavated to the ProcessedEntityMetaData based off many factors including, Modification or Creation Dates, Data Metrics, Source System. What you will receive in the end is a ProcessedEntityMetaData object that contains what CluedIn thinks is the most valid representation of an Entity. 