Shadow Entities

In an effort to remove "noise" from your CluedIn data, we have the idea of "Shadow Entitites". A Shadow entitiy is a record that exists in the datastores but has been flagged as a record that will be hidden from the results. This is based off the "Eventual Connectivity" pattern in that this Shadow Entity may turn into a real Entity when it is exposed to new data. 

If you find that you are ingesting data and you expect a result to show up in the search catalog, chances are it is a Shadow Entity. Shadow Entities are usually constructed from "Unstrcutured Text" i.e. we have a reference to a Person or Company that is only a "soft" reference. 