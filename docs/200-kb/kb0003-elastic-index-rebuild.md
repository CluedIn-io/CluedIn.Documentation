---
layout: cluedin
title: Rebuilding Elasticsearch index
parent: Knowledge base
permalink: kb/elastic-index-rebuild
tags: ["search","elasticsearch","index","rebuild","reprocess","reindex"]
last_modified: 2021-10-20
nav_order: 3
published: false
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

### Problem
Elasticsearch index is corrupt or lost. How can I save my data?

### Solution
Don't worry; your data is not lost and still exists in Neo4j and Microsoft SQL Server databases.
You can restore the Elasticsearch index by reprocessing CluedIn entities.

If the index is completely broken, it can be easier just to clear the disk and build a new index.

In this article, we will show you how to do that. **Please, keep in mind that the operations listed below are dangerous. Therefore you should be careful and understand what these operations do.**

The commands also depend on your setup and can be slightly different. Further, we assume that CluedIn is installed with a standard Helm chart in a `cluedin` namespace.


#### Scale down the Elasticsearch and CluedIn

```powershell
kubectl scale deployments --selector app=cluedin --replicas=0 -n cluedin;
kubectl scale statefulsets --selector app=elasticsearch-master --replicas=0 -n cluedin;
```

After this step, you should not see any Elasticsearch or CluedIn -server, -processing, or -crawler pods.

#### Delete the Elasticsearch persistent volume

```powershell
kubectl get pv
```

You will see a persistent volume with a claim named like `default/elasticsearch-master`. Remember its name.

Delete the Elasticsearch persistent volume:

```powershell
kubectl delete pv default/elasticsearch-master -n cluedin
```

#### Scale up the Elasticsearch

It's important to do it *before* you scale up CluedIn deployments.

```powershell
kubectl scale statefulsets --selector app=elasticsearch-master --replicas=1 -n cluedin
```

After this step, a new persistent volume will be created.

#### Scale up CluedIn

```powershell
kubectl scale deployments --selector app=cluedin --replicas=1 -n cluedin
```

You will see that CluedIn is running, but there are no entities in the UI.

#### Reprocess the entities

Now, you can reprocess the entities. However, to not overload the queue, we recommend doing it separately for each entity type:

```bash
curl \
  --location \
  --request GET '{url}/api/api/admin/commands/process/all/entityType/?organizationId={orgid}&entityType={entitytype}&minsize=0' \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Bearer ...
```

For more details about the API calls, please refer to the [API documentation](../consume/rest-api).
