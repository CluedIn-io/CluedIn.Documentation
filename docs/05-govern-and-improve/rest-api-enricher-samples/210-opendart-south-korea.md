---
layout: cluedin
title: OpenDART (South Korea)
parent: REST API enricher samples
grand_parent: Govern & improve
nav_order: 210
permalink: /govern/rest-api-enricher-samples/opendart-south-korea
content_type: reference
summary: "Looks up South Korean companies by DART corporation code in the Financial Supervisory Service's OpenDART API and adds the registered name, CEO, registration numbers, stock code and address. V2 script; needs an OpenDART API key."
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

This example looks up a South Korean company in [OpenDART](https://opendart.fss.or.kr/), the open API of the Financial Supervisory Service's electronic disclosure system (DART), by using its company overview API. For each golden record it stores the registered name in Korean and English, the CEO, the corporate and business registration numbers, the stock code and market, the address, website, industry code, and date of establishment.

**Enricher version:** V2  
**API key:** your OpenDART API key (`crtfc_key`)

{: .important }
In the current version of the REST API enricher, requests to OpenDART fail with `The SSL connection could not be established`. OpenDART accepts only TLS 1.2 cipher suites with DHE or RSA key exchange, which the enricher's HTTP client doesn't offer. The script is correct for the API, and it works once the enricher can connect to OpenDART.

To set up the enricher, see [Add REST API enricher](/govern/enrichment/rest-api#add-rest-api-enricher), then use the settings and script on this page.

## Settings

- **Accepted Business Domain** – `/Organization`, or the business domain that holds your companies.

- **Version** – V2 (recommended).

- **API Key** – your 40-character OpenDART API key. The script sends it as the `crtfc_key` query parameter.

- **Filters** – we recommend a rule that only accepts golden records where `organization.dartCorpCode` has a value. Otherwise, every record without a corporation code is listed on the enricher's **Logs** tab as having returned no results.

## Vocabulary and Properties

```
organization.dartCorpCode
```

`organization.dartCorpCode` holds the company's 8-digit DART corporation code (고유번호), for example `00126380`. If your data uses another vocabulary key, change this field and the `CORP_CODE_KEY` value at the top of the script.

OpenDART looks companies up by its own corporation code only. It doesn't accept a business registration number (사업자등록번호) or a corporate registration number (법인등록번호), and a 6-digit stock code is a different number. To find the corporation codes for your companies, download OpenDART's corporation code file (`GET https://opendart.fss.or.kr/api/corpCode.xml?crtfc_key=...`). It is a ZIP file with one XML entry per company that lists the corporation code, the company name, and the stock code of listed companies. Load it into CluedIn as a data source, or match it against your data, to add `organization.dartCorpCode` to your golden records. Keep the leading zeros: the script doesn't look up codes that have fewer than 8 digits.

## Request and response

**Base URL:** `https://opendart.fss.or.kr/api`  
**Endpoint:** `GET /company.json?crtfc_key={apiKey}&corp_code={corpCode}`  
**Authentication:** API key in the `crtfc_key` query parameter. Register on the [OpenDART website](https://opendart.fss.or.kr/) and apply for a key (인증키 신청). A key allows up to 20,000 requests a day.

The script sends one request per golden record:

```http
GET https://opendart.fss.or.kr/api/company.json?crtfc_key=your-opendart-api-key&corp_code=00126380
Accept: application/json
User-Agent: CluedIn REST API enricher
```

Shortened response:

```json
{
  "status": "000",
  "message": "정상",
  "corp_code": "00126380",
  "corp_name": "삼성전자(주)",
  "corp_name_eng": "SAMSUNG ELECTRONICS CO,.LTD",
  "stock_name": "삼성전자",
  "stock_code": "005930",
  "ceo_nm": "전영현, 노태문",
  "corp_cls": "Y",
  "jurir_no": "1301110006246",
  "bizr_no": "1248100998",
  "adres": "경기도 수원시 영통구  삼성로 129 (매탄동)",
  "hm_url": "www.samsung.com/sec",
  "ir_url": "",
  "phn_no": "02-2255-0114",
  "fax_no": "031-200-7538",
  "induty_code": "264",
  "est_dt": "19690113",
  "acc_mt": "12"
}
```

This response follows OpenDART's documented company overview response. The values are illustrative, not a captured response.

OpenDART returns HTTP 200 for errors too, and reports the result in `status`. For example, an unregistered key returns:

```json
{ "status": "010", "message": "등록되지 않은 인증키입니다." }
```

## Properties added by the enricher

| Property | Response field | Example |
| -------- | -------------- | ------- |
| `dart.corpCode` | `corp_code` | `00126380` |
| `dart.name` | `corp_name` | `삼성전자(주)` |
| `dart.nameEn` | `corp_name_eng` | `SAMSUNG ELECTRONICS CO,.LTD` |
| `dart.stockName` | `stock_name` | `삼성전자` |
| `dart.stockCode` | `stock_code` | `005930` |
| `dart.ceoName` | `ceo_nm` | `전영현, 노태문` |
| `dart.corporationClass` | `corp_cls`: `Y` is `KOSPI`, `K` is `KOSDAQ`, `N` is `KONEX`, `E` is `Other` | `KOSPI` |
| `dart.corporateRegistrationNumber` | `jurir_no` (법인등록번호) | `1301110006246` |
| `dart.businessRegistrationNumber` | `bizr_no` (사업자등록번호) | `1248100998` |
| `dart.address` | `adres` | `경기도 수원시 영통구  삼성로 129 (매탄동)` |
| `dart.website` | `hm_url` | `www.samsung.com/sec` |
| `dart.irWebsite` | `ir_url` | |
| `dart.phone` | `phn_no` | `02-2255-0114` |
| `dart.fax` | `fax_no` | `031-200-7538` |
| `dart.industryCode` | `induty_code` (Korean Standard Industrial Classification) | `264` |
| `dart.establishmentDate` | `est_dt`, converted from `YYYYMMDD` to `YYYY-MM-DD` | `1969-01-13` |
| `dart.fiscalYearEndMonth` | `acc_mt` | `12` |

A property is added only when OpenDART returns a value for it.

If the enricher has a **Preview** tab, the results appear there first. To add them to golden records, go to the **Map** tab, select **Map Data**, and choose **Auto Mapping**. Select the business domain, enter a new vocabulary named `DART` with the key prefix `dart`, and then create the mapping. Auto mapping also uses `name` as the golden record name, so remove that from the mapping if you want to keep your existing names. Then process the data on the **Process** tab. If the enricher has no **Preview** tab, the properties are added to the golden record as soon as it is enriched.

## How the script handles input and errors

- Spaces and dashes are removed, so `0012 6380` is looked up as `00126380`. The code must have exactly 8 digits. Golden records without a valid corporation code are skipped without calling the API.

- If the **API Key** field is empty, the script logs a message and adds nothing, without calling the API.

- If OpenDART rejects the key (status `010` unregistered key, `011` key that can't be used, `012` IP address not allowed, or `901` expired key), the script throws an error that says so. The golden record fails, and the error is shown on the enricher's **Logs** tab.

- If OpenDART has no data for the code (status `013`), is under maintenance (status `800`), or returns any other error, the script logs the reason and adds nothing. The answer isn't cached, so the next record with that code tries again.

- If the request limit is exceeded (status `020`, or HTTP 429), the script throws an error that makes the enricher try the golden record again later. The enricher retries every second, up to 1,000 times, so it can't wait for a daily limit to reset. If you enrich more than 20,000 golden records, spread the work over several days.

- Successful results are cached for 24 hours per corporation code. To change this, edit `CACHE_MILLISECONDS` in the script.

## Testing the enricher

- **Test connection** checks only that the script runs. It doesn't call OpenDART, so it doesn't check the key either.

- To try the setup, create a golden record with `organization.dartCorpCode` set to `00126380` (Samsung Electronics).

## Limitations

- The REST API enricher can't currently connect to OpenDART. See the note at the top of this page.

- OpenDART covers companies that file disclosures with DART: listed companies and other companies that are required to file, such as companies subject to external audit. Most small companies aren't in it.

- Lookups by business registration number or company name aren't supported. Use the corporation code file to find corporation codes, as described in [Vocabulary and Properties](#vocabulary-and-properties).

- Names and addresses are in Korean. `dart.nameEn` is added only when the company has an English name in DART.

- The script adds the company overview only. Financial statements, major shareholders and disclosure filings are available from other OpenDART endpoints.

## Process script

```javascript
// REST API enricher (V2) - South Korean company lookup with OpenDART
//
// Looks up a golden record's DART corporation code in the Financial Supervisory Service's
// OpenDART company overview API (https://opendart.fss.or.kr/), and adds the result to the
// golden record as dart.* properties:
//
//   dart.corpCode                     8-digit DART corporation code that was looked up
//   dart.name                         registered name (Korean)
//   dart.nameEn                       English name
//   dart.stockName                    stock name (short name)
//   dart.stockCode                    6-digit stock code, for listed companies
//   dart.ceoName                      name of the CEO
//   dart.corporationClass             market: KOSPI, KOSDAQ, KONEX or Other
//   dart.corporateRegistrationNumber  13-digit corporate registration number (법인등록번호)
//   dart.businessRegistrationNumber   10-digit business registration number (사업자등록번호)
//   dart.address                      address
//   dart.website                      website
//   dart.irWebsite                    investor relations website
//   dart.phone                        phone number
//   dart.fax                          fax number
//   dart.industryCode                 industry code (KSIC)
//   dart.establishmentDate            date of establishment (YYYY-MM-DD)
//   dart.fiscalYearEndMonth           month the fiscal year ends, for example 12
//
// Needs an OpenDART API key (crtfc_key) in the enricher's API Key field. See README.md next
// to this file for the enricher settings.
//
// A record gets no result (nothing is stored) when it has no valid DART corporation code, when
// OpenDART has no data for it, or when the API can't answer. A missing or rejected API key
// fails the record with an error that says so.

// ---- Settings -------------------------------------------------------------------------

// Vocabulary key to read. Add the same key to the Vocabulary and Properties field.
const CORP_CODE_KEY = "organization.dartCorpCode";

const OPENDART_URL = "https://opendart.fss.or.kr/api/company.json";

// The enricher replaces the token below with the value of the API Key field.
const API_KEY = "{APIKey}";

// How long to reuse an answer for the same corporation code. 0 turns caching off.
const CACHE_MILLISECONDS = 24 * 60 * 60 * 1000;

// ---- Script ---------------------------------------------------------------------------

// OpenDART status codes. "000" is success.
const NO_DATA_STATUS = "013";
// Request limit exceeded. Throwing an error that mentions TooManyRequests makes the enricher
// retry the record instead of skipping it.
const RETRY_STATUSES = ["020"];
// Problems with the API key: not registered, not usable, IP address not allowed, expired.
const KEY_STATUSES = ["010", "011", "012", "901"];

const CORPORATION_CLASSES = { Y: "KOSPI", K: "KOSDAQ", N: "KONEX", E: "Other" };

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

// Accepts "00126380" and "0012 6380". Returns the 8 digits, or null when the value isn't a
// corporation code. A shorter number isn't padded with zeros: a 6-digit value is more likely
// to be a stock code, which would look up a different company.
function parseCorpCode(raw) {
  const digits = raw.replace(/[\s\-]/g, "");
  return /^\d{8}$/.test(digits) && !/^0+$/.test(digits) ? digits : null;
}

function clean(value) {
  if (value === null || value === undefined) {
    return null;
  }
  const text = String(value).trim();
  return text === "" || /^-+$/.test(text) ? null : text;
}

function parseJson(text) {
  try {
    return JSON.parse(text);
  } catch (e) {
    return null;
  }
}

// OpenDART dates are YYYYMMDD.
function toIsoDate(value) {
  const text = clean(value);
  return text && /^\d{8}$/.test(text)
    ? `${text.substring(0, 4)}-${text.substring(4, 6)}-${text.substring(6, 8)}`
    : null;
}

// Calls the API. Returns the company overview, or null when there's no answer to store.
function lookUp(corpCode) {
  const apiResponse = http.send({
    url: `${OPENDART_URL}?crtfc_key=${encodeURIComponent(API_KEY)}&corp_code=${corpCode}`,
    method: "GET",
    headers: [
      { Key: "Accept", Value: "application/json" },
      // OpenDART redirects requests without a User-Agent to an HTML error page.
      { Key: "User-Agent", Value: "CluedIn REST API enricher" },
    ],
  });

  const status = String(apiResponse.HttpStatus || "");
  const body = parseJson(apiResponse.Content);
  const dartStatus = body && body.status !== undefined && body.status !== null ? String(body.status) : "";
  const message = body ? String(body.message || "") : "";

  if (status === "TooManyRequests" || RETRY_STATUSES.indexOf(dartStatus) >= 0) {
    throw new Error(`TooManyRequests - OpenDART request limit reached (${dartStatus || status} ${message}), the record will be retried`);
  }

  if (KEY_STATUSES.indexOf(dartStatus) >= 0 || status === "Unauthorized" || status === "Forbidden") {
    throw new Error(`OpenDART rejected the API key (status ${dartStatus || status}: ${message}). Check the API Key field of the enricher.`);
  }

  if (status === "OK" && dartStatus === "000" && body.corp_code) {
    return body;
  }

  if (dartStatus === NO_DATA_STATUS) {
    log(`OpenDART has no company for corporation code ${corpCode}.`);
  } else {
    // For example 100 (invalid parameter) or 800 (system maintenance).
    log(`OpenDART could not look up ${corpCode}. HTTP ${status}. ${String(apiResponse.Content || "").substring(0, 200)}`);
  }
  return null;
}

function run() {
  const corpCode = parseCorpCode(getValue(CORP_CODE_KEY));
  if (!corpCode) {
    // No valid corporation code on this record (this is also what Test connection hits,
    // because it passes placeholder values instead of real ones).
    return [];
  }

  if (API_KEY.trim() === "") {
    log("OpenDART needs an API key. Enter it in the API Key field of the enricher.");
    return [];
  }

  const cacheKey = `dart:${corpCode}`;
  const cached = CACHE_MILLISECONDS > 0 ? cache.get(cacheKey) : null;
  let company = cached ? parseJson(String(cached)) : null;

  if (!company) {
    company = lookUp(corpCode);
    if (!company) {
      return [];
    }
    if (CACHE_MILLISECONDS > 0) {
      cache.set(cacheKey, JSON.stringify(company), CACHE_MILLISECONDS);
    }
  }

  const data = {
    "dart.corpCode": clean(company.corp_code),
    "dart.name": clean(company.corp_name),
    "dart.nameEn": clean(company.corp_name_eng),
    "dart.stockName": clean(company.stock_name),
    "dart.stockCode": clean(company.stock_code),
    "dart.ceoName": clean(company.ceo_nm),
    "dart.corporationClass": CORPORATION_CLASSES[clean(company.corp_cls)] || clean(company.corp_cls),
    "dart.corporateRegistrationNumber": clean(company.jurir_no),
    "dart.businessRegistrationNumber": clean(company.bizr_no),
    "dart.address": clean(company.adres),
    "dart.website": clean(company.hm_url),
    "dart.irWebsite": clean(company.ir_url),
    "dart.phone": clean(company.phn_no),
    "dart.fax": clean(company.fax_no),
    "dart.industryCode": clean(company.induty_code),
    "dart.establishmentDate": toIsoDate(company.est_dt),
    "dart.fiscalYearEndMonth": clean(company.acc_mt),
  };

  // Leave out values OpenDART didn't return, so they don't overwrite existing data with blanks.
  Object.keys(data).forEach((key) => {
    if (data[key] === null || data[key] === undefined) {
      delete data[key];
    }
  });

  return [{ Data: data, Score: 100 }];
}

response = JSON.stringify(run());
```
