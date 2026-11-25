---
title: REST API enricher samples
url: https://documentation.cluedin.net/govern/rest-api-enricher-samples
content_type: landing
section: Govern & improve
---

# REST API enricher samples

The [REST API enricher](https://documentation.cluedin.net/govern/enrichment/rest-api.md) can call almost any external service, but you write the JavaScript that builds the request and reads the response. The pages in this section give you that work already done for specific services: the enricher settings, the vocabulary keys to send, and a script you can paste in and adapt.

Each page is named after the external service it calls. It says which enricher version the script is for (V1 uses a process request script and a process response script, V2 uses a single process script) and whether the service needs an API key. For how to add the enricher and what each setting means, and for the `log`, `cache`, `stringEncoder` and `http` helper functions the scripts use, see [REST API enricher](https://documentation.cluedin.net/govern/enrichment/rest-api.md).

The scripts are starting points. Check the vocabulary keys in each script against your own data model, and review the service's terms and rate limits before you enrich a large number of golden records.

## In this section

- [Azure OpenAI](https://documentation.cluedin.net/govern/rest-api-enricher-samples/azure-openai.md) (reference): Translates an organization name into Japanese with an Azure OpenAI chat completions deployment. V1 script; needs an Azure OpenAI API key.
- [DuckDuckGo](https://documentation.cluedin.net/govern/rest-api-enricher-samples/duckduckgo.md) (reference): Adds information about an organization from the DuckDuckGo Instant Answer API. V1 script; no API key.
- [Dun & Bradstreet](https://documentation.cluedin.net/govern/rest-api-enricher-samples/dun-and-bradstreet.md) (reference): Looks up a company by DUNS number in Dun & Bradstreet's Direct+ API. V2 script; needs a D&B API key and secret.
- [Logo.dev](https://documentation.cluedin.net/govern/rest-api-enricher-samples/logo-dev.md) (reference): Adds a company logo URL from Logo.dev, based on the company's website. V2 script; needs a Logo.dev API key.
- [Melissa](https://documentation.cluedin.net/govern/rest-api-enricher-samples/melissa.md) (reference): Validates and standardizes addresses with the Melissa Global Address API. V1 script; needs a Melissa license key.
- [OS Places (AddressBase)](https://documentation.cluedin.net/govern/rest-api-enricher-samples/os-places.md) (reference): Verifies UK addresses with Ordnance Survey's OS Places API (AddressBase). V1 script; needs an OS Data Hub API key.
- [REST Countries](https://documentation.cluedin.net/govern/rest-api-enricher-samples/rest-countries.md) (reference): Adds the official name of a country from the REST Countries API. V1 and V2 scripts; no API key.
- [VIES (EU VAT validation)](https://documentation.cluedin.net/govern/rest-api-enricher-samples/vies.md) (reference): Checks EU VAT numbers against the European Commission's VIES service and adds the registered trader name and address. V2 script; no API key.

Up: [Govern & improve](https://documentation.cluedin.net/govern.md)
