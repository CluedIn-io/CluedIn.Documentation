---
title: VIES (EU VAT validation)
url: https://documentation.cluedin.net/govern/rest-api-enricher-samples/vies
content_type: reference
section: Govern & improve > REST API enricher samples
---

# VIES (EU VAT validation)

> reference: Facts, options, APIs.

This example checks an organization's EU VAT number against the European Commission's [VIES](https://ec.europa.eu/taxation_customs/vies/) service by using its official JSON REST API. For each golden record it stores whether the number is valid, together with the registered trader name and address. No API key is needed.

**Enricher version:** V2  
**API key:** not needed

To set up the enricher, see [Add REST API enricher](https://documentation.cluedin.net/govern/enrichment/rest-api.md#add-rest-api-enricher), then use the settings and script on this page.

## Settings

- **Accepted Business Domain** – `/Organization`, or the business domain that holds your companies.

- **Version** – V2 (recommended).

- **API Key** – leave empty.

- **Filters** – we recommend a rule that only accepts golden records where `organization.vat` has a value. Otherwise, every record without a VAT number is listed on the enricher's **Logs** tab as having returned no results.

## Vocabulary and Properties

```
organization.vat
organization.address.countryCode
```

`organization.vat` holds the VAT number. `organization.address.countryCode` is optional. It is used only when the VAT number has no country prefix, and must contain a 2-letter country code. If your data uses other vocabulary keys, change this field and the `VAT_NUMBER_KEY` and `COUNTRY_CODE_KEY` values at the top of the script.

## Properties added by the enricher

| Property | Example | Description |
| -------- | ------- | ----------- |
| `vies.valid` | `True` | `True` if VIES reports the VAT number as valid, otherwise `False`. |
| `vies.name` | `GOOGLE IRELAND LIMITED` | Registered trader name. Not added when the member state doesn't share it. |
| `vies.address` | `3RD FLOOR, GORDON HOUSE, BARROW STREET, DUBLIN 4` | Registered trader address on one line. Not added when the member state doesn't share it. |
| `vies.countryCode` | `IE` | Country code that was checked. VIES uses `EL` for Greece and `XI` for Northern Ireland. |
| `vies.vatNumber` | `6388047V` | VAT number that was checked, without the country prefix. |
| `vies.requestDate` | `2026-11-24` | Date when VIES checked the number. |

Where the results go depends on the enricher's **Enable Mapping** setting. It is on by default, and can't be changed after the enricher is created.

- **Enable Mapping on** – the results first appear on the enricher's **Preview** tab, and you map and process them before they're added to golden records (see below).

- **Enable Mapping off** – the `vies.*` properties are added to the golden records directly.

With **Enable Mapping** on, the results look like this on the **Preview** tab:

![Preview tab of the REST API enricher showing VIES results for four companies, with valid, countryCode, vatNumber, requestDate, name, and address columns](https://documentation.cluedin.net/assets/images/preparation/enricher/rest-api-vies-1.png)

To add them to golden records, go to the enricher's **Map** tab, select **Map Data**, and choose **Auto Mapping**. Select the business domain, enter a new vocabulary named `VIES` with the key prefix `vies`, and then create the mapping. Auto mapping also uses `name` as the golden record name, so remove that from the mapping if you want to keep your existing names. Then process the data on the **Process** tab.

![Properties page of the Google Ireland golden record showing the vies.address, vies.countryCode, vies.name, vies.requestDate, vies.valid, and vies.vatNumber properties added by the REST API enricher](https://documentation.cluedin.net/assets/images/preparation/enricher/rest-api-vies-2.png)

## How the script handles input and errors

- Spaces, dots, and dashes are removed from the VAT number, so `ie 6388047-v` is checked as country `IE`, number `6388047V`. A leading `GR` is changed to `EL`, which is the code VIES uses for Greece.

- Golden records without a VAT number, or with a non-EU one (for example, `GB` or `US`), are skipped without calling VIES.

- If VIES can't check a number (for example, because the member state's service is unavailable or the request times out), the script adds nothing. A temporary outage is never stored as `vies.valid` = `False`.

- If VIES reports that it is too busy, the script throws an error that makes the enricher try the golden record again later.

- Successful results are cached for 24 hours per VAT number, so the same number isn't checked repeatedly. To change this, edit `CACHE_MILLISECONDS` in the script.

## Testing the enricher

- **Test connection** checks only that the script runs. It doesn't call VIES.

- To try the setup with VIES test data, temporarily change `VIES_URL` in the script to `https://ec.europa.eu/taxation_customs/vies/rest-api/check-vat-test-service`. For example, the VAT number `DE100` returns a valid result.

## Limitations

- VIES only confirms that a VAT number is registered for trade within the EU (including Northern Ireland). It doesn't validate other tax IDs or VAT numbers from outside the EU.

- VIES relies on each member state's own system. A check usually takes a few seconds, and a member state can be temporarily unavailable.

- Some member states, such as Germany, don't return the trader name or address.

- Matching the trader name and address, and requesting a consultation number, aren't supported.

## Process script

```javascript
// REST API enricher (V2) - EU VAT number validation with VIES
//
// Checks a golden record's EU VAT number against the European Commission's VIES
// service (https://ec.europa.eu/taxation_customs/vies/) using its official JSON
// REST API, and adds the result to the golden record as vies.* properties:
//
//   vies.valid        "True" / "False" - whether VIES reports the number as valid
//   vies.name         registered trader name (when the member state returns it)
//   vies.address      registered trader address (when the member state returns it)
//   vies.countryCode  country code that was checked (EL for Greece, XI for Northern Ireland)
//   vies.vatNumber    VAT number that was checked, without the country prefix
//   vies.requestDate  date VIES answered the check (YYYY-MM-DD)
//
// No API key is needed. See README.md next to this file for the enricher settings.
//
// A record gets no result (nothing is stored) when it has no usable EU VAT number, or
// when VIES can't give an answer (invalid input, member state unavailable, time-out,
// and so on). This keeps an outage from being stored as vies.valid = False.

// ---- Settings -------------------------------------------------------------------------

// Vocabulary keys to read. Add the same keys to the Vocabulary and Properties field.
const VAT_NUMBER_KEY = "organization.vat";
// Optional. Only used when the VAT number has no country prefix. Must hold a 2-letter code.
const COUNTRY_CODE_KEY = "organization.address.countryCode";

// Use .../check-vat-test-service to try the setup against VIES's test data first.
const VIES_URL = "https://ec.europa.eu/taxation_customs/vies/rest-api/check-vat-number";

// How long to reuse a VIES answer for the same VAT number. 0 turns caching off.
const CACHE_MILLISECONDS = 24 * 60 * 60 * 1000;

// ---- Script ---------------------------------------------------------------------------

// Country codes VIES accepts. Greece is EL in VIES, not GR. XI is Northern Ireland.
const VIES_COUNTRY_CODES = [
  "AT", "BE", "BG", "CY", "CZ", "DE", "DK", "EE", "EL", "ES", "FI", "FR", "HR", "HU",
  "IE", "IT", "LT", "LU", "LV", "MT", "NL", "PL", "PT", "RO", "SE", "SI", "SK", "XI",
];

// VIES errors that mean "too busy, try again later". Throwing an error that mentions
// TooManyRequests makes the enricher retry the record instead of skipping it.
const VIES_RETRY_ERRORS = [
  "GLOBAL_MAX_CONCURRENT_REQ",
  "GLOBAL_MAX_CONCURRENT_REQ_TIME",
  "MS_MAX_CONCURRENT_REQ",
  "MS_MAX_CONCURRENT_REQ_TIME",
];

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

function toViesCountryCode(code) {
  const upper = String(code || "").trim().toUpperCase();
  const mapped = upper === "GR" ? "EL" : upper;
  return VIES_COUNTRY_CODES.indexOf(mapped) >= 0 ? mapped : null;
}

// Works out the VIES country code and national number from the record's values.
// Accepts "DE 123 456 789", "de123456789", "123.456.789" (with a country code key), etc.
function parseVatNumber(rawVatNumber, rawCountryCode) {
  const cleaned = rawVatNumber.toUpperCase().replace(/[^A-Z0-9]/g, "");
  if (!cleaned) {
    return null;
  }

  const prefixCountry = /^[A-Z]{2}/.test(cleaned) ? toViesCountryCode(cleaned.substring(0, 2)) : null;
  if (prefixCountry) {
    const nationalNumber = cleaned.substring(2);
    return nationalNumber ? { countryCode: prefixCountry, vatNumber: nationalNumber } : null;
  }

  const country = toViesCountryCode(rawCountryCode);
  return country ? { countryCode: country, vatNumber: cleaned } : null;
}

// VIES returns "---" when a member state doesn't share a value.
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

function getViesErrors(body) {
  const wrappers = body && Array.isArray(body.errorWrappers) ? body.errorWrappers : [];
  return wrappers.map((x) => x && x.error).filter((x) => !!x);
}

// Calls VIES. Returns the parsed answer, or null when VIES couldn't give one.
function checkVatNumber(input) {
  const viesResponse = http.send({
    url: VIES_URL,
    method: "POST",
    headers: [
      { Key: "Content-Type", Value: "application/json" },
      { Key: "Accept", Value: "application/json" },
    ],
    body: { countryCode: input.countryCode, vatNumber: input.vatNumber },
  });

  const status = String(viesResponse.HttpStatus || "");
  const body = parseJson(viesResponse.Content);
  const errors = getViesErrors(body);

  if (status === "TooManyRequests" || errors.some((x) => VIES_RETRY_ERRORS.indexOf(x) >= 0)) {
    throw new Error(`TooManyRequests - VIES is busy (${errors.join(", ") || status}), the record will be retried`);
  }

  if (status !== "OK" || !body || typeof body.valid !== "boolean" || errors.length > 0) {
    log(`VIES could not check ${input.countryCode}${input.vatNumber}. HTTP ${status}. ${errors.join(", ") || String(viesResponse.Content || "").substring(0, 200)}`);
    return null;
  }

  return body;
}

function run() {
  const input = parseVatNumber(getValue(VAT_NUMBER_KEY), getValue(COUNTRY_CODE_KEY));
  if (!input) {
    // No EU VAT number on this record (this is also what Test Connection hits, because
    // it passes placeholder values instead of real ones).
    return [];
  }

  const cacheKey = `vies:${input.countryCode}${input.vatNumber}`;
  const cached = CACHE_MILLISECONDS > 0 ? cache.get(cacheKey) : null;
  let result = cached ? parseJson(String(cached)) : null;

  if (!result) {
    result = checkVatNumber(input);
    if (!result) {
      return [];
    }
    if (CACHE_MILLISECONDS > 0) {
      cache.set(cacheKey, JSON.stringify(result), CACHE_MILLISECONDS);
    }
  }

  const data = {
    "vies.valid": result.valid,
    "vies.countryCode": clean(result.countryCode) || input.countryCode,
    "vies.vatNumber": clean(result.vatNumber) || input.vatNumber,
    // Date only (YYYY-MM-DD). A full timestamp would be turned into a date in the server's
    // own format (e.g. 11/24/2026 03:44:18) when the enricher reads the script's result.
    "vies.requestDate": clean(result.requestDate) ? String(result.requestDate).substring(0, 10) : null,
    "vies.name": clean(result.name),
    // VIES puts each address line on its own line; store it on one line.
    "vies.address": clean(String(result.address || "").trim().replace(/\s*\n\s*/g, ", ")),
  };

  // Leave out values VIES didn't return, so they don't overwrite existing data with blanks.
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
