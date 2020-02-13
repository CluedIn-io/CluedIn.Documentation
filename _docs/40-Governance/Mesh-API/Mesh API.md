---
category: Governance
title: Mesh API
---

The Mesh API allows a developer to implement the ability for CluedIn to write back values from CluedIn to source systems. This comes in the form of the following operation types: 

Edit
Delete
Archive
Associate
Disassociate
Anonymise
De-anonymise
Remove from Processing

Due to the nature of this feature, there are no mesh API’s that are implemented in a blank installation of CluedIn. This is due to the nature that most mutation operations will change requirements per customer. This does not mean however that a lot of the framework around the operations is not turned on by default. The following actions will cause mesh commands to be generated:

Manually edit a property in the Property view within CluedIn
Any operation within CluedIn Clean that changes values
When a value is determined through the Data Quality scores to be a higher statistical confidence than what is in the source system. 
When a core vocabulary is empty from one source and available in another. 
When the data governance pieces around Subject Access Requests are initiated i.e. Anonymisation, Magnification, Deletion. 

All Mesh Commands are queued by default i.e. they don't automatically run. It requires the product owner of that integration point to click the "Approve" operation on that mesh command to physically run the command. You can see these commands in your Mesh Center from the main menu. It also requires that the authorisation and authentication that has been provided for that source is given the right permissions to fulfil the operation. 

Notes from the field: Especially when talking to databases directly, it is often hard to gauge what operations are needed to run to properly run an expected operation. For example, cascading support is often needed on databases if you are trying to run an operation that has referential integrity in another table and hence when you try to run an operation it may respond with exceptions. 

It is often the case that with proper base implementations, that Mesh API implementations can become cleaner and less work, with the only changes per endpoint being the Url to call and the package of data to send. 

By implementing the base classes for Mesh Processors you will receive a flow as follows:

Step 1: Given input from CluedIn, you can construct a textual preview of what command you will be running against the source system.
Step 2: If the user decides to run the command, it will make the appropriate call to the endpoint to make the mutation. 
Step 3: CluedIn will run the validation function so that you can check if your operation worked successfully e.g. if you ran a delete operation, you would expect that if you tried to lookup the value again that you would not get a record back. If your validation fails, then CluedIn will retry for a number of times and then mark the mesh command in a failed state. This means that there is a strong chance that the operation failed.

When mesh operations are run, it will update the records in the source systems and in most cases will update their modification stamp as well. This means the next time that CluedIn runs a scheduled crawl against that system, if the source sends us the updated modification stamp then CluedIn will process it; if it does not send us the updated modification date then CluedIn will assume it is the same and throw it away in processing. This is due to the hash that CluedIn generates on entities as to do quick comparisons of records. 

Mesh API commands can be generated through the CluedIn REST API, or it can be all managed through the CluedIn User Inteface. There are many operations that will generate a Mesh Command, but in summary - any mutation operation that runs in CluedIn will cause Mesh API commands by default. These include:

 Any of these operations will generate Messh API commands and will place these under the affected Entities in the "Pending Changes" tab of the entity page and in the Global Mesh Center where all Mesh Commands are visible. All Mesh Commands that are generated through the CluedIn User Interface are by default "Queued" and are not run until the Product Owner of the record that is being mutated accepts the change. You might find that an Entity has been merged from many sources and hence every single individual Product Owner will need to be involved in the Approval Process. 

 Mesh Commands are Vocabulary enabled, meaning that they will utilise the hierarchy of Vocabularies that you have built so that you can change a particular value and CluedIn will "unravel" the Vocabulary of that value as to create Mesh Commands for all child and sub-child nodes of the records edited. 