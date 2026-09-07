---
layout: cluedin
title: Scheduled Time Jobs
parent: Legacy development documentation
grand_parent: Archive
nav_order: 160
permalink: /archive/legacy-development/scheduled-time-jobs
content_type: reference
redirect_from: ["/development/scheduled-time-jobs"]
source_path: docs/090-development/180-scheduled-time-jobs.md
tags: ["development","jobs"]
published: false
---

CluedIn has a generic Job system that allows you to run simple background jobs. Here is an example of how you could add your own custom jobs that run once at a later point in time. 

```csharp
var jobServerClient = this.ApplicationContext.Container.TryResolve<IJobServerClient>();

if (jobServerClient == null)
{
    context.Log.Error(() => "Could not find IJobServerClient in container");
    return this.Request.CreateErrorResponse(HttpStatusCode.InternalServerError, "Our job server is down and not accepting new providers for now. Please try again later.");
}

//Schedule Recurring Job
jobServerClient.Run(this.ApplicationContext.Container.Resolve<IJob>(), new JobArgs() { UserId = context.Principal.Identity.UserId.ToString(), Message = providerDefinition.ProviderId.ToString(), Schedule = jobDataCheck.Schedule(DateTimeOffset.Now, providerDefinition.WebHooks != null ? providerDefinition.WebHooks.Value : false), ConfigurationId = providerDefinition.Id.ToString(), OrganizationId = context.Organization.Id.ToString() });
```