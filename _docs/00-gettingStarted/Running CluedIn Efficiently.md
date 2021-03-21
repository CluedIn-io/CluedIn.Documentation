---
category: Get Started
title: Running CluedIn Efficiently for Cost
---

### Introduction

When running big data platforms in the cloud, it is important to remember that things cost money to run. There are mainly two main expenses in running CluedIn and they are processing of data and storage. To put things in perspective, processing is usually 90% of the cost, storage being the other. Hence, CluedIn can be run in a way to optimise for cost, but can also be run in a way that does not. 

Setting the baseline, CluedIn costs roughly $10 a day to run in Microsoft Azure with no data in it. As soon as you add data to CluedIn, and in turn, require processing of that data, the cost goes up. With processing being the main expense, one can also optimise workloads in order to capitilise on doing many things at the same time. For example, imagine that you add a new processing rule where every record that has a name that includes "Lego" should be tagged with Lego. Naturally, the only records that need to be reprocessed are those that have "Lego""in the name. This does not require a full re-process of all data, and hence although you can do this, it would not be optiminal for cost as you would need to load up all records back into the processing pipeline to have it only pay attention to the few records that actually meet the requirements of change. CluedIn will still need to evalulate all of its processes to see what it needs to do. 

CluedIn is an application that ships as a product with many dependencies. These dependencies are packaged up into Docker Containers. For example, CluedIn use ElasticSearch as one of its dependencies. This means that the cost of running this service is embedded into the cost of running CluedIn. There are many times where you would want to pull this service out of the CluedIn stack and move it onto a PAAS or even SAAS version. In our experience, this is typically more expensive, but it does also come with its benefits. Running CluedIn with all dependencies internally hosted within CluedIn itself will typically yield the most cost effective way to host CluedIn.

### Batching up Changes

If we look at the way we run projects, we will typically make changes, add functionality and more. To run CluedIn as "cheaply" as possible, your best option is to have all of the additions and changes have as much overlap in reprocessing as possible. For example, if we have 1000 records in our CluedIn instance and we have added 10 rules, 3 more streams and 2 new quality metrics. Your best and cheapest option is to only need to reprocess the records that would be matched by the 3 rules, 3 streams and new quality metrics. 

The easiest way to do this today is to use your "actions" in GraphQL. In GraphQL, you can come up with your filter using the search function and for the matched records, you can run the postProcessing action. 

```JSON
{
  search(query:"entityType:/Movie")
  {
    entries
    {
      actions
      {
        postProcessing
      }
    }
  }
}
```