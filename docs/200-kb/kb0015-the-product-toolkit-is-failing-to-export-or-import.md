---
layout: cluedin
title: The Product Toolkit is failing to export or import
parent: Knowledge base
permalink: /kb/product-toolkit-issues
tags: ["Environment", "Deployment"]
nav_order: 16
published: false
---

# Troubleshooting: The Product Toolkit Is Failing to Export or Import

The CluedIn Product Toolkit allows you to export and import configurations such as entities, schemas, and rules between environments. This is essential for promoting changes from development to staging and production.  

Sometimes, you may encounter failures when running exports or imports. This article explains the most common reasons for failures, how to troubleshoot them, and best practices to ensure smooth operation.

---

## Common Reasons for Failures

### 1. Timeouts During Execution
- **Symptom**: Export or import jobs stall or fail with timeout errors.  
- **Cause**: Large datasets or complex configurations can exceed default timeout limits, especially if run on underpowered machines.  
- **Fix**:  
  - Run the Product Toolkit on a **dedicated server or cloud VM**, not on a personal laptop.  
  - Ensure stable network connectivity with sufficient bandwidth.  
  - For very large jobs, break down exports/imports into smaller, more manageable chunks.  

---

### 2. Insufficient Permissions (RACI Access)
- **Symptom**: Export or import completes partially, or fails with “permission denied” errors.  
- **Cause**: The account running the Toolkit does not have **Accountable (A)** level RACI access to the entities or configurations being moved.  
- **Fix**:  
  - Verify that your account has Accountable permissions for **all objects** in the scope of the export or import.  
  - If not, request elevated access from your CluedIn administrator.  

---

### 3. Missing or Incomplete Dependencies
- **Symptom**: Import fails due to missing references (e.g., schemas, rules, or entities not found).  
- **Cause**: Dependencies were not included in the export package, or were imported out of order.  
- **Fix**:  
  - Ensure you export **all dependent configurations** together.  
  - Import dependencies (schemas, vocabularies) before higher-level artifacts (rules, pipelines).  

---

### 4. Version Mismatches
- **Symptom**: Import fails due to incompatible format or unexpected fields.  
- **Cause**: Export was created in a different CluedIn version than the target environment.  
- **Fix**:  
  - Confirm both environments are running the same version of CluedIn.  
  - If not, upgrade/downgrade to align versions before attempting import.  

---

### 5. Environment Resource Constraints
- **Symptom**: Export/import hangs, crashes, or causes instability.  
- **Cause**: The machine running the Toolkit does not have enough memory, CPU, or disk space.  
- **Fix**:  
  - Run the Toolkit on a machine with **at least 4 vCPUs and 8GB+ RAM**.  
  - Monitor system resources during execution.  
  - Clean up temporary files and ensure adequate disk space is available.  

---

## How to Troubleshoot

1. **Check Logs**  
   - Review Toolkit log output for specific error messages.  
   - Logs are typically stored in the working directory where you ran the command.  

2. **Validate Permissions**  
   - Confirm the user has Accountable RACI access for the entire scope of the operation.  

3. **Test with Smaller Scope**  
   - Try exporting or importing a smaller subset of objects.  
   - If that works, expand gradually until you identify the problematic artifact.  

4. **Verify Environment Setup**  
   - Ensure the Toolkit is running on a dedicated machine with sufficient resources.  
   - Avoid running from personal laptops or unstable network connections.  

5. **Check CluedIn Version Compatibility**  
   - Confirm both source and target environments are on the same version.  
   - Align versions if mismatched.  

6. **Re-run with Debug Mode**  
   - Use debug flags (if available) to capture more detailed logs.  
   - Share logs with CluedIn Support if the issue persists.  

---

## Best Practices for Reliable Toolkit Operations

- **Run on a Dedicated Machine**: Use a dedicated server or VM for large exports/imports.  
- **Use Accountable RACI Access**: Always ensure you have Accountable access before starting.  
- **Export/Import in Logical Order**: Move foundational artifacts (schemas, vocabularies) before dependent ones (rules, pipelines).  
- **Monitor Logs and Metrics**: Track execution logs and system resource usage.  
- **Align Environments**: Keep source and target environments on the same CluedIn version.  
- **Test Before Production**: Run exports/imports in staging first before applying to production.  

---

## Summary

Product Toolkit export/import issues usually arise from **timeouts, missing permissions, incomplete dependencies, version mismatches, or resource limitations**. By running the Toolkit on a dedicated machine, ensuring Accountable RACI access, and following best practices, you can significantly reduce the risk of failures.  

If problems persist, collect execution logs and contact CluedIn Support for assistance.  

---


