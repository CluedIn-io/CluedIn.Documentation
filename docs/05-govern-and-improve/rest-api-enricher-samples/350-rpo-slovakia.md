---
layout: cluedin
title: Register of Legal Entities (Slovakia)
parent: REST API enricher samples
grand_parent: Govern & improve
nav_order: 350
permalink: /govern/rest-api-enricher-samples/rpo-slovakia
content_type: reference
summary: "Looks up Slovak IČO numbers in the Statistical Office's Register of Legal Entities (RPO) API and adds the registered name, legal form, address, main activity, registration and capital. V2 script; no API key."
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

This example looks up a Slovak identification number (IČO) in the Register of Legal Entities, Entrepreneurs and Public Authorities (Register právnických osôb, RPO), which the Statistical Office of the Slovak Republic runs. It uses the public [RPO API](https://api.statistics.sk/rpo/v1/). For each golden record it stores the current registered name, legal form, legal status, address, establishment and termination dates, main economic activity, the register and file number, and the registered capital. No API key is needed.

**Enricher version:** V2  
**API key:** not needed

To set up the enricher, see [Add REST API enricher](/govern/enrichment/rest-api#add-rest-api-enricher), then use the settings and script on this page.

## Settings

- **Accepted Business Domain** – `/Organization`, or the business domain that holds your companies.

- **Version** – V2 (recommended).

- **API Key** – leave empty.

- **Filters** – we recommend a rule that only accepts golden records where `organization.ico` has a value. Otherwise, every record without an IČO is listed on the enricher's **Logs** tab as having returned no results.

## Vocabulary and Properties

```
organization.ico
```

`organization.ico` holds the 8-digit IČO, for example `31322832`. Numbers written without their leading zeros, such as `151742` for `00151742`, are also accepted. If your data uses another vocabulary key, change this field and the `ICO_KEY` value at the top of the script.

## Request and response

**Base URL:** `https://api.statistics.sk/rpo/v1`  
**Endpoints:** `GET /search?identifier={ico}`, then `GET /entity/{id}?showHistoricalData=false&showOrganizationUnits=false`  
**Authentication:** none

The script sends two requests per golden record. The search finds the entity's internal `id` from the IČO:

```http
GET https://api.statistics.sk/rpo/v1/search?identifier=31322832
Accept: application/json
```

Shortened response. The search result includes the history of names and addresses, with `validFrom` and `validTo` dates:

```json
{
  "results": [
    {
      "id": 1003617,
      "dbModificationDate": "2026-07-09",
      "identifiers": [{ "value": "31322832", "validFrom": "1992-04-29" }],
      "fullNames": [
        { "value": "SLOVNAFT a.s.", "validFrom": "1992-04-29", "validTo": "1998-11-29" },
        { "value": "SLOVNAFT , a.s.", "validFrom": "1998-11-30", "validTo": "2008-05-29" },
        { "value": "SLOVNAFT, a.s.", "validFrom": "2008-05-30" }
      ],
      "addresses": [
        { "validFrom": "2006-06-16", "street": "Vlčie hrdlo", "regNumber": 0, "buildingNumber": "1", "postalCodes": ["82412"], "municipality": { "value": "Bratislava" }, "country": { "value": "Slovenská republika", "code": "703" } }
      ],
      "establishment": "1992-05-01"
    }
  ]
}
```

The second request gets the entity's current details:

```http
GET https://api.statistics.sk/rpo/v1/entity/1003617?showHistoricalData=false&showOrganizationUnits=false
Accept: application/json
```

Shortened response:

```json
{
  "id": 1003617,
  "identifiers": [{ "value": "31322832", "validFrom": "1992-04-29" }],
  "fullNames": [{ "value": "SLOVNAFT, a.s.", "validFrom": "2008-05-30" }],
  "addresses": [
    { "validFrom": "2006-06-16", "street": "Vlčie hrdlo", "regNumber": 0, "buildingNumber": "1", "postalCodes": ["82412"], "municipality": { "value": "Bratislava" }, "country": { "value": "Slovenská republika", "code": "703" } }
  ],
  "legalForms": [{ "value": { "value": "Akciová spoločnosť", "code": "121", "codelistCode": "CL000056" }, "validFrom": "1992-04-29" }],
  "establishment": "1992-05-01",
  "equities": [{ "validFrom": "2009-04-02", "value": 684757602.8, "currency": { "value": "euro", "code": "EUR" } }],
  "sourceRegister": {
    "value": { "value": "Obchodný register", "code": "1" },
    "registrationOffices": [{ "value": "Mestský súd Bratislava III", "validFrom": "1992-04-29" }],
    "registrationNumbers": [{ "value": "Sa/426/B", "validFrom": "1992-04-29" }]
  },
  "statisticalCodes": {
    "statCodesActualization": "2026-01-01",
    "mainActivity": { "value": "Výroba rafinovaných ropných produktov a produktov z fosílnych palív", "code": "1920" }
  }
}
```

## Properties added by the enricher

| Property | Response field | Example |
| -------- | -------------- | ------- |
| `rpo.ico` | `identifiers[].value` | `31322832` |
| `rpo.name` | current `fullNames[].value` | `SLOVNAFT, a.s.` |
| `rpo.legalForm` | current `legalForms[].value.value` | `Akciová spoločnosť` |
| `rpo.legalFormCode` | current `legalForms[].value.code` | `121` |
| `rpo.legalStatus` | current `legalStatuses[].value.value`, when there is one | `Zaniknutá spoločnosť` (dissolved company) |
| `rpo.address` | current `addresses[]`: street, register and building number, postal code, and municipality on one line | `Vlčie hrdlo 1, 82412 Bratislava` |
| `rpo.municipality` | current `addresses[].municipality.value` | `Bratislava` |
| `rpo.postalCode` | current `addresses[].postalCodes[0]` | `82412` |
| `rpo.country` | current `addresses[].country.value` | `Slovenská republika` |
| `rpo.establishmentDate` | `establishment` | `1992-05-01` |
| `rpo.terminationDate` | `termination` | `2018-01-01` |
| `rpo.mainActivity` | `statisticalCodes.mainActivity.value` (SK NACE) | `Výroba rafinovaných ropných produktov a produktov z fosílnych palív` |
| `rpo.mainActivityCode` | `statisticalCodes.mainActivity.code` | `1920` |
| `rpo.sourceRegister` | `sourceRegister.value.value` | `Obchodný register` |
| `rpo.registrationOffice` | current `sourceRegister.registrationOffices[].value` | `Mestský súd Bratislava III` |
| `rpo.registrationNumber` | current `sourceRegister.registrationNumbers[].value` | `Sa/426/B` |
| `rpo.registeredCapital` | current `equities[].value` | `684757602.8` |
| `rpo.registeredCapitalCurrency` | current `equities[].currency.code` | `EUR` |

The current value of a list is the entry without a `validTo` date. For a dissolved entity, which has no current name or address, the script uses the last name and address from the search result's history. A property is added only when the register has a value for it.

If the enricher has a **Preview** tab, the results appear there first. To add them to golden records, go to the **Map** tab, select **Map Data**, and choose **Auto Mapping**. Select the business domain, enter a new vocabulary named `Slovak RPO` with the key prefix `rpo`, and then create the mapping. Auto mapping also uses `name` as the golden record name, so remove that from the mapping if you want to keep your existing names. Then process the data on the **Process** tab. If the enricher has no **Preview** tab, the properties are added to the golden record as soon as it is enriched.

## How the script handles input and errors

- Spaces and a leading `IČO:` are removed, and a number with 6 or 7 digits gets leading zeros, so `IČO: 31 322 832` is looked up as `31322832`. The IČO must have a valid check digit (modulus 11). Golden records without a valid IČO are skipped without calling the API.

- If the register has no entity with the IČO, or the API returns an error, the script logs the reason and adds nothing.

- If the API reports that it is too busy (HTTP 429 or 503), the script throws an error that makes the enricher try the golden record again later.

- Successful results are cached for 24 hours per IČO. Only the properties are cached, not the API responses. To change this, edit `CACHE_MILLISECONDS` in the script.

## Testing the enricher

- **Test connection** checks only that the script runs. It doesn't call the API.

- To try the setup, create a golden record with `organization.ico` set to `31322832` (Slovnaft). `44354258` returns a company dissolved by merger in 2018, with `rpo.legalStatus` = `Zaniknutá spoločnosť` and a termination date.

## Limitations

- Names, legal forms, statuses and activities are in Slovak.

- The script adds the main details only. The entity endpoint also returns statutory bodies, stakeholders, business activities, predecessors and successors, which you can add to the script if you need them.

- The data is published by the Statistical Office under the CC BY 4.0 licence. Credit the Statistical Office of the Slovak Republic as the source when you reuse it.

## Process script

```javascript
// REST API enricher (V2) - Slovak company lookup with the Register of Legal Entities (RPO)
//
// Looks up a golden record's Slovak identification number (IČO) in the Register of Legal
// Entities, Entrepreneurs and Public Authorities (Register právnických osôb, RPO) that the
// Statistical Office of the Slovak Republic runs, using its public RPO API
// (https://api.statistics.sk/rpo/v1/), and adds the result to the golden record as rpo.*
// properties:
//
//   rpo.ico                     8-digit IČO that was looked up
//   rpo.name                    current registered name (the last one, for a dissolved entity)
//   rpo.legalForm               legal form, for example Akciová spoločnosť
//   rpo.legalFormCode           legal form code, for example 121
//   rpo.legalStatus             legal status, when there is one, for example Zaniknutá spoločnosť
//   rpo.address                 registered address on one line
//   rpo.municipality            municipality of the registered address
//   rpo.postalCode              postal code of the registered address
//   rpo.country                 country of the registered address
//   rpo.establishmentDate       date the entity was established (YYYY-MM-DD)
//   rpo.terminationDate         date the entity ceased to exist (YYYY-MM-DD)
//   rpo.mainActivity            main economic activity (SK NACE)
//   rpo.mainActivityCode        main economic activity code
//   rpo.sourceRegister          register the entity is in, for example Obchodný register
//   rpo.registrationOffice      registration office, for example Mestský súd Bratislava III
//   rpo.registrationNumber      file number at the registration office, for example Sa/426/B
//   rpo.registeredCapital       registered capital
//   rpo.registeredCapitalCurrency currency of the registered capital, for example EUR
//
// No API key is needed. See README.md next to this file for the enricher settings.
//
// A record gets no result (nothing is stored) when it has no valid IČO, when the IČO isn't in
// the register, or when the API can't answer.

// ---- Settings -------------------------------------------------------------------------

// Vocabulary key to read. Add the same key to the Vocabulary and Properties field.
const ICO_KEY = "organization.ico";

const RPO_URL = "https://api.statistics.sk/rpo/v1";

// How long to reuse an answer for the same IČO. 0 turns caching off.
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

// Accepts "31322832", "31 322 832", "IČO: 31 322 832" and shorter numbers written without
// their leading zeros ("683 025" -> "00683025"). Returns the 8 digits, or null when the value
// isn't a valid IČO (modulus 11 check digit).
function parseIco(raw) {
  const text = raw.toUpperCase().replace(/^(IČO|ICO)\s*:?\s*/, "");
  if (!/^[0-9\s]+$/.test(text)) {
    return null;
  }
  let digits = text.replace(/\s/g, "");
  if (digits.length < 6 || digits.length > 8) {
    return null;
  }
  while (digits.length < 8) {
    digits = "0" + digits;
  }
  let sum = 0;
  for (let i = 0; i < 7; i++) {
    sum += Number(digits.charAt(i)) * (8 - i);
  }
  const checkDigit = (11 - (sum % 11)) % 10;
  return checkDigit === Number(digits.charAt(7)) ? digits : null;
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

// The current entry of a history list: one without validTo, otherwise the one that started
// last (for example the last name of a dissolved entity).
function current(list) {
  const items = Array.isArray(list) ? list : [];
  let best = null;
  for (let i = 0; i < items.length; i++) {
    const item = items[i];
    if (!item) {
      continue;
    }
    if (!item.validTo) {
      return item;
    }
    if (!best || String(item.validFrom || "") > String(best.validFrom || "")) {
      best = item;
    }
  }
  return best;
}

function codelistValue(entry) {
  return entry && entry.value ? clean(entry.value.value) : null;
}

function codelistCode(entry) {
  return entry && entry.value ? clean(entry.value.code) : null;
}

function formatAddress(address) {
  if (!address) {
    return null;
  }
  const regNumber = address.regNumber ? String(address.regNumber) : "";
  const buildingNumber = clean(address.buildingNumber) || "";
  const number = regNumber && buildingNumber ? `${regNumber}/${buildingNumber}` : regNumber || buildingNumber;
  const street = [clean(address.street), number].filter((x) => !!x).join(" ");
  const postalCode = Array.isArray(address.postalCodes) ? clean(address.postalCodes[0]) : null;
  const town = [postalCode, address.municipality ? clean(address.municipality.value) : null].filter((x) => !!x).join(" ");
  const parts = [street, town].filter((x) => !!x);
  return parts.length > 0 ? parts.join(", ") : null;
}

function get(url, what) {
  const apiResponse = http.send({
    url: url,
    method: "GET",
    headers: [{ Key: "Accept", Value: "application/json" }],
  });
  const status = String(apiResponse.HttpStatus || "");
  if (status === "TooManyRequests" || status === "ServiceUnavailable") {
    throw new Error(`TooManyRequests - the RPO API is busy (HTTP ${status}), the record will be retried`);
  }
  const body = parseJson(apiResponse.Content);
  if (status !== "OK" || !body) {
    log(`The RPO API could not ${what}. HTTP ${status}. ${String(apiResponse.Content || "").substring(0, 200)}`);
    return null;
  }
  return body;
}

function hasIdentifier(entity, ico) {
  const identifiers = entity && Array.isArray(entity.identifiers) ? entity.identifiers : [];
  for (let i = 0; i < identifiers.length; i++) {
    if (identifiers[i] && String(identifiers[i].value) === ico) {
      return true;
    }
  }
  return false;
}

// Finds the entity by IČO, then gets its current details. Returns the properties to store, or
// null when there's no answer to store.
function lookUp(ico) {
  const search = get(`${RPO_URL}/search?identifier=${ico}`, `search for IČO ${ico}`);
  if (!search) {
    return null;
  }
  const results = Array.isArray(search.results) ? search.results : [];
  let found = null;
  for (let i = 0; i < results.length; i++) {
    if (hasIdentifier(results[i], ico)) {
      found = results[i];
      break;
    }
  }
  if (!found) {
    log(`The Register of Legal Entities has no entity with IČO ${ico}.`);
    return null;
  }

  const entity = get(`${RPO_URL}/entity/${found.id}?showHistoricalData=false&showOrganizationUnits=false`, `get entity ${found.id} (IČO ${ico})`);
  if (!entity) {
    return null;
  }

  // Without history, a dissolved entity has no current name or address: use the last ones
  // from the search result, which includes history.
  const name = current(entity.fullNames) || current(found.fullNames);
  const address = current(entity.addresses) || current(found.addresses);
  const legalForm = current(entity.legalForms);
  const legalStatus = current(entity.legalStatuses);
  const sourceRegister = entity.sourceRegister || found.sourceRegister || {};
  const office = current(sourceRegister.registrationOffices);
  const fileNumber = current(sourceRegister.registrationNumbers);
  const mainActivity = entity.statisticalCodes ? entity.statisticalCodes.mainActivity : null;
  let capital = null;
  const equities = Array.isArray(entity.equities) ? entity.equities : [];
  for (let i = 0; i < equities.length; i++) {
    if (equities[i] && typeof equities[i].value === "number" && !equities[i].validTo) {
      capital = equities[i];
      break;
    }
  }

  return {
    "rpo.ico": ico,
    "rpo.name": name ? clean(name.value) : null,
    "rpo.legalForm": codelistValue(legalForm),
    "rpo.legalFormCode": codelistCode(legalForm),
    "rpo.legalStatus": codelistValue(legalStatus),
    "rpo.address": formatAddress(address),
    "rpo.municipality": address && address.municipality ? clean(address.municipality.value) : null,
    "rpo.postalCode": address && Array.isArray(address.postalCodes) ? clean(address.postalCodes[0]) : null,
    "rpo.country": address && address.country ? clean(address.country.value) : null,
    "rpo.establishmentDate": dateOnly(entity.establishment || found.establishment),
    "rpo.terminationDate": dateOnly(entity.termination || found.termination),
    "rpo.mainActivity": mainActivity ? clean(mainActivity.value) : null,
    "rpo.mainActivityCode": mainActivity ? clean(mainActivity.code) : null,
    "rpo.sourceRegister": sourceRegister.value ? clean(sourceRegister.value.value) : null,
    "rpo.registrationOffice": office ? clean(office.value) : null,
    "rpo.registrationNumber": fileNumber ? clean(fileNumber.value) : null,
    "rpo.registeredCapital": capital ? capital.value : null,
    "rpo.registeredCapitalCurrency": capital && capital.currency ? clean(capital.currency.code) : null,
  };
}

function run() {
  const ico = parseIco(getValue(ICO_KEY));
  if (!ico) {
    // No valid IČO on this record (this is also what Test connection hits, because it passes
    // placeholder values instead of real ones).
    return [];
  }

  // Only the properties are cached, not the full API responses, which can be large.
  const cacheKey = `rpo:${ico}`;
  const cached = CACHE_MILLISECONDS > 0 ? cache.get(cacheKey) : null;
  let data = cached ? parseJson(String(cached)) : null;

  if (!data) {
    data = lookUp(ico);
    if (!data) {
      return [];
    }
    // Leave out values the register didn't return, so they don't overwrite existing data with blanks.
    Object.keys(data).forEach((key) => {
      if (data[key] === null) {
        delete data[key];
      }
    });
    if (CACHE_MILLISECONDS > 0) {
      cache.set(cacheKey, JSON.stringify(data), CACHE_MILLISECONDS);
    }
  }

  return [{ Data: data, Score: 100 }];
}

response = JSON.stringify(run());
```
