---
title: AJPES Business Register (Slovenia)
url: https://documentation.cluedin.net/govern/rest-api-enricher-samples/ajpes-slovenia
content_type: reference
section: Govern & improve > REST API enricher samples
---

# AJPES Business Register (Slovenia)

> reference: Facts, options, APIs.

This example looks up an organization in the Slovenian Business Register (Poslovni register Slovenije, PRS) by using AJPES' [restPrsInfo REST API](https://www.ajpes.si/restPrsInfo/swagger/index.html). It looks the subject up by its registration number (matična številka), or by its tax number (davčna številka) when the golden record has no registration number. For each golden record it stores the full and short name, tax and VAT numbers, legal form, registered address, main activity, sector, size, registered capital, and foundation and registration dates.

**Enricher version:** V2  
**API key:** your AJPES portal user name and password, entered as `username:password`. The user needs the PRS web service, which AJPES sells in packages of lookups ([re-use of PRS data](https://www.ajpes.si/registri/poslovni_register/ponovna_uporaba)).

To set up the enricher, see [Add REST API enricher](https://documentation.cluedin.net/govern/enrichment/rest-api.md#add-rest-api-enricher), then use the settings and script on this page.

## Why restPrsInfo

AJPES offers the Business Register in several ways: free searches on its website, bulk files, and web services. restPrsInfo is the only one that answers one company at a time over a JSON REST API, which is what an enricher needs. It replaced the SOAP web service wsPrsInfo, which AJPES discontinued on 28 February 2026. It needs no client certificate: the AJPES user name, password and data scheme are sent in the body of each request.

## Settings

- **Accepted Business Domain** – `/Organization`, or the business domain that holds your companies.

- **Version** – V2 (recommended).

- **API Key** – your AJPES portal user name and password, separated by a colon: `username:password`. Everything after the first colon is the password. If the field is empty or has no colon, the script adds nothing and doesn't call AJPES.

- **Data scheme** – set `DATA_SCHEME` at the top of the script to the data scheme (šifra sheme) AJPES registered for your user. The scheme decides how much data you get (minimal, narrower or broader) and which package it's charged to. The default, `PRS_ON_P`, is the narrower scheme charged per lookup, as named in AJPES' documentation.

- **Filters** – we recommend a rule that only accepts golden records where `organization.registrationNumber` or `organization.taxNumber` has a value. Otherwise, every record without either is listed on the enricher's **Logs** tab as having returned no results.

## Vocabulary and Properties

```
organization.registrationNumber
organization.taxNumber
```

`organization.registrationNumber` holds the registration number (matična številka). `organization.taxNumber` holds the 8-digit tax number and is optional: it's used only when the record has no registration number. If your data uses other vocabulary keys, change this field and the `REGISTRATION_NUMBER_KEY` and `TAX_NUMBER_KEY` values at the top of the script.

## Request and response

**Base URL:** `https://www.ajpes.si/restPrsInfo` (test environment: `https://wwwa.ajpes.si/restPrsInfo`)  
**Endpoints:** `POST /get` (by registration number) and `POST /find` (search, used for the tax number)  
**Authentication:** AJPES user name, password and data scheme in the `ident` object of the request body

The API is described by its own OpenAPI specification, linked from the [Swagger page](https://www.ajpes.si/restPrsInfo/swagger/index.html), and in AJPES' [developer guide](https://www.ajpes.si/Doc/AJPES/Za_razvijalce/restPrsInfo_Opis_servisa_za_razvijalce.pdf) (in Slovenian).

With a registration number, the script sends one request per golden record:

```http
POST https://www.ajpes.si/restPrsInfo/get
Content-Type: application/json

{
  "ident": { "uporabnik": "<user name>", "geslo": "<password>", "shema": "PRS_ON_P" },
  "maticna": "5860571000",
  "izbrisan": false
}
```

Shortened response. The field names come from the API's specification; the values are illustrative, because the API couldn't be called with a real AJPES user:

```json
{
  "status": 0,
  "message": "OK",
  "payload": {
    "formatted": {
      "info": {
        "stMaticna": "5860571000",
        "stDavcna": "92719236",
        "idDDV": "SI92719236",
        "dtUstanovitev": "1991-04-02T00:00:00",
        "dtVpis": "1995-03-27T00:00:00",
        "firma": {
          "oblika": "Delniška družba",
          "velikostRS": "velika",
          "naslovF": { "ulica": "Verovškova ulica", "stHisna": "57", "sifPosta": "1000", "posta": "Ljubljana", "obcina": "Ljubljana" },
          "imeFirme": [ { "popolnoIme": "Krka, tovarna zdravil, d.d., Novo mesto", "kratkoIme": "Krka, d.d." } ]
        },
        "glavnaDejavnost": { "sifDejavnost": "21.200", "dejavnostOpis": "Proizvodnja farmacevtskih preparatov" },
        "sektor": { "sektorizacija": "Nefinančne družbe" },
        "kapital": { "vreKapital": 54732264.71, "valuta": "EUR" }
      }
    }
  }
}
```

With only a tax number, the script first calls `POST /find` with `"davcna": "92719236"` and `"maxRecords": 1`, takes the registration number (`maticna`) from the first result in `payload.formatted.prsData`, and then calls `POST /get` with it.

Errors come back with HTTP 200 and a status code in the body. These two were returned by the real service:

```json
{ "payload": { "raw": null, "formatted": null }, "status": 4099, "message": "Napaka pri avtentikaciji uporabnika. Podrobnosti: Napačno uporabniško ime ali geslo.", "timestamp": null }
```

```json
{ "payload": { "raw": null, "formatted": null }, "status": 4010, "message": "Napaka pri validaciji vhodnih podatkov! Napačna šifra storitve: 'PrsInfoOsnovni'.", "timestamp": null }
```

## Properties added by the enricher

| Property | Response field (under `payload.formatted.info`) | Example |
| -------- | ----------------------------------------------- | ------- |
| `ajpes.registrationNumber` | `stMaticna` | `5860571000` |
| `ajpes.taxNumber` | `stDavcna` | `92719236` |
| `ajpes.vatId` | `idDDV` | `SI92719236` |
| `ajpes.name` | `firma.imeFirme[0].popolnoIme` | `Krka, tovarna zdravil, d.d., Novo mesto` |
| `ajpes.shortName` | `firma.imeFirme[0].kratkoIme` | `Krka, d.d.` |
| `ajpes.legalForm` | `firma.oblika` | `Delniška družba` |
| `ajpes.address` | `firma.naslovF` (street, house number, postcode and post office on one line) | `Verovškova ulica 57, 1000 Ljubljana` |
| `ajpes.municipality` | `firma.naslovF.obcina` | `Ljubljana` |
| `ajpes.mainActivityCode` | `glavnaDejavnost.sifDejavnost` (SKD) | `21.200` |
| `ajpes.mainActivity` | `glavnaDejavnost.dejavnostOpis` | `Proizvodnja farmacevtskih preparatov` |
| `ajpes.sector` | `sektor.sektorizacija` | `Nefinančne družbe` |
| `ajpes.size` | `firma.velikostRS` | `velika` |
| `ajpes.capital` | `kapital.vreKapital` and `kapital.valuta` | `54732264.71 EUR` |
| `ajpes.foundationDate` | `dtUstanovitev` (as YYYY-MM-DD) | `1991-04-02` |
| `ajpes.registrationDate` | `dtVpis` (as YYYY-MM-DD) | `1995-03-27` |
| `ajpes.deleted` | `True` when `bZbrisan` marks the subject as deleted | `True` |
| `ajpes.deletionDate` | `dtZbrisan` (as YYYY-MM-DD) | `2024-03-09` |

A property is added only when AJPES returns a value for it. Which fields AJPES returns depends on your data scheme: the minimal scheme returns fewer than the narrower and broader ones.

If the enricher has a **Preview** tab, the results appear there first. To add them to golden records, go to the **Map** tab, select **Map Data**, and choose **Auto Mapping**. Select the business domain, enter a new vocabulary named `AJPES` with the key prefix `ajpes`, and then create the mapping. Auto mapping also uses `name` as the golden record name, so remove that from the mapping if you want to keep your existing names. Then process the data on the **Process** tab. If the enricher has no **Preview** tab, the properties are added to the golden record as soon as it is enriched.

## How the script handles input and errors

- Spaces and dots are removed from the registration number. A 7-digit number is completed with `000` (the head office), so `5860571` is looked up as `5860571000`. A registration number must have 7 or 10 digits.

- A leading `SI` is removed from the tax number, which must have 8 digits and not start with 0.

- Golden records without a valid registration or tax number are skipped without calling AJPES.

- If the API Key field is empty or isn't `username:password`, the script logs a message and adds nothing. If AJPES rejects the user (status `4099`), or the data scheme (status `4010` about the scheme), the script fails the golden record with an error that says so.

- If AJPES has no subject with that number, the input is invalid, or AJPES returns another error, the script logs AJPES' status code and message and adds nothing.

- If AJPES is busy (HTTP 429 or 503), the script throws an error that makes the enricher try the golden record again later.

- Successful results are cached for 7 days per subject, because every lookup uses up part of your PRS package. To change this, edit `CACHE_MILLISECONDS` in the script.

## Testing the enricher

- **Test connection** checks only that the script runs. It doesn't call AJPES.

- To try the setup without using your production package, temporarily change `AJPES_URL` to AJPES' test environment, `https://wwwa.ajpes.si/restPrsInfo`, with a test user from AJPES.

- AJPES records the caller's IP address with every lookup.

## Limitations

- restPrsInfo is a paid service: you need an AJPES user with a PRS package, and each lookup uses up part of it. AJPES' free website search isn't an API.

- restPrsInfo isn't meant for copying the whole register. For that, AJPES provides daily, weekly and monthly files.

- AJPES' success status code and its exact not-found answer aren't documented, so the script treats any answer with data in `payload.formatted` as a result. The values in the sample response above are illustrative: the request format and field names come from the API's own specification, and the error answers were returned by the real service, but no lookup could be made with a real AJPES user while this sample was written.

## Process script

```javascript
// REST API enricher (V2) - Slovenian company lookup with the AJPES Business Register
//
// Looks up a golden record's Slovenian registration number (matična številka), or its tax number
// (davčna številka), in the Slovenian Business Register (Poslovni register Slovenije, PRS) with
// AJPES' restPrsInfo REST API (https://www.ajpes.si/restPrsInfo/swagger/index.html), and adds the
// result to the golden record as ajpes.* properties:
//
//   ajpes.registrationNumber  10-digit registration number (matična številka)
//   ajpes.taxNumber           tax number (davčna številka)
//   ajpes.vatId               VAT identification number (ID za DDV)
//   ajpes.name                full registered name
//   ajpes.shortName           short name
//   ajpes.legalForm           legal form
//   ajpes.address             registered address on one line
//   ajpes.municipality        municipality (občina)
//   ajpes.mainActivityCode    main activity code (SKD)
//   ajpes.mainActivity        main activity description
//   ajpes.sector              institutional sector
//   ajpes.size                company size (Slovenian classification)
//   ajpes.capital             registered capital, with currency
//   ajpes.foundationDate      date of foundation (YYYY-MM-DD)
//   ajpes.registrationDate    date of entry in the register (YYYY-MM-DD)
//   ajpes.deleted             "True" when the subject has been deleted from the register
//   ajpes.deletionDate        date it was deleted (YYYY-MM-DD)
//
// Needs an AJPES portal user with the PRS web service enabled. Enter "username:password" in the
// enricher's API Key field, and set DATA_SCHEME below to the data scheme AJPES registered for
// you. See README.md next to this file for the enricher settings.
//
// A record gets no result (nothing is stored) when it has no valid registration or tax number,
// when the register has no subject with it, or when the API can't answer. A missing or rejected
// user, or an unknown data scheme, fails the record with an error that says so.

// ---- Settings -------------------------------------------------------------------------

// Vocabulary keys to read. Add the same keys to the Vocabulary and Properties field.
const REGISTRATION_NUMBER_KEY = "organization.registrationNumber";
// Optional. Used only when the record has no registration number.
const TAX_NUMBER_KEY = "organization.taxNumber";

// Use https://wwwa.ajpes.si/restPrsInfo to try the setup in AJPES' test environment first.
const AJPES_URL = "https://www.ajpes.si/restPrsInfo";

// The data scheme (šifra sheme) AJPES registered for your user, for example PRS_ON_P.
const DATA_SCHEME = "PRS_ON_P";

// The {APIKey} placeholder is replaced with the API Key field value ("username:password").
const API_KEY = "{APIKey}";

// How long to reuse an answer for the same subject. 0 turns caching off. Every lookup uses up
// a unit of your PRS package, so a long cache saves units.
const CACHE_MILLISECONDS = 7 * 24 * 60 * 60 * 1000;

// ---- Script ---------------------------------------------------------------------------

// AJPES status codes for a rejected user and for invalid input (such as an unknown scheme).
const AUTHENTICATION_ERROR = 4099;
const VALIDATION_ERROR = 4010;

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

// Accepts "5860571000", "5860571" (the 7-digit form, completed with 000) and spaced or dotted
// forms. Returns the 10 digits, or null when it isn't a registration number.
function parseRegistrationNumber(raw) {
  if (/[A-Za-z]/.test(raw)) {
    return null;
  }
  const digits = raw.replace(/[^0-9]/g, "");
  if (digits.length === 7) {
    return digits + "000";
  }
  return digits.length === 10 ? digits : null;
}

// Accepts "92719236", "SI92719236" and "SI 9271 9236". Returns the 8 digits, or null.
function parseTaxNumber(raw) {
  const text = raw.toUpperCase().replace(/^SI/, "");
  if (/[A-Z]/.test(text)) {
    return null;
  }
  const digits = text.replace(/[^0-9]/g, "");
  return /^[1-9]\d{7}$/.test(digits) ? digits : null;
}

function credentials() {
  const value = String(API_KEY || "").trim();
  const separator = value.indexOf(":");
  if (separator <= 0 || separator === value.length - 1) {
    return null;
  }
  return { uporabnik: value.substring(0, separator), geslo: value.substring(separator + 1), shema: DATA_SCHEME };
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

// AJPES dates are ISO date-times. Returns YYYY-MM-DD; .NET's default date (0001-01-01) means none.
function toDate(value, specified) {
  const text = clean(value);
  if (specified === false || !text || !/^\d{4}-\d{2}-\d{2}/.test(text) || text.indexOf("0001-01-01") === 0) {
    return null;
  }
  return text.substring(0, 10);
}

function formatAddress(address) {
  if (!address) {
    return null;
  }
  const street = [clean(address.ulica) || clean(address.naselje), clean(address.stHisna), clean(address.txtDodatek)]
    .filter((x) => !!x)
    .join(" ");
  const town = [clean(address.sifPosta), clean(address.posta)].filter((x) => !!x).join(" ");
  const parts = [street, town].filter((x) => !!x);
  return parts.length > 0 ? parts.join(", ") : null;
}

function formatCapital(capital) {
  if (!capital || capital.vreKapitalSpecified === false || typeof capital.vreKapital !== "number") {
    return null;
  }
  return [String(capital.vreKapital), clean(capital.valuta) || clean(capital.sifValute)].filter((x) => !!x).join(" ");
}

// Calls a restPrsInfo method. Returns the response's formatted payload, or null when there's no
// answer to store.
function callAjpes(method, request, description) {
  const apiResponse = http.send({
    url: `${AJPES_URL}/${method}`,
    method: "POST",
    headers: [
      { Key: "Content-Type", Value: "application/json" },
      { Key: "Accept", Value: "application/json" },
    ],
    body: request,
  });

  const status = String(apiResponse.HttpStatus || "");
  const body = parseJson(apiResponse.Content);
  const code = body && typeof body.status === "number" ? body.status : null;
  const message = body ? clean(body.message) || "" : "";

  if (status === "TooManyRequests" || status === "ServiceUnavailable") {
    throw new Error(`TooManyRequests - AJPES is busy (HTTP ${status}), the record will be retried`);
  }

  if (code === AUTHENTICATION_ERROR || status === "Unauthorized" || status === "Forbidden") {
    throw new Error(`AJPES rejected the user in the API Key field (status ${code || status}: ${message}).`);
  }

  if (code === VALIDATION_ERROR && /shem|storitve/i.test(message)) {
    throw new Error(`AJPES rejected the data scheme "${DATA_SCHEME}" (status ${code}: ${message}). Set DATA_SCHEME to the scheme AJPES registered for your user.`);
  }

  const formatted = body && body.payload ? body.payload.formatted : null;
  if (status === "OK" && formatted) {
    return formatted;
  }

  log(`AJPES could not look up ${description}. HTTP ${status}. ${code !== null ? `Status ${code}: ${message}` : String(apiResponse.Content || "").substring(0, 200)}`);
  return null;
}

function getByRegistrationNumber(registrationNumber, ident) {
  const data = callAjpes("get", { ident: ident, maticna: registrationNumber, izbrisan: false }, `registration number ${registrationNumber}`);
  return data && data.info ? data.info : null;
}

// Finds the registration number for a tax number, then gets the subject.
function getByTaxNumber(taxNumber, ident) {
  const found = callAjpes("find", { ident: ident, davcna: taxNumber, maxRecords: 1 }, `tax number ${taxNumber}`);
  const list = found && Array.isArray(found.prsData) ? found.prsData : [];
  const registrationNumber = list.length > 0 ? parseRegistrationNumber(String(list[0].maticna || "")) : null;
  if (!registrationNumber) {
    if (found) {
      log(`AJPES has no subject with tax number ${taxNumber}.`);
    }
    return null;
  }
  return getByRegistrationNumber(registrationNumber, ident);
}

function run() {
  const registrationNumber = parseRegistrationNumber(getValue(REGISTRATION_NUMBER_KEY));
  const taxNumber = registrationNumber ? null : parseTaxNumber(getValue(TAX_NUMBER_KEY));
  if (!registrationNumber && !taxNumber) {
    // No valid registration or tax number on this record (this is also what Test connection
    // hits, because it passes placeholder values instead of real ones).
    return [];
  }

  const ident = credentials();
  if (!ident) {
    log('AJPES needs a portal user. Enter "username:password" in the enricher\'s API Key field.');
    return [];
  }

  const cacheKey = registrationNumber ? `ajpes:${registrationNumber}` : `ajpes:tax:${taxNumber}`;
  const cached = CACHE_MILLISECONDS > 0 ? cache.get(cacheKey) : null;
  let info = cached ? parseJson(String(cached)) : null;

  if (!info) {
    info = registrationNumber ? getByRegistrationNumber(registrationNumber, ident) : getByTaxNumber(taxNumber, ident);
    if (!info) {
      return [];
    }
    if (CACHE_MILLISECONDS > 0) {
      cache.set(cacheKey, JSON.stringify(info), CACHE_MILLISECONDS);
    }
  }

  const firm = info.firma || {};
  const names = Array.isArray(firm.imeFirme) ? firm.imeFirme : [];
  const name = names.length > 0 ? names[0] : {};
  const activity = info.glavnaDejavnost || null;
  const address = firm.naslovF || null;
  // bZbrisan is a text flag; treat D (da), 1 and true as deleted.
  const deleted = /^(d|da|1|true)$/i.test(String(info.bZbrisan || "").trim());

  const data = {
    "ajpes.registrationNumber": clean(info.stMaticna) || registrationNumber,
    "ajpes.taxNumber": clean(info.stDavcna),
    "ajpes.vatId": clean(info.idDDV),
    "ajpes.name": clean(name.popolnoIme),
    "ajpes.shortName": clean(name.kratkoIme),
    "ajpes.legalForm": clean(firm.oblika),
    "ajpes.address": formatAddress(address),
    "ajpes.municipality": address ? clean(address.obcina) : null,
    "ajpes.mainActivityCode": activity ? clean(activity.sifDejavnost) : null,
    "ajpes.mainActivity": activity ? clean(activity.dejavnostOpis) : null,
    "ajpes.sector": info.sektor ? clean(info.sektor.sektorizacija) : null,
    "ajpes.size": clean(firm.velikostRS),
    "ajpes.capital": formatCapital(info.kapital),
    "ajpes.foundationDate": toDate(info.dtUstanovitev, info.dtUstanovitevSpecified),
    "ajpes.registrationDate": toDate(info.dtVpis, info.dtVpisSpecified),
    "ajpes.deleted": deleted ? true : null,
    "ajpes.deletionDate": deleted ? toDate(info.dtZbrisan, info.dtZbrisanSpecified) : null,
  };

  // Leave out values AJPES didn't return, so they don't overwrite existing data with blanks.
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
