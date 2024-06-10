---
layout: cluedin
title: Vocabularies
parent: Key terms and features
nav_order: 11
has_children: false
permalink: /key-terms-and-features/vocabularies
tags: ["development","vocabularies"]
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

Vocabularies are your way to be able to describe properties that are coming in from datasources. Each Vocabulary has the following properties to set:

 - Key Name
 - Display Name
 - Data Type (of value)
 - Description
 - Visibilty
 - Editable
 - Removable
 - Personally Identifying

 To maintain proper data lineage, it is recommended that the Key Name is set to the exact same value of the property name coming in from the source system. 

 For example, if you are integrating data from a CRM system and one of the properties is named "Column_12", then even though it is tempting to change the Key Name, we would recommend that you maintain that as the Key Name and that you can set the Display Name as something different for aesthetic reasons. 

 The goal of a Vocabulary is to map into a Core Vocabulary (eventually) if possible. 

 If you find that you have multiple properties from the source systems that map into the same Vocabulary Key, then it is recommend to only map one and keep the others as non-mapped Vocabulary Keys to Core Vocabularies. An example would be if you have 3 properties called Address1, Address2, Address3 then only one of these should map into the Core Vocabulary for a Company Address. You can concatenate all Address Columns into one and set it as the Core Vocabulary Key, but you might need to make a decision on what is the best way to implement this piece. 

 There are many times where certain Vocabularies map complex objects. Let's assume for a moment that a particular source system gives you the address of a company in a complex object instead of a single string. This would mean that you receive data that contains a Street Number, Street Name, City, Post Code and more. It is typical that you will create Vocabularies that flatten this object and then map it into the Core CluedIn Vocabularies. To support the Mesh API piece of CluedIn, you might need to reconstruct this address object when you need to mutate the source system. For this reason, you will find that you have an Extension Method on your Vocabularies called "DataAnnotations". Data Annotations are a way for you to instruct to the Mesh API that when you need to update part of this Address, that in fact, you will need to send the entire Address object back to the source system, instead of simply sending the changed part e.g. Street Name. 

 Vocabularies are allowed (and designed) to be hierarchical in nature. This means that you can have many (max 10) levels of hierarchy in your Vocabularies. This is to allow you to be able to map Source systems into a Company, Department, Team or other levels. Here is a simple example of how a Vocabulary Key could map from source to Core.

```yaml
 hubspot.contact.contactName - Provider Level
 	lego.sales.contact.fullName - Department Level
 	lego.marketing.contact.leadName - Department Level
 		lego.contact.Name - Company Level
 			person.fullName - CluedIn Core Vocabulary
```

NOTE: When you map your Vocabularies, by default, CluedIn will only store the data for the final mapped key. For example, if you mapped from sap.person.jobTitle to user.jobTitle then CluedIn would not store the values of that key in both sap.person.jobTitle and user.jobTitle. If you would like to change the behaviour, make sure that you have one key that maps to user.jobTitle and one key that does not for the same input key.

## Vocabulary grouping

For aesthetic and organisation reasons, Vocabulary Groupings allow developers to group Vocabulary keys by logical groupings. There is no performance or processing benefit for this, it is only for aesthetics. 

Imagine that you are wanting to give your CluedIn users the ability to easily filter and find a property on an object. By adding intuitive Vocabulary Groupings, you will be helping the user find this data. For example, placing all Account Numbers, IBAN, SWIFT and Bank Type properties into a Vocabulary Grouping called "Bank Details" will make it easier for users to consume this data. 

## Core vocabularies

Core Vocabularies are where a lot of the “smarts” in CluedIn exist. If you map your custom integration sources' keys into Core Vocabulary keys, there is a high likelihood that something will be done on the data to your advantage. For example, if you map a phone number into a Core Vocabulary Phone Number Key then CluedIn will, amongst other things: 

- Create new normalised representations of the phone number in industry standards e.g. E164. 
- Will see if we can confidentially identify or merge records based off this phone number.

### Important Core Vocabularies

 - EditUrl
 - PreviewUrl
 - Body

The role of Core Vocabularies is to merge records from different systems based off knowing that these Clues will have a different Origin. As you have already learnt about Entity Codes, they need to be exact for a merge to occur and simply the change of the Origin could cause records not to merge. 

More often than not, you might find that you will need to introduce new Vocabularies that help you map data between different systems. It is however that you will not introduce your own Core Vocabularies. Core Vocabularies are what CluedIn produce and if you need to introduce your own Vocabulary mappings then you will build your own keys. Each key that you will introduce will need you to introduce a Processor in the processing pipeline that instructs CluedIn how to process data in those keys. It could be something as simple as it "Lowercases" the values or it could be as complex as "It runs fuzzy string manipulation over the values".

As you learnt from the Vocabularies section, you can have a hierarchy of Vocabularies. The Core Vocabularies from CluedIn are the highest possible root in this tree. You cannot map Core Vocabularies down to lower levels, but you should map lower level Vocabularies up to CluedIn Core Vocabularies. 

Core Vocabularies do not include the namespace for a source system. It will typically have the Entity Type, the name of the key - or if it is a nested key like and address, it will have the nesting shown in the key name e.g. 

 - organization.industry
 - organization.address.city
 - organization.address.countryName
 - person.age
 - person.gender

These are all valid Core Vocabularies. 

### Can I add my own Core Vocabularies?

Although you can, we suggest that you do not. The reason is mainly due to upgrade support and making sure your upgrades are as seamless and automated as possible. 

### How do I nest my Vocabularies?

Instead of creating a VocabularyKey in your Vocabularies, you can create a CompositeVocabularyKey. This will ask you to set a Key and a Base Key. This is how you will build up your tree of Vocabularies. 
