---
title: DENUE (Mexico)
url: https://documentation.cluedin.net/govern/rest-api-enricher-samples/denue-mexico
content_type: reference
section: Govern & improve > REST API enricher samples
---

# DENUE (Mexico)

> reference: Facts, options, APIs.

This example looks up a business establishment in INEGI's [DENUE](https://www.inegi.org.mx/app/mapa/denue/) (Directorio Estadístico Nacional de Unidades Económicas), Mexico's national directory of business establishments, by using the Ficha method of the [DENUE API](https://www.inegi.org.mx/servicios/api_denue.html). For each golden record it stores the establishment name, registered business name (razón social), economic activity, number of people employed, address, location, contact details and coordinates.

**Enricher version:** V2  
**API key:** your INEGI DENUE API token (free; register on the [DENUE API page](https://www.inegi.org.mx/servicios/api_denue.html))

DENUE describes **establishments** (each shop, office or plant), not legal entities, and it has no lookup by RFC (tax ID). Use this sample when your records hold DENUE establishment IDs, for example from a DENUE bulk download or an earlier search.

To set up the enricher, see [Add REST API enricher](https://documentation.cluedin.net/govern/enrichment/rest-api.md#add-rest-api-enricher), then use the settings and script on this page.

## Settings

- **Accepted Business Domain** – `/Organization`, or the business domain that holds your establishments.

- **Version** – V2 (recommended).

- **API Key** – your DENUE API token. The script puts it in the request URL. If the field is empty, the script adds nothing and doesn't call the API.

- **Filters** – we recommend a rule that only accepts golden records where `organization.denueId` has a value. Otherwise, every record without a DENUE ID is listed on the enricher's **Logs** tab as having returned no results.

## Vocabulary and Properties

```
organization.denueId
```

`organization.denueId` holds the DENUE establishment ID (the `Id` field in DENUE, a number such as `34185`). If your data uses another vocabulary key, change this field and the `DENUE_ID_KEY` value at the top of the script.

## Request and response

**Base URL:** `https://www.inegi.org.mx/app/api/denue/v1/consulta`  
**Endpoint:** `GET /Ficha/{id}/{token}`  
**Authentication:** the API token is the last segment of the URL

The script sends one request per golden record:

```http
GET https://www.inegi.org.mx/app/api/denue/v1/consulta/Ficha/34185/<your DENUE API token>
Accept: application/json
```

Response (the Ficha example from INEGI's API documentation):

```json
[
  {
    "CLEE": "01001722514004531",
    "Id": "34185",
    "Nombre": "LONCHERÍA LOS CUATES",
    "Razon_social": "",
    "Clase_actividad": "Restaurantes con servicio de preparación de tacos y tortas",
    "Estrato": "0 a 5 personas",
    "Tipo_vialidad": "CALLE",
    "Calle": "INEGI",
    "Num_Exterior": "201",
    "Num_Interior": "",
    "Colonia": "JARDIN DE LAS BUGAMBILIAS",
    "CP": "20280",
    "Ubicacion": "AGUASCALIENTES, Aguascalientes, AGUASCALIENTES",
    "Telefono": "4492214831",
    "Correo_e": "",
    "Sitio_internet": "",
    "Tipo": "Fijo",
    "Longitud": "-102.28485913",
    "Latitud": "21.85796749",
    "CentroComercial": "",
    "TipoCentroComercial": "",
    "NumLocal": ""
  }
]
```

## Properties added by the enricher

| Property | Response field | Example |
| -------- | -------------- | ------- |
| `denue.id` | `Id` | `34185` |
| `denue.clee` | `CLEE` | `01001722514004531` |
| `denue.name` | `Nombre` | `LONCHERÍA LOS CUATES` |
| `denue.legalName` | `Razon_social` | `OPERADORA HOTELERA AGS DTL S. DE R.L. DE C.V.` |
| `denue.activity` | `Clase_actividad` (in Spanish) | `Restaurantes con servicio de preparación de tacos y tortas` |
| `denue.employeeRange` | `Estrato` | `0 a 5 personas` |
| `denue.address` | `Tipo_vialidad`, `Calle`, `Num_Exterior`, `Num_Interior`, `Colonia` and `CP` on one line | `CALLE INEGI 201, JARDIN DE LAS BUGAMBILIAS, 20280` |
| `denue.postalCode` | `CP` | `20280` |
| `denue.location` | `Ubicacion` (locality, municipality and state) | `AGUASCALIENTES, Aguascalientes, AGUASCALIENTES` |
| `denue.phone` | `Telefono` | `4492214831` |
| `denue.email` | `Correo_e` | `contacto@example.mx` |
| `denue.website` | `Sitio_internet` | `www.example.mx` |
| `denue.establishmentType` | `Tipo` | `Fijo` |
| `denue.latitude` | `Latitud` | `21.85796749` |
| `denue.longitude` | `Longitud` | `-102.28485913` |

A property is added only when DENUE returns a value for it.

If the enricher has a **Preview** tab, the results appear there first. To add them to golden records, go to the **Map** tab, select **Map Data**, and choose **Auto Mapping**. Select the business domain, enter a new vocabulary named `DENUE` with the key prefix `denue`, and then create the mapping. Auto mapping also uses `name` as the golden record name, so remove that from the mapping if you want to keep your existing names. Then process the data on the **Process** tab. If the enricher has no **Preview** tab, the properties are added to the golden record as soon as it is enriched.

## How the script handles input and errors

- Spaces, dots, dashes, a leading `ID` and leading zeros are removed, so `ID 34 185` is looked up as `34185`. Golden records without a numeric DENUE ID are skipped without calling the API.

- If the token is wrong, DENUE answers HTTP 200 with the text `No autorizado. Utilice una clave válida.` The script throws an error, so the golden record is listed on the **Logs** tab with a message to check the **API Key** field.

- If DENUE has no establishment with the ID, or the API returns another error, the script logs the reason (without the token) and adds nothing.

- If the API reports that it is too busy (HTTP 429), the script throws an error that makes the enricher try the golden record again later.

- Successful results are cached for 24 hours per establishment. To change this, edit `CACHE_MILLISECONDS` in the script.

## Testing the enricher

- **Test connection** checks only that the script runs. It doesn't call the API.

- To try the setup, create a golden record with `organization.denueId` set to `34185`, the example establishment in INEGI's API documentation.

## Limitations

- DENUE is a statistical directory of establishments, not a company register. A company with several branches has one DENUE record for each, and there is no lookup by RFC.

- The API also has a **Nombre** method that searches by establishment name or razón social (`/Nombre/{name}/{state}/{from}/{to}/{token}`). It returns every partial match, so it isn't used here: it can't reliably identify one establishment. Use it to find DENUE IDs for your records before you enrich them.

- Activity and employee range descriptions are in Spanish.

## Process script

```javascript
// REST API enricher (V2) - Mexican business establishment lookup with INEGI's DENUE API
//
// Looks up a golden record's DENUE establishment ID in INEGI's Directorio Estadístico Nacional
// de Unidades Económicas (DENUE), the national directory of business establishments, by using
// the DENUE API's Ficha method (https://www.inegi.org.mx/servicios/api_denue.html), and adds
// the result to the golden record as denue.* properties:
//
//   denue.id               DENUE establishment ID that was looked up
//   denue.clee             CLEE (Clave Estadística Empresarial) of the establishment
//   denue.name             name of the establishment
//   denue.legalName        registered business name (razón social)
//   denue.activity         economic activity class (Spanish)
//   denue.employeeRange    number of people employed, as a range, for example 0 a 5 personas
//   denue.address          street address on one line
//   denue.postalCode       postal code
//   denue.location         locality, municipality and state
//   denue.phone            telephone number
//   denue.email            email address
//   denue.website          website
//   denue.establishmentType establishment type, for example Fijo
//   denue.latitude         latitude
//   denue.longitude        longitude
//
// DENUE describes establishments (each shop, office or plant), not legal entities. It has no
// lookup by RFC (tax ID), so the input must be the DENUE establishment ID.
//
// Needs an INEGI DENUE API token, entered in the enricher's API Key field. See README.md next
// to this file for the enricher settings.
//
// A record gets no result (nothing is stored) when it has no valid DENUE ID, when DENUE has no
// establishment with that ID, or when the API can't answer. A missing or rejected token fails
// the record with an error that says so.

// ---- Settings -------------------------------------------------------------------------

// Vocabulary key to read. Add the same key to the Vocabulary and Properties field.
const DENUE_ID_KEY = "organization.denueId";

const DENUE_URL = "https://www.inegi.org.mx/app/api/denue/v1/consulta/Ficha/";

// The {APIKey} placeholder is replaced with the API Key field value (your DENUE API token).
const API_KEY = "{APIKey}";

// How long to reuse an answer for the same establishment. 0 turns caching off.
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

// Accepts "34185", "34 185", "ID 34185". Returns the digits, or null when it isn't a DENUE ID.
function parseDenueId(raw) {
  const text = raw.toUpperCase().replace(/^ID/, "").replace(/[\s.,-]/g, "");
  if (!/^\d{1,12}$/.test(text)) {
    return null;
  }
  const id = text.replace(/^0+/, "");
  return id ? id : null;
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

function formatAddress(item) {
  let street = [clean(item.Tipo_vialidad), clean(item.Calle), clean(item.Num_Exterior)].filter((x) => !!x).join(" ");
  if (clean(item.Num_Interior)) {
    street = `${street} Int. ${clean(item.Num_Interior)}`.trim();
  }
  const parts = [street, clean(item.Colonia), clean(item.CP)].filter((x) => !!x);
  return parts.length > 0 ? parts.join(", ") : null;
}

// Calls the DENUE API. Returns the establishment, or null when there's no answer to store.
function lookUp(id) {
  const apiResponse = http.send({
    url: `${DENUE_URL}${id}/${encodeURIComponent(API_KEY)}`,
    method: "GET",
    headers: [{ Key: "Accept", Value: "application/json" }],
  });

  const status = String(apiResponse.HttpStatus || "");
  const content = String(apiResponse.Content || "");

  if (status === "TooManyRequests") {
    throw new Error("TooManyRequests - the DENUE API is busy, the record will be retried");
  }

  // A wrong token is answered with HTTP 200 and the text "No autorizado. Utilice una clave válida."
  if (status === "Unauthorized" || status === "Forbidden" || /no autorizado/i.test(content)) {
    throw new Error(`The DENUE API rejected the token in the API Key field (HTTP ${status}: ${content.substring(0, 100)}).`);
  }

  const body = parseJson(content);
  const items = Array.isArray(body) ? body : [];
  for (let i = 0; i < items.length; i++) {
    if (items[i] && String(items[i].Id) === id) {
      return items[i];
    }
  }

  // The token isn't included in the message, so it doesn't end up in the server log.
  log(`DENUE could not look up establishment ${id}. HTTP ${status}. ${content.substring(0, 200)}`);
  return null;
}

function run() {
  const id = parseDenueId(getValue(DENUE_ID_KEY));
  if (!id) {
    // No valid DENUE ID on this record (this is also what Test connection hits, because it
    // passes placeholder values instead of real ones).
    return [];
  }

  if (!clean(API_KEY)) {
    log("The DENUE API needs a token. Enter your INEGI DENUE API token in the enricher's API Key field.");
    return [];
  }

  const cacheKey = `denue:${id}`;
  const cached = CACHE_MILLISECONDS > 0 ? cache.get(cacheKey) : null;
  let item = cached ? parseJson(String(cached)) : null;

  if (!item) {
    item = lookUp(id);
    if (!item) {
      return [];
    }
    if (CACHE_MILLISECONDS > 0) {
      cache.set(cacheKey, JSON.stringify(item), CACHE_MILLISECONDS);
    }
  }

  const data = {
    "denue.id": clean(item.Id),
    "denue.clee": clean(item.CLEE),
    "denue.name": clean(item.Nombre),
    "denue.legalName": clean(item.Razon_social),
    "denue.activity": clean(item.Clase_actividad),
    "denue.employeeRange": clean(item.Estrato),
    "denue.address": formatAddress(item),
    "denue.postalCode": clean(item.CP),
    "denue.location": clean(item.Ubicacion),
    "denue.phone": clean(item.Telefono),
    "denue.email": clean(item.Correo_e),
    "denue.website": clean(item.Sitio_internet),
    "denue.establishmentType": clean(item.Tipo),
    "denue.latitude": clean(item.Latitud),
    "denue.longitude": clean(item.Longitud),
  };

  // Leave out values DENUE didn't return, so they don't overwrite existing data with blanks.
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
