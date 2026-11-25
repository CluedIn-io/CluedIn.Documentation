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

## Company registry lookups

These samples look up a company in a national business register by its registration number, and add the registered name, status, address and other register details to the golden record. Each one reads a single identifier from a vocabulary key, checks its format before calling the register, and adds properties under its own prefix (for example `brreg.name`).

Use the filter above the table to find a register by country, register or identifier, or to show only the registers that don't need an API key. On each sample page, open **Customize the script** above the process script to enter your own vocabulary keys and cache duration: the script and the **Vocabulary and Properties** field update as you type, ready to copy or download.

| Country | Register | Identifier | API key |
| ------- | -------- | ---------- | ------- |
| Australia | [ABN Lookup](https://documentation.cluedin.net/govern/rest-api-enricher-samples/abn-lookup-australia.md) | ABN | ABN Lookup GUID (free) |
| Brazil | [CNPJ](https://documentation.cluedin.net/govern/rest-api-enricher-samples/cnpj-brazil.md) | CNPJ | not needed |
| Canada | [Corporations Canada](https://documentation.cluedin.net/govern/rest-api-enricher-samples/corporations-canada.md) | Corporation number or business number | ISED API key (free) |
| Colombia | [RUES](https://documentation.cluedin.net/govern/rest-api-enricher-samples/rues-colombia.md) | NIT | optional |
| Estonia | [e-Business Register](https://documentation.cluedin.net/govern/rest-api-enricher-samples/e-business-register-estonia.md) | Registry code | not needed |
| Finland | [Finnish Business Information System](https://documentation.cluedin.net/govern/rest-api-enricher-samples/ytj-finland.md) | Business ID (Y-tunnus) | not needed |
| Greece | [GEMI](https://documentation.cluedin.net/govern/rest-api-enricher-samples/gemi-greece.md) | GEMI number or AFM | GEMI Open Data API key (free) |
| Hong Kong | [Companies Registry](https://documentation.cluedin.net/govern/rest-api-enricher-samples/companies-registry-hong-kong.md) | Business Registration number | not needed |
| India | [MCA company master data](https://documentation.cluedin.net/govern/rest-api-enricher-samples/mca-india.md) | CIN | data.gov.in API key (free) |
| Israel | [Companies Registrar](https://documentation.cluedin.net/govern/rest-api-enricher-samples/companies-registrar-israel.md) | Company number | not needed |
| Japan | [gBizINFO](https://documentation.cluedin.net/govern/rest-api-enricher-samples/gbizinfo-japan.md) | Corporate number | gBizINFO API token (free) |
| Latvia | [Enterprise Register](https://documentation.cluedin.net/govern/rest-api-enricher-samples/enterprise-register-latvia.md) | Registration number | not needed |
| Malta | [Malta Business Registry](https://documentation.cluedin.net/govern/rest-api-enricher-samples/mbr-malta.md) | Company registration number | MBR API package (paid) |
| Mexico | [DENUE](https://documentation.cluedin.net/govern/rest-api-enricher-samples/denue-mexico.md) | DENUE establishment ID | INEGI DENUE token (free) |
| Netherlands | [KVK](https://documentation.cluedin.net/govern/rest-api-enricher-samples/kvk-netherlands.md) | KVK number | KVK API key (paid) |
| New Zealand | [Companies Office NZBN](https://documentation.cluedin.net/govern/rest-api-enricher-samples/nzbn-new-zealand.md) | NZBN | NZBN API subscription key (free) |
| Nigeria | [CAC](https://documentation.cluedin.net/govern/rest-api-enricher-samples/cac-nigeria.md) | RC number | CAC VAS API key (paid) |
| Norway | [Brønnøysund Register Centre](https://documentation.cluedin.net/govern/rest-api-enricher-samples/brreg-norway.md) | Organization number | not needed |
| Philippines | [SEC](https://documentation.cluedin.net/govern/rest-api-enricher-samples/sec-philippines.md) | SEC registration number | SEC API Marketplace key and secret |
| Saudi Arabia | [Wathq Commercial Registration](https://documentation.cluedin.net/govern/rest-api-enricher-samples/wathq-saudi-arabia.md) | CR number | Wathq API key (paid) |
| Serbia | [APR](https://documentation.cluedin.net/govern/rest-api-enricher-samples/apr-serbia.md) | Registration number | not needed |
| Singapore | [ACRA](https://documentation.cluedin.net/govern/rest-api-enricher-samples/acra-singapore.md) | UEN | optional |
| Slovakia | [Register of Legal Entities](https://documentation.cluedin.net/govern/rest-api-enricher-samples/rpo-slovakia.md) | IČO | not needed |
| Slovenia | [AJPES Business Register](https://documentation.cluedin.net/govern/rest-api-enricher-samples/ajpes-slovenia.md) | Registration or tax number | AJPES username and password (paid) |
| South Africa | [CIPC](https://documentation.cluedin.net/govern/rest-api-enricher-samples/cipc-south-africa.md) | Enterprise number | CIPC APIVerse subscription key |
| South Korea | [OpenDART](https://documentation.cluedin.net/govern/rest-api-enricher-samples/opendart-south-korea.md) | DART corporation code | OpenDART API key (free) |
| Taiwan | [Ministry of Economic Affairs](https://documentation.cluedin.net/govern/rest-api-enricher-samples/moea-taiwan.md) | Unified business number | not needed |
| Thailand | [Open-DBD](https://documentation.cluedin.net/govern/rest-api-enricher-samples/dbd-thailand.md) | Juristic person registration number | not needed |

## In this section

- [Azure OpenAI](https://documentation.cluedin.net/govern/rest-api-enricher-samples/azure-openai.md) (reference): Translates an organization name into Japanese with an Azure OpenAI chat completions deployment. V1 script; needs an Azure OpenAI API key.
- [DuckDuckGo](https://documentation.cluedin.net/govern/rest-api-enricher-samples/duckduckgo.md) (reference): Adds information about an organization from the DuckDuckGo Instant Answer API. V1 script; no API key.
- [Dun & Bradstreet](https://documentation.cluedin.net/govern/rest-api-enricher-samples/dun-and-bradstreet.md) (reference): Looks up a company by DUNS number in Dun & Bradstreet's Direct+ API. V2 script; needs a D&B API key and secret.
- [Logo.dev](https://documentation.cluedin.net/govern/rest-api-enricher-samples/logo-dev.md) (reference): Adds a company logo URL from Logo.dev, based on the company's website. V2 script; needs a Logo.dev API key.
- [Melissa](https://documentation.cluedin.net/govern/rest-api-enricher-samples/melissa.md) (reference): Validates and standardizes addresses with the Melissa Global Address API. V1 script; needs a Melissa license key.
- [OS Places (AddressBase)](https://documentation.cluedin.net/govern/rest-api-enricher-samples/os-places.md) (reference): Verifies UK addresses with Ordnance Survey's OS Places API (AddressBase). V1 script; needs an OS Data Hub API key.
- [REST Countries](https://documentation.cluedin.net/govern/rest-api-enricher-samples/rest-countries.md) (reference): Adds the official name of a country from the REST Countries API. V1 and V2 scripts; no API key.
- [VIES (EU VAT validation)](https://documentation.cluedin.net/govern/rest-api-enricher-samples/vies.md) (reference): Checks EU VAT numbers against the European Commission's VIES service and adds the registered trader name and address. V2 script; no API key.
- [ABN Lookup (Australia)](https://documentation.cluedin.net/govern/rest-api-enricher-samples/abn-lookup-australia.md) (reference): Looks up Australian Business Numbers (ABNs) with the Australian Business Register's ABN Lookup web service and adds the entity name, type, status, ACN, GST registration and business names. V2 script; needs an ABN Lookup GUID.
- [ACRA (Singapore)](https://documentation.cluedin.net/govern/rest-api-enricher-samples/acra-singapore.md) (reference): Looks up Singapore Unique Entity Numbers (UENs) in ACRA's open data on data.gov.sg and adds the registered name, status, entity type, registration date and address. V2 script; no API key.
- [Brønnøysund Register Centre (Norway)](https://documentation.cluedin.net/govern/rest-api-enricher-samples/brreg-norway.md) (reference): Looks up Norwegian organization numbers in the Brønnøysund Register Centre (Enhetsregisteret) and adds the registered name, address, industry and status. V2 script; no API key.
- [CNPJ (Brazil)](https://documentation.cluedin.net/govern/rest-api-enricher-samples/cnpj-brazil.md) (reference): Looks up Brazilian CNPJ numbers with BrasilAPI, which serves the Receita Federal's open CNPJ data, and adds the registered name, status, main activity and address. V2 script; no API key.
- [Companies Office NZBN (New Zealand)](https://documentation.cluedin.net/govern/rest-api-enricher-samples/nzbn-new-zealand.md) (reference): Looks up New Zealand Business Numbers (NZBNs) with the Companies Office NZBN API and adds the entity name, status, type, company number, addresses, industry and trading names. V2 script; needs an NZBN API subscription key.
- [Companies Registry (Hong Kong)](https://documentation.cluedin.net/govern/rest-api-enricher-samples/companies-registry-hong-kong.md) (reference): Looks up Hong Kong Business Registration numbers in the Companies Registry's open data and adds the company name, type, registered office address and incorporation date. V2 script; no API key.
- [Corporations Canada](https://documentation.cluedin.net/govern/rest-api-enricher-samples/corporations-canada.md) (reference): Looks up Canadian federal corporations by corporation number or business number with the Corporations Canada Federal Corporation API and adds the name, status, governing act, business number, registered office address and incorporation date. V2 script; needs an ISED API key.
- [e-Business Register (Estonia)](https://documentation.cluedin.net/govern/rest-api-enricher-samples/e-business-register-estonia.md) (reference): Looks up Estonian registry codes in the e-Business Register's free public company search and adds the registered name, status and legal address. V2 script; no API key.
- [gBizINFO (Japan)](https://documentation.cluedin.net/govern/rest-api-enricher-samples/gbizinfo-japan.md) (reference): Looks up Japanese corporate numbers in gBizINFO and adds the registered name, English name, head office address, representative, capital and employee count. V2 script; needs a gBizINFO API token.
- [KVK (Netherlands)](https://documentation.cluedin.net/govern/rest-api-enricher-samples/kvk-netherlands.md) (reference): Looks up Dutch KVK numbers in the KVK Basisprofiel API and adds the registered name, trade names, legal form, main activity and address. V2 script; needs a KVK API key.
- [MCA company master data (India)](https://documentation.cluedin.net/govern/rest-api-enricher-samples/mca-india.md) (reference): Looks up Indian companies by Corporate Identification Number (CIN) in the Ministry of Corporate Affairs company master data on data.gov.in and adds the registered name, status, class, capital and registered office address. V2 script; needs a data.gov.in API key.
- [Ministry of Economic Affairs (Taiwan)](https://documentation.cluedin.net/govern/rest-api-enricher-samples/moea-taiwan.md) (reference): Looks up Taiwanese Unified Business Numbers in the Ministry of Economic Affairs' company registration open data and adds the company name, status, representative, address and capital. V2 script; no API key.
- [OpenDART (South Korea)](https://documentation.cluedin.net/govern/rest-api-enricher-samples/opendart-south-korea.md) (reference): Looks up South Korean companies by DART corporation code in the Financial Supervisory Service's OpenDART API and adds the registered name, CEO, registration numbers, stock code and address. V2 script; needs an OpenDART API key.
- [Finnish Business Information System (Finland)](https://documentation.cluedin.net/govern/rest-api-enricher-samples/ytj-finland.md) (reference): Looks up Finnish Business IDs (Y-tunnus) in the Finnish Business Information System (YTJ) and adds the registered name, company form, line of business, address and status. V2 script; no API key.
- [CIPC (South Africa)](https://documentation.cluedin.net/govern/rest-api-enricher-samples/cipc-south-africa.md) (reference): Looks up South African enterprise numbers with the CIPC APIVerse API and adds the registered name, type, status, industry, registration date and addresses. V2 script; needs a CIPC APIVerse subscription key.
- [DENUE (Mexico)](https://documentation.cluedin.net/govern/rest-api-enricher-samples/denue-mexico.md) (reference): Looks up Mexican business establishments by DENUE ID in INEGI's DENUE API and adds the establishment name, legal name, activity, employee range, address and contact details. V2 script; needs a DENUE API token.
- [Open-DBD (Thailand)](https://documentation.cluedin.net/govern/rest-api-enricher-samples/dbd-thailand.md) (reference): Looks up Thai juristic person registration numbers in the Department of Business Development (DBD) register and adds the registered name, type, status, capital, business objective and address. V2 script; no API key.
- [RUES (Colombia)](https://documentation.cluedin.net/govern/rest-api-enricher-samples/rues-colombia.md) (reference): Looks up Colombian NITs in the Registro Único Empresarial y Social (RUES) open data on datos.gov.co and adds the registered name, status, legal form, activity code, chamber of commerce and registration dates. V2 script; no API key.
- [SEC (Philippines)](https://documentation.cluedin.net/govern/rest-api-enricher-samples/sec-philippines.md) (reference): Looks up Philippine SEC registration numbers with the SECNumber API on the SEC API Marketplace and adds the registered name, approval date, status and secondary licenses. V2 script; needs SEC API Marketplace credentials.
- [AJPES Business Register (Slovenia)](https://documentation.cluedin.net/govern/rest-api-enricher-samples/ajpes-slovenia.md) (reference): Looks up Slovenian companies by registration number or tax number in the Slovenian Business Register with AJPES' restPrsInfo REST API and adds the registered name, legal form, address, main activity and capital. V2 script; needs an AJPES user with a PRS package.
- [APR (Serbia)](https://documentation.cluedin.net/govern/rest-api-enricher-samples/apr-serbia.md) (reference): Looks up Serbian companies by registration number (matični broj) in the APR Companies Open Data API and adds the business name, status, legal form, foundation date, municipality and activity code. V2 script; no API key.
- [CAC (Nigeria)](https://documentation.cluedin.net/govern/rest-api-enricher-samples/cac-nigeria.md) (reference): Looks up Nigerian companies and business names by RC, BN or IT number in the Corporate Affairs Commission's CAC-verified VAS API and adds the registered name, type, status, address, registration date and lines of business. V2 script; needs a VAS API key.
- [Companies Registrar (Israel)](https://documentation.cluedin.net/govern/rest-api-enricher-samples/companies-registrar-israel.md) (reference): Looks up Israeli company numbers in the Companies Registrar's open data on data.gov.il and adds the registered name, type, status, purpose and address. V2 script; no API key.
- [Enterprise Register (Latvia)](https://documentation.cluedin.net/govern/rest-api-enricher-samples/enterprise-register-latvia.md) (reference): Looks up Latvian registration numbers in the Register of Enterprises' open data on data.gov.lv and adds the registered name, legal form, status, dates and legal address. V2 script; no API key.
- [GEMI (Greece)](https://documentation.cluedin.net/govern/rest-api-enricher-samples/gemi-greece.md) (reference): Looks up Greek companies by GEMI number or tax number (AFM) in the GEMI Open Data API and adds the registered name, status, legal form, address and main activity. V2 script; needs a GEMI Open Data api_key.
- [Malta Business Registry](https://documentation.cluedin.net/govern/rest-api-enricher-samples/mbr-malta.md) (reference): A template for looking up Maltese companies by registration number with the Malta Business Registry's Basic Company Details API package, adding the registered name, registration date, registered address and state. V2 script; needs an MBR API subscription.
- [Register of Legal Entities (Slovakia)](https://documentation.cluedin.net/govern/rest-api-enricher-samples/rpo-slovakia.md) (reference): Looks up Slovak IČO numbers in the Statistical Office's Register of Legal Entities (RPO) API and adds the registered name, legal form, address, main activity, registration and capital. V2 script; no API key.
- [Wathq Commercial Registration (Saudi Arabia)](https://documentation.cluedin.net/govern/rest-api-enricher-samples/wathq-saudi-arabia.md) (reference): Looks up Saudi commercial registration (CR) numbers in the Ministry of Commerce's Wathq Commercial Registration API and adds the registered name, business type, status, dates, address, activities and capital. V2 script; needs a Wathq API key.

Up: [Govern & improve](https://documentation.cluedin.net/govern.md)
