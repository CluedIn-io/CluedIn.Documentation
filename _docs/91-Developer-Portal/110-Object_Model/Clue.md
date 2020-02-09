---
category: Developer
title: Clue
---

A Clue is the object model that CluedIn expects from third party systems in the form of data. It is the language that CluedIn speaks. It is the role of the developer that is implementing the CluedIn solution to map custom data formats into this universal data model. The Clue can take two main formats, JSON or XML. Despite what programming language is used to send this data to CluedIn, CluedIn only requires that you send it in either of these two formats. 

A Clue is an object model that CluedIn provide because it has generically mapped every object type that we commonly work with. It is an all purpose data structure and object model that can generically allow you to map Companies, People, Tasks, Documents or other custom types. This means that each Clue has some generic, catch-all properties, but also the ability to map properties that we have never seen before. 

It is the goal of a Clue to find other Clue or Entity objects that already exist within your CluedIn account and either merge, connect or enrich those records. 

A Clue is made up of generic properties and then a property bag to place all data that doesn’t not fit into a common well known object type. The Clue also has a way to add Entity Codes, which are a unique reference to an object. It also allows you to map Edges, which are references to other objects that may exist now, or in the future or never. 

For more advanced uses, the Clue will also allow you to map:

A Preview Image
Authors
Aliases
Change Verbs
Extracted Content e.g. Content of a file.
Uri
Tags
External Uri's

A Clue can have many Entity Codes associated with it. Imagine that you were integrating a record on a company and you had data on their local business identifier, website, LinkedIn Url, Facebook Url. These would all be considered ways to uniquely identify a company. Some are questionable as being unique identifiers, but most of the time we can accept that in more cases than not, they will be unique. For example, you could argue that a website is not a unique reference as chances are that you have purchased the website domain off a business that went bankrupt. This is completely fair, but we need to realise if this is the greater “evil” or not. More than often, a website will be unique to a company, but potentially not for a particular legal entity of that company, and for those times that it is not, we know that we might need to manually intervene in those records at a later point in time. 

An Entity Code is made up from 5 different pieces:

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
Origin:Salesforce
Organization Id:

But many would argue that an email is unique, and they are true in the case where we say that an email will uniquely identify “something”. It might not be a person, it may be a group or in some cases it may be a randomly generated email address that is used in automation or to track if an email is opened or not. This is why Vocabularies are very important. Vocabularies are your way to map certain properties to Core Vocabularies and in-turn you will be telling CluedIn to do some special processing on those values. One of the goals of the core vocabulary mappings is for CluedIn to make the bridge of Entity Codes between different integration sources. This also means that you don’t need to place any special business logic into your custom integrations. Your custom integrations should remain as simple as possible and only fetch and map data into Clues. If you find that there is not a suitable Core Vocabulary to map your data into then you will need to implement a new processor on the CluedIn server - your integrations are not a place to place this complex logic. Some good examples of Entity Code Id's are:

 - Passport Number
 - Employee Id
 - Twitter handle
 - Tax File Number
 - Social Security Number
 - Company Id
 - IBAN

Edges are a part of the Clue object that is responsible for pointing to reference objects that may or may not exist now or in the future. Edges are one of the key pieces of CluedIn that allow you to properly map data across many different data sources. To create an Edge, you will only need the Entity Type and the Id of the target record. Most importantly, you don't need to specify what source that CluedIn will actually find this record in. The only important part is that the Entity Type and Id need to 100% match. If you have this in place, then CluedIn will do all the work to join your data where a join is identified. 

Aliases are your way to set values that are a hint to a unique identity, but in no way are unique. Some good examples include references to a record that could uniquely identify different companies, people etc. The following are good examples of Aliases:

 - Phone Numbers
 - Nick Names
 - User Names
 - Initials
 - Addresses

The Created and Modified Dates for a Clue are important. If these are available in your source system, it is important to map these into your Clues. Do not manually set these Dates e.g. DateTimeOffset.UtcNow as this means that CluedIn will think that this record has changed, and then on evaluation we will realise that potentially, no properties were changed. CluedIn will generate a DiscoveryDate for you, so you do not need to manually set this. When searching for records in CluedIn and sorting by "New", CluedIn will always set the highest of the 3 Date Properties (Created, Modified, Discovered) and will set the SortDate for you automatically. 

Setting the Authors in your Clue is your way to add references to users that have modified, created or worked on your records. Each Clue can have many Authors. For setting Authors, you will set a PersonReference, which is very similar to an Entity Code, just without an Origin. 

Clues can be submitted to CluedIn in many ways. The preferred method is via the SDK's and Crawler Templates that we make available, however it can also be done using JSON. For example, you could post a Clue like so:

```json
{
  "clue": {
    "attribute-organization": "62d0a0d7-8871-4d0c-957e-71a24961d28e",
    "attribute-origin": "/Infrastructure/User#PeopleSoft:300036761",
    "attribute-appVersion": "1.8.0.0",
    "clueDetails": {
      "data": {
        "attribute-originProviderDefinitionId": "6b82efc3-3a50-42e5-b401-d217b7d83bae",
        "attribute-origin": "/Infrastructure/User#PeopleSoft:300036761",
        "attribute-appVersion": "1.8.0.0",
        "attribute-inputSource": "cluedin",
        "entityData": {
          "attribute-origin": "/Infrastructure/User#PeopleSoft:300036761",
          "entityType": "/Infrastructure/User",
          "name": "Blue,Matthew",
          "aliases": [
              "300036761",
              "36927"
          ],
          "codes": ["/Infrastructure/User#PeopleSoft:300036761"],
          "createdDate": "0001-01-01T00:00:00Z",
          "modifiedDate": "0001-01-01T00:00:00Z",
          "edges": {
            "outgoing": {
              "edge": {
                "attribute-type": "/root",
                "attribute-creationOptions": "Default",
                "attribute-from": "C:/Infrastructure/User#PeopleSoft:300036761",
                "attribute-to": "C:/Provider/Root#PeopleSoft:PeopleSoft"
              }
            }
          },
          "properties": {
            "attribute-type": "/Metadata/KeyValue",
            "property-peoplesoft.person.address": "860 West Levoy Drive",
            "property-peoplesoft.person.city": "Taylorsville",
            "property-peoplesoft.person.country": "USA",
            "property-peoplesoft.person.firstName": "Matthew",
            "property-peoplesoft.person.lastName": "Blue",
            "property-peoplesoft.person.postal": "84123",
            "property-peoplesoft.person.sex": "U",
            "property-peoplesoft.person.state": "UT"
          }
        }
      }
    }
  }
}
```
