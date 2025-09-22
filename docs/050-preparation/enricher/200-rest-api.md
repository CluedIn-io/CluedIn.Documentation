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
//     Header: [{Key:"TestHeader", Value: 123}],
//     Body: {
//        Properties: [{Key: "organization.name", Value: "CluedIn"}]
//     }
//   };
  
let detailsArray = [];  
request.Body.Properties.forEach((x) => {
 detailsArray.push(x.Value)
});
  
request.Body = {
  names: detailsArray
}

//modified request
//  let request = {
//      ApiKey: "testArray",
//      Url: "testUrl",
//      Header: [{Key:"TestHeader", Value: 123}],
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
  ‘organization.fullName':parsedContent.fullName
};
response.Content = JSON.stringify([{ Data: newContent), Score: 0 }]);  
  
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

#### Configure Melissa REST API enricher

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
    
    if ( melissaDeliveryIndicator==='B')
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

#### Example of golden record before and after enrichment

An example of a golden record before enrichment:

![golden_record_before_enrichment.png]({{ "/assets/images/preparation/enricher/rest-api/melissa/golden_record_before_enrichment.png" | relative_url }})

Same record after enrichment:

- The values for the **Type** and **Zipcode** properties were updated.

- Two new vocabulary keys (**Vocab Key 1** and **Vocab Key 2** were added).

![golden_record_after_enrichment.png]({{ "/assets/images/preparation/enricher/rest-api/melissa/golden_record_after_enrichment.png" | relative_url }})

#### Sample response

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
