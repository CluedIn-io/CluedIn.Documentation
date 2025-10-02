---
layout: cluedin
nav_order: 3
parent: Golden records
grand_parent: Key terms and features
permalink: /key-terms-and-features/golden-records/explain-log
title: Explain Log
last_modified: 2025-05-20
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article, you will learn how to use the Explain Log to track the sequence of processing steps and rules that shape a golden record. This will help you understand why a golden record appears in its current state.

## Overview

The Explain Log is a diagnostic and traceability tool that provides visibility into how data is transformed and processed with respect to golden records and their constituent records. This feature allows you to understand **why** a golden record appears in its current state and **how** the platform derived the final output values that you see. The Explain Log was designed to make making processing steps transparent, traceable, and understandable. Specifically, the Explain Log:

- **Shows processing activities** applied to a golden record and its constituent records.
    
- **Identifies business rules** that are applied to a golden record and its constituent records.

- **Shows the origin of each value** in a golden record, answering the question where a specific value came from.
    
- **Provides visibility into complex processing logic**, helping you understand what is happening under the hood.
    
- **Details the execution order** of processing steps and data transformations.
    
- **Displays transformations** that values undergo throughout the processing pipeline.

## Structure of the Explain Log

The Explain Log consists of two main sections that represent logical processing steps:

- **Golden Record** – top-level section that contains decisions made on value selection and rule application.

- **Records** – a section that tracks how each constituent record (also known as data part) contributed to the golden record. This section can contain multiple records.

![explain-log-sections.png]({{ "/assets/images/key-terms-and-features/explain-log-sections.png" | relative_url }})

Both sections consist of many elements that represent various operations, which happened within a logical processing step. The operation is a small and logical computation and typically has a single responsibility. Each operation consists of following information:

1. **Operation name** – name of the operation in the processing pipeline.

1. **Status** – indicates the outcome of the operation. The possible statuses include:

    - **Successful** – the operation executed and completed without errors. This status reflects the execution of the operation, not whether it resulted in any changes. An operation may be marked as successful even if no changes were applied—for example, when the input did not require modification.

    - **Successful with warnings** – the operation was executed but encountered non-critical issues.

    - **Skipped** - the operation was not executed due to specified reason.

    - **Failed** - the operation encountered a critical error and did not complete successfully.

2. **Duration** – the time taken by the operation to execute within the processing pipeline.

3. **Summaries** – a tabular representation of actions made by the operation. This summary is derived from events and operations recorded during execution and provides a concise and user-friendly visual overview of outcomes.

4. **Events and Operations** – a detailed breakdown of actions made by the operation. These are the primary source of insight into what the operation actually did. Events and operations are also reflected in the summary table for easier interpretation.

    Note that the information in **Summaries** and **Events and Operations** is generally the same; the difference lies in how it is visually presented. In most cases, there is a one-to-one correspondence between the two sections. However, in less common cases, some events and operations may not be included in summaries.

    ![explain-log-operation.png]({{ "/assets/images/key-terms-and-features/explain-log-operation.png" | relative_url }})

If an operation does not contain **Summaries** and **Events and Operations**, it means that no changes were applied during its execution.
   
## How to read the Explain Log

This section helps you interpret the Explain Log by focusing on two key aspects: understanding where golden record values come from and identifying rules applied to a golden record.

**Understanding where golden record values come from**

To see which values are used in the golden record, review the **Merge data parts** operation in the **Golden Record** section. The **Summaries** table within this operation shows each property value along with the ID of the record from which it originated. Once you identify the record ID, you can further investigate the operations that were applied to that specific record throughout the processing pipeline.

![explain-log-merge-data-parts.png]({{ "/assets/images/key-terms-and-features/explain-log-merge-data-parts.png" | relative_url }})

**Identifying rules applied to a golden record**

To determine which rules have been applied to a golden record, refer to the **Evaluate rules** operations in the **Golden Record** section. You may notice that this section contains two **Evaluate rules** operations:

- The **first Evaluate rules** operation is dedicated to **survivorship rules**.

- The **second Evaluate rules** operation is dedicated to **golden record rules**.

The structure of both operations in the Explain Log is the same. Let's consider an example of the **Summaries** section for golden record rules. It includes two tables:

- **Applied rules** – lists all golden record rules along with their actions that were successfully applied to the golden record as well as actions that were skipped or failed.
    
- **Evaluated rules** – lists all golden record rules along with their actions that exist in the system and indicates whether each rule was applied, partially applied, or skipped. If a rule was skipped, a reason is provided—for example, if the conditions defined in the rule’s action were not met.

    ![explain-log-evaluate-golden-record-rules.png]({{ "/assets/images/key-terms-and-features/explain-log-evaluate-golden-record-rules.png" | relative_url }})

Note that the **Golden Record** section provides information only about survivorship rules and golden record rules. It does not include information about data part rules.  To identify which **data part rules** have been applied to a constituent record, refer to the **Evaluate rules** operation in the **Records** section.

## Troubleshooting using the Explain Log

The Explain Log shows how a golden record would appear **if it were reprocessed right now**. This means the Explain Log reflects the current results of the processing pipeline—not necessarily the current state of the golden record itself. For example, if you modify a golden record rule but do not reprocess the affected golden record, the Explain Log will still show the updated rule logic, even though the golden record has not yet been updated accordingly.

**Recommendation:** To ensure consistency between the Explain Log and the actual state of the golden record, always reprocess the golden record before performing troubleshooting based on the Explain Log.