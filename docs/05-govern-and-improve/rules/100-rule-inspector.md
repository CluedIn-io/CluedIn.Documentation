---
layout: cluedin
title: Debug a rule with Rule Inspector
parent: Rules
grand_parent: Govern & improve
nav_order: 100
permalink: /govern/rules/rule-inspector
content_type: how-to
tags: ["management", "rules"]
last_modified: 2026-10-23
---

## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

Rule Inspector runs a rule against entity field values you enter by hand, and shows, step by step, how each condition and action evaluated — including every branch of a nested AND/OR filter, and the before/after value of every field an action changed. Use it to find out why a rule did, or didn't, apply the way you expected, without reprocessing real records.

## Prerequisites

- The **Rule Builder** claim with at least the Consultant access level. See [Feature access](/administer/users-and-roles/feature-access).
- The `ruleAdvancedTools` organization feature enabled. This feature is in alpha and off by default; ask an administrator to enable it under **Administration** > **Organization features**.
- A rule to inspect. See [Create a rule](/govern/rules/create-rule).

## Inputs

| Field | Required | What it accepts |
|--|--|--|
| Entity field | No | The field to set on the sample entity, for example `Properties[user.email]` for a vocabulary key, or `Name`, `DisplayName`, `Description`, `EntityType` for a built-in field. Fields you don't set are left blank. |
| Value | No | The value to give that field. |
| Also run every other active rule of this scope | No | When on, runs every other active rule of the same scope (data part, golden record, or survivorship) against the same sample entity as well, in their normal processing order — not only the rule you opened the Inspector from. |

## Inspect a rule

**To inspect a rule**

1. Open the rule, and go to the **Inspector** tab.
2. Select **Add field**, and enter a field name and a value for the sample entity. Repeat for every field the rule's conditions or actions depend on.
3. Optionally, turn on **Also run every other active rule of this scope** to see how the whole set of rules for that scope behaves against the same entity.
4. Select **Run**.

## Verify the result

The **Results** panel lists one card per rule that was run, each showing:

- A green check or red cross for whether the rule's overall filter matched.
- The filter, shown as a nested tree matching its **AND**/**OR** structure, with a green check or red cross on every branch down to each individual condition.
- For each action that ran, whether it succeeded, any message it returned, and a before/after diff of every field it changed.

An inactive rule can still be inspected directly (it still appears with its result), but is skipped when you run "every other active rule of this scope" — only active rules are included there, matching how real processing works.

## What this changes

Nothing. Rule Inspector runs against a disposable, in-memory copy of an entity built from the fields you enter — it never reads or changes a real record, and nothing it does is saved.

Rule actions that call an external service, such as an AI-powered action or downloading an image, perform that real call when run through the Inspector, the same as they would in a normal preview. Keep that in mind if a rule being inspected uses one of those actions.

## If something goes wrong

- **A condition shows a red cross unexpectedly.** Check that you set every field the condition reads — a field left blank reads as empty, which can make a comparison fail. For a Formula Condition, see [Power Fx formulas](/govern/rules/power-fx-formulas) for what each context variable holds.
- **An action shows an error instead of a before/after diff.** The message under the action explains what went wrong, for example a missing required property. Fix the rule's configuration and run the Inspector again.
