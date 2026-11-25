---
title: CIPC (South Africa)
url: https://documentation.cluedin.net/govern/rest-api-enricher-samples/cipc-south-africa
content_type: reference
section: Govern & improve > REST API enricher samples
---

# CIPC (South Africa)

> reference: Facts, options, APIs.

This example looks up an organization's South African enterprise (company) registration number with the Companies and Intellectual Property Commission's (CIPC) **CIPC Public Data - Commercial** API on the [APIVerse Hub](https://developer.cipc.co.za/), by using its **Basic company information** operation. For each golden record it stores the registered name, enterprise type and status, industry, registration and business start dates, financial year end, physical and postal addresses, and tax number.

**Enricher version:** V2  
**API key:** your CIPC APIVerse subscription key (a free tier and paid annual tiers are available)

> **Important:** This sample couldn't be tried with a real subscription key. The request and response follow the API definition published on the APIVerse Hub, and the endpoint is confirmed to exist (it rejects an invalid key), but the example values on this page are illustrative.

To set up the enricher, see [Add REST API enricher](https://documentation.cluedin.net/govern/enrichment/rest-api.md#add-rest-api-enricher), then use the settings and script on this page.

## Settings

- **Accepted Business Domain** – `/Organization`, or the business domain that holds your companies.

- **Version** – V2 (recommended).

- **API Key** – your APIVerse subscription key. To get one, sign up on the [APIVerse Hub](https://developer.cipc.co.za/), subscribe to the **CIPC Public Data - Commercial** API, and copy the primary key of the subscription from your profile. The script sends it in the `Ocp-Apim-Subscription-Key` header. If the field is empty, the script adds nothing and doesn't call CIPC.

- **Filters** – we recommend a rule that only accepts golden records where `organization.registrationNumber` has a value. Otherwise, every record without a registration number is listed on the enricher's **Logs** tab as having returned no results.

## Vocabulary and Properties

```
organization.registrationNumber
```

`organization.registrationNumber` holds the enterprise number in the `YYYY/NNNNNN/NN` format, for example `2020/939681/07`. If your data uses another vocabulary key, change this field and the `REGISTRATION_NUMBER_KEY` value at the top of the script.

## Request and response

**Base URL:** `https://apim.cipc.co.za/companies-api/v1`  
**Endpoint:** `POST /information`  
**Authentication:** subscription key in the `Ocp-Apim-Subscription-Key` request header

The script sends one request per golden record:

```http
POST https://apim.cipc.co.za/companies-api/v1/information
Ocp-Apim-Subscription-Key: <your subscription key>
Content-Type: application/json
Accept: application/json

{ "enterprise_number": "2020/939681/07" }
```

Response, with the fields from the published response schema (the values are illustrative):

```json
{
  "Enterprise": [
    {
      "enterprise_number": "2020/939681/07",
      "country_code": "ZA",
      "enterprise_name": "EXAMPLE TRADING (PTY) LTD",
      "enterprise_type_description": "Private Company",
      "sic_description": "Retail trade",
      "registration_date": "2020-11-23",
      "enterprise_status_description": "In Business",
      "financial_year_end": "February",
      "financial_year_effective_date": null,
      "physical_address_1": "1 Main Road",
      "physical_address_2": "Sandton",
      "physical_address_3": "Johannesburg",
      "physical_address_4": "",
      "physical_code": "2196",
      "postal_address_1": "PO Box 1",
      "postal_address_2": "Sandton",
      "postal_address_3": "",
      "postal_address_4": "",
      "postal_code": "2146",
      "tax_number": "9000000000",
      "business_start_date": "2020-11-23"
    }
  ]
}
```

## Properties added by the enricher

| Property | Response field | Example |
| -------- | -------------- | ------- |
| `cipc.enterpriseNumber` | `enterprise_number` | `2020/939681/07` |
| `cipc.name` | `enterprise_name` | `EXAMPLE TRADING (PTY) LTD` |
| `cipc.enterpriseType` | `enterprise_type_description` | `Private Company` |
| `cipc.status` | `enterprise_status_description` | `In Business` |
| `cipc.industry` | `sic_description` | `Retail trade` |
| `cipc.registrationDate` | `registration_date`, as `YYYY-MM-DD` | `2020-11-23` |
| `cipc.businessStartDate` | `business_start_date`, as `YYYY-MM-DD` | `2020-11-23` |
| `cipc.financialYearEnd` | `financial_year_end` | `February` |
| `cipc.physicalAddress` | `physical_address_1` to `physical_address_4` and `physical_code`, on one line | `1 Main Road, Sandton, Johannesburg, 2196` |
| `cipc.postalAddress` | `postal_address_1` to `postal_address_4` and `postal_code`, on one line | `PO Box 1, Sandton, 2146` |
| `cipc.countryCode` | `country_code` | `ZA` |
| `cipc.taxNumber` | `tax_number` | `9000000000` |

A property is added only when CIPC returns a value for it. A date in a format the script doesn't recognise is stored as returned.

If the enricher has a **Preview** tab, the results appear there first. To add them to golden records, go to the **Map** tab, select **Map Data**, and choose **Auto Mapping**. Select the business domain, enter a new vocabulary named `CIPC` with the key prefix `cipc`, and then create the mapping. Auto mapping also uses `name` as the golden record name, so remove that from the mapping if you want to keep your existing names. Then process the data on the **Process** tab. If the enricher has no **Preview** tab, the properties are added to the golden record as soon as it is enriched.

## How the script handles input and errors

- The enterprise number is sent as `YYYY/NNNNNN/NN`. Dashes, spaces and a leading `CK` or `K` are accepted, so `2020-939681-07` and `202093968107` are both sent as `2020/939681/07`. Golden records without a valid enterprise number are skipped without calling CIPC.

- If CIPC rejects the subscription key (HTTP 401 or 403), the script throws an error, so the golden record is listed on the **Logs** tab with a message to check the **API Key** field.

- If CIPC returns no enterprise with that number, or returns another error, the script logs the reason and adds nothing.

- If the rate limit of your subscription is reached (HTTP 429), the script throws an error that makes the enricher try the golden record again later.

- Successful results are cached for 7 days per enterprise number, because the free tier allows only 100 calls a year. To change this, edit `CACHE_MILLISECONDS` in the script.

## Testing the enricher

- **Test connection** checks only that the script runs. It doesn't call CIPC.

- To try the setup, create a golden record with `organization.registrationNumber` set to the enterprise number of a company you know, then enrich it.

## Limitations

- The free APIVerse tier allows 100 calls a year at 5 calls a minute. Paid tiers allow more. Check your tier before you enrich a large number of golden records.

- Directors, filing history and the registered office address are available from other operations of the same API (`/company-directors`, `/filing-history`, `/registered-office-address`) and aren't added by this script.

- CIPC's developer guide also describes an OAuth2 token flow. The published API definition for **CIPC Public Data - Commercial** only requires the subscription key, so the script doesn't request a token. If CIPC starts to require one, calls fail with HTTP 401 and the message on the **Logs** tab says so.

## Process script

```javascript
// REST API enricher (V2) - South African company lookup with the CIPC APIVerse API
//
// Looks up a golden record's South African enterprise (company) registration number with the
// Companies and Intellectual Property Commission's "CIPC Public Data - Commercial" API on the
// APIVerse Hub (https://developer.cipc.co.za/), by using its Basic company information
// operation, and adds the result to the golden record as cipc.* properties:
//
//   cipc.enterpriseNumber   enterprise number that was looked up, for example 2020/939681/07
//   cipc.name               registered enterprise name
//   cipc.enterpriseType     enterprise type, for example Private Company
//   cipc.status             enterprise status, for example In Business
//   cipc.industry           industry (SIC) description
//   cipc.registrationDate   registration date
//   cipc.businessStartDate  business start date
//   cipc.financialYearEnd   financial year end
//   cipc.physicalAddress    physical address on one line
//   cipc.postalAddress      postal address on one line
//   cipc.countryCode        country code
//   cipc.taxNumber          tax number
//
// Needs an APIVerse subscription key (Ocp-Apim-Subscription-Key), entered in the enricher's
// API Key field. See README.md next to this file for the enricher settings.
//
// A record gets no result (nothing is stored) when it has no valid enterprise number, when
// CIPC has no enterprise with that number, or when the API can't answer. A missing or rejected
// key fails the record with an error that says so.

// ---- Settings -------------------------------------------------------------------------

// Vocabulary key to read. Add the same key to the Vocabulary and Properties field.
const REGISTRATION_NUMBER_KEY = "organization.registrationNumber";

const CIPC_URL = "https://apim.cipc.co.za/companies-api/v1/information";

// The {APIKey} placeholder is replaced with the API Key field value (your subscription key).
const API_KEY = "{APIKey}";

// How long to reuse an answer for the same enterprise. 0 turns caching off. The free APIVerse
// tier allows 100 calls a year, so a long cache saves calls.
const CACHE_MILLISECONDS = 7 * 24 * 60 * 60 * 1000;

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

// Accepts "2020/939681/07", "2020-939681-07", "2020 939681 07", "202093968107" and a leading
// "CK" for close corporations. Returns "YYYY/NNNNNN/NN", or null when it isn't an enterprise
// number.
function parseEnterpriseNumber(raw) {
  const text = raw.toUpperCase().replace(/^(CK|K)\s*/, "");
  if (!/^[0-9\s/.-]+$/.test(text)) {
    return null;
  }
  const digits = text.replace(/[^0-9]/g, "");
  if (!/^(18|19|20)\d{10}$/.test(digits)) {
    return null;
  }
  return `${digits.substring(0, 4)}/${digits.substring(4, 10)}/${digits.substring(10, 12)}`;
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

// Stores dates as YYYY-MM-DD where the format is recognisable, otherwise as returned. A full
// timestamp would be turned into a date in the server's own format by the enricher.
function formatDate(value) {
  const text = clean(value);
  if (!text) {
    return null;
  }
  const iso = /^(\d{4})[-/](\d{2})[-/](\d{2})/.exec(text);
  if (iso) {
    return `${iso[1]}-${iso[2]}-${iso[3]}`;
  }
  const compact = /^(\d{4})(\d{2})(\d{2})$/.exec(text);
  return compact ? `${compact[1]}-${compact[2]}-${compact[3]}` : text;
}

function formatAddress(item, prefix, codeField) {
  const parts = [];
  for (let i = 1; i <= 4; i++) {
    const line = clean(item[`${prefix}${i}`]);
    if (line) {
      parts.push(line);
    }
  }
  const code = clean(item[codeField]);
  if (code) {
    parts.push(code);
  }
  return parts.length > 0 ? parts.join(", ") : null;
}

function getEnterprises(body) {
  if (!body) {
    return [];
  }
  const list = body.Enterprise || body.enterprise || body.Enterprises || body.enterprises;
  if (Array.isArray(list)) {
    return list;
  }
  return list && typeof list === "object" ? [list] : [];
}

function normalise(number) {
  return String(number || "").replace(/[^0-9]/g, "");
}

// Calls the CIPC API. Returns the enterprise, or null when there's no answer to store.
function lookUp(enterpriseNumber) {
  const apiResponse = http.send({
    url: CIPC_URL,
    method: "POST",
    headers: [
      { Key: "Content-Type", Value: "application/json" },
      { Key: "Accept", Value: "application/json" },
      { Key: "Ocp-Apim-Subscription-Key", Value: API_KEY },
    ],
    body: { enterprise_number: enterpriseNumber },
  });

  const status = String(apiResponse.HttpStatus || "");
  const body = parseJson(apiResponse.Content);

  if (status === "TooManyRequests") {
    throw new Error("TooManyRequests - the CIPC API rate limit was reached, the record will be retried");
  }

  if (status === "Unauthorized" || status === "Forbidden") {
    const message = body && body.message ? body.message : String(apiResponse.Content || "").substring(0, 200);
    throw new Error(`The CIPC API rejected the subscription key in the API Key field (HTTP ${status}). ${message}`);
  }

  if (status === "OK") {
    const enterprises = getEnterprises(body);
    for (let i = 0; i < enterprises.length; i++) {
      if (enterprises[i] && normalise(enterprises[i].enterprise_number) === normalise(enterpriseNumber)) {
        return enterprises[i];
      }
    }
  }

  log(`CIPC could not look up ${enterpriseNumber}. HTTP ${status}. ${String(apiResponse.Content || "").substring(0, 200)}`);
  return null;
}

function run() {
  const enterpriseNumber = parseEnterpriseNumber(getValue(REGISTRATION_NUMBER_KEY));
  if (!enterpriseNumber) {
    // No valid enterprise number on this record (this is also what Test connection hits,
    // because it passes placeholder values instead of real ones).
    return [];
  }

  if (!clean(API_KEY)) {
    log("The CIPC API needs a subscription key. Enter your APIVerse subscription key in the enricher's API Key field.");
    return [];
  }

  const cacheKey = `cipc:${enterpriseNumber}`;
  const cached = CACHE_MILLISECONDS > 0 ? cache.get(cacheKey) : null;
  let item = cached ? parseJson(String(cached)) : null;

  if (!item) {
    item = lookUp(enterpriseNumber);
    if (!item) {
      return [];
    }
    if (CACHE_MILLISECONDS > 0) {
      cache.set(cacheKey, JSON.stringify(item), CACHE_MILLISECONDS);
    }
  }

  const data = {
    "cipc.enterpriseNumber": clean(item.enterprise_number) || enterpriseNumber,
    "cipc.name": clean(item.enterprise_name),
    "cipc.enterpriseType": clean(item.enterprise_type_description),
    "cipc.status": clean(item.enterprise_status_description),
    "cipc.industry": clean(item.sic_description),
    "cipc.registrationDate": formatDate(item.registration_date),
    "cipc.businessStartDate": formatDate(item.business_start_date),
    "cipc.financialYearEnd": clean(item.financial_year_end),
    "cipc.physicalAddress": formatAddress(item, "physical_address_", "physical_code"),
    "cipc.postalAddress": formatAddress(item, "postal_address_", "postal_code"),
    "cipc.countryCode": clean(item.country_code),
    "cipc.taxNumber": clean(item.tax_number),
  };

  // Leave out values CIPC didn't return, so they don't overwrite existing data with blanks.
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
