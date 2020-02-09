---
category: User Interface
title: Webhooks
---

CluedIn can listen to web hook endpoints and process the data from those objects. This allows CluedIn to be sent provider specific object types and CluedIn will use the appropriate Clue Producers to turn it into a Clue before processing. 

Webhooks are implemented in the Crawler Template that CluedIn releases. You will find that you have many places for which you will need to implement to get the full support of the Webhooks. 

The first "handshake" you will need to make is to register your Incoming webhook with the source system. 

You will need to implement 3 methods as to be able to handle the Create, Get and Delete. 

Here is some example code on how you could set this up with Hubspot. 

```csharp
		public override async Task<IEnumerable<WebHookSignature>> CreateWebHook(ExecutionContext context, [NotNull] CrawlJobData jobData, [NotNull] IWebhookDefinition webhookDefinition, [NotNull] IDictionary<string, object> config)
        {
            if (jobData == null)
                throw new ArgumentNullException(nameof(jobData));
            if (webhookDefinition == null)
                throw new ArgumentNullException(nameof(webhookDefinition));
            if (config == null)
                throw new ArgumentNullException(nameof(config));

            var hubSpotCrawlJobData = (HubSpotCrawlJobData)jobData;
            var webhookSignatures = new List<WebHookSignature>();
            try
            {
                var client = _hubspotClientFactory.CreateNew(hubSpotCrawlJobData);

                var data = await client.GetWebHooks();

                if (data == null)
                    return webhookSignatures;

                var hookTypes = new[] { "contact.creation", "contact.deletion", "contact.propertyChange", "company.creation", "company.deletion", "company.propertyChange", "deal.creation", "deal.deletion", "deal.propertyChange" };

                foreach (var subscription in hookTypes)
                {
                    if (config.ContainsKey("webhooks"))
                    {
                        var enabledHooks = (List<Webhook>)config["webhooks"];
                        var enabled = enabledHooks.Where(s => s.Status == "ACTIVE").Select(s => s.Name);
                        if (!enabled.Contains(subscription))
                        {
                            continue;
                        }
                    }

                    try
                    {
                        await client.CreateWebHook(subscription);
                        webhookSignatures.Add(new WebHookSignature { Signature = webhookDefinition.ProviderDefinitionId.ToString(), ExternalVersion = "v1", ExternalId = null, EventTypes = "contact.creation,contact.deletion,contact.propertyChange,company.creation,company.deletion,company.propertyChange,deal.creation,deal.deletion,deal.propertyChange" });
                    }
                    catch (Exception e)
                    {
                        _log.Warn(() => $"Could not create HubSpot Webhook for subscription: {subscription}", e);
                    }
                }

                webhookDefinition.Uri = new Uri(this.appContext.System.Configuration.WebhookReturnUrl.Trim('/') + ConfigurationManager.AppSettings["Providers.HubSpot.WebhookEndpoint"]);

                webhookDefinition.Verified = true;
            }
            catch (Exception exception)
            {
                _log.Warn(() => "Could not create HubSpot Webhook", exception);
            }

            var organizationProviderDataStore = context.Organization.DataStores.GetDataStore<ProviderDefinition>();
            if (organizationProviderDataStore != null)
            {
                if (webhookDefinition.ProviderDefinitionId != null)
                {
                    var webhookEnabled = organizationProviderDataStore.GetById(context, webhookDefinition.ProviderDefinitionId.Value);
                    if (webhookEnabled != null)
                    {
                        webhookEnabled.WebHooks = true;
                        organizationProviderDataStore.Update(context, webhookEnabled);
                    }
                }
            }

            return webhookSignatures;
        }

        public override async Task<IEnumerable<WebhookDefinition>> GetWebHooks(ExecutionContext context)
        {
            var webhookDefinitionDataStore = context.Organization.DataStores.GetDataStore<WebhookDefinition>();
            return await webhookDefinitionDataStore.SelectAsync(context, s => s.Verified != null && s.Verified.Value);
        }

        public override async Task DeleteWebHook(ExecutionContext context, [NotNull] CrawlJobData jobData, [NotNull] IWebhookDefinition webhookDefinition)
        {
            if (jobData == null)
                throw new ArgumentNullException(nameof(jobData));
            if (webhookDefinition == null)
                throw new ArgumentNullException(nameof(webhookDefinition));

            await Task.Run(() =>
            {
                var webhookDefinitionProviderDataStore = context.Organization.DataStores.GetDataStore<WebhookDefinition>();
                if (webhookDefinitionProviderDataStore != null)
                {
                    var webhook = webhookDefinitionProviderDataStore.GetById(context, webhookDefinition.Id);
                    if (webhook != null)
                    {
                        webhookDefinitionProviderDataStore.Delete(context, webhook);
                    }
                }

                var organizationProviderDataStore = context.Organization.DataStores.GetDataStore<ProviderDefinition>();
                if (organizationProviderDataStore != null)
                {
                    if (webhookDefinition.ProviderDefinitionId != null)
                    {
                        var webhookEnabled = organizationProviderDataStore.GetById(context, webhookDefinition.ProviderDefinitionId.Value);
                        if (webhookEnabled != null)
                        {
                            webhookEnabled.WebHooks = false;
                            organizationProviderDataStore.Update(context, webhookEnabled);
                        }
                    }
                }
            });
        }

```

This will setup all the scaffolding you will need to be able to automatically create webhooks with your source systems when an integration is added to CluedIn. The next step is that you need to be able to process the data that these webhooks will post to CluedIn. 

If you have used the Crawler Templates that CluedIn provides then you will see a Folder in your Provider project called "Webhooks". This will have two files within it to start with in the template. The first is the Webhook PreValidator. This is responsible for validating "pre-flight" checks that come as a part of the standard Webhook flow. 

```csharp
using CluedIn.Core.Webhooks;
using CluedIn.Crawling.Custom.Core;

namespace Custom.Provider.YourTool.WebHooks
{
    public class YourTool_WebhookPreValidator : BaseWebhookPrevalidator
    {
        public YourTool_WebhookPreValidator()
            : base(YourToolConstants.ProviderId, YourToolConstants.ProviderName)
        {
        }
    }
}

You will then also need to implement the WebhookProcessor such as:

using System;
using System.Collections.Generic;
using System.Configuration;
using System.Linq;
using System.Threading.Tasks;
using CluedIn.Core;
using CluedIn.Core.Agent.Jobs;
using CluedIn.Core.Configuration;
using CluedIn.Core.Data;
using CluedIn.Core.DataStore;
using CluedIn.Core.Messages.Processing;
using CluedIn.Core.Providers;
using CluedIn.Core.Webhooks;
using CluedIn.Crawling;
using CluedIn.Crawling.YourTool.Core;

namespace Custom.Provider.YourTool.WebHooks
{
    public class YourToolWebhookProcessor : BaseWebhookProcessor
    {
        public YourToolWebhookProcessor(ApplicationContext appContext)
            : base(appContext)
        {
        }

        public override bool Accept(IWebhookDefinition webhookDefinition)
        {
            return webhookDefinition.ProviderId == HubSpotConstants.ProviderId || base.Accept(webhookDefinition);
        }

        public override IEnumerable<Clue> DoProcess(ExecutionContext context, WebhookDataCommand command)
        {
            try
            {
                if (ConfigurationManager.AppSettings.GetFlag("Feature.Webhooks.Log.Posts", false))
                    context.Log.Debug(() => command.HttpPostData);

                var configurationDataStore = context.ApplicationContext.Container.Resolve<IConfigurationRepository>();
                if (command.WebhookDefinition.ProviderDefinitionId != null)
                {
                    var providerDefinition = context.Organization.Providers.GetProviderDefinition(context, command.WebhookDefinition.ProviderDefinitionId.Value);
                    var jobDataCheck       = context.ApplicationContext.Container.ResolveAll<IProvider>().FirstOrDefault(providerInstance => providerDefinition != null && providerInstance.Id == providerDefinition.ProviderId);
                    var configStoreData    = configurationDataStore.GetConfigurationById(context, command.WebhookDefinition.ProviderDefinitionId.Value);  

                    // If you have stopped the provider then don't process the webhooks
                    if (providerDefinition?.WebHooks != null)
                        if (providerDefinition.WebHooks == false || providerDefinition.IsEnabled == false)
                            return new List<Clue>();

                    if (jobDataCheck != null)
                    {
                        var crawlJobData = new YourToolCrawlJobData(configStoreData);

                        var clues = new List<Clue>();

                        //Create your Clues out of the object coming from the command.HttpPostData

                    }
                }
            }
            catch (Exception exception)
            {
                context.Log.Error(new { command.HttpHeaders, command.HttpQueryString, command.HttpPostData, command.WebhookDefinitionId }, () => "Could not process web hook message", exception);
            }

            return new List<Clue>();
        }
    }
}
```