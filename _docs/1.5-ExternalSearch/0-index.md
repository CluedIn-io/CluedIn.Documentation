---
category: Enricher
title: Enrichers
---

### Introduction

In CluedIn, an Enricher allows you to take input from data flowing through the processing pipeline and then lookup services (typically external API’s) as to enrich just a single particular entity. 

Imagine you have an API that allows you to lookup a company by an Identifier, Name or Website and it would bring back more, enriched data so that you could extend what data you had internally on that entity. A good example would be Crunchbase, Duns and Bradstreet or. Open Corporates. One can register for these API’s and lookup individual records via certain values and it may return zero or many results. 

At the same time, you could imagine that if you looked up via something like the name of a company, you might actually receive multiple results back. The External Search framework of CluedIn can help solve this particular situation as well as key identifier lookups as well. 

#### Installing my first Enricher

[I want to install my first Enricher](/docs/1.5-ExternalSearch/install-externalsearchprovider.html)

#### Building my first Enricher

[I want to build my first Enricher](/docs/1.5-ExternalSearch/build-externalsearchprovider.html)