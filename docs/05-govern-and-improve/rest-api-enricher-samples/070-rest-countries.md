---
layout: cluedin
title: REST Countries
parent: REST API enricher samples
grand_parent: Govern & improve
nav_order: 70
permalink: /govern/rest-api-enricher-samples/rest-countries
content_type: reference
summary: "Adds the official name of a country from the REST Countries API. V1 and V2 scripts; no API key."
---

This script extracts the official name of a country from the response and formats it into a new JSON structure.

**Enricher version:** V1 or V2  
**API key:** not needed

To set up the enricher, see [Add REST API enricher](/govern/enrichment/rest-api#add-rest-api-enricher), then use the settings and script on this page.

## V1

**Method:** GET

### URL

```
https://restcountries.com/v3.1/name/{Vocabulary:country.country}?fullText=true
```

### Process response script

```javascript
let parsedContent = JSON.parse(response.Content);
let content = parsedContent[0];
let officialName = {
  "country.officialName": content.name.official,
};
response.Content = JSON.stringify([{ Data: officialName, Score: 0 }]);
log(JSON.stringify(response));
```

## V2

### Vocabulary and Properties

```
companies.country
```

### Process script

```javascript
const country = vocabularies.find((x) => x.Key === "companies.country")?.Value;
const url = `https://restcountries.com/v3.1/name/${country}?fullText=true`;

const countryResponse = http.send({
  url: url,
  method: "GET",
});

log(JSON.stringify(countryResponse));

let parsedContent = JSON.parse(countryResponse?.Content);
let results = {
  "country.officialName": parsedContent[0]?.name?.official,
};

response = JSON.stringify([{ Data: results, Score: 100 }]);
```
