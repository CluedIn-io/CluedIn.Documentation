---
category: Developer
title: Organization Entity Type
---

The Organization Entity Type is a very special Entity type, where by marking one of your Clues as an Organization, then many "smarts" of the CluedIn processing engine will kick in. 

Here is a list of the types of processing that will happen on a Clue if you make the Entity Type of that clue an "/Organization".

## Fuzzy Merging

If you have decided to make your Clue objects of type "/Organization", then you will find that by default, CluedIn will run Fuzzy Merging on your records. By default, we will use the Vocabularies that are mapped into the "Organization" Vocabulary as "features" that play a role in the Fuzzy Merging of records. This means that if the properties of your Clue are similar enough to be over the built in statistical thresholds, then CluedIn will merge many records for you automatically. 

## Web Crawling

If you have enabled the CluedIn Web Crawler (External Search) and that you have mapped a value for the Organization Website Vocabulary, then the inbuilt Web Crawler for CluedIn will lookup that website and will crawl the website for extra information. 

