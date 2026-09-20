---
layout: cluedin
nav_order: 6
parent: Rules
grand_parent: Management
permalink: /management/rules/run-rules-in-spark
title: Run rules in Spark
tags: ["management", "rules"]
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

For large volumes of records, you can reprocess a rule using Apache Spark instead of the standard CluedIn processing pipeline. Spark is a distributed processing engine that spreads the work across a cluster, which makes it a better fit for reprocessing very large numbers of records.

{:.important}
Running in Spark produces the same result as standard reprocessing—the same rule conditions and actions apply to the same records. See [Manage rules](/management/rules/manage-rules#edit-a-rule) for the standard reprocessing flow.

## Before you start

Running in Spark is available only if your organization has the feature enabled. If you don't see the **Run in Spark** option described below, contact your CluedIn administrator.

## Reprocess a rule using Spark

**To reprocess a rule using Spark**

1. On the navigation pane, go to **Management** > **Rule builder**, and open the rule you want to reprocess.

1. Save your changes, and select the checkbox to reprocess the records affected by the rule.

1. In the confirmation dialog, turn on the **Run in Spark** toggle.

    If the toggle is disabled, your rule currently isn't supported in Spark. CluedIn lists the specific reasons underneath the toggle—see [Supported rules](#supported-rules) below for what to check.

1. Confirm your choice.

    Progress is shown the same way as standard reprocessing. Records are updated exactly as they would be from a standard run.

{:.important}
If the CluedIn server restarts while a Spark-based run is still in progress—for example, during scheduled maintenance—the run automatically picks up where it left off. You don't need to start it again.

## Supported rules

Most rules work the same way in Spark, including rules that use [Formula actions (Power Fx)](/management/rules/power-fx-formulas-in-rules).

**Conditions**

Rule conditions built from the standard comparison operators are supported—for example, Equals, Not equals, Contains, Begins with, Ends with, Greater than, Less than, Between, In, Is null, Exists, and Matches pattern (along with each operator's negated form). A Formula condition is supported as well, as long as it only reads data—a Formula condition that would modify a record isn't allowed, since a condition should never have side effects.

**Actions**

Most rule actions are supported, including value changes (Set Value, Add Value, Copy Value, Move Value, Delete Value), text transformations (To UpperCase, To LowerCase, To TitleCase, To CamelCase, Trim WhiteSpace), tagging and aliases (Add Tag, Remove Tag, Remove All Tags, Add Alias, Remove Alias), and Formula actions.

A small number of actions aren't supported yet, including actions that call CluedIn AI (Add Value with CluedIn AI, Set Value with CluedIn AI) and Normalize Date. A rule that uses an unsupported action or condition is reported as incompatible, with the specific rule and action named in the reason—it's never silently skipped or run with different behavior.

## Frequently asked

**Will my results be different?**

No. CluedIn only allows **Run in Spark** for rules it can run identically to standard reprocessing. If a rule can't be run this way, the toggle tells you why instead of giving you a different result.

**Is it always faster?**

For large volumes of records, yes—that's the point of using it. For smaller reprocessing jobs, the standard pipeline is already fast, and Spark's own startup time means it isn't worth choosing until you're reprocessing a genuinely large number of records.
