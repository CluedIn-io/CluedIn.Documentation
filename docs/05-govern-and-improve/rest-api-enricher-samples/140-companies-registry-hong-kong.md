---
layout: cluedin
title: Companies Registry (Hong Kong)
parent: REST API enricher samples
grand_parent: Govern & improve
nav_order: 140
permalink: /govern/rest-api-enricher-samples/companies-registry-hong-kong
content_type: reference
summary: "Looks up Hong Kong Business Registration numbers in the Companies Registry's open data and adds the company name, type, registered office address and incorporation date. V2 script; no API key."
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

This example looks up an organization's Hong Kong Business Registration (BR) number in the [Companies Registry's open data](https://data.gov.hk/en-data/dataset/hk-cr-crdata-list-addr), which the registry publishes as an API and updates daily. For each golden record it stores the company name, company type, registered office address, and date of incorporation. No API key is needed.

The script searches the list of live local companies first. If the number isn't there, it searches the list of registered non-Hong Kong companies (companies incorporated elsewhere with a place of business in Hong Kong), and stores their principal place of business, place of incorporation, and registration date instead.

**Enricher version:** V2  
**API key:** not needed

To set up the enricher, see [Add REST API enricher](/govern/enrichment/rest-api#add-rest-api-enricher), then use the settings and script on this page.

## Settings

- **Accepted Business Domain** – `/Organization`, or the business domain that holds your companies.

- **Version** – V2 (recommended).

- **API Key** – leave empty.

- **Filters** – we recommend a rule that only accepts golden records where `organization.brNumber` has a value. Otherwise, every record without a BR number is listed on the enricher's **Logs** tab as having returned no results.

## Vocabulary and Properties

```
organization.brNumber
```

`organization.brNumber` holds the 8-character Business Registration number. The full number printed on a BR certificate, such as `80029004-000-03-26-A`, also works: only the first 8 characters are used. If your data uses another vocabulary key, change this field and the `BR_NUMBER_KEY` value at the top of the script.

## Request and response

**Base URL:** `https://data.cr.gov.hk/cr/api/api/v1/api_builder/json`  
**Endpoints:** `GET /local/search` (live local companies) and `GET /foreign/search` (registered non-Hong Kong companies), with the query `query[0][key1]=Brn&query[0][key2]=equal&query[0][key3]={brNumber}`  
**Authentication:** none, but the request must have a `User-Agent` header. Without one, the API answers HTTP 403 Forbidden. The enricher doesn't add one by itself, so the script sends `User-Agent: CluedIn REST API enricher` (the `USER_AGENT` value at the top of the script).

The script first sends:

```http
GET https://data.cr.gov.hk/cr/api/api/v1/api_builder/json/local/search?query%5B0%5D%5Bkey1%5D=Brn&query%5B0%5D%5Bkey2%5D=equal&query%5B0%5D%5Bkey3%5D=80029004
Accept: application/json
User-Agent: CluedIn REST API enricher
```

Response for a local company:

```json
[
  {
    "Brn": "80029004",
    "Chinese_Company_Name": "NULL",
    "English_Company_Name": "CLPe eMobility Limited",
    "Address_of_Registered_Office": "CLP HEADQUARTERS, 43 SHING KAI ROAD, KAI TAK, HONG KONG",
    "Company_Type": "Private company limited by shares",
    "Date_of_Incorporation": "23-03-2026",
    "Re-domiciliation_Date": null
  }
]
```

If the number isn't a live local company, the API answers HTTP 400 with an HTML page instead of JSON, and the script sends the same query to `/foreign/search`. Response for a registered non-Hong Kong company (`75698252`):

```json
[
  {
    "Brn": "75698252",
    "Corporate_Name": "中鐵大橋勘測設計院集團有限公司",
    "Approved_name_for_carrying_on_business_in_H.K._Corporate": null,
    "Other_Corporate_Name_s": "China Railway Major Bridge Reconnaissance & Design Institute Co., Ltd.",
    "Approved_name_for_carrying_on_business_in_H.K._Other_Corporate": null,
    "Principal_Place_of_Business_in_H.K.": "RM 06, 13A/F SOUTH TOWER WORLD, FINANCE CTR HARBOUR CITY 17 CANTON RD, TST KLN, HONG KONG",
    "Place_of_Incorporation": "CHINA",
    "Company_Type": "Registered non-Hong Kong company",
    "Date_of_Registration": "12-09-2023"
  }
]
```

## Properties added by the enricher

| Property | Response field | Example |
| -------- | -------------- | ------- |
| `hkcr.brNumber` | `Brn` | `80029004` |
| `hkcr.name` | `English_Company_Name` (local companies, or `Chinese_Company_Name` if there's no English name); `Corporate_Name` (non-Hong Kong companies) | `CLPe eMobility Limited` |
| `hkcr.chineseName` | `Chinese_Company_Name` (local companies) | `中國文藝復興教育基金有限公司` |
| `hkcr.otherName` | `Other_Corporate_Name_s` (non-Hong Kong companies) | `China Railway Major Bridge Reconnaissance & Design Institute Co., Ltd.` |
| `hkcr.approvedName` | `Approved_name_for_carrying_on_business_in_H.K._Corporate` or `..._Other_Corporate` (non-Hong Kong companies) | |
| `hkcr.companyType` | `Company_Type` | `Private company limited by shares` |
| `hkcr.address` | `Address_of_Registered_Office` (local companies); `Principal_Place_of_Business_in_H.K.` (non-Hong Kong companies) | `CLP HEADQUARTERS, 43 SHING KAI ROAD, KAI TAK, HONG KONG` |
| `hkcr.incorporationDate` | `Date_of_Incorporation`, as YYYY-MM-DD (local companies) | `2026-03-23` |
| `hkcr.redomiciliationDate` | `Re-domiciliation_Date`, as YYYY-MM-DD (local companies) | |
| `hkcr.registrationDate` | `Date_of_Registration`, as YYYY-MM-DD (non-Hong Kong companies) | `2023-09-12` |
| `hkcr.placeOfIncorporation` | `Place_of_Incorporation` (non-Hong Kong companies) | `CHINA` |

A property is added only when the API returns a value for it. The API returns the text `NULL` for an empty value; the script treats it as empty.

If the enricher has a **Preview** tab, the results appear there first. To add them to golden records, go to the **Map** tab, select **Map Data**, and choose **Auto Mapping**. Select the business domain, enter a new vocabulary named `HKCR` with the key prefix `hkcr`, and then create the mapping. Auto mapping also uses `name` as the golden record name, so remove that from the mapping if you want to keep your existing names. Then process the data on the **Process** tab. If the enricher has no **Preview** tab, the properties are added to the golden record as soon as it is enriched.

## How the script handles input and errors

- Spaces are removed, letters are changed to uppercase, and anything after the first dash is ignored, so `80029004-000-03-26-A` is looked up as `80029004`. The number must be 8 digits, or a letter followed by 7 digits. Golden records without a valid BR number are skipped without calling the API.

- If the number isn't in either list, the script logs `found no company` and adds nothing. If the API returns an error (for example HTTP 403 or 500), it logs `could not look up` with the HTTP status and adds nothing. In both cases nothing is cached, so the number is looked up again the next time.

- If the API reports that it is too busy (HTTP 429), the script throws an error that makes the enricher try the golden record again later.

- Successful results are cached for 24 hours per BR number. To change this, edit `CACHE_MILLISECONDS` in the script.

- To search local companies only, set `NON_HONG_KONG_COMPANIES_URL` to `""` in the script.

## Testing the enricher

- **Test connection** checks only that the script runs. It doesn't call the API.

- To try the setup, create golden records with `organization.brNumber` set to `80029004` (a local company) and `75698252` (a registered non-Hong Kong company).

## Limitations

- The open data covers live companies only. Dissolved and deregistered companies aren't found.

- Each lookup takes several seconds, and a number that isn't a local company takes two lookups.

- The open data has no directors, shareholders, filings, or company status beyond "live". For those, use the registry's paid [e-Search services](https://www.e-services.cr.gov.hk/).

- The Companies Registry's own company number (CR number) isn't accepted; search by BR number.

## Process script

```javascript
// REST API enricher (V2) - Hong Kong company lookup with the Companies Registry
//
// Looks up a golden record's Hong Kong Business Registration (BR) number in the Companies
// Registry's open-data API (https://data.gov.hk/en-data/dataset/hk-cr-crdata-list-addr), and
// adds the result to the golden record as hkcr.* properties. It searches live local companies
// first and, if the number isn't found there, registered non-Hong Kong companies:
//
//   hkcr.brNumber              BR number that was looked up
//   hkcr.name                  English company name (local companies), or corporate name
//                              (non-Hong Kong companies)
//   hkcr.chineseName           Chinese company name (local companies)
//   hkcr.otherName             other corporate name (non-Hong Kong companies)
//   hkcr.approvedName          name approved for carrying on business in Hong Kong
//                              (non-Hong Kong companies)
//   hkcr.companyType           company type, for example Private company limited by shares
//   hkcr.address               registered office address (local companies), or principal place
//                              of business in Hong Kong (non-Hong Kong companies)
//   hkcr.incorporationDate     date of incorporation (local companies, YYYY-MM-DD)
//   hkcr.redomiciliationDate   date of re-domiciliation to Hong Kong (YYYY-MM-DD)
//   hkcr.registrationDate      date of registration (non-Hong Kong companies, YYYY-MM-DD)
//   hkcr.placeOfIncorporation  place of incorporation (non-Hong Kong companies)
//
// No API key is needed. See README.md next to this file for the enricher settings.
//
// A record gets no result (nothing is stored) when it has no valid BR number, when the number
// isn't a live company in either list, or when the API can't answer.

// ---- Settings -------------------------------------------------------------------------

// Vocabulary key to read. Add the same key to the Vocabulary and Properties field.
const BR_NUMBER_KEY = "organization.brNumber";

const LOCAL_COMPANIES_URL = "https://data.cr.gov.hk/cr/api/api/v1/api_builder/json/local/search";
// Registered non-Hong Kong companies. Set to "" to search local companies only.
const NON_HONG_KONG_COMPANIES_URL = "https://data.cr.gov.hk/cr/api/api/v1/api_builder/json/foreign/search";

// The API refuses requests without a User-Agent header (HTTP 403), and the enricher's HTTP
// client doesn't send one by default.
const USER_AGENT = "CluedIn REST API enricher";

// How long to reuse an answer for the same BR number. 0 turns caching off.
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

// Accepts "80029004", "8002 9004", and the full number printed on a BR certificate, such as
// "80029004-000-03-26-A" (only the first 8 characters identify the business). Returns the
// 8-character BR number, or null when the value doesn't look like one.
function parseBrNumber(raw) {
  const first = raw.toUpperCase().split("-")[0].replace(/[^0-9A-Z]/g, "");
  return /^[0-9A-Z]\d{7}$/.test(first) ? first : null;
}

// The API returns the text "NULL" when a value is empty.
function clean(value) {
  if (value === null || value === undefined) {
    return null;
  }
  const text = String(value).trim();
  return text === "" || text.toUpperCase() === "NULL" ? null : text;
}

function parseJson(text) {
  try {
    return JSON.parse(text);
  } catch (e) {
    return null;
  }
}

// "23-03-2026" (DD-MM-YYYY) becomes "2026-03-23".
function toIsoDate(value) {
  const match = /^(\d{2})-(\d{2})-(\d{4})$/.exec(clean(value) || "");
  return match ? `${match[3]}-${match[2]}-${match[1]}` : null;
}

// Searches one list. Returns the matching company, or null when it isn't in the list or the
// API can't answer.
function search(url, brNumber) {
  const apiResponse = http.send({
    // query[0][key1]=Brn&query[0][key2]=equal&query[0][key3]=<BR number>, with the brackets encoded
    url: `${url}?query%5B0%5D%5Bkey1%5D=Brn&query%5B0%5D%5Bkey2%5D=equal&query%5B0%5D%5Bkey3%5D=${encodeURIComponent(brNumber)}`,
    method: "GET",
    headers: [
      { Key: "Accept", Value: "application/json" },
      { Key: "User-Agent", Value: USER_AGENT },
    ],
  });

  const status = String(apiResponse.HttpStatus || "");
  const body = parseJson(apiResponse.Content);

  if (status === "TooManyRequests") {
    throw new Error("TooManyRequests - the Companies Registry API is busy, the record will be retried");
  }

  if (status === "OK" && Array.isArray(body)) {
    for (let i = 0; i < body.length; i++) {
      if (body[i] && clean(body[i].Brn) === brNumber) {
        return body[i];
      }
    }
    log(`Companies Registry found no company for BR number ${brNumber} at ${url}.`);
    return null;
  }

  // A number that isn't in the list comes back as HTTP 400 with an HTML page, not JSON.
  if (status === "BadRequest") {
    log(`Companies Registry found no company for BR number ${brNumber} at ${url}.`);
    return null;
  }

  log(`Companies Registry could not look up BR number ${brNumber} at ${url}. HTTP ${status}. ${String(apiResponse.Content || "").substring(0, 200)}`);
  return null;
}

function lookUp(brNumber) {
  const local = search(LOCAL_COMPANIES_URL, brNumber);
  if (local) {
    return { local: local };
  }
  const nonHongKong = NON_HONG_KONG_COMPANIES_URL ? search(NON_HONG_KONG_COMPANIES_URL, brNumber) : null;
  return nonHongKong ? { nonHongKong: nonHongKong } : null;
}

function run() {
  const brNumber = parseBrNumber(getValue(BR_NUMBER_KEY));
  if (!brNumber) {
    // No valid BR number on this record (this is also what Test connection hits, because it
    // passes placeholder values instead of real ones).
    return [];
  }

  const cacheKey = `hkcr:${brNumber}`;
  const cached = CACHE_MILLISECONDS > 0 ? cache.get(cacheKey) : null;
  let found = cached ? parseJson(String(cached)) : null;

  if (!found) {
    found = lookUp(brNumber);
    if (!found) {
      return [];
    }
    if (CACHE_MILLISECONDS > 0) {
      cache.set(cacheKey, JSON.stringify(found), CACHE_MILLISECONDS);
    }
  }

  let data;
  if (found.local) {
    const c = found.local;
    data = {
      "hkcr.brNumber": clean(c.Brn),
      "hkcr.name": clean(c.English_Company_Name) || clean(c.Chinese_Company_Name),
      "hkcr.chineseName": clean(c.Chinese_Company_Name),
      "hkcr.companyType": clean(c.Company_Type),
      "hkcr.address": clean(c.Address_of_Registered_Office),
      "hkcr.incorporationDate": toIsoDate(c.Date_of_Incorporation),
      "hkcr.redomiciliationDate": toIsoDate(c["Re-domiciliation_Date"]),
    };
  } else {
    const c = found.nonHongKong;
    data = {
      "hkcr.brNumber": clean(c.Brn),
      "hkcr.name": clean(c.Corporate_Name) || clean(c.Other_Corporate_Name_s),
      "hkcr.otherName": clean(c.Other_Corporate_Name_s),
      "hkcr.approvedName": clean(c["Approved_name_for_carrying_on_business_in_H.K._Corporate"])
        || clean(c["Approved_name_for_carrying_on_business_in_H.K._Other_Corporate"]),
      "hkcr.companyType": clean(c.Company_Type),
      "hkcr.address": clean(c["Principal_Place_of_Business_in_H.K."]),
      "hkcr.registrationDate": toIsoDate(c.Date_of_Registration),
      "hkcr.placeOfIncorporation": clean(c.Place_of_Incorporation),
    };
  }

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
