---
title: Enterprise Register (Latvia)
url: https://documentation.cluedin.net/govern/rest-api-enricher-samples/enterprise-register-latvia
content_type: reference
section: Govern & improve > REST API enricher samples
---

# Enterprise Register (Latvia)

> reference: Facts, options, APIs.

This example looks up a Latvian registration number in the [open data of the Register of Enterprises of the Republic of Latvia](https://data.gov.lv/dati/lv/dataset/uz) (Uzņēmumu reģistrs), published on the Latvian Open Data Portal and updated every day. It uses the portal's datastore search API. For each golden record it stores the registered name, legal form, register, status, registration and termination dates, and legal address. No API key is needed.

**Enricher version:** V2  
**API key:** not needed

To set up the enricher, see [Add REST API enricher](https://documentation.cluedin.net/govern/enrichment/rest-api.md#add-rest-api-enricher), then use the settings and script on this page.

## Settings

- **Accepted Business Domain** – `/Organization`, or the business domain that holds your companies.

- **Version** – V2 (recommended).

- **API Key** – leave empty.

- **Filters** – we recommend a rule that only accepts golden records where `organization.registrationNumber` has a value. Otherwise, every record without a registration number is listed on the enricher's **Logs** tab as having returned no results.

## Vocabulary and Properties

```
organization.registrationNumber
```

`organization.registrationNumber` holds the 11-digit Latvian registration number (reģistrācijas numurs), for example `40003032949`. The VAT number form, `LV40003032949`, is also accepted. If your data uses another vocabulary key, change this field and the `REGISTRATION_NUMBER_KEY` value at the top of the script.

## Request and response

**Base URL:** `https://data.gov.lv/dati/api/3/action`  
**Endpoint:** `GET /datastore_search?resource_id=25e80bf3-f107-4ab4-89ef-251b5b9374e9&limit=1&filters={"regcode":"<number>"}`  
**Authentication:** none

The script asks for an exact match on the `regcode` column. The `filters` value is URL-encoded:

```http
GET https://data.gov.lv/dati/api/3/action/datastore_search?resource_id=25e80bf3-f107-4ab4-89ef-251b5b9374e9&limit=1&filters=%7B%22regcode%22%3A%2240003032949%22%7D
Accept: application/json
```

Response:

```json
{
  "success": true,
  "result": {
    "resource_id": "25e80bf3-f107-4ab4-89ef-251b5b9374e9",
    "records": [
      {
        "_id": 457770,
        "regcode": 40003032949,
        "sepa": "LV61ZZZ40003032949",
        "name": "Akciju sabiedrība \"Latvenergo\"",
        "name_before_quotes": "Akciju sabiedrība",
        "name_in_quotes": "Latvenergo",
        "name_after_quotes": "",
        "without_quotes": 0,
        "regtype": "K",
        "regtype_text": "Komercreģistrs",
        "type": "AS",
        "type_text": "Akciju sabiedrība",
        "registered": "1991-10-08T00:00:00",
        "terminated": null,
        "closed": " ",
        "address": "Rīga, Pulkveža Brieža iela 12",
        "index": 1010,
        "addressid": 101971850,
        "region": 0,
        "city": 100003003,
        "atvk": 10000,
        "reregistration_term": ""
      }
    ],
    "total": 1
  }
}
```

## Properties added by the enricher

| Property | Response field | Example |
| -------- | -------------- | ------- |
| `lvur.registrationNumber` | `regcode` | `40003032949` |
| `lvur.name` | `name` | `Akciju sabiedrība "Latvenergo"` |
| `lvur.legalForm` | `type_text` | `Akciju sabiedrība` |
| `lvur.legalFormCode` | `type` | `AS` |
| `lvur.register` | `regtype_text` | `Komercreģistrs` |
| `lvur.status` | `closed`: blank becomes `Registered`, `L` becomes `Liquidated`, `R` becomes `Reorganised` | `Registered` |
| `lvur.registrationDate` | `registered` | `1991-10-08` |
| `lvur.terminationDate` | `terminated`: the date the entity was removed from the register, or the reorganization date | `2014-04-10` |
| `lvur.address` | `address` | `Rīga, Pulkveža Brieža iela 12` |
| `lvur.postalCode` | `index`, written as `LV-NNNN` | `LV-1010` |
| `lvur.sepaCreditorId` | `sepa` | `LV61ZZZ40003032949` |

A property is added only when the register has a value for it.

If the enricher has a **Preview** tab, the results appear there first. To add them to golden records, go to the **Map** tab, select **Map Data**, and choose **Auto Mapping**. Select the business domain, enter a new vocabulary named `Latvian Enterprise Register` with the key prefix `lvur`, and then create the mapping. Auto mapping also uses `name` as the golden record name, so remove that from the mapping if you want to keep your existing names. Then process the data on the **Process** tab. If the enricher has no **Preview** tab, the properties are added to the golden record as soon as it is enriched.

## How the script handles input and errors

- Spaces, dots, dashes, and a leading `LV` are removed, so `LV 4000 303 2949` is looked up as `40003032949`. Golden records without an 11-digit number are skipped without calling the API.

- If the register has no entity with the number, or the API returns an error, the script logs the reason and adds nothing.

- If the portal reports that it is too busy (HTTP 429 or 503), the script throws an error that makes the enricher try the golden record again later.

- Successful results are cached for 24 hours per registration number. To change this, edit `CACHE_MILLISECONDS` in the script.

## Testing the enricher

- **Test connection** checks only that the script runs. It doesn't call the API.

- To try the setup, create a golden record with `organization.registrationNumber` set to `40003032949` (Latvenergo). `41202013815` returns a liquidated sole trader, with `lvur.status` = `Liquidated` and a termination date.

## Limitations

- The open data has the basic details of each entity only. Officers, shareholders, beneficial owners, history and filed documents are available from the Register of Enterprises' [register API web services](https://www.ur.gov.lv/en/registry-api-web-services-service-list). Some of those services are free and some are paid, and all of them need registration and an API key.

- Legal forms and register names are in Latvian.

## Process script

```javascript
// REST API enricher (V2) - Latvian company lookup with the Enterprise Register's open data
//
// Looks up a golden record's Latvian registration number in the Register of Enterprises of the
// Republic of Latvia (Uzņēmumu reģistrs) open data, which the Latvian Open Data Portal
// publishes at https://data.gov.lv/dati/lv/dataset/uz, using the portal's CKAN datastore search
// API, and adds the result to the golden record as lvur.* properties:
//
//   lvur.registrationNumber  11-digit registration number that was looked up
//   lvur.name                registered name
//   lvur.legalForm           legal form, for example Akciju sabiedrība
//   lvur.legalFormCode       legal form code, for example AS
//   lvur.register            register the entity is in, for example Komercreģistrs
//   lvur.status              Registered, Liquidated or Reorganised
//   lvur.registrationDate    date of registration (YYYY-MM-DD)
//   lvur.terminationDate     date the entity was removed from the register (YYYY-MM-DD)
//   lvur.address             legal address
//   lvur.postalCode          postal code of the legal address, for example LV-1010
//   lvur.sepaCreditorId      SEPA creditor identifier
//
// No API key is needed. See README.md next to this file for the enricher settings.
//
// A record gets no result (nothing is stored) when it has no valid registration number, when
// the number isn't in the register, or when the API can't answer.

// ---- Settings -------------------------------------------------------------------------

// Vocabulary key to read. Add the same key to the Vocabulary and Properties field.
const REGISTRATION_NUMBER_KEY = "organization.registrationNumber";

const DATASTORE_URL = "https://data.gov.lv/dati/api/3/action/datastore_search";
// "Register" resource of the Enterprise Register's open data on data.gov.lv
const RESOURCE_ID = "25e80bf3-f107-4ab4-89ef-251b5b9374e9";

// How long to reuse an answer for the same registration number. 0 turns caching off.
const CACHE_MILLISECONDS = 24 * 60 * 60 * 1000;

// ---- Script ---------------------------------------------------------------------------

// What the register's "closed" code means. A blank code means the entity is still registered.
const CLOSED_STATUSES = { L: "Liquidated", R: "Reorganised" };

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

// Accepts "40003032949", "4000 303 2949" and the VAT number form "LV40003032949". Returns the
// 11 digits, or null when the value isn't an 11-digit Latvian registration number.
function parseRegistrationNumber(raw) {
  const text = raw.toUpperCase().replace(/^LV/, "").replace(/[\s.\-]/g, "");
  return /^\d{11}$/.test(text) ? text : null;
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

// "1991-10-08T00:00:00" -> "1991-10-08"
function dateOnly(value) {
  const text = clean(value);
  return text && /^\d{4}-\d{2}-\d{2}/.test(text) ? text.substring(0, 10) : null;
}

// Calls the datastore API. Returns the entity's row, or null when there's no answer to store.
function lookUp(registrationNumber) {
  const filters = { regcode: registrationNumber };
  const apiResponse = http.send({
    url: `${DATASTORE_URL}?resource_id=${RESOURCE_ID}&limit=1&filters=${encodeURIComponent(JSON.stringify(filters))}`,
    method: "GET",
    headers: [{ Key: "Accept", Value: "application/json" }],
  });

  const status = String(apiResponse.HttpStatus || "");
  const body = parseJson(apiResponse.Content);

  if (status === "TooManyRequests" || status === "ServiceUnavailable") {
    throw new Error(`TooManyRequests - data.gov.lv is busy (HTTP ${status}), the record will be retried`);
  }

  const records = body && body.success === true && body.result && Array.isArray(body.result.records)
    ? body.result.records
    : null;

  if (status !== "OK" || !records) {
    log(`data.gov.lv could not look up registration number ${registrationNumber}. HTTP ${status}. ${String(apiResponse.Content || "").substring(0, 200)}`);
    return null;
  }

  for (let i = 0; i < records.length; i++) {
    if (String(records[i].regcode) === registrationNumber) {
      return records[i];
    }
  }

  log(`The Enterprise Register has no entity with registration number ${registrationNumber}.`);
  return null;
}

function run() {
  const registrationNumber = parseRegistrationNumber(getValue(REGISTRATION_NUMBER_KEY));
  if (!registrationNumber) {
    // No valid registration number on this record (this is also what Test connection hits,
    // because it passes placeholder values instead of real ones).
    return [];
  }

  const cacheKey = `lvur:${registrationNumber}`;
  const cached = CACHE_MILLISECONDS > 0 ? cache.get(cacheKey) : null;
  let row = cached ? parseJson(String(cached)) : null;

  if (!row) {
    row = lookUp(registrationNumber);
    if (!row) {
      return [];
    }
    if (CACHE_MILLISECONDS > 0) {
      cache.set(cacheKey, JSON.stringify(row), CACHE_MILLISECONDS);
    }
  }

  const closed = clean(row.closed);
  const postalCode = clean(row.index);

  const data = {
    "lvur.registrationNumber": registrationNumber,
    "lvur.name": clean(row.name),
    "lvur.legalForm": clean(row.type_text),
    "lvur.legalFormCode": clean(row.type),
    "lvur.register": clean(row.regtype_text),
    "lvur.status": closed ? CLOSED_STATUSES[closed] || closed : "Registered",
    "lvur.registrationDate": dateOnly(row.registered),
    "lvur.terminationDate": dateOnly(row.terminated),
    "lvur.address": clean(row.address),
    // Latvian postal codes are written LV-NNNN; the register stores only the digits.
    "lvur.postalCode": postalCode && /^\d{4}$/.test(postalCode) ? `LV-${postalCode}` : postalCode,
    "lvur.sepaCreditorId": clean(row.sepa),
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
