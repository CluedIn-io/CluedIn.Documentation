Common Problems

Floating Edges

You may find that you are browsing your data in CluedIn and you see edges to records that only have an Id. This could be because that is simply the name of that record, but more likely is that you have a floating edge. A floating edge is an edge to a record that doesn’t exist yet. Imagine that you are importing your contact list and on every contact there is a property that points to a companyId. You would naturally create an edge out of this in your crawlers and hence if we were only to ingest the contacts then we would have floating edges to records that is waiting for us to ingest the list of companies for the link to be made by CluedIn. 

Mail Previews

Mail is a bit sensitive and hence you might want to not show the previews within the UI. This is simply a matter of changing the Visibility type of the Core and Provider Specific Vocabularies to Hidden. This means that it will not only be hidden in the User Interface, but also it will not appear in the results from the Rest API of CluedIn. 

There are some properties that I don’t want to expose to downstream consumers

It is common when ingesting data from multiple different sources that there are some properties are there as metadata or supplementary fields and hence are not intended to be projected out to downstream consumers. This is why, as developers, you can control the Visibility of Vocabularies. This is an enumeration which also has Flags, meaning that you can combine different Visibility properties together. 

Order of Processing

There are many times where the order of the initial processing of data can yield better results if ordered differently. For example, for performance reasons, it is always a good idea to pre-clean data in CluedIn Clean before ingesting it and creating Entity Codes. Often this will lead to a faster processing, higher data quality and better results. Although possible, it is often best to be able to clean all the different permutations of bad entity codes before ingesting data into CluedIn. For lineage purposes, we would recommend that you store the original and bad entity codes in the property bag and fix the data for the Entity Codes. 

Heavy Records

There are times when you have records that are very "dense". It happens, it is natural. It is however that you should expect that these records take a lot longer to process than others. If possible, try to keep the number of versions/clues per records/entity to a minimum. There are many strategies that you can use to do this. In your crawlers you can break up records into sub-records.

Heavy Out-going Relationships

It is just a side-effect of using a Graph Database, that there are times where certain operations are more expensive than others. If you find that you have records that have a lot of outgoing references, then every time that we try to add a new outgoing reference, CluedIn will load all existing reference in order to check if the relationship exists already or not. If you have designed your integration correctly then this should never happen, but keep a look out for it if you find that your processing servers are slow. The concept in a graph is to not have "dense" nodes and hence if you can break up your nodes into sub-nodes then this will alleviate this type of problem.

Crawling Data

The nature of integrating and crawling data sources is that things go wrong all the time - more than you would probably like to admit. Imagine that you have 1 million records to fetch from a system and you find that you page through the data 100 records at a time. When you get to page 500, you find that it fails in fetching that page. You might have retry mechanisms in place that you will retry 10 times and if it still fails then you will continue. You might find that the rest of the crawl goes completely fine. So you have 999,900 records and are missing 1,000,000 records. How do you handle this in CluedIn? The first question would be, how would you even know that this happened? Your logs will show this, but they could be very large. You could view your log provider of choice where these logs are being processed and you will most likely easily see that this happened. You will also have this logged with the Agent Job Run tables which gives you a report of all the completed and failed operations within the job.

Once you have this you can do many things. You can issue a new crawl at a later point and add in configuration to your crawler to be able to take a range of pages that you would like to crawl. This does mean that you would need to write your integrations to support skipping to a particular page before ingesting data. You might find that some integrations do not support this - and there is sometimes not a lot you can do about it. 