---
layout: cluedin
title: Clue reference
parent: Key terms and features
permalink: /key-terms-and-features/clue-reference
nav_order: 2
has_children: false
tags: ["clue"]
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article, you will learn about a clue—an integral part of the data life cycle in CluedIn. Understanding how to interpret clues is important to ensure that they contain all the necessary details for successful processing and creation of golden records.

<div class="videoFrame">
<iframe src="https://player.vimeo.com/video/901142502?h=12b6e293b7&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" title="Clue reference"></iframe>
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

## Clue sample

```json
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

## Clue properties

The following table contains the properties that you can find in the clue.

| Property | Description |
|--|--|
| `attribute-organization` | GUID of the organization. |
| `attribute-origin` | Entity origin code of the clue as defined in the mapping details. It is the primary identifier that uniquely represents the clue. This property appears in several places in the clue structure. |
| `attribute-appVersion` | Version of the clue schema. This property appears in several places in the clue structure. |
| `attribute-originProviderDefinitionId` | GUID of the source that sent the data to CluedIn. The source can be a file, a database, an ingestion endpoint, a manual data entry project, and so on. Each source in CluedIn has a provider definition ID. The provider definition ID is used to restrict or grant user access to a specific data source.  |
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

## Ignoring insignificant changes

When CluedIn processes clues, it will generate a Hash value that will take certain values on the clue and create a unique value that represents a hash of those values. 

By default, all changes and properties in a clue are treated as something that will play a role in the hashing process. Developers can instruct Vocabularies to "Ignore Hashing", which means that even if these values change on subsequent crawls, it won't play a role in telling CluedIn that the data has changed. Only properties that have changed or been added that are not marked with "Ignore Hashing" will instruct CluedIn that things have changed. 

For example, many tools will change a timestamp value when the record has been viewed - not modified, but simply opened or viewed. You might find that this is important to change the clue, but in many occasions you will find that this change is insignificant and you will want to use your Vocabulary mappings to instruct CluedIn to ignore this change and throw away the clue from processing. This is typically to help increase the performance and lack of load placed onto the CluedIn processing servers. 

## Advanced operations with clues

This section contains information about posting clues via REST POST requests. It is intended for experienced technical users.

To post clues to CluedIn, use the following post URL: `{{baseurl}}/public/api/v2/clue?save=true`, where `baseurl` is the address of your CluedIn instance. In the request's header, add the **Authorization** key with the value `Bearer {{apitoken}}`, where `apitoken` is your API token that you can find in **Administration** > **API Tokens**.

### Delta clues and why you may need them

By default, CluedIn works in "Append" mode, where as new data comes in, it will append the data over the top of existing data that has a matching Entity Code or will create new Golden records where there is no matching Entity Code.

There are situations where you actually don't want your new data to be in "Append" mode, but rather you want to change the way that CluedIn will process and treat this data.

The most common examples include:

 - You are sending data to CluedIn with the intention to delete it from CluedIn and/or downstream Export Targets as well.

 - You are sending data to CluedIn with "Blank Values" and your intention is to ask CluedIn to "forget" that this column or columns ever had a value for this. For example, you had a phone number from a company and you would rather now have a blank value for this as the phone number is no longer active. 

 - You are sending data to CluedIn with an updated value for a column and your intention is to ask CluedIn to **REMOVE** the old Entity Code or Edge that could have been built off of this, and **REPLACE** it with the new ones, not just **APPEND** over the top.

 - You are sending blank data to CluedIn and you actually want CluedIn to treat the values as Blank and hence if a Golden Record has a value of "Hello" you actually want to turn that value into "".


### Delta data actions in clues

You can post clues that remove outgoing or incoming edges from golden records. Following is an example of a clue that removes an outgoing edge from a golden record.


### Remove Edge

```
{
  "clue": {
    "attribute-organization": "{{org_id}}",
    "attribute-origin": "/Person#Newman:{{DeltaClues_EntityA_Id}}",
    "clueDetails": {
      "deltaData": {
        "attribute-persistHash": "hwcrydlp+4jrs1dqu2io9w==",
        "attribute-appVersion": "2.17.0.0",
        "processingFlags": {},
        "deltaDataActions": {
          "action": {
            "attribute-type": "/DataAction/Edit",
            "modifications": {
              "remove": {
                "attribute-target": "OutgoingEdges",
                "attribute-referenceKey": "/EdgeType, Entity {{DeltaClues_EntityB_Id}}§C:/Person#Newman:{{DeltaClues_EntityB_Id}}"
              }
            }
          }
        },
        "entityData": {
          "entityType": "/Person",
          "codes": [
            "/Person#Newman:{{DeltaClues_EntityA_Id}}"
          ],
          "modifiedDate": "{{timestamp}}",
          "edges": {},
          "edgesSummary": {},
          "properties": {
            "attribute-type": "/Metadata/KeyValue",
            "property-hierarchy.lastUpdated": "{{timestamp}}"
          },
          "attribute-id": "6",
          "attribute-origin": "/Person#Newman:{{DeltaClues_EntityA_Id}}"
        },
        "dataActions": {},
        "processedData": {
          "edges": {},
          "edgesSummary": {},
          "properties": {
            "attribute-type": "/Metadata/KeyValue"
          },
          "attribute-ref": "6",
          "attribute-origin": "/Person#Newman:{{DeltaClues_EntityA_Id}}",
          "sortDate": "{{timestamp}}",
          "timeToLive": "0",
          "isShadowEntity": "False"
        }
      },
      "references": {}
    }
  }
}
```

### Remove Edge and Add Edge in same Clue (equivelant of an Update)

```
{
  "clue": {
    "attribute-organization": "{{org_id}}",
    "attribute-origin": "/Person#Newman:{{DeltaClues_EntityA_Id}}",
    "clueDetails": {
      "data": {
        "attribute-persistHash": "b5bvwamo85acabdz5xyb1g==",
        "attribute-appVersion": "2.17.0.0",
        "processingFlags": {},
        "deltaDataActions": {
          "action": {
            "attribute-type": "/DataAction/Edit",
            "modifications": {
              "remove": {
                "attribute-target": "OutgoingEdges",
                "attribute-referenceKey": "/HRCHY_test, Entity {{DeltaClues_EntityB_Id}}§C:/Person#Newman:{{DeltaClues_EntityB_Id}}"
              }
            }
          }
        },
        "entityData": {
          "entityType": "/Person",
          "codes": [
            "/Person#Newman:{{DeltaClues_EntityA_Id}}"
          ],
          "modifiedDate": "{{timestamp}}",
          "edges": {
            "outgoing": [
              {
                "attribute-type": "/HRCHY_test",
                "attribute-creationOptions": "Default",
                "attribute-from": "C:/Person#Newman:{{DeltaClues_EntityA_Id}}",
                "attribute-to": "C:/Person#Newman:{{DeltaClues_EntityC_Id}}",
                "property-CreatedAt": "{{timestamp}}"
              }
            ]
          },
          "edgesSummary": {},
          "attribute-id": "6",
          "attribute-origin": "/Person#Newman:{{DeltaClues_EntityA_Id}}"
        },
        "dataActions": {},
        "processedData": {
          "edges": {},
          "edgesSummary": {},
          "attribute-ref": "6",
          "attribute-origin": "/Person#Newman:{{DeltaClues_EntityA_Id}}",
          "sortDate": "{{timestamp}}",
          "timeToLive": "0",
          "isShadowEntity": "False"
        }
      },
      "references": {}
    }
  }
}
```


### Remove Incoming Edges using Delta Clues


```
{
  "clue": {
    "attribute-organization": "{{org_id}}",
    "attribute-origin": "/Person#Newman:{{DeltaClues_EntityA_Id}}",
    "clueDetails": {
      "deltaData": {
        "attribute-persistHash": "hwcrydlp+4jrs1dqu2io9w==",
        "attribute-appVersion": "2.17.0.0",
        "processingFlags": {},
        "deltaDataActions": {
          "action": {
            "attribute-type": "/DataAction/Edit",
            "modifications": {
              "remove": {
                "attribute-target": "IncomingEdges",
                "attribute-referenceKey": "/HRCHY_test, Entity {{DeltaClues_EntityB_Id}}§C:/Person#Newman:{{DeltaClues_EntityB_Id}}"
              }
            }
          }
        }
      }
    }
  }
}
```

### Remove Properties using Delta Clues


```
{
  "clue": {
    "attribute-organization": "{{org_id}}",
    "attribute-origin": "/Person#Newman:{{DeltaClues_EntityA_Id}}",
    "clueDetails": {
      "deltaData": {
        "attribute-persistHash": "hwcrydlp+4jrs1dqu2io9w==",
        "attribute-appVersion": "2.17.0.0",
        "processingFlags": {},
        "deltaDataActions": {
          "action": {
            "attribute-type": "/DataAction/Edit",
            "modifications": {
              "remove": {
                "attribute-target": "Property",
                "attribute-referenceKey": "user.email"
              }
            }
          }
        }
      }
    }
  }
}
```

### Remove Entity Code using Delta Clues


```
{
  "clue": {
    "attribute-organization": "{{org_id}}",
    "attribute-origin": "/Person#Newman:{{DeltaClues_EntityA_Id}}",
    "clueDetails": {
      "deltaData": {
        "attribute-persistHash": "hwcrydlp+4jrs1dqu2io9w==",
        "attribute-appVersion": "2.17.0.0",
        "processingFlags": {},
        "deltaDataActions": {
          "action": {
            "attribute-type": "/DataAction/Edit",
            "modifications": {
              "remove": {
                "attribute-target": "EntityCode",
                "attribute-referenceKey": "/Person#Newman:12345"
              }
            }
          }
        }
      }
    }
  }
}
```

### Remove Tag using Delta Clues


```
{
  "clue": {
    "attribute-organization": "{{org_id}}",
    "attribute-origin": "/Person#Newman:{{DeltaClues_EntityA_Id}}",
    "clueDetails": {
      "deltaData": {
        "attribute-persistHash": "hwcrydlp+4jrs1dqu2io9w==",
        "attribute-appVersion": "2.17.0.0",
        "processingFlags": {},
        "deltaDataActions": {
          "action": {
            "attribute-type": "/DataAction/Edit",
            "modifications": {
              "remove": {
                "attribute-target": "Tag",
                "attribute-referenceKey": "Hello"
              }
            }
          }
        }
      }
    }
  }
}
```

### Remove Alias using Delta Clues


```
{
  "clue": {
    "attribute-organization": "{{org_id}}",
    "attribute-origin": "/Person#Newman:{{DeltaClues_EntityA_Id}}",
    "clueDetails": {
      "deltaData": {
        "attribute-persistHash": "hwcrydlp+4jrs1dqu2io9w==",
        "attribute-appVersion": "2.17.0.0",
        "processingFlags": {},
        "deltaDataActions": {
          "action": {
            "attribute-type": "/DataAction/Edit",
            "modifications": {
              "remove": {
                "attribute-target": "Alias",
                "attribute-referenceKey": "Hello"
              }
            }
          }
        }
      }
    }
  }
}
```

### Remove Description using Delta Clues


```
{
  "clue": {
    "attribute-organization": "{{org_id}}",
    "attribute-origin": "/Person#Newman:{{DeltaClues_EntityA_Id}}",
    "clueDetails": {
      "deltaData": {
        "attribute-persistHash": "hwcrydlp+4jrs1dqu2io9w==",
        "attribute-appVersion": "2.17.0.0",
        "processingFlags": {},
        "deltaDataActions": {
          "action": {
            "attribute-type": "/DataAction/Edit",
            "modifications": {
              "remove": {
                "attribute-target": "Description"
              }
            }
          }
        }
      }
    }
  }
}
```

### Remove Name using Delta Clues


```
{
  "clue": {
    "attribute-organization": "{{org_id}}",
    "attribute-origin": "/Person#Newman:{{DeltaClues_EntityA_Id}}",
    "clueDetails": {
      "deltaData": {
        "attribute-persistHash": "hwcrydlp+4jrs1dqu2io9w==",
        "attribute-appVersion": "2.17.0.0",
        "processingFlags": {},
        "deltaDataActions": {
          "action": {
            "attribute-type": "/DataAction/Edit",
            "modifications": {
              "remove": {
                "attribute-target": "Name"
              }
            }
          }
        }
      }
    }
  }
}
```

### Remove Display Name using Delta Clues


```
{
  "clue": {
    "attribute-organization": "{{org_id}}",
    "attribute-origin": "/Person#Newman:{{DeltaClues_EntityA_Id}}",
    "clueDetails": {
      "deltaData": {
        "attribute-persistHash": "hwcrydlp+4jrs1dqu2io9w==",
        "attribute-appVersion": "2.17.0.0",
        "processingFlags": {},
        "deltaDataActions": {
          "action": {
            "attribute-type": "/DataAction/Edit",
            "modifications": {
              "remove": {
                "attribute-target": "DisplayName"
              }
            }
          }
        }
      }
    }
  }
}
```

### Remove Author using Delta Clues


```
{
  "clue": {
    "attribute-organization": "{{org_id}}",
    "attribute-origin": "/Person#Newman:{{DeltaClues_EntityA_Id}}",
    "clueDetails": {
      "deltaData": {
        "attribute-persistHash": "hwcrydlp+4jrs1dqu2io9w==",
        "attribute-appVersion": "2.17.0.0",
        "processingFlags": {},
        "deltaDataActions": {
          "action": {
            "attribute-type": "/DataAction/Edit",
            "modifications": {
              "remove": {
                "attribute-target": "DisplayName",
                "attribute-referenceKey": "/Person#Newman:hello@cluedin.com"
              }
            }
          }
        }
      }
    }
  }
}
```

The `deltaDataActions` section contains an action that removes an edge. It consists of the following properties.

| Property | Description |
|--|--|
| `attribute-type` | Type of action that will be executed on a golden record when posting the clue. Use the value as in the sample clue (`/DataAction/Edit`). |
| `attribute-target` | Type of edge that will be removed: `OutgoingEdges` or `IncomingEdges`. Specify the type of edge that you want to remove. |
| `attribute-referenceKey` | A specific edge that will be removed. You need to provide the name of the edge and the ID of the target record (to).   |