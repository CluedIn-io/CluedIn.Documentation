---
category: Get Started
title: Running CluedIn Efficiently for Cost
---

### Introduction

When running big data platforms in the cloud, it is important to remember that things cost money to run. There are mainly two main expenses in running CluedIn and they are processing of data and storage. To put things in perspective, processing is usually 90% of the cost, storage being the other. Hence, CluedIn can be run in a way to optimise for cost, but can also be run in a way that does not. 

Setting the baseline, CluedIn costs roughly $10 a day to run in Microsoft Azure with no data in it. As soon as you add data to CluedIn, and in turn, require processing of that data, the cost goes up. You can see some approximations of cloud costs in Microsoft Azure [here](https://www.cluedin.com/cluedin-on-microsoft-azure). With processing being the main expense, one can also optimise workloads in order to capitilise on doing many things at the same time. For example, imagine that you add a new processing rule where every record that has a name that includes "Lego" should be tagged with Lego. Naturally, the only records that need to be reprocessed are those that have "Lego""in the name. This does not require a full re-process of all data, and hence although you can do this, it would not be optiminal for cost as you would need to load up all records back into the processing pipeline to have it only pay attention to the few records that actually meet the requirements of change. CluedIn will still need to evalulate all of its processes to see what it needs to do. 

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

###Only store what needs attention

Often, the question is asked, "What data should CluedIn process?". The answer depends on the situation, but in general, the answer is "The data that needs attention in cleaning, governing, integrating, enriching and all the other goodness that CluedIn brings". You might find that some transactional and analytical data meets this need, you might find that other transactional data does not. Naturally, the less data you give to CluedIn the less it costs to operate. This is why you should be careful to analyse the data coming into CluedIn and decide if it actually needs to be processed by CluedIn. 

###Downscale the application when it is not being used

CluedIn uses Kubernetes for many reasons, but one of those is to make sure that the environment can scale up and down when needed. CluedIn can scale down different parts of the application to run at a lower cost while heavy processing is not occuring. 

###Setup retention policies within the platform

Although CluedIn is useful for storing the history of data as it changes, you might find that there is certain data that can benefit from CluedIn's ability to setup retention of data. This will either remove or archive the data on a time schedule. The less data in CluedIn, the cheaper it is to operate. 

###Turn features of CluedIn off

There are many features of CluedIn that you might find are not necessary to solve your usecases. By default there are a combination of features turned on or off in the release of CluedIn. You can discover these from your settings within the User Interface. Naturally, the more features that are turned on, the more CPU cycles are needed to run per record that enters CluedIn or is reprocessed. You can systematically turn features off in CluedIn to lower the operational cost if these features are not needed. As an example, you might find that calculating quality metrics or running sensitivity detection is not needed for your use cases and hence these can be globally disabled. 