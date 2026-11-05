---
layout: cluedin
title: Generate formulas with AI
parent: Rules
grand_parent: Govern & improve
nav_order: 52
permalink: /govern/rules/generate-formulas-with-ai
content_type: how-to
tags: ["management", "rules", "ai"]
last_modified: 2026-10-23
---

## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

Describe what a Formula Condition or Formula Action should do in plain language, and let AI write the [Power Fx formula](/govern/rules/power-fx-formulas) for you. Use this when you know what the rule should check or change but don't want to look up the exact function and field names yourself.

## Prerequisites

- The **Rule Builder** claim with at least the Consultant access level. See [Feature access](/administer/users-and-roles/feature-access).
- The `ruleAdvancedTools` organization feature enabled. This feature is in alpha and off by default; ask an administrator to enable it under **Administration** > **Organization features**.
- At least one AI endpoint configured for the organization. See [AI platforms](/administer). Ask an administrator if none is available to choose from.

## Inputs

| Field | Required | What it accepts |
|--|--|--|
| AI endpoint | Yes, only shown when more than one is configured | Which configured AI endpoint generates the formula. When only one endpoint is configured, it's used automatically. |
| Prompt | Yes | A plain-language description of what the formula should check (for a condition) or change (for an action). |

## Generate a formula with AI

**To generate a formula with AI**

1. In the rule builder, add a **Formula** filter, or a **Formula Action**. See [Create a rule](/govern/rules/create-rule).
2. Next to the formula editor, select **AI**.
3. If more than one AI endpoint is configured, choose one.
4. Describe what the formula should do, for example: "Check whether the email ends with @cluedin.com".
5. Select **Generate**.
6. Review the generated formula. Select **Insert** to replace the editor's contents with it, or **Cancel** to discard it and try a different prompt.

## Verify the result

The generated formula appears in the formula editor, syntax-highlighted like any formula you write by hand. Save the rule to keep it; until you save, the change only exists in the open editor.

## What this changes

Generating a formula doesn't save the rule by itself — you still need to save the rule for the inserted formula to take effect. Inserting a generated formula replaces the editor's current contents.

## If something goes wrong

- **No AI endpoint appears to choose from.** No AI endpoint is configured for your organization. Ask an administrator to add one.
- **"The AI could not generate a valid Power Fx expression for this request."** The AI's attempts didn't produce a formula that the Power Fx engine accepts, usually because the request doesn't translate into a condition or action. Rephrase the prompt to be more specific, or refer to [Power Fx formulas](/govern/rules/power-fx-formulas) and write the formula by hand.
