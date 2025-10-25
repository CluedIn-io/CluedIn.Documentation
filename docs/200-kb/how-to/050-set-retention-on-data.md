---
layout: cluedin
title: Set retention policies on data
parent: Knowledge base
permalink: /kb/set-retention
nav_order: 5
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

Retention policies define how long data is stored in CluedIn before it is automatically archived or deleted. They are essential for managing compliance requirements, controlling storage costs, and ensuring that outdated or irrelevant data does not clutter your environment.  

This article explains what retention policies are, why they matter, and how to configure them in CluedIn.

---

## What Are Retention Policies?

A **retention policy** specifies:
- **Which records** the policy applies to (e.g., Customers, Orders, Products).  
- **How long** the data should be retained.  
- **What action** to take when the retention period expires (archive, delete, or move to another system).  

Retention policies ensure that CluedIn automatically manages the lifecycle of your records in line with business and regulatory requirements.

---

## Why Retention Policies Matter

- **Regulatory Compliance**: Frameworks like GDPR and CCPA require organizations to only retain personal data for as long as it is needed.  
- **Data Governance**: Reduces clutter by removing outdated or irrelevant data.  
- **Cost Efficiency**: Helps manage storage costs by preventing unbounded data growth.  
- **Performance**: Keeping datasets lean improves ingestion, rule processing, and matching speeds.  

---

## How to Configure Retention Policies in CluedIn

### Step 1: Identify Applicable Entity Types
- Decide which entities should be subject to retention rules (e.g., `Customer`, `Order`, `LogEntry`).  
- Review regulatory requirements or internal governance guidelines for each entity type.  

### Step 2: Navigate to Retention Policy Settings
1. Log in to the **CluedIn Portal**.  
2. Go to **Governance > Retention Policies**.  
3. Click **Create Policy**.  

### Step 3: Define the Policy Scope
- Choose the **Entity Type** (e.g., Customers).  
- Select optional filters to refine scope (e.g., customers without activity in 5 years).  

### Step 4: Set Retention Duration
- Define the number of **days, months, or years** records should be retained.  
- Example: Retain inactive customer records for 7 years.  

### Step 5: Define the Action
- **Delete**: Permanently removes records and associated data.  
- **Archive**: Moves data into an archived state (still accessible but not active in workflows).  
- **Move**: Exports data to an external storage system before removal from CluedIn.  

### Step 6: Publish & Activate
- Save the retention policy.  
- Review the summary screen and activate the policy.  
- Policies will automatically apply to existing and new records within scope.  

---

## Best Practices for Retention Policies

- **Start with Non-Destructive Actions**: Use archiving before permanent deletion to reduce risk.  
- **Align with Legal Requirements**: Consult compliance and legal teams to set retention durations.  
- **Test on a Subset First**: Apply new policies to a limited dataset before rolling out broadly.  
- **Communicate Changes**: Inform stakeholders about data lifecycle policies to avoid surprises.  
- **Monitor Policy Impact**: Review retention reports to ensure policies are working as intended.  

---

## Common Issues and Troubleshooting

### Policy Not Applying
- **Cause**: Entity type or filters are misconfigured.  
- **Fix**: Double-check policy scope and filters.  

### Records Not Being Deleted
- **Cause**: Policy action is set to Archive instead of Delete.  
- **Fix**: Review action type in the policy definition.  

### Unexpected Data Removal
- **Cause**: Policy conditions too broad.  
- **Fix**: Narrow scope with additional filters (e.g., “inactive > 5 years”).  

---

## Summary

Retention policies in CluedIn allow you to automate record lifecycle management, ensuring compliance, efficiency, and improved system performance. By carefully scoping policies, aligning them with business/legal requirements, and monitoring their impact, you can maintain a clean and compliant data environment.  

---
