---
layout: default
title: Workflow Event Handlers
parent: Development
nav_order: 570
permalink: /developer/workflow-event-handlers
tags: ["development", "workflows"]
---

CluedIn processes your data with a Workflow System that runs in a series of stages. You can use Workflow Event Handlers to hook into data at different stages and apply your own actions.

Think of this as a way of subcribing to certain events within the processing of data and getting a trigger to apply your own logic when this event is triggered.

```csharp
using System;
using System.Collections.Generic;
using System.Configuration;
using System.Linq;

using CluedIn.Core;
using CluedIn.Core.Configuration;
using CluedIn.Core.Data;
using CluedIn.Core.Data.Parts;
using CluedIn.Core.Events.Types;
using CluedIn.Core.Mesh;
using CluedIn.Core.Messages.Processing;
using CluedIn.Core.Processing;
using CluedIn.Core.Processing.Statistics;
using CluedIn.Core.Serialization;
using CluedIn.DataStore.Security;
using Microsoft.Extensions.Logging;

namespace CluedIn.Processing.Events
{
    /// <summary>The workflow event handlers</summary>
    /// <seealso cref="System.IDisposable" />
    public class MergeWorkflowEventHandlers : IDisposable
    {
        /**********************************************************************************************************
         * PROPERTIES
         **********************************************************************************************************/

        /// <summary>The context</summary>
        private readonly ApplicationContext context;

        /// <summary>The subscription</summary>
        private IDisposable subscription;

        /**********************************************************************************************************
         * CONSTRUCTORS
         **********************************************************************************************************/

        /// <summary>
        /// Initializes a new instance of the <see cref="WorkflowEventHandlers"/> class.
        /// </summary>
        /// <param name="context">The context.</param>
        public MergeWorkflowEventHandlers(ApplicationContext context)
        {
            this.context = context;

            this.subscription = this.context.System.Events.Local.Subscribe<WorkflowFinishedEvent>(this.ProcessEvent);
        }

        /**********************************************************************************************************
         * METHODS
         **********************************************************************************************************/

        /// <summary>
        /// Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources.
        /// </summary>
        public void Dispose()
        {
            if (this.subscription != null)
                this.subscription.Dispose();
        }

        /// <summary>Processes the event.</summary>
        /// <param name="eventData">The event data.</param>
        private void ProcessEvent(WorkflowFinishedEvent eventData)
        {
            if (eventData.WorkflowCommandType == null)
                return;

            if ((typeof(MergeEntitiesCommand).IsAssignableFrom(eventData.WorkflowCommandType) ||
                 eventData.WorkflowCommandType == typeof(MergeEntitiesCommand))
                && eventData.SubjectId.HasValue
                && eventData.WorkflowContextData != null
                && !eventData.NoChangesMade
                && eventData.WorkflowContextData.ContainsKey("mergeTargetEntityId")
                && eventData.WorkflowContextData.ContainsKey("mergeEntitiesIds")
                && eventData.WorkflowContextData.ContainsKey("mergeChanges"))
           {
                
                if (eventData.WorkflowContextData.ContainsKey("mergeChangesWithUserInput")) //TODO: @LJU: Dirty solution to get user input into merged records.
                {
                    Guid.TryParse(eventData.WorkflowContextData.GetValue("organizationId", null).ToString(), out var organizationId);
                    Guid.TryParse(eventData.WorkflowContextData.GetValue("mergeTargetEntityId", null).ToString(), out var targetEntityId);
                    
                    if (targetEntityId == null)
                        throw new ArgumentNullException("targetEntityId", "TargetEntityId not existent");
                    
                    if (organizationId == null)
                        throw new ArgumentNullException("organizationId", "OrganizationId not existent");
                    
                    var mergePropertiesJson = eventData.WorkflowContextData.GetValue("mergeChangesWithUserInput");
                    var mergeProperties = JsonUtility.Deserialize<List<MergeWithUserInput>>(mergePropertiesJson.ToString());
                    
                    if (mergeProperties == null)
                        throw new ArgumentNullException("mergeProperties", "Merge Properties collection could not be fetched");

                    if (!mergeProperties.Any())
                    {
                        throw new ArgumentNullException("No properties were given to merge");
                    }
                    
                    if (mergeProperties.Any())
                    {
                        var executionContext = this.context.CreateExecutionContext(organizationId);
                        var entity =
                            executionContext.Organization.DataStores.PrimaryDataStore.GetById(executionContext,
                                targetEntityId);

                        if (entity == null)
                            throw new ArgumentNullException($"Entity is not found at merge workflow step. {targetEntityId}");

                        var clue = new Clue(entity.ProcessedData.OriginEntityCode, executionContext.Organization.Id);
                        clue.Data.EntityData.Name = entity.Name;
                        clue.Data.EntityData.CreatedDate = entity.CreatedDate;
                        clue.Data.EntityData.ModifiedDate = DateTimeOffset.UtcNow;
                        clue.AllowedEntityOperations = AllowedEntityOperations.MergeIntoExisting;
                        clue.Data.Attributes["inputSource"] = "user";
                        
                        foreach (var mergeProperty in mergeProperties)
                        {
                            clue.Data.EntityData.Properties.Add(mergeProperty.PropertyName, mergeProperty.PropertyValue);
                        }
                        
                        var compressed = CompressedClue.Compress(clue, executionContext.ApplicationContext);
                        var command = new ProcessPrioritizedClueCommand(null, compressed);
                        
                        executionContext.Log.LogDebug($"Appended user input to merged record: {clue.OriginEntityCode}");
                        
                        this.context.System.ServiceBus.Publish(command);
                    }
                }  
            }
        }    
    }
}
```