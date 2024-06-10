---
layout: cluedin
title: Person Entity Type
parent: Development
nav_order: 220
has_children: false
permalink: /development/person-entity-type
tags: ["development","entity-types","entities"]
published: false
---

The Person Entity Type is a special Entity Type that if you are to set your Clue objects with this Entity Type, then many "smarts" will kick in on the CluedIn processing server. 

Examples of this "smarts" include: 

 - Map First, Middle and Last Names given statistical models e.g. If you have set the Name of your Clue as "John Henry Smith", then CluedIn will attempt to set the First Name, Middle Name and Last Name if it passes our inbuilt models and tests.
 - Automatically normalise Phone Numbers to E164, RFC3966 and International standards.
 - Attempts will be made to validate if an email address is for a person or a group/contact.