---
layout: cluedin
title: Rules running slowly
parent: Knowledge base
permalink: /kb/rules-slow
tags: ["Rules", "Performance"]
nav_order: 14
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

Rules in CluedIn are a powerful way to clean, standardize, and enrich your data as it flows through the platform. They allow you to automate transformations and enforce business logic at scale. However, in some cases, you may notice that your Rules take longer than expected to process.  

This article explains the key factors that influence Rule performance, common reasons why execution may be slow, and steps you can take to optimize and troubleshoot.

---

## How Rule Processing Works

Before diving into performance issues, it’s important to understand how Rules are executed in CluedIn:

1. **Trigger** – A Rule is triggered when new data is ingested or when a Rule is explicitly re-run on existing data.  
2. **Evaluation** – The Rule engine evaluates each record against the configured conditions.  
3. **Transformation** – For matching records, the Rule applies the transformation or enrichment logic.  
4. **Propagation** – Updates are written back to the affected entities and, if configured, published to downstream systems.  

The time it takes depends on the **volume of records**, the **complexity of the logic**, and the **resources available** in your CluedIn environment.

---

## Common Reasons Rules Run Slowly

### 1. Large Data Volumes
- **Symptom**: Rules that work quickly on small datasets suddenly take much longer on production-scale data.  
- **Explanation**: Each Rule must scan through entities to find matches. Processing millions of records inevitably takes more time.  

**Tip**: Test Rules on smaller sample datasets before applying them to production.  

---

### 2. Complex Rule Conditions
- **Symptom**: Rules with multiple conditions, regex patterns, or nested logic perform slower.  
- **Explanation**: Each additional condition increases the number of evaluations per record. Regex-based conditions are especially costly.  

**Tip**: Simplify Rule logic where possible. Split complex Rules into multiple smaller, focused Rules.  

---

### 3. High Number of Active Rules
- **Symptom**: Processing slows down as more Rules are added.  
- **Explanation**: CluedIn must evaluate every active Rule against incoming records. Even if most Rules don’t apply, they still need to be checked.  

**Tip**: Review your Rule library and disable Rules that are not actively needed.  

---

### 4. Data Distribution & Entity Linking
- **Symptom**: Rules that depend on entity relationships (e.g., linked customers, orders, or products) take longer.  
- **Explanation**: Linking requires lookups across multiple entities. Large or poorly matched datasets increase lookup overhead.  

**Tip**: Ensure entity matching configurations are optimized before running Rules that depend on them.  

---

### 5. Environment & Resource Constraints
- **Symptom**: Rules slow down during periods of heavy ingestion or other intensive processing.  
- **Explanation**: The Rule engine shares compute resources with ingestion, matching, and enrichment jobs. Resource contention can delay execution.  

**Tip**: Schedule large Rule runs during off-peak hours or scale your CluedIn deployment to handle higher throughput.  

---

### 6. Reprocessing vs. Incremental Runs
- **Symptom**: A Rule re-run on all historical data takes significantly longer than on new incremental data.  
- **Explanation**: Full reprocessing forces CluedIn to re-check all records, while incremental runs only apply to newly ingested or updated data.  

**Tip**: Use incremental runs where possible. Reserve full re-runs for cases where underlying Rule logic has changed.  

---

## How to Troubleshoot Slow Rules

1. **Check Rule Execution Logs**  
   - Navigate to **Rules > Execution History**.  
   - Look for patterns (e.g., long-running conditions, high record counts).  

2. **Measure Impact of Individual Rules**  
   - Disable all Rules.  
   - Re-enable them one by one to isolate performance bottlenecks.  

3. **Profile the Data**  
   - Use **Data Quality Profiling** to identify large or inconsistent fields that may slow down evaluation (e.g., very long text fields, improperly formatted values).  

4. **Check System Resources**  
   - Review CluedIn environment metrics (CPU, memory, queue depth).  
   - If resource constraints are observed, consider scaling the environment.  

5. **Engage with CluedIn Support**  
   - If performance is consistently poor despite optimization, raise a support ticket with logs and execution metrics.  

---

## Best Practices for Optimizing Rule Performance

- **Keep Rules Simple**: Favor straightforward conditions over complex regex or nested logic.  
- **Use Targeted Scopes**: Apply Rules only to relevant entity types, not globally.  
- **Batch Complex Logic**: Break down large transformations into multiple smaller Rules.  
- **Monitor & Review**: Regularly audit your Rules and disable ones that are no longer needed.  
- **Test at Scale**: Validate Rule performance in staging with production-like volumes.  
- **Leverage Scheduling**: Run heavy Rules during low-traffic times.  

---

## Summary

Rules may process slowly for a variety of reasons, most often due to large data volumes, complex conditions, or resource contention. By understanding how Rule execution works and following best practices for optimization, you can ensure that your Rules run efficiently and continue delivering value without bottlenecks.  

If you’ve optimized your setup and still see performance issues, contact CluedIn Support for advanced troubleshooting.  

---
