---
layout: cluedin
title: Rules are not working
parent: Knowledge base
permalink: /kb/rules-not-working
tags: ["Rules", "Debug"]
nav_order: 15
---

# Why Are My CluedIn Rules Not Working as Expected?

CluedIn Rules are designed to help you automate transformations, validations, and enrichment of your data. When they don’t behave as expected, it can be frustrating and may lead to incorrect data outcomes.  

This article explains the most common reasons Rules may not work, how to troubleshoot them, and best practices to ensure they deliver the results you want.

---

## Understanding How Rules Work

At a high level, a Rule in CluedIn consists of:
- **Scope**: The entities or attributes it applies to.  
- **Conditions**: The logic that determines whether the Rule applies.  
- **Actions**: The transformation or update to apply when conditions are met.  

If any of these are misconfigured, the Rule may not execute as you expect.

---

## Common Reasons Rules Don’t Work

### 1. Incorrect Scope or Target
- **Symptom**: Rule never seems to run.  
- **Cause**: The Rule is applied to the wrong entity type or attribute. For example, applying a `Customer` Rule on `Contact` entities.  
- **Fix**: Double-check the entity type and field mappings in the Rule configuration.  

---

### 2. Conditions That Never Match
- **Symptom**: Rule exists, but no records are updated.  
- **Cause**: Condition logic is too strict or incorrectly defined.  
  - Example: Condition is `Country = US`, but data uses `USA` or `United States`.  
  - Example: Regex pattern doesn’t align with the data format.  
- **Fix**: Validate the condition logic against sample data. Loosen overly strict conditions where necessary.  

---

### 3. Action Misconfiguration
- **Symptom**: Rule triggers but doesn’t update fields as intended.  
- **Cause**: The action is pointing to the wrong field or uses the wrong transformation.  
- **Fix**: Review the action configuration to ensure it references the correct attributes and expected values.  

---

### 4. Rule Execution Order
- **Symptom**: A Rule appears to run, but results are overridden.  
- **Cause**: Another Rule is executing afterwards and undoing or replacing the changes.  
- **Fix**: Review the **Rule execution order**. Consider merging related logic into a single Rule or adjusting order of operations.  

---

### 5. Data Quality Issues
- **Symptom**: Rule applies inconsistently.  
- **Cause**: Input data does not match expected formats or contains null values.  
- **Fix**: Run **Data Profiling** to check data consistency. Create preprocessing Rules to normalize data before applying main transformations.  

---

### 6. Rule Disabled or Not Published
- **Symptom**: Rule doesn’t run at all.  
- **Cause**: The Rule has been saved but not activated, or changes have not been published.  
- **Fix**: Check the Rule’s status. Ensure it is active and published.  

---

### 7. Running Rules on the Wrong Dataset
- **Symptom**: Rule tests fine on samples but doesn’t work in production.  
- **Cause**: Rule is only applied on a test dataset or hasn’t been re-run on historical records.  
- **Fix**: Re-run the Rule on the correct dataset and confirm scope matches production data.  

---

## How to Troubleshoot Non-Working Rules

1. **Check Rule Execution Logs**  
   - Navigate to **Rules > Execution History**.  
   - Verify if the Rule ran, how many records matched, and whether any errors occurred.  

2. **Test on Sample Data**  
   - Run the Rule against a small test dataset.  
   - Confirm that the expected outcome occurs on a controlled set of records.  

3. **Validate Conditions Against Real Data**  
   - Inspect a few sample records directly in **Entity Explorer**.  
   - Confirm they satisfy the Rule conditions.  

4. **Review Dependencies**  
   - Check if other Rules, enrichments, or transformations might be interfering.  

5. **Simplify the Rule**  
   - Temporarily remove complex conditions.  
   - Reintroduce them one by one until the failure point is found.  

---

## Best Practices to Avoid Rule Misbehavior

- **Be Precise with Conditions**: Use clear logic that matches real data values.  
- **Use Standardized Data**: Normalize data (e.g., country codes, phone formats) before applying Rules.  
- **Keep Rules Modular**: Use smaller, focused Rules instead of one overly complex Rule.  
- **Document Each Rule**: Add descriptions so others understand what it is intended to do.  
- **Test in Staging First**: Validate new Rules on non-production data before applying broadly.  
- **Monitor Execution**: Regularly review Rule logs and dashboards for anomalies.  

---

## Summary

When Rules don’t work as expected in CluedIn, it is usually due to issues with scope, conditions, actions, or execution order. By systematically troubleshooting these areas and following best practices, you can ensure your Rules deliver consistent, predictable results.  

If you have confirmed your configuration is correct but Rules still fail to execute properly, contact CluedIn Support with execution logs and example records for further investigation.  

---

