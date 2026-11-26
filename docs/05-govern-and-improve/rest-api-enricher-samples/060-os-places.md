---
layout: cluedin
title: OS Places (AddressBase)
parent: REST API enricher samples
grand_parent: Govern & improve
nav_order: 60
permalink: /govern/rest-api-enricher-samples/os-places
content_type: reference
summary: "Verifies UK addresses with Ordnance Survey's OS Places API (AddressBase). V1 script; needs an OS Data Hub API key."
---

AddressBase is a set of diverse APIs one of which is address verification, like OS Places API (https://osdatahub.os.uk/).

**Enricher version:** V1  
**API key:** your OS Data Hub API key (create one on the [OS Data Hub](https://osdatahub.os.uk/); the premium plan has a 60-day trial)

To set up the enricher, see [Add REST API enricher](/govern/enrichment/rest-api#add-rest-api-enricher), then use the settings and script on this page.

**Method:** GET

## URL

```
https://api.os.uk/search/places/v1/find?key={APIKey}&query={Vocabulary:address.fu[…]s}%20{Vocabulary:address.locality}&maxresults=1&matchprecision=1
```

## Process response script

```javascript
// Expects an input object named `response` like:
// {
//   HttpStatus: "OK",
//   Content: "{...OS Places JSON...}",
//   Headers: [{ Key: "Content-Type", Value: "application/json" }, ...]
// }
//
// Output will be:
// response.Content = "[{\"Data\":{...},\"Score\":0}]"

(function () {
  function asStr(v) {
    if (v === undefined || v === null) return null;
    v = String(v);
    return v.length ? v : null;
  }

  function asNum(v) {
    if (v === undefined || v === null || v === "") return null;
    var n = Number(v);
    return isFinite(n) ? n : null;
  }

  function setHeader(key, value) {
    if (!response.Headers) response.Headers = [];
    var i;
    for (i = 0; i < response.Headers.length; i++) {
      if (
        response.Headers[i] &&
        typeof response.Headers[i].Key === "string" &&
        response.Headers[i].Key.toLowerCase() === key.toLowerCase()
      ) {
        response.Headers[i].Value = value;
        return;
      }
    }
    response.Headers.push({ Key: key, Value: value });
  }

  // Parse incoming OS Places content
  var parsed;
  try {
    parsed = JSON.parse(response.Content || "{}");
  } catch (e) {
    // If Content isn't valid JSON, return a safe empty payload
    response.HttpStatus = response.HttpStatus || "OK";
    response.Content = JSON.stringify([
      {
        Data: { "osPlaces.error": "Invalid JSON in response.Content" },
        Score: 0,
      },
    ]);
    response.ContentType = "application/x-javascript";
    setHeader("Content-Type", "application/x-javascript");
    return;
  }

  var first =
    parsed && parsed.results && parsed.results.length
      ? parsed.results[0]
      : null;

  if (!first || typeof first !== "object") {
    response.HttpStatus = response.HttpStatus || "OK";
    response.Content = JSON.stringify([
      { Data: { "osPlaces.found": false }, Score: 0 },
    ]);
    response.ContentType = "application/x-javascript";
    setHeader("Content-Type", "application/x-javascript");
    return;
  }

  var source = first.DPA ? "DPA" : first.LPI ? "LPI" : null;
  var src = source ? first[source] : null;

  if (!src) {
    response.HttpStatus = response.HttpStatus || "OK";
    response.Content = JSON.stringify([
      { Data: { "osPlaces.found": false }, Score: 0 },
    ]);
    response.ContentType = "application/x-javascript";
    setHeader("Content-Type", "application/x-javascript");
    return;
  }

  // Build normalized dotted-key output (first result only)
  var newContent = {
    "osPlaces.found": true,
    "osPlaces.source": source,
    "osPlaces.uprn": null,
    "osPlaces.fullAddress": null,
    "osPlaces.postcode": null,
    "osPlaces.town": null,
    "osPlaces.street": null,
    "osPlaces.building": null,
    "osPlaces.subBuilding": null,
    "osPlaces.organisation": null,
    "osPlaces.department": null,
    "osPlaces.easting": null,
    "osPlaces.northing": null,
    "osPlaces.latitude": null,
    "osPlaces.longitude": null,
  };

  if (source === "DPA") {
    newContent["osPlaces.uprn"] = asStr(src.UPRN);
    newContent["osPlaces.fullAddress"] = asStr(src.ADDRESS);
    newContent["osPlaces.postcode"] = asStr(src.POSTCODE);
    newContent["osPlaces.town"] = asStr(src.POST_TOWN);

    newContent["osPlaces.street"] =
      asStr(src.THOROUGHFARE) || asStr(src.DEPENDENT_THOROUGHFARE);
    newContent["osPlaces.building"] =
      asStr(src.BUILDING_NAME) || asStr(src.BUILDING_NUMBER);
    newContent["osPlaces.subBuilding"] = asStr(src.SUB_BUILDING_NAME);

    newContent["osPlaces.organisation"] = asStr(src.ORGANISATION_NAME);
    newContent["osPlaces.department"] = asStr(src.DEPARTMENT_NAME);

    newContent["osPlaces.easting"] = asNum(src.X_COORDINATE);
    newContent["osPlaces.northing"] = asNum(src.Y_COORDINATE);
    newContent["osPlaces.latitude"] = asNum(src.LAT);
    newContent["osPlaces.longitude"] = asNum(src.LNG);
  } else {
    // LPI
    newContent["osPlaces.uprn"] = asStr(src.UPRN);
    newContent["osPlaces.fullAddress"] = asStr(src.ADDRESS); // may be missing in some LPI responses
    newContent["osPlaces.postcode"] =
      asStr(src.POSTCODE_LOCATOR) || asStr(src.POSTCODE);
    newContent["osPlaces.town"] = asStr(src.TOWN_NAME) || asStr(src.POST_TOWN);

    newContent["osPlaces.street"] = asStr(src.STREET_DESCRIPTION);
    newContent["osPlaces.building"] =
      asStr(src.PAO_TEXT) ||
      asStr(src.PAO_START_NUMBER) ||
      asStr(src.PAO_START_SUFFIX);
    newContent["osPlaces.subBuilding"] =
      asStr(src.SAO_TEXT) ||
      asStr(src.SAO_START_NUMBER) ||
      asStr(src.SAO_START_SUFFIX);

    newContent["osPlaces.organisation"] = asStr(src.ORGANISATION);
    newContent["osPlaces.department"] = asStr(src.DEPARTMENT);

    newContent["osPlaces.easting"] = asNum(src.X_COORDINATE);
    newContent["osPlaces.northing"] = asNum(src.Y_COORDINATE);
    newContent["osPlaces.latitude"] = asNum(src.LAT);
    newContent["osPlaces.longitude"] = asNum(src.LNG);
  }

  // Wrap into enricher output format
  response.HttpStatus = response.HttpStatus || "OK";
  response.Content = JSON.stringify([{ Data: newContent, Score: 0 }]);

  // Keep response format consistent with your sample
  response.ContentType = "application/x-javascript";
  setHeader("Content-Type", "application/x-javascript");
})();
```
