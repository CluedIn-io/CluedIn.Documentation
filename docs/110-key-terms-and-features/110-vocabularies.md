---
layout: cluedin
title: Vocabulary (Schema)
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

A vocabulary (schema) is a framework that defines how metadata is stored and organized within the system. A well-defined vocabulary is essential for maintaining data consistency, accuracy, and usability across an organization. It ensures that all stakeholders are working with consistent and reliable master data definitions and structures.

## Vocabulary characteristics

The **primary purpose** of vocabulary is to **hold vocabulary keys**. Vocabulary keys are your way to be able to describe properties that are coming in from data sources. A vocabulary is composed of multiple vocabulary groups and multiple vocabulary keys.

### Vocabulary prefix

The vocabulary prefix is a part of what we call the **full vocabulary key**. It is added before vocabulary key names for consistent naming, efficient searching, and data filtering. The prefix is stored in our databases and is given automatically when adding a vocabulary key to a given vocabulary.

Changing the prefix of an existing vocabulary could influence many records and would require their re-processing. For example, let's take the prefix `contact_person` and two vocabulary keys `firstName` and `lastName`. If you want to rename `contact_person` to `contactPerson`, it means that all golden records using `contact_person.firstName` and `contact_person.lastName` will need to be changed. Applying those changes on millions of golden records might require a bit of time.

### Vocabulary keys (attributes)

To maintain proper data lineage, it is recommended that the key name is set to the exact same value of the property name coming in from the source system.

### Vocabulary groups

A vocabulary group is an optional group for organizing vocabulary keys in a logical collection. It is used for aesthetic purposes and has no influence on your records.

For example, you could have the **Social** group for the vocabulary **Contact**. This group would have the following vocabulary keys:

- LinkedIn Profile
- X.com username
- Website
- Blog

If you do not provide any group for your vocabulary keys, they will be located in a group called **Ungrouped Keys**.

## Vocabulary usage

### One vocabulary per source

Even if it is tempting to reuse the vocabulary across multiple sources, you should keep the vocabulary **close to your sources** for the lineage purposes. This gives you better flexibility when working with clean projects, rules, or deduplication projects because you'll know where a specific vocabulary key is coming from.

To start using what we call _shared vocabulary_, you need to **map one vocabulary key to another**. For example, let's take a field called **Email** from the CRM source. You would use a vocabulary key called `CRM.contact.email`. The `CRM.contact` would be the prefix of a vocabulary (which is probably called `CRM Contact`), and `email` would be a child vocabulary key of `CRM Contact`. So, the full vocabulary key is `CRM.contact.email`.

Now, you add a field called **Email** from the ERP source. In this case, you would use a vocabulary key called `ERP.contact.email`. The `ERP.contact` would be the prefix of a vocabulary (which is probably called `ERP Contact`), and `email` would be a child vocabulary key of `ERP Contact`. So, the full vocabulary key is `ERP.contact.email`.

Obviously, those 2 keys—`CRM.contact.email` and `ERP.contact.email`—represent the **same meaning**, so you would want to have a single **shared vocabulary key** called `contact.email` to be used in your golden records. This is possible to achieve by mapping those 2 keys to the shared vocabulary key called `contact.email`. This means that the data will be **flowing towards the shared vocabulary key**, and the values of `CRM.contact.email` and `ERP.contact.email` will now all be located in `contact.email` (as shown in the table below).

| Source | Vocabulary | Vocabulary key | Maps to |
|--|--|--|--|
| CRM | CRM.contact | email | contact.email |
| ERP | ERP.contact | email | contact.email |

By applying this principle, you can keep your lineage and have better flexibility and agility. However, it is up to you to decide when and if you want to map vocabulary keys with the same meaning to a shared vocabulary key or keep them separate.

### Entity type vs. vocabulary

When you map your data in CluedIn, you can map it to one entity type and one vocabulary. However, a vocabulary can be shared among different entity types and can represent only a partial aspect of the golden record. So, the following statements are true when describing a golden record:

- You can assign only **one entity type** to a golden record.
- You can use **multiple vocabularies** for a golden record.

By distinguishing between entity type and vocabulary, we decouple the value aspect of records from their modeling aspect. This approach provides greater flexibility in modeling and allows for evolution with changing use cases.

## Core vocabularies

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

```
 hubspot.contact.contactName - Provider Level
 	lego.sales.contact.fullName - Department Level
 	lego.marketing.contact.leadName - Department Level
 		lego.contact.Name - Company Level
 			person.fullName - CluedIn Core Vocabulary
```

## Useful resources

- [Modeling approaches](/management/data-catalog/modeling-approaches)

- [Create and manage a vocabulary](/management/data-catalog/vocabulary)

- [Create and manage vocabulary keys](/management/data-catalog/manage-vocabulary-keys)