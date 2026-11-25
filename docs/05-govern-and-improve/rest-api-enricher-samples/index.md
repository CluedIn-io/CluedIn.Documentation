---
layout: cluedin
title: REST API enricher samples
parent: Govern & improve
nav_order: 35
has_children: true
permalink: /govern/rest-api-enricher-samples
content_type: landing
summary: Ready-made REST API enricher settings and scripts for specific external services, such as VIES, Dun & Bradstreet, Melissa, Logo.dev, and national company registries.
---

The [REST API enricher](/govern/enrichment/rest-api) can call almost any external service, but you write the JavaScript that builds the request and reads the response. The pages in this section give you that work already done for specific services: the enricher settings, the vocabulary keys to send, and a script you can paste in and adapt.

Each page is named after the external service it calls. It says which enricher version the script is for (V1 uses a process request script and a process response script, V2 uses a single process script) and whether the service needs an API key. For how to add the enricher and what each setting means, and for the `log`, `cache`, `stringEncoder` and `http` helper functions the scripts use, see [REST API enricher](/govern/enrichment/rest-api).

The scripts are starting points. Check the vocabulary keys in each script against your own data model, and review the service's terms and rate limits before you enrich a large number of golden records.

## Company registry lookups

These samples look up a company in a national business register by its registration number, and add the registered name, status, address and other register details to the golden record. Each one reads a single identifier from a vocabulary key, checks its format before calling the register, and adds properties under its own prefix (for example `brreg.name`).

Use the filter above the table to find a register by country, register or identifier, or to show only the registers that don't need an API key. On each sample page, open **Customize the script** above the process script to enter your own vocabulary keys and cache duration: the script and the **Vocabulary and Properties** field update as you type, ready to copy or download.

| Country | Register | Identifier | API key |
| ------- | -------- | ---------- | ------- |
| Australia | [ABN Lookup](/govern/rest-api-enricher-samples/abn-lookup-australia) | ABN | ABN Lookup GUID (free) |
| Brazil | [CNPJ](/govern/rest-api-enricher-samples/cnpj-brazil) | CNPJ | not needed |
| Canada | [Corporations Canada](/govern/rest-api-enricher-samples/corporations-canada) | Corporation number or business number | ISED API key (free) |
| Estonia | [e-Business Register](/govern/rest-api-enricher-samples/e-business-register-estonia) | Registry code | not needed |
| Finland | [Finnish Business Information System](/govern/rest-api-enricher-samples/ytj-finland) | Business ID (Y-tunnus) | not needed |
| Hong Kong | [Companies Registry](/govern/rest-api-enricher-samples/companies-registry-hong-kong) | Business Registration number | not needed |
| India | [MCA company master data](/govern/rest-api-enricher-samples/mca-india) | CIN | data.gov.in API key (free) |
| Japan | [gBizINFO](/govern/rest-api-enricher-samples/gbizinfo-japan) | Corporate number | gBizINFO API token (free) |
| Netherlands | [KVK](/govern/rest-api-enricher-samples/kvk-netherlands) | KVK number | KVK API key (paid) |
| New Zealand | [Companies Office NZBN](/govern/rest-api-enricher-samples/nzbn-new-zealand) | NZBN | NZBN API subscription key (free) |
| Norway | [Brønnøysund Register Centre](/govern/rest-api-enricher-samples/brreg-norway) | Organization number | not needed |
| Singapore | [ACRA](/govern/rest-api-enricher-samples/acra-singapore) | UEN | optional |
| South Korea | [OpenDART](/govern/rest-api-enricher-samples/opendart-south-korea) | DART corporation code | OpenDART API key (free) |
| Taiwan | [Ministry of Economic Affairs](/govern/rest-api-enricher-samples/moea-taiwan) | Unified business number | not needed |
