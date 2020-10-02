---
category: Consume
title: Rest API
---

The CluedIn Web User Interface is driven off the Rest API. This means that whatever you can do the User Interface can also be automated and programmatically called from systems. Everything from creating new accounts, to adding integrations, to running searches can all be run through the Rest API. 

This can be very handy if you are wanting to completely automate the deployment process of your CluedIn account. For example, if you had a task to add 300 SharePoint instances to CluedIn then you can use the Rest API with your scripting language of choice to automate this. 

## Post a Clue to CluedIn

Our Rest API allows you to post data to it in the form of a Clue. 

To do this, you can implement a HTTP POST to the API endpoint like below.

```
curl --location --request POST '{{publicApiUrl}}api/v1/clue?save=true' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{access_token}}' \
--data-raw '{
  "clue": {
    "attribute-organization": "9eaf94b3-46c6-431f-8df5-3682590048c9",
    "attribute-origin": "/Person#HubSpot:27493554",
    "attribute-appVersion": "1.8.0.0",
    "clueDetails": {
      "data": {
        "attribute-origin": "/Person#HubSpot:27493554",
        "attribute-appVersion": "1.8.0.0",
        "attribute-inputSource": "cluedin",
        "entityData": {
          "attribute-origin": "/Person#HubSpot:27493554",
          "attribute-appVersion": "1.8.0.0",
          "attribute-source": "rest",
          "entityType": "/Person",
	      "propuser.jobTitle": "CEO",
          "codes": ["/Person#HubSpot:27493554"],
          "properties": {
           "attribute-type": "/Metadata/KeyValue",
           "user.jobTitle": "CEO"
          }
        }
      }
    }
  }
}
'
```

## Posting Raw Data to CluedIn where annotations already exist in the platform. 

There are times when you would like to send or post data to CluedIn but those records are not Clues or in the Clue structure. For these cases, you can post your raw data to CluedIn in which if you already have an annotation in CluedIn to map that data, CluedIn can convert them into Clues for you. Here is a example of how you could post JSON to CluedIn and it turns it into Clues.

```
curl --location --request POST '{{url}}/api/admin/entity/ProcessClue' \
--header 'Authorization: Bearer {{access_token}}' \
--header 'Content-Type: application/json' \
--data-raw '        {
  "occurred_at": 1382568826000,
  "highlight": "accepted",
  "primary_resources": [
    {
      "story_type": "feature",
      "name": "Reactor leak reported in Detention Block AA-23",
      "url": "http:///story/show/563",
      "id": 563,
      "kind": "story"
    }
  ],
  "changes": [
    {
      "story_type": "feature",
      "name": "Reactor leak reported in Detention Block AA-23",
      "new_values": {
        "accepted_at": 1382568827000,
        "before_id": 6024,
        "after_id": 559,
        "current_state": "accepted",
        "updated_at": 1382568826000
      },
      "original_values": {
        "accepted_at": null,
        "before_id": 6643,
        "after_id": 565,
        "current_state": "delivered",
        "updated_at": 1382568825000
      },
      "id": 563,
      "change_type": "update",
      "kind": "story"
    }
  ],
  "message": "Darth Vader accepted this feature",
  "project_version": 1037,
  "performed_by": {
    "name": "Darth Vader",
    "initials": "DV",
    "id": 101,
    "kind": "person"
  },
  "guid": "99_1037",
  "project": {
    "name": "Death Star",
    "id": 99,
    "kind": "project"
  },
  "kind": "story_update_activity"
}'
```