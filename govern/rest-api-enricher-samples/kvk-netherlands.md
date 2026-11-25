---
title: KVK (Netherlands)
url: https://documentation.cluedin.net/govern/rest-api-enricher-samples/kvk-netherlands
content_type: reference
section: Govern & improve > REST API enricher samples
---

# KVK (Netherlands)

> reference: Facts, options, APIs.

This example looks up an organization's KVK number (Chamber of Commerce number) in the Dutch Business Register (Handelsregister) by using the [KVK Basisprofiel API](https://developers.kvk.nl/documentation/basisprofiel-api). For each golden record it stores the registered name, statutory name, trade names, legal form, RSIN, registration and start dates, number of employees, main SBI activity, and the address of the main establishment.

**Enricher version:** V2  
**API key:** your KVK API key (a paid subscription from [KVK](https://developers.kvk.nl/); KVK also has a free test environment with a public test key)

To set up the enricher, see [Add REST API enricher](https://documentation.cluedin.net/govern/enrichment/rest-api.md#add-rest-api-enricher), then use the settings and script on this page.

## Settings

- **Accepted Business Domain** – `/Organization`, or the business domain that holds your companies.

- **Version** – V2 (recommended).

- **API Key** – your KVK API key. The script sends it in the `apikey` header. If the field is empty, the script adds nothing and doesn't call KVK.

- **Filters** – we recommend a rule that only accepts golden records where `organization.kvkNumber` has a value. Otherwise, every record without a KVK number is listed on the enricher's **Logs** tab as having returned no results.

## Vocabulary and Properties

```
organization.kvkNumber
```

`organization.kvkNumber` holds the 8-digit KVK number. If your data uses another vocabulary key, change this field and the `KVK_NUMBER_KEY` value at the top of the script.

## Request and response

**Base URL:** `https://api.kvk.nl/api/v1`  
**Endpoint:** `GET /basisprofielen/{kvkNumber}`  
**Authentication:** API key in the `apikey` request header

The script sends one request per golden record:

```http
GET https://api.kvk.nl/api/v1/basisprofielen/68750110
apikey: <your KVK API key>
Accept: application/json
```

Shortened response (from KVK's test environment):

```json
{
  "kvkNummer": "68750110",
  "naam": "Test BV Donald",
  "formeleRegistratiedatum": "20170519",
  "materieleRegistratie": { "datumAanvang": "20170519" },
  "totaalWerkzamePersonen": 1,
  "statutaireNaam": "Test BV Donald",
  "handelsnamen": [
    { "naam": "Test BV Donald", "volgorde": 0 },
    { "naam": "Test BV Donald Nevenvestiging", "volgorde": 1 }
  ],
  "sbiActiviteiten": [
    { "sbiCode": "01241", "sbiOmschrijving": "Teelt van appels en peren", "indHoofdactiviteit": "Ja" }
  ],
  "_embedded": {
    "eigenaar": { "rsin": "857587973", "rechtsvorm": "Besloten vennootschap" },
    "hoofdvestiging": {
      "vestigingsnummer": "000037178598",
      "adressen": [
        { "type": "correspondentieadres", "volledigAdres": "Postbus 200                                 1000AE Rommeldam", "postcode": "1000AE", "plaats": "Rommeldam" },
        { "type": "bezoekadres", "volledigAdres": "Hizzaarderlaan 3 A                                 8823SJ Lollum", "postcode": "8823SJ", "plaats": "Lollum" }
      ]
    }
  }
}
```

## Properties added by the enricher

| Property | Response field | Example |
| -------- | -------------- | ------- |
| `kvk.kvkNumber` | `kvkNummer` | `68750110` |
| `kvk.name` | `naam` | `Test BV Donald` |
| `kvk.statutoryName` | `statutaireNaam` | `Test BV Donald` |
| `kvk.tradeNames` | `handelsnamen[].naam`, separated by `; ` | `Test BV Donald; Test BV Donald Nevenvestiging` |
| `kvk.legalForm` | `_embedded.eigenaar.rechtsvorm` | `Besloten vennootschap` |
| `kvk.rsin` | `_embedded.eigenaar.rsin` | `857587973` |
| `kvk.registrationDate` | `formeleRegistratiedatum`, as `YYYY-MM-DD` | `2017-05-19` |
| `kvk.startDate` | `materieleRegistratie.datumAanvang`, as `YYYY-MM-DD` | `2017-05-19` |
| `kvk.employees` | `totaalWerkzamePersonen` | `1` |
| `kvk.mainActivityCode` | `sbiActiviteiten[].sbiCode` where `indHoofdactiviteit` is `Ja` | `01241` |
| `kvk.mainActivity` | `sbiActiviteiten[].sbiOmschrijving` of the main activity (in Dutch) | `Teelt van appels en peren` |
| `kvk.establishmentNumber` | `_embedded.hoofdvestiging.vestigingsnummer` | `000037178598` |
| `kvk.visitingAddress` | `volledigAdres` of the `bezoekadres` address, on one line | `Hizzaarderlaan 3 A, 8823SJ Lollum` |
| `kvk.postalAddress` | `volledigAdres` of the `correspondentieadres` address, on one line | `Postbus 200, 1000AE Rommeldam` |
| `kvk.city` | `plaats` of the visiting address | `Lollum` |
| `kvk.postalCode` | `postcode` of the visiting address | `8823SJ` |
| `kvk.website` | first entry of `_embedded.hoofdvestiging.websites` | `www.example.nl` |

A property is added only when KVK returns a value for it. A date with an unknown month or day (`00`) isn't added.

If the enricher has a **Preview** tab, the results appear there first. To add them to golden records, go to the **Map** tab, select **Map Data**, and choose **Auto Mapping**. Select the business domain, enter a new vocabulary named `KVK` with the key prefix `kvk`, and then create the mapping. Auto mapping also uses `name` as the golden record name, so remove that from the mapping if you want to keep your existing names. Then process the data on the **Process** tab. If the enricher has no **Preview** tab, the properties are added to the golden record as soon as it is enriched.

## How the script handles input and errors

- Spaces, dots, and a leading `KVK` are removed, so `KVK 6875 0110` is looked up as `68750110`. A 7-digit number that lost its leading zero is padded to 8 digits. Golden records without a valid KVK number are skipped without calling KVK.

- If the KVK number isn't registered (HTTP 404, error `IPD0005`), the request is invalid (HTTP 400), or KVK returns another error, the script logs the reason and adds nothing.

- If KVK rejects the API key (HTTP 401 or 403), the script throws an error, so the golden record is listed on the **Logs** tab with a message to check the **API Key** field.

- If KVK reports that it is too busy (HTTP 429), the script throws an error that makes the enricher try the golden record again later.

- Successful results are cached for 24 hours per KVK number. To change this, edit `CACHE_MILLISECONDS` in the script.

## Testing the enricher

- **Test connection** checks only that the script runs. It doesn't call KVK.

- To try the setup without a paid subscription, temporarily change `KVK_URL` in the script to `https://api.kvk.nl/test/api/v1/basisprofielen/` and enter KVK's public test API key, `l7xx1f2691f2520d487b902f4e0b57a0b197`, in the **API Key** field. The test environment returns fictitious companies; for example, the KVK number `68750110` returns `Test BV Donald`.

## Limitations

- KVK charges for API use. Check your subscription before you enrich a large number of golden records, and keep the cache on.

- Only the main establishment (`hoofdvestiging`) is used. Other establishments (`vestigingen`) aren't added.

- SBI activity descriptions are in Dutch.

- Addresses that the owner has shielded (`indAfgeschermd`) may not be returned in full.

## Process script

```javascript
// REST API enricher (V2) - Dutch company lookup with the KVK Basisprofiel API
//
// Looks up a golden record's KVK number (Chamber of Commerce number) in the Dutch Business
// Register (Handelsregister) by using the KVK Basisprofiel API
// (https://developers.kvk.nl/documentation/basisprofiel-api), and adds the result to the golden
// record as kvk.* properties:
//
//   kvk.kvkNumber          8-digit KVK number that was looked up
//   kvk.name               name (naam)
//   kvk.statutoryName      statutory name (statutaireNaam)
//   kvk.tradeNames         all trade names, separated by "; "
//   kvk.legalForm          legal form, for example Besloten vennootschap
//   kvk.rsin               RSIN (legal entities and partnerships identification number)
//   kvk.registrationDate   date of formal registration (YYYY-MM-DD)
//   kvk.startDate          date the business started (YYYY-MM-DD)
//   kvk.employees          total number of people working for the business
//   kvk.mainActivityCode   SBI code of the main activity, for example 01241
//   kvk.mainActivity       description of the main activity (Dutch)
//   kvk.establishmentNumber establishment number (vestigingsnummer) of the main establishment
//   kvk.visitingAddress    visiting address of the main establishment on one line
//   kvk.postalAddress      postal address of the main establishment on one line
//   kvk.city               city of the visiting address
//   kvk.postalCode         postal code of the visiting address
//   kvk.website            first website of the main establishment
//
// Needs a KVK API key, entered in the enricher's API Key field. See README.md next to this
// file for the enricher settings.
//
// A record gets no result (nothing is stored) when it has no valid KVK number, when the
// number isn't registered, or when the API can't answer.

// ---- Settings -------------------------------------------------------------------------

// Vocabulary key to read. Add the same key to the Vocabulary and Properties field.
const KVK_NUMBER_KEY = "organization.kvkNumber";

// Use https://api.kvk.nl/test/api/v1/basisprofielen/ (with KVK's public test API key) to try
// the setup against KVK's test data first.
const KVK_URL = "https://api.kvk.nl/api/v1/basisprofielen/";

// The {APIKey} placeholder is replaced with the API Key field value.
const API_KEY = "{APIKey}";

// How long to reuse an answer for the same KVK number. 0 turns caching off.
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

// Accepts "6875 0110", "68.75.01.10", "KVK 68750110", and numbers that lost their leading zero
// (for example 1234567). Returns the 8 digits, or null when it isn't a KVK number.
function parseKvkNumber(raw) {
  const text = raw.toUpperCase().replace(/^KVK/, "");
  if (/[A-Z]/.test(text)) {
    return null;
  }
  const digits = text.replace(/[^0-9]/g, "");
  if (digits.length < 7 || digits.length > 8) {
    return null;
  }
  return digits.length === 7 ? "0" + digits : digits;
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

// KVK dates are YYYYMMDD. Returns YYYY-MM-DD, or null for a missing or partial date (KVK uses
// 00 for an unknown month or day).
function toDate(value) {
  const text = clean(value);
  if (!text || !/^\d{8}$/.test(text) || text.substring(4, 6) === "00" || text.substring(6, 8) === "00") {
    return null;
  }
  return `${text.substring(0, 4)}-${text.substring(4, 6)}-${text.substring(6, 8)}`;
}

// volledigAdres separates the street line from the postcode and city with a run of spaces.
// Returns it on one line, for example "Hizzaarderlaan 3 A, 8823SJ Lollum".
function formatAddress(value) {
  if (value === null || value === undefined) {
    return null;
  }
  return clean(String(value).trim().replace(/\s{2,}/g, ", "));
}

function findAddress(addresses, type) {
  const list = Array.isArray(addresses) ? addresses : [];
  for (let i = 0; i < list.length; i++) {
    if (list[i] && list[i].type === type) {
      return list[i];
    }
  }
  return null;
}

function getErrors(body) {
  const errors = body && Array.isArray(body.fout) ? body.fout : [];
  return errors.map((x) => x && `${x.code}: ${x.omschrijving}`).filter((x) => !!x);
}

// Calls the API. Returns the basic profile, or null when there's no answer to store.
function lookUp(kvkNumber) {
  const apiResponse = http.send({
    url: KVK_URL + kvkNumber,
    method: "GET",
    headers: [
      { Key: "apikey", Value: API_KEY },
      { Key: "Accept", Value: "application/json" },
    ],
  });

  const status = String(apiResponse.HttpStatus || "");
  const body = parseJson(apiResponse.Content);

  if (status === "TooManyRequests") {
    throw new Error("TooManyRequests - the KVK API is busy, the record will be retried");
  }

  if (status === "Unauthorized" || status === "Forbidden") {
    throw new Error(`The KVK API rejected the API key (HTTP ${status}). Check the API Key field of the enricher.`);
  }

  if (status === "OK" && body && body.kvkNummer) {
    return body;
  }

  log(`KVK could not look up ${kvkNumber}. HTTP ${status}. ${getErrors(body).join(", ") || String(apiResponse.Content || "").substring(0, 200)}`);
  return null;
}

function run() {
  const kvkNumber = parseKvkNumber(getValue(KVK_NUMBER_KEY));
  if (!kvkNumber) {
    // No valid KVK number on this record (this is also what Test connection hits, because it
    // passes placeholder values instead of real ones).
    return [];
  }

  if (!API_KEY) {
    log("No KVK API key. Enter it in the API Key field of the enricher.");
    return [];
  }

  const cacheKey = `kvk:${kvkNumber}`;
  const cached = CACHE_MILLISECONDS > 0 ? cache.get(cacheKey) : null;
  let profile = cached ? parseJson(String(cached)) : null;

  if (!profile) {
    profile = lookUp(kvkNumber);
    if (!profile) {
      return [];
    }
    if (CACHE_MILLISECONDS > 0) {
      cache.set(cacheKey, JSON.stringify(profile), CACHE_MILLISECONDS);
    }
  }

  const embedded = profile._embedded || {};
  const owner = embedded.eigenaar || {};
  const mainEstablishment = embedded.hoofdvestiging || {};

  const tradeNames = (Array.isArray(profile.handelsnamen) ? profile.handelsnamen : [])
    .map((x) => x && clean(x.naam))
    .filter((x) => !!x);

  const activities = Array.isArray(profile.sbiActiviteiten) ? profile.sbiActiviteiten : [];
  let mainActivity = null;
  for (let i = 0; i < activities.length; i++) {
    if (activities[i] && activities[i].indHoofdactiviteit === "Ja") {
      mainActivity = activities[i];
      break;
    }
  }
  mainActivity = mainActivity || {};

  const visitingAddress = findAddress(mainEstablishment.adressen, "bezoekadres") || {};
  const postalAddress = findAddress(mainEstablishment.adressen, "correspondentieadres") || {};
  const websites = Array.isArray(mainEstablishment.websites) ? mainEstablishment.websites : [];

  const data = {
    "kvk.kvkNumber": clean(profile.kvkNummer),
    "kvk.name": clean(profile.naam),
    "kvk.statutoryName": clean(profile.statutaireNaam),
    "kvk.tradeNames": tradeNames.length > 0 ? tradeNames.join("; ") : null,
    "kvk.legalForm": clean(owner.rechtsvorm),
    "kvk.rsin": clean(owner.rsin),
    "kvk.registrationDate": toDate(profile.formeleRegistratiedatum),
    "kvk.startDate": toDate(profile.materieleRegistratie && profile.materieleRegistratie.datumAanvang),
    "kvk.employees": typeof profile.totaalWerkzamePersonen === "number" ? profile.totaalWerkzamePersonen : null,
    "kvk.mainActivityCode": clean(mainActivity.sbiCode),
    "kvk.mainActivity": clean(mainActivity.sbiOmschrijving),
    "kvk.establishmentNumber": clean(mainEstablishment.vestigingsnummer),
    "kvk.visitingAddress": formatAddress(visitingAddress.volledigAdres),
    "kvk.postalAddress": formatAddress(postalAddress.volledigAdres),
    "kvk.city": clean(visitingAddress.plaats),
    "kvk.postalCode": clean(visitingAddress.postcode),
    "kvk.website": websites.length > 0 ? clean(websites[0]) : null,
  };

  // Leave out values KVK didn't return, so they don't overwrite existing data with blanks.
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
