Clue

A Clue is the object model that CluedIn expects from third party systems in the form of data. It is the role of the developer that is implementing the CluedIn solution to map custom data formats into this ubiquitous data model. The Clue can take two main formats, JSON or XML. Despite what programming language is used to send this data to CluedIn, CluedIn only requires that you send it in either of these two formats. 

A Clue is an object model that CluedIn provide because it has generically mapped every object type that we commonly work with. It is an all purpose data structure and object model that can generically allow you to map Companies, People, Tasks, Documents or other custom types. This means that each Clue has some generic, catch-all properties, but also the ability to map properties that we have never seen before. 

It is the goal of a Clue to find other Clue or Entity objects that already exist within your CluedIn account and either merge, connect or enrich those records. 

A Clue is made up of generic properties and then a property bag to place all data that doesn’t not fit into a common well known object type. The Clue also has a way to add Entity Codes, which are a unique reference to an object. It also allows you to map Edges, which are references to other objects that may exist now, or in the future. 

For more advanced uses, the Clue will also allow you to map:

A Preview Image
Authors
Aliases
Change Verbs
Extracted Content e.g. Content of a file.
Uri
External Uri's

A Clue can have many Entity Codes associated with it. Imagine that you were integrating a record on a company and you had data on their local business identifier, website, LinkedIn Url, Facebook Url. These would all be considered ways to uniquely identify a company. Some are questionable as being unique identifiers, but most of the time we can accept that in more cases that not, they will be unique. For example, you could argue that a website is not a unique reference as chances are that you have purchased the website domain off a business that went bankrupt. This is completely fair, but we need to realise if this is the greater “evil” or not. More than often, a website will be unique to a company and for those times that it is not, we know that we might need to manually intervene in those records at a later point in time. 

An Entity Code is made up on 4 different pieces:

Entity Type
Provider Definition Id
Id
Origin
Organization Id

This combination will allow us to achieve absolute uniqueness across any datasource that we interact with. 

If two Clues have exactly the same EntityCode, they have a 100% chance of merging. More often than not, Clues need to be processed to turn what is usually unique into something that would overlap with another system. For example, if we integrated two records on the same person from two different systems with exactly the same email address then this would never merge. 

EntityType: /Person
Provider Definition Id: 
Id:john.smith@fakecompany.com
Origin:
Organization Id:

But many would argue that an email is unique, and they are true in the case where we say that an email will uniquely identify “something”. It might not be a person, it may be a group or in some cases it may be a randomly generated email address that is used in automation or to track if an email is opened or not. This is why Vocabularies are very important. Vocabularies are your way to map certain properties to Core Vocabularies and in-turn you will be telling CluedIn to do some special processing on those values. One of the goals of the core vocabulary mappings is for CluedIn to make the bridge of Entity Codes between different integration sources. This also means that you don’t need to place any special business logic into your custom integrations. Your custom integrations should remain as simple as possible and only fetch, transform and map data into Clues. If you find that there is not a suitable Core Vocabulary to map your data into then you will need to implement a new processor on the CluedIn server - your integrations are not a place to place this complex logic. 

Edges are a part of the Clue object that is responsible for pointing to reference objects that may or may not exist now or in the future. 