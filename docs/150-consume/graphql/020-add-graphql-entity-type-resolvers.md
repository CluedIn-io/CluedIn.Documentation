---
layout: cluedin
nav_order: 1
parent: GraphQL
grand_parent: Consume
permalink: consume/graphql/add-graphql-entity-type-resolvers
title: Add GraphQL entity type resolvers
tags: ["consume","graphql"]
---

You can add your own specific resolvers to fetch data given filters such as what business domain a record is. 

Here is an example of how to return Calendar Events in a different way through the GraphQL endpoints.


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

Here is a more complex example:

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