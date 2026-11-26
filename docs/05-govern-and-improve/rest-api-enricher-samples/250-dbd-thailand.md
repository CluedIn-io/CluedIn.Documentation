---
layout: cluedin
title: Open-DBD (Thailand)
parent: REST API enricher samples
grand_parent: Govern & improve
nav_order: 250
permalink: /govern/rest-api-enricher-samples/dbd-thailand
content_type: reference
summary: "Looks up Thai juristic person registration numbers in the Department of Business Development (DBD) register and adds the registered name, type, status, capital, business objective and address. V2 script; no API key."
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

This example looks up an organization's 13-digit juristic person registration number in the register of Thailand's Department of Business Development (DBD), by using the juristic person API that DBD lists on its [Open-DBD data portal](https://opendata.dbd.go.th/). For each golden record it stores the registered name in Thai and English, the type of juristic person, its status, registration date, registered and paid-up capital, business objective, and registered address. No API key is needed.

**Enricher version:** V2  
**API key:** not needed

{: .important }
DBD's API is behind a web application firewall that blocks requests from some cloud-hosted servers. When it does, the API answers HTTP 403 with an HTML page instead of data, and the script logs `DBD's firewall may be blocking this server` and adds nothing. Before you rely on this enricher, check that the server CluedIn runs on can reach `https://openapi.dbd.go.th/api/v1/juristic_person/0107544000108`. If it can't, ask DBD to allow your server's address, or call the API through a proxy that DBD allows.

To set up the enricher, see [Add REST API enricher](/govern/enrichment/rest-api#add-rest-api-enricher), then use the settings and script on this page.

## Settings

- **Accepted Business Domain** – `/Organization`, or the business domain that holds your companies.

- **Version** – V2 (recommended).

- **API Key** – leave empty.

- **Filters** – we recommend a rule that only accepts golden records where `organization.juristicId` has a value. Otherwise, every record without a juristic person number is listed on the enricher's **Logs** tab as having returned no results.

## Vocabulary and Properties

```
organization.juristicId
```

`organization.juristicId` holds the 13-digit juristic person registration number (เลขทะเบียนนิติบุคคล), which is also the company's tax ID. If your data uses another vocabulary key, change this field and the `JURISTIC_ID_KEY` value at the top of the script.

## Request and response

**Base URL:** `https://openapi.dbd.go.th/api/v1`  
**Endpoint:** `GET /juristic_person/{juristicId}`  
**Authentication:** none

The script sends one request per golden record:

```http
GET https://openapi.dbd.go.th/api/v1/juristic_person/0107544000108
Accept: application/json
User-Agent: CluedIn REST API enricher
```

Shortened response, for illustration (the server this sample was built on was blocked by DBD's firewall, so this is a response captured elsewhere, in the shape the API returns):

```json
{
  "status": { "code": "1000", "description": "Success" },
  "data": [
    {
      "cd:OrganizationJuristicPerson": {
        "cd:OrganizationJuristicID": "0107544000108",
        "cd:OrganizationJuristicNameTH": "บริษัท ปตท. จำกัด (มหาชน)",
        "cd:OrganizationJuristicNameEN": "PTT PUBLIC COMPANY LIMITED",
        "cd:OrganizationJuristicType": "บริษัทมหาชนจำกัด",
        "cd:OrganizationJuristicRegisterDate": "20011001",
        "cd:OrganizationJuristicStatus": "ยังดำเนินกิจการอยู่",
        "cd:OrganizationJuristicObjective": {
          "td:JuristicObjective": {
            "td:JuristicObjectiveCode": "71209",
            "td:JuristicObjectiveTextTH": "การทดสอบและวิเคราะห์ทางเทคนิคอื่นๆซึ่งมิได้จัดประเภท ไว้ในที่อื่น",
            "td:JuristicObjectiveTextEN": "Other technical testing and analysis, not elsewhere classified"
          }
        },
        "cd:OrganizationJuristicRegisterCapital": "28562996250.0",
        "cd:OrganizationJuristicPaidUpCapital": "28562996250.00",
        "cd:OrganizationJuristicBranchName": "สำนักงานใหญ่",
        "cd:OrganizationJuristicAddress": {
          "cr:AddressType": {
            "cd:Address": "555 ถนนวิภาวดีรังสิต ",
            "cd:CitySubDivision": { "cr:CitySubDivisionCode": "10300500", "cr:CitySubDivisionTextTH": "จตุจักร" },
            "cd:City": { "cr:CityCode": "1030", "cr:CityTextTH": "เขตจตุจักร" },
            "cd:CountrySubDivision": { "cr:CountrySubDivisionCode": "TH-10", "cr:CountrySubDivisionTextTH": "กรุงเทพมหานคร" }
          }
        }
      }
    }
  ]
}
```

`status.code` is `1000` for a result. `1004` means that no juristic person has the number.

## Properties added by the enricher

| Property | Response field | Example |
| -------- | -------------- | ------- |
| `dbd.juristicId` | `cd:OrganizationJuristicID` | `0107544000108` |
| `dbd.name` | `cd:OrganizationJuristicNameTH` | `บริษัท ปตท. จำกัด (มหาชน)` |
| `dbd.nameEn` | `cd:OrganizationJuristicNameEN` | `PTT PUBLIC COMPANY LIMITED` |
| `dbd.juristicType` | `cd:OrganizationJuristicType` (in Thai) | `บริษัทมหาชนจำกัด` (public limited company) |
| `dbd.status` | `cd:OrganizationJuristicStatus` (in Thai) | `ยังดำเนินกิจการอยู่` (still operating) |
| `dbd.registrationDate` | `cd:OrganizationJuristicRegisterDate` | `2001-10-01` |
| `dbd.registeredCapital` | `cd:OrganizationJuristicRegisterCapital` (baht) | `28562996250` |
| `dbd.paidUpCapital` | `cd:OrganizationJuristicPaidUpCapital` (baht) | `28562996250` |
| `dbd.objectiveCode` | `td:JuristicObjectiveCode` (TSIC) | `71209` |
| `dbd.objective` | `td:JuristicObjectiveTextEN`, or `td:JuristicObjectiveTextTH` when there's no English text | `Other technical testing and analysis, not elsewhere classified` |
| `dbd.branchName` | `cd:OrganizationJuristicBranchName` (in Thai) | `สำนักงานใหญ่` (head office) |
| `dbd.address` | `cd:Address`, sub-district, district and province on one line (in Thai) | `555 ถนนวิภาวดีรังสิต, จตุจักร, เขตจตุจักร, กรุงเทพมหานคร` |
| `dbd.province` | `cr:CountrySubDivisionTextTH` | `กรุงเทพมหานคร` |
| `dbd.provinceCode` | `cr:CountrySubDivisionCode` | `TH-10` |

A property is added only when DBD returns a value for it.

If the enricher has a **Preview** tab, the results appear there first. To add them to golden records, go to the **Map** tab, select **Map Data**, and choose **Auto Mapping**. Select the business domain, enter a new vocabulary named `DBD` with the key prefix `dbd`, and then create the mapping. Auto mapping also uses `name` as the golden record name, so remove that from the mapping if you want to keep your existing names. Then process the data on the **Process** tab. If the enricher has no **Preview** tab, the properties are added to the golden record as soon as it is enriched.

## How the script handles input and errors

- Spaces, dots, and dashes are removed, so `0107-544-000-108` is looked up as `0107544000108`. The number must have 13 digits and a valid check digit (the same MOD 11 check as Thai ID numbers). Golden records without a valid number are skipped without calling the API.

- If no juristic person has the number (`1004`), the request is rejected, or the API returns an error, the script logs the reason and adds nothing.

- If the answer isn't JSON (for example, DBD's firewall page), the script logs that the firewall may be blocking the server and adds nothing. The answer isn't cached, so the record is looked up again the next time it's enriched.

- Registration dates are stored as `YYYY-MM-DD` in the Common Era. A date with a Buddhist Era year (2400 or later) is converted by subtracting 543 years.

- If the API reports that it is too busy (HTTP 429), the script throws an error that makes the enricher try the golden record again later.

- Successful results are cached for 24 hours per number. To change this, edit `CACHE_MILLISECONDS` in the script.

## Testing the enricher

- **Test connection** checks only that the script runs. It doesn't call the API.

- To try the setup, create a golden record with `organization.juristicId` set to `0107544000108` (PTT Public Company Limited).

## Limitations

- DBD's firewall can block the server CluedIn runs on. See the note at the top of this page.

- Lookups by company name aren't supported. DBD offers name search only through the Digital Government Development Agency's data exchange (GDX), which needs a registered key.

- Names, types, statuses and addresses are in Thai, except `dbd.nameEn` and, usually, `dbd.objective`.

- Directors, shareholders and financial statements aren't added. They aren't part of this API.

## Process script

```javascript
// REST API enricher (V2) - Thai company lookup with the Department of Business Development
//
// Looks up a golden record's 13-digit juristic person registration number in the register
// of Thailand's Department of Business Development (DBD), using the juristic person API
// that DBD lists on its Open-DBD data portal (https://opendata.dbd.go.th/), and adds the
// result to the golden record as dbd.* properties:
//
//   dbd.juristicId          13-digit juristic person registration number that was looked up
//   dbd.name                registered name in Thai
//   dbd.nameEn              registered name in English
//   dbd.juristicType        type of juristic person (in Thai), for example บริษัทมหาชนจำกัด
//   dbd.status              status (in Thai), for example ยังดำเนินกิจการอยู่ (still operating)
//   dbd.registrationDate    date the juristic person was registered (YYYY-MM-DD)
//   dbd.registeredCapital   registered capital in baht
//   dbd.paidUpCapital       paid-up capital in baht
//   dbd.objectiveCode       business objective code (TSIC), for example 71209
//   dbd.objective           business objective in English (Thai when there's no English text)
//   dbd.branchName          branch name of the address (in Thai), for example สำนักงานใหญ่ (head office)
//   dbd.address             registered address on one line (in Thai)
//   dbd.province            province (in Thai)
//   dbd.provinceCode        province code, for example TH-10
//
// No API key is needed. See README.md next to this file for the enricher settings.
//
// A record gets no result (nothing is stored) when it has no valid juristic person number,
// when the number isn't registered, or when the API can't answer. DBD's firewall blocks some
// cloud-hosted servers; when it does, the script logs that and stores nothing.

// ---- Settings -------------------------------------------------------------------------

// Vocabulary key to read. Add the same key to the Vocabulary and Properties field.
const JURISTIC_ID_KEY = "organization.juristicId";

const DBD_URL = "https://openapi.dbd.go.th/api/v1/juristic_person/";

// Sent with every request. Some services reject requests without a User-Agent.
const USER_AGENT = "CluedIn REST API enricher";

// How long to reuse an answer for the same number. 0 turns caching off.
const CACHE_MILLISECONDS = 24 * 60 * 60 * 1000;

// ---- Script ---------------------------------------------------------------------------

// DBD answer codes (status.code in the response).
const DBD_SUCCESS = "1000";
const DBD_NO_DATA = "1004";

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

// Accepts "0107544000108", "0 1075 44000 10 8", "0107-544-000-108", etc. Returns the 13 digits,
// or null when the number isn't valid (the same MOD 11 check digit as Thai ID numbers).
function parseJuristicId(raw) {
  const digits = raw.replace(/[\s.\-]/g, "");
  if (!/^\d{13}$/.test(digits)) {
    return null;
  }
  let sum = 0;
  for (let i = 0; i < 12; i++) {
    sum += Number(digits.charAt(i)) * (13 - i);
  }
  return (11 - (sum % 11)) % 10 === Number(digits.charAt(12)) ? digits : null;
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

// DBD dates are YYYYMMDD. Years of 2400 or later are Buddhist Era years (543 years ahead).
function formatDate(value) {
  const text = clean(value);
  if (!text || !/^\d{8}$/.test(text)) {
    return null;
  }
  let year = Number(text.substring(0, 4));
  if (year >= 2400) {
    year -= 543;
  }
  const month = text.substring(4, 6);
  const day = text.substring(6, 8);
  return month === "00" || day === "00" ? null : `${year}-${month}-${day}`;
}

// DBD sends amounts as text, for example "28562996250.0".
function toAmount(value) {
  const text = clean(value);
  if (!text) {
    return null;
  }
  const amount = Number(text.replace(/,/g, ""));
  return isFinite(amount) ? amount : null;
}

function formatAddress(addressType) {
  if (!addressType) {
    return null;
  }
  const subDistrict = addressType["cd:CitySubDivision"] || {};
  const district = addressType["cd:City"] || {};
  const province = addressType["cd:CountrySubDivision"] || {};
  const parts = [
    clean(addressType["cd:Address"]),
    clean(subDistrict["cr:CitySubDivisionTextTH"]),
    clean(district["cr:CityTextTH"]),
    clean(province["cr:CountrySubDivisionTextTH"]),
  ].filter((x) => !!x);
  return parts.length > 0 ? parts.join(", ") : null;
}

// Calls the API. Returns the juristic person, or null when there's no answer to store.
function lookUp(juristicId) {
  const apiResponse = http.send({
    url: DBD_URL + juristicId,
    method: "GET",
    headers: [
      { Key: "Accept", Value: "application/json" },
      { Key: "User-Agent", Value: USER_AGENT },
    ],
  });

  const status = String(apiResponse.HttpStatus || "");
  const body = parseJson(apiResponse.Content);

  if (status === "TooManyRequests") {
    throw new Error("TooManyRequests - the DBD API is busy, the record will be retried");
  }

  if (!body) {
    // For example DBD's firewall (Incapsula), which answers 403 with an HTML page when it
    // blocks the server the enricher runs on.
    log(`DBD could not look up ${juristicId}. HTTP ${status}, and the answer wasn't JSON. DBD's firewall may be blocking this server. ${String(apiResponse.Content || "").substring(0, 120)}`);
    return null;
  }

  const code = body.status ? String(body.status.code || "") : "";
  const description = body.status ? String(body.status.description || "") : "";
  const first = Array.isArray(body.data) && body.data.length > 0 ? body.data[0] : null;
  const person = first ? first["cd:OrganizationJuristicPerson"] : null;

  if (status === "OK" && code === DBD_SUCCESS && person && person["cd:OrganizationJuristicID"]) {
    return person;
  }

  if (code === DBD_NO_DATA || status === "NotFound" || (code === DBD_SUCCESS && !person)) {
    log(`DBD has no juristic person with number ${juristicId}.`);
  } else {
    log(`DBD could not look up ${juristicId}. HTTP ${status}. ${code} ${description}`);
  }
  return null;
}

function run() {
  const juristicId = parseJuristicId(getValue(JURISTIC_ID_KEY));
  if (!juristicId) {
    // No valid juristic person number on this record (this is also what Test connection
    // hits, because it passes placeholder values instead of real ones).
    return [];
  }

  const cacheKey = `dbd:${juristicId}`;
  const cached = CACHE_MILLISECONDS > 0 ? cache.get(cacheKey) : null;
  let person = cached ? parseJson(String(cached)) : null;

  if (!person) {
    person = lookUp(juristicId);
    if (!person) {
      return [];
    }
    if (CACHE_MILLISECONDS > 0) {
      cache.set(cacheKey, JSON.stringify(person), CACHE_MILLISECONDS);
    }
  }

  const objectiveContainer = person["cd:OrganizationJuristicObjective"] || {};
  const objective = Array.isArray(objectiveContainer["td:JuristicObjective"])
    ? objectiveContainer["td:JuristicObjective"][0] || {}
    : objectiveContainer["td:JuristicObjective"] || {};
  const addressContainer = person["cd:OrganizationJuristicAddress"] || {};
  const addressType = addressContainer["cr:AddressType"] || null;
  const province = addressType ? addressType["cd:CountrySubDivision"] || {} : {};

  const data = {
    "dbd.juristicId": clean(person["cd:OrganizationJuristicID"]),
    "dbd.name": clean(person["cd:OrganizationJuristicNameTH"]),
    "dbd.nameEn": clean(person["cd:OrganizationJuristicNameEN"]),
    "dbd.juristicType": clean(person["cd:OrganizationJuristicType"]),
    "dbd.status": clean(person["cd:OrganizationJuristicStatus"]),
    "dbd.registrationDate": formatDate(person["cd:OrganizationJuristicRegisterDate"]),
    "dbd.registeredCapital": toAmount(person["cd:OrganizationJuristicRegisterCapital"]),
    "dbd.paidUpCapital": toAmount(person["cd:OrganizationJuristicPaidUpCapital"]),
    "dbd.objectiveCode": clean(objective["td:JuristicObjectiveCode"]),
    "dbd.objective": clean(objective["td:JuristicObjectiveTextEN"]) || clean(objective["td:JuristicObjectiveTextTH"]),
    "dbd.branchName": clean(person["cd:OrganizationJuristicBranchName"]),
    "dbd.address": formatAddress(addressType),
    "dbd.province": clean(province["cr:CountrySubDivisionTextTH"]),
    "dbd.provinceCode": clean(province["cr:CountrySubDivisionCode"]),
  };

  // Leave out values DBD didn't return, so they don't overwrite existing data with blanks.
  Object.keys(data).forEach((key) => {
    if (data[key] === null) {
      delete data[key];
    }
  });

  return [{ Data: data, Score: 100 }];
}

response = JSON.stringify(run());
```
