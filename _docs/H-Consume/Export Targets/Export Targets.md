Export Targets

Export Targets are used to authenticate with an integration point with the intention that CluedIn will make data available to this consumer via a push mechanish that CluedIn calls Outgoing Streams. Good examples include: 

 - Business Intelligence Tools
 - Data Warehouse Dimension Tables
 - Machine Learning Platforms
 - Custom Applications
 - Databases

An Export Target is composed of the authentication piece involved in CluedIn and the target being able to converse, a Transform, a Target and a Matcher. 

The Transform is responsible for taking the data in CluedIn and projecting it out into a format that matches what the consumer is expecting. 

A Target is responsible for detailing the location of the data that CluedIn will send over to the consumer. 

A Matcher is responsible for determining what data will be sent over from CluedIn. 

Similar to Integrations, an Export Target may talk to a Sql Database, a Rest API, a Stream, a SOAP endpoint or more. 

Developers can add brand new Export Targets by implementing the OutgoingWebhookProcessor class. This class will be responsible for authentication and making sure that the correct Transforms, Triggers and Targets are established. 

Here is an example of how you could introduce a new Export Target:

using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Threading;

using CluedIn.Core;
using CluedIn.Core.Data.Relational;
using CluedIn.Core.Processing;
using CluedIn.Core.Webhooks;
using CluedIn.Core.Workflows;
using CluedIn.Processing;
using CluedIn.WebHooks.Commands;

namespace Custom.WebHooks.Actors
{
    public class OutgoingCustomWebHookActor : ProcessingBase<OutgoingCustomWebHookCommand>
    {
        public OutgoingCustomWebHookActor([NotNull] ApplicationContext appContext) : base(appContext)
        {
        }

        public override int? SubscriptionConsumerPriority
        {
            get
            {
                return 0;
            }
        }

	    protected override ProcessingContext CreateProcessingContext(OutgoingCustomWebHookCommand processCommand)
        {
            var context = this.appContext.CreateExecutionContext(processCommand.OrganizationId)
                                                .ToProcessingContext()
                                                .WithExecutionOption(ExecutionOptions.PreferMasterDataStore)
                                                .WithExecutionOption(ExecutionOptions.IgnoreDuplicates)
                                                .WithExecutionOption(ExecutionOptions.IgnoreEdges);

            return context;
        }

        protected override IWorkflowStepResult ProcessWorkflowStep(ProcessingContext processingContext, OutgoingCustomWebHookCommand processCommand)
        {
            if (processCommand == null)
                throw new ArgumentNullException(nameof(processCommand));

            if (processingContext.IsSystemContext)
                throw new ArgumentException("Context cannot be system context", nameof(processingContext));s

            if (!processingContext.Organization.WebHooks.HasOutgoingCustomWebhooks)
                return WorkflowStepResult.Ignored;

            using (var context = processingContext.Clone().WithExecutionOption(ExecutionOptions.IgnoreEdges))
            {
                var dataStore = context.Organization.DataStores.PrimaryDataStore;
                var entity      = dataStore.GetById(context, processCommand.SubjectId);

                if (entity == null)
                    return WorkflowStepResult.Ignored;

                ProviderDefinition providerDefinition = null;

                if (processCommand.ProviderDefinitionId.HasValue)
                    providerDefinition = context.Organization.Providers.GetProviderDefinition(context, processCommand.ProviderDefinitionId.Value);

                var definitions = context.Organization.WebHooks.GetWebHookDefinitions(context, w => w.ProviderId == CustomWebHooksConstants.ProviderId && w.WebhookType == WebhookType.Outgoing && w.AccountId == processCommand.OrganizationId);
                var saveResults = new List<SaveResult>();

                foreach (var webhookDefinition in definitions)
                {
                    var outgoing = webhookDefinition as IOutgoingWebhookDefinition;

                    if (outgoing == null)
                        continue;

                    if (outgoing.Trigger.Match(entity, processCommand.EntityChanges, providerDefinition))
                    {
                        var saveResult = SaveResult.Unknown;

                        try
                        {
                            try
                            {
                                ActionExtensions.ExecuteWithRetry(() =>
                                    {
                                        //Send data to consumer
                                    },
                                    isTransient: ExceptionHelper.ShouldRequeue);
                            }
                            catch (Exception ex)
                            {
                                saveResult = saveResult.WithData(ex).WithState(SaveResultState.Failed);
                            }

                            if (saveResult.State != SaveResultState.Success)
                                saveResult.WithState(SaveResultState.Failed);
                        }
                        catch (Exception ex)
                        {
                            saveResult = saveResult.WithState(SaveResultState.Failed).WithData(ex);
                        }

                        saveResults.Add(saveResult);
                    }
                }

                return new WorkflowStepResult(new AggregateSaveResult(saveResults), processCommand.SubjectId);
            }
        }
    }
}