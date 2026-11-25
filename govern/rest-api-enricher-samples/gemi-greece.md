---
title: GEMI (Greece)
url: https://documentation.cluedin.net/govern/rest-api-enricher-samples/gemi-greece
content_type: reference
section: Govern & improve > REST API enricher samples
---

# GEMI (Greece)

> reference: Facts, options, APIs.

This example looks up an organization in the Greek General Commercial Registry (Γενικό Εμπορικό Μητρώο, GEMI) by using the [GEMI Open Data API](https://opendata.businessportal.gr/). It looks the company up by its GEMI number, or by its tax number (AFM) when the golden record has no GEMI number. For each golden record it stores the registered name in Greek and Latin characters, distinctive titles, status, legal form, GEMI office, address, website, email, incorporation date, and main activity (ΚΑΔ).

**Enricher version:** V2  
**API key:** your GEMI Open Data `api_key` (free; request access with the [registration form](https://opendata.businessportal.gr/register/) and wait for GEMI to approve it)

To set up the enricher, see [Add REST API enricher](https://documentation.cluedin.net/govern/enrichment/rest-api.md#add-rest-api-enricher), then use the settings and script on this page.

## Settings

- **Accepted Business Domain** – `/Organization`, or the business domain that holds your companies.

- **Version** – V2 (recommended).

- **API Key** – your GEMI Open Data `api_key`. The script sends it in the `api_key` header. If the field is empty, the script adds nothing and doesn't call GEMI.

- **Filters** – we recommend a rule that only accepts golden records where `organization.gemiNumber` or `organization.afm` has a value. Otherwise, every record without either is listed on the enricher's **Logs** tab as having returned no results.

## Vocabulary and Properties

```
organization.gemiNumber
organization.afm
```

`organization.gemiNumber` holds the GEMI number (Αριθμός ΓΕΜΗ). `organization.afm` holds the 9-digit tax number (ΑΦΜ) and is optional: it's used only when the record has no GEMI number. If your data uses other vocabulary keys, change this field and the `GEMI_NUMBER_KEY` and `AFM_KEY` values at the top of the script.

## Request and response

**Base URL:** `https://opendata-api.businessportal.gr/api/opendata/v1`  
**Endpoints:** `GET /companies/{arGemi}` (by GEMI number) and `GET /companies?afm={afm}` (search by tax number)  
**Authentication:** API key in the `api_key` request header

The API is described by its own OpenAPI (Swagger 2.0) specification at `https://opendata-api.businessportal.gr/api-docs`, and in the [technical documentation](https://opendata.businessportal.gr/techdocs/) (in Greek).

With a GEMI number, the script sends one request per golden record:

```http
GET https://opendata-api.businessportal.gr/api/opendata/v1/companies/121201000
api_key: <your GEMI api_key>
Accept: application/json
```

Shortened response. The field names come from the API's specification; the values are illustrative, because the API couldn't be called without an approved key:

```json
{
  "arGemi": 121201000,
  "afm": "094019245",
  "coNameEl": "ΟΡΓΑΝΙΣΜΟΣ ΤΗΛΕΠΙΚΟΙΝΩΝΙΩΝ ΤΗΣ ΕΛΛΑΔΟΣ Α.Ε.",
  "coNamesEn": ["HELLENIC TELECOMMUNICATIONS ORGANIZATION S.A."],
  "coTitlesEl": ["ΟΤΕ Α.Ε."],
  "municipality": { "id": 1, "descr": "ΑΜΑΡΟΥΣΙΟΥ" },
  "prefecture": { "id": 2, "descr": "ΑΤΤΙΚΗΣ" },
  "city": "ΜΑΡΟΥΣΙ",
  "street": "ΚΗΦΙΣΙΑΣ",
  "streetNumber": "99",
  "zipCode": "15124",
  "url": "www.cosmote.gr",
  "isBranch": false,
  "legalType": { "id": 3, "descr": "Ανώνυμη Εταιρεία", "descrEn": "Societe Anonyme" },
  "gemiOffice": { "id": 4, "descr": "ΕΠΙΜΕΛΗΤΗΡΙΟ ΑΘΗΝΩΝ", "descrEn": "ATHENS CHAMBER" },
  "incorporationDate": "1949-04-23",
  "status": { "id": 1, "descr": "Ενεργή", "descrEn": "Active", "isActive": true },
  "activities": [
    { "activity": { "id": "61.10.10", "descr": "Υπηρεσίες ενσύρματων τηλεπικοινωνιών" }, "type": "Κύρια" }
  ]
}
```

With only a tax number, the script calls `GET /companies?afm=094019245&resultsSize=10`. The answer has the matching companies in `searchResults`, and the script uses the one that isn't a branch (`isBranch` is `false`).

## Properties added by the enricher

| Property | Response field | Example |
| -------- | -------------- | ------- |
| `gemi.gemiNumber` | `arGemi` | `121201000` |
| `gemi.afm` | `afm` | `094019245` |
| `gemi.name` | `coNameEl` | `ΟΡΓΑΝΙΣΜΟΣ ΤΗΛΕΠΙΚΟΙΝΩΝΙΩΝ ΤΗΣ ΕΛΛΑΔΟΣ Α.Ε.` |
| `gemi.nameEn` | first of `coNamesEn` | `HELLENIC TELECOMMUNICATIONS ORGANIZATION S.A.` |
| `gemi.distinctiveTitle` | `coTitlesEl`, separated by `; ` | `ΟΤΕ Α.Ε.` |
| `gemi.status` | `status.descrEn`, or `status.descr` | `Active` |
| `gemi.active` | `status.isActive` | `True` |
| `gemi.legalForm` | `legalType.descrEn`, or `legalType.descr` | `Societe Anonyme` |
| `gemi.gemiOffice` | `gemiOffice.descrEn`, or `gemiOffice.descr` | `ATHENS CHAMBER` |
| `gemi.address` | `street`, `streetNumber`, `zipCode` and `city` on one line | `ΚΗΦΙΣΙΑΣ 99, 15124 ΜΑΡΟΥΣΙ` |
| `gemi.municipality` | `municipality.descr` | `ΑΜΑΡΟΥΣΙΟΥ` |
| `gemi.prefecture` | `prefecture.descr` | `ΑΤΤΙΚΗΣ` |
| `gemi.website` | `url` | `www.cosmote.gr` |
| `gemi.email` | `email` | `info@ote.gr` |
| `gemi.incorporationDate` | `incorporationDate` (as YYYY-MM-DD) | `1949-04-23` |
| `gemi.lastStatusChange` | `lastStatusChange` (as YYYY-MM-DD) | `2011-05-26` |
| `gemi.isBranch` | `isBranch` | `False` |
| `gemi.mainActivityCode` | `activities[].activity.id` of the current main (Κύρια) activity | `61.10.10` |
| `gemi.mainActivity` | `activities[].activity.descr` of the same activity | `Υπηρεσίες ενσύρματων τηλεπικοινωνιών` |

A property is added only when GEMI returns a value for it.

If the enricher has a **Preview** tab, the results appear there first. To add them to golden records, go to the **Map** tab, select **Map Data**, and choose **Auto Mapping**. Select the business domain, enter a new vocabulary named `GEMI` with the key prefix `gemi`, and then create the mapping. Auto mapping also uses `name` as the golden record name, so remove that from the mapping if you want to keep your existing names. Then process the data on the **Process** tab. If the enricher has no **Preview** tab, the properties are added to the golden record as soon as it is enriched.

## How the script handles input and errors

- Spaces, dots, and dashes are removed from the GEMI number, and leading zeros are dropped, so `000121201000` is looked up as `121201000`. A GEMI number must have 6 to 12 digits.

- A leading `EL` or `GR` is removed from the tax number, and a missing leading zero is added back. The AFM must have 9 digits and a valid check digit.

- Golden records without a valid GEMI number or AFM are skipped without calling the API.

- If GEMI has no company with that number (HTTP 404, or an empty search), the request is invalid, or the API returns an error or is unavailable (HTTP 503), the script logs the reason and adds nothing.

- If the API Key field is empty, the script logs a message and adds nothing. If GEMI rejects the key (HTTP 401 or 403), the script fails the golden record with an error that says the key was rejected.

- If GEMI's rate limit is reached (HTTP 429), the script throws an error that makes the enricher try the golden record again later.

- Successful results are cached for 24 hours per company. To change this, edit `CACHE_MILLISECONDS` in the script.

## Testing the enricher

- **Test connection** checks only that the script runs. It doesn't call GEMI.

- The [technical documentation](https://opendata.businessportal.gr/techdocs/) mentions a demonstration key, `api-docs-key`, for trying the API in its documentation pages. It's limited per IP address and isn't a substitute for your own key. When this sample was written, the API rejected it (HTTP 401) from the server it was tested on.

## Limitations

- Names, addresses and activities are in Greek. Status, legal form and GEMI office are in English when GEMI provides an English description.

- The script adds the company's basic details only. Persons, capital, stocks and published documents are in the same response (or the `/companies/{arGemi}/documents` endpoint), but aren't added.

- The values in the sample response above are illustrative. The field names and endpoints come from the API's specification, but the API couldn't be called with a real key while this sample was written.

## Process script

```javascript
// REST API enricher (V2) - Greek company lookup with the GEMI Open Data API
//
// Looks up a golden record's Greek General Commercial Registry (GEMI) number, or its tax number
// (AFM), with the GEMI Open Data API (https://opendata.businessportal.gr/), and adds the result
// to the golden record as gemi.* properties:
//
//   gemi.gemiNumber          GEMI number (Αριθμός ΓΕΜΗ)
//   gemi.afm                 tax number (ΑΦΜ)
//   gemi.name                registered name in Greek
//   gemi.nameEn              registered name in Latin characters
//   gemi.distinctiveTitle    distinctive title(s) in Greek
//   gemi.status              company status (in English when GEMI provides it)
//   gemi.active              "True" / "False" - whether GEMI counts the status as active
//   gemi.legalForm           legal form (in English when GEMI provides it)
//   gemi.gemiOffice          GEMI office that keeps the record
//   gemi.address             street, number, postcode and city on one line
//   gemi.municipality        municipality
//   gemi.prefecture          prefecture
//   gemi.website             website
//   gemi.email               email
//   gemi.incorporationDate   date of incorporation (YYYY-MM-DD)
//   gemi.lastStatusChange    date of the last status change (YYYY-MM-DD)
//   gemi.isBranch            "True" when the record is a branch
//   gemi.mainActivityCode    main activity code (ΚΑΔ)
//   gemi.mainActivity        main activity description
//
// Needs a GEMI Open Data api_key, entered in the enricher's API Key field. See README.md next to
// this file for the enricher settings.
//
// A record gets no result (nothing is stored) when it has no valid GEMI number or AFM, when GEMI
// has no company with it, or when the API can't answer. A missing or rejected key fails the
// record with an error that says so.

// ---- Settings -------------------------------------------------------------------------

// Vocabulary keys to read. Add the same keys to the Vocabulary and Properties field.
const GEMI_NUMBER_KEY = "organization.gemiNumber";
// Optional. Used only when the record has no GEMI number.
const AFM_KEY = "organization.afm";

const GEMI_URL = "https://opendata-api.businessportal.gr/api/opendata/v1/companies";

// The {APIKey} placeholder is replaced with the API Key field value (your GEMI api_key).
const API_KEY = "{APIKey}";

// How long to reuse an answer for the same company. 0 turns caching off.
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

// Accepts "000121201000", "121201000", "121 201 000". Returns the number without leading zeros
// (the API takes it as an integer), or null when it isn't a GEMI number.
function parseGemiNumber(raw) {
  if (/[A-Za-z]/.test(raw)) {
    return null;
  }
  const digits = raw.replace(/[^0-9]/g, "");
  if (digits.length < 6 || digits.length > 12) {
    return null;
  }
  const number = digits.replace(/^0+/, "");
  return number.length >= 6 ? number : null;
}

// Accepts "094014201", "EL094014201", "GR 094 014 201" and numbers that lost their leading zero.
// Returns the 9 digits, or null when it isn't a valid AFM (check digit).
function parseAfm(raw) {
  const text = raw.toUpperCase().replace(/^(EL|GR)/, "");
  if (/[A-Z]/.test(text)) {
    return null;
  }
  let digits = text.replace(/[^0-9]/g, "");
  if (digits.length === 8) {
    digits = "0" + digits;
  }
  if (!/^\d{9}$/.test(digits) || /^0+$/.test(digits)) {
    return null;
  }
  let sum = 0;
  for (let i = 0; i < 8; i++) {
    sum += Number(digits.charAt(i)) * Math.pow(2, 8 - i);
  }
  return (sum % 11) % 10 === Number(digits.charAt(8)) ? digits : null;
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

// GEMI dates come as YYYY-MM-DD (optionally with a time) or DD/MM/YYYY. Returns YYYY-MM-DD.
function toDate(value) {
  const text = clean(value);
  if (!text) {
    return null;
  }
  if (/^\d{4}-\d{2}-\d{2}/.test(text)) {
    return text.substring(0, 10);
  }
  const match = /^(\d{1,2})\/(\d{1,2})\/(\d{4})/.exec(text);
  if (match) {
    return `${match[3]}-${("0" + match[2]).slice(-2)}-${("0" + match[1]).slice(-2)}`;
  }
  return null;
}

function joinList(list) {
  const values = (Array.isArray(list) ? list : []).map((x) => clean(x)).filter((x) => !!x);
  return values.length > 0 ? values.join("; ") : null;
}

// English description when there is one, otherwise the Greek one.
function describe(item) {
  return item ? clean(item.descrEn) || clean(item.descr) : null;
}

function mainActivity(activities) {
  const list = Array.isArray(activities) ? activities.filter((x) => x && x.activity && !clean(x.dtTo)) : [];
  for (let i = 0; i < list.length; i++) {
    if (/κύρια|κυρια|main|primary/i.test(String(list[i].type || ""))) {
      return list[i].activity;
    }
  }
  return list.length > 0 ? list[0].activity : null;
}

function formatAddress(company) {
  const street = [clean(company.street), clean(company.streetNumber)].filter((x) => !!x).join(" ");
  const town = [clean(company.zipCode), clean(company.city)].filter((x) => !!x).join(" ");
  const parts = [street, town].filter((x) => !!x);
  return parts.length > 0 ? parts.join(", ") : null;
}

// Calls the API. Returns the parsed body, or null when there's no answer to store.
function callGemi(url, description) {
  const apiResponse = http.send({
    url: url,
    method: "GET",
    headers: [
      { Key: "api_key", Value: API_KEY },
      { Key: "Accept", Value: "application/json" },
    ],
  });

  const status = String(apiResponse.HttpStatus || "");
  const body = parseJson(apiResponse.Content);

  if (status === "TooManyRequests") {
    throw new Error(`TooManyRequests - the GEMI Open Data API rate limit was reached for ${description}, the record will be retried`);
  }

  if (status === "Unauthorized" || status === "Forbidden") {
    const message = body && body.message ? body.message : String(apiResponse.Content || "").substring(0, 200);
    throw new Error(`The GEMI Open Data API rejected the api_key in the API Key field (HTTP ${status}: ${message}).`);
  }

  if (status === "OK" && body) {
    return body;
  }

  if (status === "NotFound") {
    log(`GEMI has no company for ${description}.`);
  } else {
    log(`GEMI could not look up ${description}. HTTP ${status}. ${String(apiResponse.Content || "").substring(0, 200)}`);
  }
  return null;
}

function lookUpByGemiNumber(gemiNumber) {
  const company = callGemi(`${GEMI_URL}/${gemiNumber}`, `GEMI number ${gemiNumber}`);
  return company && company.arGemi !== undefined && company.arGemi !== null ? company : null;
}

// The search can return the company and its branches; prefer the company itself.
function lookUpByAfm(afm) {
  const body = callGemi(`${GEMI_URL}?afm=${afm}&resultsSize=10`, `AFM ${afm}`);
  const results = body && Array.isArray(body.searchResults) ? body.searchResults.filter((x) => x && x.afm === afm) : [];
  if (results.length === 0) {
    if (body) {
      log(`GEMI has no company for AFM ${afm}.`);
    }
    return null;
  }
  const head = results.filter((x) => x.isBranch !== true);
  return head.length > 0 ? head[0] : results[0];
}

function run() {
  const gemiNumber = parseGemiNumber(getValue(GEMI_NUMBER_KEY));
  const afm = gemiNumber ? null : parseAfm(getValue(AFM_KEY));
  if (!gemiNumber && !afm) {
    // No valid GEMI number or AFM on this record (this is also what Test connection hits,
    // because it passes placeholder values instead of real ones).
    return [];
  }

  if (!clean(API_KEY)) {
    log("The GEMI Open Data API needs an api_key. Enter it in the enricher's API Key field.");
    return [];
  }

  const cacheKey = gemiNumber ? `gemi:${gemiNumber}` : `gemi:afm:${afm}`;
  const cached = CACHE_MILLISECONDS > 0 ? cache.get(cacheKey) : null;
  let company = cached ? parseJson(String(cached)) : null;

  if (!company) {
    company = gemiNumber ? lookUpByGemiNumber(gemiNumber) : lookUpByAfm(afm);
    if (!company) {
      return [];
    }
    if (CACHE_MILLISECONDS > 0) {
      cache.set(cacheKey, JSON.stringify(company), CACHE_MILLISECONDS);
    }
  }

  const activity = mainActivity(company.activities);
  const companyStatus = company.status || null;

  const data = {
    "gemi.gemiNumber": company.arGemi !== undefined && company.arGemi !== null ? String(company.arGemi) : null,
    "gemi.afm": clean(company.afm),
    "gemi.name": clean(company.coNameEl),
    "gemi.nameEn": Array.isArray(company.coNamesEn) && company.coNamesEn.length > 0 ? clean(company.coNamesEn[0]) : null,
    "gemi.distinctiveTitle": joinList(company.coTitlesEl),
    "gemi.status": describe(companyStatus),
    "gemi.active": companyStatus && typeof companyStatus.isActive === "boolean" ? companyStatus.isActive : null,
    "gemi.legalForm": describe(company.legalType),
    "gemi.gemiOffice": describe(company.gemiOffice),
    "gemi.address": formatAddress(company),
    "gemi.municipality": describe(company.municipality),
    "gemi.prefecture": describe(company.prefecture),
    "gemi.website": clean(company.url),
    "gemi.email": clean(company.email),
    "gemi.incorporationDate": toDate(company.incorporationDate),
    "gemi.lastStatusChange": toDate(company.lastStatusChange),
    "gemi.isBranch": typeof company.isBranch === "boolean" ? company.isBranch : null,
    "gemi.mainActivityCode": activity ? clean(activity.id) : null,
    "gemi.mainActivity": activity ? clean(activity.descr) : null,
  };

  // Leave out values GEMI didn't return, so they don't overwrite existing data with blanks.
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
