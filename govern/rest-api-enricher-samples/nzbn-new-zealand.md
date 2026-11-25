---
title: Companies Office NZBN (New Zealand)
url: https://documentation.cluedin.net/govern/rest-api-enricher-samples/nzbn-new-zealand
content_type: reference
section: Govern & improve > REST API enricher samples
---

# Companies Office NZBN (New Zealand)

> reference: Facts, options, APIs.

This example looks up an organization's New Zealand Business Number (NZBN) in the NZBN Register by using the [NZBN API](https://portal.api.business.govt.nz/api/nzbn) (version 5), which the New Zealand Companies Office provides on its API portal. For each golden record it stores the entity name, status, entity type, registration date, its number in the source register (the company number for companies), the registered and postal addresses, website, main industry classification, and trading names.

**Enricher version:** V2  
**API key:** your NZBN API subscription key. Create an account on the [Companies Office API portal](https://portal.api.business.govt.nz/) and subscribe to the NZBN API to get one.

To set up the enricher, see [Add REST API enricher](https://documentation.cluedin.net/govern/enrichment/rest-api.md#add-rest-api-enricher), then use the settings and script on this page.

## Settings

- **Accepted Business Domain** – `/Organization`, or the business domain that holds your companies.

- **Version** – V2 (recommended).

- **API Key** – your NZBN API subscription key. The enricher puts it in place of `{APIKey}` in the script, which sends it in the `Ocp-Apim-Subscription-Key` header.

- **Filters** – we recommend a rule that only accepts golden records where `organization.nzbn` has a value. Otherwise, every record without an NZBN is listed on the enricher's **Logs** tab as having returned no results.

## Vocabulary and Properties

```
organization.nzbn
```

`organization.nzbn` holds the 13-digit NZBN. If your data uses another vocabulary key, change this field and the `NZBN_KEY` value at the top of the script.

## Request and response

**Base URL:** `https://api.business.govt.nz/gateway/nzbn/v5`  
**Endpoint:** `GET /entities/{nzbn}`  
**Authentication:** subscription key in the `Ocp-Apim-Subscription-Key` header

The script sends one request per golden record:

```http
GET https://api.business.govt.nz/gateway/nzbn/v5/entities/9429040402543
Accept: application/json
Ocp-Apim-Subscription-Key: your-subscription-key
```

Shortened response:

```json
{
  "entityStatusCode": "50",
  "entityName": "AIR NEW ZEALAND LIMITED",
  "nzbn": "9429040402543",
  "entityTypeCode": "LTD",
  "entityTypeDescription": "NZ Limited Company",
  "entityStatusDescription": "Registered",
  "registrationDate": "1940-04-26T00:00:00.000+1200",
  "sourceRegister": "COMPANY",
  "sourceRegisterUniqueIdentifier": "104799",
  "addresses": {
    "addressList": [
      { "addressType": "POSTAL", "address1": "Private Bag 92007", "address2": "Victoria Street West", "address3": "Auckland", "postCode": "1142", "countryCode": "NZ", "endDate": null },
      { "addressType": "REGISTERED", "address1": "185 Fanshawe Street", "address3": "Auckland", "postCode": "1010", "countryCode": "NZ", "endDate": null }
    ]
  },
  "websites": [{ "url": "www.airnewzealand.co.nz" }],
  "industryClassifications": [
    { "classificationCode": "I490008", "classificationDescription": "Air transport under CAA Rules part 121, 125, or 129" }
  ],
  "tradingNames": [{ "name": "Air New Zealand Limited", "endDate": null }]
}
```

## Properties added by the enricher

| Property | Response field | Example |
| -------- | -------------- | ------- |
| `nzbn.nzbn` | `nzbn` | `9429040402543` |
| `nzbn.name` | `entityName` | `AIR NEW ZEALAND LIMITED` |
| `nzbn.status` | `entityStatusDescription` | `Registered` |
| `nzbn.entityType` | `entityTypeDescription` | `NZ Limited Company` |
| `nzbn.entityTypeCode` | `entityTypeCode` | `LTD` |
| `nzbn.registrationDate` | `registrationDate` (date only) | `1940-04-26` |
| `nzbn.sourceRegister` | `sourceRegister` | `COMPANY` |
| `nzbn.sourceRegisterId` | `sourceRegisterUniqueIdentifier` (the company number for companies) | `104799` |
| `nzbn.registeredAddress` | current `REGISTERED` address in `addresses.addressList`, on one line | `185 Fanshawe Street, Auckland, 1010` |
| `nzbn.postalAddress` | current `POSTAL` address in `addresses.addressList`, on one line | `Private Bag 92007, Victoria Street West, Auckland, 1142` |
| `nzbn.website` | first `websites[].url` | `www.airnewzealand.co.nz` |
| `nzbn.industryCode` | first `industryClassifications[].classificationCode` | `I490008` |
| `nzbn.industry` | first `industryClassifications[].classificationDescription` | `Air transport under CAA Rules part 121, 125, or 129` |
| `nzbn.tradingNames` | current `tradingNames[].name` (separated by `; `) | `Air New Zealand Limited` |

A property is added only when the register returns a value for it. Addresses and trading names with an `endDate` are no longer current and are left out.

If the enricher has a **Preview** tab, the results appear there first. To add them to golden records, go to the **Map** tab, select **Map Data**, and choose **Auto Mapping**. Select the business domain, enter a new vocabulary named `NZBN` with the key prefix `nzbn`, and then create the mapping. Auto mapping also uses `name` as the golden record name, so remove that from the mapping if you want to keep your existing names. Then process the data on the **Process** tab. If the enricher has no **Preview** tab, the properties are added to the golden record as soon as it is enriched.

## How the script handles input and errors

- Spaces and dashes are removed, so `94 2904 0402 543` is looked up as `9429040402543`. The NZBN must have 13 digits, start with `94`, and have a valid check digit. Golden records without a valid NZBN are skipped without calling the API.

- If the **API Key** field is empty, the script logs a message and adds nothing, without calling the API.

- If the API rejects the subscription key (HTTP 401 or 403), the script throws an error, so the golden record fails with the message on the enricher's **Logs** tab. Correct the key in the **API Key** field.

- If the NZBN isn't found (HTTP 404) or the API returns another error, the script logs the reason and adds nothing.

- If the API reports that the rate limit is reached (HTTP 429), the script throws an error that makes the enricher try the golden record again later.

- Successful results are cached for 24 hours per NZBN. To change this, edit `CACHE_MILLISECONDS` in the script.

## Testing the enricher

- **Test connection** checks only that the script runs. It doesn't call the API.

- To try the setup against sandbox data first, subscribe to the NZBN sandbox on the API portal, and temporarily change `NZBN_URL` in the script to `https://api.business.govt.nz/sandbox/nzbn/v5/entities/`.

- With a production key, create a golden record with `organization.nzbn` set to `9429040402543` (Air New Zealand Limited).

## Limitations

- The request, headers, and rejected-key response on this page were checked against the live API. A successful lookup couldn't be run against the API itself while writing this example because it needs a subscription key. The response layout and field values were checked against the same NZBN Register data published on the public NZBN website.

- Only the first website and the first industry classification are added.

- Roles, shareholders, and filing details (in `company-details` and `roles`) aren't added.

## Process script

```javascript
// REST API enricher (V2) - New Zealand company lookup with the NZBN API
//
// Looks up a golden record's New Zealand Business Number (NZBN) in the NZBN Register, using
// the Companies Office / MBIE NZBN API v5 (https://portal.api.business.govt.nz/api/nzbn), and
// adds the result to the golden record as nzbn.* properties:
//
//   nzbn.nzbn              13-digit NZBN that was looked up
//   nzbn.name              entity name
//   nzbn.status            entity status, for example Registered or Removed
//   nzbn.entityType        entity type, for example NZ Limited Company
//   nzbn.entityTypeCode    entity type code, for example LTD
//   nzbn.registrationDate  date the entity was registered (YYYY-MM-DD)
//   nzbn.sourceRegister    register that holds the entity, for example COMPANY
//   nzbn.sourceRegisterId  the entity's number in that register (the company number for companies)
//   nzbn.registeredAddress current registered address on one line
//   nzbn.postalAddress     current postal address on one line
//   nzbn.website           first website
//   nzbn.industryCode      first industry classification code (BIC), for example I490008
//   nzbn.industry          first industry classification description
//   nzbn.tradingNames      current trading names, separated by "; "
//
// Needs an NZBN API subscription key, entered in the enricher's API Key field. Subscribe to
// the NZBN API on https://portal.api.business.govt.nz/ to get one.
// See README.md next to this file for the enricher settings.
//
// A record gets no result (nothing is stored) when it has no valid NZBN, when the NZBN isn't
// found, or when the API can't answer. A subscription key that the API rejects fails the
// record with an error, so the problem is visible on the enricher's Logs tab.

// ---- Settings -------------------------------------------------------------------------

// Vocabulary key to read. Add the same key to the Vocabulary and Properties field.
const NZBN_KEY = "organization.nzbn";

// The enricher replaces {APIKey} with the API Key field value (your NZBN API subscription key).
const API_KEY = "{APIKey}";

// Use https://api.business.govt.nz/sandbox/nzbn/v5/entities/ with a sandbox subscription
// key to try the setup against sandbox data first.
const NZBN_URL = "https://api.business.govt.nz/gateway/nzbn/v5/entities/";

// How long to reuse an answer for the same NZBN. 0 turns caching off.
const CACHE_MILLISECONDS = 24 * 60 * 60 * 1000;

// ---- Script ---------------------------------------------------------------------------

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

// Accepts "9429040402543", "94 2904 0402 543", etc. Returns the 13 digits, or null when the
// number isn't a valid NZBN (starts with 94, GS1 check digit).
function parseNzbn(raw) {
  const digits = raw.replace(/[^0-9]/g, "");
  if (!/^94\d{11}$/.test(digits)) {
    return null;
  }
  let sum = 0;
  for (let i = 0; i < 12; i++) {
    sum += Number(digits.charAt(i)) * (i % 2 === 0 ? 1 : 3);
  }
  return (10 - (sum % 10)) % 10 === Number(digits.charAt(12)) ? digits : null;
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

// "1940-04-26T00:00:00.000+1200" -> "1940-04-26" (the date in New Zealand time)
function dateOnly(value) {
  const text = clean(value);
  return text ? text.substring(0, 10) : null;
}

function currentItems(list) {
  return Array.isArray(list) ? list.filter((x) => x && !clean(x.endDate)) : [];
}

function formatAddress(entity, addressType) {
  const list = entity.addresses && Array.isArray(entity.addresses.addressList) ? entity.addresses.addressList : [];
  const addresses = currentItems(list).filter((x) => x.addressType === addressType);
  if (addresses.length === 0) {
    return null;
  }
  const address = addresses[0];
  const parts = [address.address1, address.address2, address.address3, address.address4, address.postCode]
    .map((x) => clean(x))
    .filter((x) => !!x);
  if (clean(address.countryCode) && address.countryCode !== "NZ") {
    parts.push(address.countryCode);
  }
  return parts.length > 0 ? parts.join(", ") : null;
}

// Calls the NZBN API. Returns the entity, or null when there's no answer to store.
function lookUp(nzbn) {
  const apiResponse = http.send({
    url: NZBN_URL + nzbn,
    method: "GET",
    headers: [
      { Key: "Accept", Value: "application/json" },
      { Key: "Ocp-Apim-Subscription-Key", Value: API_KEY },
    ],
  });

  const status = String(apiResponse.HttpStatus || "");
  const body = parseJson(apiResponse.Content);

  if (status === "TooManyRequests") {
    throw new Error("TooManyRequests - NZBN API rate limit reached, the record will be retried");
  }

  if (status === "Unauthorized" || status === "Forbidden") {
    throw new Error(`The NZBN API rejected the subscription key in the API Key field (HTTP ${status}). ${String(apiResponse.Content || "").substring(0, 200)}`);
  }

  if (status === "OK" && body && body.nzbn) {
    return body;
  }

  log(`The NZBN API could not look up ${nzbn}. HTTP ${status}. ${String(apiResponse.Content || "").substring(0, 200)}`);
  return null;
}

function run() {
  const nzbn = parseNzbn(getValue(NZBN_KEY));
  if (!nzbn) {
    // No valid NZBN on this record (this is also what Test connection hits, because it passes
    // placeholder values instead of real ones).
    return [];
  }

  if (!clean(API_KEY)) {
    log("The NZBN API needs a subscription key. Enter your key in the enricher's API Key field.");
    return [];
  }

  const cacheKey = `nzbn:${nzbn}`;
  const cached = CACHE_MILLISECONDS > 0 ? cache.get(cacheKey) : null;
  let entity = cached ? parseJson(String(cached)) : null;

  if (!entity) {
    entity = lookUp(nzbn);
    if (!entity) {
      return [];
    }
    if (CACHE_MILLISECONDS > 0) {
      cache.set(cacheKey, JSON.stringify(entity), CACHE_MILLISECONDS);
    }
  }

  const websites = Array.isArray(entity.websites) ? entity.websites.filter((x) => x && clean(x.url)) : [];
  const industries = Array.isArray(entity.industryClassifications)
    ? entity.industryClassifications.filter((x) => x && (clean(x.classificationCode) || clean(x.classificationDescription)))
    : [];
  const tradingNames = currentItems(entity.tradingNames).map((x) => clean(x.name)).filter((x) => !!x);

  const data = {
    "nzbn.nzbn": clean(entity.nzbn),
    "nzbn.name": clean(entity.entityName),
    "nzbn.status": clean(entity.entityStatusDescription),
    "nzbn.entityType": clean(entity.entityTypeDescription),
    "nzbn.entityTypeCode": clean(entity.entityTypeCode),
    "nzbn.registrationDate": dateOnly(entity.registrationDate),
    "nzbn.sourceRegister": clean(entity.sourceRegister),
    "nzbn.sourceRegisterId": clean(entity.sourceRegisterUniqueIdentifier),
    "nzbn.registeredAddress": formatAddress(entity, "REGISTERED"),
    "nzbn.postalAddress": formatAddress(entity, "POSTAL"),
    "nzbn.website": websites.length > 0 ? clean(websites[0].url) : null,
    "nzbn.industryCode": industries.length > 0 ? clean(industries[0].classificationCode) : null,
    "nzbn.industry": industries.length > 0 ? clean(industries[0].classificationDescription) : null,
    "nzbn.tradingNames": tradingNames.length > 0 ? tradingNames.join("; ") : null,
  };

  // Leave out values the register didn't return, so they don't overwrite existing data with blanks.
  Object.keys(data).forEach((key) => {
    if (data[key] === null) {
      delete data[key];
    }
  });

  return [{ Data: data, Score: 100 }];
}

response = JSON.stringify(run());
```

Up: [REST API enricher samples](https://documentation.cluedin.net/govern/rest-api-enricher-samples.md)
