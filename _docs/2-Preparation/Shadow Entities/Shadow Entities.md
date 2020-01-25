Shadow Entities

In an effort to remove "noise" from your CluedIn data, we have the idea of "Shadow Entitites". A Shadow entitiy is a record that exists in the datastores but has been flagged as a record that will be hidden from the results in your data access layers of CluedIn. This is based off the "Eventual Connectivity" pattern in that this Shadow Entity may turn into a real Entity when it is exposed to new and more data. 

If you find that you are ingesting data and you expect a result to show up in the search catalog (and it does not), chances are it is a Shadow Entity. Shadow Entities are usually constructed from "Unstrcutured Text" i.e. we have a reference to a Person or Company that is only a "soft" reference. 

Shadow Entities are also constructed when the "Eventual Connectivity" patterns constructs an edge to an Entity via an Entity Code and that Entity Code doesn't not exist in any other data source yet. 

The Shadow Entity Center is the User Interface that CluedIn provides in which a Data Steward can manually link Shadow Entities to Entities. The main use-case of this is when we find a "soft" reference to a Person or Company in unstructured text and the Data Steward knows the exact Entity that this can be linked to or merged with. 