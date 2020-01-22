Parent Aggregation

Although CluedIn will persist data into many datastores, CluedIn will construct a parent hierarchy of data based off certain patterns in the graph. This becomes useful for when we would like to aggregate subtrees of parent / child relationships. Imagine you wanted to know an aggregate breakdown of all records that are linked to a particular company whether it is a direct child reference, or even a sub-child - parent aggregation will give you this but there are only certain edge types that will react to this functionality. Those include: 

/Parent
/PartOf

All other types of edges will not play a role in parent processing. You can extend the inbuilt implementation to add your own Edge types to watch, but we do recommend against creating hard coded new edge types in your crawlers. 