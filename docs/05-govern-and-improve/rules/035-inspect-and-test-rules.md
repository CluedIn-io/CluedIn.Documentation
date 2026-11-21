---
layout: cluedin
title: Inspect and test rules
parent: Rules
grand_parent: Govern & improve
nav_order: 35
permalink: /govern/rules/inspect-and-test-rules
content_type: how-to
tags: ["management", "rules"]
last_modified: 2026-11-21
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

Check what your rules do before they change real data: the **Rule Inspector** steps through rules against a sample record, and **rule unit tests** save examples you can re-run after every change. Neither changes any data.

The **How rules work** card on the **Rule builder** page (**Management** > **Rule builder**) summarizes the rule pipeline, [approval rules](/govern/rules/rule-types#approval-rules) and these tools.

![The How rules work card, with the approval rules, Rule Inspector and rule unit tests tools]({{ "/assets/images/management/rules/inspect-test-how-rules-work.png" | relative_url }})

## Prerequisites

- The **Rule Inspector, AI Formula Builder and Rule Tests** feature is turned on for your organization. If you don't see the Rule Inspector, ask an administrator to turn it on.
- Access to the Rule builder. Creating, editing and running unit tests needs the same access as editing the rule: you own the rule, or you have Accountable access to the Rule builder.

## Rule Inspector

The Rule Inspector runs rules against a record and shows, for each rule in processing order:

- **Why it did or did not match** – every condition, whether it matched, and the value it was evaluated against. A rule without conditions says that it matches every record.
- **Actions** – what each action did, including the fields it changed and any error.
- **Entity state** – every field before and after the rule ran.

Open it from **Rule builder** > **Rule Inspector** to step through data part, survivorship and golden record rules together, or from the **Inspector** tab of a rule to step through the rules of that rule's type. The Inspector never changes any data.

To run it:

1. Search for a record to load its current values, or select **Show manual fields** and enter field values by hand.
1. Select **Run**.
1. Use the timeline, the arrow buttons, or the ↑/↓ keys to step through the rules. Use **Only show active** and **Only show matched** to narrow the list.

Inactive rules are evaluated too, so you can see whether a rule would match and what it would change before you activate it. An inactive rule says so above its explanation.

### What the Inspector can check

Select **What the Inspector can check** on the Inspector to see this list in the product.

| Data | Supported | Details |
|---|---|---|
| Vocabulary keys and built-in fields | Yes | Enter a vocabulary key (for example, `customer.email`) or a built-in field (for example, `Name`, `DisplayName`, `EntityType`). |
| Lookup fields | Yes | A Lookup key holds the value users see, and the referenced record's entity code is kept in a companion `<key>-EntityCode` field. That field is what the **Is Valid Lookup** / **Is Invalid Lookup** operators check. A record you search for includes it. When you enter a value by hand, enter the entity code (for example, `/Country#Glossary:DK`) or a name followed by the code in curly brackets (for example, `Denmark {/Country#Glossary:DK}`). The Inspector does not search for the referenced record, so any other value is treated as *cannot find a match*. A note above the results explains how each Lookup field was read. |
| Edges | Edges that rules add | Edges added by the **Add Edge** action appear as `OutgoingEdges` and `IncomingEdges` in the entity state. A record's existing edges are not loaded, so conditions and formulas that read them (for example, `LoadOutgoingRelationships`) see none in the Inspector. |
| Survivorship rules | On a survivorship rule's Inspector tab | Survivorship rules choose a value by comparing the source records of a golden record, so they need [source records](#inspect-survivorship-rules). |

### Inspect survivorship rules

Survivorship rules decide which of a golden record's conflicting values wins, by comparing the records it was merged from. On the **Inspector** tab of a survivorship rule, you enter those source records instead of a single set of values:

1. For each source record, enter its source name (for example, *CRM*), when it was last modified, and its vocabulary key values. Select **Add record** to add more records.
1. Select **Run**.

![Three source records entered on a survivorship rule's Inspector tab]({{ "/assets/images/management/rules/inspect-test-survivorship-records.png" | relative_url }})

Before any survivorship rule runs, each field holds the value of the most recently modified record that has one. Records without a date count as modified in the order listed. Records with the same name count as coming from the same source - this matters for actions such as **Most Frequent Value**, which counts one vote per source.

For each rule, the **Survivorship decision** section lists every field, the value each source record offered, and which record the golden record value came from.

![The survivorship decision: DK wins because two of the three sources offered it]({{ "/assets/images/management/rules/inspect-test-survivorship-decision.png" | relative_url }})

## Rule unit tests

A unit test saves an example input and the result you expect. Open the **Tests** tab of a rule, then:

1. Select **New test** and enter a name.
1. Enter the input:
    - For data part, golden record and approval rules, enter **Input fields**.
    - For survivorship rules, enter the source records under **Given these source records**, the same way as in the [Inspector](#inspect-survivorship-rules).
1. Enter the values you expect after the rule has run (**Expected output fields**, or **Expect these golden record values** for survivorship rules).
1. Select **Save**.

Select **Run** on a test, or **Run all**. Each test shows **Passed** or **Failed**, and a table of every expected field with its actual value - fields that don't match are highlighted. For survivorship rules, the **Won by** column shows which source records held the winning value. When a test fails for a reason the table can't show - the rule's condition did not match, an action failed, or a survivorship test has no source records - the reason is listed below the table.

![Two survivorship rule unit tests: one passed, one failed with the expected and actual values]({{ "/assets/images/management/rules/inspect-test-unit-tests.png" | relative_url }})

## Verify the result

- In the Inspector, each rule in the timeline shows **Matched**, **Not matched** or **Error**, and the entity state highlights the fields a rule changed.
- A unit test shows **Passed** or **Failed** after it runs. Running tests updates the rule's health: a rule with a failing unit test is marked **Unhealthy**, and is marked healthy again once all its tests pass.

## What this changes

The Inspector only simulates: it changes no records and saves nothing. Unit tests are saved with the rule; running them changes no records, only the rule's healthy or unhealthy status.

## If something goes wrong

| What you see | What it means |
|---|---|
| A note above the results that a Lookup field was not resolved | The value entered is not an entity code. Enter the referenced record's entity code, or a name followed by the code in curly brackets. |
| A survivorship action that says it can't be previewed | The rule was run without source records - for example, from the Rule Inspector page. Open the survivorship rule's own **Inspector** tab and enter source records. |
| A survivorship unit test fails with a message about source records | The test has no source records. Edit it and add them. |
| **Editing or running this rule's unit tests requires owning the rule...** | You don't have the access needed to change this rule. Ask its owner. |
