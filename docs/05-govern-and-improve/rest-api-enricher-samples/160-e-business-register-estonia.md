---
layout: cluedin
title: e-Business Register (Estonia)
parent: REST API enricher samples
grand_parent: Govern & improve
nav_order: 160
permalink: /govern/rest-api-enricher-samples/e-business-register-estonia
content_type: reference
summary: "Looks up Estonian registry codes in the e-Business Register's free public company search and adds the registered name, status and legal address. V2 script; no API key."
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

This example looks up an organization's Estonian registry code (registrikood) in the [e-Business Register](https://ariregister.rik.ee/eng) (Äriregister), run by the Centre of Registers and Information Systems (RIK). For each golden record it stores the registered name, status, legal address, legal form code, previous names, and a link to the company's page in the register. No API key is needed.

The script uses the register's free public company search service (`/api/autocomplete`), the same service that powers the search box on the register's website. It returns basic data only. The register's full data (financial year reports, board members, shareholders, and so on) is available through the paid e-Business Register API (XML/SOAP), which needs a contract with RIK and a different script.

**Enricher version:** V2  
**API key:** not needed

To set up the enricher, see [Add REST API enricher](/govern/enrichment/rest-api#add-rest-api-enricher), then use the settings and script on this page.

## Settings

- **Accepted Business Domain** – `/Organization`, or the business domain that holds your companies.

- **Version** – V2 (recommended).

- **API Key** – leave empty.

- **Filters** – we recommend a rule that only accepts golden records where `organization.registryCode` has a value. Otherwise, every record without a registry code is listed on the enricher's **Logs** tab as having returned no results.

## Vocabulary and Properties

```
organization.registryCode
```

`organization.registryCode` holds the 8-digit registry code. If your data uses another vocabulary key, change this field and the `REGISTRY_CODE_KEY` value at the top of the script.

## Request and response

**Base URL:** `https://ariregister.rik.ee/eng/api`  
**Endpoint:** `GET /autocomplete?q={registryCode}`  
**Authentication:** none

The script sends one request per golden record:

```http
GET https://ariregister.rik.ee/eng/api/autocomplete?q=10137319
Accept: application/json
```

Response:

```json
{
  "status": "OK",
  "data": [
    {
      "company_id": 2000004900,
      "reg_code": 10137319,
      "name": "aktsiaselts TALLINNA SADAM",
      "historical_names": [],
      "status": "R",
      "legal_address": "Harju maakond, Tallinn, Kesklinna linnaosa, Sadama tn 25",
      "zip_code": "15051",
      "legal_form": "1",
      "url": "https://ariregister.rik.ee/eng/company/10137319/aktsiaselts-TALLINNA-SADAM"
    }
  ]
}
```

The search also matches company names, so the response can list more than one company. The script uses the one whose `reg_code` is the registry code it sent.

## Properties added by the enricher

| Property | Response field | Example |
| -------- | -------------- | ------- |
| `ariregister.registryCode` | `reg_code` | `10137319` |
| `ariregister.name` | `name` | `aktsiaselts TALLINNA SADAM` |
| `ariregister.statusCode` | `status` | `R` |
| `ariregister.status` | `status`, in English: `R` is `Registered`, `L` is `In liquidation` | `Registered` |
| `ariregister.legalAddress` | `legal_address` | `Harju maakond, Tallinn, Kesklinna linnaosa, Sadama tn 25` |
| `ariregister.postalCode` | `zip_code` | `15051` |
| `ariregister.legalFormCode` | `legal_form` (the register's own code) | `1` |
| `ariregister.previousNames` | `historical_names`, separated by `; ` | `Grematamera UÜ` |
| `ariregister.url` | `url` | `https://ariregister.rik.ee/eng/company/10137319/aktsiaselts-TALLINNA-SADAM` |

A property is added only when the register returns a value for it. Only the status codes `R` and `L` have been confirmed against the register's pages, so only those get an English `ariregister.status`. Any other status code is stored in `ariregister.statusCode` only. To add a name for another code, add it to `STATUS_NAMES` at the top of the script.

If the enricher has a **Preview** tab, the results appear there first. To add them to golden records, go to the **Map** tab, select **Map Data**, and choose **Auto Mapping**. Select the business domain, enter a new vocabulary named `Ariregister` with the key prefix `ariregister`, and then create the mapping. Auto mapping also uses `name` as the golden record name, so remove that from the mapping if you want to keep your existing names. Then process the data on the **Process** tab. If the enricher has no **Preview** tab, the properties are added to the golden record as soon as it is enriched.

## How the script handles input and errors

- Spaces, dots, dashes, and a leading `EE` are removed, so `EE 10137319` is looked up as `10137319`. The code must have 8 digits. Golden records without a valid registry code are skipped without calling the service.

- If no company has the registry code, or the service returns an error, the script logs the reason and adds nothing.

- The service limits how often it can be called. When it does, it answers HTTP 429, and the script throws an error that makes the enricher try the golden record again later.

- Successful results are cached for 24 hours per registry code. To change this, edit `CACHE_MILLISECONDS` in the script.

## Testing the enricher

- **Test connection** checks only that the script runs. It doesn't call the service.

- To try the setup, create a golden record with `organization.registryCode` set to `10137319` (AS Tallinna Sadam).

## Limitations

- This is the register's public search service, not a contracted API. It has no documented service level, and it rate-limits clients that send many requests in a short time. For large volumes, use the paid e-Business Register API or the register's free [open data files](https://avaandmed.ariregister.rik.ee/en).

- Companies that have been deleted from the register aren't returned.

- Only basic data is returned: no board members, shareholders, activity codes, or financial data.

- The legal form is a code. The register doesn't publish its meaning in the search response.

## Process script

```javascript
// REST API enricher (V2) - Estonian company lookup with the e-Business Register
//
// Looks up a golden record's Estonian registry code in the e-Business Register (Äriregister),
// using the register's free public company search service
// (https://ariregister.rik.ee/eng/api/autocomplete), and adds the result to the golden record
// as ariregister.* properties:
//
//   ariregister.registryCode    8-digit registry code that was looked up
//   ariregister.name            registered name
//   ariregister.statusCode      status code, for example R (registered) or L (in liquidation)
//   ariregister.status          status in English, for the codes listed in STATUS_NAMES
//   ariregister.legalAddress    legal address on one line
//   ariregister.postalCode      postal code of the legal address
//   ariregister.legalFormCode   the register's legal form code, for example 1 or 5
//   ariregister.previousNames   previous names, separated by "; "
//   ariregister.url             link to the company's page in the e-Business Register
//
// No API key is needed. See README.md next to this file for the enricher settings.
//
// A record gets no result (nothing is stored) when it has no valid registry code, when the
// code isn't found (deleted companies aren't returned), or when the service can't answer.

// ---- Settings -------------------------------------------------------------------------

// Vocabulary key to read. Add the same key to the Vocabulary and Properties field.
const REGISTRY_CODE_KEY = "organization.registryCode";

// "eng" returns links to the English pages of the register. Use "est" for Estonian.
const ARIREGISTER_URL = "https://ariregister.rik.ee/eng/api/autocomplete";

// How long to reuse an answer for the same registry code. 0 turns caching off.
const CACHE_MILLISECONDS = 24 * 60 * 60 * 1000;

// Status codes with an English name. Other codes are stored in ariregister.statusCode only.
const STATUS_NAMES = {
  R: "Registered",
  L: "In liquidation",
};

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

// Accepts "10137319", "10 137 319", "EE10137319" (with an Estonian prefix), etc. Returns the 8
// digits, or null when the value isn't an 8-digit code.
function parseRegistryCode(raw) {
  const digits = raw.toUpperCase().replace(/^EE/, "").replace(/[\s.\-]/g, "");
  return /^\d{8}$/.test(digits) ? digits : null;
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

// Calls the service. Returns the company whose registry code matches, or null when there's
// no answer to store.
function lookUp(registryCode) {
  const apiResponse = http.send({
    url: `${ARIREGISTER_URL}?q=${encodeURIComponent(registryCode)}`,
    method: "GET",
    headers: [{ Key: "Accept", Value: "application/json" }],
  });

  const status = String(apiResponse.HttpStatus || "");
  const body = parseJson(apiResponse.Content);

  if (status === "TooManyRequests") {
    throw new Error("TooManyRequests - the e-Business Register is busy, the record will be retried");
  }

  if (status === "OK" && body && Array.isArray(body.data)) {
    // The search also matches names, so pick the company whose registry code is the one we sent.
    for (let i = 0; i < body.data.length; i++) {
      if (body.data[i] && String(body.data[i].reg_code) === registryCode) {
        return body.data[i];
      }
    }
    log(`e-Business Register found no company with registry code ${registryCode}.`);
    return null;
  }

  log(`e-Business Register could not look up ${registryCode}. HTTP ${status}. ${String(apiResponse.Content || "").substring(0, 200)}`);
  return null;
}

function run() {
  const registryCode = parseRegistryCode(getValue(REGISTRY_CODE_KEY));
  if (!registryCode) {
    // No valid registry code on this record (this is also what Test connection hits, because
    // it passes placeholder values instead of real ones).
    return [];
  }

  const cacheKey = `ariregister:${registryCode}`;
  const cached = CACHE_MILLISECONDS > 0 ? cache.get(cacheKey) : null;
  let company = cached ? parseJson(String(cached)) : null;

  if (!company) {
    company = lookUp(registryCode);
    if (!company) {
      return [];
    }
    if (CACHE_MILLISECONDS > 0) {
      cache.set(cacheKey, JSON.stringify(company), CACHE_MILLISECONDS);
    }
  }

  const statusCode = clean(company.status);
  const previousNames = Array.isArray(company.historical_names)
    ? company.historical_names.map((x) => clean(x)).filter((x) => !!x)
    : [];

  const data = {
    "ariregister.registryCode": clean(company.reg_code),
    "ariregister.name": clean(company.name),
    "ariregister.statusCode": statusCode,
    "ariregister.status": statusCode && STATUS_NAMES[statusCode] ? STATUS_NAMES[statusCode] : null,
    "ariregister.legalAddress": clean(company.legal_address),
    "ariregister.postalCode": clean(company.zip_code),
    "ariregister.legalFormCode": clean(company.legal_form),
    "ariregister.previousNames": previousNames.length > 0 ? previousNames.join("; ") : null,
    "ariregister.url": clean(company.url),
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
