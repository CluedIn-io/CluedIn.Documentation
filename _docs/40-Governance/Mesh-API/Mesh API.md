---
category: Governance
title: Mesh API
---

The Mesh API allows a developer to implement the ability for CluedIn to write back values from CluedIn to source systems. This comes in the form of the following operation types: 

Update
Delete
Archive
Associate
Disassociate
Anonymise
De-anonymise
Remove from Processing

Due to the nature of this feature, there are no mesh API’s that are implemented in a blank installation of CluedIn. This is due to the nature that most mutation operations will change requirements per customer. This does not mean however that a lot of the framework around the operations is not turned on by default. The following actions will cause mesh commands to be generated:

Manually edit a property in the Property view within CluedIn
Any operation within CluedIn Clean that changes values
When a value is determined through the Data Quality scores to be a higher statistical confidence than what is in the source system. 
When a core vocabulary is empty from one source and available in another.
When a core vocabulary is enriched from Enrichers. 
When the data governance pieces around Subject Access Requests are initiated i.e. Anonymisation, Magnification, Deletion. 
When a record merges within CluedIn or is Split within CluedIn.

All Mesh Commands are queued by default i.e. they don't automatically run. It requires the product owner of that integration point to click the "Approve" operation on that mesh command to physically run the command. You can see these commands in your Mesh Center from the main menu. It also requires that the authorisation and authentication that has been provided for that source is given the right permissions to fulfil the operation. It may have been that for ingestion of data you are using an account that has read access, but for Mesh commands it will typically require write, delete and other types of permissions. 

Notes from the field: Especially when talking to databases directly, it is often hard to gauge what operations are needed to run to properly run an expected operation. For example, cascading support is often needed on databases if you are trying to run an operation that has referential integrity in another table and hence when you try to run an operation it may respond with exceptions. 

It is often the case that with proper base implementations, that Mesh API implementations can become cleaner and less work, with the only changes per endpoint being the Url to call and the package of data to send. 

By implementing the base classes for Mesh Processors you will receive a flow as follows:

Step 1: Given input from CluedIn, you can construct a textual preview of what command you will be running against the source system.
Step 2: If the user decides to run the command, it will make the appropriate call to the endpoint to make the mutation. 
Step 3: CluedIn will run the validation function so that you can check if your operation worked successfully e.g. if you ran a delete operation, you would expect that if you tried to lookup the value again that you would not get a record back. If your validation fails, then CluedIn will retry for a number of times and then mark the mesh command in a failed state. This means that there is a strong chance that the operation failed.

When mesh operations are run, it will update the records in the source systems and in most cases will update their modification stamp as well. This means the next time that CluedIn runs a scheduled crawl against that system, if the source sends us the updated modification stamp then CluedIn will process it; if it does not send us the updated modification date then CluedIn will assume it is the same and throw it away in processing. This is due to the hash that CluedIn generates on entities as to do quick comparisons of records. 

Mesh API commands can be generated through the CluedIn REST API, or it can be all managed through the CluedIn User Inteface. There are many operations that will generate a Mesh Command, but in summary - any mutation operation that runs in CluedIn will cause Mesh API commands by default. These include:

 Any of these operations will generate Mesh API commands and will place these under the affected Entities in the "Pending Changes" tab of the entity page and in the Global Mesh Center where all Mesh Commands are visible. All Mesh Commands that are generated through the CluedIn User Interface are by default "Queued" and are not run until the Product Owner of the record that is being mutated accepts the change. You might find that an Entity has been merged from many sources and hence every single individual Product Owner will need to be involved in the Approval Process. 

 Mesh Commands are Vocabulary enabled, meaning that they will utilise the hierarchy of Vocabularies that you have built so that you can change a particular value and CluedIn will "unravel" the Vocabulary of that value as to create Mesh Commands for all child and sub-child nodes of the records edited. 

Due to the nature of certain data, for the MESH API, you might find that while developing your crawlers, you will want to add an extra Entity Code to uniquely identify an individual row of data. Although Entity Codes should uniquely identify an object, this is an example where it is fine to add an Entity Code that is Mesh specific. An Entity Code example of this would be "/Person#CluedIn(Mesh):<Row Identifier>".

Let's use the following Mesh implementation as an example on how to implement others.

https://github.com/CluedIn-io/CluedIn.Crawling.HubSpot/tree/develop/src/HubSpot.Provider/Mesh/HubSpot

```csharp
﻿using System;
using System.Collections.Generic;
using System.Linq;
using CluedIn.Core;
using CluedIn.Core.Data;
using CluedIn.Core.Mesh;
using CluedIn.Core.Messages.Processing;
using CluedIn.Core.Messages.WebApp;
using CluedIn.Crawling.HubSpot.Core;
using RestSharp;

namespace CluedIn.Provider.HubSpot.Mesh.HubSpot
{
    public abstract class HubSpotUpdateBaseMeshProcessor : BaseMeshProcessor
    {
        public EntityType[] EntityType { get; }
        public string EditUrl { get; }

        protected HubSpotUpdateBaseMeshProcessor(ApplicationContext appContext, string editUrl, params EntityType[] entityType)
            : base(appContext)
        {
            EntityType = entityType;
            EditUrl = editUrl;
        }

        public override bool Accept(MeshDataCommand command, MeshQuery query, IEntity entity)
        {
            return command.ProviderId == this.GetProviderId() && query.Action == ActionType.UPDATE && EntityType.Contains(entity.EntityType);
        }

        public override void DoProcess(CluedIn.Core.ExecutionContext context, MeshDataCommand command, IDictionary<string, object> jobData, MeshQuery query)
        {
            return;
        }

        public override List<RawQuery> GetRawQueries(IDictionary<string, object> config, IEntity entity, Core.Mesh.Properties properties)
        {
            var hubSpotCrawlJobData = new HubSpotCrawlJobData(config);

            return new List<Core.Messages.WebApp.RawQuery>()
            {
                new Core.Messages.WebApp.RawQuery()
                {
                    Query = string.Format("curl -X PUT https://api.hubapi.com/" + EditUrl + "{1}?hapikey={0} "  + "--header \"Content-Type: application/json\"" + " --data '{2}'", hubSpotCrawlJobData.ApiToken, this.GetLookupId(entity), JsonUtility.Serialize(properties)),
                    Source = "cUrl"
                }
            };
        }

        public override Guid GetProviderId()
        {
            return Constants.Providers.HubSpotId;
        }

        public override string GetVocabularyProviderKey()
        {
            return "hubspot";
        }

        public override string GetLookupId(IEntity entity)
        {
            var code = entity.Codes.ToList().FirstOrDefault(d => d.Origin.Code == "HubSpot");
            long id;
            if (!long.TryParse(code.Value, out id))
            {
                //It does not match the id I need.
            }

            return code.Value;
        }

        public override List<QueryResponse> RunQueries(IDictionary<string, object> config, string id, Core.Mesh.Properties properties)
        {
            var hubSpotCrawlJobData = new HubSpotCrawlJobData(config);
            var client = new RestClient("https://api.hubapi.com");
            var request = new RestRequest(string.Format(EditUrl + "{0}", id), Method.PUT);
            request.AddQueryParameter("hapikey", hubSpotCrawlJobData.ApiToken); // adds to POST or URL querystring based on Method
            request.AddJsonBody(properties);

            var result = client.ExecuteTaskAsync(request).Result;

            return new List<QueryResponse>() { new QueryResponse() { Content = result.Content, StatusCode = result.StatusCode } };
        }

        public override List<QueryResponse> Validate(ExecutionContext context, MeshDataCommand command, IDictionary<string, object> config, string id, MeshQuery query)
        {
            var hubSpotCrawlJobData = new HubSpotCrawlJobData(config);

            var client = new RestClient("https://api.hubapi.com");
            var request = new RestRequest(string.Format(EditUrl + "{0}", id), Method.GET);
            request.AddQueryParameter("hapikey", hubSpotCrawlJobData.ApiToken); // adds to POST or URL querystring based on Method

            var result = client.ExecuteTaskAsync(request).Result;

            return new List<QueryResponse>() { new QueryResponse() { Content = result.Content, StatusCode = result.StatusCode } };
        }


    }
}
```

In the example above, we are actually building an abstraction layer to handle all UPDATE types of operations due to the fact that Hubspot (this may differ from source to source) has very similar patterns for updating records, even if they are a different type of record. The only thing that changes are the Url and the Body of the HTTP PUT. 

To implement the Mesh API, you will want to inherit from the BaseMeshProcessor class as this is your way to tell CluedIn that your new implementation should be included at boot time. Coming with this inheritence will be a set of methods that you can optionally override. Be aware that this class itself will require you to implement the abstract class in other implementations due to the fact that CluedIn's container will not boot abstract implementations of Mesh API's. 

For example here is an implementation of the abstract class above for handling the editting / updating of Contacts in Hubspot: https://github.com/CluedIn-io/CluedIn.Crawling.HubSpot/blob/develop/src/HubSpot.Provider/Mesh/HubSpot/HubSpotContactMeshProcessor.cs

```csharp
﻿using CluedIn.Core;

namespace CluedIn.Provider.HubSpot.Mesh.HubSpot
{
    public class HubSpotContactMeshProcessor : HubSpotUpdateBaseMeshProcessor
    {
        public HubSpotContactMeshProcessor(ApplicationContext appContext)
            : base(appContext, "contacts/v1/contact/vid/:vid/profile", CluedIn.Core.Data.EntityType.Infrastructure.Contact, CluedIn.Core.Data.EntityType.Person)
        {
        }

    }
}
```

Notice how the implementation is literally only a constructor and changes the Url and the supported Entity Types in CluedIn that will use this Url to modify the values in Hubspot. 

Once you have implmemented the Mesh API, you can deploy it exactly like you deploy any other code to CluedIn - you will need to copy the dll's into the running application and reboot those parts. 

###Making multiple source changes

The Mesh API framework is setup to be very flexible on what you run against the source system to implement the changes. Imagine a situation where given a change in CluedIn that triggers this Mesh API to be evaluated, you would like to remove all records from a system, not just the Golden Record. 

For this, you could essentially create a foreach loop that loops through all the Entity Codes with an Origin of your source (e.g. Hubspot) and then create a Mesh Command per instance of this. This is also why the Mesh Base Processor allows a List of queries to be returned.

###Common things to think about

Making changes in source systems is much more disruptive and invasive than simply reading data from a system. For this reason, we have compiled a list of things to think about when you are implementing mesh commands. 

 - The CluedIn Mesh API is simply a framework that listens to events within CluedIn and then allows you to subscribe to these events and handle them how you would like to. 
 - CluedIn is responsible for passing the Event Type, the Entity in question, the proposed change as well as the Old Value and the New Value and some metadata around how to authenticate with the source system in question. 
 - Mesh commands are handled at a ProviderDefinition level which means that one source system is not aware of how other systems are handling the change and can also be run independently of each other in no particular order. If order of change is needed then it is important to make these all within the same Mesh implementation. 

The Mesh API can be setup to completely bypass the approval process that is within the MESH Center within the UI. This can be done within CluedIn but we recommend this is only done if you have some other way of approving changes or you are very confident with the implementation of your Mesh API. 