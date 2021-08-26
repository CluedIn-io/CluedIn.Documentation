---
category: Preparation
title: How to add a new Data Quality Metric
---

Here is an example of how to calculate Accuracy of data. You can use this as a guide to implement your own custom data metrics.

Note: you may also review other implementations [here](https://github.com/CluedIn-io/CluedIn.Custom.Metrics/tree/master/src/CluedIn.Custom.Metrics/Implementations)


```csharp
using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Text;

using CluedIn.Core;
using CluedIn.Core.Data;
using CluedIn.Core.Data.Parts;
using CluedIn.Core.Metrics;
using CluedIn.Processing.Processors;

namespace Custom.Metrics.Implementations
{
    public class AccuracyMetric : PercentageMetric
    {
        private readonly IMetricProviderResolver providerResolver;

        public AccuracyMetric(IMetricProviderResolver providerResolver)
        {
            this.providerResolver = providerResolver;
        }

        public override short ValueSize => sizeof(ushort);

        public override Guid Id { get; } = new Guid("{987D2A08-E9A0-4661-BC8A-468E7BB34873}");

        public override string[] Categories { get; } = { MetricCategories.DataQuality };

        protected override PercentageMetricValue CalculatePct(
            MetricsProcessingContext context,
            IMetricDimension dimension,
            IMetricValues<short> existingMetricValues,
            Entity entity)
        {
            if (context == null)
                throw new ArgumentNullException(nameof(context));

            if (dimension == null)
                throw new ArgumentNullException(nameof(dimension));

            if (existingMetricValues == null)
                throw new ArgumentNullException(nameof(existingMetricValues));

            /*
             *                                                                        Dimension Table:
             *
             *                                                                      | DimensionType         | DetailType | ProviderDefinitionId | ProviderId | Detail        | Persistence                       |
             *                                                                      |-----------------------|------------|----------------------|------------|---------------|-----------------------------------|
             * Global                                                               | Global                |            |                      |            |               |                                   |
             *  │  Global Property                                                  | Global                | Property   |                      |            | Property Name |                                   |
             *  │   │  Global Provider                                              | GlobalIntegrationType |            |                      | Id         |               |                                   |
             *  │   │   │  Global Provider Definition                               | GlobalIntegration     |            | Id                   | Id         |               |                                   |
             *  │   │   │   │                                                       |-----------------------|------------|----------------------|------------|---------------|-----------------------------------|
             *  └───│───│───│── Entity                                              | Entity                |            |                      |            |               | Blob, Graph, Search, EntityMetric |
             *      └───│───│────└─ Entity Property                                 | Entity                | Property   |                      |            | Property Name |                                   |
             *          └───│── Entity Provider                                     | EntityIntegrationType |            |                      | Id         |               | EntityMetric                      |
             *              │    └─ Entity Provider Property                        | EntityIntegrationType | Property   |                      | Id         | Property Name |                                   |
             *              └── Entity Provider Definition                          | EntityIntegration     |            | Id                   | Id         |               | EntityMetric                      |
             *                   └─ Entity Provider Definition Property             | EntityIntegration     | Property   | Id                   | Id         | Property Name |                                   |
             *
             */

            if (dimension.DimensionType.HasFlag(MetricDimensionType.Entity))
            {
                if (entity == null)
                    throw new ArgumentNullException();

                var isProperty            = dimension.DimensionDetailType == MetricDimensionDetailType.Property;
                var hasProviderDefinition = dimension.ProviderDefinitionId.HasValue;
                var hasProvider           = dimension.ProviderId.HasValue;

                // EntityIntegration
                if (hasProviderDefinition && hasProvider)
                {
                    if (isProperty)
                    {
                        var uniqueValue = this.GetUniqueValuesMap(entity, dimension.DimensionDetail, v => v.DataPart.OriginProviderDefinitionId == dimension.ProviderDefinitionId.Value);

                        var average = CalculateMetricValue(uniqueValue);

                        return new PercentageMetricValue(dimension, entity.Id, average).WithExplanation(this.GetExplanation(context, uniqueValue));
                    }
                    else
                    {
                        var average = (short)existingMetricValues.Average(this, v => v.Dimension.DimensionType == MetricDimensionType.EntityIntegration && v.Dimension.DimensionDetailType == MetricDimensionDetailType.Property);
                        return new PercentageMetricValue(dimension, entity.Id, average).WithExplanation(this.GetAggregatedValueExplanation(context, MetricDimensionType.EntityIntegration, MetricDimensionDetailType.Property));
                    }
                }

                // EntityIntegrationType
                if (hasProvider)
                {
                    if (isProperty)
                    {
                        var uniqueValue = this.GetUniqueValuesMap(entity, dimension.DimensionDetail, v => this.providerResolver.ResolveProvider(context, v.DataPart.OriginProviderDefinitionId)?.Id == dimension.ProviderId.Value);

                        var average = CalculateMetricValue(uniqueValue);

                        return new PercentageMetricValue(dimension, entity.Id, average).WithExplanation(this.GetExplanation(context, uniqueValue));
                    }
                    else
                    {
                        var average = (short)existingMetricValues.Average(this, v => v.Dimension.DimensionType == MetricDimensionType.EntityIntegrationType && v.Dimension.DimensionDetailType == MetricDimensionDetailType.Property);
                        return new PercentageMetricValue(dimension, entity.Id, average).WithExplanation(this.GetAggregatedValueExplanation(context, MetricDimensionType.EntityIntegrationType, MetricDimensionDetailType.Property));
                    }
                }

                // Entity
                if (isProperty)
                {
                    var uniqueValue = this.GetUniqueValuesMap(entity, dimension.DimensionDetail);

                    var average = CalculateMetricValue(uniqueValue);

                    return new PercentageMetricValue(dimension, entity.Id, average).WithExplanation(this.GetExplanation(context, uniqueValue));
                }
                else
                {
                    var average = (short)existingMetricValues.Average(this, v => v.Dimension.DimensionType == MetricDimensionType.Entity && v.Dimension.DimensionDetailType == MetricDimensionDetailType.Property);
                    return new PercentageMetricValue(dimension, entity.Id, average).WithExplanation(this.GetAggregatedValueExplanation(context, MetricDimensionType.Entity, MetricDimensionDetailType.Property));
                }
            }
            else if (dimension.DimensionType.HasFlag(MetricDimensionType.Global))
            {
                var dateDimension = MetricDateDimension.Today;

                short   average;
                string  explanation;

                switch (dimension.DimensionType)
                {
                    case MetricDimensionType.GlobalIntegration:
                        average     = (short)existingMetricValues.Average(this, v => v.Dimension.DimensionType == MetricDimensionType.EntityIntegration);
                        explanation = this.GetAggregatedValueExplanation(context, MetricDimensionType.EntityIntegration, null);
                        break;

                    case MetricDimensionType.GlobalIntegrationType:
                        average     = (short)existingMetricValues.Average(this, v => v.Dimension.DimensionType == MetricDimensionType.EntityIntegrationType);
                        explanation = this.GetAggregatedValueExplanation(context, MetricDimensionType.EntityIntegrationType, null);
                        break;

                    case MetricDimensionType.Global:
                        average     = (short)existingMetricValues.Average(this, v => v.Dimension.DimensionType == MetricDimensionType.Entity);
                        explanation = this.GetAggregatedValueExplanation(context, MetricDimensionType.Entity, null);
                        break;

                    default:
                        throw new Exception();
                }

                return new PercentageMetricValue(dimension, dateDimension, average).WithExplanation(explanation);
            }

            throw new Exception();
        }

        private string GetExplanation(MetricsProcessingContext context, UniqueValuesMap uniqueValue)
        {
            if (!context.MetricsExecutionOptions.HasFlag(MetricsExecutionOption.Explanation))
                return null;

            var sb = new StringBuilder();

            var table = AsciiTableGenerator.GenerateTable(
                new[] { "Value", "Count", "CountAtHead"}, 
                uniqueValue.Values.OrderByDescending(v => v.Value != null).ThenByDescending(v => v.Count).ThenByDescending(v => v.CountAtHead),
                v => v.Value ?? "[Missing]",
                v => v.Count.ToString(),
                v => v.CountAtHead.ToString()
            );

            sb.AppendLine(table);

            sb.AppendLine();
            sb.AppendLine($"MaxUniqueValueCount:    {uniqueValue.MaxUniqueValueCount}");
            sb.AppendLine($"ValuesCount:            {uniqueValue.ValuesCount}");
            sb.AppendLine($"MissingValuesCount:     {uniqueValue.MissingValuesCount}");
            sb.AppendLine($"BranchCount:            {uniqueValue.BranchCount}");

            sb.AppendLine();
            sb.AppendLine("Calculation:");
            sb.AppendLine($"{uniqueValue.MaxUniqueValueCount} / ({uniqueValue.ValuesCount} + ({uniqueValue.MissingValuesCount} / {uniqueValue.BranchCount})) = {CalculateMetricValue(uniqueValue).ToString(CultureInfo.InvariantCulture)}");

            return sb.ToString();
        }

        private static double CalculateMetricValue(UniqueValuesMap v)
        {
            /*
              Formula:
                [Max Unique Value Count] / ([Sum of value counts] + ([Missing values] / [Branch Count]))
                
                max         Max Unique Value Count
                populated   Sum of value counts / Count populated records
                missing     Number of records with missing value
                branches    Branch Count
                
                Alternative
                
                Min(1, ([Max Unique Value Count] + ([Count at head] / [Branch Count])) / ([Sum of value counts] + ([Missing values] / [Branch Count]))
             */

            var average = (double)v.MaxUniqueValueCount / ((double)v.ValuesCount + ((double)v.MissingValuesCount / (double)v.BranchCount));

            // Alternative
            //var average = Math.Min(1d, ((double)v.MaxUniqueValueCount + ((double)v.HeadValuesCount / (double)v.BranchCount)) / ((double)v.ValuesCount + ((double)v.MissingValuesCount / (double)v.BranchCount)));

            return average;
        }

        public override bool ShouldPersist(IMetricDimension dimension)
        {
            throw new NotImplementedException();
        }

        public override IEnumerable<IMetricDimension> GetDimensions(MetricsProcessingContext context, IMetricsModel model)
        {
            var existingDimensions = model.MetricDimensions.Where(d => d.MetricId == this.Id);

            /*
             *                                                                        Dimension Table:
             *
             *                                                                      | DimensionType         | DetailType | ProviderDefinitionId | ProviderId | Detail        | Persistence                       |
             *                                                                      |-----------------------|------------|----------------------|------------|---------------|-----------------------------------|
             * Global                                                               | Global                |            |                      |            |               |                                   |
             *  │  Global Property                                                  | Global                | Property   |                      |            | Property Name |                                   |
             *  │   │  Global Provider                                              | GlobalIntegrationType |            |                      | Id         |               |                                   |
             *  │   │   │  Global Provider Definition                               | GlobalIntegration     |            | Id                   | Id         |               |                                   |
             *  │   │   │   │                                                       |-----------------------|------------|----------------------|------------|---------------|-----------------------------------|
             *  └───│───│───│── Entity                                              | Entity                |            |                      |            |               | Blob, Graph, Search, EntityMetric |
             *      └───│───│────└─ Entity Property                                 | Entity                | Property   |                      |            | Property Name |                                   |
             *          └───│── Entity Provider                                     | EntityIntegrationType |            |                      | Id         |               | EntityMetric                      |
             *              │    └─ Entity Provider Property                        | EntityIntegrationType | Property   |                      | Id         | Property Name |                                   |
             *              └── Entity Provider Definition                          | EntityIntegration     |            | Id                   | Id         |               | EntityMetric                      |
             *                   └─ Entity Provider Definition Property             | EntityIntegration     | Property   | Id                   | Id         | Property Name |                                   |
             *
             */

            var entityIntegrationDimensions = existingDimensions.Where(d => d.DimensionType == MetricDimensionType.EntityIntegration && d.DimensionDetailType == MetricDimensionDetailType.None && d.ProviderDefinitionId.HasValue && d.ProviderId.HasValue);

            if (entityIntegrationDimensions.Any())
            {
                foreach (var entityDimension in entityIntegrationDimensions)
                    yield return this.GetDefaultGlobalDimension(context, entityDimension.ProviderDefinitionId, entityDimension.ProviderId);
            }

            var entityIntegrationTypeDimensions = existingDimensions.Where(d => d.DimensionType == MetricDimensionType.EntityIntegrationType && d.DimensionDetailType == MetricDimensionDetailType.None && d.ProviderId.HasValue);

            if (entityIntegrationTypeDimensions.Any())
            {
                foreach (var entityDimension in entityIntegrationTypeDimensions)
                    yield return this.GetDefaultGlobalDimension(context, entityDimension.ProviderId);
            }

            if (existingDimensions.Any(d => d.DimensionType == MetricDimensionType.Entity))
                yield return this.GetDefaultGlobalDimension(context);
        }

        public override IEnumerable<IMetricDimension> GetDimensionsToCalculate(MetricsProcessingContext context, Entity entity)
        {
            /*
             *                                                                        Dimension Table:
             *
             *                                                                      | DimensionType         | DetailType | ProviderDefinitionId | ProviderId | Detail        | Persistence                       |
             *                                                                      |-----------------------|------------|----------------------|------------|---------------|-----------------------------------|
             * Global                                                               | Global                |            |                      |            |               |                                   |
             *  │  Global Property                                                  | Global                | Property   |                      |            | Property Name |                                   |
             *  │   │  Global Provider                                              | GlobalIntegrationType |            |                      | Id         |               |                                   |
             *  │   │   │  Global Provider Definition                               | GlobalIntegration     |            | Id                   | Id         |               |                                   |
             *  │   │   │   │                                                       |-----------------------|------------|----------------------|------------|---------------|-----------------------------------|
             *  └───│───│───│── Entity                                              | Entity                |            |                      |            |               | Blob, Graph, Search, EntityMetric |
             *      └───│───│────└─ Entity Property                                 | Entity                | Property   |                      |            | Property Name |                                   |
             *          └───│── Entity Provider                                     | EntityIntegrationType |            |                      | Id         |               | EntityMetric                      |
             *              │    └─ Entity Provider Property                        | EntityIntegrationType | Property   |                      | Id         | Property Name |                                   |
             *              └── Entity Provider Definition                          | EntityIntegration     |            | Id                   | Id         |               | EntityMetric                      |
             *                   └─ Entity Provider Definition Property             | EntityIntegration     | Property   | Id                   | Id         | Property Name |                                   |
             *
             */

            // Provider Definition
            foreach (var group in entity.Details.DataEntries.GroupBy(d => d.OriginProviderDefinitionId))
            {
                if (group.Key == null)
                    continue;

                var providerDefinition = context.Organization.Providers.GetProviderDefinition(context, group.Key.Value);

                if (providerDefinition == null)
                    break;

                var keys = group.SelectMany(d => d.ProcessedEntityData.Properties.Keys).Distinct().ToList();

                var globalDimension      = this.GetDefaultGlobalDimension(context, group.Key, providerDefinition.ProviderId);
                var entityLevelDimension = new MetricDimension(context, this, MetricDimensionType.EntityIntegration, MetricDimensionDetailType.None, providerDefinitionId: group.Key, providerId: providerDefinition.ProviderId, persistence: MetricDimensionPersistence.EntityMetric) { ParentDimension = globalDimension };

                foreach (var key in keys)
                    yield return new MetricDimension(context, this, entityLevelDimension, MetricDimensionType.EntityIntegration, MetricDimensionDetailType.Property, providerDefinitionId: group.Key, providerId: providerDefinition.ProviderId, dimensionDetail: key);

                if (keys.Any())
                    yield return entityLevelDimension;
            }

            // Provider
            foreach (var group in entity.Details.DataEntries.Where(d => d.OriginProviderDefinitionId.HasValue)
                .GroupBy(d => this.providerResolver.ResolveProvider(context, d.OriginProviderDefinitionId.Value)))
            {
                if (group.Key == null)
                    continue;

                var keys = group.SelectMany(d => d.ProcessedEntityData.Properties.Keys).Distinct().ToList();

                var globalDimension      = this.GetDefaultGlobalDimension(context, group.Key.Id);
                var entityLevelDimension = new MetricDimension(context, this, MetricDimensionType.EntityIntegrationType, MetricDimensionDetailType.None, providerId: group.Key.Id, persistence: MetricDimensionPersistence.EntityMetric) { ParentDimension = globalDimension };

                foreach (var key in keys)
                    yield return new MetricDimension(context, this, entityLevelDimension, MetricDimensionType.EntityIntegrationType, MetricDimensionDetailType.Property, providerId: group.Key.Id, dimensionDetail: key);

                if (keys.Any())
                    yield return entityLevelDimension;
            }

            // Entity Property
            {
                var globalDimension      = this.GetDefaultGlobalDimension(context);
                var entityLevelDimension = new MetricDimension(context, this, MetricDimensionType.Entity, MetricDimensionDetailType.None, persistence: MetricDimensionPersistence.Blob | MetricDimensionPersistence.Graph | MetricDimensionPersistence.Search | MetricDimensionPersistence.EntityMetric) { ParentDimension = globalDimension };

                foreach (var key in entity.Properties.Keys)
                {
                    yield return new MetricDimension(context, this, entityLevelDimension, MetricDimensionType.Entity, MetricDimensionDetailType.Property, dimensionDetail: key, persistence: MetricDimensionPersistence.None);
                }

                // Entity
                if (entity.Properties.Any())
                    yield return entityLevelDimension;
            }
        }

        private UniqueValuesMap GetUniqueValuesMap(Entity entity, string propertyName, Func<IVersionPart, bool> versionFilter = null)
        {
            if (entity.Details.VersionHistory.Versions.Count != entity.Details.DataEntries.Count || entity.Details.VersionHistory.Versions.Any(v => v.DataPart == null))
                VersionHistoryProcessing.CreateChangeHistory(entity);

            var branches = entity.Details.VersionHistory.Branches;

            var mergedBranches = new List<MergedBranch>();

            foreach (var branch in branches)
            {
                var versionParts    = entity.Details.VersionHistory.GetBranch(branch);
                var allVersionParts = versionParts;

                if (versionFilter != null)
                    versionParts = versionParts.Where(versionFilter);

                if (!versionParts.Any())
                    continue;

                var mergedBranch = this.MergeDataParts(versionParts, allVersionParts);

                mergedBranches.Add(mergedBranch);
            }

            var uniqueValue = this.GetUniqueValues(mergedBranches, p => p.Properties.GetValue(propertyName));

            return uniqueValue;
        }

        public UniqueValuesMap GetUniqueValues(IEnumerable<MergedBranch> mergedBranches, Func<IProcessedEntityMetadata, string> func)
        {
            var groups      = mergedBranches.Select(m => func(m.MergedData)).GroupBy(v => v);
            var headGroups  = mergedBranches.Select(m => func(m.HeadData)).GroupBy(v => v);

            var branchCount = mergedBranches.Count();

            return new UniqueValuesMap(branchCount, groups, headGroups);
        }

        /**********************************************************************************************************
         * INNER TYPES
         **********************************************************************************************************/

        public struct UniqueValuesMap
        {
            public UniqueValuesMap(
                int branchCount,
                IEnumerable<IGrouping<string, string>> groups,
                IEnumerable<IGrouping<string, string>> headGroups)
            {
                var heads = headGroups.ToLookup(g => g.Key);

                this.Values = groups.Select(g => new UniqueValueEntry(g.Key, g.Count(), heads.Contains(g.Key) ? heads[g.Key].Sum(l => l.Count()) : 0)).ToList();

                this.ValuesCount            = this.Values.Where(v => v.Value != null).Sum(v => v.Count);
                this.MissingValuesCount     = this.Values.Where(v => v.Value == null).Sum(v => v.Count);
                this.MaxUniqueValueCount    = this.Values.Where(v => v.Value != null).Max(v => v.Count, 0);
                this.HeadValuesCount        = this.Values.Where(v => v.Value != null).Max(v => v.CountAtHead, 0);
                this.BranchCount            = branchCount;
            }

            public ICollection<UniqueValueEntry> Values { get; }

            public int MaxUniqueValueCount { get; }
            public int ValuesCount { get; }
            public int MissingValuesCount { get; }
            public int HeadValuesCount { get; }
            public int BranchCount { get; }
        }

        public struct UniqueValueEntry
        {
            public UniqueValueEntry(string value, int count, int countAtHead)
            {
                this.Value = value;
                this.Count = count;
                this.CountAtHead = countAtHead;
            }

            public string Value { get; }
            public int Count { get; }
            public int CountAtHead { get; }
        }
    }
}

```