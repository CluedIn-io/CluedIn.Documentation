---
layout: cluedin
title: ABN Lookup (Australia)
parent: REST API enricher samples
grand_parent: Govern & improve
nav_order: 90
permalink: /govern/rest-api-enricher-samples/abn-lookup-australia
content_type: reference
summary: "Looks up Australian Business Numbers (ABNs) with the Australian Business Register's ABN Lookup web service and adds the entity name, type, status, ACN, GST registration and business names. V2 script; needs an ABN Lookup GUID."
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

This example looks up an organization's Australian Business Number (ABN) in the Australian Business Register by using the [ABN Lookup web services](https://abr.business.gov.au/Tools/WebServices) JSON interface. For each golden record it stores the ABN status, the entity name and type, the Australian Company Number (ACN), the state and postcode of the main business location, the date the entity registered for GST, and its registered business names.

**Enricher version:** V2  
**API key:** your ABN Lookup GUID (authentication key). It is free: register on the [ABN Lookup web services agreement](https://abr.business.gov.au/Tools/WebServicesAgreement) page and the GUID is emailed to you.

To set up the enricher, see [Add REST API enricher](/govern/enrichment/rest-api#add-rest-api-enricher), then use the settings and script on this page.

## Settings

- **Accepted Business Domain** – `/Organization`, or the business domain that holds your companies.

- **Version** – V2 (recommended).

- **API Key** – your ABN Lookup GUID. The enricher puts it in place of `{APIKey}` in the script.

- **Filters** – we recommend a rule that only accepts golden records where `organization.abn` has a value. Otherwise, every record without an ABN is listed on the enricher's **Logs** tab as having returned no results.

## Vocabulary and Properties

```
organization.abn
```

`organization.abn` holds the 11-digit ABN. If your data uses another vocabulary key, change this field and the `ABN_KEY` value at the top of the script.

## Request and response

**Base URL:** `https://abr.business.gov.au/json`  
**Endpoint:** `GET /AbnDetails.aspx?abn={abn}&callback=callback&guid={GUID}`  
**Authentication:** the GUID in the `guid` query parameter

The script sends one request per golden record:

```http
GET https://abr.business.gov.au/json/AbnDetails.aspx?abn=51824753556&callback=callback&guid=your-abn-lookup-guid
Accept: application/javascript
```

ABN Lookup answers with JSONP: a JSON object wrapped in the `callback(...)` function call. The script removes the wrapper. Example response (illustrative values):

```javascript
callback({
  "Abn": "51824753556",
  "AbnStatus": "Active",
  "AbnStatusEffectiveFrom": "2000-07-01",
  "Acn": "",
  "AddressDate": "2014-09-12",
  "AddressPostcode": "2600",
  "AddressState": "ACT",
  "BusinessName": [],
  "EntityName": "AUSTRALIAN TAXATION OFFICE",
  "EntityTypeCode": "CGE",
  "EntityTypeName": "Commonwealth Government Entity",
  "Gst": "2000-07-01",
  "Message": ""
})
```

Errors come back with HTTP 200 and the reason in `Message`, for example:

```javascript
callback({"Abn":"","AbnStatus":"", ... ,"Message":"The GUID entered is not recognised as a Registered Party"})
```

## Properties added by the enricher

| Property | Response field | Example |
| -------- | -------------- | ------- |
| `abn.abn` | `Abn` | `51824753556` |
| `abn.status` | `AbnStatus` | `Active` |
| `abn.statusEffectiveFrom` | `AbnStatusEffectiveFrom` | `2000-07-01` |
| `abn.acn` | `Acn` (companies only) | `123456789` |
| `abn.entityName` | `EntityName` | `AUSTRALIAN TAXATION OFFICE` |
| `abn.entityType` | `EntityTypeName` | `Commonwealth Government Entity` |
| `abn.entityTypeCode` | `EntityTypeCode` | `CGE` |
| `abn.businessNames` | `BusinessName` (separated by `; `) | `ATO; Australian Tax Office` |
| `abn.state` | `AddressState` | `ACT` |
| `abn.postcode` | `AddressPostcode` | `2600` |
| `abn.gstRegisteredFrom` | `Gst` | `2000-07-01` |

A property is added only when ABN Lookup returns a value for it.

If the enricher has a **Preview** tab, the results appear there first. To add them to golden records, go to the **Map** tab, select **Map Data**, and choose **Auto Mapping**. Select the business domain, enter a new vocabulary named `ABN` with the key prefix `abn`, and then create the mapping. Then process the data on the **Process** tab. If the enricher has no **Preview** tab, the properties are added to the golden record as soon as it is enriched.

## How the script handles input and errors

- Spaces, dashes, and a leading `ABN` are removed, so `ABN 51 824 753 556` is looked up as `51824753556`. The number must have 11 digits and pass the ABN check-digit (modulus 89) test. Golden records without a valid ABN are skipped without calling ABN Lookup.

- If the **API Key** field is empty, the script logs a message and adds nothing, without calling ABN Lookup.

- If ABN Lookup rejects the GUID, the script throws an error, so the golden record fails with the message on the enricher's **Logs** tab. Correct the GUID in the **API Key** field.

- If the ABN isn't found or ABN Lookup returns another error, the script logs the reason and adds nothing.

- If ABN Lookup is too busy (HTTP 429 or 503), the script throws an error that makes the enricher try the golden record again later.

- Successful results are cached for 24 hours per ABN. To change this, edit `CACHE_MILLISECONDS` in the script.

## Testing the enricher

- **Test connection** checks only that the script runs. It doesn't call ABN Lookup.

- To try the setup, create a golden record with `organization.abn` set to `51824753556` (the Australian Taxation Office).

## Limitations

- The response layout and the GUID error on this page were checked against the live ABN Lookup service. A successful lookup couldn't be run while writing this example because it needs a registered GUID, so the example response values are illustrative.

- The ABN Lookup JSON interface returns the state and postcode of the main business location, not the full street address.

- Historical details (previous names, earlier statuses) aren't added. They are available from the ABN Lookup SOAP web services.

## Process script

```javascript
// REST API enricher (V2) - Australian company lookup with ABN Lookup
//
// Looks up a golden record's Australian Business Number (ABN) in the Australian Business
// Register, using the ABN Lookup JSON web service (https://abr.business.gov.au/Tools/WebServices),
// and adds the result to the golden record as abn.* properties:
//
//   abn.abn                    11-digit ABN that was looked up
//   abn.status                 ABN status, for example Active or Cancelled
//   abn.statusEffectiveFrom    date the current ABN status took effect (YYYY-MM-DD)
//   abn.acn                    Australian Company Number (companies only)
//   abn.entityName             registered entity name
//   abn.entityType             entity type, for example Australian Private Company
//   abn.entityTypeCode         entity type code, for example PRV
//   abn.businessNames          registered business names, separated by "; "
//   abn.state                  state of the main business location, for example NSW
//   abn.postcode               postcode of the main business location
//   abn.gstRegisteredFrom      date the entity registered for GST (YYYY-MM-DD)
//
// Needs an ABN Lookup GUID (authentication key), entered in the enricher's API Key field.
// Register for one at https://abr.business.gov.au/Tools/WebServicesAgreement
// See README.md next to this file for the enricher settings.
//
// A record gets no result (nothing is stored) when it has no valid ABN, when the ABN isn't
// found, or when the service can't answer. A GUID that ABN Lookup rejects fails the record
// with an error, so the problem is visible on the enricher's Logs tab.

// ---- Settings -------------------------------------------------------------------------

// Vocabulary key to read. Add the same key to the Vocabulary and Properties field.
const ABN_KEY = "organization.abn";

// The enricher replaces {APIKey} with the API Key field value (your ABN Lookup GUID).
const API_KEY = "{APIKey}";

const ABN_LOOKUP_URL = "https://abr.business.gov.au/json/AbnDetails.aspx";

// How long to reuse an answer for the same ABN. 0 turns caching off.
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

// Accepts "51 824 753 556", "51824753556", "ABN 51-824-753-556", etc. Returns the 11 digits,
// or null when the number isn't a valid ABN (modulus 89 check).
function parseAbn(raw) {
  const digits = raw.toUpperCase().replace(/^ABN/, "").replace(/[^0-9]/g, "");
  if (!/^\d{11}$/.test(digits)) {
    return null;
  }
  const weights = [10, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19];
  let sum = 0;
  for (let i = 0; i < 11; i++) {
    const digit = Number(digits.charAt(i)) - (i === 0 ? 1 : 0);
    sum += digit * weights[i];
  }
  return sum % 89 === 0 ? digits : null;
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

// ABN Lookup answers with JSONP: callback({...}). Returns the object inside, or null.
function parseJsonp(text) {
  const content = String(text || "").trim();
  const start = content.indexOf("(");
  const end = content.lastIndexOf(")");
  if (start < 0 || end <= start) {
    return parseJson(content);
  }
  return parseJson(content.substring(start + 1, end));
}

// Calls ABN Lookup. Returns the ABN details, or null when there's no answer to store.
function lookUp(abn) {
  const apiResponse = http.send({
    url: `${ABN_LOOKUP_URL}?abn=${abn}&callback=callback&guid=${encodeURIComponent(API_KEY)}`,
    method: "GET",
    headers: [{ Key: "Accept", Value: "application/javascript" }],
  });

  const status = String(apiResponse.HttpStatus || "");
  const body = parseJsonp(apiResponse.Content);
  const message = body ? clean(body.Message) : null;

  if (status === "TooManyRequests" || status === "ServiceUnavailable") {
    throw new Error(`TooManyRequests - ABN Lookup is busy (HTTP ${status}), the record will be retried`);
  }

  // ABN Lookup reports errors in Message, with HTTP 200.
  if (message && /guid/i.test(message)) {
    throw new Error(`ABN Lookup rejected the GUID in the API Key field: ${message}`);
  }

  if (status === "OK" && body && clean(body.Abn) && !message) {
    return body;
  }

  log(`ABN Lookup could not look up ${abn}. HTTP ${status}. ${message || String(apiResponse.Content || "").substring(0, 200)}`);
  return null;
}

function run() {
  const abn = parseAbn(getValue(ABN_KEY));
  if (!abn) {
    // No valid ABN on this record (this is also what Test connection hits, because it passes
    // placeholder values instead of real ones).
    return [];
  }

  if (!clean(API_KEY)) {
    log("ABN Lookup needs a GUID. Enter your ABN Lookup GUID in the enricher's API Key field.");
    return [];
  }

  const cacheKey = `abn:${abn}`;
  const cached = CACHE_MILLISECONDS > 0 ? cache.get(cacheKey) : null;
  let details = cached ? parseJson(String(cached)) : null;

  if (!details) {
    details = lookUp(abn);
    if (!details) {
      return [];
    }
    if (CACHE_MILLISECONDS > 0) {
      cache.set(cacheKey, JSON.stringify(details), CACHE_MILLISECONDS);
    }
  }

  const businessNames = Array.isArray(details.BusinessName)
    ? details.BusinessName.map((x) => clean(x)).filter((x) => !!x)
    : [];

  const data = {
    "abn.abn": clean(details.Abn),
    "abn.status": clean(details.AbnStatus),
    "abn.statusEffectiveFrom": dateOnly(details.AbnStatusEffectiveFrom),
    "abn.acn": clean(details.Acn),
    "abn.entityName": clean(details.EntityName),
    "abn.entityType": clean(details.EntityTypeName),
    "abn.entityTypeCode": clean(details.EntityTypeCode),
    "abn.businessNames": businessNames.length > 0 ? businessNames.join("; ") : null,
    "abn.state": clean(details.AddressState),
    "abn.postcode": clean(details.AddressPostcode),
    "abn.gstRegisteredFrom": dateOnly(details.Gst),
  };

  // Leave out values ABN Lookup didn't return, so they don't overwrite existing data with blanks.
  Object.keys(data).forEach((key) => {
    if (data[key] === null) {
      delete data[key];
    }
  });

  return [{ Data: data, Score: 100 }];
}

response = JSON.stringify(run());
```
