Common Problems

Floating Edges

You may find that you are browsing your data in CluedIn and you see edges to records that only have an Id. This could be because that is simply the name of that record, but more likely is that you have a floating edge. A floating edge is an edge to a record that doesn’t exist yet. Imagine that you are important your contact list and on every contact there is a property that points to a companyId. You would naturally create an edge out of this in your crawlers and hence if we were only to ingest the contacts then we would have floating edges to records that is waiting for us to ingest the list of companies for the link to be made by CluedIn. 

Mail Previews

Mail is a bit sensitive and hence you might want to not show the previews within the UI. This is simply a matter of changing the Visibility type of the Core and Provider Specific Vocabularies to Hidden. This means that it will not only be hidden in the User Interface, but also it will not appear in the results from the Rest API of CluedIn. 

There are some properties that I don’t want to expose to downstream consumers

It is common when ingesting data from multiple different sources that there are some properties are there as metadata or supplementary fields and hence are not intended to be projected out to downstream consumers. This is why, as developers, you can control the Visibility of Vocabularies. This is an enumeration which also has Flags, meaning that you can combine different Visibility properties together. 

Order of Processing

There are many times where the order of the initial processing of data can yield better results if managed. For example, for performance reasons, it is always a good idea to pre-clean data in CluedIn Clean before ingesting it and creating Entity Codes. Often this will lead to a faster processing, higher data quality and better results. Although possible, it is often best to be able to clean all the different permutations of bad entity codes before ingesting data into CluedIn. For lineage purposes, we would recommend that you store the original and bad entity codes in the property bag and fix the data for the Entity Codes. 
