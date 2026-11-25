---
title: Wathq Commercial Registration (Saudi Arabia)
url: https://documentation.cluedin.net/govern/rest-api-enricher-samples/wathq-saudi-arabia
content_type: reference
section: Govern & improve > REST API enricher samples
---

# Wathq Commercial Registration (Saudi Arabia)

> reference: Facts, options, APIs.

This example looks up an organization's commercial registration (CR) number by using the full information operation of the [Wathq](https://developer.wathq.sa/) Commercial Registration API, the Ministry of Commerce's official API for the Saudi commercial register. For each golden record it stores the registered name, entity and main CR numbers, business type, status, issue and expiry dates, city, national address, contact details, ISIC activities, paid-up capital, and whether the business is registered for e-commerce.

**Enricher version:** V2  
**API key:** your Wathq API key (subscribe to the Commercial Registration API on the [Wathq developer portal](https://developer.wathq.sa/); calls are charged according to Wathq's pricing, where full information is listed at SAR 12 per call)

To set up the enricher, see [Add REST API enricher](https://documentation.cluedin.net/govern/enrichment/rest-api.md#add-rest-api-enricher), then use the settings and script on this page.

## Settings

- **Accepted Business Domain** – `/Organization`, or the business domain that holds your companies.

- **Version** – V2 (recommended).

- **API Key** – your Wathq API key. The script sends it in the `apiKey` header. If the field is empty, the script adds nothing and doesn't call Wathq.

- **Filters** – we recommend a rule that only accepts golden records where `organization.crNumber` has a value. Otherwise, every record without a CR number is listed on the enricher's **Logs** tab as having returned no results.

## Vocabulary and Properties

```
organization.crNumber
```

`organization.crNumber` holds the 10-digit CR number. If your data uses another vocabulary key, change this field and the `CR_NUMBER_KEY` value at the top of the script.

## Request and response

**Base URL:** `https://api.wathq.sa/commercial-registration`  
**Endpoint:** `GET /fullinfo/{crNumber}?language=en`  
**Authentication:** API key in the `apiKey` request header

The script sends one request per golden record:

```http
GET https://api.wathq.sa/commercial-registration/fullinfo/1010000000?language=en
apiKey: <your Wathq API key>
Accept: application/json
```

Shortened response (illustrative values, with the field names of Wathq's full information model; this sample couldn't be run against real data without a Wathq subscription):

```json
{
  "crName": "Example Trading Company",
  "crNumber": "1010000000",
  "crEntityNumber": "7000000000",
  "issueDate": "1431/06/18",
  "expiryDate": "1448/06/18",
  "crMainNumber": "1010000000",
  "businessType": { "id": "201", "name": "شركة ذات مسؤولية محدودة", "nameEn": "Limited Liability Company" },
  "status": { "id": "active", "name": "نشط", "nameEn": "Active" },
  "location": { "id": "1010", "name": "Riyadh" },
  "isEcommerce": false,
  "capital": { "paidAmount": 500000, "subscribedAmount": 500000, "announcedAmount": 500000 },
  "address": {
    "general": { "website": "www.example.sa", "email": "info@example.sa", "telephone1": "0110000000" },
    "national": { "buildingNumber": "1234", "streetName": "King Fahd Road", "city": "Riyadh", "zipcode": "12345", "district": { "id": "1", "name": "Al Olaya" } }
  },
  "activities": { "isic": [ { "id": "4610", "name": "وكلاء البيع", "nameEn": "Wholesale on a fee or contract basis" } ] }
}
```

Errors come back as a code and a message, for example `{ "code": "404.2.1", "message": "No Results Found" }` or, for a wrong key, `{ "code": "401.1.1", "message": "Invalid ApiKey" }`.

## Properties added by the enricher

| Property | Response field | Example |
| -------- | -------------- | ------- |
| `wathq.crNumber` | `crNumber` | `1010000000` |
| `wathq.name` | `crName` | `Example Trading Company` |
| `wathq.entityNumber` | `crEntityNumber` | `7000000000` |
| `wathq.mainCrNumber` | `crMainNumber` | `1010000000` |
| `wathq.businessType` | `businessType.nameEn`, or `businessType.name` | `Limited Liability Company` |
| `wathq.status` | `status.nameEn`, or `status.name` | `Active` |
| `wathq.issueDate` | `issueDate`, as returned | `1431/06/18` |
| `wathq.expiryDate` | `expiryDate`, as returned | `1448/06/18` |
| `wathq.city` | `location.name` | `Riyadh` |
| `wathq.address` | `address.national` (building number, street, district, city, postcode) on one line | `1234 King Fahd Road, Al Olaya, Riyadh 12345` |
| `wathq.website` | `address.general.website` | `www.example.sa` |
| `wathq.email` | `address.general.email` | `info@example.sa` |
| `wathq.phone` | `address.general.telephone1` | `0110000000` |
| `wathq.activities` | `activities.isic[].nameEn` (or `name`), separated by `; ` | `Wholesale on a fee or contract basis` |
| `wathq.paidCapital` | `capital.paidAmount` | `500000` |
| `wathq.ecommerce` | `isEcommerce` | `False` |

A property is added only when Wathq returns a value for it. Where Wathq has no English name, the Arabic one is used.

If the enricher has a **Preview** tab, the results appear there first. To add them to golden records, go to the **Map** tab, select **Map Data**, and choose **Auto Mapping**. Select the business domain, enter a new vocabulary named `Wathq` with the key prefix `wathq`, and then create the mapping. Auto mapping also uses `name` as the golden record name, so remove that from the mapping if you want to keep your existing names. Then process the data on the **Process** tab. If the enricher has no **Preview** tab, the properties are added to the golden record as soon as it is enriched.

## How the script handles input and errors

- Spaces, dots, dashes, and a leading `CR` are removed, and Arabic-Indic digits are converted, so `CR 1010 000 000` is looked up as `1010000000`. The number must have 10 digits and not start with 0. Golden records without a valid CR number are skipped without calling Wathq.

- If Wathq has no registration with that number (HTTP 404, code `404.2.1`), the input is invalid (HTTP 400), or Wathq returns another error, the script logs the reason and adds nothing.

- If Wathq rejects the API key (HTTP 401) or your subscription doesn't include the operation (HTTP 403), the script throws an error, so the golden record is listed on the **Logs** tab with a message to check the **API Key** field.

- If Wathq reports that it is too busy or your plan's rate limit is reached (HTTP 429), the script throws an error that makes the enricher try the golden record again later.

- Successful results are cached for 7 days per CR number, because every call is charged. To change this, edit `CACHE_MILLISECONDS` in the script.

## Testing the enricher

- **Test connection** checks only that the script runs. It doesn't call Wathq.

- Wathq also has a sandbox for trying the API with test data. Use the sandbox base URL and key from your Wathq application by changing `WATHQ_URL` in the script and the **API Key** field.

## Limitations

- Every call is charged. Keep the cache on, and add a filter so only records with a CR number are sent.

- Issue and expiry dates are stored as Wathq returns them, and Hijri dates aren't converted to Gregorian.

- Owners, managers, and branches are available from other Wathq operations (`/owners`, `/managers`, `/branches`) and aren't added.

## Process script

```javascript
// REST API enricher (V2) - Saudi commercial registration lookup with Wathq
//
// Looks up a golden record's Saudi commercial registration (CR) number with the Ministry of
// Commerce's Wathq Commercial Registration API (https://developer.wathq.sa/), by using its
// full information operation, and adds the result to the golden record as wathq.* properties:
//
//   wathq.crNumber       CR number that was looked up
//   wathq.name           registered name
//   wathq.entityNumber   CR entity number
//   wathq.mainCrNumber   CR number of the main registration (for a branch)
//   wathq.businessType   business type, for example Limited Liability Company
//   wathq.status         CR status
//   wathq.issueDate      issue date, as returned by Wathq
//   wathq.expiryDate     expiry date, as returned by Wathq
//   wathq.city           location (city) of the registration
//   wathq.address        national address on one line
//   wathq.website        website
//   wathq.email          email address
//   wathq.phone          telephone number
//   wathq.activities     ISIC activities, separated by "; "
//   wathq.paidCapital    paid-up capital
//   wathq.ecommerce      "True" / "False" - registered for e-commerce
//
// Needs a Wathq API key (sent in the apiKey header), entered in the enricher's API Key field.
// Calls are charged per your Wathq plan. See README.md next to this file.
//
// A record gets no result (nothing is stored) when it has no valid CR number, when Wathq has no
// registration with that number, or when the API can't answer. A missing or rejected key fails
// the record with an error that says so.

// ---- Settings -------------------------------------------------------------------------

// Vocabulary key to read. Add the same key to the Vocabulary and Properties field.
const CR_NUMBER_KEY = "organization.crNumber";

const WATHQ_URL = "https://api.wathq.sa/commercial-registration/fullinfo/";

// Language of names and descriptions in the answer: en or ar.
const LANGUAGE = "en";

// The {APIKey} placeholder is replaced with the API Key field value.
const API_KEY = "{APIKey}";

// How long to reuse an answer for the same CR number. 0 turns caching off. Every call is
// charged, so a long cache saves money.
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

// Accepts "1010000000", "1010 000 000", "CR 1010000000" and Arabic-Indic digits. Returns the 10
// digits, or null when it isn't a CR number.
function parseCrNumber(raw) {
  const western = raw.replace(/[٠-٩]/g, (d) => String(d.charCodeAt(0) - 0x0660));
  const text = western.toUpperCase().replace(/^C\.?R\.?/, "");
  if (!/^[0-9\s.-]+$/.test(text)) {
    return null;
  }
  const digits = text.replace(/[^0-9]/g, "");
  return /^[1-9]\d{9}$/.test(digits) ? digits : null;
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

// Dates are kept as Wathq returns them (Hijri dates such as 1440/05/12 aren't converted). A
// Gregorian timestamp is cut to its date, so the enricher doesn't reformat it.
function dateText(value) {
  const text = clean(value);
  if (!text) {
    return null;
  }
  const iso = /^(\d{4}-\d{2}-\d{2})T/.exec(text);
  return iso ? iso[1] : text;
}

// The English name where Wathq has one, otherwise the Arabic one.
function nameOf(item) {
  if (!item) {
    return null;
  }
  if (typeof item !== "object") {
    return clean(item);
  }
  return clean(item.nameEn) || clean(item.name);
}

function formatAddress(national) {
  if (!national) {
    return null;
  }
  const street = [clean(national.buildingNumber), clean(national.streetName)].filter((x) => !!x).join(" ");
  const district = national.district ? nameOf(national.district) : null;
  const city = [clean(national.city), clean(national.zipcode)].filter((x) => !!x).join(" ");
  const parts = [street, district, city].filter((x) => !!x);
  return parts.length > 0 ? parts.join(", ") : null;
}

function errorText(body) {
  return body ? [clean(body.code), clean(body.message)].filter((x) => !!x).join(" ") : "";
}

// Calls Wathq. Returns the registration, or null when there's no answer to store.
function lookUp(crNumber) {
  const apiResponse = http.send({
    url: `${WATHQ_URL}${crNumber}?language=${encodeURIComponent(LANGUAGE)}`,
    method: "GET",
    headers: [
      { Key: "apiKey", Value: API_KEY },
      { Key: "Accept", Value: "application/json" },
    ],
  });

  const status = String(apiResponse.HttpStatus || "");
  const body = parseJson(apiResponse.Content);

  if (status === "TooManyRequests") {
    throw new Error("TooManyRequests - the Wathq API is busy or the plan's rate limit was reached, the record will be retried");
  }

  if (status === "Unauthorized" || status === "Forbidden") {
    throw new Error(`The Wathq API rejected the API key (HTTP ${status}: ${errorText(body) || "no details"}). Check the API Key field of the enricher and your Wathq subscription.`);
  }

  if (status === "OK" && body && clean(body.crNumber)) {
    return body;
  }

  // 404 with code 404.2.1 "No Results Found", 400 for invalid input, or a server error.
  log(`Wathq could not look up ${crNumber}. HTTP ${status}. ${errorText(body) || String(apiResponse.Content || "").substring(0, 200)}`);
  return null;
}

function run() {
  const crNumber = parseCrNumber(getValue(CR_NUMBER_KEY));
  if (!crNumber) {
    // No valid CR number on this record (this is also what Test connection hits, because it
    // passes placeholder values instead of real ones).
    return [];
  }

  if (!API_KEY) {
    log("No Wathq API key. Enter it in the API Key field of the enricher.");
    return [];
  }

  const cacheKey = `wathq:${crNumber}`;
  const cached = CACHE_MILLISECONDS > 0 ? cache.get(cacheKey) : null;
  let cr = cached ? parseJson(String(cached)) : null;

  if (!cr) {
    cr = lookUp(crNumber);
    if (!cr) {
      return [];
    }
    if (CACHE_MILLISECONDS > 0) {
      cache.set(cacheKey, JSON.stringify(cr), CACHE_MILLISECONDS);
    }
  }

  const address = cr.address || {};
  const general = address.general || {};
  const activities = cr.activities && Array.isArray(cr.activities.isic)
    ? cr.activities.isic.map((x) => nameOf(x)).filter((x) => !!x)
    : [];
  const capital = cr.capital || {};

  const data = {
    "wathq.crNumber": clean(cr.crNumber),
    "wathq.name": clean(cr.crName),
    "wathq.entityNumber": clean(cr.crEntityNumber),
    "wathq.mainCrNumber": clean(cr.crMainNumber),
    "wathq.businessType": nameOf(cr.businessType),
    "wathq.status": nameOf(cr.status),
    "wathq.issueDate": dateText(cr.issueDate),
    "wathq.expiryDate": dateText(cr.expiryDate),
    "wathq.city": nameOf(cr.location),
    "wathq.address": formatAddress(address.national),
    "wathq.website": clean(general.website),
    "wathq.email": clean(general.email),
    "wathq.phone": clean(general.telephone1),
    "wathq.activities": activities.length > 0 ? activities.join("; ") : null,
    "wathq.paidCapital": typeof capital.paidAmount === "number" || clean(capital.paidAmount) ? capital.paidAmount : null,
    "wathq.ecommerce": typeof cr.isEcommerce === "boolean" ? cr.isEcommerce : null,
  };

  // Leave out values Wathq didn't return, so they don't overwrite existing data with blanks.
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
