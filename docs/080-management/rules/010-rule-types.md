---
layout: cluedin
nav_order: 1
parent: Rules
grand_parent: Management
permalink: management/rules/rule-types
title: Rule types
tags: ["management", "rules"]
last_modified: 2023-11-16
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

There are three types of rules: data part rules, survivorship rules, and golden record rules. Each rule serves a distinct purpose in managing and optimizing your golden records. The following diagram shows the order in which the rules should be applied to the records in CluedIn.

![rule-types-1.png]({{ "/assets/images/management/rules/rule-types-1.png" | relative_url }})

## Data parts rules

The purpose of **data parts rules** is to modify the values in records that come from different sources. Data part rules are mostly used for normalization and transformation of values on the vocabulary key level. While you have the option to create data part rules manually, they can also be generated automatically from a [clean project](/preparation/clean).

The following video explains variuos actions available in the data part rules.

<div class="videoFrame">
<iframe src="https://player.vimeo.com/video/982424576?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write" title="Data part rules"></iframe>
</div>

## Survivorship rules

The purpose of **survivorship rules** is to determine which value contributes to the golden record among many potential values. By default, the latest value coming to CluedIn is the value used in the golden record. If you want to use another value for your golden record, you can set up a survivorship rule with the needed [action](/management/rules/rules-reference).

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

## Example of using rules

Let's take a look at the example of using different rule types in the lifecycle of a golden record in CluedIn. Suppose you are receiving data about a company from various systems such as Salesforce, SAP, and MS SQL Server. Among other properties, the records from these systems include the countryCode property, which is used in the company golden record. However, the countryCode property contains inconsistent values—some country codes are in lower case and others in title case. To normalize these values, you can create a data part rule.

![rule-types-2.png]({{ "/assets/images/management/rules/rule-types-2.png" | relative_url }})

After normalizing the values, it turns out that records from different systems contributing to a single golden record contain different countryCode values. To make an informed decision over which value should be used in the golden record, you can create a survivorship rule. For example, the records coming from Salesforce and SAP have the countryCode property set to 'DK', while the records coming from MS SQL Server have the countryCode property set to 'FI'. The survivorship rule's action can select the winning value based on criteria such as the latest modified value, the record with the most properties, or a preference for a specific provider. In this case, the rule's action identifies the most frequent value and applies it to the golden record (the chosen value is 'DK').

![rule-types-3.png]({{ "/assets/images/management/rules/rule-types-3.png" | relative_url }})

To make it easier to find a golden record, you can add tag to it. As an example, let's add a tag "Nordic" to the golden record with the countryCode property set to 'DK'. This simplifies the process of locating the tagged record and adding it to the clean project, glossary, or stream.

![rule-types-4.png]({{ "/assets/images/management/rules/rule-types-4.png" | relative_url }})
