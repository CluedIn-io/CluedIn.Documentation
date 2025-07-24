---
layout: cluedin
title: Adding a new PreProcessor
parent: Development
nav_order: 440
permalink: developer/preprocessor
tags: ["development","processors"]
last_modified: 2021-11-29
published: false
---

If you look at the processing pipeline flow diagram below, you can see that you have the ability very early on to inject custom logic to change a Clue before the processing starts. There are many good use cases this e.g. removing bad Entity Codes before data is processed.

<a href="../assets/images/development/processing-pipeline.png" target="_blank">![Processing Pipeline Flow Diagram](../assets/images/development/processing-pipeline.png)</a>

The main use of the PreProcessor stage is that it is your first chance to manipulate the Clue in the context of the pipeline to be changed in any way that you want before CluedIn takes over and applies some automated processing. 

Below is an example of removing all Codes from all Clues coming through the processing pipeline if the Value of the EntityCodes contains the word "SomeBadValue" with a perfect case match.


```csharp
using System.Collections.Generic;
using System.Linq;

using CluedIn.Core;
using CluedIn.Core.Data;
using CluedIn.Core.Data.Parts;
using CluedIn.Processing.Models.Utilities;

namespace CluedIn.Processing.Processors.PreProcessing
{
    /// <summary>The hubspot pre processor.</summary>
    /// <seealso cref="PropertyUtility{TMetadata}.Core.Data.Parts.IEntityMetadataPart}" />
    /// <seealso cref="CluedIn.Processing.Processors.PreProcessing.IPreProcessor" />
    public class RemoveBadEntityCodesPreProcessor : PropertyUtility<IEntityMetadataPart>, IPreProcessor
    {
        /// <inheritdoc/>
        public bool Accepts(ExecutionContext context, IEnumerable<IEntityCode> codes)
        {
            return codes.Any(c => c.Origin.Value.Contains("SomeBadValue"));
        }

        /// <summary>Processes the specified data.</summary>
        /// <param name="context">The context.</param>
        /// <param name="metadata">The metadata.</param>
        /// <param name="data">The data part.</param>
        public void Process(ExecutionContext context, IEntityMetadataPart metadata, IDataPart data)
        {
           metadata.Codes.Where(c => c.Origin.Value.Contains("SomeBadValue")).Remove();
        }

       
    }
}
```