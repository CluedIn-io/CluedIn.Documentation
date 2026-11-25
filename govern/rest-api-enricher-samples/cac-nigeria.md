---
title: CAC (Nigeria)
url: https://documentation.cluedin.net/govern/rest-api-enricher-samples/cac-nigeria
content_type: reference
section: Govern & improve > REST API enricher samples
---

# CAC (Nigeria)

> reference: Facts, options, APIs.

This example looks up an organization's registration number (RC number for companies, BN for business names, IT for incorporated trustees) in the Corporate Affairs Commission's (CAC) register by using the **Get Company by RC Number** operation of the [CAC-verified VAS API](https://vas.cac.gov.ng/). For each golden record it stores the registered name, entity type, status, address, registration date, and lines of business.

**Enricher version:** V2  
**API key:** your CAC VAS API key (create an account on the [VAS portal](https://vas.cac.gov.ng/), complete KYC, and generate a key; calls are charged to your prepaid VAS account balance)

To set up the enricher, see [Add REST API enricher](https://documentation.cluedin.net/govern/enrichment/rest-api.md#add-rest-api-enricher), then use the settings and script on this page.

## Settings

- **Accepted Business Domain** – `/Organization`, or the business domain that holds your companies.

- **Version** – V2 (recommended).

- **API Key** – your VAS API key. The script sends it in the `X_API_KEY` header. If the field is empty, the script adds nothing and doesn't call CAC.

- **Filters** – we recommend a rule that only accepts golden records where `organization.rcNumber` has a value. Otherwise, every record without a registration number is listed on the enricher's **Logs** tab as having returned no results.

## Vocabulary and Properties

```
organization.rcNumber
```

`organization.rcNumber` holds the CAC registration number, with or without its `RC`, `BN` or `IT` prefix. If your data uses another vocabulary key, change this field and the `RC_NUMBER_KEY` value at the top of the script.

## Request and response

**Base URL:** `https://vasapp.cac.gov.ng` (staging: `https://vasapp.oasisproducts.ng`)  
**Endpoint:** `POST /api/vas/validation/company/rc`  
**Authentication:** API key in the `X_API_KEY` request header. The endpoints are documented in CAC's [VAS Validation API documentation](https://documenter.getpostman.com/view/54596520/2sBY4VJcUc).

The script sends one request per golden record:

```http
POST https://vasapp.cac.gov.ng/api/vas/validation/company/rc
X_API_KEY: <your VAS API key>
Content-Type: application/json

{ "rc_number": "7068861" }
```

Response (the example from CAC's documentation; this sample couldn't be run against real data without a funded VAS account):

```json
{
  "statusCode": 200,
  "status": "OK",
  "message": "company data",
  "data": {
    "rc_number": "7068861",
    "entity_name": "24 HOUSE OF GRAPHICS AND CAFE",
    "entity_type": "BUSINESS_NAME_FIRM",
    "address": " sultan Bello Road Unguwan Sarki Kaduna",
    "registration_date": "Wed Jul 26 12:32:04 GMT 2023",
    "entity_status": "ACTIVE",
    "line_of_business": ["Computer programming, consultancy and related activities"]
  },
  "success": true,
  "count": 0
}
```

## Properties added by the enricher

| Property | Response field | Example |
| -------- | -------------- | ------- |
| `cac.rcNumber` | `data.rc_number` | `7068861` |
| `cac.name` | `data.entity_name` | `24 HOUSE OF GRAPHICS AND CAFE` |
| `cac.entityType` | `data.entity_type` | `BUSINESS_NAME_FIRM` |
| `cac.status` | `data.entity_status` | `ACTIVE` |
| `cac.address` | `data.address` | `sultan Bello Road Unguwan Sarki Kaduna` |
| `cac.registrationDate` | `data.registration_date`, as `YYYY-MM-DD` | `2023-07-26` |
| `cac.lineOfBusiness` | `data.line_of_business`, separated by `; ` | `Computer programming, consultancy and related activities` |

A property is added only when CAC returns a value for it.

If the enricher has a **Preview** tab, the results appear there first. To add them to golden records, go to the **Map** tab, select **Map Data**, and choose **Auto Mapping**. Select the business domain, enter a new vocabulary named `CAC` with the key prefix `cac`, and then create the mapping. Auto mapping also uses `name` as the golden record name, so remove that from the mapping if you want to keep your existing names. Then process the data on the **Process** tab. If the enricher has no **Preview** tab, the properties are added to the golden record as soon as it is enriched.

## How the script handles input and errors

- An `RC`, `BN` or `IT` prefix, spaces, dots, dashes, and leading zeros are removed, so `RC-7068861` is looked up as `7068861`. Golden records without a valid number (1 to 9 digits) are skipped without calling CAC.

- If CAC has no entity with that number (HTTP 400, `company not found`), the number is invalid (HTTP 400, `invalid rc_number passed`), or CAC returns another error, the script logs the reason and adds nothing.

- If CAC rejects the API key (HTTP 401), the script throws an error, so the golden record is listed on the **Logs** tab with a message to check the **API Key** field.

- If the VAS account doesn't have enough balance, or has no permission for the service (HTTP 403), the script throws an error with CAC's message, for example `insufficient balance to make this call.`

- If CAC reports that it is too busy (HTTP 429), the script throws an error that makes the enricher try the golden record again later.

- Successful results are cached for 7 days per registration number, because every call is charged. To change this, edit `CACHE_MILLISECONDS` in the script.

## Testing the enricher

- **Test connection** checks only that the script runs. It doesn't call CAC.

- To try the setup against CAC's staging environment, temporarily change `CAC_URL` in the script to `https://vasapp.oasisproducts.ng/api/vas/validation/company/rc` and enter a staging API key.

## Limitations

- Each call is charged to your VAS account balance. Keep the cache on, and add a filter so only records with a registration number are sent.

- The **Get Company by RC Number** operation returns basic details. Directors (affiliates), share capital, and status reports are separate VAS services that need a VRC (Virtual RC) code, and aren't used here.

- Entity types are returned as codes, such as `BUSINESS_NAME_FIRM`.

## Process script

```javascript
// REST API enricher (V2) - Nigerian company lookup with the CAC VAS API
//
// Looks up a golden record's RC, BN or IT number in the Corporate Affairs Commission's (CAC)
// register by using the "Get Company by RC Number" operation of the CAC-verified VAS API
// (https://vas.cac.gov.ng/), and adds the result to the golden record as cac.* properties:
//
//   cac.rcNumber          registration number that was looked up
//   cac.name              registered entity name
//   cac.entityType        entity type, for example BUSINESS_NAME_FIRM
//   cac.status            entity status, for example ACTIVE
//   cac.address           registered address
//   cac.registrationDate  date the entity was registered (YYYY-MM-DD)
//   cac.lineOfBusiness    lines of business, separated by "; "
//
// Needs a VAS API key (sent in the X_API_KEY header), entered in the enricher's API Key field.
// Each call is charged to your VAS account balance. See README.md next to this file.
//
// A record gets no result (nothing is stored) when it has no valid registration number, when CAC
// has no entity with that number, or when the API can't answer. A missing or rejected key, or an
// account without enough balance, fails the record with an error that says so.

// ---- Settings -------------------------------------------------------------------------

// Vocabulary key to read. Add the same key to the Vocabulary and Properties field.
const RC_NUMBER_KEY = "organization.rcNumber";

// Use https://vasapp.oasisproducts.ng/api/vas/validation/company/rc (with a staging API key) to
// try the setup against CAC's staging environment first.
const CAC_URL = "https://vasapp.cac.gov.ng/api/vas/validation/company/rc";

// The {APIKey} placeholder is replaced with the API Key field value.
const API_KEY = "{APIKey}";

// How long to reuse an answer for the same registration number. 0 turns caching off. Every
// call is charged, so a long cache saves money.
const CACHE_MILLISECONDS = 7 * 24 * 60 * 60 * 1000;

// ---- Script ---------------------------------------------------------------------------

const MONTHS = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"];

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

// Accepts "RC 123456", "RC-123456", "rc123456", "BN 2345678", "IT 12345" and plain digits.
// Returns the digits, or null when it isn't a CAC registration number.
function parseRcNumber(raw) {
  const text = raw.toUpperCase().replace(/^(RC|BN|IT)[\s.:-]*/, "");
  if (!/^[0-9\s.-]+$/.test(text)) {
    return null;
  }
  const digits = text.replace(/[^0-9]/g, "").replace(/^0+/, "");
  return /^\d{1,9}$/.test(digits) ? digits : null;
}

function clean(value) {
  if (value === null || value === undefined) {
    return null;
  }
  const text = String(value).replace(/\s+/g, " ").trim();
  return text === "" ? null : text;
}

function parseJson(text) {
  try {
    return JSON.parse(text);
  } catch (e) {
    return null;
  }
}

// The API returns dates such as "Wed Jul 26 12:32:04 GMT 2023". Returns "2023-07-26", or null.
function toDate(value) {
  const text = clean(value);
  if (!text) {
    return null;
  }
  const iso = /^(\d{4}-\d{2}-\d{2})/.exec(text);
  if (iso) {
    return iso[1];
  }
  const match = /^[A-Za-z]{3} ([A-Za-z]{3}) (\d{1,2}) [\d:]+ [A-Z]+ (\d{4})$/.exec(text);
  if (!match) {
    return null;
  }
  const month = MONTHS.indexOf(match[1].toUpperCase()) + 1;
  if (month === 0) {
    return null;
  }
  return `${match[3]}-${month < 10 ? "0" : ""}${month}-${match[2].length === 1 ? "0" : ""}${match[2]}`;
}

function errorText(body) {
  if (!body) {
    return "";
  }
  return [body.error, body.message].filter((x) => !!clean(x)).join(" - ");
}

// Calls the VAS API. Returns the entity, or null when there's no answer to store.
function lookUp(rcNumber) {
  const apiResponse = http.send({
    url: CAC_URL,
    method: "POST",
    headers: [
      { Key: "X_API_KEY", Value: API_KEY },
      { Key: "Content-Type", Value: "application/json" },
      { Key: "Accept", Value: "application/json" },
    ],
    body: { rc_number: rcNumber },
  });

  const status = String(apiResponse.HttpStatus || "");
  const body = parseJson(apiResponse.Content);

  if (status === "TooManyRequests") {
    throw new Error("TooManyRequests - the CAC VAS API is busy, the record will be retried");
  }

  if (status === "Unauthorized") {
    throw new Error("The CAC VAS API rejected the API key (HTTP Unauthorized). Check the API Key field of the enricher.");
  }

  // 403: not enough balance on the VAS account, or no permission for this service.
  if (status === "Forbidden") {
    throw new Error(`The CAC VAS API refused the call (HTTP Forbidden): ${errorText(body) || "forbidden"}. Check your VAS account balance and services.`);
  }

  const data = body && body.data;
  if (status === "OK" && data && !Array.isArray(data) && clean(data.rc_number)) {
    return data;
  }

  // 400 with "company not found" or "invalid rc_number passed", or a server error.
  log(`CAC could not look up ${rcNumber}. HTTP ${status}. ${errorText(body) || String(apiResponse.Content || "").substring(0, 200)}`);
  return null;
}

function run() {
  const rcNumber = parseRcNumber(getValue(RC_NUMBER_KEY));
  if (!rcNumber) {
    // No valid registration number on this record (this is also what Test connection hits,
    // because it passes placeholder values instead of real ones).
    return [];
  }

  if (!API_KEY) {
    log("No CAC VAS API key. Enter it in the API Key field of the enricher.");
    return [];
  }

  const cacheKey = `cac:${rcNumber}`;
  const cached = CACHE_MILLISECONDS > 0 ? cache.get(cacheKey) : null;
  let entity = cached ? parseJson(String(cached)) : null;

  if (!entity) {
    entity = lookUp(rcNumber);
    if (!entity) {
      return [];
    }
    if (CACHE_MILLISECONDS > 0) {
      cache.set(cacheKey, JSON.stringify(entity), CACHE_MILLISECONDS);
    }
  }

  const lines = Array.isArray(entity.line_of_business)
    ? entity.line_of_business.map((x) => clean(x)).filter((x) => !!x)
    : [];

  const data = {
    "cac.rcNumber": clean(entity.rc_number),
    "cac.name": clean(entity.entity_name),
    "cac.entityType": clean(entity.entity_type),
    "cac.status": clean(entity.entity_status),
    "cac.address": clean(entity.address),
    "cac.registrationDate": toDate(entity.registration_date),
    "cac.lineOfBusiness": lines.length > 0 ? lines.join("; ") : null,
  };

  // Leave out values CAC didn't return, so they don't overwrite existing data with blanks.
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
