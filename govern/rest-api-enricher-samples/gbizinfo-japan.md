---
title: gBizINFO (Japan)
url: https://documentation.cluedin.net/govern/rest-api-enricher-samples/gbizinfo-japan
content_type: reference
section: Govern & improve > REST API enricher samples
---

# gBizINFO (Japan)

> reference: Facts, options, APIs.

This example looks up an organization's 13-digit Japanese corporate number (法人番号, *hōjin bangō*) in [gBizINFO](https://info.gbiz.go.jp/), the corporate information service of Japan's Ministry of Economy, Trade and Industry (METI), by using its REST API. For each golden record it stores the registered name in Japanese, English and katakana, the head office address, the representative, capital stock, number of employees, date of establishment, website, and, for a closed corporation, the closing date and reason.

**Enricher version:** V2  
**API key:** your gBizINFO API token

To set up the enricher, see [Add REST API enricher](https://documentation.cluedin.net/govern/enrichment/rest-api.md#add-rest-api-enricher), then use the settings and script on this page.

## Settings

- **Accepted Business Domain** – `/Organization`, or the business domain that holds your companies.

- **Version** – V2 (recommended).

- **API Key** – your gBizINFO API token. The script sends it in the `X-hojinInfo-api-token` header.

- **Filters** – we recommend a rule that only accepts golden records where `organization.corporateNumber` has a value. Otherwise, every record without a corporate number is listed on the enricher's **Logs** tab as having returned no results.

## Vocabulary and Properties

```
organization.corporateNumber
```

`organization.corporateNumber` holds the 13-digit corporate number assigned by Japan's National Tax Agency. If your data uses another vocabulary key, change this field and the `CORPORATE_NUMBER_KEY` value at the top of the script.

## Request and response

**Base URL:** `https://api.info.gbiz.go.jp/hojin`  
**Endpoint:** `GET /v2/hojin/{corporateNumber}`  
**Authentication:** API token in the `X-hojinInfo-api-token` header. Apply for a token on the [gBizINFO API page](https://info.gbiz.go.jp/api/index.html). The application form is in Japanese, and the token is sent to you by email.

The full API definition is in gBizINFO's [Swagger UI](https://api.info.gbiz.go.jp/hojin/swagger-ui/index.html).

The script sends one request per golden record:

```http
GET https://api.info.gbiz.go.jp/hojin/v2/hojin/1180301018771
X-hojinInfo-api-token: your-gbizinfo-api-token
Accept: application/json
```

Shortened response:

```json
{
  "id": null,
  "message": "200 - OK.",
  "errors": [],
  "hojin-infos": [
    {
      "corporate_number": "1180301018771",
      "name": "トヨタ自動車株式会社",
      "name_en": "TOYOTA MOTOR CORPORATION",
      "kana": "トヨタジドウシャ",
      "location": "愛知県豊田市トヨタ町1番地",
      "postal_code": "4718571",
      "representative_name": "佐藤恒治",
      "capital_stock": 635401000000,
      "employee_number": 70056,
      "date_of_establishment": "1937-08-28T00:00:00+09:00",
      "founding_year": 1937,
      "company_url": "https://global.toyota/",
      "business_summary": "自動車の製造・販売",
      "industry": ["製造業"],
      "update_date": "2026-10-01T00:00:00+09:00"
    }
  ]
}
```

This response follows the `HojinInfoResponseV2` schema in gBizINFO's API definition. The values are illustrative, not a captured response.

## Properties added by the enricher

| Property | Response field | Example |
| -------- | -------------- | ------- |
| `gbiz.corporateNumber` | `corporate_number` | `1180301018771` |
| `gbiz.name` | `name` | `トヨタ自動車株式会社` |
| `gbiz.nameEn` | `name_en` | `TOYOTA MOTOR CORPORATION` |
| `gbiz.kana` | `kana` | `トヨタジドウシャ` |
| `gbiz.location` | `location` (head office address) | `愛知県豊田市トヨタ町1番地` |
| `gbiz.postalCode` | `postal_code` | `4718571` |
| `gbiz.status` | `status` | `閉鎖` |
| `gbiz.closeDate` | `close_date` (date only) | `2020-03-31` |
| `gbiz.closeCause` | `close_cause` | `清算の結了` |
| `gbiz.representativeName` | `representative_name` | `佐藤恒治` |
| `gbiz.capitalStock` | `capital_stock` (yen) | `635401000000` |
| `gbiz.employeeNumber` | `employee_number` | `70056` |
| `gbiz.dateOfEstablishment` | `date_of_establishment` (date only) | `1937-08-28` |
| `gbiz.foundingYear` | `founding_year` | `1937` |
| `gbiz.companyUrl` | `company_url` | `https://global.toyota/` |
| `gbiz.businessSummary` | `business_summary` | `自動車の製造・販売` |
| `gbiz.industry` | `industry` (joined with `; `) | `製造業` |
| `gbiz.updateDate` | `update_date` (date only) | `2026-10-01` |

A property is added only when gBizINFO returns a value for it. Many corporations have only a name, address and corporate number in gBizINFO; the other values come from filings with government agencies and are often missing.

If the enricher has a **Preview** tab, the results appear there first. To add them to golden records, go to the **Map** tab, select **Map Data**, and choose **Auto Mapping**. Select the business domain, enter a new vocabulary named `gBizINFO` with the key prefix `gbiz`, and then create the mapping. Auto mapping also uses `name` as the golden record name, so remove that from the mapping if you want to keep your existing names. Then process the data on the **Process** tab. If the enricher has no **Preview** tab, the properties are added to the golden record as soon as it is enriched.

## How the script handles input and errors

- Spaces, dots and dashes are removed, and full-width digits (`１２３`) are converted, so `1-1803-0101-8771` is looked up as `1180301018771`. The number must have 13 digits and a valid check digit (the first digit). Golden records without a valid corporate number, such as a qualified invoice issuer number that starts with `T`, are skipped without calling the API.

- If the **API Key** field is empty, the script logs a message and adds nothing, without calling the API.

- If gBizINFO rejects the token (HTTP 401 or 403), the script throws an error that says so. The golden record fails, and the error is shown on the enricher's **Logs** tab.

- If gBizINFO has no record for the number, or returns any other error, the script logs the reason and adds nothing. The answer isn't cached, so the next record with that number tries again.

- If the API reports that it is too busy (HTTP 429), the script throws an error that makes the enricher try the golden record again later.

- Successful results are cached for 24 hours per corporate number. To change this, edit `CACHE_MILLISECONDS` in the script.

## Testing the enricher

- **Test connection** checks only that the script runs. It doesn't call gBizINFO, so it doesn't check the token either.

- To try the setup, create a golden record with `organization.corporateNumber` set to `1180301018771` (Toyota Motor Corporation) or `7000012050002` (the National Tax Agency).

## Limitations

- gBizINFO only answers lookups by corporate number. To find a corporate number from a company name, use gBizINFO's search endpoint (`GET /v2/hojin?name=...`) or the National Tax Agency's corporate number publication site.

- Names, addresses, status and descriptions are in Japanese. `gbiz.nameEn` is added only when the corporation has registered an English name.

- The script adds the basic corporate information only. Certifications, commendations, finance, patents, procurement, subsidies and workplace information are available from separate endpoints, such as `/v2/hojin/{corporateNumber}/finance`.

## Process script

```javascript
// REST API enricher (V2) - Japanese company lookup with gBizINFO
//
// Looks up a golden record's 13-digit Japanese corporate number (法人番号) in gBizINFO, the
// Ministry of Economy, Trade and Industry's corporate information service, using its REST API
// (https://info.gbiz.go.jp/), and adds the result to the golden record as gbiz.* properties:
//
//   gbiz.corporateNumber      13-digit corporate number that was looked up
//   gbiz.name                 registered name (Japanese)
//   gbiz.nameEn               English name, when registered
//   gbiz.kana                 name in katakana
//   gbiz.location             head office address
//   gbiz.postalCode           head office postal code
//   gbiz.status               status, when gBizINFO has one (for example 閉鎖 for closed)
//   gbiz.closeDate            date the registration was closed (YYYY-MM-DD)
//   gbiz.closeCause           reason the registration was closed
//   gbiz.representativeName   name of the representative
//   gbiz.capitalStock         capital stock in yen
//   gbiz.employeeNumber       number of employees
//   gbiz.dateOfEstablishment  date of establishment (YYYY-MM-DD)
//   gbiz.foundingYear         year the business was founded
//   gbiz.companyUrl           website
//   gbiz.businessSummary      business summary
//   gbiz.industry             industries, separated by "; "
//   gbiz.updateDate           date gBizINFO last updated the record (YYYY-MM-DD)
//
// Needs a gBizINFO API token in the enricher's API Key field. See README.md next to this file
// for the enricher settings.
//
// A record gets no result (nothing is stored) when it has no valid corporate number, when
// gBizINFO has no record for it, or when the API can't answer. A missing or rejected API token
// fails the record with an error that says so.

// ---- Settings -------------------------------------------------------------------------

// Vocabulary key to read. Add the same key to the Vocabulary and Properties field.
const CORPORATE_NUMBER_KEY = "organization.corporateNumber";

const GBIZINFO_URL = "https://api.info.gbiz.go.jp/hojin/v2/hojin/";

// The enricher replaces the token below with the value of the API Key field.
const API_KEY = "{APIKey}";

// How long to reuse an answer for the same corporate number. 0 turns caching off.
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

// Accepts "7000012050002", "7-0000-1205-0002", "7000 0120 50002", and full-width digits.
// Returns the 13 digits, or null when the number isn't a valid corporate number (the first
// digit is a check digit over the other 12).
function parseCorporateNumber(raw) {
  const halfWidth = raw.replace(/[０-９]/g, (c) => String.fromCharCode(c.charCodeAt(0) - 0xfee0));
  const digits = halfWidth.replace(/[\s\-.]/g, "");
  if (!/^\d{13}$/.test(digits)) {
    return null;
  }
  // Check digit = 9 - (sum of the 12 base digits, weighted 1, 2, 1, 2, ... from the right) mod 9
  let sum = 0;
  for (let n = 1; n <= 12; n++) {
    sum += Number(digits.charAt(13 - n)) * (n % 2 === 1 ? 1 : 2);
  }
  return 9 - (sum % 9) === Number(digits.charAt(0)) ? digits : null;
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

// gBizINFO dates can carry a time and offset (1949-05-24T00:00:00+09:00); keep the date only.
function dateOnly(value) {
  const text = clean(value);
  return text && /^\d{4}-\d{2}-\d{2}/.test(text) ? text.substring(0, 10) : null;
}

function numberOrNull(value) {
  return typeof value === "number" ? value : null;
}

// Calls the API. Returns the corporation, or null when there's no answer to store.
function lookUp(corporateNumber) {
  const apiResponse = http.send({
    url: GBIZINFO_URL + corporateNumber,
    method: "GET",
    headers: [
      { Key: "X-hojinInfo-api-token", Value: API_KEY },
      { Key: "Accept", Value: "application/json" },
    ],
  });

  const status = String(apiResponse.HttpStatus || "");
  const body = parseJson(apiResponse.Content);

  if (status === "TooManyRequests") {
    throw new Error("TooManyRequests - gBizINFO is busy, the record will be retried");
  }

  if (status === "Unauthorized" || status === "Forbidden") {
    throw new Error(`gBizINFO rejected the API token (HTTP ${status}). Check the API Key field of the enricher.`);
  }

  const infos = body && Array.isArray(body["hojin-infos"]) ? body["hojin-infos"] : [];
  if (status === "OK" && infos.length > 0 && infos[0] && infos[0].corporate_number) {
    return infos[0];
  }

  log(`gBizINFO could not look up ${corporateNumber}. HTTP ${status}. ${String(apiResponse.Content || "").substring(0, 200)}`);
  return null;
}

function run() {
  const corporateNumber = parseCorporateNumber(getValue(CORPORATE_NUMBER_KEY));
  if (!corporateNumber) {
    // No valid corporate number on this record (this is also what Test connection hits,
    // because it passes placeholder values instead of real ones).
    return [];
  }

  if (API_KEY.trim() === "") {
    log("gBizINFO needs an API token. Enter it in the API Key field of the enricher.");
    return [];
  }

  const cacheKey = `gbiz:${corporateNumber}`;
  const cached = CACHE_MILLISECONDS > 0 ? cache.get(cacheKey) : null;
  let hojin = cached ? parseJson(String(cached)) : null;

  if (!hojin) {
    hojin = lookUp(corporateNumber);
    if (!hojin) {
      return [];
    }
    if (CACHE_MILLISECONDS > 0) {
      cache.set(cacheKey, JSON.stringify(hojin), CACHE_MILLISECONDS);
    }
  }

  const industry = Array.isArray(hojin.industry) ? hojin.industry.filter((x) => !!clean(x)) : [];

  const data = {
    "gbiz.corporateNumber": clean(hojin.corporate_number),
    "gbiz.name": clean(hojin.name),
    "gbiz.nameEn": clean(hojin.name_en),
    "gbiz.kana": clean(hojin.kana),
    "gbiz.location": clean(hojin.location),
    "gbiz.postalCode": clean(hojin.postal_code),
    "gbiz.status": clean(hojin.status),
    "gbiz.closeDate": dateOnly(hojin.close_date),
    "gbiz.closeCause": clean(hojin.close_cause),
    "gbiz.representativeName": clean(hojin.representative_name),
    "gbiz.capitalStock": numberOrNull(hojin.capital_stock),
    "gbiz.employeeNumber": numberOrNull(hojin.employee_number),
    "gbiz.dateOfEstablishment": dateOnly(hojin.date_of_establishment),
    "gbiz.foundingYear": numberOrNull(hojin.founding_year),
    "gbiz.companyUrl": clean(hojin.company_url),
    "gbiz.businessSummary": clean(hojin.business_summary),
    "gbiz.industry": industry.length > 0 ? industry.join("; ") : null,
    "gbiz.updateDate": dateOnly(hojin.update_date),
  };

  // Leave out values gBizINFO didn't return, so they don't overwrite existing data with blanks.
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
