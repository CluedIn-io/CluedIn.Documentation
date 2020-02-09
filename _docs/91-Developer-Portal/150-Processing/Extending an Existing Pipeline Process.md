Extending an Existing Pipeline Process

Knowing that there are many processing pipelines that ship with the CluedIn product, you might find that you will want to only override small parts of CluedIn, rather than introducing your own custom pipeline processing steps. 

You will notice in the ProcessingBase class that we offer many methods that you can override and hence introduce your own logic. 

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
	//Extend an existing implementation in CluedIn.
    public class MyCustomMergeProcessing : AggregateEntityProcessing
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
        	//Run something custom
        	//Then run the base implementation
        	this.base(context);
        }                    
    }
}
```

Compile the code and then drop the DLL into the ServerComponent directory of CluedIn. 