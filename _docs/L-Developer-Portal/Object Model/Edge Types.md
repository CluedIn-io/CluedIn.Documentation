Edge Types

Edges Types are a way to determine the relationships between data. This is typically in the structure of a Object - Verb - Object. For example, John works at Lego. In CluedIn, edges can store properties such as weights and general metadata, but the main idea behind these edges is to describe the relationship for processing and querying purposes. 

In CluedIn, there are static Edge Types and Dynamic Edge Types. Static Edge Types are your way to set an Edge Type based off known rules that will not change. All other Edge Types should be Dynamic. 

It is always recommended to leave Edges in crawlers as generic as possible and introduce new processors in the processing server to dynamically resolve generic edge types into specific ones. Imagine you have an edge type of "Works At" that you set statically in your crawlers - you can see that it has a temporal factor to it, in that you have no guarantee that this will always be "Works At". Due to this, you can introduce new processors that would check other values e.g. A Job start and end date, and use this to dynamically change the edge type to "Worked At" if this person was ever to leave. 
