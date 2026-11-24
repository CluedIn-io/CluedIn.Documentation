---
layout: cluedin
title: REST API enricher samples
parent: Govern & improve
nav_order: 35
has_children: true
permalink: /govern/rest-api-enricher-samples
content_type: landing
summary: Ready-made REST API enricher settings and scripts for specific external services, such as VIES, Dun & Bradstreet, Melissa, and Logo.dev.
---

The [REST API enricher](/govern/enrichment/rest-api) can call almost any external service, but you write the JavaScript that builds the request and reads the response. The pages in this section give you that work already done for specific services: the enricher settings, the vocabulary keys to send, and a script you can paste in and adapt.

Each page is named after the external service it calls. It says which enricher version the script is for (V1 uses a process request script and a process response script, V2 uses a single process script) and whether the service needs an API key. For how to add the enricher and what each setting means, and for the `log`, `cache`, `stringEncoder` and `http` helper functions the scripts use, see [REST API enricher](/govern/enrichment/rest-api).

The scripts are starting points. Check the vocabulary keys in each script against your own data model, and review the service's terms and rate limits before you enrich a large number of golden records.
