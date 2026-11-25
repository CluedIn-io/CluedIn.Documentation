---
layout: cluedin
title: Companies Registrar (Israel)
parent: REST API enricher samples
grand_parent: Govern & improve
nav_order: 310
permalink: /govern/rest-api-enricher-samples/companies-registrar-israel
content_type: reference
summary: "Looks up Israeli company numbers in the Companies Registrar's open data on data.gov.il and adds the registered name, type, status, purpose and address. V2 script; no API key."
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

This example looks up an Israeli company number in the companies dataset of the Israeli Corporations Authority's Companies Registrar ([מאגר חברות - רשם החברות](https://data.gov.il/dataset/ica_companies)), which the Ministry of Justice publishes on the Israel Government Data portal. It uses the portal's datastore search API. For each golden record it stores the registered Hebrew name and, when there is one, the English name, together with the type of corporation, status, purpose, date of incorporation, and registered address. No API key is needed.

**Enricher version:** V2  
**API key:** not needed

To set up the enricher, see [Add REST API enricher](/govern/enrichment/rest-api#add-rest-api-enricher), then use the settings and script on this page.

## Settings

- **Accepted Business Domain** – `/Organization`, or the business domain that holds your companies.

- **Version** – V2 (recommended).

- **API Key** – leave empty.

- **Filters** – we recommend a rule that only accepts golden records where `organization.companyNumber` has a value. Otherwise, every record without a company number is listed on the enricher's **Logs** tab as having returned no results.

## Vocabulary and Properties

```
organization.companyNumber
```

`organization.companyNumber` holds the 9-digit Israeli company number (מספר חברה), for example `520013954` or `52-001395-4`. If your data uses another vocabulary key, change this field and the `COMPANY_NUMBER_KEY` value at the top of the script.

## Request and response

**Base URL:** `https://data.gov.il/api/3/action`  
**Endpoint:** `GET /datastore_search?resource_id=f004176c-b85f-4542-8901-7b3176f9a054&limit=1&filters={"מספר חברה":<number>}`  
**Authentication:** none

The script asks for an exact match on the company number column. The `filters` value is URL-encoded:

```http
GET https://data.gov.il/api/3/action/datastore_search?resource_id=f004176c-b85f-4542-8901-7b3176f9a054&limit=1&filters=%7B%22%D7%9E%D7%A1%D7%A4%D7%A8%20%D7%97%D7%91%D7%A8%D7%94%22%3A520013954%7D
Accept: application/json
```

Shortened response. The column names and most values are in Hebrew, and the dataset writes a quote mark inside a name as `~`:

```json
{
  "success": true,
  "result": {
    "resource_id": "f004176c-b85f-4542-8901-7b3176f9a054",
    "records": [
      {
        "_id": 494599,
        "מספר חברה": 520013954,
        "שם חברה": "טבע תעשיות פרמצבטיות בע~מ",
        "שם באנגלית": "TEVA PHARMACEUTICAL INDUSTRIES LIMITED",
        "סוג תאגיד": "ישראלית חברה ציבורית",
        "סטטוס חברה": "פעילה",
        "מטרת החברה": "לעסוק בסוגי עיסוק שפורטו בתקנון",
        "תאריך התאגדות": "13/02/1944",
        "חברה ממשלתית": "לא",
        "מגבלות": "מוגבלת",
        "שנה אחרונה של דוח שנתי (שהוגש)": 2006,
        "שם עיר": "תל אביב - יפו",
        "שם רחוב": "דבורה הנביאה",
        "מספר בית": "124",
        "מיקוד": 6944020,
        "מדינה": "ישראל"
      }
    ],
    "total": 1
  }
}
```

## Properties added by the enricher

| Property | Response field | Example |
| -------- | -------------- | ------- |
| `ilcr.companyNumber` | `מספר חברה` (company number) | `520013954` |
| `ilcr.name` | `שם חברה` (company name), with `~` changed back to `"` | `טבע תעשיות פרמצבטיות בע"מ` |
| `ilcr.nameEn` | `שם באנגלית` (English name) | `TEVA PHARMACEUTICAL INDUSTRIES LIMITED` |
| `ilcr.companyType` | `סוג תאגיד` (type of corporation) | `ישראלית חברה ציבורית` (Israeli public company) |
| `ilcr.status` | `סטטוס חברה` (company status) | `פעילה` (active) |
| `ilcr.subStatus` | `תת סטטוס` (sub-status) | |
| `ilcr.description` | `תאור חברה` (company description) | |
| `ilcr.purpose` | `מטרת החברה` (company purpose) | `לעסוק בסוגי עיסוק שפורטו בתקנון` |
| `ilcr.limitation` | `מגבלות` (limitation) | `מוגבלת` (limited) |
| `ilcr.violator` | `מפרה` (violating company) | |
| `ilcr.governmentCompany` | `חברה ממשלתית` (government company): `כן` becomes `True`, `לא` becomes `False` | `False` |
| `ilcr.incorporationDate` | `תאריך התאגדות` (date of incorporation), changed from DD/MM/YYYY | `1944-02-13` |
| `ilcr.lastAnnualReportYear` | `שנה אחרונה של דוח שנתי (שהוגש)` (last annual report filed) | `2006` |
| `ilcr.address` | `שם רחוב`, `מספר בית`, `שם עיר`, `מיקוד` (street, house number, city, postal code) on one line | `דבורה הנביאה 124, תל אביב - יפו, 6944020` |
| `ilcr.city` | `שם עיר` (city) | `תל אביב - יפו` |
| `ilcr.postalCode` | `מיקוד` (postal code) | `6944020` |
| `ilcr.country` | `מדינה` (country) | `ישראל` |

A property is added only when the dataset has a value for it. The Hebrew column names are kept together in the `FIELDS` block at the top of the script, so you can change them if the dataset renames a column.

If the enricher has a **Preview** tab, the results appear there first. To add them to golden records, go to the **Map** tab, select **Map Data**, and choose **Auto Mapping**. Select the business domain, enter a new vocabulary named `Israeli Companies Registrar` with the key prefix `ilcr`, and then create the mapping. Auto mapping also uses `name` as the golden record name, so remove that from the mapping if you want to keep your existing names. Then process the data on the **Process** tab. If the enricher has no **Preview** tab, the properties are added to the golden record as soon as it is enriched.

## How the script handles input and errors

- Spaces, dots, dashes, and slashes are removed, so `52-001395-4` is looked up as `520013954`. The number must have 9 digits, start with `5`, and have a valid check digit (the same algorithm as the Israeli ID number). Golden records without a valid number are skipped without calling the API.

- If the dataset has no company with the number, or the API returns an error, the script logs the reason and adds nothing.

- If the portal reports that it is too busy (HTTP 429 or 503), the script throws an error that makes the enricher try the golden record again later.

- Successful results are cached for 24 hours per company number. To change this, edit `CACHE_MILLISECONDS` in the script.

## Testing the enricher

- **Test connection** checks only that the script runs. It doesn't call the API.

- To try the setup, create a golden record with `organization.companyNumber` set to `520013954` (Teva Pharmaceutical Industries) or `520000118` (Bank Hapoalim).

## Limitations

- The script looks up the companies dataset only. Other registers of the Israeli Corporations Authority, such as partnerships and non-profit associations (amutot), are separate datasets.

- Names, types, statuses and addresses are in Hebrew. Many companies have no English name.

- Officers, shareholders and charges aren't in this dataset. They are available from the Companies Registrar for a fee.

- The portal updates the dataset periodically, so a very recent change might not appear yet.

## Process script

```javascript
// REST API enricher (V2) - Israeli company lookup with the Companies Registrar's open data
//
// Looks up a golden record's Israeli company number in the Israeli Corporations Authority's
// companies dataset (מאגר חברות - רשם החברות), which the Israel Government Data portal
// publishes at https://data.gov.il/dataset/ica_companies, using the portal's CKAN datastore
// search API, and adds the result to the golden record as ilcr.* properties:
//
//   ilcr.companyNumber        9-digit company number that was looked up
//   ilcr.name                 registered name (Hebrew)
//   ilcr.nameEn               registered English name, when there is one
//   ilcr.companyType          type of corporation, for example ישראלית חברה ציבורית
//   ilcr.status               company status, for example פעילה (active)
//   ilcr.subStatus            sub-status, when there is one
//   ilcr.description          company description, when there is one
//   ilcr.purpose              company purpose
//   ilcr.limitation           limitation, for example מוגבלת (limited)
//   ilcr.violator             violating company indication, when there is one
//   ilcr.governmentCompany    "True" / "False" - government company
//   ilcr.incorporationDate    date of incorporation (YYYY-MM-DD)
//   ilcr.lastAnnualReportYear last year an annual report was filed
//   ilcr.address              registered address on one line
//   ilcr.city                 city of the registered address
//   ilcr.postalCode           postal code of the registered address
//   ilcr.country              country of the registered address
//
// No API key is needed. See README.md next to this file for the enricher settings.
//
// A record gets no result (nothing is stored) when it has no valid company number, when the
// number isn't in the dataset, or when the API can't answer.

// ---- Settings -------------------------------------------------------------------------

// Vocabulary key to read. Add the same key to the Vocabulary and Properties field.
const COMPANY_NUMBER_KEY = "organization.companyNumber";

const DATASTORE_URL = "https://data.gov.il/api/3/action/datastore_search";
// "Companies" (חברות) resource of the Companies Registrar dataset on data.gov.il
const RESOURCE_ID = "f004176c-b85f-4542-8901-7b3176f9a054";

// How long to reuse an answer for the same company number. 0 turns caching off.
const CACHE_MILLISECONDS = 24 * 60 * 60 * 1000;

// Which dataset column (the column names are in Hebrew) each property comes from. If the
// dataset renames a column, change it here.
const NUMBER_FIELD = "מספר חברה";
const FIELDS = {
  "ilcr.name": "שם חברה",
  "ilcr.nameEn": "שם באנגלית",
  "ilcr.companyType": "סוג תאגיד",
  "ilcr.status": "סטטוס חברה",
  "ilcr.subStatus": "תת סטטוס",
  "ilcr.description": "תאור חברה",
  "ilcr.purpose": "מטרת החברה",
  "ilcr.limitation": "מגבלות",
  "ilcr.violator": "מפרה",
  "ilcr.lastAnnualReportYear": "שנה אחרונה של דוח שנתי (שהוגש)",
  "ilcr.city": "שם עיר",
  "ilcr.postalCode": "מיקוד",
  "ilcr.country": "מדינה",
};
const INCORPORATION_DATE_FIELD = "תאריך התאגדות";
const GOVERNMENT_COMPANY_FIELD = "חברה ממשלתית";
const STREET_FIELD = "שם רחוב";
const HOUSE_NUMBER_FIELD = "מספר בית";

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

// Accepts "52-000011-8", "520000118", "520 000 118", etc. Returns the 9 digits, or null when
// the number isn't a valid Israeli corporation number: 9 digits, starting with 5, and a valid
// check digit (the same algorithm as the Israeli ID number).
function parseCompanyNumber(raw) {
  const digits = raw.replace(/[^0-9]/g, "");
  if (!/^5\d{8}$/.test(digits) || raw.replace(/[\s.\-/]/g, "") !== digits) {
    return null;
  }
  let sum = 0;
  for (let i = 0; i < 9; i++) {
    let product = Number(digits.charAt(i)) * (i % 2 === 0 ? 1 : 2);
    if (product > 9) {
      product -= 9;
    }
    sum += product;
  }
  return sum % 10 === 0 ? digits : null;
}

// The dataset writes a quote mark inside a name as "~", for example בע~מ (בע"מ).
function clean(value) {
  if (value === null || value === undefined) {
    return null;
  }
  const text = String(value).replace(/~/g, '"').replace(/\s+/g, " ").trim();
  return text === "" ? null : text;
}

function parseJson(text) {
  try {
    return JSON.parse(text);
  } catch (e) {
    return null;
  }
}

// "15/05/1921" -> "1921-05-15"
function isoDate(value) {
  const match = /^(\d{1,2})\/(\d{1,2})\/(\d{4})$/.exec(clean(value) || "");
  if (!match) {
    return null;
  }
  const pad = (x) => (x.length === 1 ? "0" + x : x);
  return `${match[3]}-${pad(match[2])}-${pad(match[1])}`;
}

function yesNo(value) {
  const text = clean(value);
  if (text === "כן") {
    return true;
  }
  if (text === "לא") {
    return false;
  }
  return null;
}

// Calls the datastore API. Returns the company's row, or null when there's no answer to store.
function lookUp(companyNumber) {
  const filters = {};
  filters[NUMBER_FIELD] = Number(companyNumber);
  const apiResponse = http.send({
    url: `${DATASTORE_URL}?resource_id=${RESOURCE_ID}&limit=1&filters=${encodeURIComponent(JSON.stringify(filters))}`,
    method: "GET",
    headers: [{ Key: "Accept", Value: "application/json" }],
  });

  const status = String(apiResponse.HttpStatus || "");
  const body = parseJson(apiResponse.Content);

  if (status === "TooManyRequests" || status === "ServiceUnavailable") {
    throw new Error(`TooManyRequests - data.gov.il is busy (HTTP ${status}), the record will be retried`);
  }

  const records = body && body.success === true && body.result && Array.isArray(body.result.records)
    ? body.result.records
    : null;

  if (status !== "OK" || !records) {
    log(`data.gov.il could not look up company ${companyNumber}. HTTP ${status}. ${String(apiResponse.Content || "").substring(0, 200)}`);
    return null;
  }

  for (let i = 0; i < records.length; i++) {
    if (String(records[i][NUMBER_FIELD]) === companyNumber) {
      return records[i];
    }
  }

  log(`The Companies Registrar dataset has no company ${companyNumber}.`);
  return null;
}

function formatAddress(row) {
  const street = [clean(row[STREET_FIELD]), clean(row[HOUSE_NUMBER_FIELD])].filter((x) => !!x).join(" ");
  const parts = [street, clean(row[FIELDS["ilcr.city"]]), clean(row[FIELDS["ilcr.postalCode"]])].filter((x) => !!x);
  return parts.length > 0 ? parts.join(", ") : null;
}

function run() {
  const companyNumber = parseCompanyNumber(getValue(COMPANY_NUMBER_KEY));
  if (!companyNumber) {
    // No valid company number on this record (this is also what Test connection hits, because
    // it passes placeholder values instead of real ones).
    return [];
  }

  const cacheKey = `ilcr:${companyNumber}`;
  const cached = CACHE_MILLISECONDS > 0 ? cache.get(cacheKey) : null;
  let row = cached ? parseJson(String(cached)) : null;

  if (!row) {
    row = lookUp(companyNumber);
    if (!row) {
      return [];
    }
    if (CACHE_MILLISECONDS > 0) {
      cache.set(cacheKey, JSON.stringify(row), CACHE_MILLISECONDS);
    }
  }

  const data = { "ilcr.companyNumber": companyNumber };
  Object.keys(FIELDS).forEach((property) => {
    data[property] = clean(row[FIELDS[property]]);
  });
  data["ilcr.incorporationDate"] = isoDate(row[INCORPORATION_DATE_FIELD]);
  data["ilcr.governmentCompany"] = yesNo(row[GOVERNMENT_COMPANY_FIELD]);
  data["ilcr.address"] = formatAddress(row);

  // Leave out values the dataset didn't return, so they don't overwrite existing data with blanks.
  Object.keys(data).forEach((key) => {
    if (data[key] === null) {
      delete data[key];
    }
  });

  return [{ Data: data, Score: 100 }];
}

response = JSON.stringify(run());
```
