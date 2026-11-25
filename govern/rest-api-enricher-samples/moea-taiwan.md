---
title: Ministry of Economic Affairs (Taiwan)
url: https://documentation.cluedin.net/govern/rest-api-enricher-samples/moea-taiwan
content_type: reference
section: Govern & improve > REST API enricher samples
---

# Ministry of Economic Affairs (Taiwan)

> reference: Facts, options, APIs.

This example looks up an organization's Unified Business Number (統一編號) in the company registration data that Taiwan's Ministry of Economic Affairs (MOEA) publishes on its [GCIS open-data platform](https://data.gcis.nat.gov.tw/od/rule). For each golden record it stores the registered company name, status, representative, address, registration authority, capital, and the dates the company was set up and last changed. No API key is needed.

The values are in Traditional Chinese, as the register holds them.

**Enricher version:** V2  
**API key:** not needed

To set up the enricher, see [Add REST API enricher](https://documentation.cluedin.net/govern/enrichment/rest-api.md#add-rest-api-enricher), then use the settings and script on this page.

## Settings

- **Accepted Business Domain** – `/Organization`, or the business domain that holds your companies.

- **Version** – V2 (recommended).

- **API Key** – leave empty.

- **Filters** – we recommend a rule that only accepts golden records where `organization.unifiedBusinessNumber` has a value. Otherwise, every record without a Unified Business Number is listed on the enricher's **Logs** tab as having returned no results.

## Vocabulary and Properties

```
organization.unifiedBusinessNumber
```

`organization.unifiedBusinessNumber` holds the 8-digit Unified Business Number. If your data uses another vocabulary key, change this field and the `UNIFIED_BUSINESS_NUMBER_KEY` value at the top of the script.

## Request and response

**Base URL:** `https://data.gcis.nat.gov.tw/od/data/api`  
**Endpoint:** `GET /5F64D864-61CB-4D0D-8AD9-492047CC1EA6?$format=json&$filter=Business_Accounting_NO eq {number}&$skip=0&$top=1` (the company registration basic information dataset, 公司登記基本資料)  
**Authentication:** none

The script sends one request per golden record:

```http
GET https://data.gcis.nat.gov.tw/od/data/api/5F64D864-61CB-4D0D-8AD9-492047CC1EA6?$format=json&$filter=Business_Accounting_NO%20eq%2022099131&$skip=0&$top=1
Accept: application/json
```

Response:

```json
[
  {
    "Business_Accounting_NO": "22099131",
    "Company_Status_Desc": "核准設立",
    "Company_Name": "台灣積體電路製造股份有限公司",
    "Capital_Stock_Amount": 280500000000,
    "Paid_In_Capital_Amount": 259323700670,
    "Share_Val": 10,
    "Equity_Amt": 25932370067,
    "Responsible_Name": "魏哲家",
    "Company_Location": "新竹科學園區新竹市力行六路8號",
    "Register_Organization_Desc": "國家科學及技術委員會新竹科學園區管理局",
    "Company_Setup_Date": "0760221",
    "Change_Of_Approval_Data": "1150821",
    "Revoke_App_Date": "",
    "Case_Status": "",
    "Case_Status_Desc": "",
    "Sus_App_Date": "",
    "Sus_Beg_Date": "",
    "Sus_End_Date": ""
  }
]
```

For a number that isn't a registered company, the API answers HTTP 200 with an empty body.

## Properties added by the enricher

| Property | Response field | Example |
| -------- | -------------- | ------- |
| `moea.unifiedBusinessNumber` | `Business_Accounting_NO` | `22099131` |
| `moea.name` | `Company_Name` | `台灣積體電路製造股份有限公司` |
| `moea.status` | `Company_Status_Desc`, for example `核准設立` (approved and established) or `撤銷` (revoked) | `核准設立` |
| `moea.responsiblePerson` | `Responsible_Name` (the representative, 代表人) | `魏哲家` |
| `moea.address` | `Company_Location` | `新竹科學園區新竹市力行六路8號` |
| `moea.registrationAuthority` | `Register_Organization_Desc` | `國家科學及技術委員會新竹科學園區管理局` |
| `moea.capital` | `Capital_Stock_Amount` (TWD) | `280500000000` |
| `moea.paidInCapital` | `Paid_In_Capital_Amount` (TWD) | `259323700670` |
| `moea.setupDate` | `Company_Setup_Date`, as YYYY-MM-DD | `1987-02-21` |
| `moea.lastChangeDate` | `Change_Of_Approval_Data`, as YYYY-MM-DD | `2026-08-21` |
| `moea.revocationDate` | `Revoke_App_Date`, as YYYY-MM-DD | `1992-02-13` |
| `moea.suspensionStartDate` | `Sus_Beg_Date`, as YYYY-MM-DD | |
| `moea.suspensionEndDate` | `Sus_End_Date`, as YYYY-MM-DD | |

A property is added only when the API returns a value for it. Dates in the response use the Republic of China (Minguo) calendar as `YYYMMDD`; the script converts them, so `0760221` (year 76) becomes `1987-02-21`.

If the enricher has a **Preview** tab, the results appear there first. To add them to golden records, go to the **Map** tab, select **Map Data**, and choose **Auto Mapping**. Select the business domain, enter a new vocabulary named `MOEA` with the key prefix `moea`, and then create the mapping. Auto mapping also uses `name` as the golden record name, so remove that from the mapping if you want to keep your existing names. Then process the data on the **Process** tab. If the enricher has no **Preview** tab, the properties are added to the golden record as soon as it is enriched.

## How the script handles input and errors

- Spaces, dots, and dashes are removed, so `2209 9131` is looked up as `22099131`. The number must have 8 digits and pass the Unified Business Number check (weights 1, 2, 1, 2, 1, 2, 4, 1, modulus 5). Golden records without a valid number are skipped without calling the API.

- If the number isn't a registered company (an empty response), or the API returns an error, the script logs the reason and adds nothing.

- If the API reports that it is too busy (HTTP 429), the script throws an error that makes the enricher try the golden record again later.

- Successful results are cached for 24 hours per number. To change this, edit `CACHE_MILLISECONDS` in the script.

## Testing the enricher

- **Test connection** checks only that the script runs. It doesn't call the API.

- To try the setup, create a golden record with `organization.unifiedBusinessNumber` set to `22099131` (Taiwan Semiconductor Manufacturing Company).

## Limitations

- The dataset covers companies (公司) only. Businesses registered under the Business Registration Act (商業登記, such as sole proprietorships and partnerships) and branches of foreign companies are in other GCIS datasets and aren't found.

- Values are in Traditional Chinese. There is no English company name in this dataset.

- Directors, supervisors, and business activities aren't added. They are available from other GCIS datasets.

## Process script

```javascript
// REST API enricher (V2) - Taiwanese company lookup with the Ministry of Economic Affairs
//
// Looks up a golden record's Unified Business Number (統一編號) in the company registration
// data that the Ministry of Economic Affairs (MOEA) publishes on its GCIS open-data platform
// (https://data.gcis.nat.gov.tw/od/rule), and adds the result to the golden record as
// moea.* properties. Text values are in Traditional Chinese, as the register holds them:
//
//   moea.unifiedBusinessNumber   8-digit Unified Business Number that was looked up
//   moea.name                    registered company name
//   moea.status                  company status, for example 核准設立 (approved and established)
//   moea.responsiblePerson       name of the representative (代表人)
//   moea.address                 company location
//   moea.registrationAuthority   authority the company is registered with
//   moea.capital                 authorized capital in TWD
//   moea.paidInCapital           paid-in capital in TWD
//   moea.setupDate               date the company was established (YYYY-MM-DD)
//   moea.lastChangeDate          date of the last approved change (YYYY-MM-DD)
//   moea.revocationDate          date the company was dissolved or revoked (YYYY-MM-DD)
//   moea.suspensionStartDate     start of a suspension of business (YYYY-MM-DD)
//   moea.suspensionEndDate       end of a suspension of business (YYYY-MM-DD)
//
// No API key is needed. See README.md next to this file for the enricher settings.
//
// A record gets no result (nothing is stored) when it has no valid Unified Business Number,
// when the number isn't a registered company, or when the API can't answer.

// ---- Settings -------------------------------------------------------------------------

// Vocabulary key to read. Add the same key to the Vocabulary and Properties field.
const UNIFIED_BUSINESS_NUMBER_KEY = "organization.unifiedBusinessNumber";

// The GCIS "company registration basic information" (公司登記基本資料) dataset.
const MOEA_URL = "https://data.gcis.nat.gov.tw/od/data/api/5F64D864-61CB-4D0D-8AD9-492047CC1EA6";

// How long to reuse an answer for the same number. 0 turns caching off.
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

// Accepts "22099131", "2209 9131", etc. Returns the 8 digits, or null when the value isn't a
// valid Unified Business Number. The check uses the weights 1,2,1,2,1,2,4,1 and modulus 5
// (numbers that passed the older modulus 10 check also pass it).
function parseUnifiedBusinessNumber(raw) {
  const digits = raw.replace(/[\s.\-]/g, "");
  if (!/^\d{8}$/.test(digits)) {
    return null;
  }
  const weights = [1, 2, 1, 2, 1, 2, 4, 1];
  let sum = 0;
  for (let i = 0; i < 8; i++) {
    const product = Number(digits.charAt(i)) * weights[i];
    sum += Math.floor(product / 10) + (product % 10);
  }
  // When the 7th digit is 7, its product (28) may count as 10 or as 1.
  const valid = sum % 5 === 0 || (digits.charAt(6) === "7" && (sum + 1) % 5 === 0);
  return valid ? digits : null;
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

// Dates are in the Republic of China (Minguo) calendar as YYYMMDD: "0760221" is 21 February
// of year 76, which is 1987 (76 + 1911).
function rocToIsoDate(value) {
  const match = /^(\d{2,3})(\d{2})(\d{2})$/.exec(clean(value) || "");
  if (!match) {
    return null;
  }
  return `${Number(match[1]) + 1911}-${match[2]}-${match[3]}`;
}

// Calls the API. Returns the company, or null when there's no answer to store.
function lookUp(unifiedBusinessNumber) {
  const filter = `Business_Accounting_NO eq ${unifiedBusinessNumber}`;
  const apiResponse = http.send({
    url: `${MOEA_URL}?$format=json&$filter=${encodeURIComponent(filter)}&$skip=0&$top=1`,
    method: "GET",
    headers: [{ Key: "Accept", Value: "application/json" }],
  });

  const status = String(apiResponse.HttpStatus || "");
  const body = parseJson(apiResponse.Content);

  if (status === "TooManyRequests") {
    throw new Error("TooManyRequests - the MOEA open-data API is busy, the record will be retried");
  }

  if (status === "OK" && Array.isArray(body)) {
    for (let i = 0; i < body.length; i++) {
      if (body[i] && clean(body[i].Business_Accounting_NO) === unifiedBusinessNumber) {
        return body[i];
      }
    }
  }

  // A number that isn't a registered company comes back as OK with an empty body.
  log(`MOEA found no company with Unified Business Number ${unifiedBusinessNumber}. HTTP ${status}. ${String(apiResponse.Content || "").substring(0, 200)}`);
  return null;
}

function run() {
  const unifiedBusinessNumber = parseUnifiedBusinessNumber(getValue(UNIFIED_BUSINESS_NUMBER_KEY));
  if (!unifiedBusinessNumber) {
    // No valid number on this record (this is also what Test connection hits, because it
    // passes placeholder values instead of real ones).
    return [];
  }

  const cacheKey = `moea:${unifiedBusinessNumber}`;
  const cached = CACHE_MILLISECONDS > 0 ? cache.get(cacheKey) : null;
  let company = cached ? parseJson(String(cached)) : null;

  if (!company) {
    company = lookUp(unifiedBusinessNumber);
    if (!company) {
      return [];
    }
    if (CACHE_MILLISECONDS > 0) {
      cache.set(cacheKey, JSON.stringify(company), CACHE_MILLISECONDS);
    }
  }

  const data = {
    "moea.unifiedBusinessNumber": clean(company.Business_Accounting_NO),
    "moea.name": clean(company.Company_Name),
    "moea.status": clean(company.Company_Status_Desc),
    "moea.responsiblePerson": clean(company.Responsible_Name),
    "moea.address": clean(company.Company_Location),
    "moea.registrationAuthority": clean(company.Register_Organization_Desc),
    "moea.capital": typeof company.Capital_Stock_Amount === "number" ? company.Capital_Stock_Amount : null,
    "moea.paidInCapital": typeof company.Paid_In_Capital_Amount === "number" ? company.Paid_In_Capital_Amount : null,
    "moea.setupDate": rocToIsoDate(company.Company_Setup_Date),
    "moea.lastChangeDate": rocToIsoDate(company.Change_Of_Approval_Data),
    "moea.revocationDate": rocToIsoDate(company.Revoke_App_Date),
    "moea.suspensionStartDate": rocToIsoDate(company.Sus_Beg_Date),
    "moea.suspensionEndDate": rocToIsoDate(company.Sus_End_Date),
  };

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

Up: [REST API enricher samples](https://documentation.cluedin.net/govern/rest-api-enricher-samples.md)
