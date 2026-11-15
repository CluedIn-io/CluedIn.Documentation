---
layout: cluedin
title: Data profile rules
parent: Rules
grand_parent: Govern & improve
nav_order: 100
permalink: /govern/rules/data-profile-rules
content_type: how-to
tags: ["management", "rules"]
last_modified: 2026-11-15
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

Data profile rules validate the structure and statistical quality of an entity type's records - row and column counts, completeness, uniqueness, distribution, freshness, and schema match - independently of the data part, survivorship, and golden record rules described in [rule types](/govern/rules/rule-types). Use a data profile rule when you want to be alerted that a data set no longer meets a quality bar, rather than to transform or tag individual records.

## Prerequisites

- The `management.rulebuilder` permission to view or edit data profile rules.
- The vocabulary key you want to check must already be used by at least one ingested record, since the column picker only lists vocabulary keys with data.

## Create a data profile rule

1. On the navigation pane, go to **Management** > **Data Profile Rules**.

1. Select **Create data profile rule**.

1. In **Entity type**, select the entity type whose records this rule validates, for example `/Organization`.

1. In **Metric**, choose what to measure - row count, column count, duplicate row count, completeness, uniqueness, column correlation, distinct values, and more.

1. If the metric needs one or two columns, select them in **Column**. Start typing to search the organization's vocabulary keys.

    **Is complete** and **Is unique** are evaluated as a true/false check for each record, so there is nothing further to configure - the **Condition** step explains this instead of asking for an operator and threshold.

    ![The Condition step for the Is unique metric, showing an explanation that the metric is true or false for each record instead of operator and threshold fields]({{ "/assets/images/management/rules/data-profile-rules/boolean-metric-condition.png" | relative_url }})

    Every other metric needs an **Operator** (for example greater than, between) and a **Threshold** the computed value is compared against.

1. In **Name**, enter a name for the rule, and optionally a **Description**.

1. Select **Create data profile rule**.

The rule evaluates on the organization's configured data profiling automation schedule. Select **Run** on the rule's own page, or **Run all** from the list, to evaluate it immediately instead of waiting for the schedule.

## Configure alerts

By default, a data profile rule notifies organization admins the first time it starts failing, and again if it recovers. To keep being reminded for as long as a rule stays unresolved:

1. On the **Data Profile Rules** list, select **Alerts**.

1. Next to the rule, select **Keep reminding me while it keeps failing**, and set how often, in minutes, to repeat the reminder.

    ![The Data profile rule alerts panel with Keep reminding me while it keeps failing enabled, a 60-minute interval, and the rule shown as Currently failing]({{ "/assets/images/management/rules/data-profile-rules/alerts-panel.png" | relative_url }})

A rule currently failing its condition shows **Currently failing** next to its name in this panel.

## Organize rules into folders

Data profile rules support folders the same way described for other rule types in [organize rules into folders](/govern/rules/manage-rules#organize-rules-into-folders):

- From the list, open a rule's action menu and select **Move to folder** to assign it to an existing folder or type a new folder name to create one.
- Folders and rules appear together in the same list; select a folder's chevron to expand it.
- Rename a folder from its own action menu.

![The Data Profile Rules list with a Demo Folder row showing a rule count]({{ "/assets/images/management/rules/data-profile-rules/folder-grouped-list.png" | relative_url }})

## Verify the result

After running a rule, its **Run history** shows whether the most recent run passed, the computed value, and a chart of past runs. The rule's own page shows an **Active**/**Inactive** badge and, when relevant, the **Currently failing** status also surfaced in the Alerts panel.

## What this changes

Running or evaluating a data profile rule only reads data and records the result - it does not change, tag, or reprocess any records. Enabling **Keep reminding me while it keeps failing** only affects whether and how often admins are notified; it does not change the rule's own pass/fail condition.

## If something goes wrong

If the column picker shows no results, the vocabulary key you are looking for has not been used by any ingested record yet - ingest at least one record with that value first, then try again.
