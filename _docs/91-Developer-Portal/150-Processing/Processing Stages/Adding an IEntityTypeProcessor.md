---
category: Developer
title: Adding an IEntityTypeProcessor
---

This is your ability to interact with the data just before it is about to finish the processing pipeline and before it will write the data to the databases.


```csharp
using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;

using CluedIn.Core;
using CluedIn.Core.Data;
using CluedIn.Core.Data.Parts;
using CluedIn.Core.Data.Vocabularies;
using CluedIn.Processing.Models.Utilities;

namespace CluedIn.Processing.Processors.Specific
{
    /// <summary>
    /// The task processor.
    /// </summary>
    public class DogProcessor : PropertyUtility, IEntityTypeProcessor
    {
        /// <summary>
        /// Checks if the specified entity type can be matched be this instance.
        /// </summary>
        /// <param name="type">The type.</param>
        /// <returns>
        ///   <c>true</c> if the entity matcher can match the specified entity type; otherwise <c>false</c>.
        /// </returns>
        public bool Accepts(EntityType type)
        {
            return type.Is("/Dog");
        }

        /// <summary>Processes the specified data.</summary>
        /// <param name="context">The context.</param>
        /// <param name="processedMetadata">The processed metadata.</param>
        /// <param name="data">The data part.</param>
        public void Process(ExecutionContext context, IProcessedEntityMetadataPart processedMetadata, IDataPart data)
        {
            if (context == null)
                throw new ArgumentNullException(nameof(context));

            if (processedMetadata == null)
                throw new ArgumentNullException(nameof(processedMetadata));

            processedMetadata.Tags.Add("Woof!");
        }
    }
}
```