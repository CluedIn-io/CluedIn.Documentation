---
layout: cluedin
title: Adding a new IProcessingFilter
parent: Development
nav_order: 420
permalink: /developer/iprocessingfilter
tags: ["development","processors"]
published: false
---

The main use of the IProcessingFiltering interface is to introduce your ability to define logic to Ignore a Clue completely. Imagine that you only want to accept Clues where they are of a particular Entity Type. This is your ability to inject this logic very early in the processing of data.


```csharp
using System;
using System.Collections.Generic;
using System.Linq;

using CluedIn.Core;
using CluedIn.Core.Configuration;
using CluedIn.Core.Data;
using CluedIn.Core.Data.Parts;
using CluedIn.Core.Serialization;

namespace CluedIn.Processing
{
    /// <summary>The clue filtering.</summary>
    public class ClueProcessingFiltering : IProcessingFiltering
    {
        /**********************************************************************************************************
         * FIELDS
         **********************************************************************************************************/

        /// <summary>The context</summary>
        private readonly ApplicationContext context;


        /**********************************************************************************************************
         * CONSTRUCTORS
         **********************************************************************************************************/

        /// <summary>
        /// Initializes a new instance of the <see cref="ProcessingFiltering"/> class.
        /// </summary>
        /// <param name="context">The context.</param>
        public ProcessingFiltering(ApplicationContext context)
        {
            this.context = context;
         
        }

        /**********************************************************************************************************
         * METHODS
         **********************************************************************************************************/

        public bool IsPreFiltered(CompressedClue clue)
        {
            if (clue.EntityType != "/Organization")
                return true;

            return false;
        }

        public bool IsPreFiltered(Clue clue)
        {
            // Additional checks not possible by IsPreFiltered(CompressedClue)
            return false;
        }

        public bool IsPreFiltered(IEntityMetadata entity)
        {
             return false;
        }

        public bool IsMergePrefiltered(Clue clue)
        {
            return false;
        }

        public bool IsMergePrefiltered(IEntityMetadata entity)
        {
            return false;
        }

        public bool IsEdgeProcessingPrefiltered(IEntityMetadata entity)
        {
             return false;
        }

        public bool IsFuzzyMatchEntityPrefiltered(Clue clue)
        {
            return false;
        }

        public bool IsCreateNewEntityPreFiltered(Clue clue)
        {
            return false;
        }     
    }
}
```