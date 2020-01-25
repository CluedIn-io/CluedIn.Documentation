Data Metric Explanations

Example queries
  metrics
  {
    name
    
    dimensions
    {
      id
      type
      ... on GlobalMetricDimension
      {
        children
        {
          id
        }
      }
      ... on MetricDimension
      {
        valueHistogram
      }
    }
    
    globalLevel: dimension(id : "25118d8c-696e-591f-9eb5-083bff9488d4")
    {
      id
      ... on GlobalMetricDimension
      {
        children
        {
          id
        }
      }
    }
    
    entityLevel: dimension(id: "b545b625-5a9b-5614-ae57-f2c61e02bdb9")
    {
      id
      ... on MetricDimension
      {
        valueHistogram
      }
    }
    
    globalDimension
    {
      id
      latestValue
      parentId
      
      children
      {
        id
        parentId
        type
        detailType
        detail
        providerDefinitionId
        providerId
        providerName
        
#        valueHistogram
        
        entityValues(
          sort: VALUE, 
          sortDirection: ASCENDING,
          cursor: "ewAiAFAAYQBnAGUAIgA6ADUALAAiAFAAYQBnAGUAUwBpAHoAZQAiADoAMgAwAH0A"
        )
        {
          entries
          {
            value
            dimension
            {
              detailType
              latestValue
              children
              {
                detailType
                detail
                latestValue
              }
            }
            entity
            {
              name
              entityType
            }
          }
          cursor
        }
       
        children
        {
        	id
        	parentId
        	type
        	detailType
        	detail
        	providerDefinitionId
        	providerId
        	providerName
          
          valueHistogram
          
          entityValues(sortDirection: ASCENDING)
          {
            entries
            {
              value
            }
            cursor
          }
        }
      }
    }
  }