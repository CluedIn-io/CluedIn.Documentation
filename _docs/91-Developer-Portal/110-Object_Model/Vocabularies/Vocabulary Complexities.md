---
category: Developer
title: Vocabulary Complexities
---

There are some Vocabulary mappings that are a bit more complex to understand than others. This documentation aims to help answer some of the common occurrences of complex mappings and how to resolve them. 

## Mapping an Address where there is multiple address values

Often you will find that a system allows you to map multiple address values e.g. Primary Address, Work Address, Home Address, Postal Address and other permutations. However you will find the Core Vocabularies only allow you to map one address. The answer is that you can create multiple Clues from one record and each Clue will have a different address mapping in it. It is at this time that we will remind you that a Row or a Record in a source system does not dictate a single Clue. A Row of data might actually create multiple clues and this is an example where it would be the case. 

## Mapping a record that has multiple emails

It can be said that an email is unique. It can also be said that an email doesn't necessarily identify a person. If you find that you are processing records that have multiple emails then instead of mapping this to the Email Vocabulary, you can create many Entity Codes for the emails and make sure that you specific the Type in the Entity Code as /Infrastructure/User. CluedIn will do the work on the server to validate if this is in fact an email address for a person or a group or a mailbox. If it can't get this answer from the mail server, then it will use the classification engine in CluedIn to attempt to strongly type the email. Similar to the Address question above, you can split it into multiple Clues and set the Email Vocabulary to a different email on each Clue. The difference will be that one will generate many Clues, the other will generate just one. 

## What happens if there is no Vocabulary for me to map into?

This will happen often and it can be due to the following types of situations:

 - CluedIn has not mapped this into their Core Vocabulary and that a request should be made to do so to your CluedIn Account Manager. 
 - There is no mapping because the property is so specific to your data that it cannot be generically handled in a Core Vocabulary. 
 - That the Core Vocabulary has a name that is not intuitive for you to find e.g. it may be called "Job Title" but you are looking for "Position" or some other synonym. 

To understand why you would want to add new Vocabularies for mapping values from source systems, you need to understand what the Vocabularies are for. Please refer to the Vocabularies section to validate this. 

To answer the question posed here, you essentially need to answer "Will we see many examples of data in source systems that match this Vocabulary and is it likely that you would want to do some standard processing on this data as well". For example, you might find that you have a customer lifetime score that spans across many systems and it is called different things in different systems and is also de-normlised in the way it is represented such as one will use decimal values, one uses integers and the other uses strings - then this is a prime candidate to introduce a Vocabulary to process and standardise this data.