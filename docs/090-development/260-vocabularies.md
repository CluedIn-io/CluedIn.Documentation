---
layout: cluedin
title: Vocabularies
parent: Development
nav_order: 260
has_children: false
permalink: /development/vocabularies
tags: ["development","vocabularies"]
---

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
