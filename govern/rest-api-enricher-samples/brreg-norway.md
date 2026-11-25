---
title: Brønnøysund Register Centre (Norway)
url: https://documentation.cluedin.net/govern/rest-api-enricher-samples/brreg-norway
content_type: reference
section: Govern & improve > REST API enricher samples
---

# Brønnøysund Register Centre (Norway)

> reference: Facts, options, APIs.

This example looks up an organization's Norwegian organization number (organisasjonsnummer) in the Central Coordinating Register for Legal Entities (Enhetsregisteret) by using the [Brønnøysund Register Centre's open-data API](https://data.brreg.no/enhetsregisteret/api/dokumentasjon/en/index.html). For each golden record it stores the registered name, organization form, addresses, main industry, number of employees, and whether the entity is VAT-registered, bankrupt, under liquidation, or deleted. No API key is needed.

**Enricher version:** V2  
**API key:** not needed

To set up the enricher, see [Add REST API enricher](https://documentation.cluedin.net/govern/enrichment/rest-api.md#add-rest-api-enricher), then use the settings and script on this page.

## Settings

- **Accepted Business Domain** – `/Organization`, or the business domain that holds your companies.

- **Version** – V2 (recommended).

- **API Key** – leave empty.

- **Filters** – we recommend a rule that only accepts golden records where `organization.organizationNumber` has a value. Otherwise, every record without an organization number is listed on the enricher's **Logs** tab as having returned no results.

## Vocabulary and Properties

```
organization.organizationNumber
```

`organization.organizationNumber` holds the 9-digit Norwegian organization number. If your data uses another vocabulary key, change this field and the `ORGANIZATION_NUMBER_KEY` value at the top of the script.

## Request and response

**Base URL:** `https://data.brreg.no/enhetsregisteret/api`  
**Endpoint:** `GET /enheter/{organizationNumber}`  
**Authentication:** none

The script sends one request per golden record:

```http
GET https://data.brreg.no/enhetsregisteret/api/enheter/923609016
Accept: application/json
```

Shortened response:

```json
{
  "organisasjonsnummer": "923609016",
  "navn": "EQUINOR ASA",
  "organisasjonsform": { "kode": "ASA", "beskrivelse": "Allmennaksjeselskap" },
  "hjemmeside": "www.equinor.com",
  "postadresse": { "adresse": ["Postboks 8500"], "postnummer": "4035", "poststed": "STAVANGER", "landkode": "NO" },
  "registreringsdatoEnhetsregisteret": "1995-03-12",
  "registrertIMvaregisteret": true,
  "naeringskode1": { "kode": "06.100", "beskrivelse": "Utvinning av råolje" },
  "antallAnsatte": 21182,
  "forretningsadresse": { "adresse": ["Forusbeen 50"], "postnummer": "4035", "poststed": "STAVANGER", "kommune": "STAVANGER", "landkode": "NO" },
  "stiftelsesdato": "1972-09-18",
  "konkurs": false,
  "underAvvikling": false
}
```

## Properties added by the enricher

| Property | Response field | Example |
| -------- | -------------- | ------- |
| `brreg.organizationNumber` | `organisasjonsnummer` | `923609016` |
| `brreg.name` | `navn` | `EQUINOR ASA` |
| `brreg.organizationForm` | `organisasjonsform.beskrivelse` | `Allmennaksjeselskap` |
| `brreg.organizationFormCode` | `organisasjonsform.kode` | `ASA` |
| `brreg.businessAddress` | `forretningsadresse` (address lines, postcode, and town on one line) | `Forusbeen 50, 4035 STAVANGER` |
| `brreg.postalAddress` | `postadresse` | `Postboks 8500, 4035 STAVANGER` |
| `brreg.municipality` | `forretningsadresse.kommune` | `STAVANGER` |
| `brreg.countryCode` | `forretningsadresse.landkode` | `NO` |
| `brreg.industryCode` | `naeringskode1.kode` (NACE / SN2007) | `06.100` |
| `brreg.industry` | `naeringskode1.beskrivelse` (in Norwegian) | `Utvinning av råolje` |
| `brreg.employees` | `antallAnsatte` | `21182` |
| `brreg.website` | `hjemmeside` | `www.equinor.com` |
| `brreg.foundationDate` | `stiftelsesdato` | `1972-09-18` |
| `brreg.registrationDate` | `registreringsdatoEnhetsregisteret` | `1995-03-12` |
| `brreg.vatRegistered` | `registrertIMvaregisteret` | `True` |
| `brreg.bankrupt` | `konkurs` | `False` |
| `brreg.underLiquidation` | `underAvvikling` | `False` |
| `brreg.deleted` | `True` when `slettedato` is set | `True` |
| `brreg.deletionDate` | `slettedato` | `2024-03-09` |

A property is added only when the register returns a value for it.

If the enricher has a **Preview** tab, the results appear there first. To add them to golden records, go to the **Map** tab, select **Map Data**, and choose **Auto Mapping**. Select the business domain, enter a new vocabulary named `Brreg` with the key prefix `brreg`, and then create the mapping. Auto mapping also uses `name` as the golden record name, so remove that from the mapping if you want to keep your existing names. Then process the data on the **Process** tab. If the enricher has no **Preview** tab, the properties are added to the golden record as soon as it is enriched.

## How the script handles input and errors

- Spaces, dots, a leading `NO`, and a trailing `MVA` are removed, so `NO 923 609 016 MVA` is looked up as `923609016`. The number must have 9 digits, start with 8 or 9, and have a valid check digit. Golden records without a valid number are skipped without calling the API.

- If the number isn't registered (HTTP 404), the request is invalid, or the API returns an error, the script logs the reason and adds nothing.

- An entity that has been deleted from the register is still returned. The script adds its name, `brreg.deleted` = `True`, and `brreg.deletionDate`.

- An entity that has been removed from the public register for legal reasons (HTTP 410) gets no result, and the answer isn't cached.

- If the API reports that it is too busy (HTTP 429), the script throws an error that makes the enricher try the golden record again later.

- Successful results are cached for 24 hours per organization number. To change this, edit `CACHE_MILLISECONDS` in the script.

## Testing the enricher

- **Test connection** checks only that the script runs. It doesn't call the API.

- To try the setup, create a golden record with `organization.organizationNumber` set to `974760673` (the Brønnøysund Register Centre itself) or `923609016` (Equinor ASA).

## Limitations

- The script looks up main entities (`enheter`) only, not sub-entities such as branches (`underenheter`).

- Industry and organization form descriptions are in Norwegian.

- Roles (board members, CEO) aren't added. They are available from the separate `/enheter/{organizationNumber}/roller` endpoint.

## Process script

```javascript
// REST API enricher (V2) - Norwegian company lookup with the Brønnøysund Register Centre
//
// Looks up a golden record's Norwegian organization number in the Central Coordinating
// Register for Legal Entities (Enhetsregisteret), using the Brønnøysund Register Centre's
// open-data API (https://data.brreg.no/enhetsregisteret/api/docs/index.html), and adds the
// result to the golden record as brreg.* properties:
//
//   brreg.organizationNumber  9-digit organization number that was looked up
//   brreg.name                registered name
//   brreg.organizationForm    organization form, for example Allmennaksjeselskap
//   brreg.organizationFormCode organization form code, for example ASA
//   brreg.businessAddress     business address on one line
//   brreg.postalAddress       postal address on one line
//   brreg.municipality        municipality of the business address
//   brreg.countryCode         country code of the business address
//   brreg.industryCode        main industry code (NACE, SN2007), for example 06.100
//   brreg.industry            main industry description (Norwegian)
//   brreg.employees           number of employees
//   brreg.website             website
//   brreg.foundationDate      date the entity was founded (YYYY-MM-DD)
//   brreg.registrationDate    date it was registered in Enhetsregisteret (YYYY-MM-DD)
//   brreg.vatRegistered       "True" / "False" - registered in the VAT register
//   brreg.bankrupt            "True" / "False"
//   brreg.underLiquidation    "True" / "False"
//   brreg.deleted             "True" when the entity has been deleted from the register
//   brreg.deletionDate        date it was deleted (YYYY-MM-DD)
//
// No API key is needed. See README.md next to this file for the enricher settings.
//
// A record gets no result (nothing is stored) when it has no valid organization number, when
// the number isn't registered (or has been removed from the public register), or when the API
// can't answer.

// ---- Settings -------------------------------------------------------------------------

// Vocabulary key to read. Add the same key to the Vocabulary and Properties field.
const ORGANIZATION_NUMBER_KEY = "organization.organizationNumber";

const BRREG_URL = "https://data.brreg.no/enhetsregisteret/api/enheter/";

// How long to reuse an answer for the same organization number. 0 turns caching off.
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

// Accepts "923 609 016", "923609016", "NO 923 609 016 MVA", etc. Returns the 9 digits, or null
// when the number isn't a valid Norwegian organization number (MOD11 check digit).
function parseOrganizationNumber(raw) {
  const digits = raw.toUpperCase().replace(/^NO/, "").replace(/MVA$/, "").replace(/[^0-9]/g, "");
  if (!/^[89]\d{8}$/.test(digits)) {
    return null;
  }
  const weights = [3, 2, 7, 6, 5, 4, 3, 2];
  let sum = 0;
  for (let i = 0; i < 8; i++) {
    sum += Number(digits.charAt(i)) * weights[i];
  }
  const remainder = sum % 11;
  const checkDigit = remainder === 0 ? 0 : 11 - remainder;
  return checkDigit !== 10 && checkDigit === Number(digits.charAt(8)) ? digits : null;
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

function dateOnly(value) {
  const text = clean(value);
  return text ? text.substring(0, 10) : null;
}

function formatAddress(address) {
  if (!address) {
    return null;
  }
  const lines = Array.isArray(address.adresse) ? address.adresse.filter((x) => !!clean(x)) : [];
  const postalTown = [clean(address.postnummer), clean(address.poststed)].filter((x) => !!x).join(" ");
  if (postalTown) {
    lines.push(postalTown);
  }
  if (clean(address.landkode) && address.landkode !== "NO" && clean(address.land)) {
    lines.push(address.land);
  }
  return lines.length > 0 ? lines.join(", ") : null;
}

// Calls the API. Returns the entity, or null when there's no answer to store.
function lookUp(organizationNumber) {
  const apiResponse = http.send({
    url: BRREG_URL + organizationNumber,
    method: "GET",
    headers: [{ Key: "Accept", Value: "application/json" }],
  });

  const status = String(apiResponse.HttpStatus || "");
  const body = parseJson(apiResponse.Content);

  if (status === "TooManyRequests") {
    throw new Error("TooManyRequests - the Brønnøysund Register Centre API is busy, the record will be retried");
  }

  // A deleted entity is still returned (with OK), with its name and deletion date (slettedato).
  if (status === "OK" && body && body.organisasjonsnummer) {
    return body;
  }

  // 410 Gone: the entity has been removed from the public register for legal reasons. The
  // register asks that copies aren't kept, so nothing is stored or cached.

  log(`Brønnøysund Register Centre could not look up ${organizationNumber}. HTTP ${status}. ${String(apiResponse.Content || "").substring(0, 200)}`);
  return null;
}

function run() {
  const organizationNumber = parseOrganizationNumber(getValue(ORGANIZATION_NUMBER_KEY));
  if (!organizationNumber) {
    // No valid organization number on this record (this is also what Test connection hits,
    // because it passes placeholder values instead of real ones).
    return [];
  }

  const cacheKey = `brreg:${organizationNumber}`;
  const cached = CACHE_MILLISECONDS > 0 ? cache.get(cacheKey) : null;
  let entity = cached ? parseJson(String(cached)) : null;

  if (!entity) {
    entity = lookUp(organizationNumber);
    if (!entity) {
      return [];
    }
    if (CACHE_MILLISECONDS > 0) {
      cache.set(cacheKey, JSON.stringify(entity), CACHE_MILLISECONDS);
    }
  }

  const form = entity.organisasjonsform || {};
  const industry = entity.naeringskode1 || {};
  const businessAddress = entity.forretningsadresse || entity.beliggenhetsadresse || null;
  const deletionDate = dateOnly(entity.slettedato);

  const data = {
    "brreg.organizationNumber": clean(entity.organisasjonsnummer),
    "brreg.name": clean(entity.navn),
    "brreg.organizationForm": clean(form.beskrivelse),
    "brreg.organizationFormCode": clean(form.kode),
    "brreg.businessAddress": formatAddress(businessAddress),
    "brreg.postalAddress": formatAddress(entity.postadresse),
    "brreg.municipality": businessAddress ? clean(businessAddress.kommune) : null,
    "brreg.countryCode": businessAddress ? clean(businessAddress.landkode) : null,
    "brreg.industryCode": clean(industry.kode),
    "brreg.industry": clean(industry.beskrivelse),
    "brreg.employees": typeof entity.antallAnsatte === "number" ? entity.antallAnsatte : null,
    "brreg.website": clean(entity.hjemmeside),
    "brreg.foundationDate": dateOnly(entity.stiftelsesdato),
    "brreg.registrationDate": dateOnly(entity.registreringsdatoEnhetsregisteret),
    "brreg.vatRegistered": typeof entity.registrertIMvaregisteret === "boolean" ? entity.registrertIMvaregisteret : null,
    "brreg.bankrupt": typeof entity.konkurs === "boolean" ? entity.konkurs : null,
    "brreg.underLiquidation": typeof entity.underAvvikling === "boolean" ? entity.underAvvikling : null,
    "brreg.deleted": deletionDate ? true : null,
    "brreg.deletionDate": deletionDate,
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
