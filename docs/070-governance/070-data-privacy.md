---
layout: cluedin
title: Data Privacy
parent: Governance
nav_order: 070
has_children: false
permalink: /governance/data-privacy
tags: ["governance","data-privacy"]
published: false
---

CluedIn detects PII data by default. Here is a description of how it is implemented.

![Diagram](../assets/images/governance/intro-compliance.png)  

Data Extractors

Implemented data extractors:

```csharp
BitcoinAddressDataExtractor
CreditCardDataExtractor
CurrencyDataExtractor
EmailDataExtractor
IBANDataExtractor
IpAddressDataExtractor
NamedEntityDataExtractor
NationalIdDataExtractor
PhoneNumberDataExtractor
UncDataExtractor
UriDataExtractor
Data Classification Types
```
You can implement your own new PII detection rules, and can use the above implementations as guides on how to achieve that. 

Type list:

```csharp
/None
/DocumentBody
/Email
/Uri
/Unc
/PhoneNumber
/PassportNo
/OrganizationName
/Identifier
/SocialMediaIdentifier
/IPAddress
/TimeZone
/Tag
/JobTitle
/Date
/Currency
/EmployeeId
/MessagingIdentifier
/WebProfile
/HRData
/CreditCard/Number
/NationalId
/Person/Name
/Person/FirstName
/Person/MiddleName
/Person/LastName
/Person/MaidenName
/Person/Gender
/Person/Birthday
/Person/Age
/Person/Identifier
/SSN
/SSN/DK
/SSN/US
/Location
/Location/Geocode
/Location/Address
/Location/PostalCode
/Geography
/Geography/City
/Geography/Country
/Geography/State
/Employment
/Employment/Status
/Finance
/Finance/BankAccount
/Finance/BankAccount/IBAN
/Finance/BankAccount/AccountNumber
/CryptoCurrency
/CryptoCurrency/BitcoinAddress
```
Extension to the entity level processed data

```xml
        <dataDescription>
        	<dataClasses>
        		<class type="/documentBody" />
        		<class type="/emailAddress" />
        		<class type="/uri" />
        		<class type="/personName" />
        		<class type="/phoneNumber" />
        		<class type="/ssn" />
        		<class type="/ssn/dk" />
        	</dataClasses>
        </dataDescription>
        ```
DataClassificationTypeMetric

Measures instance counts of found data classification types.
For example an entity containing the content tiw@cluedin.com, pid@cluedin.com, msh@cluedin.com
will result in a measurement of 3 email addresses.

Individual unique instances of data is measured, only the data class of the found is measured.

                                                                    Dimension Table:

                                                                  | DimensionType         | DetailType             | ProviderDefinitionId | ProviderId | Detail              | Persistence                       |
                                                                  |-----------------------|------------------------|----------------------|------------|---------------------|-----------------------------------|
 Global Data Classification                                       | Global                | DataClassificationType |                      |            | Classification Type | EntityMetric                      |
  │  Global Provider Data Classification                          | GlobalIntegrationType | DataClassificationType |                      | Id         | Classification Type | EntityMetric                      |
  │   │  Global Provider Definition Data Classification           | GlobalIntegration     | DataClassificationType | Id                   | Id         | Classification Type | EntityMetric                      |
  │   │   │                                                       |-----------------------|------------------------|----------------------|------------|---------------------|-----------------------------------|
  └───│───│────── Entity Data Classification                      | Entity                | DataClassificationType |                      |            | Classification Type | EntityMetric                      |
      │   └────── Entity Provider Data Classification             | EntityIntegrationType | DataClassificationType |                      | Id         | Classification Type | EntityMetric                      |
      └────────── Entity Provider Definition Data Classification  | EntityIntegration     | DataClassificationType | Id                   | Id         | Classification Type | EntityMetric                      |
GraphQL example

Get the id for the /CreditCard/Number dimension

SELECT 
      *
  FROM [dbo].[Dimension]
  WHERE DetailType = 4 AND Type = 1 AND Detail = '/CreditCard/Number'
or from graph ql

dataclassificationtype: metrics(names: ["dataclassificationtype"])
{
   dimensions
   {
      id
      type
      detailType
      detail
   }
}
Get values for /CreditCard/Number dimension

```json
dataclassificationtype: metrics(names: ["dataclassificationtype"]) 
  {
    globalLevel: dimension(id : "11431454-A2BA-5F3C-94A2-17067A18EF23")
    {
      id
      type
      detailType
      detail
      ... on GlobalMetricDimension
      {
        children
        {
          id
      		type
      		detailType
      		detail
          entityValues
          {
            cursor
            entries
            {
              value
              entity
              {
                id
                name
                entityType
              }
            }
          }
        }
      }
    }
  }
  ```
Output

```json
   "dataclassificationtype": [
      {
        "globalLevel": {
          "id": "11431454-a2ba-5f3c-94a2-17067a18ef23",
          "type": "GLOBAL",
          "detailType": "DATA_CLASSIFICATION_TYPE",
          "detail": "/CreditCard/Number",
          "children": [
            {
              "id": "bc9d7576-2a8a-50d6-a479-e4b885d1b9e4",
              "type": "ENTITY",
              "detailType": "DATA_CLASSIFICATION_TYPE",
              "detail": "/CreditCard/Number",
              "entityValues": {
                "cursor": "ewAiAFAAYQBnAGUAIgA6ADEALAAiAFAAYQBnAGUAUwBpAHoAZQAiADoAMgAwAH0A",
                "entries": [
                  {
                    "value": {
                      "entityId": "ec4950e5-413d-54ef-92d4-014e969ecab0",
                      "value": 1
                    },
                    "entity": {
                      "id": "ec4950e5-413d-54ef-92d4-014e969ecab0",
                      "name": null,
                      "entityType": "/Mail"
                    }
                  }
                ]
              }
            }
          ]
        }
      }
    ]
```