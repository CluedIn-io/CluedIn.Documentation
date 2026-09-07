---
layout: cluedin
title: Use tags with rules
parent: Tags
grand_parent: Govern & improve
nav_order: 20
permalink: /govern/tags/use-tags-with-rules
content_type: how-to
redirect_from: ["/kb/how-to-use-tags-with-golden-records-and-data-parts"]
source_path: docs/200-kb/how-to/060-working-with-tags-with-golden-record-or-data-part-rules.md
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

Tags in CluedIn allow you to add metadata labels to records that can drive automation, filtering, and reporting. When used together with [golden record rules](/govern/rules/rule-types#golden-record-rules) and [data part rules](/govern/rules/rule-types#data-parts-rules), tags become a powerful way to classify, prioritize, and enrich your data lifecycle.

---

## What are tags?

- **Tags are labels** you can attach to [golden records](/get-started/core-concepts/golden-records) or [data parts](/get-started/core-concepts/data-life-cycle).  
- They provide **contextual information** (e.g., `VIP Customer`, `DoNotContact`, or `HighRisk`).  
- Tags can be **added automatically** by [rules](/govern/rules) or **manually** by Data Stewards.  
- Tags are **non-destructive** – they don’t overwrite existing values but enrich records with extra classification.

---

## Why use tags with rules?

- **Golden record rules**: Apply tags to identify or categorize the final, trusted version of a record. Example: Mark customers who pass validation as `Verified`.  
- **Data part rules**: Apply tags at the data part (source record) level to flag issues or classify records before they are merged. Example: Tag data from a specific system as `LegacySource`.  

Benefits:  
- Drive workflow automation (e.g., escalate tagged entities to specific teams).  
- Improve [search](/master/search) and [filtering](/master/filters) in CluedIn.  
- Support compliance and governance (e.g., tag PII records).  
- Provide visibility into how records are sourced and resolved.

---

## How to work with tags in golden record rules

### Step 1: Navigate to rules
1. Sign in to CluedIn.  
2. Go to **Management** > **Rule Builder**.  
3. Choose **Golden Record Rules**.  

### Step 2: Create or edit a rule
- Click **New Rule** or select an existing golden record rule to edit.  

### Step 3: Define conditions
- Configure the conditions that determine when a record should be tagged.  
- Example: If `Customer.Spend > 10000`, then apply tag `HighValue`.  

### Step 4: Add tag action
- In the **Actions** section, choose **Add Tag**.  
- Enter one or more tags to apply (e.g., `VIP`, `PrioritySupport`).  

### Step 5: Save & activate the rule
- Save the rule and publish it.  
- Once active, matching golden records will automatically be tagged.  

---

## How to work with tags in data part rules

### Step 1: Navigate to rules
1. Sign in to CluedIn.  
1. Go to **Management** > **Rule Builder**.   
1. Choose **Data Part Rules**.  

### Step 2: Create or edit a rule
- Click **New Rule** or edit an existing data part rule.  

### Step 3: Define conditions
- Set up conditions to identify specific source records.  
- Example: If `SourceSystem = LegacyCRM`, then apply tag `LegacySource`. 

### Step 4: Add tag action
- In the **Actions** section, choose **Add Tag**.  
- Apply tags such as `NeedsValidation`, `LowConfidence`, or `HighRisk`.  

### Step 5: Save & activate the rule
- Save and publish the rule.  
- Tags will now apply to data parts that meet your conditions.  

---

## Best practices for using tags

- **Use clear naming conventions**: Keep tag names short, consistent, and meaningful (e.g., `HighValueCustomer`, not `customer_high_value_flag`).  
- **Automate where possible**: Use rules to apply tags automatically rather than relying on manual tagging.  
- **Leverage tags in search and filters**: Use the portal’s search filters to find records with specific tags.  
- **Combine with workflows**: Route tagged records into downstream workflows (e.g., send `DoNotContact` to marketing suppression lists).  
- **Audit regularly**: Review tag usage periodically to ensure consistency and remove obsolete tags.  

---

## Common use cases

- Tagging **VIP customers** in golden record rules for reporting.  
- Flagging **low-confidence data parts** for stewardship review.  
- Marking **legacy system records** during migration projects.  
- Adding compliance-related tags like `ContainsPII`.  
- Tagging products as `Discontinued` for downstream systems.  

---

## Summary

Tags in CluedIn provide an effective way to enrich, classify, and control data across golden records and data parts. By combining tags with rules, you can ensure that important metadata is applied consistently, driving better governance, compliance, and automation.  
