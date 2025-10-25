---
layout: cluedin
nav_order: 1
parent: GraphQL
grand_parent: Consume
permalink: /consume/graphql/add-graphql-entity-type-resolvers
title: Add GraphQL entity type resolvers
tags: ["consume","graphql"]
---
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

You can extend CluedIn’s GraphQL endpoint by adding custom entity resolvers that fetch data based on specific filters. For example, by business domain or entity type.

The following examples demonstrate how to implement your own GraphQL resolvers for specific entity types.

## Example 1: Calendar event entity resolver

This example shows how to return calendar events in a customized way through the GraphQL endpoint.


```csharp
using System.Linq;
using System.Threading.Tasks;

using CluedIn.Core.Data;
using CluedIn.Core.GraphQL.Builders;

using GraphQL.Types;

namespace Custom.GraphQL.Types.Specific
{
    /// <summary>The entity graph type.</summary>
    /// <seealso cref="Entity" />
    /// <seealso cref="IEntity" />
    public class CalendarEventEntityGraphType : ObjectGraphType<CalendarEventEntity>, IComplexGraphType<CalendarEventEntity>
    {
        public CalendarEventEntityGraphType(ICluedInData data)
        {
            this.Name = "Calendar_Event_Entity";

            this.Field<ListGraphType<EntityInterface>>()
                .Name("attendees")
                .Resolve(ctx => ctx.GetDataLoader(async ids =>
                    {
                        // var ast = ctx.FieldAst;
                        // ast.SelectionSet.Selections;

                        var authors = data.GetEdgesOfType(ids, EntityEdgeType.Attended);
                        var lookup = authors.SelectMany(f => f.Endpoints.Select(ff => new { Key = f.ContextEntityId, Endpoint = ff }))
                            .ToLookup(x => x.Key, x => TypedEntityConverter.CreateSpecificType(x.Endpoint));

                        return await Task.FromResult(lookup);
                    }).LoadAsync(ctx.Source.Id));

            EntityInterface.ConfigureInterface(this, data);

            this.ConfigureFields(CluedIn.Core.Data.Vocabularies.Vocabularies.CluedInEvent);

            this.Interface<EntityInterface>();
        }
    }
}
```

## Example 2: File entity resolver

The following example shows a more advanced resolver for file entities. This implementation demonstrates additional logic, including field inspection and working directly with entity edges.


```csharp
using System.Linq;

using CluedIn.Core.Data;
using CluedIn.Core.Data.Parts;
using CluedIn.Core.GraphQL.Builders;
using CluedIn.Core.GraphQL.Types.Specific;

using GraphQL.Types;

namespace Custom.GraphQL.Types.Specific
{
    /// <summary>The entity graph type.</summary>
    /// <seealso cref="Entity" />
    /// <seealso cref="IEntity" />
    public class FilesFileEntityGraphType : ObjectGraphType<FilesFileEntity>, IComplexGraphType<FilesFileEntity>
    {
        public FilesFileEntityGraphType(ICluedInData data)
        {
            this.Name = "Files_File_Entity";

            this.Field<ListGraphType<EntityInterface>>()
                .Name("attendees")
                .Resolve(ctx => ctx.GetDataLoader(async ids =>
                    {
                        var ast = ctx.FieldAst;
                        ast.SelectionSet.Selections;

                        var authors = data.GetEdgesOfType(ids, EntityEdgeType.Attended);
                        var lookup = authors.SelectMany(f => f.Endpoints.Select(ff => new { Key = f.ContextEntityId, Endpoint = ff }))
                            .ToLookup(x => x.Key, x => x.Endpoint);

                        return lookup;
                    }).LoadAsync(ctx.Source.Id));

            EntityInterface.ConfigureInterface(this, data);

            this.ConfigureFields(CluedIn.Core.Data.Vocabularies.Vocabularies.CluedInFile);

            this.Interface<EntityInterface>();
        }
    }
}
```