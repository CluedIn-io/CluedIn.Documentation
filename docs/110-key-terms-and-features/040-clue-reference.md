---
layout: default
title: Clue reference
parent: Key terms and features
permalink: /key-terms-and-features/clue-reference
nav_order: 1
has_children: false
tags: ["record", "clue", "golden record"]
---
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

In this article, you will learn about a clue—an integral part of the data life cycle in CluedIn. Understanding how to interpret clues is important to ensure that they contain all the necessary details for successful processing and creation of golden records.

<div style="padding:56.25% 0 0 0;position:relative;">
<iframe src="https://player.vimeo.com/video/901142502?h=12b6e293b7&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" style="position:absolute;top:0;left:0;width:100%;height:100%;" title="Clue reference"></iframe>
</div>

## Clue overview

Clue is an object model in JSON format that CluedIn generates for your records as a result of mapping. Clue represents a transitional stage between the ingested record and the resulting golden record. Essentially, a clue is what CluedIn can process in order to produce a golden record.

After you create the mapping, you can generate clues and take a look at their structure.

**To generate clues**

1. Go to the **Processing** tab of the data set.

1. Near the upper-right corner of the table, select the vertical ellipsis button, and then select **Generate sample clues**.

    A JSON file with all clues created from your data set is downloaded to your computer. You can open the file in any text editor.

It is a good idea to check the clues before processing to make sure they contain all the necessary details so that identical clues can be merged by codes, thus reducing the number of duplicates in the system. You can do the following:

- Check if the codes are correct.

- Check if the property and pre-process rules have been applied as intended.

- Check if the code written in advanced mapping has been applied as intended.

<details>
    <summary>Click here to view the clue sample</summary>
    
```
{
"clue": {
      "attribute-organization": "cafab9fd-7185-4f37-a753-20ec9ed71a2c",
      "attribute-origin": "/Customer#customers_smallcopycsv:1",
      "attribute-appVersion": "2.17.0.0",
      "clueDetails": {
        "data": {
          "attribute-originProviderDefinitionId": "03B88B70-D11F-4572-8F3D-AB6260610498",
          "attribute-origin": "/Customer#customers_smallcopycsv:1",
          "attribute-appVersion": "2.17.0.0",
          "attribute-inputSource": "cluedin-annotation",
          "entityData": {
            "name": "Grace Acton",
            "description": "",
            "entityType": "/Customer",
            "attribute-origin": "/Customer#customers_smallcopycsv:1",
            "attribute-appVersion": "2.17.0.0",
            "attribute-source": "cafab9fd-7185-4f37-a753-20ec9ed71a2c",
            "codes": [
              "/Customer#File Data Source:CluedIn(hash-sha1):f333b1b1269a730fcf756ddbdf776d52edfb9f24",
              "/Customer#cluedin(email):gactony@bravesites.com"
            ],
            "edges": {
              "outgoing": [
                {
                  "attribute-from": "C:/Customer#customers_smallcopycsv:1",
                  "attribute-type": "/WorksFor",
                  "attribute-to": "C:/Company#companiescsv:2"
                }
              ]
            },
            "properties": {
              "attribute-type": "/Metadata/KeyValue",
              "property-customer.id": "1",
              "property-customer.firstName": "Grace",
              "property-customer.lastName": "Acton",
              "property-customer.fullName": "Grace Acton",
              "property-customer.email": "gactony@bravesites.com",
              "property-customer.country": "CN",
              "property-customer.companyId": "2"
            }
          }
        }
      }
    }
  }
```
</details>

## Clue properties

The following table contains the properties that you can find in the clue.

| Property | Description |
|--|--|
| `attribute-organization` | GUID of the organization. |
| `attribute-origin` | Entity origin code of the clue as defined in the mapping details. It is the primary identifier that uniquely represents the clue. This property appears in several places in the clue structure. |
| `attribute-appVersion` | Version of the clue schema. This property appears in several places in the clue structure. |
| `attribute-originProviderDefinitionId` | GUID of the source that sent the data to CluedIn. The source can be a file, a database, an endpoint, a manual data entry project, and so on. Each source in CluedIn has a provider definition ID. The provider definition ID is used to restrict or grant user access to a specific data source.  |
| `attribute-inputSource` | System that pushed the clue. Usually, the clue is created as a result of the mapping process, which is represented by the `cluedin-annotation` service.  |
| `name` | Name of the clue. The name is shown on the search results page and on the golden record details page. |
| `description` | Description of the clue. The description is shown in the default search results view and on the golden record details page. |
| `entityType` | A common attribute that defines the business domain that the clue belongs to. The selection of the entity type is part of the mapping process. |
| `attributeSource` | A service source of the clue. |
| `codes` | Additional unique identifiers of the clue as defined in the mapping details. |
| `edges` | An object that represents a specific relation (`attribute-type`) between the source clue (`attribute-from`) and the target clue (`attribute-to`), identified through their entity origin codes. |
| `properties` | An object (also called a _property bag_) that contains all the properties (vocabulary keys) of the clue. |
| `attribute-type` | A format of data in the property bag. |
| `aliases` | A value used as an alternative or secondary name associated with the clue. |
| `tags` | A value used as a label to categorize clues across entity types. |
| `createdDate` | Date when the record was created in the source system. |
| `modifiedDate` | Date when the record was modified in the source system. |
| `quarantine` | Metadata information about the rules that were applied to the clue to send it to quarantine. |