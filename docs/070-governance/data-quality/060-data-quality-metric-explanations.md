---
layout: cluedin
title: Data Quality Metric Explanations
parent: Data Quality Metrics
grand_parent: Governance
nav_order: 3
has_children: false
permalink: /preparation/data-quality-metrics/data-quality-metric-explanations
tags: ["governance","quality-metrics"]
---

CluedIn calculates data quality metrics based off all data that is ingested into the platform. There are many times where you will want a verbose explanation on why a certain data quality score was given. For example, imagine if your had what you think is golden records, but CluedIn gave it very low quality scores - you would want to know exactly why. 

The first option is to visualize this explanation within the user interface by clicking on the "Explain" button when you see a data quality score widget. 

The second example would be to get this data from our GraphQL endpoint. 

Here is an example that will fetch a detailed explanation of the "Accuracy" metric for Global and Entity Level dimensions.

```json
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
```