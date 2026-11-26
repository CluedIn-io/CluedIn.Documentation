---
layout: cluedin
title: Finnish Business Information System (Finland)
parent: REST API enricher samples
grand_parent: Govern & improve
nav_order: 220
permalink: /govern/rest-api-enricher-samples/ytj-finland
content_type: reference
summary: "Looks up Finnish Business IDs (Y-tunnus) in the Finnish Business Information System (YTJ) and adds the registered name, company form, line of business, address and status. V2 script; no API key."
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

This example looks up an organization's Finnish Business ID (Y-tunnus) in the Finnish Business Information System (YTJ) by using the [YTJ open-data API](https://avoindata.prh.fi/en/ytj/swagger-ui) of the Finnish Patent and Registration Office (PRH). For each golden record it stores the current company name, company form, main line of business, website, addresses, registration date, and status on the Trade Register, including any liquidation, bankruptcy, or re-organisation. No API key is needed.

**Enricher version:** V2  
**API key:** not needed

To set up the enricher, see [Add REST API enricher](/govern/enrichment/rest-api#add-rest-api-enricher), then use the settings and script on this page.

## Settings

- **Accepted Business Domain** – `/Organization`, or the business domain that holds your companies.

- **Version** – V2 (recommended).

- **API Key** – leave empty.

- **Filters** – we recommend a rule that only accepts golden records where `organization.businessId` has a value. Otherwise, every record without a Business ID is listed on the enricher's **Logs** tab as having returned no results.

## Vocabulary and Properties

```
organization.businessId
```

`organization.businessId` holds the Finnish Business ID, for example `0112038-9`. If your data uses another vocabulary key, change this field and the `BUSINESS_ID_KEY` value at the top of the script.

## Request and response

**Base URL:** `https://avoindata.prh.fi/opendata-ytj-api/v3`  
**Endpoint:** `GET /companies?businessId={businessId}`  
**Authentication:** none

The script sends one request per golden record:

```http
GET https://avoindata.prh.fi/opendata-ytj-api/v3/companies?businessId=0112038-9
Accept: application/json
```

Shortened response:

```json
{
  "totalResults": 1,
  "companies": [
    {
      "businessId": { "value": "0112038-9", "registrationDate": "1978-03-15" },
      "euId": { "value": "FIFPRO.0112038-9" },
      "names": [
        { "name": "Nokia Oyj", "type": "1", "registrationDate": "1997-09-01", "version": 1 },
        { "name": "Oy Nokia Ab", "type": "1", "registrationDate": "1966-06-10", "endDate": "1997-08-31", "version": 2 }
      ],
      "mainBusinessLine": {
        "type": "70100",
        "descriptions": [{ "languageCode": "3", "description": "Activities of head offices" }]
      },
      "website": { "url": "www.nokia.com" },
      "companyForms": [
        { "type": "17", "descriptions": [{ "languageCode": "3", "description": "Public limited company" }] }
      ],
      "companySituations": [],
      "addresses": [
        { "type": 1, "street": "Karakaari", "buildingNumber": "7", "postCode": "02610", "postOffices": [{ "city": "ESPOO", "languageCode": "1" }] },
        { "type": 2, "postOfficeBox": "226", "postCode": "00045", "postOffices": [{ "city": "NOKIA GROUP", "languageCode": "1" }] }
      ],
      "tradeRegisterStatus": "1",
      "status": "2",
      "registrationDate": "1896-12-19"
    }
  ]
}
```

## Properties added by the enricher

| Property | Response field | Example |
| -------- | -------------- | ------- |
| `ytj.businessId` | `businessId.value` | `0112038-9` |
| `ytj.euId` | `euId.value` | `FIFPRO.0112038-9` |
| `ytj.name` | `names[].name` of type `1` (company name) with no `endDate` | `Nokia Oyj` |
| `ytj.companyForm` | `companyForms[].descriptions` in English, of the form with no `endDate` | `Public limited company` |
| `ytj.companyFormCode` | `companyForms[].type` | `17` |
| `ytj.mainBusinessLineCode` | `mainBusinessLine.type` (TOL 2008) | `70100` |
| `ytj.mainBusinessLine` | `mainBusinessLine.descriptions` in English | `Activities of head offices` |
| `ytj.website` | `website.url` | `www.nokia.com` |
| `ytj.visitingAddress` | address of type `1` (street address), on one line | `Karakaari 7, 02610 ESPOO` |
| `ytj.postalAddress` | address of type `2` (postal address), on one line | `PL 226, 00045 NOKIA GROUP` |
| `ytj.city` | Finnish `postOffices[].city` of the street address | `ESPOO` |
| `ytj.postalCode` | `postCode` of the street address | `02610` |
| `ytj.registrationDate` | `registrationDate` | `1896-12-19` |
| `ytj.endDate` | `endDate` (only for a company that has ceased) | `2025-02-03` |
| `ytj.businessIdStatus` | `status`: `1` Pending, `2` Valid, `5` Business ID invalidated | `Valid` |
| `ytj.tradeRegisterStatus` | `tradeRegisterStatus`: `0` Unregistered, `1` Registered, `2` Removed from register, `3` Start-up not registered, `4` Ceased | `Registered` |
| `ytj.situation` | `companySituations[].type` with no `endDate`: `SELTILA` Liquidation, `KONK` Bankrupt, `SANE` Company re-organisation | `Liquidation` |

A property is added only when YTJ returns a value for it.

If the enricher has a **Preview** tab, the results appear there first. To add them to golden records, go to the **Map** tab, select **Map Data**, and choose **Auto Mapping**. Select the business domain, enter a new vocabulary named `YTJ` with the key prefix `ytj`, and then create the mapping. Auto mapping also uses `name` as the golden record name, so remove that from the mapping if you want to keep your existing names. Then process the data on the **Process** tab. If the enricher has no **Preview** tab, the properties are added to the golden record as soon as it is enriched.

## How the script handles input and errors

- Spaces and a leading `FI` are removed, so the VAT number form `FI01120389` and `0112038-9` are both looked up as `0112038-9`. An old 6-digit Business ID such as `112038-9` gets its leading zero back. The check digit must be valid. Golden records without a valid Business ID are skipped without calling the API.

- If the Business ID isn't found (the API returns `totalResults` = `0`) or the API returns an error, the script logs the reason and adds nothing.

- If the API reports that it is too busy (HTTP 429), the script throws an error that makes the enricher try the golden record again later.

- Successful results are cached for 24 hours per Business ID. To change this, edit `CACHE_MILLISECONDS` in the script.

## Testing the enricher

- **Test connection** checks only that the script runs. It doesn't call the API.

- To try the setup, create a golden record with `organization.businessId` set to `0112038-9` (Nokia Oyj).

## Limitations

- The YTJ open-data API covers companies and other entities with a Finnish Business ID. Board members and financial statements aren't included.

- Line of business and company form are added in English. Finnish and Swedish descriptions are also in the response; to use one of them, change `ENGLISH` in the script to `"1"` (Finnish) or `"2"` (Swedish).

## Process script

```javascript
// REST API enricher (V2) - Finnish company lookup with the Finnish Business Information System
//
// Looks up a golden record's Finnish Business ID (Y-tunnus) in the Finnish Business Information
// System (YTJ), using the Finnish Patent and Registration Office's open-data YTJ API v3
// (https://avoindata.prh.fi/en/ytj/swagger-ui), and adds the result to the golden record as
// ytj.* properties:
//
//   ytj.businessId           Business ID that was looked up, for example 0112038-9
//   ytj.euId                 EUID, for example FIFPRO.0112038-9
//   ytj.name                 current company name
//   ytj.companyForm          company form in English, for example Public limited company
//   ytj.companyFormCode      company form code, for example 17
//   ytj.mainBusinessLineCode main line of business (TOL 2008 / NACE), for example 70100
//   ytj.mainBusinessLine     main line of business in English
//   ytj.website              website
//   ytj.visitingAddress      street address on one line
//   ytj.postalAddress        postal address on one line
//   ytj.city                 city of the street address (Finnish name)
//   ytj.postalCode           postal code of the street address
//   ytj.registrationDate     date the company was registered (YYYY-MM-DD)
//   ytj.endDate              date the company ceased (YYYY-MM-DD)
//   ytj.businessIdStatus     Pending, Valid or Business ID invalidated
//   ytj.tradeRegisterStatus  status on the Trade Register, for example Registered
//   ytj.situation            current liquidation, bankruptcy or re-organisation, if any
//
// No API key is needed. See README.md next to this file for the enricher settings.
//
// A record gets no result (nothing is stored) when it has no valid Business ID, when the
// Business ID isn't found, or when the API can't answer.

// ---- Settings -------------------------------------------------------------------------

// Vocabulary key to read. Add the same key to the Vocabulary and Properties field.
const BUSINESS_ID_KEY = "organization.businessId";

const YTJ_URL = "https://avoindata.prh.fi/opendata-ytj-api/v3/companies";

// How long to reuse an answer for the same Business ID. 0 turns caching off.
const CACHE_MILLISECONDS = 24 * 60 * 60 * 1000;

// ---- Script ---------------------------------------------------------------------------

// Code lists from https://avoindata.prh.fi/opendata-ytj-api/v3/description?code=...&lang=en
const BUSINESS_ID_STATUSES = { "1": "Pending", "2": "Valid", "5": "Business ID invalidated" };
const TRADE_REGISTER_STATUSES = {
  "0": "Unregistered",
  "1": "Registered",
  "2": "Removed from register",
  "3": "Start-up not registered",
  "4": "Ceased",
};
const SITUATIONS = { KONK: "Bankrupt", SANE: "Company re-organisation", SELTILA: "Liquidation" };
const ENGLISH = "3";
const FINNISH = "1";

function getValue(key) {
  // A plain loop rather than vocabularies.find(...): vocabularies is a .NET list, and when
  // .find is called from inside a function, later calls return the first call's match.
  const items = vocabularies || [];
  for (let i = 0; i < items.length; i++) {
    if (items[i].Key === key) {
      const value = items[i].Value;
      return value === null || value === undefined ? "" : String(value).trim();
    }
  }
  return "";
}

// Accepts "0112038-9", "01120389", "112038-9" (old form without the leading zero), and the VAT
// number form "FI01120389". Returns "1234567-8", or null when it isn't a valid Business ID
// (MOD11 check digit).
function parseBusinessId(raw) {
  const text = raw.toUpperCase().replace(/\s/g, "").replace(/^FI/, "");
  const match = /^(\d{6,7})-?(\d)$/.exec(text);
  if (!match) {
    return null;
  }
  const body = match[1].length === 6 ? "0" + match[1] : match[1];
  const weights = [7, 9, 10, 5, 8, 4, 2];
  let sum = 0;
  for (let i = 0; i < 7; i++) {
    sum += Number(body.charAt(i)) * weights[i];
  }
  const remainder = sum % 11;
  if (remainder === 1) {
    return null;
  }
  const checkDigit = remainder === 0 ? 0 : 11 - remainder;
  return checkDigit === Number(match[2]) ? `${body}-${match[2]}` : null;
}

function clean(value) {
  if (value === null || value === undefined) {
    return null;
  }
  const text = String(value).trim();
  return text === "" ? null : text;
}

function parseJson(text) {
  try {
    return JSON.parse(text);
  } catch (e) {
    return null;
  }
}

function dateOnly(value) {
  const text = clean(value);
  return text ? text.substring(0, 10) : null;
}

function list(value) {
  return Array.isArray(value) ? value.filter((x) => !!x) : [];
}

// Returns the description in the given language, or the first one there is.
function describe(descriptions, languageCode) {
  const items = list(descriptions);
  for (let i = 0; i < items.length; i++) {
    if (items[i].languageCode === languageCode && clean(items[i].description)) {
      return clean(items[i].description);
    }
  }
  return items.length > 0 ? clean(items[0].description) : null;
}

function cityOf(address) {
  const offices = list(address && address.postOffices);
  for (let i = 0; i < offices.length; i++) {
    if (offices[i].languageCode === FINNISH && clean(offices[i].city)) {
      return clean(offices[i].city);
    }
  }
  return offices.length > 0 ? clean(offices[0].city) : null;
}

function findAddress(company, type) {
  const addresses = list(company.addresses);
  for (let i = 0; i < addresses.length; i++) {
    if (Number(addresses[i].type) === type) {
      return addresses[i];
    }
  }
  return null;
}

function formatAddress(address) {
  if (!address) {
    return null;
  }
  const apartment = [clean(address.apartmentNumber), clean(address.apartmentIdSuffix)].filter((x) => !!x).join("");
  const street = [clean(address.street), clean(address.buildingNumber), clean(address.entrance), apartment]
    .filter((x) => !!x)
    .join(" ");
  const parts = [];
  if (clean(address.co)) {
    parts.push(`c/o ${clean(address.co)}`);
  }
  if (street) {
    parts.push(street);
  }
  if (clean(address.postOfficeBox)) {
    parts.push(`PL ${clean(address.postOfficeBox)}`);
  }
  const postalTown = [clean(address.postCode), cityOf(address)].filter((x) => !!x).join(" ");
  if (postalTown) {
    parts.push(postalTown);
  }
  return parts.length > 0 ? parts.join(", ") : null;
}

// Current company name: type 1 ("Company name") with no end date.
function currentName(company) {
  const names = list(company.names);
  for (let i = 0; i < names.length; i++) {
    if (names[i].type === "1" && !names[i].endDate && clean(names[i].name)) {
      return clean(names[i].name);
    }
  }
  return null;
}

function current(items) {
  const all = list(items);
  for (let i = 0; i < all.length; i++) {
    if (!all[i].endDate) {
      return all[i];
    }
  }
  return null;
}

// Calls the API. Returns the company, or null when there's no answer to store.
function lookUp(businessId) {
  const apiResponse = http.send({
    url: `${YTJ_URL}?businessId=${businessId}`,
    method: "GET",
    headers: [{ Key: "Accept", Value: "application/json" }],
  });

  const status = String(apiResponse.HttpStatus || "");
  const body = parseJson(apiResponse.Content);

  if (status === "TooManyRequests") {
    throw new Error("TooManyRequests - the YTJ API is busy, the record will be retried");
  }

  const companies = body ? list(body.companies) : [];
  for (let i = 0; i < companies.length; i++) {
    if (companies[i].businessId && companies[i].businessId.value === businessId) {
      return companies[i];
    }
  }

  log(`YTJ could not look up ${businessId}. HTTP ${status}. ${status === "OK" && body ? "Business ID not found" : String(apiResponse.Content || "").substring(0, 200)}`);
  return null;
}

function run() {
  const businessId = parseBusinessId(getValue(BUSINESS_ID_KEY));
  if (!businessId) {
    // No valid Business ID on this record (this is also what Test connection hits, because
    // it passes placeholder values instead of real ones).
    return [];
  }

  const cacheKey = `ytj:${businessId}`;
  const cached = CACHE_MILLISECONDS > 0 ? cache.get(cacheKey) : null;
  let company = cached ? parseJson(String(cached)) : null;

  if (!company) {
    company = lookUp(businessId);
    if (!company) {
      return [];
    }
    if (CACHE_MILLISECONDS > 0) {
      cache.set(cacheKey, JSON.stringify(company), CACHE_MILLISECONDS);
    }
  }

  const form = current(company.companyForms) || {};
  const businessLine = company.mainBusinessLine || {};
  const visitingAddress = findAddress(company, 1);
  const situations = list(company.companySituations)
    .filter((x) => !x.endDate)
    .map((x) => SITUATIONS[x.type] || clean(x.type))
    .filter((x) => !!x);

  const data = {
    "ytj.businessId": businessId,
    "ytj.euId": company.euId ? clean(company.euId.value) : null,
    "ytj.name": currentName(company),
    "ytj.companyForm": describe(form.descriptions, ENGLISH),
    "ytj.companyFormCode": clean(form.type),
    "ytj.mainBusinessLineCode": clean(businessLine.type),
    "ytj.mainBusinessLine": describe(businessLine.descriptions, ENGLISH),
    "ytj.website": company.website ? clean(company.website.url) : null,
    "ytj.visitingAddress": formatAddress(visitingAddress),
    "ytj.postalAddress": formatAddress(findAddress(company, 2)),
    "ytj.city": cityOf(visitingAddress),
    "ytj.postalCode": visitingAddress ? clean(visitingAddress.postCode) : null,
    "ytj.registrationDate": dateOnly(company.registrationDate),
    "ytj.endDate": dateOnly(company.endDate),
    "ytj.businessIdStatus": BUSINESS_ID_STATUSES[company.status] || clean(company.status),
    "ytj.tradeRegisterStatus": TRADE_REGISTER_STATUSES[company.tradeRegisterStatus] || clean(company.tradeRegisterStatus),
    "ytj.situation": situations.length > 0 ? situations.join("; ") : null,
  };

  // Leave out values YTJ didn't return, so they don't overwrite existing data with blanks.
  Object.keys(data).forEach((key) => {
    if (data[key] === null) {
      delete data[key];
    }
  });

  return [{ Data: data, Score: 100 }];
}

response = JSON.stringify(run());
```
