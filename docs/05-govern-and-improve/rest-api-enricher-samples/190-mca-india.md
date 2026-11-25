---
layout: cluedin
title: MCA company master data (India)
parent: REST API enricher samples
grand_parent: Govern & improve
nav_order: 190
permalink: /govern/rest-api-enricher-samples/mca-india
content_type: reference
summary: "Looks up Indian companies by Corporate Identification Number (CIN) in the Ministry of Corporate Affairs company master data on data.gov.in and adds the registered name, status, class, capital and registered office address. V2 script; needs a data.gov.in API key."
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

This example looks up an organization's Corporate Identification Number (CIN) in the Ministry of Corporate Affairs (MCA) company master data. The MCA publishes this data as the [Registrars of Companies (RoC)-wise Company Master Data](https://www.data.gov.in/resource/registrars-companies-roc-wise-company-master-data) resource on India's Open Government Data (OGD) platform, data.gov.in, and the script uses the platform's API to read it. For each golden record it stores the registered name, company status, class, category, Registrar of Companies, date of registration, registered office address, authorized and paid-up capital, listing status, and industrial classification.

**Enricher version:** V2  
**API key:** your data.gov.in API key

To set up the enricher, see [Add REST API enricher](/govern/enrichment/rest-api#add-rest-api-enricher), then use the settings and script on this page.

## Settings

- **Accepted Business Domain** – `/Organization`, or the business domain that holds your companies.

- **Version** – V2 (recommended).

- **API Key** – your data.gov.in API key. The script sends it as the `api-key` query parameter.

- **Filters** – we recommend a rule that only accepts golden records where `organization.cin` has a value. Otherwise, every record without a CIN is listed on the enricher's **Logs** tab as having returned no results.

## Vocabulary and Properties

```
organization.cin
```

`organization.cin` holds the company's 21-character CIN, for example `L17110MH1973PLC019786`. If your data uses another vocabulary key, change this field and the `CIN_KEY` value at the top of the script.

## Request and response

**Base URL:** `https://api.data.gov.in/resource`  
**Endpoint:** `GET /4dbe5667-7b6b-41d7-82af-211562424d9a?api-key={apiKey}&format=json&limit=1&filters[CIN]={cin}`  
**Authentication:** API key in the `api-key` query parameter. Sign up on [data.gov.in](https://data.gov.in/), and then copy the API key from your account's **My Account** page. The key is free.

`4dbe5667-7b6b-41d7-82af-211562424d9a` is the ID of the company master data resource. The script sends the square brackets in `filters[CIN]` URL-encoded, as `filters%5BCIN%5D`.

The script sends one request per golden record:

```http
GET https://api.data.gov.in/resource/4dbe5667-7b6b-41d7-82af-211562424d9a?api-key=your-data-gov-in-api-key&format=json&limit=1&filters%5BCIN%5D=L17110MH1973PLC019786
Accept: application/json
```

Shortened response:

```json
{
  "status": "ok",
  "total": 1,
  "count": 1,
  "records": [
    {
      "CIN": "L17110MH1973PLC019786",
      "CompanyName": "RELIANCE INDUSTRIES LIMITED",
      "CompanyROCcode": "RoC-Mumbai",
      "CompanyCategory": "Company limited by Shares",
      "CompanySubCategory": "Non-govt company",
      "CompanyClass": "Public",
      "AuthorizedCapital": "150000000000",
      "PaidupCapital": "135320000000",
      "CompanyRegistrationdate_date": "1973-05-08",
      "Registered_Office_Address": "3rd Floor, Maker Chambers IV, 222, Nariman Point, Mumbai, Maharashtra, 400021",
      "Listingstatus": "Listed",
      "CompanyStatus": "Active",
      "CompanyStateCode": "Maharashtra",
      "nic_code": "17110",
      "CompanyIndustrialClassification": "Manufacturing (Textiles)"
    }
  ]
}
```

This response shows the structure of a data.gov.in resource response with the field names published for the MCA company master data. The values are illustrative, not a captured response.

## Properties added by the enricher

| Property | Response field | Example |
| -------- | -------------- | ------- |
| `mca.cin` | `CIN` | `L17110MH1973PLC019786` |
| `mca.name` | `CompanyName` | `RELIANCE INDUSTRIES LIMITED` |
| `mca.status` | `CompanyStatus` | `Active` |
| `mca.class` | `CompanyClass` | `Public` |
| `mca.category` | `CompanyCategory` | `Company limited by Shares` |
| `mca.subCategory` | `CompanySubCategory` | `Non-govt company` |
| `mca.rocCode` | `CompanyROCcode` | `RoC-Mumbai` |
| `mca.registrationDate` | `CompanyRegistrationdate_date` (as `YYYY-MM-DD`) | `1973-05-08` |
| `mca.registeredOfficeAddress` | `Registered_Office_Address` | `3rd Floor, Maker Chambers IV, 222, Nariman Point, Mumbai, Maharashtra, 400021` |
| `mca.stateCode` | `CompanyStateCode` | `Maharashtra` |
| `mca.authorizedCapital` | `AuthorizedCapital` (rupees) | `150000000000` |
| `mca.paidUpCapital` | `PaidupCapital` (rupees) | `135320000000` |
| `mca.listingStatus` | `Listingstatus` | `Listed` |
| `mca.industrialClassification` | `CompanyIndustrialClassification` | `Manufacturing (Textiles)` |
| `mca.nicCode` | `nic_code` (National Industrial Classification) | `17110` |

A property is added only when the record has a value for it. Values such as `NA` or `-` are treated as empty.

The field names come from the dataset's published column list. Field names are matched without regard to case, so `cin` and `CIN` both work. If data.gov.in renames a field, change the `FIELDS` list at the top of the script; it maps each property to the field it is read from.

If the enricher has a **Preview** tab, the results appear there first. To add them to golden records, go to the **Map** tab, select **Map Data**, and choose **Auto Mapping**. Select the business domain, enter a new vocabulary named `MCA` with the key prefix `mca`, and then create the mapping. Auto mapping also uses `name` as the golden record name, so remove that from the mapping if you want to keep your existing names. Then process the data on the **Process** tab. If the enricher has no **Preview** tab, the properties are added to the golden record as soon as it is enriched.

## How the script handles input and errors

- Spaces, dots and dashes are removed and letters are capitalized, so `l17110-mh1973-plc019786` is looked up as `L17110MH1973PLC019786`. The CIN must have the 21-character CIN format: `L` (listed) or `U` (unlisted), a 5-digit industry code, a 2-letter state code, the year of incorporation, a 3-letter ownership code, and a 6-digit registration number. Golden records without a valid CIN, for example with an LLP identification number (LLPIN) or a GSTIN, are skipped without calling the API.

- Registration dates in `DD-MM-YYYY` or `DD/MM/YYYY` format are converted to `YYYY-MM-DD`.

- If the **API Key** field is empty, the script logs a message and adds nothing, without calling the API.

- If data.gov.in rejects the key (HTTP 401 or 403, or an error message about the key), the script throws an error that says so. The golden record fails, and the error is shown on the enricher's **Logs** tab.

- If the dataset has no company with that CIN, or data.gov.in returns any other error, the script logs the reason and adds nothing. The answer isn't cached, so the next record with that CIN tries again.

- If data.gov.in reports that the rate limit has been reached (HTTP 429), the script throws an error that makes the enricher try the golden record again later.

- Successful results are cached for 24 hours per CIN. To change this, edit `CACHE_MILLISECONDS` in the script.

## Testing the enricher

- **Test connection** checks only that the script runs. It doesn't call data.gov.in, so it doesn't check the key either.

- To try the setup, create a golden record with `organization.cin` set to `L17110MH1973PLC019786` (Reliance Industries Limited).

## Limitations

- The data is the MCA master data as published on data.gov.in, which is updated periodically. It can be behind the MCA's own records. For current filings, directors and charges, use the MCA portal or a commercial provider.

- Limited liability partnerships (LLPs) aren't covered: their LLPIN isn't a CIN.

- data.gov.in blocks some networks, including some cloud hosting providers. If every request fails with a connection error, check that your CluedIn environment can reach `api.data.gov.in`.

## Process script

```javascript
// REST API enricher (V2) - Indian company lookup with MCA company master data
//
// Looks up a golden record's Corporate Identification Number (CIN) in the Ministry of Corporate
// Affairs (MCA) company master data, published as the "Registrars of Companies (RoC)-wise
// Company Master Data" resource on India's Open Government Data platform (https://data.gov.in/),
// and adds the result to the golden record as mca.* properties:
//
//   mca.cin                      21-character CIN that was looked up
//   mca.name                     registered company name
//   mca.status                   company status, for example ACTIVE or STRIKE OFF
//   mca.class                    company class, for example Private or Public
//   mca.category                 company category, for example Company limited by Shares
//   mca.subCategory              company subcategory, for example Non-govt company
//   mca.rocCode                  Registrar of Companies, for example RoC-Mumbai
//   mca.registrationDate         date of registration (YYYY-MM-DD)
//   mca.registeredOfficeAddress  registered office address
//   mca.stateCode                state of the registered office
//   mca.authorizedCapital        authorized capital in rupees
//   mca.paidUpCapital            paid-up capital in rupees
//   mca.listingStatus            listing status, for example Listed or Unlisted
//   mca.industrialClassification industrial activity (NIC description)
//   mca.nicCode                  NIC industry code
//
// Needs a data.gov.in API key in the enricher's API Key field. See README.md next to this
// file for the enricher settings.
//
// A record gets no result (nothing is stored) when it has no valid CIN, when the dataset has
// no company with that CIN, or when the API can't answer. A missing or rejected API key fails
// the record with an error that says so.

// ---- Settings -------------------------------------------------------------------------

// Vocabulary key to read. Add the same key to the Vocabulary and Properties field.
const CIN_KEY = "organization.cin";

// data.gov.in resource for the MCA company master data.
const MCA_URL = "https://api.data.gov.in/resource/4dbe5667-7b6b-41d7-82af-211562424d9a";

// The enricher replaces the token below with the value of the API Key field.
const API_KEY = "{APIKey}";

// How long to reuse an answer for the same CIN. 0 turns caching off.
const CACHE_MILLISECONDS = 24 * 60 * 60 * 1000;

// Which dataset field each property comes from. Field names are matched without regard to
// case. If data.gov.in renames a field, change it here.
const CIN_FIELD = "CIN";
const FIELDS = {
  "mca.cin": "CIN",
  "mca.name": "CompanyName",
  "mca.status": "CompanyStatus",
  "mca.class": "CompanyClass",
  "mca.category": "CompanyCategory",
  "mca.subCategory": "CompanySubCategory",
  "mca.rocCode": "CompanyROCcode",
  "mca.registrationDate": "CompanyRegistrationdate_date",
  "mca.registeredOfficeAddress": "Registered_Office_Address",
  "mca.stateCode": "CompanyStateCode",
  "mca.authorizedCapital": "AuthorizedCapital",
  "mca.paidUpCapital": "PaidupCapital",
  "mca.listingStatus": "Listingstatus",
  "mca.industrialClassification": "CompanyIndustrialClassification",
  "mca.nicCode": "nic_code",
};
const DATE_PROPERTIES = ["mca.registrationDate"];

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

// Accepts "L17110MH1973PLC019786", "l17110mh1973plc019786" and "L 17110 MH 1973 PLC 019786".
// Returns the CIN, or null when the value isn't a CIN: listing status (L or U), 5-digit
// industry code, 2-letter state, year, 3-letter ownership code and 6-digit registration number.
function parseCin(raw) {
  const cin = raw.toUpperCase().replace(/[\s\-.]/g, "");
  return /^[LU]\d{5}[A-Z]{2}\d{4}[A-Z]{3}\d{6}$/.test(cin) ? cin : null;
}

// The dataset uses "NA", "-" and similar for values it doesn't have.
function clean(value) {
  if (value === null || value === undefined) {
    return null;
  }
  const text = String(value).replace(/\s+/g, " ").trim();
  return text === "" || /^(-+|NA|N\/A|NULL|NIL)$/i.test(text) ? null : text;
}

function parseJson(text) {
  try {
    return JSON.parse(text);
  } catch (e) {
    return null;
  }
}

// Reads a field from a record without regard to the case of the field name.
function field(record, name) {
  if (Object.prototype.hasOwnProperty.call(record, name)) {
    return record[name];
  }
  const lower = name.toLowerCase();
  const keys = Object.keys(record);
  for (let i = 0; i < keys.length; i++) {
    if (keys[i].toLowerCase() === lower) {
      return record[keys[i]];
    }
  }
  return null;
}

// Accepts YYYY-MM-DD (with or without a time), DD-MM-YYYY and DD/MM/YYYY. Returns YYYY-MM-DD.
function toIsoDate(value) {
  const text = clean(value);
  if (!text) {
    return null;
  }
  if (/^\d{4}-\d{2}-\d{2}/.test(text)) {
    return text.substring(0, 10);
  }
  const match = /^(\d{1,2})[-\/](\d{1,2})[-\/](\d{4})$/.exec(text);
  if (match) {
    return `${match[3]}-${("0" + match[2]).slice(-2)}-${("0" + match[1]).slice(-2)}`;
  }
  return null;
}

// Calls the API. Returns the company record, or null when there's no answer to store.
function lookUp(cin) {
  const apiResponse = http.send({
    url: `${MCA_URL}?api-key=${encodeURIComponent(API_KEY)}&format=json&limit=1&filters%5B${CIN_FIELD}%5D=${cin}`,
    method: "GET",
    headers: [{ Key: "Accept", Value: "application/json" }],
  });

  const status = String(apiResponse.HttpStatus || "");
  const body = parseJson(apiResponse.Content);
  const failed = status !== "OK" || (body && (body.status === "error" || !!body.error));
  const error = body && failed ? String(body.error || body.message || "") : "";

  if (status === "TooManyRequests") {
    throw new Error("TooManyRequests - data.gov.in rate limit reached, the record will be retried");
  }

  if (status === "Unauthorized" || status === "Forbidden" || /key/i.test(error)) {
    throw new Error(`data.gov.in rejected the API key (HTTP ${status}${error ? `: ${error}` : ""}). Check the API Key field of the enricher.`);
  }

  const records = body && Array.isArray(body.records) ? body.records : [];
  if (status === "OK" && records.length > 0 && records[0]) {
    // The filter matches the CIN exactly, but check it anyway.
    const record = records[0];
    if (String(field(record, CIN_FIELD) || "").toUpperCase().trim() === cin) {
      return record;
    }
  }

  log(`MCA company master data has no company for ${cin}, or data.gov.in could not answer. HTTP ${status}. ${String(apiResponse.Content || "").substring(0, 200)}`);
  return null;
}

function run() {
  const cin = parseCin(getValue(CIN_KEY));
  if (!cin) {
    // No valid CIN on this record (this is also what Test connection hits, because it
    // passes placeholder values instead of real ones).
    return [];
  }

  if (API_KEY.trim() === "") {
    log("data.gov.in needs an API key. Enter it in the API Key field of the enricher.");
    return [];
  }

  const cacheKey = `mca:${cin}`;
  const cached = CACHE_MILLISECONDS > 0 ? cache.get(cacheKey) : null;
  let record = cached ? parseJson(String(cached)) : null;

  if (!record) {
    record = lookUp(cin);
    if (!record) {
      return [];
    }
    if (CACHE_MILLISECONDS > 0) {
      cache.set(cacheKey, JSON.stringify(record), CACHE_MILLISECONDS);
    }
  }

  const data = {};
  Object.keys(FIELDS).forEach((property) => {
    const raw = field(record, FIELDS[property]);
    const value = DATE_PROPERTIES.indexOf(property) >= 0 ? toIsoDate(raw) : clean(raw);
    // Leave out values the dataset doesn't have, so they don't overwrite existing data with blanks.
    if (value !== null) {
      data[property] = value;
    }
  });

  return [{ Data: data, Score: 100 }];
}

response = JSON.stringify(run());
```
