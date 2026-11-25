---
title: SEC (Philippines)
url: https://documentation.cluedin.net/govern/rest-api-enricher-samples/sec-philippines
content_type: reference
section: Govern & improve > REST API enricher samples
---

# SEC (Philippines)

> reference: Facts, options, APIs.

This example looks up an organization's SEC registration number with the Philippine Securities and Exchange Commission's **SECNumber** API on the [SEC API Marketplace](https://portal.sec.gov.ph/). For each golden record it stores the registered company name, the date the registration was approved, the registration status and secondary licenses.

**Enricher version:** V2  
**API key:** your SEC API Marketplace consumer key and secret (the SECNumber package is free, but needs a credentialed eSECURE account)

> **Important:** This sample couldn't be tried against the live service: the SEC API gateway and the Marketplace answered with an "SEC Website Maintenance" page (HTTP 403) while this sample was written. The request, response and token flow follow the SEC's own guide, *Using the SEC API Marketplace with Postman*, and the example values on this page are illustrative.

To set up the enricher, see [Add REST API enricher](https://documentation.cluedin.net/govern/enrichment/rest-api.md#add-rest-api-enricher), then use the settings and script on this page.

## Settings

- **Accepted Business Domain** – `/Organization`, or the business domain that holds your companies.

- **Version** – V2 (recommended).

- **API Key** – your Marketplace credentials, as `consumerKey:consumerSecret`. To get them:
  1. Sign in to the SEC API Marketplace with your eSECURE account.
  2. Subscribe an application to the **SECNumber** API.
  3. In **Applications**, open the application, go to **Production Keys** › **OAuth2 Tokens**, and select **Generate Keys**.
  4. Copy the **Consumer Key** and **Consumer Secret**, and enter them in the **API Key** field separated by a colon.

  The script gets an access token from the token endpoint with these credentials and reuses it until shortly before it expires. You can also enter an access token on its own (no colon). The script then uses it as it is, but access tokens expire, after which every record fails until you replace it. If the field is empty, the script adds nothing and doesn't call the SEC.

- **Filters** – we recommend a rule that only accepts golden records where `organization.secRegistrationNumber` has a value. Otherwise, every record without an SEC number is listed on the enricher's **Logs** tab as having returned no results.

## Vocabulary and Properties

```
organization.secRegistrationNumber
```

`organization.secRegistrationNumber` holds the SEC registration number, for example `A199600179` or `CS201912345`. If your data uses another vocabulary key, change this field and the `SEC_NUMBER_KEY` value at the top of the script.

## Request and response

**Gateway URL:** `https://gwwso2.sec.gov.ph/secnumber/1.0.0`  
**Endpoint:** `GET /client_sec_no_status.php?sec_no={secNumber}`  
**Authentication:** OAuth2 bearer token in the `Authorization` header. Tokens come from `https://portal.sec.gov.ph/oauth2/token` with the client credentials grant.

When it has no valid token, the script first requests one:

```http
POST https://portal.sec.gov.ph/oauth2/token
Content-Type: application/x-www-form-urlencoded
Accept: application/json

grant_type=client_credentials&client_id=<consumer key>&client_secret=<consumer secret>&scope=openid
```

```json
{ "access_token": "eyJ4NXQiOi...", "scope": "openid", "token_type": "Bearer", "expires_in": 3600 }
```

Then it sends one request per golden record:

```http
GET https://gwwso2.sec.gov.ph/secnumber/1.0.0/client_sec_no_status.php?sec_no=A199600179
Authorization: Bearer eyJ4NXQiOi...
Accept: application/json
```

Response, with the fields shown in the SEC's guide (the values are illustrative):

```json
{
  "success": true,
  "data": [
    {
      "sec_no": "A199600179",
      "company_name": "EXAMPLE HOLDINGS, INC.",
      "date_approved": "1996-01-15",
      "licenses": "None",
      "status": "Registered"
    }
  ]
}
```

## Properties added by the enricher

| Property | Response field | Example |
| -------- | -------------- | ------- |
| `secph.secNumber` | `sec_no` | `A199600179` |
| `secph.name` | `company_name` | `EXAMPLE HOLDINGS, INC.` |
| `secph.dateApproved` | `date_approved`, as `YYYY-MM-DD` | `1996-01-15` |
| `secph.status` | `status` | `Registered` |
| `secph.licenses` | `licenses` | `None` |

A property is added only when the SEC returns a value for it. A date in a format the script doesn't recognise is stored as returned.

If the enricher has a **Preview** tab, the results appear there first. To add them to golden records, go to the **Map** tab, select **Map Data**, and choose **Auto Mapping**. Select the business domain, enter a new vocabulary named `SEC Philippines` with the key prefix `secph`, and then create the mapping. Auto mapping also uses `name` as the golden record name, so remove that from the mapping if you want to keep your existing names. Then process the data on the **Process** tab. If the enricher has no **Preview** tab, the properties are added to the golden record as soon as it is enriched.

## How the script handles input and errors

- The SEC number is converted to capitals, and spaces, dots, dashes and slashes are removed, so `cs 2019-12345` is looked up as `CS201912345`. It must be up to 4 letters followed by 5 to 12 digits. Golden records without a valid SEC number are skipped without calling the SEC.

- If the token endpoint rejects the consumer key and secret, or the API rejects the token (HTTP 401, or HTTP 403 with a JSON error such as an application that isn't subscribed to SECNumber), the script throws an error, so the golden record is listed on the **Logs** tab with a message to check the **API Key** field. When a token that was reused from the cache is rejected, the script first gets a new token and tries once more.

- If the SEC has no company with that number, or the service is unavailable (for example an HTML maintenance page), the script logs the reason and adds nothing.

- If the SEC reports that it is too busy or the call limit is reached (HTTP 429), the script throws an error that makes the enricher try the golden record again later.

- Successful results are cached for 30 days per SEC number, because the free SECNumber package allows only a few calls a day. To change this, edit `CACHE_MILLISECONDS` in the script.

## Testing the enricher

- **Test connection** checks only that the script runs. It doesn't call the SEC.

- To try the setup, create a golden record with `organization.secRegistrationNumber` set to the SEC number of a company you know, then enrich it.

## Limitations

- The free SECNumber package allows roughly 10 calls a day. Enrich a small number of golden records at a time, or subscribe to a paid package.

- The SECNumber API only looks up a known SEC number. Name search, addresses, the General Information Sheet (GIS) and audited financial statements (AFS) are in the paid **CompanyInformationLookup** API, which this script doesn't use.

- Access needs a credentialed eSECURE account.

## Process script

```javascript
// REST API enricher (V2) - Philippine company lookup with the SEC API Marketplace
//
// Looks up a golden record's SEC registration number with the Philippine Securities and
// Exchange Commission's SECNumber API on the SEC API Marketplace (https://portal.sec.gov.ph/),
// and adds the result to the golden record as secph.* properties:
//
//   secph.secNumber      SEC registration number that was looked up, for example A199600179
//   secph.name           registered company name
//   secph.dateApproved   date the registration was approved
//   secph.status         registration status
//   secph.licenses       secondary licenses
//
// Credentials go in the enricher's API Key field, in one of two forms:
//   consumerKey:consumerSecret  (recommended) the Production Keys of your Marketplace
//                               application. The script gets an access token from the token
//                               endpoint itself and reuses it until shortly before it expires.
//   accessToken                 an access token you generated yourself. It expires, after
//                               which every record fails until you replace it.
// See README.md next to this file for the enricher settings.
//
// A record gets no result (nothing is stored) when it has no valid SEC number, when the SEC has
// no company with that number, or when the API can't answer. Missing or rejected credentials
// fail the record with an error that says so.

// ---- Settings -------------------------------------------------------------------------

// Vocabulary key to read. Add the same key to the Vocabulary and Properties field.
const SEC_NUMBER_KEY = "organization.secRegistrationNumber";

const SEC_URL = "https://gwwso2.sec.gov.ph/secnumber/1.0.0/client_sec_no_status.php";
const TOKEN_URL = "https://portal.sec.gov.ph/oauth2/token";

// The {APIKey} placeholder is replaced with the API Key field value.
const API_KEY = "{APIKey}";

// How long to reuse an answer for the same SEC number. 0 turns caching off. The free SECNumber
// package allows only a few calls a day, so a long cache saves calls.
const CACHE_MILLISECONDS = 30 * 24 * 60 * 60 * 1000;

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

// Accepts "A199600179", "a1996-00179", "CS 2019 12345". Returns the number in capitals without
// spaces or dashes, or null when it doesn't look like an SEC registration number (up to 4
// letters followed by 5 to 12 digits).
function parseSecNumber(raw) {
  const text = raw.toUpperCase().replace(/[\s.\-/]/g, "");
  return /^[A-Z]{0,4}\d{5,12}$/.test(text) ? text : null;
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
  const us = /^(\d{1,2})\/(\d{1,2})\/(\d{4})$/.exec(text);
  if (us) {
    return `${us[3]}-${us[1].padStart(2, "0")}-${us[2].padStart(2, "0")}`;
  }
  return text;
}

function credentials() {
  const value = clean(API_KEY) || "";
  const separator = value.indexOf(":");
  if (separator > 0) {
    return { consumerKey: value.substring(0, separator), consumerSecret: value.substring(separator + 1) };
  }
  return value ? { accessToken: value } : null;
}

// Gets an access token with the OAuth2 client credentials grant.
function requestToken(creds) {
  const tokenResponse = http.send({
    url: TOKEN_URL,
    method: "POST",
    headers: [
      { Key: "Content-Type", Value: "application/x-www-form-urlencoded" },
      { Key: "Accept", Value: "application/json" },
    ],
    body:
      "grant_type=client_credentials" +
      `&client_id=${encodeURIComponent(creds.consumerKey)}` +
      `&client_secret=${encodeURIComponent(creds.consumerSecret)}` +
      "&scope=openid",
  });

  const status = String(tokenResponse.HttpStatus || "");
  const body = parseJson(tokenResponse.Content);

  if (status === "TooManyRequests") {
    throw new Error("TooManyRequests - the SEC token endpoint is busy, the record will be retried");
  }

  if (status !== "OK" || !body || !body.access_token) {
    const reason = body && (body.error_description || body.error) ? `${body.error || ""} ${body.error_description || ""}`.trim() : `HTTP ${status}`;
    // A 403 HTML page (rather than a JSON error) means the service is unavailable, not that
    // the credentials are wrong.
    if (status === "BadRequest" || status === "Unauthorized" || (status === "Forbidden" && body)) {
      throw new Error(`The SEC token endpoint rejected the consumer key and secret in the API Key field (${reason}).`);
    }
    log(`Could not get an SEC access token. ${reason}. ${String(tokenResponse.Content || "").substring(0, 200)}`);
    return null;
  }

  return { accessToken: String(body.access_token), expiresIn: Number(body.expires_in) || 3600 };
}

// Returns an access token, from the cache when there's one that hasn't expired.
function getAccessToken(creds, forceNew) {
  if (creds.accessToken) {
    return creds.accessToken;
  }

  const cacheKey = `secph:token:${creds.consumerKey}`;
  if (!forceNew) {
    const cached = cache.get(cacheKey);
    if (cached) {
      return String(cached);
    }
  }

  const token = requestToken(creds);
  if (!token) {
    return null;
  }
  // Reuse the token until 5 minutes before it expires (at least 1 minute).
  const lifetime = Math.max(60, token.expiresIn - 300) * 1000;
  if (!forceNew) {
    cache.set(cacheKey, token.accessToken, lifetime);
  }
  return token.accessToken;
}

function callApi(secNumber, accessToken) {
  return http.send({
    url: `${SEC_URL}?sec_no=${encodeURIComponent(secNumber)}`,
    method: "GET",
    headers: [
      { Key: "Authorization", Value: `Bearer ${accessToken}` },
      { Key: "Accept", Value: "application/json" },
    ],
  });
}

// Calls the SECNumber API. Returns the company, or null when there's no answer to store.
function lookUp(secNumber, creds) {
  const accessToken = getAccessToken(creds, false);
  if (!accessToken) {
    return null;
  }

  let apiResponse = callApi(secNumber, accessToken);
  let status = String(apiResponse.HttpStatus || "");

  // A cached token can stop working before it expires (for example when the keys are
  // regenerated). Try once more with a new token.
  if (status === "Unauthorized" && !creds.accessToken) {
    const newToken = getAccessToken(creds, true);
    if (!newToken) {
      return null;
    }
    apiResponse = callApi(secNumber, newToken);
    status = String(apiResponse.HttpStatus || "");
  }

  const body = parseJson(apiResponse.Content);

  if (status === "TooManyRequests") {
    throw new Error("TooManyRequests - the SEC API is busy or the daily call limit was reached, the record will be retried");
  }

  // 401 is a missing, expired or wrong token. A 403 with a JSON body is a token that isn't
  // subscribed to the SECNumber API. (A 403 HTML page means the service is unavailable.)
  if (status === "Unauthorized" || (status === "Forbidden" && body)) {
    const message = body && body.description ? body.description : String(apiResponse.Content || "").substring(0, 200);
    throw new Error(`The SEC API rejected the credentials in the API Key field (HTTP ${status}). ${message}`);
  }

  if (status === "OK" && body) {
    const items = Array.isArray(body.data) ? body.data : Array.isArray(body) ? body : [];
    for (let i = 0; i < items.length; i++) {
      if (items[i] && parseSecNumber(String(items[i].sec_no || "")) === secNumber) {
        return items[i];
      }
    }
    if (items.length === 1 && items[0] && !items[0].sec_no) {
      return items[0];
    }
  }

  log(`The SEC API could not look up ${secNumber}. HTTP ${status}. ${String(apiResponse.Content || "").substring(0, 200)}`);
  return null;
}

function run() {
  const secNumber = parseSecNumber(getValue(SEC_NUMBER_KEY));
  if (!secNumber) {
    // No valid SEC number on this record (this is also what Test connection hits, because it
    // passes placeholder values instead of real ones).
    return [];
  }

  const creds = credentials();
  if (!creds) {
    log("The SEC API needs credentials. Enter consumerKey:consumerSecret (or an access token) in the enricher's API Key field.");
    return [];
  }

  const cacheKey = `secph:${secNumber}`;
  const cached = CACHE_MILLISECONDS > 0 ? cache.get(cacheKey) : null;
  let item = cached ? parseJson(String(cached)) : null;

  if (!item) {
    item = lookUp(secNumber, creds);
    if (!item) {
      return [];
    }
    if (CACHE_MILLISECONDS > 0) {
      cache.set(cacheKey, JSON.stringify(item), CACHE_MILLISECONDS);
    }
  }

  const data = {
    "secph.secNumber": clean(item.sec_no) || secNumber,
    "secph.name": clean(item.company_name),
    "secph.dateApproved": formatDate(item.date_approved),
    "secph.status": clean(item.status),
    "secph.licenses": clean(item.licenses),
  };

  // Leave out values the SEC didn't return, so they don't overwrite existing data with blanks.
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
