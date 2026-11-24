---
layout: cluedin
title: DuckDuckGo
parent: REST API enricher samples
grand_parent: Govern & improve
nav_order: 20
permalink: /govern/rest-api-enricher-samples/duckduckgo
content_type: reference
summary: "Adds information about an organization from the DuckDuckGo Instant Answer API. V1 script; no API key."
---

This script handles the JSON response returned by a DuckDuckGo API call. The main purpose is to extract useful information from the API response and transform it into a format usable by the enricher.

**Enricher version:** V1  
**API key:** not needed

CluedIn also has a built-in [DuckDuckGo enricher](/govern/enrichment/duckduckgo).

To set up the enricher, see [Add REST API enricher](/govern/enrichment/rest-api#add-rest-api-enricher), then use the settings and script on this page.

**Method:** GET

## URL

```
https://api.duckduckgo.com?q={Vocabulary:organization.name}&format=json
```

## Process response script

```javascript
function extractStringValues(obj, dict = new Map()) {
  for (const [key, value] of Object.entries(obj)) {
    if (value && typeof value !== "object" && !Array.isArray(value)) {
      dict.set("duckDuckGo.organization." + key, value.toString());
    }
  }
  return dict;
}
function extractInfobox(content, dict = new Map()) {
  content?.forEach((x) => {
    dict.set("duckDuckGo.organization.infobox." + x.label, x.value);
  });
}
function extractRelatedTopics(relatedTopics, dict = new Map()) {
  for (let i = 0; i < relatedTopics.length; i++) {
    dict.set(
      "duckDuckGo.organization.relatedTopics" + i + ".firstUrl",
      relatedTopics[i]?.FirstURL
    );
    dict.set(
      "duckDuckGo.organization.relatedTopics" + i + ".text",
      relatedTopics[i]?.Text
    );
    dict.set(
      "duckDuckGo.organization.relatedTopics" + i + ".icon",
      relatedTopics[i]?.Icon?.Url
    );
  }
}
try {
  // Update the content here
  let parsedContent = JSON.parse(response.Content);
  let vocabularyKeysWithValue = extractStringValues(parsedContent);
  extractInfobox(parsedContent.Infobox?.content, vocabularyKeysWithValue);
  extractRelatedTopics(parsedContent.RelatedTopics, vocabularyKeysWithValue);
  response.Content = JSON.stringify([
    { Data: Object.fromEntries(vocabularyKeysWithValue), Score: 0 },
  ]);
  log(response);
} catch (error) {
  const errorDetails = {
    name: error?.name,
    message: error?.message,
    stack: error?.stack,
  };
  log("Error caught:" + JSON.stringify(errorDetails));
}
```
