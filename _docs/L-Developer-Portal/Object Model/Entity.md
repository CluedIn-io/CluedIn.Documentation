Entity

An Entity is the object model that CluedIn builds based off 1 or many Clue objects. An Entity will contain a history of every single Clue that was merged into, connected to or enriched a particular record. An Entity will store an object, referred to as the ProcessedMetaData which is a collection of data that CluedIn has decided is the “instance” or “version” of this record that it deemed to be the highest fidelity, most accurate and most statically confident permutation of the data for this record. Hence in the many different datastores for CluedIn, some of the database providers will only store a single permutation of an Entity, where others will store the full history. 

When an Entity is made up of multiple Clue objects, CluedIn will store the history of this record. You can see this history in the "History" tab of our Entity record. 
