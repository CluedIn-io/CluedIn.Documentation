---
layout: cluedin
title: Debug a rule with Rule Inspector
parent: Rules
grand_parent: Govern & improve
nav_order: 100
permalink: /govern/rules/rule-inspector
content_type: how-to
tags: ["management", "rules"]
last_modified: 2026-10-24
---

## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

Rule Inspector steps through rules against a sample entity the way a debugger steps through code: one rule at a time, with the entity's complete field values before and after it ran, and why its filter did or didn't match. Use it to find out why a rule did, or didn't, apply the way you expected, without reprocessing real records.

## Prerequisites

- The **Rule Builder** claim with at least the Consultant access level. See [Feature access](/administer/users-and-roles/feature-access).
- The `ruleAdvancedTools` organization feature enabled. This feature is in alpha and off by default; ask an administrator to enable it under **Administration** > **Organization features**.
- A rule to inspect. See [Create a rule](/govern/rules/create-rule).

## Inputs

| Field | Required | What it accepts |
|--|--|--|
| Record | No | An existing record to load field values from, picked by searching its name. Loads every vocabulary property and built-in field the record currently has into the field list below, which you can then still edit before running. |
| Entity field | No | The field to set on the sample entity, for example `Properties[user.email]` for a vocabulary key, or `Name`, `DisplayName`, `Description`, `EntityType` for a built-in field. Fields you don't set are left blank. |
| Value | No | The value to give that field. |

## Inspect a rule

Open the Inspector either from a specific rule, or on its own across every scope:

- From a rule's own **Inspector** tab — the stepper runs only that rule's own scope, and lands on that rule once you run it.
- From **Rule builder** > the **Rule Inspector** tile, alongside the Data part/Survivorship/Golden record rules tiles. This runs data part, survivorship, and golden record rules together, in one combined run — each rule in the list and the detail panel carries its own scope badge so you can tell them apart.

**To inspect a rule**

1. Open the Inspector (see above).
2. Either search for and pick an existing record to load its field values, or select **Show manual fields** and then **Add field** to enter a field name and a value by hand. You can combine both — pick a record, then adjust individual fields before running.
3. Select **Run**.

Running always walks every rule in scope — data part, golden record, and survivorship when opened from the Rule Builder dashboard, or just the current rule's own scope when opened from a rule's Inspector tab — in their normal processing order, whether each one is active or not. It is not limited to rules whose conditions match the sample entity.

## Step through the rules

After running, a panel on the left lists every rule that ran, in processing order, each marked with its own match/no-match/error status and whether it's active — a map of the whole run you can scan at a glance. From the standalone page, each entry also shows which of the three scopes it belongs to. Select any rule in that list to jump straight to it, or use the toggles above it to narrow the list (and Previous/Next):

- **Only show active** — hides inactive rules.
- **Only show matched** — hides rules whose own condition didn't match the sample entity.

Both toggles can be turned on together.

The Inspector lands on the rule you opened it from and shows one rule at a time on the right:

- A green check or red cross for whether the rule's overall filter matched, whether it's active, and (in a combined run across all three scopes) which scope it belongs to.
- The filter, shown as a nested tree matching its **AND**/**OR** structure, with a green check or red cross on every branch down to each individual condition. A Formula Condition shows its Power Fx expression directly, instead of just a pass/fail.
- Each action group's own condition, if it has one — an action group only runs its actions when its own condition also matches; when it doesn't, the Inspector says so instead of just showing nothing.
- For each action that ran, whether it succeeded, any message it returned, and its own configured properties (for example a Set Value action's field name and value) — a Formula Action's Power Fx expression is shown the same way a Formula Condition's is.
- The sample entity's complete field values immediately before and immediately after the rule ran, with any field the rule changed highlighted — not just the fields an action touched. Turn on **Show only changed fields** to hide everything that didn't change.

Use **Previous** and **Next** (or the <kbd>←</kbd>/<kbd>→</kbd> arrow keys, or <kbd>p</kbd>/<kbd>n</kbd>) to step to the previous or next rule in processing order, or select a rule directly from the list on the left. Keyboard shortcuts are ignored while you're typing in a field.

Because every rule runs in order against the same entity, a later rule's "before" state already reflects every change an earlier rule made — the same as real processing.

The rule list and the detail panel each scroll on their own, and the step name, status badges, and Previous/Next stay in place at the top of the detail panel — so reading a long entity-state table, or scanning a long rule list, never scrolls the stepping controls out of view.

## What this changes

Nothing. Rule Inspector runs against a disposable, in-memory copy of an entity — seeded from a picked record's current values, or built from the fields you enter by hand — and never reads or changes a real record; nothing it does is saved.

Rule actions that call an external service, such as an AI-powered action or downloading an image, perform that real call when run through the Inspector, the same as they would in a normal preview. Keep that in mind if a rule being inspected uses one of those actions.

A survivorship rule's own condition, and each action group's condition, run against the sample entity exactly as a golden record rule's would. Its actions (Best Quality, Latest Matching Condition, and the rest of the "set golden record value" actions) are different: they resolve a value by comparing a golden record's real underlying source records, which the Inspector's single sample entity can never provide. They always fail when run through the Inspector — read the message under the action for confirmation that this is expected, not a problem with the rule.

## If something goes wrong

- **A condition shows a red cross unexpectedly.** Check that you set every field the condition reads — a field left blank reads as empty, which can make a comparison fail. For a Formula Condition, see [Power Fx formulas](/govern/rules/power-fx-formulas) for what each context variable holds.
- **An action shows an error instead of updating the "after" state.** The message under the action explains what went wrong, for example a missing required property. Fix the rule's configuration and run the Inspector again.
