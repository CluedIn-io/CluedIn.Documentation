---
layout: cluedin
title: Organization Vocabulary
parent: Legacy development documentation
grand_parent: Archive
nav_order: 270
permalink: /archive/legacy-development/organization-vocabulary
content_type: reference
redirect_from: ["/development/organization-vocabulary"]
source_path: docs/090-development/320-organization-vocabulary.md
tags: ["development","vocabularies"]
published: false
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

 This Vocabulary also includes Vocabulary mappings for all the popular Social Accounts and it is worth mentioning that if you have two Clues that have the same Social Accounts or Global Company Identifiers then by default, these Clues will merge with 100% confidence if they are valid representations of those values. 