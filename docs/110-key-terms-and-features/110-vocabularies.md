---
layout: cluedin
title: Vocabularies (Schema)
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

A vocabulary is a framework that defines how metadata is stored and organized within the system. A well-defined vocabulary is essential for maintaining data consistency, accuracy, and usability across an organization. By providing a standardized framework, a vocabulary contributes to effective data integration, improved decision making, and streamlined operations. It ensures that all stakeholders are working with consistent and reliable master data definitions and structures. For more information, see [Vocabulary](/management/data-catalog/vocabulary).

The **primary purpose** of vocabulary is to **hold vocabulary keys**. Vocabulary keys are your way to be able to describe properties that are coming in from data sources.

A vocabulary is composted by multiple vocabulary groups and multiple vocabulary keys.

### Why is the prefix of vocabulary so important?

The prefix of a vocabulary will be part of what we call the **full vocabulary key**, this will be name of the attribute being stored in our databases and will be given automatically when adding a vocabulary key to a given vocabulary.

Changing the _prefix_ of an existing vocabulary could influence many of the records and would re-require a `re-processing` of the golden records (automatically when changing the name of the UI).

Let's take the prefix `contact_person` and a vocabulary key called `firstName` and `lastName`.

If you want to rename `contact_person` to `contactPerson`, it means that now, in _all the golden records_ using `contact_person.firstName` and `contact_person.lastName` will need to be changed. Please, be mindful that applying those changing on millions of golden records may require a bit of time.

### What is the different between Entity Type and Vocabulary?

When you map your data in CluedIn, you can have a one to one. However, vocabulary can be share among different entity type or may only represent a partial aspect of the golden record.

For example:

- There can be only 1 entity Type assigned to a golden record.
- You can have multiple vocabularies being used for a given golden record.

By dividing the notion of Entity Type and Vocabulary, we are de-coupling the "value" aspect of the records from its "modeling" aspect, opening for better flexibility when it comes to modeling and be to evolve with your use-cases.

## Vocabulary Groups

A vocabulary group is an optional group of vocabulary keys. It helps re-group some of the vocabulary keys in logical grouping.

For example having a "Social" groups for the Vocabulary "Contact".

The social group would have:

- LinkedIn Profile
- X.com username
- Website
- Blog

It is aestetic and has no influences on your record.

If you do not provide any grouping for you vocabulary keys, they will be located under a group called `Ungrouped Keys`.

## Vocabulary Keys (Attribute)

To maintain proper data lineage, it is recommended that the Key Name is set to the exact same value of the property name coming in from the source system.

For example, if you are integrating data from a CRM system and one of the properties is named "Column_12", then even though it is tempting to change the Key Name, we would recommend that you maintain that as the Key Name and that you can set the Display Name as something different for aesthetic reasons. For more information, see [Vocabulary keys](/management/data-catalog/vocabulary-keys).



**Core vocabularies**

Core vocabularies are where a lot of the “smarts” in CluedIn exist. If you map your custom integration sources' keys into core vocabulary keys, there is a high likelihood that something will be done on the data to your advantage. For example, if you map a phone number into a core vocabulary Phone Number Key, then CluedIn will, amongst other things: 

- Create new normalized representations of the phone number in industry standards e.g. E164. 
- Will see if we can confidentially identify or merge records based off this phone number.

The role of core vocabularies is to merge records from different systems based on knowing that these clues will have a different origin. As you have already learnt about entity codes, they need to be exact for a merge to occur and simply the change of the origin could cause records not to merge.

Although you can add your own core vocabularies, we suggest that you do not. The reason is mainly due to upgrade support and making sure your upgrades are as seamless and automated as possible. 

Core vocabularies do not include the namespace for a source system. It will typically have the entity type, the name of the key - or if it is a nested key like and address, it will have the nesting shown in the key name:

 - organization.industry
 - organization.address.city
 - organization.address.countryName
 - person.age
 - person.gender

 Vocabularies are allowed (and designed) to be hierarchical in nature. This means that you can have many (max 10) levels of hierarchy in your vocabularies. This is to allow you to be able to map source systems into a Company, Department, Team, or other levels. Here is a simple example of how a vocabulary key could map from source to core.

```yaml
 hubspot.contact.contactName - Provider Level
 	lego.sales.contact.fullName - Department Level
 	lego.marketing.contact.leadName - Department Level
 		lego.contact.Name - Company Level
 			person.fullName - CluedIn Core Vocabulary
```
