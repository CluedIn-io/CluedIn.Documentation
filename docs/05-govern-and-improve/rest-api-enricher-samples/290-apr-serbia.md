---
layout: cluedin
title: APR (Serbia)
parent: REST API enricher samples
grand_parent: Govern & improve
nav_order: 290
permalink: /govern/rest-api-enricher-samples/apr-serbia
content_type: reference
summary: "Looks up Serbian companies by registration number (matični broj) in the APR Companies Open Data API and adds the business name, status, legal form, foundation date, municipality and activity code. V2 script; no API key."
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

This example looks up an organization's Serbian registration number (matični broj) in the Register of Companies of the Business Registers Agency (Агенција за привредне регистре, APR), by using APR's [Companies Open Data API](https://data.gov.rs/sr/datasets/api-za-registar-privrednikh-drushtava/). For each golden record it stores the business name, status, legal form, foundation date, municipality of the registered seat, and registered activity code. No API key is needed.

**Enricher version:** V2  
**API key:** not needed

To set up the enricher, see [Add REST API enricher](/govern/enrichment/rest-api#add-rest-api-enricher), then use the settings and script on this page.

## How the lookup works

APR's open data API has no lookup for a single company. It returns the whole register of companies (about 130,000 companies, roughly 60 MB) in one response, and APR updates it monthly. So the script:

1. Downloads the register once, and keeps it in the enricher's cache for 24 hours (`CACHE_MILLISECONDS`). Only one download runs at a time across the cluster. Golden records that arrive during the download wait for it, or are retried by the enricher until it has finished.

2. Finds each golden record's company in the cached copy, without calling APR again.

The download usually takes 20 to 40 seconds. The enricher's HTTP calls time out after 60 seconds, so if APR is very slow the download fails and the golden record fails with an error; a later golden record starts a new download. The cached copy uses memory on the CluedIn server (around 120 MB) for as long as it's cached.

## Settings

- **Accepted Business Domain** – `/Organization`, or the business domain that holds your companies.

- **Version** – V2 (recommended).

- **API Key** – leave empty.

- **Filters** – we recommend a rule that only accepts golden records where `organization.registrationNumber` has a value. Otherwise, every record without a registration number is listed on the enricher's **Logs** tab as having returned no results.

## Vocabulary and Properties

```
organization.registrationNumber
```

`organization.registrationNumber` holds the 8-digit registration number (matični broj). If your data uses another vocabulary key, change this field and the `REGISTRATION_NUMBER_KEY` value at the top of the script.

## Request and response

**Base URL:** `https://openapi.apr.gov.rs/api/opendata`  
**Endpoint:** `GET /companies`  
**Authentication:** none

The script sends this request once per cache period, not once per golden record:

```http
GET https://openapi.apr.gov.rs/api/opendata/companies
Accept: application/json
User-Agent: CluedIn REST API enricher
```

The response has the date of the data and every company, keyed by registration number. Shortened real response:

```json
{
  "DatumPreseka": "2026-10-31",
  "Podaci": {
    "07042701": {
      "PoslovnoIme": "AKCIONARSKO DRUŠTVO INDUSTRIJA MLEKA I MLEČNIH PROIZVODA IMLEK, PADINSKA SKELA",
      "SifraOpstine": "70203",
      "NazivOpstine": "ПАЛИЛУЛА (БЕОГРАД)",
      "NazivStatus": "Активан",
      "DatumOsnivanja": "1991-03-12",
      "NazivPravneForme": "Акционарско друштво",
      "SifraDelatnosti": "1051"
    },
    "20084693": {
      "PoslovnoIme": "DRUŠTVO ZA ISTRAŽIVANJE, PROIZVODNJU, PRERADU, DISTRIBUCIJU I PROMET NAFTE ... NAFTNA INDUSTRIJA SRBIJE A.D. NOVI SAD",
      "SifraOpstine": "89010",
      "NazivOpstine": "НОВИ САД",
      "NazivStatus": "Активан",
      "DatumOsnivanja": "2005-10-01",
      "NazivPravneForme": "Акционарско друштво",
      "SifraDelatnosti": "0610"
    }
  }
}
```

## Properties added by the enricher

| Property | Response field | Example |
| -------- | -------------- | ------- |
| `apr.registrationNumber` | key of the company in `Podaci` | `07042701` |
| `apr.name` | `PoslovnoIme` | `AKCIONARSKO DRUŠTVO INDUSTRIJA MLEKA I MLEČNIH PROIZVODA IMLEK, PADINSKA SKELA` |
| `apr.status` | `NazivStatus` | `Активан` |
| `apr.legalForm` | `NazivPravneForme` | `Акционарско друштво` |
| `apr.foundationDate` | `DatumOsnivanja` | `1991-03-12` |
| `apr.municipality` | `NazivOpstine` | `ПАЛИЛУЛА (БЕОГРАД)` |
| `apr.municipalityCode` | `SifraOpstine` | `70203` |
| `apr.activityCode` | `SifraDelatnosti` | `1051` |
| `apr.dataDate` | `DatumPreseka` | `2026-10-31` |

The status is one of Активан (active), У ликвидацији (in liquidation), У стечају (in bankruptcy) and У принудној ликвидацији (in compulsory liquidation). Status, legal form and municipality are in Serbian Cyrillic, as APR publishes them.

If the enricher has a **Preview** tab, the results appear there first. To add them to golden records, go to the **Map** tab, select **Map Data**, and choose **Auto Mapping**. Select the business domain, enter a new vocabulary named `APR` with the key prefix `apr`, and then create the mapping. Auto mapping also uses `name` as the golden record name, so remove that from the mapping if you want to keep your existing names. Then process the data on the **Process** tab. If the enricher has no **Preview** tab, the properties are added to the golden record as soon as it is enriched.

## How the script handles input and errors

- Spaces, dots, and a leading `MB` are removed, and a missing leading zero is added back, so `7042701` is looked up as `07042701`. The number must have 8 digits. Golden records without a valid number are skipped without downloading the register.

- If the company isn't in the open data, the script logs this and adds nothing. The open data only has companies that are active, in liquidation or in bankruptcy, so deleted companies aren't found.

- If APR can't provide the register (an error, or an answer without company data), the golden record fails with an error that says so. Nothing is cached, so a later golden record tries again.

- If APR reports that it is too busy (HTTP 429), or another golden record's download is still running, the script throws an error that makes the enricher try the golden record again later.

## Testing the enricher

- **Test connection** checks only that the script runs. It doesn't download the register.

- To try the setup, create golden records with `organization.registrationNumber` set to `07042701` (Imlek) or `20084693` (NIS). The first one waits for the download; the second is answered from the cache.

## Limitations

- Lookups by tax number (PIB) aren't supported: the open data has no PIB.

- The data is updated monthly, so recent changes can take up to a month to appear. The date of the data is stored in `apr.dataDate`.

- APR's server sends an incomplete TLS certificate chain, so tools such as curl report `unable to get local issuer certificate`. The REST API enricher completes the chain itself and connects normally.

- The open data has only basic details. Financial statements are in a separate APR open data API (`/api/opendata/companies/financial-statements`), which also returns all companies at once.

## Process script

```javascript
// REST API enricher (V2) - Serbian company lookup with the APR Companies Open Data API
//
// Looks up a golden record's Serbian registration number (matični broj) in the Business
// Registers Agency's (APR) Register of Companies, by using APR's open data API
// (https://openapi.apr.gov.rs/api/opendata/companies), and adds the result to the golden
// record as apr.* properties:
//
//   apr.registrationNumber  8-digit registration number (matični broj)
//   apr.name                registered business name (poslovno ime)
//   apr.status              status, for example Активан (active) or У ликвидацији (in liquidation)
//   apr.legalForm           legal form
//   apr.foundationDate      date of foundation (YYYY-MM-DD)
//   apr.municipality        municipality of the registered seat
//   apr.municipalityCode    municipality code
//   apr.activityCode        registered activity code
//   apr.dataDate            date of the APR data the answer comes from (YYYY-MM-DD)
//
// No API key is needed. See README.md next to this file for the enricher settings.
//
// The API has no per-company lookup: it returns the whole register (about 130,000 companies,
// roughly 60 MB) in one response, updated monthly. The script downloads it once, keeps it in the
// enricher's cache for CACHE_MILLISECONDS, and finds each company in the cached copy. The first
// record after the cache expires waits for the download (usually 20 to 40 seconds); records that
// arrive meanwhile are retried until the download has finished.
//
// A record gets no result (nothing is stored) when it has no valid registration number or when
// the company isn't in the open data. The open data only has companies that are active, in
// liquidation or in bankruptcy.

// ---- Settings -------------------------------------------------------------------------

// Vocabulary key to read. Add the same key to the Vocabulary and Properties field.
const REGISTRATION_NUMBER_KEY = "organization.registrationNumber";

const APR_URL = "https://openapi.apr.gov.rs/api/opendata/companies";

// How long to keep the downloaded register. APR updates it monthly. Must be more than 0.
const CACHE_MILLISECONDS = 24 * 60 * 60 * 1000;

// ---- Script ---------------------------------------------------------------------------

const CACHE_KEY = "apr:companies";

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

// Accepts "07042701", "0704 2701", "MB 07042701" and numbers that lost their leading zero.
// Returns the 8 digits, or null when it isn't a registration number.
function parseRegistrationNumber(raw) {
  const text = raw.toUpperCase().replace(/^MB/, "");
  if (/[A-Z]/.test(text)) {
    return null;
  }
  const digits = text.replace(/[^0-9]/g, "");
  if (digits.length === 7) {
    return "0" + digits;
  }
  return digits.length === 8 && !/^0+$/.test(digits) ? digits : null;
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

function dateOnly(value) {
  const text = clean(value);
  return text && /^\d{4}-\d{2}-\d{2}/.test(text) ? text.substring(0, 10) : null;
}

// Downloads the whole register. Returns its text; throws when APR can't provide it.
function download() {
  const apiResponse = http.send({
    url: APR_URL,
    method: "GET",
    headers: [
      { Key: "Accept", Value: "application/json" },
      { Key: "User-Agent", Value: "CluedIn REST API enricher" },
    ],
  });

  const status = String(apiResponse.HttpStatus || "");
  const content = String(apiResponse.Content || "");
  if (status === "TooManyRequests") {
    throw new Error("TooManyRequests - APR is busy, the record will be retried");
  }
  if (status !== "OK" || content.indexOf('"Podaci"') < 0) {
    throw new Error(`APR could not provide the register of companies. HTTP ${status}. ${content.substring(0, 200)}`);
  }
  return content;
}

// Finds one company in the register's text without parsing all of it: each company is a flat
// object keyed by its registration number, for example "07042701": { "PoslovnoIme": ... }.
function findCompany(text, registrationNumber) {
  const marker = `"${registrationNumber}"`;
  let at = text.indexOf(marker);
  while (at >= 0) {
    const colon = text.indexOf(":", at + marker.length);
    const start = text.indexOf("{", at + marker.length);
    if (colon >= 0 && start > colon && text.substring(at + marker.length, colon).trim() === "" && text.substring(colon + 1, start).trim() === "") {
      // A name could contain "}", so try the next few closing braces.
      let end = text.indexOf("}", start);
      for (let attempt = 0; attempt < 5 && end >= 0; attempt++) {
        const company = parseJson(text.substring(start, end + 1));
        if (company) {
          return company;
        }
        end = text.indexOf("}", end + 1);
      }
      return null;
    }
    at = text.indexOf(marker, at + marker.length);
  }
  return null;
}

function run() {
  const registrationNumber = parseRegistrationNumber(getValue(REGISTRATION_NUMBER_KEY));
  if (!registrationNumber) {
    // No valid registration number on this record (this is also what Test connection hits,
    // because it passes placeholder values instead of real ones).
    return [];
  }

  // Only one download at a time: other records wait for it (cluster-wide lock). If the wait
  // runs out, the record is retried, by when the register is usually in the cache.
  const cached = cache.getOrSetFactory(CACHE_KEY, () => download(), CACHE_MILLISECONDS);
  if (cached === null || cached === undefined) {
    throw new Error("TooManyRequests - the APR register of companies is still downloading, the record will be retried");
  }

  const text = String(cached);
  const company = findCompany(text, registrationNumber);
  if (!company) {
    log(`APR's open data has no company with registration number ${registrationNumber}. It only has companies that are active, in liquidation or in bankruptcy.`);
    return [];
  }

  const dataDate = /"DatumPreseka"\s*:\s*"([^"]+)"/.exec(text.substring(0, 300));

  const data = {
    "apr.registrationNumber": registrationNumber,
    "apr.name": clean(company.PoslovnoIme),
    "apr.status": clean(company.NazivStatus),
    "apr.legalForm": clean(company.NazivPravneForme),
    "apr.foundationDate": dateOnly(company.DatumOsnivanja),
    "apr.municipality": clean(company.NazivOpstine),
    "apr.municipalityCode": clean(company.SifraOpstine),
    "apr.activityCode": clean(company.SifraDelatnosti),
    "apr.dataDate": dataDate ? dateOnly(dataDate[1]) : null,
  };

  // Leave out values APR didn't return, so they don't overwrite existing data with blanks.
  Object.keys(data).forEach((key) => {
    if (data[key] === null) {
      delete data[key];
    }
  });

  return [{ Data: data, Score: 100 }];
}

response = JSON.stringify(run());
```
