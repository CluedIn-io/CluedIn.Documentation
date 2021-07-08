---
category: Developer
title: Adding an IDataPartProcessor
---

This is the first part in the processing stage where you get to inject custom logic into the middle of the CluedIn Processing Pipeline. It runs after some of the critical parts of the inbuilt data processing has run from CluedIn.

```csharp
using System;
using System.Linq;

using CluedIn.Core;
using CluedIn.Core.Data;
using CluedIn.Core.Data.Parts;
using CluedIn.Core.Data.Vocabularies;
using CluedIn.Core.Processing;

namespace CluedIn.Processing.ContentProcessing
{
    public class AutoTagProcessor : IDataPartProcessor
    {
        public void Process(ProcessingContext context, IDataPart dataPart, IProcessedEntityMetadataPart processedMetadata)
        {
           processedMetadata.Tags.Add("I made it here");
        }
    }
}

```