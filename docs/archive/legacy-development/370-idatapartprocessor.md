---
layout: cluedin
title: Adding a new IDataPartProcessor
parent: Legacy development documentation
grand_parent: Archive
nav_order: 370
permalink: /archive/legacy-development/idatapartprocessor
content_type: reference
redirect_from: ["/developer/idatapartprocessor"]
source_path: docs/090-development/450-adding-idatapartprocessorexecutor.md
tags: ["development","processors"]
published: false
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