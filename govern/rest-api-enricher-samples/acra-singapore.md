---
title: ACRA (Singapore)
url: https://documentation.cluedin.net/govern/rest-api-enricher-samples/acra-singapore
content_type: reference
section: Govern & improve > REST API enricher samples
---

# ACRA (Singapore)

> reference: Facts, options, APIs.

This example looks up an organization's Singapore Unique Entity Number (UEN) in the [Entities Registered with ACRA](https://data.gov.sg/datasets/d_3f960c10fed6145404ca7b821f263b87/view) dataset. The Accounting and Corporate Regulatory Authority (ACRA) publishes this dataset on data.gov.sg, Singapore's open data portal, and updates it monthly. The script searches it with the data.gov.sg datastore API. For each golden record it stores the registered name, UEN status, entity type, registration date, and the street name and postal code of the registered address.

This uses ACRA's **open data** on data.gov.sg, which is free and needs no API key. It is not ACRA's paid bizfile+ API (available through ACRA's API marketplace), which adds details such as officers and shareholders.

**Enricher version:** V2  
**API key:** not needed. A data.gov.sg API key is optional and gives a higher rate limit.

To set up the enricher, see [Add REST API enricher](https://documentation.cluedin.net/govern/enrichment/rest-api.md#add-rest-api-enricher), then use the settings and script on this page.

## Settings

- **Accepted Business Domain** – `/Organization`, or the business domain that holds your companies.

- **Version** – V2 (recommended).

- **API Key** – leave empty, or enter a data.gov.sg API key to get a higher rate limit. When the field has a value, the script sends it in the `x-api-key` header.

- **Filters** – we recommend a rule that only accepts golden records where `organization.uen` has a value. Otherwise, every record without a UEN is listed on the enricher's **Logs** tab as having returned no results.

## Vocabulary and Properties

```
organization.uen
```

`organization.uen` holds the UEN. If your data uses another vocabulary key, change this field and the `UEN_KEY` value at the top of the script.

## Request and response

**Base URL:** `https://data.gov.sg/api/action`  
**Endpoint:** `GET /datastore_search?resource_id=d_3f960c10fed6145404ca7b821f263b87&filters={"uen":"{uen}"}&limit=1`  
**Authentication:** none; optionally a data.gov.sg API key in the `x-api-key` header

The script sends one request per golden record (the `filters` value is URL-encoded):

```http
GET https://data.gov.sg/api/action/datastore_search?resource_id=d_3f960c10fed6145404ca7b821f263b87&filters=%7B%22uen%22%3A%22196800306E%22%7D&limit=1
Accept: application/json
```

Shortened response:

```json
{
  "success": true,
  "result": {
    "resource_id": "d_3f960c10fed6145404ca7b821f263b87",
    "records": [
      {
        "_id": 1383192,
        "uen": "196800306E",
        "issuance_agency_desc": "ACRA",
        "uen_status_desc": "Registered",
        "entity_name": "DBS BANK LTD.",
        "entity_type_desc": "Local Company",
        "uen_issue_date": "1968-07-16",
        "reg_street_name": "MARINA BOULEVARD",
        "reg_postal_code": "018982"
      }
    ],
    "total": 1,
    "limit": 1
  }
}
```

A UEN that isn't in the dataset returns `"records": []`.

## Properties added by the enricher

| Property | Response field | Example |
| -------- | -------------- | ------- |
| `acra.uen` | `uen` | `196800306E` |
| `acra.name` | `entity_name` | `DBS BANK LTD.` |
| `acra.status` | `uen_status_desc` | `Registered` |
| `acra.entityType` | `entity_type_desc` | `Local Company` |
| `acra.registrationDate` | `uen_issue_date` | `1968-07-16` |
| `acra.streetName` | `reg_street_name` | `MARINA BOULEVARD` |
| `acra.postalCode` | `reg_postal_code` | `018982` |
| `acra.issuanceAgency` | `issuance_agency_desc` | `ACRA` |

A property is added only when the dataset has a value for it.

If the enricher has a **Preview** tab, the results appear there first. To add them to golden records, go to the **Map** tab, select **Map Data**, and choose **Auto Mapping**. Select the business domain, enter a new vocabulary named `ACRA` with the key prefix `acra`, and then create the mapping. Auto mapping also uses `name` as the golden record name, so remove that from the mapping if you want to keep your existing names. Then process the data on the **Process** tab. If the enricher has no **Preview** tab, the properties are added to the golden record as soon as it is enriched.

## How the script handles input and errors

- Spaces, dashes, and other punctuation are removed and letters are made upper case, so `1968 00306 e` is looked up as `196800306E`. The UEN must have one of the three UEN formats: 8 digits and a letter (businesses), a 4-digit year, 5 digits and a letter (local companies), or `T`, `S`, or `R`, 2 digits, a 2-letter entity type, 4 digits and a letter (other entities). Golden records without a valid UEN are skipped without calling the API.

- If the UEN isn't in the dataset or the API returns an error, the script logs the reason and adds nothing.

- If data.gov.sg rejects the API key, the script throws an error, so the golden record fails with the message on the enricher's **Logs** tab. Correct the key or leave the **API Key** field empty.

- If data.gov.sg reports that the rate limit is reached (HTTP 429), the script throws an error that makes the enricher try the golden record again later. If you enrich many golden records, add a data.gov.sg API key.

- Successful results are cached for 24 hours per UEN. To change this, edit `CACHE_MILLISECONDS` in the script.

## Testing the enricher

- **Test connection** checks only that the script runs. It doesn't call the API.

- To try the setup, create a golden record with `organization.uen` set to `196800306E` (DBS Bank) or `199201624D` (Singapore Telecommunications).

## Limitations

- The dataset covers entities registered with ACRA (businesses, companies, limited partnerships, limited liability partnerships, and others). UENs issued by other agencies aren't in it.

- The dataset is updated monthly, so a very recent change may not be in it yet.

- Only the street name and postal code of the registered address are published, not the full address. Officers, shareholders, and financial details aren't included.

## Process script

```javascript
// REST API enricher (V2) - Singapore company lookup with ACRA open data
//
// Looks up a golden record's Unique Entity Number (UEN) in the "Entities Registered with
// ACRA" dataset that the Accounting and Corporate Regulatory Authority (ACRA) publishes on
// data.gov.sg (https://data.gov.sg/datasets/d_3f960c10fed6145404ca7b821f263b87/view), using
// the data.gov.sg datastore search API, and adds the result to the golden record as acra.*
// properties:
//
//   acra.uen               UEN that was looked up
//   acra.name              registered entity name
//   acra.status            UEN status, for example Registered or Deregistered
//   acra.entityType        entity type, for example Local Company
//   acra.registrationDate  date the UEN was issued (YYYY-MM-DD)
//   acra.streetName        street name of the registered address
//   acra.postalCode        postal code of the registered address
//   acra.issuanceAgency    agency that issued the UEN, for example ACRA
//
// No API key is needed. A data.gov.sg API key is optional and raises the rate limit: enter it
// in the enricher's API Key field and it's sent in the x-api-key header.
// See README.md next to this file for the enricher settings.
//
// A record gets no result (nothing is stored) when it has no valid UEN, when the UEN isn't in
// the dataset, or when the API can't answer.

// ---- Settings -------------------------------------------------------------------------

// Vocabulary key to read. Add the same key to the Vocabulary and Properties field.
const UEN_KEY = "organization.uen";

// Optional. The enricher replaces {APIKey} with the API Key field value (your data.gov.sg
// API key). Leave the API Key field empty to call the API without a key.
const API_KEY = "{APIKey}";

const DATASTORE_URL = "https://data.gov.sg/api/action/datastore_search";
// "Entities Registered with ACRA" dataset on data.gov.sg
const RESOURCE_ID = "d_3f960c10fed6145404ca7b821f263b87";

// How long to reuse an answer for the same UEN. 0 turns caching off.
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

// Accepts "196800306E", "1968 00306 e", "T08LL0001A", etc. Returns the UEN in upper case, or
// null when it doesn't have one of the three UEN formats:
//   businesses       8 digits + check letter          (for example 53012345D)
//   local companies  4-digit year + 5 digits + letter (for example 196800306E)
//   other entities   T/S/R + 2 digits + 2-letter type + 4 digits + letter (for example T08LL0001A)
function parseUen(raw) {
  const uen = raw.toUpperCase().replace(/[^A-Z0-9]/g, "");
  return /^(\d{8}[A-Z]|\d{9}[A-Z]|[TSR]\d{2}[A-Z]{2}\d{4}[A-Z])$/.test(uen) ? uen : null;
}

function clean(value) {
  if (value === null || value === undefined) {
    return null;
  }
  const text = String(value).trim();
  return text === "" || text.toLowerCase() === "na" ? null : text;
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

// Calls the data.gov.sg datastore search API. Returns the entity, or null when there's no
// answer to store.
function lookUp(uen) {
  const headers = [{ Key: "Accept", Value: "application/json" }];
  if (clean(API_KEY)) {
    headers.push({ Key: "x-api-key", Value: API_KEY });
  }

  const filters = encodeURIComponent(JSON.stringify({ uen: uen }));
  const apiResponse = http.send({
    url: `${DATASTORE_URL}?resource_id=${RESOURCE_ID}&filters=${filters}&limit=1`,
    method: "GET",
    headers: headers,
  });

  const status = String(apiResponse.HttpStatus || "");
  const body = parseJson(apiResponse.Content);

  if (status === "TooManyRequests") {
    throw new Error("TooManyRequests - data.gov.sg rate limit reached, the record will be retried");
  }

  if (status === "Unauthorized" || status === "Forbidden") {
    throw new Error(`data.gov.sg rejected the API key in the API Key field (HTTP ${status}). Correct the key, or leave the field empty.`);
  }

  const records = body && body.success === true && body.result && Array.isArray(body.result.records)
    ? body.result.records
    : null;

  if (status === "OK" && records) {
    for (let i = 0; i < records.length; i++) {
      if (records[i] && String(records[i].uen || "").toUpperCase() === uen) {
        return records[i];
      }
    }
    log(`UEN ${uen} isn't in the Entities Registered with ACRA dataset.`);
    return null;
  }

  log(`data.gov.sg could not look up ${uen}. HTTP ${status}. ${String(apiResponse.Content || "").substring(0, 200)}`);
  return null;
}

function run() {
  const uen = parseUen(getValue(UEN_KEY));
  if (!uen) {
    // No valid UEN on this record (this is also what Test connection hits, because it passes
    // placeholder values instead of real ones).
    return [];
  }

  const cacheKey = `acra:${uen}`;
  const cached = CACHE_MILLISECONDS > 0 ? cache.get(cacheKey) : null;
  let entity = cached ? parseJson(String(cached)) : null;

  if (!entity) {
    entity = lookUp(uen);
    if (!entity) {
      return [];
    }
    if (CACHE_MILLISECONDS > 0) {
      cache.set(cacheKey, JSON.stringify(entity), CACHE_MILLISECONDS);
    }
  }

  const data = {
    "acra.uen": clean(entity.uen),
    "acra.name": clean(entity.entity_name),
    "acra.status": clean(entity.uen_status_desc),
    "acra.entityType": clean(entity.entity_type_desc),
    "acra.registrationDate": dateOnly(entity.uen_issue_date),
    "acra.streetName": clean(entity.reg_street_name),
    "acra.postalCode": clean(entity.reg_postal_code),
    "acra.issuanceAgency": clean(entity.issuance_agency_desc),
  };

  // Leave out values the dataset doesn't have, so they don't overwrite existing data with blanks.
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
