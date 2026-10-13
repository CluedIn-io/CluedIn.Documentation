---
title: Rule types
url: https://documentation.cluedin.net/govern/rules/rule-types
content_type: reference
section: Govern & improve > Rules
---

# Rule types

> reference: Facts, options, APIs.

There are three types of rules: data part rules, survivorship rules, and golden record rules. Each rule serves a distinct purpose in managing and optimizing your golden records. The following diagram shows the order in which the rules should be applied to the records in CluedIn.

![Diagram: data part rules apply to records, then survivorship rules apply to processed records, then golden record rules apply to golden records](https://documentation.cluedin.net/assets/images/management/rules/rule-types-1.png)

## Data parts rules

The purpose of **data parts rules** is to modify the values in records that come from different sources. Data part rules are mostly used for normalization and transformation of values on the vocabulary key level. While you have the option to create data part rules manually, they can also be generated automatically from a [clean project](https://documentation.cluedin.net/govern/cleaning.md).

The following video explains variuos actions available in the data part rules.

## Survivorship rules

The purpose of **survivorship rules** is to determine which value contributes to the golden record among many potential values. By default, the latest value coming to CluedIn is the value used in the golden record. If you want to use another value for your golden record, you can set up a survivorship rule with the needed [action](https://documentation.cluedin.net/govern/rules/rules-reference.md).

The following video explains each action available in the survivorship rules.

## Golden record rules

The purpose of **golden record rules** is to facilitate the easy identification and retrieval of golden records within the system. You can use a golden record rule to tag records containing invalid data that should be addressed by a Data Steward. In this case, a responsible person can quickly find tagged records and create a clean project.

The following video explains each action available in the golden record rules.

## Example of using rules

Let's take a look at the example of using different rule types in the lifecycle of a golden record in CluedIn. Suppose you are receiving data about a company from various systems such as Salesforce, SAP, and MS SQL Server. Among other properties, the records from these systems include the countryCode property, which is used in the company golden record. However, the countryCode property contains inconsistent values—some country codes are in lower case and others in title case. To normalize these values, you can create a data part rule.

![Diagram: Company 1 records from Salesforce, SAP and MS SQL Server with countryCode values Dk, DK and fi pass through a data part rule with action To Upper Case, producing DK, DK and FI](https://documentation.cluedin.net/assets/images/management/rules/rule-types-2.png)

After normalizing the values, it turns out that records from different systems contributing to a single golden record contain different countryCode values. To make an informed decision over which value should be used in the golden record, you can create a survivorship rule. For example, the records coming from Salesforce and SAP have the countryCode property set to 'DK', while the records coming from MS SQL Server have the countryCode property set to 'FI'. The survivorship rule's action can select the winning value based on criteria such as the latest modified value, the record with the most properties, or a preference for a specific provider. In this case, the rule's action identifies the most frequent value and applies it to the golden record (the chosen value is 'DK').

![Diagram: Company 1 records with countryCode DK, DK and FI pass through a survivorship rule with action Most Frequent Value Wins, producing a golden record Company 1 with countryCode DK](https://documentation.cluedin.net/assets/images/management/rules/rule-types-3.png)

To make it easier to find a golden record, you can add tag to it. As an example, let's add a tag "Nordic" to the golden record with the countryCode property set to 'DK'. This simplifies the process of locating the tagged record and adding it to the clean project, glossary, or stream.

![Diagram: golden record Company 1 with countryCode DK passes through a golden record rule with action Add Tag Nordic, resulting in Company 1 tagged Nordic](https://documentation.cluedin.net/assets/images/management/rules/rule-types-4.png)

Up: [Rules](https://documentation.cluedin.net/govern/rules.md)
