---
layout: cluedin
title: Frequently Asked Questions
parent: Knowledge base
permalink: /kb/faq
tags: ["getting-started", "faq"]
nav_order: 11
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

# What happens if I change the default configuration installed using the Azure Marketplace offering?

Any modifications made to the default configuration, except those explicitly documented as post-install adjustments on the Documentation portal, will result in the termination of support. This includes Premium Support, Azure Managed Application, and any other customer support service. The reason for this is the high probability that the cluster may not operate correctly. Changes outside the documented scope are considered out of support, and CluedIn will not provide assistance or troubleshooting for configurations that deviate from the originally installed setup.

Here is a list of allowed changes:

- Adjusting requests and limits on CluedIn operating pods for both CPU and Memory
- Setting up and receiving assistance with the CluedIn Backup Solution
- Configuring Single Sign-On
- Setting up SMTP details for Welcome Emails
- Configuring Extended alerts via CluedIn (Note: CluedIn-specific alerts only, not customer-specific alerts)
- Troubleshooting ad-hoc cluster failures, if determined not to be caused by the customer
- Upgrading environments
- Installing the product using our default configuration
- Usage of Azure Key Vault to provide secrets to the cluster
- General AKS maintenance on the default configuration

Any deviation from this list will be considered out of support, and assistance for the issue is not guaranteed and may incur charges.

# What is different between CluedIn and other data integration platforms?

Whether you are using SAP Data Services, Azure Data Factory, SSIS, Talend, Python, SAS Institute, Informatica PowerCenter, or other ETL-based tools, they all hold something in common - they require you as the engineer, architecture or business user to map different systems together. However, at CluedIn, we have found that the process of finding out what IDs need to be connected between systems as to unify or connect the records is actually the hardest part of the entire process - in fact, it gets to a point where it is just impossible to do.

CluedIn uses a schema-less based integration pattern that doesn't require a developer, architect, or business user to instruct our platform on how different systems connect - instead, we ask for a much simpler and streamlined mapping, and CluedIn will do all the work to find the relationships between the systems. As a result, we will often find connections that you could never see yourself. 

# What happens with the data ingested that is terrible quality, has non-allowed values, or is noise or mess?

CluedIn is an ELT type of integration platform where we want to take the data in as it is. No transforms. No cleaning. Nothing. That is our job! Insufficient quality data will happen all the time, and hence this is one of the big reasons enterprise companies take so long to get access to ready-to-use data. There are so many places in CluedIn that will catch and distribute the work involved in fixing and addressing the data quality issues that stream through the CluedIn processing engine. Firstly, it starts with CluedIn having many prebuilt processing steps to automatically clean and normalize data into the highest-fidelity format.  Secondly, you can build up lists of "black-listed" values and either remove them or automatically transform them into another value on processing. Finally, you can set up rules that dictate good versus wrong values. It means that data keeps flowing for data that meet the standards - CluedIn will put everything else into a quarantine section for you to resolve so that less and fewer data has issues. 

# What do you do about sensitive and personal data?

CluedIn will natively detect personal data and will start by simply letting you know where it is. Then, depending on your requirements, we allow simple actions to either mask, anonymize or remove the data. As for sensitive data, this is often open to interpretation. What is sensitive for you might not be for another business, and hence CluedIn allows you to flag records as sensitive. This will build up a data model specifically for your account that will be trained to look for records with similar traits and flag them automatically over time. 

# If CluedIn has four different databases, all storing my raw data - isn't that going to be a lot of storage?

The first thing to answer here is that you have complete control over what data you ingest into CluedIn. There are many cases where you will not want to bring in all the data. For the data that we do ingest, it is also worth mentioning that for certain types of data, we are not taking a full copy of the data but rather extracting what we need e.g., files only extract content and metadata. CluedIn also compresses all the data stored in the databases, meaning that the storage size is often much smaller than the source data itself. To put this in perspective, we have customers that have processed 100's of TB's of raw data, but in CluedIn, the databases will collectively be approximately 2 to 3 TB's. 

# Once the data is in CluedIn, how do I get it out?

CluedIn is designed to sit in-between source and target systems, and hence it is in our interest to make it extremely easy to get the data out of us. There are two main ways that we recommend this, but ask that in production, you don't use the CSV or File options - after all, this is typically the cause for siloed data in the first place! Firstly, our GraphQL API allows you to search through all the data in your CluedIn account and will return the results in JSON format. In addition, you can choose what properties you would like to select or project from the query to limit the data to only what you need. It is useful when you have other systems that want to "pull" data from CluedIn. Quite honestly, you won't find many systems that support making GraphQL queries or REST queries, and hence we offer another option that we think is more suitable. Secondly, we allow you to create data streams directly out of CluedIn (Push) to a target. This target could be a SQL database, an Apache Spark stream, direct to Power BI, or your Data Warehouse's dimension tables. 

# Considering that CluedIn uses OTS databases (off-the-shelf), can I access data directly from there?

We will not stop you from doing this, but we recommend that you only do this in a developer environment. If you want to talk directly to the databases, CluedIn has built you GraphQL interfaces to do this in a way that guarantees that you have remote access to only the data from your account. CluedIn ships with tools to administrate the different datastores, and hence we are influencing you to look in these datastores as a developer. The recommendation is to turn off native access to these datastores when you deploy into your production environment - in fact, by default, our Kubernetes setup has it disabled by default. 

# When CluedIn says it has prebuilt integrations, what about when we have customized our system so much?

The majority of integrations that CluedIn has been working with the assumption that you can change the underlying model of the source system. Hence, most of our integration will still require you to map the source objects into CluedIn to get the best out of your data. The integrations handle all the connection, delivery, and scheduling, paging, and sourcing of data. You, as a Data Architect, will need to map this into the Clue object. Fortunately, our data integration pattern makes this a simple task, and unlike other data integration platforms, we don't need you to tell us how everything wires together - that's our job!

# If CluedIn is connecting the data for us, won't that end up in a data model that is a mess?

Yes! Because guess what? Your data landscape is typically a mess! The goal of CluedIn is not to form the perfect model of your data for a particular use case - it is to find how the data is naturally connected and then allow you to project your ideal model for ANY use case you can think of. You will find that the model that we build (we use the Graph for this part) will match the model that your data finds to find links between your different systems. Then, using the same model, we give intuitive and simple-to-use tools to mutate this natural model to a more rigid model for the use cases you want in that particular model. The good news is that the Graph was designed for running these types of projects. They are as fast as an index lookup. It means that projecting a "dirty" model into a clean one is something that scales and performs really well.

# The Admin screen of CluedIn is great, but I want to automate things! How do I do this?

The good news is that the native CluedIn administration screen is built on top of the same REST API that you have direct access to as well. This means that you can do everything in the REST API that you can do in the user interface (and more!). It also means that you can script anything in CluedIn via our REST API, PowerShell, or other scripting languages. 

# I have made a change in CluedIn that requires me to re-process all the data. What do I do?

It will happen many times with your CluedIn account! It is highly typical and expected. CluedIn has been designed with the idea in mind that we will re-process the data all the time. Once you have made your change, you have quite a lot of control over the level of re-processing. You can re-process at a source level, globally, record level, or even something a little more custom, e.g., entity type level.

# Does CluedIn index everything?

Yes. Yes, we do. You can, however, influence the CluedIn engine to store data in a more optimum way. When you are setting up your Vocabularies, you have the chance to set a Vocabulary Key Data Type. It will influence how indexes are built, and we would strongly recommend doing this. Even if you do not do this, all your content will be searchable, but you can always make things faster and more efficient if you set up your Vocabularies correctly.

# With four databases, how does CluedIn guarantee transactions?

CluedIn ingests data into an enterprise service bus. It helps us guarantee the delivery of data. CluedIn utilizes "Eventual Consistency" for the different data stores. It means that CluedIn takes all records off the bus into a transactional log. The various databases will then read off the transaction log as fast as they can. It guarantees transactional support on your data but "eventual consistency" in the different data stores. With this setup and the fact that the different datastores will consume off the log in batches, it lessens the likelihood that the database will have issues with having a 100% consistency across the datastores simultaneously.

# Why is CluedIn written in C#? Isn't that slow?

For many reasons, the team behind CluedIn purposefully chose .net core and C# as the language for our processing engine. 

1: Our core development team has decades of combined experience in building large, scalable, and performant .net applications. 
2: The .NET environment has jumped leaps and bounds and has continued support for Microsoft and the community. The fact that it is open-source helped in the decision as well. 
3: .NET is designed to write very large applications and scale in maintaining, separation of concern, and ease of deployment. 
4: .net and C# is very much not slow. Compared to the majority of popular languages today, it is very fast. Some could argue that it is not as memory-efficient, but we think that the trade-offs to deliver solutions to you faster is well worth it. 

# I am not a C# developer. Does that mean I can't extend CluedIn?

The interfaces to communicate with CluedIn are actually HTTP, i.e. REST. Our C# layer essentially wraps this and talks REST. It means that you can actually use any language that you want to talk to CluedIn, however, there are some restrictions or limitations if you do this:

 - You cannot inject custom logic into the same application domain as CluedIn.
 - You will have to host your custom code in another host that is not CluedIn. 
 - You cannot currently use the crawler templates that are available only in C#. 

 Let's go with some examples for you. What if you are a Python, R, SQL, or GO developer? Let's say you want to build a custom integration that can be added through the user interface, but the code itself is written in Python. 

# What type of data is CluedIn not suited for?

There are many use-cases where CluedIn could be considered overkill or not fit for purpose. There are many use-cases that do not need all of the data preparation and cleaning pieces of CluedIn. It could very much be argued that IoT data doesn't suffer from the same problems or require the same data preparation than other data such as operation business data. Hence here is a list of use-cases or data that we don't think is necessarily suitable for CluedIn:

1: Processing Signal/IoT data that doesn't have data quality issues or doesn't need cataloging, governance - but instead needs to be made available in a Dashboard as fast as humanly possible. 
2: If you have a limited number of systems to integrate and there are no problems determining how the records are connected between the different systems. A good example would be if you just wanted to integrate your Dropbox account with your CRM. 
3: Where you do not want to move data. CluedIn copies data from sources to target. It won't necessarily take all the data, but it is an ingestion engine. You have to be very careful with this use case as many problems cannot be properly solved without copying the data.

