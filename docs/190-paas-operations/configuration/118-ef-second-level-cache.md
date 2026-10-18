---
layout: cluedin
nav_order: 118
parent: Configuration
grand_parent: PaaS operations
permalink: /deployment/infra-how-tos/ef-second-level-cache
title: EF Core second-level cache
headerIcon: "paas"
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

CluedIn 5.0 includes an optional EF Core second-level cache for reducing repeated SQL queries against read-heavy, low-churn relational data such as vocabularies, glossary data, rules, and organization settings.

{:.important}
The cache is disabled by default. Enable and tune it only when you operate the CluedIn platform and understand the impact of caching relational reads.

## Architecture

The cache uses two levels:

- **L1** — in-process memory cache on each CluedIn server instance.
- **L2** — Redis cache shared by all server instances.

On a read, CluedIn checks L1 first. If the value is not available, CluedIn checks L2 and backfills L1. If neither cache contains the value, the query is executed against SQL Server and the result can be cached.

When cached data is changed or deleted, CluedIn invalidates both levels and publishes an invalidation message through Redis so L1 caches on other running instances are also evicted.

## Prerequisites

Before enabling the feature:

- configure the `CacheStore` connection string to point to Redis
- confirm that all CluedIn server instances can reach the same Redis cache
- define an appropriate default TTL and any required table-specific overrides

## Configuration

The primary configuration settings are:

| Key | Default | Description |
|---|---:|---|
| `Feature.EFSecondLevelCache.Enabled` | `false` | Enables or disables the second-level cache. |
| `Feature.EFSecondLevelCache.DefaultTTLSeconds` | `60` | Default time-to-live for cacheable queries. |
| `Feature.EFSecondLevelCache.L1Enabled` | `true` | Enables the in-process L1 cache. Set to `false` for Redis-only behavior. |
| `Feature.EFSecondLevelCache.TTL.<TableName>` | not set | Overrides the TTL for a specific table. Set to `0` to exclude the table from caching. |

For example:

```text
Feature.EFSecondLevelCache.Enabled = true
Feature.EFSecondLevelCache.DefaultTTLSeconds = 60
Feature.EFSecondLevelCache.L1Enabled = true
Feature.EFSecondLevelCache.TTL.Vocabulary = 300
Feature.EFSecondLevelCache.TTL.SomeFrequentlyChangingTable = 0
```

## Whitelist-only caching

You can configure the cache so that only explicitly selected tables are cached:

1. Set `Feature.EFSecondLevelCache.DefaultTTLSeconds` to `0`.
1. Add `Feature.EFSecondLevelCache.TTL.<TableName>` entries with a positive TTL for the tables you want to cache.

This is useful when you want to start conservatively and only cache data known to be read-heavy and low-churn.

## Choose appropriate TTLs

Use shorter TTLs for data that changes frequently and longer TTLs for relatively static configuration data.

Long TTLs can improve cache hit rates but also make invalidation behavior more important. CluedIn invalidates cached entries on writes and propagates invalidation through Redis, but TTLs should still reflect the expected volatility of the data.

## Observability

The cache exposes Prometheus counters through the existing metrics endpoint:

| Metric | Description |
|---|---|
| `EFCacheL1HitCount` | Queries served from the in-process cache. |
| `EFCacheL2HitCount` | Queries served from Redis. |
| `EFCacheMissCount` | Queries that were not served from cache and went to SQL Server. |

The metrics include labels for the DbContext, SQL schema, and table or tables involved in the query.

Use these metrics to measure:

- overall cache hit rate
- L1 versus L2 effectiveness
- frequently missed tables
- cache behavior by CluedIn pod
- whether TTL tuning is improving database load

## When to enable the cache

The feature is most useful when:

- the platform performs repeated reads of the same relational configuration data
- SQL read load is significant
- the relevant tables change infrequently relative to how often they are read
- Redis is already configured and highly available

Leave the feature disabled if the operational benefit is unclear or you do not want to introduce another caching layer into query behavior.
