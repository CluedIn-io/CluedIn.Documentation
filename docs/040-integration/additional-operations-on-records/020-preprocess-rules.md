---
layout: cluedin
nav_order: 2
parent: Additional operations
grand_parent: Ingestion
permalink: {{ site.baseurl }}/integration/additional-operations-on-records/preprocess-rules
title: Pre-process rules
tags: ["integration", "pre-process rules"]
last_modified: 2024-01-15
---

Pre-process rules are applied to the records that are already mapped ([clues](/key-terms-and-features/clue-reference)). You can create pre-process rules when you want to add tags or aliases to the records or send the records to quarantine. The difference between [property rules](/integration/additional-operations-on-records/property-rules) and pre-process rules is that property rules are applied only to property values of the record while pre-process rules are applied to the whole record. So, if you want to apply some changes to multiple records, create a pre-process rule.

Pre-process rules are applied to the clues after the property rules have been already applied.

![pre-process-rules-diagram.png](../../assets/images/integration/additional-operations/pre-process-rules-diagram.png)

All pre-process rules are listed on the **Pre-process rules** tab of the data set.

**Prerequisites**

To access pre-process rules, go to **Administration** > **Feature Flags** and make sure that the following features are enabled:

- **Data Set Pre-Process Rules**

- **Data Set Quarantine**

**To create a pre-process rule**

1. On the navigation pane, go to **Integrations** > **Data Sources**. Then, find and open the data set.

1. Go to the **Pre-process rules** tab, and then select **Add pre-process rule**.

1. Enter the **Display name** of the rule.

1. In the **Filter** section, select whether you want to apply the rule to all records or to specific records.

1. If you want to apply the rule to specific records:

    1. Select a condition to determine which records will be affected by the rule.

    1. Depending on what you selected in the previous step, specify the entity property or the vocabulary key that will be affected by the rule.

    1. Select whether you want to apply the rule when the condition is met or when the condition is not met.

        The following screenshot demonstrates that all records that do not contain the job title will be sent to the quarantine.

        ![pre-process-rules-1.png](../../assets/images/integration/additional-operations/pre-process-rules-1.png)

        {:.important}
        You can add only one filter to the rule. For example, if you want to quarantine all records that, in addition to the job title, do not contain the email address and the phone number, you need to create separate rules for each vocabulary key.

    1. Select the **Action** that will be applied to the records.

1. In the lower-right corner, select **Add rule**.

    The rule is added to the table on the **Pre-process rules** tab. You can edit or delete the rule, if needed. The rule will be applied after you process the records.