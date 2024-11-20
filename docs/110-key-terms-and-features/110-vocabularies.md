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

### One vocabulary per source to keep the lineage

Even if it is tempting to re-use vocabulary across the multiple sources, you should keep the Vocabulary **close to your sources**.

This gives you better flexibility as you can target your clean-project and/or rules and/or deduplication project to know where this vocabulary key is coming from.

To start using what we called "Shared Vocabulary", you needs to use the feature of "Mapping" a key to another Vocabulary Key.

For example, let's take a field called "Email", from a source "CRM".

You should use a vocabulary key called: "CRM.contact.email".

The `CRM.contact` would be the prefix of a Vocabulary, probably called "CRM Contact" and `email` would be a child vocabulary key of "CRM Contact". Producing a full key of `CRM.contact.email`.

If you add now a source ERP, you would use a prefix such as `ERP.contact` which would be the prefix of a Vocabulary, probably called "ERP Contact" and `email` would be a child vocabulary key of "ERP Contact". Producing a full key of `ERP.contact.email`.

Obviously, those 2 keys called (`CRM.contact.email` and `ERP.contact.email`) represent the **same meaning**, so you would want in your golden record to have a single **shared vocabulary key** called `contact.email`.

This is possible by mapping those 2 keys to the shared vocabulary key called `contact.email`.

Bear in mind, it means the data will be **flowing towards the shared vocabulary key** and the values of `CRM.contact.email` and `ERP.contact.email` will now all be located in `contact.email`.

Such as:

| Source Type | Vocabulary | Vocabulary Key | Maps to |
|--|--|--|
| CRM | CRM.contact | email | contact.email |
| ERP | ERP.contact | email | contact.email |

By applying this principle, you can keep your lineage but as well it gives you better flexibility and better agility. As you can "map to" the shared vocabulary key only when you feel it is "ready". Maybe you want to clean it before, maybe you do want to keep it separate...

### What is the difference between Entity Type and Vocabulary?

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

## Vocabulary Keys (attribute)

To maintain proper data lineage, it is recommended that the Key Name is set to the exact same value of the property name coming in from the source system.


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
