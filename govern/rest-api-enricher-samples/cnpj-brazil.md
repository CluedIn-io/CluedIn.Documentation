---
title: CNPJ (Brazil)
url: https://documentation.cluedin.net/govern/rest-api-enricher-samples/cnpj-brazil
content_type: reference
section: Govern & improve > REST API enricher samples
---

# CNPJ (Brazil)

> reference: Facts, options, APIs.

This example looks up an organization's CNPJ (Cadastro Nacional da Pessoa Jurídica) with [BrasilAPI's CNPJ API](https://brasilapi.com.br/docs#tag/CNPJ). For each golden record it stores the registered name (razão social), trade name, registration status, legal nature, main activity (CNAE), share capital, company size, and address. No API key is needed.

BrasilAPI is a free, community-run API that serves the [open CNPJ data](https://dados.gov.br/dados/conjuntos-dados/cadastro-nacional-da-pessoa-juridica---cnpj) published by the Receita Federal (Brazil's federal revenue service). It isn't an official government service and has no service level agreement. If you need an official, contracted service, the Receita Federal's CNPJ data is also available as a paid API from SERPRO (Consulta CNPJ), which needs its own credentials and a different script.

**Enricher version:** V2  
**API key:** not needed

To set up the enricher, see [Add REST API enricher](https://documentation.cluedin.net/govern/enrichment/rest-api.md#add-rest-api-enricher), then use the settings and script on this page.

## Settings

- **Accepted Business Domain** – `/Organization`, or the business domain that holds your companies.

- **Version** – V2 (recommended).

- **API Key** – leave empty.

- **Filters** – we recommend a rule that only accepts golden records where `organization.cnpj` has a value. Otherwise, every record without a CNPJ is listed on the enricher's **Logs** tab as having returned no results.

## Vocabulary and Properties

```
organization.cnpj
```

`organization.cnpj` holds the 14-character CNPJ, with or without punctuation. If your data uses another vocabulary key, change this field and the `CNPJ_KEY` value at the top of the script.

## Request and response

**Base URL:** `https://brasilapi.com.br/api`  
**Endpoint:** `GET /cnpj/v1/{cnpj}`  
**Authentication:** none

The script sends one request per golden record:

```http
GET https://brasilapi.com.br/api/cnpj/v1/33000167000101
Accept: application/json
```

Shortened response:

```json
{
  "uf": "RJ",
  "cep": "20031170",
  "cnpj": "33000167000101",
  "porte": "DEMAIS",
  "bairro": "CENTRO",
  "numero": "65",
  "municipio": "RIO DE JANEIRO",
  "logradouro": "REPUBLICA DO CHILE",
  "cnae_fiscal": 600001,
  "complemento": "",
  "razao_social": "PETROLEO BRASILEIRO S A PETROBRAS",
  "nome_fantasia": "PETROBRAS - EDISE",
  "capital_social": 205431960000,
  "ddd_telefone_1": "2121660000",
  "natureza_juridica": "Sociedade de Economia Mista",
  "cnae_fiscal_descricao": "Extração de petróleo e gás natural",
  "data_inicio_atividade": "1966-09-28",
  "data_situacao_cadastral": "2005-11-03",
  "codigo_natureza_juridica": 2038,
  "descricao_situacao_cadastral": "ATIVA",
  "descricao_tipo_de_logradouro": "AVENIDA",
  "descricao_identificador_matriz_filial": "MATRIZ"
}
```

The full response also lists the partners (`qsa`) and secondary activities (`cnaes_secundarios`), which the script doesn't add.

## Properties added by the enricher

| Property | Response field | Example |
| -------- | -------------- | ------- |
| `cnpj.cnpj` | `cnpj` | `33000167000101` |
| `cnpj.name` | `razao_social` | `PETROLEO BRASILEIRO S A PETROBRAS` |
| `cnpj.tradeName` | `nome_fantasia` | `PETROBRAS - EDISE` |
| `cnpj.status` | `descricao_situacao_cadastral` | `ATIVA` |
| `cnpj.statusDate` | `data_situacao_cadastral` | `2005-11-03` |
| `cnpj.establishmentType` | `descricao_identificador_matriz_filial` (`MATRIZ` is the head office, `FILIAL` a branch) | `MATRIZ` |
| `cnpj.legalNature` | `natureza_juridica` | `Sociedade de Economia Mista` |
| `cnpj.legalNatureCode` | `codigo_natureza_juridica` | `2038` |
| `cnpj.mainActivityCode` | `cnae_fiscal`, as 7 digits | `0600001` |
| `cnpj.mainActivity` | `cnae_fiscal_descricao` (in Portuguese) | `Extração de petróleo e gás natural` |
| `cnpj.openingDate` | `data_inicio_atividade` | `1966-09-28` |
| `cnpj.shareCapital` | `capital_social` (BRL) | `205431960000` |
| `cnpj.companySize` | `porte` | `DEMAIS` |
| `cnpj.address` | `descricao_tipo_de_logradouro`, `logradouro`, `numero`, `complemento`, and `bairro` on one line | `AVENIDA REPUBLICA DO CHILE, 65, CENTRO` |
| `cnpj.city` | `municipio` | `RIO DE JANEIRO` |
| `cnpj.state` | `uf` | `RJ` |
| `cnpj.postalCode` | `cep` | `20031170` |
| `cnpj.phone` | `ddd_telefone_1` (area code and number) | `2121660000` |
| `cnpj.email` | `email` | |

A property is added only when the API returns a value for it.

If the enricher has a **Preview** tab, the results appear there first. To add them to golden records, go to the **Map** tab, select **Map Data**, and choose **Auto Mapping**. Select the business domain, enter a new vocabulary named `CNPJ` with the key prefix `cnpj`, and then create the mapping. Auto mapping also uses `name` as the golden record name, so remove that from the mapping if you want to keep your existing names. Then process the data on the **Process** tab. If the enricher has no **Preview** tab, the properties are added to the golden record as soon as it is enriched.

## How the script handles input and errors

- Dots, slashes, dashes, and spaces are removed, so `33.000.167/0001-01` is looked up as `33000167000101`. The CNPJ must have 14 characters and valid check digits. The new alphanumeric CNPJ format (letters in the first 12 characters, issued from July 2026) is accepted too. Golden records without a valid CNPJ are skipped without calling the API.

- If the CNPJ isn't found (HTTP 404), BrasilAPI rejects it (HTTP 400), or the API returns an error, the script logs the reason and adds nothing.

- If the API reports that it is too busy (HTTP 429), the script throws an error that makes the enricher try the golden record again later.

- Successful results are cached for 24 hours per CNPJ. To change this, edit `CACHE_MILLISECONDS` in the script.

## Testing the enricher

- **Test connection** checks only that the script runs. It doesn't call the API.

- To try the setup, create a golden record with `organization.cnpj` set to `33.000.167/0001-01` (Petróleo Brasileiro S.A. – Petrobras).

## Limitations

- BrasilAPI is a free community service with rate limits and no guaranteed availability. For large volumes, check its terms first, or use an official paid service.

- Each CNPJ identifies one establishment. A branch (`FILIAL`) has its own CNPJ, and the script returns that branch's data, not the head office's.

- Descriptions (status, legal nature, activity) are in Portuguese.

- Partners (`qsa`) and secondary activities aren't added.

## Process script

```javascript
// REST API enricher (V2) - Brazilian company lookup by CNPJ with BrasilAPI
//
// Looks up a golden record's CNPJ (Cadastro Nacional da Pessoa Jurídica) with BrasilAPI's free
// CNPJ API (https://brasilapi.com.br/docs#tag/CNPJ), which serves the Receita Federal's open
// CNPJ data, and adds the result to the golden record as cnpj.* properties:
//
//   cnpj.cnpj               14-character CNPJ that was looked up, without punctuation
//   cnpj.name               registered name (razão social)
//   cnpj.tradeName          trade name (nome fantasia)
//   cnpj.status             registration status, for example ATIVA or BAIXADA
//   cnpj.statusDate         date of the registration status (YYYY-MM-DD)
//   cnpj.establishmentType  MATRIZ (head office) or FILIAL (branch)
//   cnpj.legalNature        legal nature, for example Sociedade Anônima Aberta
//   cnpj.legalNatureCode    legal nature code, for example 2046
//   cnpj.mainActivityCode   main activity code (CNAE, 7 digits)
//   cnpj.mainActivity       main activity description (Portuguese)
//   cnpj.openingDate        date the activity started (YYYY-MM-DD)
//   cnpj.shareCapital       share capital in BRL
//   cnpj.companySize        company size (porte), for example MICRO EMPRESA or DEMAIS
//   cnpj.address            street address on one line
//   cnpj.city               municipality
//   cnpj.state              state (UF), for example RJ
//   cnpj.postalCode         postal code (CEP)
//   cnpj.phone              first phone number, with area code
//   cnpj.email              email address
//
// No API key is needed. See README.md next to this file for the enricher settings.
//
// A record gets no result (nothing is stored) when it has no valid CNPJ, when the CNPJ isn't
// found, or when the API can't answer.

// ---- Settings -------------------------------------------------------------------------

// Vocabulary key to read. Add the same key to the Vocabulary and Properties field.
const CNPJ_KEY = "organization.cnpj";

const BRASILAPI_URL = "https://brasilapi.com.br/api/cnpj/v1/";

// How long to reuse an answer for the same CNPJ. 0 turns caching off.
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

// CNPJ check digit (modulo 11). Each character counts as its character code minus 48, so
// digits count as themselves and letters (used by the alphanumeric CNPJ) as 17 (A) and up.
function checkDigit(base) {
  let sum = 0;
  let weight = 2;
  for (let i = base.length - 1; i >= 0; i--) {
    sum += (base.charCodeAt(i) - 48) * weight;
    weight = weight === 9 ? 2 : weight + 1;
  }
  const remainder = sum % 11;
  return remainder < 2 ? 0 : 11 - remainder;
}

// Accepts "33.000.167/0001-01", "33000167000101", "33 000 167 0001 01", etc. Returns the 14
// characters, or null when the value isn't a valid CNPJ.
function parseCnpj(raw) {
  const cnpj = raw.toUpperCase().replace(/[^0-9A-Z]/g, "");
  if (!/^[0-9A-Z]{12}[0-9]{2}$/.test(cnpj) || /^(\d)\1{13}$/.test(cnpj)) {
    return null;
  }
  const first = checkDigit(cnpj.substring(0, 12));
  const second = checkDigit(cnpj.substring(0, 12) + first);
  return cnpj.substring(12) === `${first}${second}` ? cnpj : null;
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

function formatAddress(company) {
  const street = [clean(company.descricao_tipo_de_logradouro), clean(company.logradouro)].filter((x) => !!x).join(" ");
  const parts = [street, clean(company.numero), clean(company.complemento), clean(company.bairro)].filter((x) => !!x);
  return parts.length > 0 ? parts.join(", ") : null;
}

// Calls the API. Returns the company, or null when there's no answer to store.
function lookUp(cnpj) {
  const apiResponse = http.send({
    url: BRASILAPI_URL + encodeURIComponent(cnpj),
    method: "GET",
    headers: [{ Key: "Accept", Value: "application/json" }],
  });

  const status = String(apiResponse.HttpStatus || "");
  const body = parseJson(apiResponse.Content);

  if (status === "TooManyRequests") {
    throw new Error("TooManyRequests - BrasilAPI is busy, the record will be retried");
  }

  if (status === "OK" && body && body.cnpj) {
    return body;
  }

  // NotFound: the CNPJ isn't registered. BadRequest: BrasilAPI rejected the CNPJ.
  log(`BrasilAPI could not look up CNPJ ${cnpj}. HTTP ${status}. ${String(apiResponse.Content || "").substring(0, 200)}`);
  return null;
}

function run() {
  const cnpj = parseCnpj(getValue(CNPJ_KEY));
  if (!cnpj) {
    // No valid CNPJ on this record (this is also what Test connection hits, because it passes
    // placeholder values instead of real ones).
    return [];
  }

  const cacheKey = `cnpj:${cnpj}`;
  const cached = CACHE_MILLISECONDS > 0 ? cache.get(cacheKey) : null;
  let company = cached ? parseJson(String(cached)) : null;

  if (!company) {
    company = lookUp(cnpj);
    if (!company) {
      return [];
    }
    if (CACHE_MILLISECONDS > 0) {
      cache.set(cacheKey, JSON.stringify(company), CACHE_MILLISECONDS);
    }
  }

  const activityCode = clean(company.cnae_fiscal);

  const data = {
    "cnpj.cnpj": clean(company.cnpj),
    "cnpj.name": clean(company.razao_social),
    "cnpj.tradeName": clean(company.nome_fantasia),
    "cnpj.status": clean(company.descricao_situacao_cadastral),
    "cnpj.statusDate": dateOnly(company.data_situacao_cadastral),
    "cnpj.establishmentType": clean(company.descricao_identificador_matriz_filial),
    "cnpj.legalNature": clean(company.natureza_juridica),
    "cnpj.legalNatureCode": clean(company.codigo_natureza_juridica),
    // The API returns the CNAE code as a number, so a leading zero is lost. CNAE codes have 7 digits.
    "cnpj.mainActivityCode": activityCode ? ("0000000" + activityCode).slice(-7) : null,
    "cnpj.mainActivity": clean(company.cnae_fiscal_descricao),
    "cnpj.openingDate": dateOnly(company.data_inicio_atividade),
    "cnpj.shareCapital": typeof company.capital_social === "number" ? company.capital_social : null,
    "cnpj.companySize": clean(company.porte),
    "cnpj.address": formatAddress(company),
    "cnpj.city": clean(company.municipio),
    "cnpj.state": clean(company.uf),
    "cnpj.postalCode": clean(company.cep),
    "cnpj.phone": clean(company.ddd_telefone_1),
    "cnpj.email": clean(company.email),
  };

  // Leave out values the API didn't return, so they don't overwrite existing data with blanks.
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
