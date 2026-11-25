---
title: Corporations Canada
url: https://documentation.cluedin.net/govern/rest-api-enricher-samples/corporations-canada
content_type: reference
section: Govern & improve > REST API enricher samples
---

# Corporations Canada

> reference: Facts, options, APIs.

This example looks up a Canadian federal corporation in the Corporations Canada registry by using the [Federal Corporation API](https://api.ised-isde.canada.ca/en/docs?api=corporations) from Innovation, Science and Economic Development Canada (ISED). It uses the golden record's corporation number or, if the record has none, its business number. For each golden record it stores the current corporation name, status, the act it is governed by, its 9-digit business number, the registered office address, the incorporation date, and the most recent year an annual return was filed.

**Enricher version:** V2  
**API key:** your ISED API key. Sign in to the [ISED API store](https://api.ised-isde.canada.ca/) and subscribe to the Corporations API to get one.

To set up the enricher, see [Add REST API enricher](https://documentation.cluedin.net/govern/enrichment/rest-api.md#add-rest-api-enricher), then use the settings and script on this page.

## Settings

- **Accepted Business Domain** – `/Organization`, or the business domain that holds your companies.

- **Version** – V2 (recommended).

- **API Key** – your ISED API key. The enricher puts it in place of `{APIKey}` in the script, which sends it in the `user-key` header.

- **Filters** – we recommend a rule that only accepts golden records where `organization.canadaCorporationNumber` or `organization.canadaBusinessNumber` has a value. Otherwise, every record without one is listed on the enricher's **Logs** tab as having returned no results.

## Vocabulary and Properties

```
organization.canadaCorporationNumber
organization.canadaBusinessNumber
```

`organization.canadaCorporationNumber` holds the federal corporation number (up to 7 digits, for example `000100-7`). `organization.canadaBusinessNumber` is optional. It is used only when the record has no corporation number, and holds the 9-digit business number from the Canada Revenue Agency, or a 15-character program account number such as `106679285RC0001`. If your data uses other vocabulary keys, change this field and the `CORPORATION_NUMBER_KEY` and `BUSINESS_NUMBER_KEY` values at the top of the script.

## Request and response

**Base URL:** `https://apigateway-passerelledapi.ised-isde.canada.ca/corporations/api/v1`  
**Endpoint:** `GET /corporations/{corporationNumber}.json?lang=eng` or `GET /corporations/{businessNumber}.json?lang=eng`  
**Authentication:** API key in the `user-key` header

The script sends one request per golden record:

```http
GET https://apigateway-passerelledapi.ised-isde.canada.ca/corporations/api/v1/corporations/1007.json?lang=eng
Accept: application/json
user-key: your-ised-api-key
```

Shortened response (the example from the API's specification):

```json
[
  {
    "corporationId": "1007",
    "act": "Boards of Trade Act - Part II",
    "status": "Active",
    "corporationNames": [
      { "CorporationName": { "name": "ABBOTSFORD-MATSQUI CHAMBER OF COMMERCE", "nameType": "Primary", "current": false, "effectiveDate": "1991-12-27", "expiryDate": "1995-02-06" } },
      { "CorporationName": { "name": "Abbotsford Chamber of Commerce", "nameType": "Primary", "current": true, "effectiveDate": "1995-02-06" } }
    ],
    "adresses": [
      { "address": { "addressLine": ["207 - 32900 SOUTH FRASER WAY"], "city": "ABBOTSFORD", "postalCode": "V2S 5A1", "provinceCode": "BC", "countryCode": "CA" } }
    ],
    "businessNumbers": { "businessNumber": "106679285" },
    "annualReturns": [{ "annualReturn": { "annualMeetingdate": "2019-03-27", "yearOfFiling": "2019" } }],
    "activities": [{ "activity": { "activity": "Incorporation", "date": "1947-01-10" } }]
  }
]
```

A corporation that isn't found still returns HTTP 200, with messages instead of a corporation:

```json
["could not find corporation 123", "Corporation 123 est inconnu."]
```

## Properties added by the enricher

| Property | Response field | Example |
| -------- | -------------- | ------- |
| `corporationscanada.corporationNumber` | `corporationId` | `1007` |
| `corporationscanada.name` | current `Primary` name in `corporationNames` | `Abbotsford Chamber of Commerce` |
| `corporationscanada.status` | `status` | `Active` |
| `corporationscanada.act` | `act` | `Boards of Trade Act - Part II` |
| `corporationscanada.businessNumber` | `businessNumbers.businessNumber` | `106679285` |
| `corporationscanada.address` | first address in `adresses`, on one line | `207 - 32900 SOUTH FRASER WAY, ABBOTSFORD, BC, V2S 5A1` |
| `corporationscanada.city` | `address.city` | `ABBOTSFORD` |
| `corporationscanada.province` | `address.provinceCode` | `BC` |
| `corporationscanada.postalCode` | `address.postalCode` | `V2S 5A1` |
| `corporationscanada.incorporationDate` | date of the `Incorporation` activity | `1947-01-10` |
| `corporationscanada.lastAnnualReturn` | latest `annualReturns[].annualReturn.yearOfFiling` | `2019` |

A property is added only when the API returns a value for it. The address field is spelled `adresses` in the API.

If the enricher has a **Preview** tab, the results appear there first. To add them to golden records, go to the **Map** tab, select **Map Data**, and choose **Auto Mapping**. Select the business domain, enter a new vocabulary named `Corporations Canada` with the key prefix `corporationscanada`, and then create the mapping. Auto mapping also uses `name` as the golden record name, so remove that from the mapping if you want to keep your existing names. Then process the data on the **Process** tab. If the enricher has no **Preview** tab, the properties are added to the golden record as soon as it is enriched.

## How the script handles input and errors

- Spaces and dashes are removed from the corporation number, so `000100-7` is looked up as `1007`. A corporation number has up to 7 digits. When the record has no valid corporation number, the business number is used: its first 9 digits, which must pass the business number check digit (Luhn) test. Golden records with neither are skipped without calling the API.

- If the **API Key** field is empty, the script logs a message and adds nothing, without calling the API.

- If the API rejects the API key (HTTP 401 or 403), the script throws an error, so the golden record fails with the message on the enricher's **Logs** tab. Correct the key in the **API Key** field.

- If the corporation isn't found or the API returns another error, the script logs the reason and adds nothing.

- If the API reports that the rate limit is reached (HTTP 429), the script throws an error that makes the enricher try the golden record again later.

- Successful results are cached for 24 hours per number. To change this, edit `CACHE_MILLISECONDS` in the script.

- To get French names and descriptions, change `LANGUAGE` in the script to `fra`.

## Testing the enricher

- **Test connection** checks only that the script runs. It doesn't call the API.

- To try the setup, create a golden record with `organization.canadaCorporationNumber` set to `000100-7` (Abbotsford Chamber of Commerce), or `organization.canadaBusinessNumber` set to `106679285`.

## Limitations

- Only federal corporations are covered, not corporations registered only with a province or territory.

- The request and the rejected-key response on this page were checked against the live API. A successful lookup couldn't be run while writing this example because it needs an ISED API key, so the response layout and values are taken from the API's published specification.

- Directors aren't added. They are available from the separate `/v2/corporations/{number}/directors` endpoint.

## Process script

```javascript
// REST API enricher (V2) - Canadian federal corporation lookup with Corporations Canada
//
// Looks up a golden record's federal corporation number (or, if it has none, its 9-digit
// business number) in the Corporations Canada Federal Corporation API
// (https://api.ised-isde.canada.ca/en/docs?api=corporations), and adds the result to the
// golden record as corporationscanada.* properties:
//
//   corporationscanada.corporationNumber  corporation number, as returned (for example 1007)
//   corporationscanada.name               current corporation name
//   corporationscanada.status             status, for example Active or Dissolved
//   corporationscanada.act                act the corporation is governed by
//   corporationscanada.businessNumber     9-digit business number (BN9) from the CRA
//   corporationscanada.address            registered office address on one line
//   corporationscanada.city               city of the registered office
//   corporationscanada.province           province code, for example BC
//   corporationscanada.postalCode         postal code
//   corporationscanada.incorporationDate  date of incorporation (YYYY-MM-DD)
//   corporationscanada.lastAnnualReturn   most recent year an annual return was filed
//
// Needs an ISED API key, entered in the enricher's API Key field. Sign in to the ISED API
// store (https://api.ised-isde.canada.ca/) and subscribe to the Corporations API to get one.
// See README.md next to this file for the enricher settings.
//
// Only federal corporations are covered (not corporations registered only with a province or
// territory). A record gets no result (nothing is stored) when it has no valid number, when
// the corporation isn't found, or when the API can't answer. An API key that the API rejects
// fails the record with an error, so the problem is visible on the enricher's Logs tab.

// ---- Settings -------------------------------------------------------------------------

// Vocabulary keys to read. Add the same keys to the Vocabulary and Properties field.
const CORPORATION_NUMBER_KEY = "organization.canadaCorporationNumber";
// Optional. Only used when the record has no corporation number. A 9-digit business number,
// or a 15-character program account number such as 106679285RC0001.
const BUSINESS_NUMBER_KEY = "organization.canadaBusinessNumber";

// The enricher replaces {APIKey} with the API Key field value (your ISED API key).
const API_KEY = "{APIKey}";

const CORPORATIONS_URL = "https://apigateway-passerelledapi.ised-isde.canada.ca/corporations/api/v1/corporations/";
// eng for English, fra for French
const LANGUAGE = "eng";

// How long to reuse an answer for the same number. 0 turns caching off.
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

// Accepts "000100-7", "1007", "1234567", etc. Returns the number without leading zeros, or null.
function parseCorporationNumber(raw) {
  const text = raw.replace(/[\s-]/g, "");
  if (!/^\d{1,7}$/.test(text)) {
    return null;
  }
  const number = text.replace(/^0+/, "");
  return number === "" ? null : number;
}

// Accepts "106679285", "106 679 285", "106679285RC0001", etc. Returns the 9-digit business
// number, or null when it isn't valid (Luhn check digit).
function parseBusinessNumber(raw) {
  const text = raw.toUpperCase().replace(/[\s-]/g, "");
  const match = /^(\d{9})([A-Z]{2}\d{4})?$/.exec(text);
  if (!match) {
    return null;
  }
  const digits = match[1];
  let sum = 0;
  for (let i = 0; i < 9; i++) {
    let digit = Number(digits.charAt(8 - i));
    if (i % 2 === 1) {
      digit *= 2;
      if (digit > 9) {
        digit -= 9;
      }
    }
    sum += digit;
  }
  return sum % 10 === 0 ? digits : null;
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

function currentName(corporation) {
  const names = Array.isArray(corporation.corporationNames) ? corporation.corporationNames : [];
  let fallback = null;
  for (let i = 0; i < names.length; i++) {
    const name = names[i] && names[i].CorporationName;
    if (name && name.current === true && clean(name.name)) {
      if (String(name.nameType || "").toLowerCase() === "primary") {
        return clean(name.name);
      }
      fallback = fallback || clean(name.name);
    }
  }
  return fallback;
}

function firstAddress(corporation) {
  const addresses = Array.isArray(corporation.adresses) ? corporation.adresses : [];
  for (let i = 0; i < addresses.length; i++) {
    if (addresses[i] && addresses[i].address) {
      return addresses[i].address;
    }
  }
  return null;
}

function formatAddress(address) {
  if (!address) {
    return null;
  }
  const lines = Array.isArray(address.addressLine) ? address.addressLine.map((x) => clean(x)).filter((x) => !!x) : [];
  const parts = lines.concat([clean(address.city), clean(address.provinceCode), clean(address.postalCode)].filter((x) => !!x));
  if (clean(address.countryCode) && address.countryCode !== "CA") {
    parts.push(address.countryCode);
  }
  return parts.length > 0 ? parts.join(", ") : null;
}

function incorporationDate(corporation) {
  const activities = Array.isArray(corporation.activities) ? corporation.activities : [];
  for (let i = 0; i < activities.length; i++) {
    const activity = activities[i] && activities[i].activity;
    if (activity && String(activity.activity || "").trim().toLowerCase() === "incorporation") {
      return dateOnly(activity.date);
    }
  }
  return null;
}

function lastAnnualReturn(corporation) {
  const returns = Array.isArray(corporation.annualReturns) ? corporation.annualReturns : [];
  let latest = null;
  for (let i = 0; i < returns.length; i++) {
    const year = returns[i] && returns[i].annualReturn ? clean(returns[i].annualReturn.yearOfFiling) : null;
    if (year && (!latest || year > latest)) {
      latest = year;
    }
  }
  return latest;
}

// Calls the Corporations API. Returns the corporation, or null when there's no answer to store.
function lookUp(number) {
  const apiResponse = http.send({
    url: `${CORPORATIONS_URL}${number}.json?lang=${LANGUAGE}`,
    method: "GET",
    headers: [
      { Key: "Accept", Value: "application/json" },
      { Key: "user-key", Value: API_KEY },
    ],
  });

  const status = String(apiResponse.HttpStatus || "");
  const body = parseJson(apiResponse.Content);

  if (status === "TooManyRequests") {
    throw new Error("TooManyRequests - Corporations Canada API rate limit reached, the record will be retried");
  }

  if (status === "Unauthorized" || status === "Forbidden") {
    throw new Error(`The Corporations Canada API rejected the API key in the API Key field (HTTP ${status}). ${String(apiResponse.Content || "").substring(0, 200)}`);
  }

  // A corporation that isn't found still returns OK, with messages instead of a corporation:
  // ["could not find corporation 123", "Corporation 123 est inconnu."]
  if (status === "OK" && Array.isArray(body)) {
    for (let i = 0; i < body.length; i++) {
      if (body[i] && typeof body[i] === "object" && clean(body[i].corporationId)) {
        return body[i];
      }
    }
  }

  log(`Corporations Canada could not look up ${number}. HTTP ${status}. ${String(apiResponse.Content || "").substring(0, 200)}`);
  return null;
}

function run() {
  const number = parseCorporationNumber(getValue(CORPORATION_NUMBER_KEY))
    || parseBusinessNumber(getValue(BUSINESS_NUMBER_KEY));
  if (!number) {
    // No valid number on this record (this is also what Test connection hits, because it
    // passes placeholder values instead of real ones).
    return [];
  }

  if (!clean(API_KEY)) {
    log("The Corporations Canada API needs an API key. Enter your ISED API key in the enricher's API Key field.");
    return [];
  }

  const cacheKey = `corporationscanada:${number}`;
  const cached = CACHE_MILLISECONDS > 0 ? cache.get(cacheKey) : null;
  let corporation = cached ? parseJson(String(cached)) : null;

  if (!corporation) {
    corporation = lookUp(number);
    if (!corporation) {
      return [];
    }
    if (CACHE_MILLISECONDS > 0) {
      cache.set(cacheKey, JSON.stringify(corporation), CACHE_MILLISECONDS);
    }
  }

  const address = firstAddress(corporation);
  const businessNumbers = corporation.businessNumbers || {};

  const data = {
    "corporationscanada.corporationNumber": clean(corporation.corporationId),
    "corporationscanada.name": currentName(corporation),
    "corporationscanada.status": clean(corporation.status),
    "corporationscanada.act": clean(corporation.act),
    "corporationscanada.businessNumber": clean(businessNumbers.businessNumber),
    "corporationscanada.address": formatAddress(address),
    "corporationscanada.city": address ? clean(address.city) : null,
    "corporationscanada.province": address ? clean(address.provinceCode) : null,
    "corporationscanada.postalCode": address ? clean(address.postalCode) : null,
    "corporationscanada.incorporationDate": incorporationDate(corporation),
    "corporationscanada.lastAnnualReturn": lastAnnualReturn(corporation),
  };

  // Leave out values the API didn't return, so they don't overwrite existing data with blanks.
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
