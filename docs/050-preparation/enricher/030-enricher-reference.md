---
layout: cluedin
nav_order: 3
parent: Enricher
grand_parent: Preparation
permalink: /preparation/enricher/enricher-reference
title: Enricher reference
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article, you will find reference information about the built-in enrichers available in CluedIn.

Please note that the enrichers are not included in the CluedIn license. Each enricher is an open-source package provided by the CluedIn team for free to help you enrich your golden records with information from external sources.

{:.important}
If you need a custom enricher, use the [REST API enricher](/preparation/enricher/rest-api) or contact us, and we will build one for you.

## Azure OpenAI

The [Azure OpenAI](/preparation/enricher/azure-openai) enricher allows you to enhance data quality by providing more complete, current, and detailed information for your golden records. It supports the following endpoints:

- `{baseUrl}/openai/deployments/{deploymentName}/completions?api-version=2022-12-01`
    
- `{baseUrl}/openai/deployments/deploymentName}/chat/completions?api-version=2024-06-01`

| Package name | Package version | Source code |
|--|--|--|
| CluedIn.Enricher.AzureOpenAI | 4.4.0 | [Source code](https://github.com/CluedIn-io/CluedIn.Enricher.AzureOpenAI/releases/tag/4.4.0) |


## Brreg

The [Brreg](/preparation/enricher/brreg) enricher retrieves a wide range of information about Norwegian and foreign businesses operating in Norway. It supports the following endpoints:

- `http://data.brreg.no/enhetsregisteret/api/enheter/{id}`, where `{id}` is the Brreg code.

- `http://data.brreg.no/enhetsregisteret/api/enheter?page=0&size=30&navn={name}`, where `{name}` is the company name.

| Package name | Package version | Source code |
|--|--|--|
| CluedIn.Provider.ExternalSearch.Bregg | 4.4.0 | [Source code](https://github.com/CluedIn-io/CluedIn.Enricher.Brreg/releases/tag/4.4.0) |
| CluedIn.Provider.ExternalSearch.Bregg | 4.0.1 | [Source code](https://github.com/CluedIn-io/CluedIn.Enricher.Brreg/releases/tag/4.0.1) |
| CluedIn.Provider.ExternalSearch.Bregg | 4.0.0 | [Source code](https://github.com/CluedIn-io/CluedIn.Enricher.Brreg/releases/tag/4.0.0) |


## BvD

The BvD enricher retrieves a wide range of information about companies.

| Package name | Package version | Source code |
|--|--|--|
| CluedIn.Provider.ExternalSearch.BvD | 4.4.0 | [Source code](https://github.com/CluedIn-io/CluedIn.Enricher.BvD) |

## Clearbit

The [Clearbit](/preparation/enricher/clearbit) enricher retrieves company logo and domain information. It supports the following endpoint:

- `https://autocomplete.clearbit.com/v1/companies/suggest?query=`

| Package name | Package version | Source code |
|--|--|--|
| CluedIn.Provider.ExternalSearch.ClearBit | 4.4.0 | [Source code](https://github.com/CluedIn-io/CluedIn.Enricher.ClearBit/releases/tag/4.4.0) |
| CluedIn.Provider.ExternalSearch.ClearBit | 4.1.1 | [Source code](https://github.com/CluedIn-io/CluedIn.Enricher.ClearBit/releases/tag/4.1.1) |
| CluedIn.Provider.ExternalSearch.ClearBit | 4.1.0 | [Source code](https://github.com/CluedIn-io/CluedIn.Enricher.ClearBit/releases/tag/4.1.0) |
| CluedIn.Provider.ExternalSearch.ClearBit | 4.0.0 | [Source code](https://github.com/CluedIn-io/CluedIn.Enricher.ClearBit/releases/tag/4.0.0) |

## Companies House

The [Companies House](/preparation/enricher/companies-house) enricher retrieves information about UK companies. This enricher uses the company name to return public information including registered office address, filing history, and so on.

The Companies House enricher supports the following endpoints:

- `https://api.companieshouse.gov.uk/search/company/{companyNumber}`, where `{companyNumber}` is the Companies House number – this endpoint is called when the Companies House number is provided.

- `https://api.companieshouse.gov.uk/search/companies?q={name}`, where `{name}` is the company name – this endpoint is called when the Companies House number is not provided.

| Package name | Package version | Source code |
|--|--|--|
| CluedIn.Provider.ExternalSearch.CompanyHouse | 4.4.0 | [Source code](https://github.com/CluedIn-io/CluedIn.Enricher.CompanyHouse/releases/tag/4.4.0) |
| CluedIn.Provider.ExternalSearch.CompanyHouse | 4.0.1 | [Source code](https://github.com/CluedIn-io/CluedIn.Enricher.CompanyHouse/releases/tag/4.0.1) |
| CluedIn.Provider.ExternalSearch.CompanyHouse | 4.0.0 | [Source code](https://github.com/CluedIn-io/CluedIn.Enricher.CompanyHouse/releases/tag/4.0.0) |

## CVR

The [CVR](/preparation/enricher/cvr) enricher retrieves a wide range of information about companies registered in Denmark. It supports the following endpoint:

- `http://{username}:{password}@distribution.virk.dk/cvr-permanent/_search`, where `{username} and {password}` are the valid credentials for your CVR account.

| Package name | Package version | Source code |
|--|--|--|
| CluedIn.Provider.ExternalSearch.CVR | 4.4.0 | [Source code](https://github.com/CluedIn-io/CluedIn.Enricher.CVR/releases/tag/4.4.0) |
| CluedIn.Provider.ExternalSearch.CVR | 4.1.1 | [Source code](https://github.com/CluedIn-io/CluedIn.Enricher.CVR/releases/tag/4.1.1) |
| CluedIn.Provider.ExternalSearch.CVR | 4.1.0 | [Source code](https://github.com/CluedIn-io/CluedIn.Enricher.CVR/releases/tag/4.1.0) |
| CluedIn.Provider.ExternalSearch.CVR | 4.0.2 | [Source code](https://github.com/CluedIn-io/CluedIn.Enricher.CVR/releases/tag/4.0.2) |
| CluedIn.Provider.ExternalSearch.CVR | 4.0.1 | [Source code](https://github.com/CluedIn-io/CluedIn.Enricher.CVR/releases/tag/4.0.1) |
| CluedIn.Provider.ExternalSearch.CVR | 4.0.0 | [Source code](https://github.com/CluedIn-io/CluedIn.Enricher.CVR/releases/tag/4.0.0) |

## DuckDuckGo

The [DuckDuckGo](/preparation/enricher/duckduckgo) enricher retrieves general information about organizations from the DuckDuckGo search engine. It supports the following endpoint:

- `https://api.duckduckgo.com`

| Package name | Package version | Source code |
|--|--|--|
| CluedIn.ExternalSearch.Providers.DuckDuckGo.Provider | 4.4.0 | [Source code](https://github.com/CluedIn-io/CluedIn.Enricher.DuckDuckGo/releases/tag/4.4.0) |
| CluedIn.ExternalSearch.Providers.DuckDuckGo.Provider | 4.3.0 | [Source code](https://github.com/CluedIn-io/CluedIn.Enricher.DuckDuckGo/releases/tag/4.3.0) |
| CluedIn.ExternalSearch.Providers.DuckDuckGo.Provider | 4.0.1 | [Source code](https://github.com/CluedIn-io/CluedIn.Enricher.DuckDuckGo/releases/tag/4.0.1) |
| CluedIn.ExternalSearch.Providers.DuckDuckGo.Provider | 4.0.0 | [Source code](https://github.com/CluedIn-io/CluedIn.Enricher.DuckDuckGo/releases/tag/4.0.0) |

## Duns & Bradstreet

The Duns & Bradstreet enricher retrieves information about organizations. It supports the following endpoints:

- `{hostUrl}/data/duns/{dunsNumber}` – this endpoint is called when the D&B number is provided.

- `{hostUrl}/v1/match/extendedMatch` – this endpoint is called when the D&B number is not provided.

| Package name | Package version | Source code |
|--|--|--|
| CluedIn.ExternalSearch.Providers.DNB | - | Contact CluedIn for details |


## Gleif

The [Gleif](/preparation/enricher/gleif) enricher retrieves information about organizations using the Legal Entity Identifier (LEI). It supports the following endpoint:

- `https://api.gleif.org/api/v1/lei-records?page[size]=1&page[number]=1&filter[lei]={leicode}`, where `{leicode}` is the LEI code of the company.

| Package name | Package version | Source code |
|--|--|--|
| CluedIn.Provider.ExternalSearch.Gleif | 4.4.0 | [Source code](https://github.com/CluedIn-io/CluedIn.Enricher.Gleif/releases/tag/4.4.0) |
| CluedIn.Provider.ExternalSearch.Gleif | 4.0.1 | [Source code](https://github.com/CluedIn-io/CluedIn.Enricher.Gleif/releases/tag/4.0.1) |
| CluedIn.Provider.ExternalSearch.Gleif | 4.0.0 | [Source code](https://github.com/CluedIn-io/CluedIn.Enricher.Gleif/releases/tag/4.0.0) |


## Google Maps

The [Google Maps](/preparation/enricher/google-maps) enricher cleans, standardizes, and enriches international postal addresses with geocoding information. This enricher returns correct information about company address.

The Google Maps enricher supports the following endpoints:

- `https://maps.googleapis.com/maps/api/place/textsearch/json?query={organizationName}{organizationAddress}{organizationCity}{organizationZip}{organizationState}{organizationCountry}` – if organization name, address, city, zip, state, and country are provided.

- `https://maps.googleapis.com/maps/api/place/textsearch/json?query={organizationName}` – if organization name is provided.

- `https://maps.googleapis.com/maps/api/place/textsearch/json?query={organizationAddress}` – if organization address is provided.

- `https://maps.googleapis.com/maps/api/place/textsearch/json?query={location}` – if one of the addresses other than organization address is provided.

- `https://maps.googleapis.com/maps/api/place/textsearch/json?query={location}&location={latitude}{longitude}` – if one of the addresses other than organization address and latitude and longitude are provided.

- `https://maps.googleapis.com/maps/api/place/textsearch/json?query=location={latitude}{longitude}` – if latitude and longitude are provided.

- `https://maps.googleapis.com/maps/api/place/details/json?placeid={id}` – the ID is taken from the previous text search API (the result of `https://maps.googleapis.com/maps/api/place/textsearch/json`).

| Package name | Package version | Source code |
|--|--|--|
| CluedIn.Provider.ExternalSearch.GoogleMaps | 4.4.0 | [Source code](https://github.com/CluedIn-io/CluedIn.Enricher.GoogleMaps/releases/tag/4.4.0) |
| CluedIn.Provider.ExternalSearch.GoogleMaps | 4.1.1 | [Source code](https://github.com/CluedIn-io/CluedIn.Enricher.GoogleMaps/releases/tag/4.1.1) |
| CluedIn.Provider.ExternalSearch.GoogleMaps | 4.1.0 | [Source code](https://github.com/CluedIn-io/CluedIn.Enricher.GoogleMaps/releases/tag/4.1.0) |
| CluedIn.Provider.ExternalSearch.GoogleMaps | 4.0.5 | [Source code](https://github.com/CluedIn-io/CluedIn.Enricher.GoogleMaps/releases/tag/4.0.5) |
| CluedIn.Provider.ExternalSearch.GoogleMaps | 4.0.4 | [Source code](https://github.com/CluedIn-io/CluedIn.Enricher.GoogleMaps/releases/tag/4.0.4) |
| CluedIn.Provider.ExternalSearch.GoogleMaps | 4.0.3 | [Source code](https://github.com/CluedIn-io/CluedIn.Enricher.GoogleMaps/releases/tag/4.0.3) |
| CluedIn.Provider.ExternalSearch.GoogleMaps | 4.0.0 | [Source code](https://github.com/CluedIn-io/CluedIn.Enricher.GoogleMaps/releases/tag/4.0.0) |

## Knowledge Graph

The [Knowledge Graph](/preparation/enricher/knowledge-graph) enricher retrieves descriptions of organizations using the Google Knowledge Graph API. It supports the following endpoint:

- `https://kgsearch.googleapis.com?query={nameOrUri}&key={apiKey}&limit=10&indent=true`, where `{nameOrUri}` is the name or website of the organization and `{apiKey}` is your API key for accessing Google’s Knowledge Graph database.

| Package name | Package version | Source code |
|--|--|--|
| CluedIn.Provider.ExternalSearch.KnowledgeGraph | 4.4.0 | [Source code](https://github.com/CluedIn-io/CluedIn.Enricher.KnowledgeGraph/releases/tag/4.4.0) |
| CluedIn.Provider.ExternalSearch.KnowledgeGraph | 4.0.1 | [Source code](https://github.com/CluedIn-io/CluedIn.Enricher.KnowledgeGraph/releases/tag/4.0.1) |
| CluedIn.Provider.ExternalSearch.KnowledgeGraph | 4.0.0 | [Source code](https://github.com/CluedIn-io/CluedIn.Enricher.KnowledgeGraph/releases/tag/4.0.0) |

## Libpostal

The [Libpostal](/preparation/enricher/libpostal) enricher parses and normalizes street addresses using statistical NLP and open data. This enricher returns international street address.

The Libpostal enricher supports the following endpoint:

- `http://<host>:<port>/parser    body = {query: {address}}`

| Package name | Package version | Source code |
|--|--|--|
| CluedIn.Provider.ExternalSearch.Libpostal | 4.4.0 | [Source code](https://github.com/CluedIn-io/CluedIn.Enricher.libpostal/releases/tag/4.4.0) |
| CluedIn.Provider.ExternalSearch.Libpostal | 4.1.2 | [Source code](https://github.com/CluedIn-io/CluedIn.Enricher.libpostal/releases/tag/4.1.2) |
| CluedIn.Provider.ExternalSearch.Libpostal | 4.1.1 | [Source code](https://github.com/CluedIn-io/CluedIn.Enricher.libpostal/releases/tag/4.1.1) |
| CluedIn.Provider.ExternalSearch.Libpostal | 4.1.0 | [Source code](https://github.com/CluedIn-io/CluedIn.Enricher.libpostal/releases/tag/4.1.0) |
| CluedIn.Provider.ExternalSearch.Libpostal | 4.0.0 | [Source code](https://github.com/CluedIn-io/CluedIn.Enricher.libpostal/releases/tag/4.0.0) |

## Open Corporates

The [Open Corporates](/preparation/enricher/open-corporates) enricher retrieves information on all companies worldwide. This enricher returns VAT/TAX number.

The Open Corporates enricher supports the following endpoints:

- `https://api.opencorporates.com/v0.4/companies/search?q={nameLookup}`, where `{nameLookup}` is the name of company – this endpoint is called when no company codes can be found in golden record's organization.codes.cvr, organization.codes.brreg, organization.codes.companyHouse, or organization.codes.cik

- `https://api.opencorporates.com/v0.4companies/{jurisdictionCodeLookup.Jurisdiction}/{jurisdictionCodeLookup.Value}?format=json` – this endpoint is called when there are company codes, so the jurisdiction of golden record will be retrieved and used in the API.

| Package name | Package version | Source code |
|--|--|--|
| CluedIn.Provider.ExternalSearch.OpenCorporates | 4.4.0 | [Source code](https://github.com/CluedIn-io/CluedIn.Enricher.OpenCorporates/releases/tag/4.4.0) |
| CluedIn.Provider.ExternalSearch.OpenCorporates | 4.1.2 | [Source code](https://github.com/CluedIn-io/CluedIn.Enricher.OpenCorporates/releases/tag/4.1.2) |
| CluedIn.Provider.ExternalSearch.OpenCorporates | 4.1.1 | [Source code](https://github.com/CluedIn-io/CluedIn.Enricher.OpenCorporates/releases/tag/4.1.1) |
| CluedIn.Provider.ExternalSearch.OpenCorporates | 4.1.0 | [Source code](https://github.com/CluedIn-io/CluedIn.Enricher.OpenCorporates/releases/tag/4.1.0) |
| CluedIn.Provider.ExternalSearch.OpenCorporates | 4.0.0 | [Source code](https://github.com/CluedIn-io/CluedIn.Enricher.OpenCorporates/releases/tag/4.0.0) |

## PermId

The [PermId](/preparation/enricher/perm-id) enricher retrieves information about organizations from the PermID database. It supports the following endpoints:

- `https://api-eit.refinitiv.com/permid` – this API is called first.

- `https://permid.org/api/mdaas/getEntityById/` – this API is called second to get the social data.

| Package name | Package version | Source code |
|--|--|--|
| CluedIn.ExternalSearch.Providers.PermId.Provider | 4.4.0 | [Source code](https://github.com/CluedIn-io/CluedIn.Enricher.Permid/releases/tag/4.4.0) |
| CluedIn.ExternalSearch.Providers.PermId.Provider | 4.0.1 | [Source code](https://github.com/CluedIn-io/CluedIn.Enricher.Permid/releases/tag/4.0.1) |
| CluedIn.ExternalSearch.Providers.PermId.Provider | 4.0.0 | [Source code](https://github.com/CluedIn-io/CluedIn.Enricher.Permid/releases/tag/4.0.0) |

## Vatlayer

The [Vatlayer](/preparation/enricher/vatlayer) enricher validates and cleans EU VAT numbers. It supports the following endpoint:

- `http://www.apilayer.net/api/validate?access_key={apiToken}&vat_number={vat}&format=1`, where `{apiToken}` is your API key for retrieving information from the Vatlayer website and `{vat}` is the VAT number of the company.

| Package name | Package version | Source code |
|--|--|--|
| CluedIn.Provider.ExternalSearch.Providers.VatLayer | 4.4.0 | [Source code](https://github.com/CluedIn-io/CluedIn.Enricher.VatLayer/releases/tag/4.4.0) |
| CluedIn.Provider.ExternalSearch.Providers.VatLayer | 4.0.1 | [Source code](https://github.com/CluedIn-io/CluedIn.Enricher.VatLayer/releases/tag/4.0.1) |
| CluedIn.Provider.ExternalSearch.Providers.VatLayer | 4.0.0 | [Source code](https://github.com/CluedIn-io/CluedIn.Enricher.VatLayer/releases/tag/4.0.0) |

## Web

The [Web](/preparation/enricher/web) enricher retrieves information about organizations through their websites. The Web enricher supports any website provided in the **Website Vocab Key** field of the enricher configuration.

| Package name | Package version | Source code |
|--|--|--|
| CluedIn.ExternalSearch.Providers.Web | 4.4.0 | [Source code](https://github.com/CluedIn-io/CluedIn.Enricher.Web/releases/tag/4.4.0) |
| CluedIn.ExternalSearch.Providers.Web | 4.1.2 | [Source code](https://github.com/CluedIn-io/CluedIn.Enricher.Web/releases/tag/4.1.2) |
| CluedIn.ExternalSearch.Providers.Web | 4.1.0 | [Source code](https://github.com/CluedIn-io/CluedIn.Enricher.Web/releases/tag/4.1.0) |
| CluedIn.ExternalSearch.Providers.Web | 4.0.0 | [Source code](https://github.com/CluedIn-io/CluedIn.Enricher.Web/releases/tag/4.0.0) |
