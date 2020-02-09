Adding a new Processing Pipeline

There are many reasons to add a new processing pipeline. The concept behind a processing pipeline is that it allows you to process input data and produce an output. 

The CluedIn processing pipeline can be conceptualised as a never ending stream of incoming data in which this data will flow through many processing pipelines. Some of the pipelines will take input, will fix or clean certain types of data and then output it for it to be input to another processing pipeline step. 

CluedIn already has many processing pipeline steps that it ships with, including (but not limited to):

 - Detecting Duplicate Records.
 - Automatically normalising dates, phone numbers, abbreviations.
 - Running entity detection on text.

 Imagine if you are ingesting data from a new system that you have built in-house. This system stores data on Dogs and their Vetenary visits. These are, by default, not well known Domain objects to CluedIn. Although it is completely fine to ingest these types of Domain objects, you can probably imagine that there will not be much out of the log logic that knows how to clean, enrich, measure and normalise data on Dogs. This is the reason why you would introduce new processing pipeline steps. In very high level pseduo code, you would visualise that you will have a process that will look something like this:

 (if EntityType == Dog)
 {
 	//Do some magic
 }

Here as an example of a Processor that you could implement that will run some custom entity merging logic that you may want:

```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using CluedIn.Core;
using CluedIn.Core.Agent;
using CluedIn.Core.Data;
using CluedIn.Core.Diagnostics;
using CluedIn.Core.Messages.Processing;
using CluedIn.Core.Processing;
using CluedIn.Core.Workflows;

namespace Your.Custom.Namespace
{
    public class CustomMergeProcessing : ProcessingBase<MergeEntityCommand>
    {      
        public CustomMergeProcessing([NotNull] ApplicationContext appContext)
            : base(appContext)
        {
        }
       
        protected override ProcessingContext CreateProcessingContext(MergeEntityCommand processCommand)
        {
            var context = this.appContext.CreateProcessingContext(processCommand).WithExecutionOption(ExecutionOptions.PreferMasterDataStore).WithExecutionOption(ExecutionOptions.Overwrite).WithExecutionOption(ExecutionOptions.Force);
            return context;
        }

        protected override IWorkflowStepResult ProcessWorkflowStep(ProcessingContext context, MergeEntityCommand processCommand)
        {
            if (processCommand == null)
                throw new ArgumentNullException(nameof(processCommand));

  
            var result      = SaveResult.Unknown;

            using (processCommand.JobId != null ? context.CreateLoggingScope(new { processCommand.JobId }) : (IDisposable)new DummyDisposable())
            {
                var entity = context.Organization.DataStores.BlobDataStore.GetById(context, processCommand.SourceId);

                if (entity == null)
                    return WorkflowStepResult.Ignored;        

                var entity2 = context.Organization.DataStores.BlobDataStore.GetById(context, processCommand.TargetId);

                if (entity2 == null)
                    return WorkflowStepResult.Ignored;            

                if (entity1.Name == entity2.Name)
                {
                	//Save into the databasess
                }

                return new WorkflowStepResult(operations, SaveResult.Complete);
            }
        }
        
    }
}
```



 There is, however, the restriction that you must write this code in .net. There are many developers and users of CluedIn that will not know this and hence what we often suggest and recommend that, in fact, at the end of the day - CluedIn is really just talking in JSON and REST. Hence, if you need to create a custom processing pipeline, you can also build it completely outside of CluedIn completely and take the data from CluedIn using either our GraphQL api or using our streams mechanism to push data to another platform to process data there. 

 Once you have processed your data, all we ask is that you send that back to CluedIn with our REST endpoint for accepting clues in JSON or XML format.