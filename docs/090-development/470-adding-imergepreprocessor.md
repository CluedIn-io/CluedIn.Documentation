---
layout: cluedin
title: Adding a new IMergePreProcessor
parent: Development
nav_order: 470
permalink: developer/imergepreprocessor
tags: ["development","processors"]
published: false
---

The IMergePreProcessor is your ability to provide custom input before records will Merge. This is useful if you want to inject your own custom logic to either cancel a merge or to modify the record or add logging before a Merge happens. 


```csharp
using System;
using System.Collections.Generic;
using System.Linq;

using CluedIn.Core;
using CluedIn.Core.Data;
using CluedIn.Core.Data.Parts;
using CluedIn.Core.Processing;
using CluedIn.Processing.Models.Utilities;

namespace CluedIn.Processing.Processors.PreProcessing
{
    /// <summary>A merge pre processor.</summary>
    /// <seealso cref="IEntityMetadataPart"/>
    /// <seealso cref="IMergePreProcessor"/>
    public class TimeStampMergePreProcessor : PropertyUtility<IEntityMetadataPart>, IMergePreProcessor
    {
        /// <inheritdoc/>
        public bool Accepts(ExecutionContext context, IEnumerable<IEntityCode> codes)
        {
            return true;
        }

        public SaveResult Process(ExecutionContext context, IEntityMetadataPart metadataToMerge, IDataPart dataToMerge, Entity targetEntity)
        {
            if (dataToMerge == null)
                return SaveResult.Ignored;

            metadataToMerge.Properties["mergeTimeStamp"] = DateTimeOffset.UtcNow.ToString();

            return SaveResult.Success;
        }
    }
}
```