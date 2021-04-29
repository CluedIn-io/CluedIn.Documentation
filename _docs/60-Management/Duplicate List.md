---
category: Management
title: Duplicate List
---

Your duplicates menu will give you a list of different types of possible duplicate records. 

Clicking on the duplicate entries will allow you to see the list of possible duplicates and then place them into a merge operation as to choose which properties are more likely to be the golden value. 

As a developer, you can also add your own types of duplicate detection as well.

To do this, create a C# class and inherit from the IDuplicateQuery interface and CluedIn will then run the SearchDescriptors to generate the list. Compile your class and drop the DLL into the ServerComponent folder and reboot CluedIn.

Here as an example of a Duplicate Query detection that you could add yourself: 

```csharp
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

using CluedIn.Core;
using CluedIn.Core.Configuration;
using CluedIn.Core.Data;
using CluedIn.Core.DataStore;

using Core.Data.Repositories;
using Core.Data.Repositories.Search;
using Core.Data.Repositories.Search.Aggregations;
using Core.Data.Repositories.Search.Filtering;

namespace CluedIn.Processing.EntityResolution.Queries
{
    public class DuplicateEntityNameQuery : IOnlineDuplicateEntityQuery
    {
        public string Name { get; } = "Organization Name";

        public string DisplayName { get; } = "Duplicate Vocabulary Key for Organization Names";

        public async Task<IEnumerable<IDuplicateEntityQueryResultSet>> GetPotentialDuplicatesAsync(ExecutionContext context, EntityType entityType = null)
        {
            var repos = new CluedInRepositories();

            IEnumerable<EntityType> entityTypes;

            if (entityType == null)
            {
                var query = new ParsedQuery();
                query.Query                           = "*";
                query.Fields                          = new List<string>() { "entityType" };
                query.Cursor                          = PagingCursor.Default;
                query.Aggregations                    = new List<AggregationQuery>() { new TermAggregationQuery("entityType", 150)};
                query.RankingSettings                 = ParsedQuery.DefaultRanking;
                query.IncludeUnstructuredData         = !ConfigurationManagerEx.AppSettings.GetFlag("Feature.Filters.ShadowEntities", true);
                query.OptionalFields                  = new List<string>();
                query.SearchSpecificEntityTypesByName = new List<string>();

                var results = await repos.Search.ExecuteQuery(context, query);

                var entityTypeAggregation = (TermAggregationBucket)results.Aggregations.First().Value;

                entityTypes = entityTypeAggregation.Items.Select(t => (EntityType)t.Name).ToList();
            }
            else
                entityTypes = new[] { entityType };

            var resultSets = new List<IDuplicateEntityQueryResultSet>(entityTypes.Count());

            foreach (var type in entityTypes)
            {
                var query = new ParsedQuery();
                query.Query                           = "*";
                query.Fields                          = new List<string>() { "properties.organization.name" };
                query.Cursor                          = PagingCursor.Default;
                query.Aggregations                    = new List<AggregationQuery>() { new TermAggregationQuery("properties.organization.name", 150)};
                query.RankingSettings                 = ParsedQuery.DefaultRanking;
                query.IncludeUnstructuredData         = !ConfigurationManagerEx.AppSettings.GetFlag("Feature.Filters.ShadowEntities", true);
                query.OptionalFields                  = new List<string>();
                query.SearchSpecificEntityTypesByName = new List<string>();

                query.Filters = ParsedFilteringQuery.Parse(context, query, null, new[]
                                                                                 {
                                                                                     new FilterQuery()
                                                                                     {
                                                                                         FieldName       = "entityType",
                                                                                         AggregationName = "entityType",
                                                                                         Operator        = DefaultSearchOperator.And,
                                                                                         Value           = type.ToString()
                                                                                     }
                                                                                 });

                var results = await repos.Search.ExecuteQuery(context, query);

                var nameAggregation = (TermAggregationBucket)results.Aggregations.First().Value;

                if (nameAggregation.Items.Any(f => f.Count > 1))
                {
                    resultSets.Add(
                        new DuplicateEntityQueryResultSet(
                            this, 
                            type, 
                            $"Possible {type} Duplicates", 
                            nameAggregation.Items.Where(f => f.Count > 1).Select(f => new DuplicateEntityQueryGrouping(f.Name, f.Name, f.Count)))
                    );
                }
            }

            return resultSets;
        }

        public async Task<PagedDataResultWithCount<IEntity>> GetPotentialDuplicateEntityInstancesAsync(ExecutionContext context, string resultSetKey, string itemGroupingKey, PagingCursor cursor = null)
        {
            var repos = new CluedInRepositories();

            cursor = cursor ?? PagingCursor.Default;

            var query = new ParsedQuery();
            query.Query                           = "*";
            query.Fields                          = new List<string>() { "properties.organization.name" };
            query.Cursor                          = cursor;
            query.RankingSettings                 = ParsedQuery.DefaultRanking;
            query.IncludeUnstructuredData         = !ConfigurationManagerEx.AppSettings.GetFlag("Feature.Filters.ShadowEntities", true);
            query.OptionalFields                  = new List<string>();
            query.SearchSpecificEntityTypesByName = new List<string>();

            query.Filters = ParsedFilteringQuery.Parse(context, query, null, new[]
                                                                             {
                                                                                 new FilterQuery()
                                                                                 {
                                                                                     FieldName       = "entityType",
                                                                                     AggregationName = "entityType",
                                                                                     Operator        = DefaultSearchOperator.And,
                                                                                     Value           = resultSetKey
                                                                                 },
                                                                                 new FilterQuery()
                                                                                 {
                                                                                     FieldName       = "properties.organization.name",
                                                                                     AggregationName = "properties.organization.name",
                                                                                     Operator        = DefaultSearchOperator.And,
                                                                                     Value           = itemGroupingKey
                                                                                 }
                                                                             });

            var results = await repos.Search.ExecuteQuery(context, query);

            return new PagedDataResultWithCount<IEntity>(results.Entries.Select(e => e.Entity), results.TotalResults, ((cursor.Page + 1) * cursor.PageSize) < results.TotalResults ? results.NextCursor : null);
        }
    }
}
```

##Multi-Field Duplicates

It is often that you will want to check for parity across multiple fields to help validate if you have a possible duplicate.

The recommended way to handle this is to concatenate your values using a pre-processor within CluedIn so that you are not running this calculation at query time, but rather at indexing time. 

To do this, create a pre-processor and have your logic to take entities and combine properties together into a new value. For example if you were wanting to see if the organization.name, organization.website and organization.employeeSize was the same then you would create a new Vocabulary called combined.organization.keys and you would concatenate the values together of the 3 keys into one. 

You then can use the code above and instead of using organization.name as your field, you can use your new combined.organization.keys. 

You will most likely also want to support the case where this data changes and that this field also gets changed in that process. For this, implement a post-processor with the same logic. This will take care of the situations where you Clean data in CluedIn Clean and if one of those 3 values is update, you would also want to update the combined key as well.  