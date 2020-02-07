CluedIn Clean

CluedIn Clean is an application targeted towards cleaning data so that downstream consumers of CluedIn can have a much more ready to use set of data. This includes:

Normalising values to a common standard for downstream consumers. 
Manually enriching entities from online and external data sets. 
Having a bulk way to clean data and generate Mesh commands back to the source systems.

CluedIn Clean is targeted at Data Engineers and Business Analysts. The closer to the context of the data the resource is, the better. CluedIn Clean currently only supports cleaning data in Core Vocabularies. This is on purpose, as the Core Vocabularies are typically what downstream consumers will want to use. 

You can create brand new Cleaning projects and choose the type of data you would like to clean and the number of records as well. This will generate a cleaning project for you and make it available in the list of projects when you first enter the cleaning menu option.

CluedIn Clean should be used for the following reasons:

 - To normalise representations of values that are the same, but sometimes in different formats e.g. Addresses that are the same location, but the order of the different pieces of the address are different. 
 - To standardise representations of labels, geographical locations. Although not mandated, it is quite common to standardise on a language of data to downstream consumers e.g English, Danish, Italian. Hence CluedIn Clean can help with standardising this. 
 - To fix uniformity in casing of values e.g. First and Last Names of people.
 - To manually enrich data using online external services and to manually choose which records are matching the ones that you intend to enrich. 
 - To move values from one property to another. Sometimes you will find that you receive that where the intention was to have the city in the City column, but instead the Country was entered. CluedIn Clean can help with these types of issues. 
 - To detect outliers in values for a particular property. 

CluedIn Clean should not be used for the following reasons:

 - To correct data that requires business domain knowledge to fix e.g. First and Last Names spelt differently to how they are regularly spelt.
 - Add new fields.
 - Correct Entity Codes.

CluedIn Clean can handle transliteration, which is the ability to handle normalisation of text with accented and diacritic characters. 

One of the main use cases of CluedIn Clean is to clean erroneous Entity Code values before persisting them into the Datastores e.g. often you will find that we will mark certain properties as Entity Codes but then realise in the data that the values can have values like -1, N/A, Empty String etc. When you are adding an integration there is a simple flag that  can be set to ingest and process or ingest and place into a sandbox where only after the data has been cleaned will be then persist and create the proper entity codes. It is suggested that for the initial ingestion of data that it will go into CluedIn Clean in this sandbox environment and then for subsequent runs, we will accecpt that new types of anomaly data will have to be dealt with pro-rata. This will be handled by our Quarantine application that flags data that doesn't conform to what is expected. 

CluedIn Clean projects are only committed and processed when the Commit button is pressed. Until that point, the projects are kept in their own sandbox environment. Once committed, CluedIn will take every row of data in that project and will create a respective Clue out of it, marking the source as “CluedIn Clean”. This will show itself in the history just like any other Clue that would have come from a source of data. This will provide you with the data lineage necessary to trace what clean operations have been made on the data as well. It is recommended to remove a cleaning dataset after you have committed it. You can always create another cleaning dataset at a later point. 

Try to keep your cleaning projects relatively small i.e. less than 50,000 records at a time. This means that your cleaning will go a lot smoother as it doesn't have to analyse (potentially) millions of records every time that you want to clean the data. 

Once you are finished with cleaning the data, you will have a commit button available on the main list of cleaning projects. This will then write the data back to CluedIn and will create any mesh commands that need to be created to write this clean data back to the source systems as well. 