Outgoing Streams

It is often the case the introducing new platforms like CluedIn can be thought of as quite "disruptive" i.e. our teams need to learn a new system and query language to be able to interact with the data. 

Although we offer our GraphQL api to "pull" data from CluedIn, we often recommend and prefer that you "push" the data from CluedIn to a target consumer. We call these out "Outgoing Streams" in which a CluedIn user will specify the filter of data that a consumer needs and a target and target model and CluedIn will open up a "long-running" stream of data that matches that filter in CluedIn today and in the future until you turn the stream off. 

In version 2.7 of CluedIn, you can only setup streams using our API. In later versions we will allows users to do this through a user interface. 

To create an outgoing stream, you can call the CluedIn REST API at

You will need to include a Body of JSON to POST to the REST API which has your instructions on what to create. 

HTTPPOST
{{url}}/api/v2/organization/providers?providerId=F084EAE7-6DF4-4FF6-BAED-082419BCC328

{
    "helperConfiguration": 
        {
            "customWebHooks":
            {
                "entity":
                {
                    "incoming": [],
                    "outgoing": [
                            {
                                "uri": "https://api.powerbi.com/beta/f5ae2761-b3fc-449d-a9e7-49c14d011ac0/datasets/0d601582-7c22-4b8d-b487-82180e6413e2/rows?key=<Insert Your Key Here>",
                                "signature": "",
                                "webhookType": "Outgoing",
                                "version": "1",
                                "externalId": "asdf",
                                "externalVersion": "1",
                                "mimeType": "application/json",
                                "transform":
                                {
                                    "name": "EntityToSimpleJson"
                                },
                                "trigger":
                                {
                                    "matchers": [
                                        {
                                            "name": "PropertyValue",
                                            "propertyName": "user.jobTitle",
                                            "propertyValue": "CEO"
                                        }
                                        ]
                                }
                            }
                        ]
                }
            }
        }
}

Once this has run, CluedIn will then fetch historical data in CluedIn where the user.jobTitle Vocabulary is already "CEO" and then will maintain a watch on any new or modified records that match this filter. Everything this is triggered, CluedIn will post Entities in the format of the "EntityToSimpleJson" format to the Uri you see in the "uri" part of the message. 

Developers can add their own "Transforms" that allow you to take data and mould it into the shape that you want. For example, here is a custom Transform that you could implement:

using System.IO;

using CluedIn.Core;
using CluedIn.Core.Data;
using CluedIn.Core.Registration;
using CluedIn.Core.Webhooks;

using Newtonsoft.Json.Linq;

namespace Custom.WebHooks.Transforms
{
    [NamedComponent("SplitByEntityTypeToSimpleJson")]
    public class SplitByEntityTypeToSimpleJsonOutputTransform : IEntityOutputTransform
    {
        public string Name { get; } = "SplitByEntityTypeToSimpleJson";

        public void Transform(Entity entity, Stream outputStream)
        {
        	if (entity.entityType == EntityType.Organization)
        	{
	            var json = new JObject();

	            json.Add("id", entity.Id);
	            json.Add("name", entity.Name);

	            using (var textWriter = new StreamWriter(outputStream))
	                JsonUtility.Serialize(json, textWriter);
            }
            else 
            {
            	var json = new JObject();

	            json.Add("id", entity.Id);
	            json.Add("name", entity.Name);
	            json.Add("displayName", entity.DisplayName);
	            json.Add("createdDate", entity.CreatedDate);
	            json.Add("modifiedDate", entity.ModifiedDate);
	            json.Add("discoveryDate", entity.DiscoveryDate);
	            json.Add("entityType", entity.EntityType.ToString());
	            json.Add("uri", entity.Uri);
	            json.Add("description", entity.Description);

	            if (entity.PreviewImage != null)
	                json.Add("PreviewImageUri", entity.PreviewImage.Uri);

	            foreach (var kp in entity.Properties)
	            {
	                json.Add("property-" + kp.Key, kp.Value);
	            }

	            using (var textWriter = new StreamWriter(outputStream))
	                JsonUtility.Serialize(json, textWriter);
            }
        }
    }
}
