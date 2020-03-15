---
category: Developer
title: Core Vocabularies
---

Core Vocabularies are where a lot of the “smarts” in CluedIn exist. If you map your custom integration sources into Core Vocabularies, there is a high likelihood that something will be done on the data to your advantage. For example, if you map a phone number into the Core Vocabulary Phone Number then CluedIn will, amongst other things: 

- Create new normalised representations of the phone number in industry standards e.g. E164. 
- Will see if we can confidentially identify or merge records based off this phone number.

## Important Core Vocabularies

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

## Can I add my own Core Vocabularies?

Although you can, we suggest that you do not. The reason is mainly due to upgrade support and making sure your upgrades are as seamless and automated as possible. 

## How do I nest my Vocabularies?

Instead of creating a VocabularyKey in your Vocabularies, you can create a CompositeVocabularyKey. This will ask you to set a Key and a Base Key. This is how you will build up your tree of Vocabularies. 