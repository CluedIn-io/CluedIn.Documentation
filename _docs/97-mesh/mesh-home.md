**Mesh API**

**Create (or Queue) Mesh Command**

_POST_ request to our **Public** API _/api/v1/mesh_

with body:

```JSON
{
  "Action": "UPDATE",
  "Query": "c52b0be2-7aca-58b0-8bba-cb4b63fcc28a",
  "Transform": [{
    "key": "hubspot.organization.phoneNumber",
    "value": "123456789"
  },
  ], 
  "IsQueued" :  true,
  "RemoveFromCluedIn" :  false,
  "DisconnectAccountAndRemoveFromCluedIn" :  false
}
```

where "Action" can be one of these: "UPDATE", "REMOVE", "ARCHIVE", "ASSOCIATE", "DISASSOCIATE"

"Query" is the Entity Id,
"Transform" has the keys whose values we want updated

This will add (queue) a Mesh Command to the message broker. This message will be then picked up by the server and if there are any Mesh Processors that match the request, the result command(s) (e.g. could be SQL or cURL) will be created and then inserted into the datastore.

The command then will be available for either approval or rejection.

**Get Entity Mesh Command List**
To get the commands available related to an entity use /api/v1/gdprmessages?id=<EntityId>


**Approve Mesh Command**

To approve the command, send a copy of the **Create (or Queue) Mesh Command** request but with ProviderDefinitionId added to the body and "IsQueued" set to false:

```JSON
{
  "Action": "UPDATE",
  "Query": "c52b0be2-7aca-58b0-8bba-cb4b63fcc28a",
  "ProviderDefinitionId": "9841268f-bfd9-4d75-9924-b218d8975542",
  "Transform": [{
    "key": "hubspot.organization.phoneNumber",
    "value": "123456789"
  },
  ], 
  "IsQueued" :  false,
  "RemoveFromCluedIn" :  false,
  "DisconnectAccountAndRemoveFromCluedIn" :  false
}
```

This will execute the command in the corresponding Mesh Processor.

Then it will go and find the Mesh Command in the datastore and delete it. Then it will insert and new row with the same data as the deleted row but with "Queued" set to false and a new Id.


**Reject Mesh Command**

_POST_ request to our Web API _/api/mesh/reject?id=<MessageId>_

This will simply remove the command from the datastore.