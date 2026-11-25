---
layout: cluedin
title: Rule types
parent: Rules
grand_parent: Govern & improve
nav_order: 10
permalink: /govern/rules/rule-types
content_type: reference
redirect_from: ["/management/rules/rule-types"]
source_path: docs/080-management/rules/010-rule-types.md
tags: ["management", "rules"]
last_modified: 2026-10-28
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

There are four types of rules: data part rules, survivorship rules, golden record rules, and data profile rules. Each rule serves a distinct purpose in managing and optimizing your golden records. The following diagram shows the order in which the first three rule types should be applied to the records in CluedIn. Data profile rules are run on demand or on a schedule against existing records, independently of this pipeline.

![Diagram: data part rules apply to records, then survivorship rules apply to processed records, then golden record rules apply to golden records]({{ "/assets/images/management/rules/rule-types-1.png" | relative_url }})

## Data parts rules

The purpose of **data parts rules** is to modify the values in records that come from different sources. Data part rules are mostly used for normalization and transformation of values on the vocabulary key level. While you have the option to create data part rules manually, they can also be generated automatically from a [clean project](/govern/cleaning).

The following video explains variuos actions available in the data part rules.

<div class="videoFrame">
<iframe src="https://player.vimeo.com/video/982424576?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write" title="Data part rules"></iframe>
</div>

## Survivorship rules

The purpose of **survivorship rules** is to determine which value contributes to the golden record among many potential values. By default, the latest value coming to CluedIn is the value used in the golden record. If you want to use another value for your golden record, you can set up a survivorship rule with the needed [action](/govern/rules/rules-reference).

The following video explains each action available in the survivorship rules.

<div class="videoFrame">
<iframe src="https://player.vimeo.com/video/923699241?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write" title="Survivorship rules"></iframe>
</div>

## Golden record rules

The purpose of **golden record rules** is to facilitate the easy identification and retrieval of golden records within the system. You can use a golden record rule to tag records containing invalid data that should be addressed by a Data Steward. In this case, a responsible person can quickly find tagged records and create a clean project.

The following video explains each action available in the golden record rules.

<div class="videoFrame">
<iframe src="https://player.vimeo.com/video/995011124?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write" title="Golden record rules"></iframe>
</div>

## Data profile rules

The purpose of **data profile rules** is to validate the structure and statistical quality of the records of an entity type, rather than the value of a single record. Use a data profile rule to check things like how many records or columns an entity type has, whether a column is complete or unique enough, how two columns correlate, or how fresh the data is.

Unlike data part, survivorship, and golden record rules, a data profile rule is not applied automatically as records are processed. Instead, it is evaluated either on demand - by selecting Run on the rule - or automatically, on a recurring schedule, for every active rule in the organization. Either way, it returns a pass or fail result together with the computed value it was evaluated against. See [rules reference](/govern/rules/rules-reference#metrics-in-data-profile-rules) for the full list of available metrics.

Every run is kept, whether triggered manually or by the schedule, so the rule's detail page shows a chart of its computed value and pass/fail status over time - useful for seeing whether a metric is trending in the right direction, not just whether its most recent run passed.

## Example of using rules

Let's take a look at the example of using different rule types in the lifecycle of a golden record in CluedIn. Suppose you are receiving data about a company from various systems such as Salesforce, SAP, and MS SQL Server. Among other properties, the records from these systems include the countryCode property, which is used in the company golden record. However, the countryCode property contains inconsistent values—some country codes are in lower case and others in title case. To normalize these values, you can create a data part rule.

![Diagram: Company 1 records from Salesforce, SAP and MS SQL Server with countryCode values Dk, DK and fi pass through a data part rule with action To Upper Case, producing DK, DK and FI]({{ "/assets/images/management/rules/rule-types-2.png" | relative_url }})

After normalizing the values, it turns out that records from different systems contributing to a single golden record contain different countryCode values. To make an informed decision over which value should be used in the golden record, you can create a survivorship rule. For example, the records coming from Salesforce and SAP have the countryCode property set to 'DK', while the records coming from MS SQL Server have the countryCode property set to 'FI'. The survivorship rule's action can select the winning value based on criteria such as the latest modified value, the record with the most properties, or a preference for a specific provider. In this case, the rule's action identifies the most frequent value and applies it to the golden record (the chosen value is 'DK').

![Diagram: Company 1 records with countryCode DK, DK and FI pass through a survivorship rule with action Most Frequent Value Wins, producing a golden record Company 1 with countryCode DK]({{ "/assets/images/management/rules/rule-types-3.png" | relative_url }})

To make it easier to find a golden record, you can add tag to it. As an example, let's add a tag "Nordic" to the golden record with the countryCode property set to 'DK'. This simplifies the process of locating the tagged record and adding it to the clean project, glossary, or stream.

![Diagram: golden record Company 1 with countryCode DK passes through a golden record rule with action Add Tag Nordic, resulting in Company 1 tagged Nordic]({{ "/assets/images/management/rules/rule-types-4.png" | relative_url }})
