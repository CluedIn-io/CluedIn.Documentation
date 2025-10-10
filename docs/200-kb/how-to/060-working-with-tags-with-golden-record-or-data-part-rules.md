---
layout: cluedin
title: Working with tags on golden records and data parts
parent: Knowledge base
permalink: /kb/how-to-use-tags-with-golden-records-and-data-parts
nav_order: 2
---

## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

Tags in CluedIn allow you to add metadata labels to records that can drive automation, filtering, and reporting. When used together with **Golden Record Rules** and **Data Part Rules**, tags become a powerful way to classify, prioritize, and enrich your data lifecycle.

---

## What Are Tags?

- **Tags are labels** you can attach to entities, golden records, or data parts.  
- They provide **contextual information** (e.g., `VIP Customer`, `DoNotContact`, `HighRisk`).  
- Tags can be **added automatically** by Rules or **manually** by data stewards.  
- Tags are **non-destructive** – they don’t overwrite existing values but enrich records with extra classification.

---

## Why Use Tags with Rules?

- **Golden Record Rules**:  
  Apply tags to identify or categorize the final, trusted version of a record. Example: Mark customers who pass validation as `Verified`.  

- **Data Part Rules**:  
  Apply tags at the data part (source record) level to flag issues or classify records before they are merged. Example: Tag data from a specific system as `LegacySource`.  

Benefits:  
- Drive workflow automation (e.g., escalate tagged entities to specific teams).  
- Improve search and filtering in the CluedIn portal.  
- Support compliance and governance (e.g., tag PII records).  
- Provide visibility into how records are sourced and resolved.

---

## How to Work with Tags in Golden Record Rules

### Step 1: Navigate to Rules
1. Log in to the **CluedIn Portal**.  
2. Go to **Governance > Rules**.  
3. Choose **Golden Record Rules**.  

### Step 2: Create or Edit a Rule
- Click **New Rule** or select an existing Golden Record Rule to edit.  

### Step 3: Define Conditions
- Configure the conditions that determine when a record should be tagged.  
- Example: *If `Customer.Spend > 10000`, then apply tag `HighValue`.*  

### Step 4: Add Tag Action
- In the **Actions** section, choose **Add Tag**.  
- Enter one or more tags to apply (e.g., `VIP`, `PrioritySupport`).  

### Step 5: Save & Activate
- Save the Rule and publish it.  
- Once active, matching golden records will automatically be tagged.  

---

## How to Work with Tags in Data Part Rules

### Step 1: Navigate to Rules
1. In the **CluedIn Portal**, go to **Governance > Rules**.  
2. Choose **Data Part Rules**.  

### Step 2: Create or Edit a Rule
- Click **New Rule** or edit an existing Data Part Rule.  

### Step 3: Define Conditions
- Set up conditions to identify specific source records.  
- Example: *If `SourceSystem = LegacyCRM`, then apply tag `LegacySource`.*  

### Step 4: Add Tag Action
- In the **Actions** section, choose **Add Tag**.  
- Apply tags such as `NeedsValidation`, `LowConfidence`, or `HighRisk`.  

### Step 5: Save & Activate
- Save and publish the Rule.  
- Tags will now apply to data parts that meet your conditions.  

---

## Best Practices for Using Tags

- **Use Clear Naming Conventions**: Keep tag names short, consistent, and meaningful (e.g., `HighValueCustomer`, not `customer_high_value_flag`).  
- **Automate Where Possible**: Use Rules to apply tags automatically rather than relying on manual tagging.  
- **Leverage Tags in Search & Filters**: Use the portal’s search filters to find records with specific tags.  
- **Combine with Workflows**: Route tagged records into downstream workflows (e.g., send `DoNotContact` to marketing suppression lists).  
- **Audit Regularly**: Review tag usage periodically to ensure consistency and remove obsolete tags.  

---

## Common Use Cases

- Tagging **VIP customers** in Golden Record Rules for reporting.  
- Flagging **low-confidence data parts** for stewardship review.  
- Marking **legacy system records** during migration projects.  
- Adding compliance-related tags like `ContainsPII`.  
- Tagging products as `Discontinued` for downstream systems.  

---

## Summary

Tags in CluedIn provide an effective way to enrich, classify, and control data across Golden Records and Data Parts. By combining Tags with Rules, you can ensure that important metadata is applied consistently, driving better governance, compliance, and automation.
