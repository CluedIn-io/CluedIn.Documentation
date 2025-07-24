---
layout: cluedin
title: Parent Aggregation
parent: Development
nav_order: 530
permalink: developer/parent-aggregation
tags: ["development"]
published: false
---

Although CluedIn will persist data into many datastores, CluedIn will construct a parent hierarchy of data based off certain patterns in the graph. This becomes useful for when we would like to aggregate subtrees of parent / child relationships. Imagine you wanted to know an aggregate breakdown of all records that are linked to a particular company whether it is a direct child reference, or even a sub-child - parent aggregation will give you this but there are only certain edge types that will react to this functionality. Those include: 

 - /Parent
 - /PartOf

All other types of edges will not play a role in parent processing. You can extend the inbuilt implementation to add your own Edge types to watch, but we do recommend against creating hard coded new edge types in your crawlers. 

For a detailed list of supported Parent Aggregation types: 

```csharp
var ignoredParentEdgeTypes = new EntityEdgeType[]
                    {
                        "/Code",
                        EntityEdgeType.Follows,
                        EntityEdgeType.For,         
                        EntityEdgeType.WorkedOn,    
                        EntityEdgeType.Read,
                        EntityEdgeType.ReadWrite,
                    };

                var nonTemporalLocalParentEdgeTypes = new[]
                    {
                        EntityEdgeType.At,
                        EntityEdgeType.CreatedAt,
                        EntityEdgeType.Modified,    
                        EntityEdgeType.ModifiedAt,
                        EntityEdgeType.DiscoveredAt,

                      
                        EntityEdgeType.IsType,      
                        EntityEdgeType.LocatedIn,
                        EntityEdgeType.Recipient,
                        EntityEdgeType.RequestedBy,
                       
                        EntityEdgeType.WorkedOn,    
                        EntityEdgeType.WorkedOnBy,
                        EntityEdgeType.Action,

                        EntityEdgeType.Mentioned,
                 
                        EntityEdgeType.Author,
                        EntityEdgeType.Birthday,

                        EntityEdgeType.Created,
                        EntityEdgeType.CreatedBy,
                        EntityEdgeType.DeletedBy,
                        EntityEdgeType.ManagedBy,
                        EntityEdgeType.ModifiedBy,
                        EntityEdgeType.OwnedBy,
                        EntityEdgeType.Owns,

                        EntityEdgeType.RequestedBy,
                        EntityEdgeType.WorkedOnBy,

                        EntityEdgeType.Received,
                        EntityEdgeType.Attended,
                        EntityEdgeType.Deployed,
                        EntityEdgeType.DueOn,
                        EntityEdgeType.InvitedTo,
                        EntityEdgeType.MemberOf,
                        EntityEdgeType.Presented,
                        EntityEdgeType.Received,
                        EntityEdgeType.Recipient,
                        EntityEdgeType.Registered,
                        EntityEdgeType.RequestedBy,
                        EntityEdgeType.StartedOn,
                        EntityEdgeType.EndedOn,
                        EntityEdgeType.WitheldIn,
                        EntityEdgeType.Competitor,
                        EntityEdgeType.Investor,
                        EntityEdgeType.ApprovedBy
                    };

                var nonTemporalParentEdgeTypes = new[]
                    {
                        EntityEdgeType.Parent,
                        EntityEdgeType.PartOf,
                        EntityEdgeType.AttachedTo,
                        EntityEdgeType.ManagedIn,
                        EntityEdgeType.WorksFor,
                        EntityEdgeType.UsedBy,     
                    };

                var parentOnlyEdgeTypes = new[]
                    {
                        EntityEdgeType.Represents   
                    };

                return new RuleSet
                    {
                        IgnoredParentEdgeTypes          = ignoredParentEdgeTypes,
                        NonTemporalLocalParentEdgeTypes = nonTemporalLocalParentEdgeTypes,
                        NonTemporalParentEdgeTypes      = nonTemporalParentEdgeTypes,
                        ParentOnlyEdgeTypes             = parentOnlyEdgeTypes,
                        SelectLocalParentEdges          = SelectLocalParentEdgesV2,
                        SelectParentEdges               = SelectParentEdgesV2,
                        SelectParentOnlyEdges           = SelectParentOnlyEdgesV2,
                        FilterIgnoredEdges              = FilterIgnoredEdgesV2
                    };
```