---
layout: cluedin
title: Malta Business Registry
parent: REST API enricher samples
grand_parent: Govern & improve
nav_order: 340
permalink: /govern/rest-api-enricher-samples/mbr-malta
content_type: reference
summary: "A template for looking up Maltese companies by registration number with the Malta Business Registry's Basic Company Details API package, adding the registered name, registration date, registered address and state. V2 script; needs an MBR API subscription."
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

This example looks up an organization's Maltese company registration number with the Malta Business Registry's (MBR) **Basic Company Details** API package. For each golden record it stores the registered company name, registration date, registered address, and state.

**Enricher version:** V2  
**API key:** your MBR API subscription key (contact the MBR at `ictsupport.mbr@mbr.mt` to subscribe to an API package)

{: .important }
This script is a template. The MBR gives the endpoint URL, the authentication header, and the response format to subscribers of its API packages, and they aren't published. Before you use the script, set `MBR_URL` and `API_KEY_HEADER` at the top of the script from the documentation MBR sends you, and check the field names in `FIELDS` against it. Until `MBR_URL` and `API_KEY_HEADER` are set, the script adds nothing. The script hasn't been run against the MBR API.

To set up the enricher, see [Add REST API enricher](/govern/enrichment/rest-api#add-rest-api-enricher), then use the settings and script on this page.

## MBR API packages

The MBR offers four API packages, mainly for subject persons such as corporate service providers:

- **Company Search API** – searches by company name or registration number, and returns the name and registration number.
- **Basic Company Details API** – by registration number, returns the company name, registration number, registration date, registered address, and state. This script is written for this package.
- **Full Company Details API** – adds involvements (officers and shareholders), share capital, and a list of filed documents.
- **Bundle API** – all three.

The MBR doesn't publish prices or technical documentation for the packages. Ask the MBR for both when you subscribe.

## Settings

- **Accepted Business Domain** – `/Organization`, or the business domain that holds your companies.

- **Version** – V2 (recommended).

- **API Key** – your MBR API subscription key. The script sends it in the header named in `API_KEY_HEADER`. If the field is empty, the script adds nothing and doesn't call the MBR.

- **Filters** – we recommend a rule that only accepts golden records where `organization.registrationNumber` has a value. Otherwise, every record without a registration number is listed on the enricher's **Logs** tab as having returned no results.

## Vocabulary and Properties

```
organization.registrationNumber
```

`organization.registrationNumber` holds the MBR registration number, for example `C 12345`. If your data uses another vocabulary key, change this field and the `REGISTRATION_NUMBER_KEY` value at the top of the script.

## Request and response

**Base URL:** from MBR's API documentation, in `MBR_URL`  
**Endpoint:** `GET` the Basic Company Details URL, with the registration number in the place of `{registrationNumber}`, or at the end of the URL  
**Authentication:** your subscription key in the header named in `API_KEY_HEADER`

With `MBR_URL` set to, for example, `https://<mbr-api-host>/companies/{registrationNumber}`, the script sends one request per golden record:

```http
GET https://<mbr-api-host>/companies/C%2012345
<API_KEY_HEADER>: <your MBR subscription key>
Accept: application/json
```

Response (illustrative; MBR's real field names may differ, see `FIELDS`):

```json
{
  "registrationNumber": "C 12345",
  "companyName": "EXAMPLE HOLDINGS LIMITED",
  "registrationDate": "2010-05-12T00:00:00",
  "registeredAddress": { "line1": "1, Example Street", "locality": "Valletta", "postCode": "VLT 1000" },
  "state": "Active"
}
```

The script reads the company from the response itself, from a `data`, `result` or `company` property, or from the first item of an array.

## Properties added by the enricher

| Property | Response field (first match in `FIELDS`, ignoring case) | Example |
| -------- | -------------- | ------- |
| `mbr.registrationNumber` | `registrationNumber`, `companyRegistrationNumber`, `regNo`, or `companyNumber`; otherwise the number that was looked up | `C 12345` |
| `mbr.name` | `companyName` or `name` | `EXAMPLE HOLDINGS LIMITED` |
| `mbr.registrationDate` | `registrationDate`, `dateOfRegistration`, or `incorporationDate` | `2010-05-12` |
| `mbr.registeredAddress` | `registeredAddress`, `registeredOffice`, or `address`; an address object is joined into one line | `1, Example Street, Valletta, VLT 1000` |
| `mbr.state` | `state`, `status`, `companyState`, or `companyStatus` | `Active` |

A property is added only when the response has a value for it. To read a field with another name, add it to the list for that property in `FIELDS`.

If the enricher has a **Preview** tab, the results appear there first. To add them to golden records, go to the **Map** tab, select **Map Data**, and choose **Auto Mapping**. Select the business domain, enter a new vocabulary named `MBR` with the key prefix `mbr`, and then create the mapping. Auto mapping also uses `name` as the golden record name, so remove that from the mapping if you want to keep your existing names. Then process the data on the **Process** tab. If the enricher has no **Preview** tab, the properties are added to the golden record as soon as it is enriched.

## How the script handles input and errors

- The number is upper-cased and its spacing normalised, so `c12345` and `C-12345` are looked up as `C 12345`. A number with digits only gets the prefix in `DEFAULT_PREFIX` (`C`, for companies). Other prefixes, such as `P` (partnerships) and `OC` (overseas companies), are kept. Golden records without a valid number (a prefix of 1 to 3 letters and up to 6 digits) are skipped without calling the MBR.

- If the MBR has no company with that number, or returns an error or an answer without a company name, the script logs the reason and adds nothing.

- If the MBR rejects the key (HTTP 401 or 403), the script throws an error, so the golden record is listed on the **Logs** tab with a message to check the **API Key** field and `API_KEY_HEADER`.

- If the MBR reports that it is too busy (HTTP 429), the script throws an error that makes the enricher try the golden record again later.

- Successful results are cached for 7 days per registration number. To change this, edit `CACHE_MILLISECONDS` in the script.

## Testing the enricher

- **Test connection** checks only that the script runs. It doesn't call the MBR.

- After you set `MBR_URL` and `API_KEY_HEADER`, enrich a golden record with a known registration number and check the **Logs** tab. If the script logs that the answer has no company name, compare the response with `FIELDS`.

## Limitations

- The endpoint, header, and field names aren't published, so this script hasn't been tested against the MBR API. Treat it as a starting point.

- The MBR's public registry website (`register.mbr.mt`) refuses some cloud-hosted servers. If the API host does the same for your CluedIn servers, ask the MBR to allow their IP addresses.

- Only the Basic Company Details package is used. Officers, shareholders, and share capital need the Full Company Details package and other properties.

## Process script

```javascript
// REST API enricher (V2) - Maltese company lookup with the Malta Business Registry API
//
// TEMPLATE: the Malta Business Registry (MBR) gives the endpoint URL, the authentication header
// and the response format to subscribers of its API packages; they aren't published. Fill in
// MBR_URL and API_KEY_HEADER below from the documentation MBR sends you, and check FIELDS against
// it, before you use this script.
//
// Looks up a golden record's Maltese company registration number with the MBR "Basic Company
// Details" API package (https://mbr.mt/), and adds the result to the golden record as mbr.*
// properties:
//
//   mbr.registrationNumber  registration number, for example C 12345
//   mbr.name                registered company name
//   mbr.registrationDate    date the company was registered
//   mbr.registeredAddress   registered office address
//   mbr.state               company state, for example Active
//
// Needs an MBR API subscription key, entered in the enricher's API Key field. See README.md next
// to this file.
//
// A record gets no result (nothing is stored) when it has no valid registration number, when MBR
// has no company with that number, when the script isn't configured yet, or when the API can't
// answer. A rejected key fails the record with an error that says so.

// ---- Settings -------------------------------------------------------------------------

// Vocabulary key to read. Add the same key to the Vocabulary and Properties field.
const REGISTRATION_NUMBER_KEY = "organization.registrationNumber";

// The Basic Company Details endpoint from MBR's API documentation. {registrationNumber} is
// replaced with the URL-encoded number (for example C%2012345); without it, the number is added
// to the end of the URL.
const MBR_URL = "";

// The request header MBR's documentation says carries your key. The key itself goes in the
// enricher's API Key field.
const API_KEY_HEADER = "";

// Prefix used when a registration number has digits only. C is for companies.
const DEFAULT_PREFIX = "C";

// The enricher replaces {APIKey} with the API Key field value.
const API_KEY = "{APIKey}";

// How long to reuse an answer for the same company. 0 turns caching off.
const CACHE_MILLISECONDS = 7 * 24 * 60 * 60 * 1000;

// Response fields to read for each property. The first name found (ignoring case) is used.
// Replace them with the names in MBR's documentation if they differ.
const FIELDS = {
  "mbr.registrationNumber": ["registrationNumber", "companyRegistrationNumber", "regNo", "companyNumber"],
  "mbr.name": ["companyName", "name"],
  "mbr.registrationDate": ["registrationDate", "dateOfRegistration", "incorporationDate"],
  "mbr.registeredAddress": ["registeredAddress", "registeredOffice", "address"],
  "mbr.state": ["state", "status", "companyState", "companyStatus"],
};

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

// Accepts "C 12345", "c12345", "C-12345", "OC 1234", "P 123" and "12345" (DEFAULT_PREFIX is added).
// Returns "PREFIX DIGITS", or null when it isn't an MBR registration number.
function parseRegistrationNumber(raw) {
  const text = raw.toUpperCase().replace(/[\s.-]+/g, " ").trim();
  const match = /^([A-Z]{1,3}) ?(\d{1,6})$/.exec(text) || /^()(\d{1,6})$/.exec(text);
  if (!match) {
    return null;
  }
  const prefix = match[1] || DEFAULT_PREFIX;
  return `${prefix} ${match[2]}`;
}

function clean(value) {
  if (value === null || value === undefined || typeof value === "object") {
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

function dateText(value) {
  const text = clean(value);
  if (!text) {
    return null;
  }
  const iso = /^(\d{4}-\d{2}-\d{2})T/.exec(text);
  return iso ? iso[1] : text;
}

// The company object in the answer: the body itself, or its data/result/company property, or
// the first item of an array.
function companyOf(body) {
  let item = body;
  for (let i = 0; i < 3 && item; i++) {
    if (Array.isArray(item)) {
      item = item.length > 0 ? item[0] : null;
    } else if (typeof item === "object" && (item.data || item.result || item.company)) {
      item = item.data || item.result || item.company;
    } else {
      break;
    }
  }
  return item && typeof item === "object" && !Array.isArray(item) ? item : null;
}

function readField(company, names) {
  const keys = Object.keys(company);
  for (let i = 0; i < names.length; i++) {
    for (let j = 0; j < keys.length; j++) {
      if (keys[j].toLowerCase() === names[i].toLowerCase()) {
        const value = company[keys[j]];
        if (value && typeof value === "object" && !Array.isArray(value)) {
          // An address object: join its text values.
          const parts = Object.keys(value).map((k) => clean(value[k])).filter((x) => !!x);
          return parts.length > 0 ? parts.join(", ") : null;
        }
        return clean(value);
      }
    }
  }
  return null;
}

// Calls the MBR API. Returns the company, or null when there's no answer to store.
function lookUp(registrationNumber) {
  const encoded = encodeURIComponent(registrationNumber);
  const url = MBR_URL.indexOf("{registrationNumber}") >= 0
    ? MBR_URL.split("{registrationNumber}").join(encoded)
    : MBR_URL + encoded;

  const apiResponse = http.send({
    url: url,
    method: "GET",
    headers: [
      { Key: API_KEY_HEADER, Value: API_KEY },
      { Key: "Accept", Value: "application/json" },
      { Key: "User-Agent", Value: "CluedIn REST API enricher" },
    ],
  });

  const status = String(apiResponse.HttpStatus || "");
  const body = parseJson(apiResponse.Content);

  if (status === "TooManyRequests") {
    throw new Error("TooManyRequests - the MBR API is busy, the record will be retried");
  }

  if (status === "Unauthorized" || status === "Forbidden") {
    throw new Error(`The MBR API rejected the API key (HTTP ${status}). Check the API Key field of the enricher, and API_KEY_HEADER in the script.`);
  }

  const company = status === "OK" ? companyOf(body) : null;
  if (company && readField(company, FIELDS["mbr.name"])) {
    return company;
  }

  log(`MBR could not look up ${registrationNumber}. HTTP ${status}. ${String(apiResponse.Content || "").substring(0, 200)}`);
  return null;
}

function run() {
  const registrationNumber = parseRegistrationNumber(getValue(REGISTRATION_NUMBER_KEY));
  if (!registrationNumber) {
    // No valid registration number on this record (this is also what Test connection hits,
    // because it passes placeholder values instead of real ones).
    return [];
  }

  if (!MBR_URL || !API_KEY_HEADER) {
    log("The MBR script isn't configured. Set MBR_URL and API_KEY_HEADER from MBR's API documentation.");
    return [];
  }

  if (!API_KEY) {
    log("No MBR API key. Enter it in the API Key field of the enricher.");
    return [];
  }

  const cacheKey = `mbr:${registrationNumber}`;
  const cached = CACHE_MILLISECONDS > 0 ? cache.get(cacheKey) : null;
  let company = cached ? parseJson(String(cached)) : null;

  if (!company) {
    company = lookUp(registrationNumber);
    if (!company) {
      return [];
    }
    if (CACHE_MILLISECONDS > 0) {
      cache.set(cacheKey, JSON.stringify(company), CACHE_MILLISECONDS);
    }
  }

  const data = {};
  Object.keys(FIELDS).forEach((property) => {
    const value = readField(company, FIELDS[property]);
    if (value !== null) {
      data[property] = property === "mbr.registrationDate" ? dateText(value) : value;
    }
  });
  if (!data["mbr.registrationNumber"]) {
    data["mbr.registrationNumber"] = registrationNumber;
  }

  return [{ Data: data, Score: 100 }];
}

response = JSON.stringify(run());
```
