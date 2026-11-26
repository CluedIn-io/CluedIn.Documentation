---
layout: cluedin
title: Logo.dev
parent: REST API enricher samples
grand_parent: Govern & improve
nav_order: 40
permalink: /govern/rest-api-enricher-samples/logo-dev
content_type: reference
summary: "Adds a company logo URL from Logo.dev, based on the company's website. V2 script; needs a Logo.dev API key."
---

This example retrieves a company's logo URL from [Logo.dev](https://www.logo.dev/) by using the website stored on the golden record. It stores a stable Logo.dev image URL and the matched domain; it does not store the binary image response as a property value.

**Enricher version:** V2  
**API key:** your Logo.dev API key

To set up the enricher, see [Add REST API enricher](/govern/enrichment/rest-api#add-rest-api-enricher), then use the settings and script on this page.

## API Key
```
your-logo-dev-api-key
```

## Vocabulary and Properties

```
companies.website
```

## Process script

```javascript
// REST API Enricher V2 - Logo.dev logo URL enrichment
// The {APIKey} placeholder is replaced with the API Key field value.

const website = vocabularies.find((x) => x.Key === "companies.website")?.Value;

if (!website) {
  response = JSON.stringify([]);
} else {
  // Accept a full URL, a bare domain, or a domain with a port.
  // Logo.dev expects only the hostname.
  const domain = String(website)
    .trim()
    .replace(/^https?:\/\//i, "")
    .replace(/^www\./i, "")
    .split(/[\/?#]/)[0]
    .split(":")[0]

  if (!domain) {
    response = JSON.stringify([]);
  } else {
    const logoUrl = `https://img.logo.dev/${encodeURIComponent(domain)}?token={APIKey}`;

    // Request the image so an unavailable logo or API error does not create
    // an enrichment result. The returned image bytes are intentionally ignored.
    const logoResponse = http.send({
      url: logoUrl,
      method: "GET",
    });

    const status = String(logoResponse?.HttpStatus || "");
    if (status === "OK") {
      response = JSON.stringify([
        {
          Data: {
            "companies.logoUrl": logoUrl,
            "companies.logoDomain": domain,
          },
          Score: 100,
        },
      ]);
    } else {
      log(`Logo.dev did not return a logo for ${domain}. Status: ${status}`);
      response = JSON.stringify([]);
    }
  }
}
```
