---
layout: cluedin
nav_order: 16
parent: Enricher
grand_parent: Preparation
permalink: /preparation/enricher/rest-api
title: REST API
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

This article explains how to add the REST API enricher. The purpose of this enricher is to retrieve data from a wide variety of endpoints. It provides a flexible way to integrate diverse data sources into your golden records.  

{:.important}
This enricher is intended for users who are comfortable **writing JavaScript code**, as scripting is required to customize request and response handling.

## Add REST API enricher

The REST API enricher requires the URL of an external endpoint to retrieve data. You can use JavaScript to customize request construction and response processing for precise control over data extraction. You can find some examples of JavaScript code in the [Sample scripts](#sample-scripts) section of this page.

**To add REST API enricher**

1. On the navigation pane, go to **Preparation** > **Enrich**. Then, select **Add Enricher**.

1. On the **Choose Enricher** tab, select **REST API**, and then select **Next**.

    ![rest-api-enricher-1.png]({{ "/assets/images/preparation/enricher/rest-api-enricher-1.png" | relative_url }})

1. On the **Configure** tab, provide the following details:

    1. **Accepted Business Domain** – enter the business domain to define which golden records will be enriched.

    1. **Method** – select the HTTP method (GET or POST) that will be used to retrieve data.

    1. **URL** – enter the URL of the external endpoint. This can be:

        - An external API endpoint (for example, DuckDuckGo) that returns data directly to the enricher, where it is processed using the **Process Response Script**.

        - A service endpoint (for example, Power Automate, Jupyter Notebook, or a Cloud Function) that acts as a wrapper for external APIs. These endpoints can call external APIs, process the responses internally, and return the final result to the enricher.

        You can use placeholders in **URL** to dynamically insert values at runtime:

        - `{APIKey}` – this placeholder will be replaced by the actual API key value provided in **API Key**.
    
        - `{Vocabulary:vocabularykey}` – this placeholder will be replaced with the value of the specified vocabulary key from the golden record. For example, if the URL contains `{Vocabulary:trainingcontact.country}` and the golden record contains `"trainingcontact.country": "Norway"`, the placeholder will be replaced with `Norway`.

        ![rest-api-enricher-2.png]({{ "/assets/images/preparation/enricher/rest-api-enricher-2.png" | relative_url }})

    1. **API Key** – enter the API key required to authenticate with the endpoint, if applicable. Provide this only if the API requires a key for access.

    1. **Headers** – enter any HTTP headers needed to call the endpoint. Enter one header per line in the format `Header-Name=value`.

    1. **Vocabulary and Properties** – enter the vocabulary keys and properties to include in the request payload, with one entry per line. These will be passed to the endpoint to retrieve the relevant data.

    1. **Process Request Script** – provide the JavaScript code used to construct or modify the request before it is sent to the external endpoint. You can find an example of the process request script in the [Sample scripts](#sample-process-request-script) section of this page.

    1. **Process Response Script** – provide the JavaScript code used to process the response returned from the external endpoint. This script is required to transform the API response into a format that the enricher can understand and use. You can find an example of the process response script in the [Sample scripts](#sample-process-response-script) section of this page.

    1. **Include Confidence Score** – decide whether the results will include a confidence score, which can be used during data processing.


1. Select **Test Connection** to make sure the enricher is properly configured, and then select **Add**.

    The REST API enricher is added and has an active status. This means that it will enrich relevant golden records during processing or when you trigger external enrichment.

After the REST API enricher is added, you can modify its details:

- **Settings** – add a user-friendly display name, select the description for data coming from the enricher, and define the source quality for determining the winning values.

- **Authentication** – modify the details you provided while configuring the enricher.

## View properties added by REST API enricher

You can find the properties added to golden records from the REST API enricher on the **Properties** page. The vocabulary keys added to golden records by the REST API enricher are grouped under **No Source** source type.

![rest-api-enricher-3.png]({{ "/assets/images/preparation/enricher/rest-api-enricher-3.png" | relative_url }})

For a more detailed information about the changes made to a golden record by the REST API enricher, check the corresponding data part on the **History** page.

![rest-api-enricher-4.png]({{ "/assets/images/preparation/enricher/rest-api-enricher-4.png" | relative_url }})

## Sample scripts

This section provides some sample scripts that you can use to configure the RESP API enricher.

### Sample process request script

```  
// sample request that can be accessed in the script
//  let request = {
//     ApiKey: "testApiKey",
//     Url: "testUrl",
//     Headers: [
//        { Key: "TestHeader", Value: "123"}
//     ],
//     Body: {
//        Properties: [{Key: "organization.name", Value: "CluedIn"}]
//     }
//   };
  
// Add Header
request.AddHeader('TestHeader2', '456');

let detailsArray = [];  
request.Body.Properties.forEach((x) => {
 detailsArray.push(x.Value)
});

// Update Body that will be sent to external api
request.Body = {
  names: detailsArray
}

//modified request
//  let request = {
//      ApiKey: "testArray",
//      Url: "testUrl",
//      Headers: [
//          { Key: "TestHeader", Value: "123"},
//          { Key: "TestHeader2", Value: "456"}
//      ],
//      Body: {
//          name: ["CluedIn"]
//      }
//  };
```

### Sample process response script

```
//  Sample response that returned from external api to enricher
//    const response = {
//        HttpStatus: "OK".
//        Content: "{\"fullName\": \"CluedIn ApS\"}",
//        Headers: [
//            { Key: "Connection", Value: "keep-alive"},
//            { Key: "Content-Type, Value "application/x-javascript"}",
//        ],
//    };

let parsedContent = JSON.parse(response.Content); 
let newContent = {
  "organization.fullName":parsedContent.fullName
};

// Data must be returned in the following format to be processed by enricher
// Score can be assigned with external api response
response.Content = JSON.stringify([{ Data: newContent, Score: 0 }]);  
  
// Sample response after executing the script
//    const response = {
//        HttpStatus: "OK",
//        Content: "[{\"Data\":{\"organization.fullName\":\"CluedIn Aps\"}, \"Score\":0}]",
//        ContentType: "application/x-javascript",
//        Headers: [
//            { Key: "Connection", Value: "keep-alive"},
//            { Key: "Content-Type", Value: "application/x-javscript",
//        ],
```

### Modifying request and response objects in process request and response scripts


| Name              | Type      | Description                                                                                          |
| ----------------- | --------- | ---------------------------------------------------------------------------------------------------- |
| `request`         | Request   | The current HTTP request object that can be modified during script execution.                        |
| `originalRequest` | Request   | The original, unmodified HTTP request for reference purposes.                                        |
| `response`        | Response  | The response from external endpoint that can be populated or modified by the script.                 |

**Request**

| Property  | Type            | Description                                   |
| --------- | --------------- | --------------------------------------------- |
| `Method`  | `string`        | The HTTP request method (e.g. `GET`, `POST`). |
| `Url`     | `string`        | The target URL for the HTTP request.          |
| `Headers` | `Array<Header>` | List of HTTP headers included in the request. |
| `ApiKey`  | `string`        | API key used for authenticating the request.  |
| `Body`    | `object`        | The body content of the HTTP request.         |

| Method      | Signature                                     | Description                       |
| ----------- | --------------------------------------------- | --------------------------------- |
| `addHeader` | `addHeader(key: string, value: string): void` | Adds a new header to the request. |

**Header**

| Property | Type     | Description   |
| -------- | -------- | ------------- |
| `Key`    | `string` | Header name.  |
| `Value`  | `string` | Header value. |

**Response**

| Property      | Type            | Description                                                                                               |
| ------------- | --------------- | --------------------------------------------------------------------------------------------------------- |
| `HttpStatus`  | `string`        | The HTTP status code of the response (e.g. `200 OK`).                                                     |
| `Content`     | `string`        | The raw response body content. Must be in **Result format** when returned to the enricher for processing. |
| `ContentType` | `string`        | The response content type (e.g. `application/json`).                                                      |
| `Headers`     | `Array<Header>` | List of HTTP headers included in the response.                                                            |


**Result (Format for Response Content for returning value to enricher)**

| Property | Type     | Description                                                                       |
| -------- | -------- | --------------------------------------------------------------------------------- |
| `Data`   | `object` | Key-value data extracted from the response. Each key represents a vocabulary key. |
| `Score`  | `number` | A numeric score indicating the relevance or confidence of the results.            |

### Helper functions
You can use the following helper functions in your scripts to facilitate common tasks.

**Logging**

| Function | Signature    | Description                                                                                     |
| -------- | ------------ | ----------------------------------------------------------------------------------------------- |
| `log`    | `log(value)` | Writes a message to the application log at **Information** level. Useful for debugging scripts. |

Example:
```
log("Processing response from API");
```

**String Encoding**

| Function     | Signature                           | Description                                    |
| ------------ | ----------------------------------- | ---------------------------------------------- |
| `toBase64`   | `toBase64(value: string): string`   | Encodes a UTF-8 string into Base64 format.     |
| `fromBase64` | `fromBase64(value: string): string` | Decodes a Base64-encoded string back to UTF-8. |
| `urlEncode`  | `urlEncode(value: string): string`  | Encodes a string for safe use in a URL.        |
| `urlDecode`  | `urlDecode(value: string): string`  | Decodes a URL-encoded string.                  |

Example: 
```
var encoded = stringEncoder.toBase64("hello");
var decoded = stringEncoder.fromBase64(encoded);
```

**Cache**

| Function | Signature                                                   | Description                                                                                                |
| -------- | ----------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `get`    | `get(key: string): object`                                  | Retrieves a cached value for the current organization. Returns `null` if not found.                        |
| `set`    | `set(key: string, value: object, expiration: number): void` | Stores a value in cache with an expiration time (in milliseconds). Does nothing if the key already exists. |

Example:
```
var token = cache.get("authToken");

if (!token) {
    token = "new-token";
    cache.set("authToken", token, 60000);
}
```

### Clearbit

This code takes a company name as input and sends it to the Clearbit Autocomplete API. Then, it extracts the domain and logo of the top matching company and returns that data in a structured format usable by the enricher.

**Method:** GET

**URL**

```
https://autocomplete.clearbit.com/v1/companies/suggest?query={Vocabulary:organization.name}
```

**Process response script**  

```
let parsedContent = JSON.parse(response.Content);
let content = parsedContent[0];
let image = {
  'clearbit.organization.domain': content.domain,
  'clearbit.organization.logo': content.logo,
};

response.Content = JSON.stringify([{ Data: image, Score: 0 }]);
log(JSON.stringify(response));
```

### Azure OpenAI

This code takes an organization's name and sends a request to Azure OpenAI GPT-4 asking it to translate the name into Japanese. Then, it ensures the model responds in a defined JSON format and parses and returns the result in a structure compatible with the enricher. Note that you can use the [Azure Open AI enricher](/preparation/enricher/azure-openai) for the same task.

**Method:** POST

**URL**

```
https://copilot2.openai.azure.com/openai/deployments/gpt-4-32k/chat/completions?api-version=2024-06-01
```

**Vocabulary key and properties**

```
organization.name
```

**Headers**

```
api-key={APIKey}
```

**Process request script**

```
let prompt = String.raw`Please get {organization.japaneseNameRestApi} by translating {Vocabulary:organization.name} into Japanese.
  
                    Response in JSON using the following template
                    ###
                    {
                        "organization.japaneseNameRestApi": ""
                    }
                    ###
  `;

  request.Body.Properties.forEach((x) => {
    prompt = prompt.replace('{Vocabulary:' + x.Key + '}', x.Value);
  });

  request.Body = {
    messages: [{ role: 'user', content: prompt }],
    temperature: 0,
  };
```

**Process response script**

```
let parsedContent = JSON.parse(response.Content);
let content = parsedContent.choices[0].message.content.trimEnd();
response.Content = JSON.stringify([{ Data: JSON.parse(content), Score: 0 }]);
log(JSON.stringify(response));
```

### DuckDuckGo

This script handles the JSON response returned by a DuckDuckGo API call. The main purpose is to extract useful information from the API response and transform it into a format usable by the enricher.

**Method:** GET

**URL**

```
https://api.duckduckgo.com?q={Vocabulary:organization.name}&format=json
```

**Process response script**

```
function extractStringValues(obj, dict = new Map()) {
  for (const [key, value] of Object.entries(obj)) {
    if (value && typeof value !== 'object' && !Array.isArray(value)) {
      dict.set('duckDuckGo.organization.' + key, value.toString());
    }
  }
  return dict;
}
function extractInfobox(content, dict = new Map()) {
  content?.forEach((x) => {
    dict.set('duckDuckGo.organization.infobox.' + x.label, x.value);
  });
}
function extractRelatedTopics(relatedTopics, dict = new Map()) {
  for (let i = 0; i < relatedTopics.length; i++) {
    dict.set(
      'duckDuckGo.organization.relatedTopics' + i + '.firstUrl',
      relatedTopics[i]?.FirstURL,
    );
    dict.set(
      'duckDuckGo.organization.relatedTopics' + i + '.text',
      relatedTopics[i]?.Text,
    );
    dict.set(
      'duckDuckGo.organization.relatedTopics' + i + '.icon',
      relatedTopics[i]?.Icon?.Url,
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
  log('Error caught:' + JSON.stringify(errorDetails));
}
```

### REST Countries

This code extracts the official name of a country from the response and formats it into a new JSON structure.

**Method:** GET

**URL**

```
https://restcountries.com/v3.1/name/{Vocabulary:country.country}?fullText=true
```

**Process response script**

```
let parsedContent = JSON.parse(response.Content);
let content = parsedContent[0];
let officialName = {
  'country.officialName': content.name.official,
};
response.Content = JSON.stringify([{ Data: officialName, Score: 0 }]);
log(JSON.stringify(response));
```

### Melissa

[Melissa](https://www.melissa.com/developer/global-address) is a widely used address validation and data quality service that helps organizations keep address data accurate, standardized, and up to date.

CluedIn can connect to Melissa through its REST API, sending address data for validation. The API responds with standardized and enriched results, which CluedIn processes and maps to the appropriate vocabulary keys for storage and further use.

In the following example, ingested company data contains missing or incorrect address details. We will use Melissa REST API calls to send address-related data stored in different vocabulary keys and enrich golden records with validated and parsed addresses.

![data-before-enrichment.png]({{ "/assets/images/preparation/enricher/rest-api/melissa/data-before-enrichment.png" | relative_url }})

**Configure Melissa REST API enricher**

To [add the Melissa REST API enricher](#add-rest-api-enricher), on the **Configure** tab, provide the following information:

- **Accepted Business Domain:** In this example, **/Address**.

- **Method:** GET.

- **URL:**

   In this example, the URL references several vocabulary keys that store address-related data.

    ```
    https://address.melissadata.net/V3/WEB/GlobalAddress/doGlobalAddress?id={APIKey}&a1={Vocabulary:company.address.streetAddress}&loc={Vocabulary:company.address.city}&admarea={Vocabulary:company.address.state}&ctry={Vocabulary:company.address.country}&postal={Vocabulary:company.address.zipcode}
    ```

- **Headers:**

    ```
    Content-Type=application/json
    ```

- **Process response script:**

    This script transforms the raw response into a structured format that fits CluedIn’s schema.

    ```
    let parsedContent = JSON.parse(response.Content); 
    let content=parsedContent.Records[0];
    
    let melissaCountryName=content.CountryName;
    let melissaCountryISO=content.CountryISO3166_1_Alpha3;
    let melissaZipcode=content.PostalCode;
    let melissaFullAddress =content.FormattedAddress;
    let melissaCity=content.Locality;
    let melissaState=content.AdministrativeArea;
    let melissaDeliveryIndicator=content.DeliveryIndicator;
    
    
    let newContent = {
      'company.address.city':melissaCity,
      'company.address.zipcode':melissaZipcode,
      'company.address.state':melissaState,
      'company.address.country':melissaCountryISO,
      'company.address.vocabKey2':melissaCountryName,
      'company.address.vocabKey1':melissaFullAddress,
      'company.address.type':melissaDeliveryIndicator,
    
    };
    
    //apply conditions if required
    
    if( melissaDeliveryIndicator==='B')
    {
       newContent[ 'company.address.type']='Business';
    }
    else if( melissaDeliveryIndicator==='R'){
       newContent['company.address.type']='Residential';
    }
    else{
       newContent['company.address.type']='Unknown';
    }
    
    response.Content = JSON.stringify([{ Data: newContent, Score: 0 }]);
    //log(JSON.stringify(response));
    ```

![configure_tab.png]({{ "/assets/images/preparation/enricher/rest-api/melissa/configure_tab.png" | relative_url }})

**Example of golden record before and after enrichment**

An example of a golden record before enrichment:

![golden_record_before_enrichment.png]({{ "/assets/images/preparation/enricher/rest-api/melissa/golden_record_before_enrichment.png" | relative_url }})

Same record after enrichment:

- The values for the **Type** and **Zipcode** properties were updated.

- Two new vocabulary keys (**Vocab Key 1** and **Vocab Key 2** were added).

![golden_record_after_enrichment.png]({{ "/assets/images/preparation/enricher/rest-api/melissa/golden_record_after_enrichment.png" | relative_url }})

**Sample response**

Provided below is an example of the response you would receive for the same request in Postman. If you need an additional address line in your golden records, select the relevant fields from the response and add them to the [process response script](#configure-melissa-rest-api-enricher) provided earlier on this page. For example, you could include the **Latitude** and **Longitude** fields.

- **URL:**

    ```
    https://address.melissadata.net/V3/WEB/GlobalAddress/doGlobalAddress?id=key&org=Walmart Inc.&a1=702 S.W. 8th St.&loc=Bentonville&admarea=AR&ctry=USA&postal=72716&act=check,verify&format=JSON
    ```
- **Response:**

    ```
    {
        "Version": "9.4.1.1228",
        "TransmissionReference": "",
        "TransmissionResults": "",
        "TotalRecords": "1",
        "Records": [
            {
                "RecordID": "1",
                "Results": "AC16,AV24,GS05",
                "FormattedAddress": "Walmart Inc.;702 SW 8th St;Bentonville AR  72716-6299",
                "Organization": "Walmart Inc.",
                "AddressLine1": "702 SW 8th St",
                "AddressLine2": "Bentonville AR  72716-6299",
                "AddressLine3": "",
                "AddressLine4": "",
                "AddressLine5": "",
                "AddressLine6": "",
                "AddressLine7": "",
                "AddressLine8": "",
                "SubPremises": "",
                "DoubleDependentLocality": "",
                "DependentLocality": "",
                "Locality": "Bentonville",
                "SubAdministrativeArea": "Benton",
                "AdministrativeArea": "AR",
                "PostalCode": "72716-6299",
                "PostalCodeType": "U",
                "AddressType": "F",
                "AddressKey": "72716629902",
                "SubNationalArea": "",
                "CountryName": "United States of America",
                "CountryISO3166_1_Alpha2": "US",
                "CountryISO3166_1_Alpha3": "USA",
                "CountryISO3166_1_Numeric": "840",
                "CountrySubdivisionCode": "US-AR",
                "Thoroughfare": "SW 8th St",
                "ThoroughfarePreDirection": "SW",
                "ThoroughfareLeadingType": "",
                "ThoroughfareName": "8th",
                "ThoroughfareTrailingType": "St",
                "ThoroughfarePostDirection": "",
                "DependentThoroughfare": "",
                "DependentThoroughfarePreDirection": "",
                "DependentThoroughfareLeadingType": "",
                "DependentThoroughfareName": "",
                "DependentThoroughfareTrailingType": "",
                "DependentThoroughfarePostDirection": "",
                "Building": "",
                "PremisesType": "",
                "PremisesNumber": "702",
                "SubPremisesType": "",
                "SubPremisesNumber": "",
                "PostBox": "",
                "Latitude": "36.363516",
                "Longitude": "-94.183177",
                "DeliveryIndicator": "U",
                "MelissaAddressKey": "2153275541",
                "MelissaAddressKeyBase": "",
                "PostOfficeLocation": "",
                "SubPremiseLevel": "",
                "SubPremiseLevelType": "",
                "SubPremiseLevelNumber": "",
                "SubBuilding": "",
                "SubBuildingType": "",
                "SubBuildingNumber": "",
                "UTC": "UTC-06:00",
                "DST": "Y",
                "DeliveryPointSuffix": "",
                "CensusKey": "050070205041002",
                "Extras": {}
            }
        ]
    }
    ```

### Duns and Bradstreet (D&B)
This code takes an organization’s DUNS number, or its name and country, and sends a request to the Dun & Bradstreet API to retrieve additional details. Before doing so, an enricher must be set up to obtain the authentication key.

**Authentication**

**Method:** POST

**URL**
```
https://plus.dnb.com/v2/token
```

**Process request script**
```
const authCacheKey = 'dnb_auth_token';
const cachedAuthToken = cache.Get(authCacheKey);

if (!cachedAuthToken) {
  const key =
    '{Consumer Key}';
  const secret =
    '{Consumer Secret}';

  const credentials = `${key}:${secret}`;

  const base64 = stringEncoder.toBase64(credentials);

  request.AddHeader('Content-Type', 'application/json');
  request.AddHeader('Authorization', `Basic ${base64}`);

  request.Body = { grant_type: 'client_credentials' };
} else {
  log('Auth token: ' + cachedAuthToken);
}
```

**Process response script**
```
try {
  let parsedContent = JSON.parse(response.Content);
  cache.Set(
    "dnb_auth_token",
    parsedContent.access_token,
    parsedContent.expiresIn * 1000
  );
  response.Content = JSON.stringify([{ Data: {}, Score: 0 }]);
} catch (error) {
  const errorDetails = {
    name: error?.name,
    message: error?.message,
    stack: error?.stack,
  };
  log("Authentication failed :" + JSON.stringify(errorDetails));
}
```


**Search using DUNS number**

**Method:** GET

**URL**

```
https://plus.dnb.com/v1/data/duns/{Vocabulary:testduns.dunsnumber}?blockIDs=companyfinancials_L1_v3,hierarchyconnections_L1_v1,companyinfo_L3_v1,companyinfo_identifiers_v1,esginsight_L3_v1
```

**Process request script**
```
const authCacheKey = 'dnb_auth_token';
const cachedAuthToken = cache.Get(authCacheKey);

if (cachedAuthToken) {
  request.AddHeader('Authorization', `Bearer ${cachedAuthToken}`);

  request.Body = { grant_type: 'client_credentials' };
} else {
  log('Unable to retrieve DnB auth token');
}
```

**Process response script**

```
function populateIndustryCodes(results, parsedContent) {
  const selectedTypes = ['19295', '37788'];

  const industryCodeValues =
    parsedContent?.organization?.industryCodes?.filter(
      x =>
        x?.typeDnBCode > 0 &&
        selectedTypes.includes(String(x.typeDnBCode))
    ) ?? [];

  if (industryCodeValues.length === 0) return;

  let industryCodesIndex = 0;
  for (const industryCode of industryCodeValues) {
      results[`Industry_${industryCodesIndex}_Description`] = industryCode.description;
      results[`Industry_${industryCodesIndex}_TypeDescription`] = industryCode.typeDescription;
      results[`Industry_${industryCodesIndex}_TypeDnBCode`] = industryCode.typeDnBCode;
      results[`Industry_${industryCodesIndex}_Priority`] = industryCode.priority;
      results[`Industry_${industryCodesIndex}_Code`] = industryCode.code;

      industryCodesIndex++;
    }
}

function populateOrganizationInfo(results, parsedContent) {
  const org = parsedContent?.organization;

  // DUNS Control Status
  if (org?.dunsControlStatus) {
    const status = org.dunsControlStatus;

    results.DunsControlStatusFullReportDate = status.fullReportDate;
    results.DunsControlStatusLastUpdateDate = status.lastUpdateDate;
    results.DunsControlStatusOperatingStatusDescription = status.operatingStatus?.description;
    results.DunsControlStatusOperatingStatusDnbCode = status.operatingStatus?.dnbCode;
    results.DunsControlStatusIsMarketable = status.isMarketable;
    results.DunsControlStatusIsMailUndeliverable = status.isMailUndeliverable;
    results.DunsControlStatusIsTelephoneDisconnected = status.isTelephoneDisconnected;
    results.DunsControlStatusIsDelisted = status.isDelisted;

    if (status?.operatingStatus) {
      results.OperatingStatusCode = status.operatingStatus?.dnbCode;
      results.OperatingStatusDescription = status.operatingStatus?.description;
    }
  }

  // DUNS Numbers
  results.Duns = org?.duns;
  results.DomesticUltimateDuns = org?.corporateLinkage?.domesticUltimate?.duns;
  results.GlobalUltimateDuns = org?.corporateLinkage?.globalUltimate?.duns;
  results.ParentDuns = org?.corporateLinkage?.parent?.duns;
  results.HeadQuarterDuns = org?.corporateLinkage?.headQuarter?.duns;

  // Business Information
  results.PrimaryBusinessName = org?.primaryName;
  results.BusinessEntityTypeDnbCode = org?.businessEntityType?.dnbCode;
  results.BusinessEntityTypeDescription = org?.businessEntityType?.description;

  // Trade Style Names
  const tradeStyleNames =
    org?.tradeStyleNames
      ?.map(t => t?.name)
      ?.filter(n => n && n.length > 0) ?? [];

  if (tradeStyleNames.length > 0) {
    results.TradeStyleNames = tradeStyleNames.join(" | ");
  }

  // Website
  const website = org?.websiteAddress?.[0];
  if (website) {
    results.WebsiteUrl = website.url;
  }

  // Telephone
  const telephone = org?.telephone?.[0];
  if (telephone?.isdCode && telephone?.telephoneNumber) {
    results.Telephone = `+${telephone.isdCode} ${telephone.telephoneNumber}`;
  }

  // Fax
  const fax = org?.fax?.[0];
  if (fax?.isdCode && fax?.faxNumber) {
    results.Fax = `+${fax.isdCode} ${fax.faxNumber}`;
  }

  // Stock Exchange
  const primaryStockExchange =
    org?.stockExchanges?.find(x => x?.isPrimary === true);

  if (primaryStockExchange) {
    results.StockExchangeTickerName = primaryStockExchange.tickerName;
    results.StockExchangeName = primaryStockExchange.exchangeName?.description;
    results.StockExchangeCountryCode = primaryStockExchange.exchangeCountry?.isoAlpha2Code;
  }

  // Registration Numbers
  const selectedRegistrationNumberTypes = ['2541'];

  if (selectedRegistrationNumberTypes.length > 0) {
    const registrationNumbers =
      org?.registrationNumbers?.filter(
        x =>
          x?.typeDnBCode > 0 &&
          selectedRegistrationNumberTypes.includes(
            String(x.typeDnBCode)
          )
      ) ?? [];

    let index = 0;
    for (const reg of registrationNumbers) {
      results[`RegistrationNumbers_${index}_RegistrationNumber`] = reg.registrationNumber;
      results[`RegistrationNumbers_${index}_TypeDescription`] = reg.typeDescription;
      results[`RegistrationNumbers_${index}_TypeDnBCode`] = reg.typeDnBCode;
      results[`RegistrationNumbers_${index}_RegistrationNumberClassDescription`] = reg.registrationNumberClass?.description;
      results[`RegistrationNumbers_${index}_RegistrationNumberClassDnbCode`] = reg.registrationNumberClass?.dnbCode;

      index++;
    }
  }

  // Corporate Linkage - Family Tree Roles Played
  let familyIndex = 0;
  for (const role of org?.corporateLinkage?.familytreeRolesPlayed ?? []) {
    results[`CorporateLinkageFamilyTreeRolesPlayedVocabulary_${familyIndex}_Description`] = role.description;
    results[`CorporateLinkageFamilyTreeRolesPlayedVocabulary_${familyIndex}_DnbCode`] = role.dnbCode;
    familyIndex++;
  }

  results.HierarchyLevel = org?.corporateLinkage?.hierarchyLevel;
  results.GlobalUltimateFamilyTreeMembersCount = org?.corporateLinkage?.globalUltimateFamilyTreeMembersCount;

  // Number of Employees
  results.NumberOfEmployees = org?.numberOfEmployees?.[0]?.value;
  results.GlobalUltimateNumberOfEmployees = org?.corporateLinkage?.globalUltimate?.numberOfEmployees?.[0]?.value;
  results.DomesticUltimateNumberOfEmployees = org?.corporateLinkage?.domesticUltimate?.numberOfEmployees?.[0]?.value;

  // Yearly Revenue
  const orgFinancial = org?.financials?.[0];
  const orgRevenue = orgFinancial?.yearlyRevenue?.[0];

  results.YearlyRevenue = orgRevenue && orgRevenue.currency
      ? `${orgRevenue.value} ${orgRevenue.currency}`
      : null;

  const globalUltimateFinancial = org?.globalUltimate?.financials?.[0];
  const globalUltimateRevenue = globalUltimateFinancial?.yearlyRevenue?.[0];

  results.GlobalUltimateYearlyRevenue = globalUltimateRevenue && globalUltimateRevenue.currency
      ? `${globalUltimateRevenue.value} ${globalUltimateRevenue.currency}`
      : null;

  const domesticUltimateFinancial = org?.domesticUltimate?.financials?.[0];
  const domesticUltimateRevenue = domesticUltimateFinancial?.yearlyRevenue?.[0];

  results.DomesticUltimateYearlyRevenue = domesticUltimateRevenue && domesticUltimateRevenue.currency
      ? `${domesticUltimateRevenue.value} ${domesticUltimateRevenue.currency}`
      : null;
}

function populatePrimaryAddresses(results, parsedContent) {
  const org = parsedContent?.organization;

  const domesticUltimateDuns = org?.corporateLinkage?.domesticUltimate?.duns;
  const globalUltimateDuns = org?.corporateLinkage?.globalUltimate?.duns;
  const parentDuns = org?.corporateLinkage?.parent?.duns;
  const headQuarterDuns = org?.corporateLinkage?.headQuarter?.duns;
  const duns = org?.duns;

  // Domestic Ultimate
  if (
    org?.corporateLinkage?.domesticUltimate?.primaryAddress &&
    domesticUltimateDuns &&
    domesticUltimateDuns !== duns
  ) {
    const addr = org.corporateLinkage.domesticUltimate.primaryAddress;

    results.DomesticUltimatePrimaryAddressCountry = addr.addressCountry?.name;
    results.DomesticUltimateISO2CountryCode = addr.addressCountry?.isoAlpha2Code;
    results.DomesticUltimatePrimaryAddressCountyName = addr.addressCounty?.name;
    results.DomesticUltimatePrimaryAddressLocality = addr.addressLocality?.name;
    results.DomesticUltimatePrimaryAddressPostalCode = addr.postalCode;
    results.DomesticUltimatePrimaryAddressRegionName = addr.addressRegion?.name;
    results.DomesticUltimatePrimaryAddressRegionAbbreviatedName = addr.addressRegion?.abbreviatedName;
    results.DomesticUltimatePrimaryAddressStreetLine1 = addr.streetAddress?.line1;
    results.DomesticUltimatePrimaryAddressStreetLine2 = addr.streetAddress?.line2;
  }

  // Global Ultimate
  if (
    org?.corporateLinkage?.globalUltimate?.primaryAddress &&
    globalUltimateDuns &&
    globalUltimateDuns !== duns
  ) {
    const addr = org.corporateLinkage.globalUltimate.primaryAddress;

    results.GlobalUltimatePrimaryAddressCountry = addr.addressCountry?.name;
    results.GlobalUltimateISO2CountryCode = addr.addressCountry?.isoAlpha2Code;
    results.GlobalUltimatePrimaryAddressCountyName = addr.addressCounty?.name;
    results.GlobalUltimatePrimaryAddressLocality = addr.addressLocality?.name;
    results.GlobalUltimatePrimaryAddressPostalCode = addr.postalCode;
    results.GlobalUltimatePrimaryAddressRegionName = addr.addressRegion?.name;
    results.GlobalUltimatePrimaryAddressRegionAbbreviatedName = addr.addressRegion?.abbreviatedName;
    results.GlobalUltimatePrimaryAddressStreetLine1 = addr.streetAddress?.line1;
    results.GlobalUltimatePrimaryAddressStreetLine2 = addr.streetAddress?.line2;
  }

  // Parent
  if (
    org?.corporateLinkage?.parent?.primaryAddress &&
    parentDuns &&
    parentDuns !== duns
  ) {
    const addr = org.corporateLinkage.parent.primaryAddress;

    results.ParentPrimaryAddressCountry = addr.addressCountry?.name;
    results.ParentISO2CountryCode = addr.addressCountry?.isoAlpha2Code;
    results.ParentPrimaryAddressCountyName = addr.addressCounty?.name;
    results.ParentPrimaryAddressLocality = addr.addressLocality?.name;
    results.ParentPrimaryAddressPostalCode = addr.postalCode;
    results.ParentPrimaryAddressRegionName = addr.addressRegion?.name;
    results.ParentPrimaryAddressRegionAbbreviatedName = addr.addressRegion?.abbreviatedName;
    results.ParentPrimaryAddressStreetLine1 = addr.streetAddress?.line1;
    results.ParentPrimaryAddressStreetLine2 = addr.streetAddress?.line2;
  }

  // HeadQuarter
  if (
    org?.corporateLinkage?.headQuarter?.primaryAddress &&
    headQuarterDuns &&
    headQuarterDuns !== duns
  ) {
    const addr = org.corporateLinkage.headQuarter.primaryAddress;

    results.HeadQuarterPrimaryAddressCountry = addr.addressCountry?.name;
    results.HeadQuarterISO2CountryCode = addr.addressCountry?.isoAlpha2Code;
    results.HeadQuarterPrimaryAddressCountyName = addr.addressCounty?.name;
    results.HeadQuarterPrimaryAddressLocality = addr.addressLocality?.name;
    results.HeadQuarterPrimaryAddressPostalCode = addr.postalCode;
    results.HeadQuarterPrimaryAddressRegionName = addr.addressRegion?.name;
    results.HeadQuarterPrimaryAddressRegionAbbreviatedName = addr.addressRegion?.abbreviatedName;
    results.HeadQuarterPrimaryAddressStreetLine1 = addr.streetAddress?.line1;
    results.HeadQuarterPrimaryAddressStreetLine2 = addr.streetAddress?.line2;
  }

  // Self
  if (!org?.primaryAddress) return;

  const primary = org.primaryAddress;

  results.PrimaryAddressCountry = primary.addressCountry?.name;
  results.ISO2CountryCode = primary.addressCountry?.isoAlpha2Code;
  results.PrimaryAddressCountyName = primary.addressCounty?.name;
  results.PrimaryAddressLocality = primary.addressLocality?.name;
  results.PrimaryAddressPostalCode = primary.postalCode;
  results.PrimaryAddressRegionName = primary.addressRegion?.name;
  results.PrimaryAddressRegionAbbreviatedName = primary.addressRegion?.abbreviatedName;
  results.PrimaryAddressStreetLine1 = primary.streetAddress?.line1;
  results.PrimaryAddressStreetLine2 = primary.streetAddress?.line2;
}

try {
  let parsedContent = JSON.parse(response.Content);
  let results = {};

  const confidenceScore = parsedContent?.matchCandidates?.[0]?.matchQualityInformation?.confidenceCode;
  populatePrimaryAddresses(results, parsedContent);
  populateOrganizationInfo(results, parsedContent);
  populateIndustryCodes(results, parsedContent);

  log('Parsed DnB Results: ' + JSON.stringify(results));
  response.Content = JSON.stringify([{ Data: results, Score: confidenceScore ? confidenceScore * 10 : 100 }]);
} catch (error) {
  const errorDetails = {
    name: error?.name,
    message: error?.message,
    stack: error?.stack,
  };
  log("Authentication failed :" + JSON.stringify(errorDetails));
}
```


**Search using Name and Country**

**Method:** GET

**URL**
```
https://plus.dnb.com/v1/match/extendedMatch?name={Vocabulary:testduns.account}&countryISOAlpha2Code={Vocabulary:testduns.adminregion}&blockIDs=companyfinancials_L1_v3,hierarchyconnections_L1_v1,companyinfo_L3_v1,companyinfo_identifiers_v1,esginsight_L3_v1
```

**Process request script**
```
const authCacheKey = 'dnb_auth_token';
const cachedAuthToken = cache.Get(authCacheKey);

if (cachedAuthToken) {
  request.AddHeader('Authorization', `Bearer ${cachedAuthToken}`);

  request.Body = { grant_type: 'client_credentials' };
} else {
  log('Unable to retrieve DnB auth token');
}
```


**Process response script**
```
function populateIndustryCodes(results, parsedContent) {
  const selectedTypes = ['19295', '37788'];

  const industryCodeValues =
    parsedContent?.embeddedProduct?.organization?.industryCodes?.filter(
      x =>
        x?.typeDnBCode > 0 &&
        selectedTypes.includes(String(x.typeDnBCode))
    ) ?? [];

  if (industryCodeValues.length === 0) return;

  let industryCodesIndex = 0;
  for (const industryCode of industryCodeValues) {
      results[`Industry_${industryCodesIndex}_Description`] = industryCode.description;
      results[`Industry_${industryCodesIndex}_TypeDescription`] = industryCode.typeDescription;
      results[`Industry_${industryCodesIndex}_TypeDnBCode`] = industryCode.typeDnBCode;
      results[`Industry_${industryCodesIndex}_Priority`] = industryCode.priority;
      results[`Industry_${industryCodesIndex}_Code`] = industryCode.code;

      industryCodesIndex++;
    }
}

function populateOrganizationInfo(results, parsedContent) {
  const org = parsedContent?.embeddedProduct?.organization;

  // DUNS Control Status
  if (org?.dunsControlStatus) {
    const status = org.dunsControlStatus;

    results.DunsControlStatusFullReportDate = status.fullReportDate;
    results.DunsControlStatusLastUpdateDate = status.lastUpdateDate;
    results.DunsControlStatusOperatingStatusDescription = status.operatingStatus?.description;
    results.DunsControlStatusOperatingStatusDnbCode = status.operatingStatus?.dnbCode;
    results.DunsControlStatusIsMarketable = status.isMarketable;
    results.DunsControlStatusIsMailUndeliverable = status.isMailUndeliverable;
    results.DunsControlStatusIsTelephoneDisconnected = status.isTelephoneDisconnected;
    results.DunsControlStatusIsDelisted = status.isDelisted;

    if (status?.operatingStatus) {
      results.OperatingStatusCode = status.operatingStatus?.dnbCode;
      results.OperatingStatusDescription = status.operatingStatus?.description;
    }
  }

  // DUNS Numbers
  results.Duns = org?.duns;
  results.DomesticUltimateDuns = org?.corporateLinkage?.domesticUltimate?.duns;
  results.GlobalUltimateDuns = org?.corporateLinkage?.globalUltimate?.duns;
  results.ParentDuns = org?.corporateLinkage?.parent?.duns;
  results.HeadQuarterDuns = org?.corporateLinkage?.headQuarter?.duns;

  // Business Information
  results.PrimaryBusinessName = org?.primaryName;
  results.BusinessEntityTypeDnbCode = org?.businessEntityType?.dnbCode;
  results.BusinessEntityTypeDescription = org?.businessEntityType?.description;

  // Trade Style Names
  const tradeStyleNames =
    org?.tradeStyleNames
      ?.map(t => t?.name)
      ?.filter(n => n && n.length > 0) ?? [];

  if (tradeStyleNames.length > 0) {
    results.TradeStyleNames = tradeStyleNames.join(" | ");
  }

  // Website
  const website = org?.websiteAddress?.[0];
  if (website) {
    results.WebsiteUrl = website.url;
  }

  // Telephone
  const telephone = org?.telephone?.[0];
  if (telephone?.isdCode && telephone?.telephoneNumber) {
    results.Telephone = `+${telephone.isdCode} ${telephone.telephoneNumber}`;
  }

  // Fax
  const fax = org?.fax?.[0];
  if (fax?.isdCode && fax?.faxNumber) {
    results.Fax = `+${fax.isdCode} ${fax.faxNumber}`;
  }

  // Stock Exchange
  const primaryStockExchange =
    org?.stockExchanges?.find(x => x?.isPrimary === true);

  if (primaryStockExchange) {
    results.StockExchangeTickerName = primaryStockExchange.tickerName;
    results.StockExchangeName = primaryStockExchange.exchangeName?.description;
    results.StockExchangeCountryCode = primaryStockExchange.exchangeCountry?.isoAlpha2Code;
  }

  // Registration Numbers
  const selectedRegistrationNumberTypes = ['2541'];

  if (selectedRegistrationNumberTypes.length > 0) {
    const registrationNumbers =
      org?.registrationNumbers?.filter(
        x =>
          x?.typeDnBCode > 0 &&
          selectedRegistrationNumberTypes.includes(
            String(x.typeDnBCode)
          )
      ) ?? [];

    let index = 0;
    for (const reg of registrationNumbers) {
      results[`RegistrationNumbers_${index}_RegistrationNumber`] = reg.registrationNumber;
      results[`RegistrationNumbers_${index}_TypeDescription`] = reg.typeDescription;
      results[`RegistrationNumbers_${index}_TypeDnBCode`] = reg.typeDnBCode;
      results[`RegistrationNumbers_${index}_RegistrationNumberClassDescription`] = reg.registrationNumberClass?.description;
      results[`RegistrationNumbers_${index}_RegistrationNumberClassDnbCode`] = reg.registrationNumberClass?.dnbCode;

      index++;
    }
  }

  // Corporate Linkage - Family Tree Roles Played
  let familyIndex = 0;
  for (const role of org?.corporateLinkage?.familytreeRolesPlayed ?? []) {
    results[`CorporateLinkageFamilyTreeRolesPlayedVocabulary_${familyIndex}_Description`] = role.description;
    results[`CorporateLinkageFamilyTreeRolesPlayedVocabulary_${familyIndex}_DnbCode`] = role.dnbCode;
    familyIndex++;
  }

  results.HierarchyLevel = org?.corporateLinkage?.hierarchyLevel;
  results.GlobalUltimateFamilyTreeMembersCount = org?.corporateLinkage?.globalUltimateFamilyTreeMembersCount;

  // Number of Employees
  results.NumberOfEmployees = org?.numberOfEmployees?.[0]?.value;
  results.GlobalUltimateNumberOfEmployees = org?.corporateLinkage?.globalUltimate?.numberOfEmployees?.[0]?.value;
  results.DomesticUltimateNumberOfEmployees = org?.corporateLinkage?.domesticUltimate?.numberOfEmployees?.[0]?.value;

  // Yearly Revenue
  const orgFinancial = org?.financials?.[0];
  const orgRevenue = orgFinancial?.yearlyRevenue?.[0];

  results.YearlyRevenue = orgRevenue && orgRevenue.currency
      ? `${orgRevenue.value} ${orgRevenue.currency}`
      : null;

  const globalUltimateFinancial = org?.globalUltimate?.financials?.[0];
  const globalUltimateRevenue = globalUltimateFinancial?.yearlyRevenue?.[0];

  results.GlobalUltimateYearlyRevenue = globalUltimateRevenue && globalUltimateRevenue.currency
      ? `${globalUltimateRevenue.value} ${globalUltimateRevenue.currency}`
      : null;

  const domesticUltimateFinancial = org?.domesticUltimate?.financials?.[0];
  const domesticUltimateRevenue = domesticUltimateFinancial?.yearlyRevenue?.[0];

  results.DomesticUltimateYearlyRevenue = domesticUltimateRevenue && domesticUltimateRevenue.currency
      ? `${domesticUltimateRevenue.value} ${domesticUltimateRevenue.currency}`
      : null;
}

function populatePrimaryAddresses(results, parsedContent) {
  const org = parsedContent?.embeddedProduct?.organization;

  const domesticUltimateDuns = org?.corporateLinkage?.domesticUltimate?.duns;
  const globalUltimateDuns = org?.corporateLinkage?.globalUltimate?.duns;
  const parentDuns = org?.corporateLinkage?.parent?.duns;
  const headQuarterDuns = org?.corporateLinkage?.headQuarter?.duns;
  const duns = org?.duns;

  // Domestic Ultimate
  if (
    org?.corporateLinkage?.domesticUltimate?.primaryAddress &&
    domesticUltimateDuns &&
    domesticUltimateDuns !== duns
  ) {
    const addr = org.corporateLinkage.domesticUltimate.primaryAddress;

    results.DomesticUltimatePrimaryAddressCountry = addr.addressCountry?.name;
    results.DomesticUltimateISO2CountryCode = addr.addressCountry?.isoAlpha2Code;
    results.DomesticUltimatePrimaryAddressCountyName = addr.addressCounty?.name;
    results.DomesticUltimatePrimaryAddressLocality = addr.addressLocality?.name;
    results.DomesticUltimatePrimaryAddressPostalCode = addr.postalCode;
    results.DomesticUltimatePrimaryAddressRegionName = addr.addressRegion?.name;
    results.DomesticUltimatePrimaryAddressRegionAbbreviatedName = addr.addressRegion?.abbreviatedName;
    results.DomesticUltimatePrimaryAddressStreetLine1 = addr.streetAddress?.line1;
    results.DomesticUltimatePrimaryAddressStreetLine2 = addr.streetAddress?.line2;
  }

  // Global Ultimate
  if (
    org?.corporateLinkage?.globalUltimate?.primaryAddress &&
    globalUltimateDuns &&
    globalUltimateDuns !== duns
  ) {
    const addr = org.corporateLinkage.globalUltimate.primaryAddress;

    results.GlobalUltimatePrimaryAddressCountry = addr.addressCountry?.name;
    results.GlobalUltimateISO2CountryCode = addr.addressCountry?.isoAlpha2Code;
    results.GlobalUltimatePrimaryAddressCountyName = addr.addressCounty?.name;
    results.GlobalUltimatePrimaryAddressLocality = addr.addressLocality?.name;
    results.GlobalUltimatePrimaryAddressPostalCode = addr.postalCode;
    results.GlobalUltimatePrimaryAddressRegionName = addr.addressRegion?.name;
    results.GlobalUltimatePrimaryAddressRegionAbbreviatedName = addr.addressRegion?.abbreviatedName;
    results.GlobalUltimatePrimaryAddressStreetLine1 = addr.streetAddress?.line1;
    results.GlobalUltimatePrimaryAddressStreetLine2 = addr.streetAddress?.line2;
  }

  // Parent
  if (
    org?.corporateLinkage?.parent?.primaryAddress &&
    parentDuns &&
    parentDuns !== duns
  ) {
    const addr = org.corporateLinkage.parent.primaryAddress;

    results.ParentPrimaryAddressCountry = addr.addressCountry?.name;
    results.ParentISO2CountryCode = addr.addressCountry?.isoAlpha2Code;
    results.ParentPrimaryAddressCountyName = addr.addressCounty?.name;
    results.ParentPrimaryAddressLocality = addr.addressLocality?.name;
    results.ParentPrimaryAddressPostalCode = addr.postalCode;
    results.ParentPrimaryAddressRegionName = addr.addressRegion?.name;
    results.ParentPrimaryAddressRegionAbbreviatedName = addr.addressRegion?.abbreviatedName;
    results.ParentPrimaryAddressStreetLine1 = addr.streetAddress?.line1;
    results.ParentPrimaryAddressStreetLine2 = addr.streetAddress?.line2;
  }

  // HeadQuarter
  if (
    org?.corporateLinkage?.headQuarter?.primaryAddress &&
    headQuarterDuns &&
    headQuarterDuns !== duns
  ) {
    const addr = org.corporateLinkage.headQuarter.primaryAddress;

    results.HeadQuarterPrimaryAddressCountry = addr.addressCountry?.name;
    results.HeadQuarterISO2CountryCode = addr.addressCountry?.isoAlpha2Code;
    results.HeadQuarterPrimaryAddressCountyName = addr.addressCounty?.name;
    results.HeadQuarterPrimaryAddressLocality = addr.addressLocality?.name;
    results.HeadQuarterPrimaryAddressPostalCode = addr.postalCode;
    results.HeadQuarterPrimaryAddressRegionName = addr.addressRegion?.name;
    results.HeadQuarterPrimaryAddressRegionAbbreviatedName = addr.addressRegion?.abbreviatedName;
    results.HeadQuarterPrimaryAddressStreetLine1 = addr.streetAddress?.line1;
    results.HeadQuarterPrimaryAddressStreetLine2 = addr.streetAddress?.line2;
  }

  // Self
  if (!org?.primaryAddress) return;

  const primary = org.primaryAddress;

  results.PrimaryAddressCountry = primary.addressCountry?.name;
  results.ISO2CountryCode = primary.addressCountry?.isoAlpha2Code;
  results.PrimaryAddressCountyName = primary.addressCounty?.name;
  results.PrimaryAddressLocality = primary.addressLocality?.name;
  results.PrimaryAddressPostalCode = primary.postalCode;
  results.PrimaryAddressRegionName = primary.addressRegion?.name;
  results.PrimaryAddressRegionAbbreviatedName = primary.addressRegion?.abbreviatedName;
  results.PrimaryAddressStreetLine1 = primary.streetAddress?.line1;
  results.PrimaryAddressStreetLine2 = primary.streetAddress?.line2;
}

try {
  let parsedContent = JSON.parse(response.Content);
  let results = {};

  const confidenceScore = parsedContent?.matchCandidates?.[0]?.matchQualityInformation?.confidenceCode;
  populatePrimaryAddresses(results, parsedContent);
  populateOrganizationInfo(results, parsedContent);
  populateIndustryCodes(results, parsedContent);

  log('Parsed DnB Results: ' + JSON.stringify(results));
  response.Content = JSON.stringify([{ Data: results, Score: confidenceScore ? confidenceScore * 10 : 100 }]);
} catch (error) {
  const errorDetails = {
    name: error?.name,
    message: error?.message,
    stack: error?.stack,
  };
  log("Authentication failed :" + JSON.stringify(errorDetails));
}
```