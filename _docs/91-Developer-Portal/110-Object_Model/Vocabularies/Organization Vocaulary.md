---
category: Developer
title: Organization Vocaulary
---

The CluedIn Organization Vocabulary is a very important Vocabulary. By mapping your custom Clue Vocabularies into this core Organization Vocabulary, a lot of "smarts" will kick in on the processing server to help automate cleaning, normalization, insights and more. 

This Vocabulary also includes many inbuilt global company identifiers, including:

 - Duns
 - LEI
 - SIC
 - CVR
 - Company House
 - Local Business Id
 - Perm Id

 Each of the Company Identifiers above will have their own Vocabularies, but all will be mapped to a Core Vocabulary called organization.codes.companyNumber. If you find that you introduce your own new company identifiers, make sure that it also maps to organization.codes.companyNumber. This means that when you would like to use the data, instead of having to search or filter on each different company Id type (e.g. CVR) you can just use the organization.codes.companyNumber which aggregates all into one. 

 This Vocabulary also includes Vocabulary mappings for all the popular Social Accounts and it is worth mentioning that if you have two Clues that have the same Social Accounts or Global Company Identifiers then by default, these Clues will merge with 100% confidence if they are valid representations of those values. 