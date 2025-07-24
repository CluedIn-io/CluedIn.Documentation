---
layout: cluedin
title: Recurring Time Jobs
parent: Development
nav_order: 170
has_children: false
permalink: development/recurring-time-jobs
tags: ["development","jobs"]
published: false
---

CluedIn has a generic Job system that allows you to run simple background jobs. Here is an example of how you could add your own custom jobs that run on a recurring schedule.

```csharp
var jobServerClient = this.ApplicationContext.Container.TryResolve<IJobServerClient>();

if (jobServerClient == null)
{
    context.Log.Error(() => "Could not find IJobServerClient in container");
    return this.Request.CreateErrorResponse(HttpStatusCode.InternalServerError, "Our job server is down and not accepting new providers for now. Please try again later.");
}

//Schedule Weekly Full Recrawl Recurring Job
jobServerClient.Run(this.ApplicationContext.Container.Resolve<IFullCrawlJob>(), new JobArgs() { UserId = context.Principal.Identity.UserId.ToString(), Message = providerDefinition.ProviderId.ToString(), Schedule = jobDataCheck.Schedule(DateTimeOffset.Now, providerDefinition.WebHooks != null ? providerDefinition.WebHooks.Value : false), ConfigurationId = providerDefinition.Id.ToString(), OrganizationId = context.Organization.Id.ToString() });
```
