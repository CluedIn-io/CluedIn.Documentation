---
layout: cluedin
title: How to roll back or undo changes
parent: Golden records
grand_parent: Master
nav_order: 60
permalink: /master/golden-records/how-to-rollback-or-undo
content_type: how-to
redirect_from: ["/kb/how-to-rollback-or-undo"]
source_path: docs/200-kb/how-to/070-undo-or-rollback-changes.md
---

## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

Mistakes happen — whether it’s applying a transformation you didn’t mean to, merging the wrong records, or running a cleaning project with unintended results. CluedIn provides several built-in features to **rollback or undo changes**, helping you recover quickly and maintain trust in your data.

---

## Why Rollback Matters

- **Data Governance**: Ensure that incorrect changes don’t become permanent.  
- **User Confidence**: Experiment safely, knowing that changes can be reversed.  
- **Audit & Compliance**: Maintain a clear history of what was changed and when.  

---

## Features That Support Rollback

### 1. Undo Changes to Data
- **Where**: Entity Explorer or Data Stewardship workspace.  
- **What It Does**:  
  - If you merge records incorrectly, you can unmerge them.  
  - If you update or overwrite a field manually, you can revert to the previous value.  
  - If enrichment or transformation introduces bad data, you can undo the applied changes.  
- **How to Use**:  
  1. Open the affected record in **Entity Explorer**.  
  2. Navigate to the **History** tab.  
  3. Select the change you want to reverse.  
  4. Click **Undo** or **Restore Previous Value**.  
- **Notes**:  
  - Undo actions are logged in the audit trail.  
  - Some automated transformations may re-apply on the next pipeline run, so check active Rules.  

---

### 2. Undo a Cleaning Project
- **Where**: Cleaning Projects workspace.  
- **What It Does**:  
  - Reverts the results of a data cleaning project if the changes were incorrect or incomplete.  
  - Removes tags, corrections, or transformations applied during the project.  
- **How to Use**:  
  1. Go to **Data Quality > Cleaning Projects**.  
  2. Open the completed project.  
  3. Click **Rollback / Undo Project**.  
  4. Confirm the rollback action.  
- **Notes**:  
  - Undoing a project restores the dataset to its pre-cleaning state.  
  - You can always re-run the project later with updated rules or corrections.  

---

### 3. Undo Record Merges (Golden Record Rollback)
- **Where**: Data Stewardship workspace.  
- **What It Does**:  
  - Unmerges records that were incorrectly consolidated into a Golden Record.  
- **How to Use**:  
  1. Navigate to the merged entity in **Entity Explorer**.  
  2. Open the **History** tab.  
  3. Select the merge event.  
  4. Click **Unmerge**.  
- **Notes**:  
  - The original source records are preserved, so unmerging restores them.  
  - Any downstream systems synced with the Golden Record will be updated after rollback.  

---

### 4. Audit Trail & Versioning
- **Where**: Entity Explorer → History.  
- **What It Does**:  
  - Lets you review all changes made to a record over time.  
  - Provides the option to revert specific attributes to previous values.  
- **Notes**:  
  - Every change is timestamped and attributed to the user or process that made it.  
  - This supports granular rollback (attribute-level undo) as well as record-level undo.  

---

### 5. Undo Manual or Bulk Record Edits (Global Audit Log)
- **Where**: Administer → Global Audit Log.  
- **What It Does**:  
  - Lists manual single-record edits (for example, editing a record's tags, aliases, description, display name, name, business domain, URI, external references or properties from its detail page) and bulk edits applied to many records at once (for example, adding a tag to every record on a page of search results) as individual, revertible entries.  
  - Reverting an entry restores the fields it changed on the affected record to their value before the edit.  
- **How to Use**:  
  1. Go to **Administer > Global Audit Log**.  
  2. Filter by object type to see record changes.  
  3. Select one or more revertible entries.  
  4. Click **Revert** (or **Revert since** a point in time, to revert every revertible entry from then on).  
- **Notes**:  
  - A record edit can only be reverted while it is still within the organization's audit log retention period, and only by a user with permission to edit that data.  
  - Reverting an entry is itself written to the Global Audit Log, including who reverted it, when, and which original entry it reverted.  
  - If the record was changed again since the entry you are reverting, reverting still applies — it sets the field back to its recorded previous value, which may overwrite that later change.  

---

## Limitations of Rollback
- Not all actions are reversible (e.g., permanent deletion of data after retention policy expiry).  
- Automated pipelines may re-apply transformations after rollback unless the underlying Rule or cleaning logic is adjusted.  
- Large rollbacks (e.g., undoing a massive cleaning project) may take time and resources to complete.  

---

## Best Practices for Safe Rollbacks
- **Preview Before Applying**: Use preview functionality in cleaning projects and rules to validate expected outcomes.  
- **Start Small**: Test rules and cleaning projects on subsets of data before applying at scale.  
- **Monitor Audit Logs**: Regularly review audit trails to catch unexpected changes early.  
- **Coordinate with Teams**: Inform downstream system owners if a rollback will affect synchronized data.  
- **Disable Problematic Rules**: If a rule caused incorrect changes, disable or adjust it before rolling back, to avoid reapplication.  

---

## Summary

CluedIn offers multiple ways to **undo or rollback changes**, including undoing data changes, unmerging Golden Records, reverting entire cleaning projects, and reverting manual or bulk record edits from the Global Audit Log. Combined with detailed audit trails and version history, these features give you confidence to manage your data safely — knowing that mistakes can be corrected without permanent damage.
