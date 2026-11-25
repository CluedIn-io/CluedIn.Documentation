---
title: Azure OpenAI
url: https://documentation.cluedin.net/govern/rest-api-enricher-samples/azure-openai
content_type: reference
section: Govern & improve > REST API enricher samples
---

# Azure OpenAI

> reference: Facts, options, APIs.

This script takes an organization's name and sends a request to an Azure OpenAI deployment using GPT-5.1 or higher, asking it to translate the name into Japanese. Then, it ensures the model responds in a defined JSON format and parses and returns the result in a structure compatible with the enricher. Note that you can use the [Azure Open AI enricher](https://documentation.cluedin.net/govern/enrichment/artificial-intelligence.md) for the same task.

**Enricher version:** V1  
**API key:** your Azure OpenAI API key

To set up the enricher, see [Add REST API enricher](https://documentation.cluedin.net/govern/enrichment/rest-api.md#add-rest-api-enricher), then use the settings and script on this page.

**Method:** POST

## URL

```
https://<your-resource-name>.openai.azure.com/openai/deployments/<your-gpt-5.1-or-higher-deployment-name>/chat/completions?api-version=<api-version>
```

## Vocabulary key and properties

```
organization.name
```

## Headers

```
api-key={APIKey}
```

## Process request script

```javascript
let prompt = String.raw`Please get {organization.japaneseNameRestApi} by translating {Vocabulary:organization.name} into Japanese.

                    Response in JSON using the following template
                    ###
                    {
                        "organization.japaneseNameRestApi": ""
                    }
                    ###
  `;

request.Body.Properties.forEach((x) => {
  prompt = prompt.replace("{Vocabulary:" + x.Key + "}", x.Value);
});

request.Body = {
  messages: [{ role: "user", content: prompt }],
  temperature: 0,
};
```

## Process response script

```javascript
let parsedContent = JSON.parse(response.Content);
let content = parsedContent.choices[0].message.content.trimEnd();
response.Content = JSON.stringify([{ Data: JSON.parse(content), Score: 0 }]);
log(JSON.stringify(response));
```

Up: [REST API enricher samples](https://documentation.cluedin.net/govern/rest-api-enricher-samples.md)
