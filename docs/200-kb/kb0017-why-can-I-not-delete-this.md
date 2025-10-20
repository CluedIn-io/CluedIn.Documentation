---
layout: cluedin
title: Why can I not delete certain objects in CluedIn
parent: Knowledge base
permalink: /kb/unable-to-delete
tags: ["Delete", "Known Issue"]
nav_order: 17
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

CluedIn provides extensive capabilities for creating, managing, and governing master data assets. However, there are certain object types that **cannot currently be deleted once created**. These are known product limitations and are on the roadmap for improvement.

This article outlines what those objects are, why deletion is not yet supported, and recommended workarounds or best practices.

---

## Objects That Cannot Be Deleted

### 1. Business Domains
- **Description**: Business Domains define the logical areas of your data model (e.g., Customer, Product, Supplier).
- **Issue**: Once created, Business Domains cannot be deleted.  
- **Impact**: Unused domains remain visible in the portal.  
- **Workaround**: Mark unused domains as *Inactive* or rename them with a prefix (e.g., `ZZ_Obsolete`) to indicate they are not in use.

---

### 2. Vocabularies
- **Description**: Vocabularies are controlled lists of business terms and definitions used across CluedIn.  
- **Issue**: Vocabularies cannot be deleted.  
- **Impact**: Test or unused vocabularies can clutter the governance layer.  
- **Workaround**: Mark them as *Deprecated* or rename with an `ARCHIVE_` prefix.

---

### 3. Vocabulary Keys
- **Description**: Keys represent individual entries within a Vocabulary.  
- **Issue**: Vocabulary Keys cannot be removed once added.  
- **Impact**: Erroneous or outdated keys persist in dropdowns and rules.  
- **Workaround**: Use tagging or mark keys as *Inactive/Obsolete* and provide clear descriptions that they should not be used.

---

### 4. Roles
- **Description**: Roles control user permissions and responsibilities (e.g., Steward, Analyst, Administrator).  
- **Issue**: Roles cannot be deleted once created.  
- **Impact**: Experimental or obsolete roles remain in the UI.  
- **Workaround**: Remove all user assignments from unused roles and rename them with an archival prefix.

---

### 5. Golden Record Layouts
- **Description**: Layouts define how Golden Record data is displayed in the portal.  
- **Issue**: Layouts cannot be deleted once created.  
- **Impact**: Testing and experimentation can create clutter.  
- **Workaround**: Rename layouts with an `ARCHIVE_` prefix or move them into a separate grouping for clarity.

---

### 6. Deduplication Projects
- **Description**: Deduplication Projects configure and test matching rules for resolving duplicate records.  
- **Issue**: Deduplication Projects cannot be deleted.  
- **Impact**: Old experiments or tests stay visible in the list.  
- **Workaround**: Use descriptive naming (e.g., `Test_Project_DO_NOT_USE`) or archive notes to separate them from active projects.

---

### 7. Cleaning Projects
- **Description**: Cleaning Projects are used to standardize and fix bulk data issues.  
- **Issue**: Cleaning Projects cannot be deleted.  
- **Impact**: Completed or test cleaning jobs remain in the history.  
- **Workaround**: Clearly label completed or obsolete projects; they remain valuable for audit and rollback purposes.

---

## Why Deletion Is Restricted

These limitations are primarily due to **auditability, lineage, and rollback guarantees**:
- CluedIn ensures a full historical view of governance objects and transformations.
- Removing these objects would create gaps in **audit trails** and **lineage history**.
- Certain items (like Cleaning Projects) support **undo/rollback**, which depends on retaining the original record.

---

## Best Practices

- **Adopt a naming convention**: Prefix unused or test objects with `ZZ_`, `ARCHIVE_`, or `DO_NOT_USE`.  
- **Document clearly**: Add notes in descriptions indicating the status of the object.  
- **Limit testing clutter**: Use a non-production environment (sandbox) for experimenting with Business Domains, Deduplication, or Cleaning Projects.  
- **Govern creation**: Restrict who can create these objects to reduce the number of unused items.

---

## Roadmap Note

Deletion support for these object types is a **known product limitation**. The CluedIn team is tracking this and working toward improvements to better support **archival and lifecycle management** of governance objects.

---

## Summary

Currently, the following objects cannot be deleted in CluedIn:
- Business Domains  
- Vocabularies  
- Vocabulary Keys  
- Roles  
- Golden Record Layouts  
- Deduplication Projects  
- Cleaning Projects  

Until deletion support is available, use **naming conventions, documentation, and governance controls** to manage unused items effectively.


