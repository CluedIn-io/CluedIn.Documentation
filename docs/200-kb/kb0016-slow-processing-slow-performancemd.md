---
layout: cluedin
title: Slow Performance
parent: Knowledge base
permalink: /kb/slow
tags: ["Rules", "Performance"]
nav_order: 17
---

# CluedIn Is Processing Slowly and Feels Slow in General

CluedIn is designed to process large volumes of data at scale, but in some cases you may notice that the platform feels “slow” — whether that’s during ingestion, rule execution, data linking, or even while navigating the user interface.  

This article explains the typical reasons why CluedIn might perform slowly, how to troubleshoot performance bottlenecks, and best practices to keep your environment running efficiently.

---

## What Does "Slow" Mean?

Performance issues in CluedIn can show up in different ways:

- **Ingestion Lag**: New data takes longer than expected to appear in the platform.  
- **Rule Processing Delays**: Rules take longer to apply or complete.  
- **Entity Linking/Matching**: Deduplication or linking jobs run slowly.  
- **Export Latency**: Exports to downstream systems take longer to complete.  
- **UI Responsiveness**: The CluedIn portal feels sluggish when navigating or opening dashboards.  

Identifying *which area feels slow* is the first step to diagnosing the cause.

---

## Common Causes of Performance Issues

### 1. High Data Volumes
- **Symptom**: Processing slows as more records are ingested.  
- **Explanation**: Larger datasets mean more work for ingestion, matching, and rules engines.  
- **Fix**: Scale your CluedIn environment to handle growth; consider batching ingestion jobs.  

---

### 2. Complex or Excessive Rules
- **Symptom**: Rules engine takes a long time to run.  
- **Explanation**: Multiple active rules or complex regex conditions can increase evaluation overhead.  
- **Fix**: Review active rules, simplify logic, and disable rules that are not essential.  

---

### 3. Resource Constraints
- **Symptom**: The whole platform (processing + UI) feels sluggish.  
- **Explanation**: The CluedIn instance does not have enough CPU, memory, or storage IOPS to handle workload.  
- **Fix**:  
  - Run CluedIn on **dedicated infrastructure**, not a shared environment.  
  - Scale up VM/container resources.  
  - Monitor system utilization to detect bottlenecks.  

---

### 4. Network or Connectivity Issues
- **Symptom**: Ingestion from external sources and exports to downstream systems are slow.  
- **Explanation**: Latency or instability in network connections to source/target systems slows down jobs.  
- **Fix**: Ensure stable, high-bandwidth connections between CluedIn and data sources/destinations.  

---

### 5. Inefficient Matching Configurations
- **Symptom**: Linking and deduplication jobs are disproportionately slow.  
- **Explanation**: Overly broad or poorly tuned match rules increase the number of comparisons per entity.  
- **Fix**: Optimize matching rules to focus on the most reliable identifiers.  

---

### 6. Running Heavy Jobs on Underpowered Machines
- **Symptom**: Toolkit exports/imports or processing jobs time out.  
- **Explanation**: Running CluedIn utilities (e.g., Product Toolkit) on personal laptops or small VMs can cause slowness.  
- **Fix**: Use **dedicated servers or cloud VMs** with sufficient resources for large-scale jobs.  

---

### 7. Competing Workloads
- **Symptom**: Performance degrades when multiple ingestion, rules, and export jobs run in parallel.  
- **Explanation**: Shared resources are consumed by concurrent jobs.  
- **Fix**: Schedule heavy workloads during off-peak hours or stagger job execution.  

---

## Troubleshooting Checklist

1. **Identify Where It’s Slow**  
   - Is it ingestion, rule execution, linking, exporting, or UI?  

2. **Check Logs & Dashboards**  
   - Review processing logs for errors or bottlenecks.  
   - Check dashboards for job status and queue lengths.  

3. **Monitor System Resources**  
   - CPU, memory, and disk usage should be reviewed on the CluedIn host.  

4. **Audit Rules & Match Configurations**  
   - Disable unnecessary rules.  
   - Simplify complex logic.  
   - Refine match rules.  

5. **Test Environment Sizing**  
   - Compare resource allocation (CPU/RAM/storage) to recommended CluedIn sizing guidelines.  
   - Scale up if needed.  

6. **Check Network Performance**  
   - Ensure data source/destination connectivity is reliable and performant.  

7. **Try Smaller Batches**  
   - Re-run ingestion or exports on smaller subsets to isolate scaling issues.  

---

## Best Practices to Maintain Good Performance

- **Run CluedIn on Dedicated Infrastructure**: Avoid running on shared or undersized machines.  
- **Scale with Data Growth**: Allocate more resources as your dataset grows.  
- **Schedule Heavy Jobs Strategically**: Run big exports/imports or reprocessing during quiet hours.  
- **Regularly Audit Rules**: Keep only the Rules that add value; retire unused ones.  
- **Optimize Matching Configurations**: Focus on the most discriminating identifiers.  
- **Monitor Continuously**: Use system and CluedIn logs/dashboards to stay ahead of bottlenecks.  

---

## Summary

When CluedIn feels slow, it is usually due to **large data volumes, complex rules, insufficient resources, or network constraints**. By identifying where the slowness occurs, monitoring resources, and following optimization best practices, you can significantly improve performance.  

If slowness persists even after optimization, collect logs and environment metrics and contact CluedIn Support for further assistance.  

---

