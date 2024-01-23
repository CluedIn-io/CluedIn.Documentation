---
layout: cluedin
title: Common Design Decisions
parent: Development
nav_order: 390
has_children: false
permalink: /development/common-design-decisions
tags: ["development","architecture"]
---

# Multiple Email Addresses

There is a special Core Vocaulary for mapping multiple Email Addresses instead of having to map just one. It is the CluedIn.Core.Data.Vocabularies.CluedInOrganization.EmailAddresses

# Integrating Databases with Seed Identity

It is quite normal for Databases to generate Identifiers for records starting from the Id of 0 and then incrementing this Id for every new record by 1. This might lead you to think that this will not be a unique reference to a record, but rest assured that it can be. If you need to create an Entity Code out of this record, you have to remember that this Entity Code will also contain a Entity Type, Code Origin and an Identifier. 

# Flattening Records

Without a doubt, if two clues or entities have the same Entity Code then they will be flattened into the same record and will have the history of both clues contained within it. It can sometimes be hard to determine if records should flatten or not, but this is more a business based decision than a technical one. 

# Build Hierarchies or not?

There are many times where you will have data that has a hierachy to it. For example, imagine a company that has a parent or mother company. If we had the same Entity Codes for these 2 records then CluedIn will treat these as the same company. This is not always the intention of your data project. The other option is to create hierarchies where if these two company objects need to be linked, instead of merged - you will often need to look at creating edges between these objects instead of entity codes. 

The most common use-cases with hierarchies is typically for companies and people. When it comes to companies, you can have a varied detail of hierarchy, but the following is what CluedIn usually includes: 

 - Ultimate Parent—The very top company listed in a company hierarchy and the ultimate controlling company within a corporate structure.  

 - Parent—The top tier within an organization but may not be the “ultimate parent.” It should have other companies reporting to it, and would itself report to another legal entity. In many cases the terms, “parent” and “ultimate parent” are used synonymously.  

 - Subsidiary—Separate corporate legal entity owned by the company at 50.1% or more.  

 - Joint Venture—A business in which two or more companies share responsibility and ownership.  

 - Affiliate—A separate legal entity in which there is an ownership interest by the parent company of less than 50%.  

 - Division, Unit, Factory or Plant—An internal unit of a company, not incorporated or a separate legal entity. Usually tends to have many employees.  

 - Branch—An internal unit of a company, not incorporated or a separate legal entity. Usually tends to have a small number of employees.  

 - Group—Corporate classification grouping “like” industries or businesses,  

 - Holding—A business whose voting stock is owned to influence its board, policies, and management.  

 - Non–Operating Entities (Shells)—Legal non-operating entities (displayed at the bottom of its immediate parent’s hierarchy). 

# How to you build these hierachies in CluedIn?

 There are some easy, easier and harder approaches that you can take. If you enable our Duns and Bradstreet, Lexis Nexus or Open Corporates external search providers then CluedIn will use this to be able to build hierarchies. The next approach is to handle this all manually which mappings of edges between companies if you already have this data and hierachy in your own data. The other is to use CluedIn's fuzzy-linking engine to build the hierarchies automatically for you. 