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

A vocabulary is a framework that defines how metadata is stored and organized within the system. A well-defined vocabulary is essential for maintaining data consistency, accuracy, and usability across an organization. By providing a standardized framework, a vocabulary contributes to effective data integration, improved decision making, and streamlined operations. It ensures that all stakeholders are working with consistent and reliable master data definitions and structures. For more information, see [Vocabulary](/management/data-catalog/vocabulary).

The primary purpose of vocabulary is to hold vocabulary keys. Vocabulary keys are your way to be able to describe properties that are coming in from data sources. To maintain proper data lineage, it is recommended that the Key Name is set to the exact same value of the property name coming in from the source system. For example, if you are integrating data from a CRM system and one of the properties is named "Column_12", then even though it is tempting to change the Key Name, we would recommend that you maintain that as the Key Name and that you can set the Display Name as something different for aesthetic reasons. For more information, see [Vocabulary keys](/management/data-catalog/vocabulary-keys).

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
