---
layout: cluedin
title: Test a rule with unit tests
parent: Rules
grand_parent: Govern & improve
nav_order: 110
permalink: /govern/rules/rule-unit-tests
content_type: how-to
tags: ["management", "rules"]
last_modified: 2026-10-23
---

## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

Define a set of manual inputs and the output you expect a rule to produce from them, then run that test case on demand to get a pass or fail with a field-by-field diff. Use rule unit tests to confirm a rule still behaves as intended after you change it, without having to reprocess real records or manually check [Rule Inspector](/govern/rules/rule-inspector) results each time.

## Prerequisites

- The **Rule Builder** claim with at least the Consultant access level. See [Feature access](/administer/users-and-roles/feature-access).
- The `ruleAdvancedTools` organization feature enabled. This feature is in alpha and off by default; ask an administrator to enable it under **Administration** > **Organization features**.
- A rule to test. See [Create a rule](/govern/rules/create-rule).

## Inputs

| Field | Required | What it accepts |
|--|--|--|
| Name | Yes | The name of the test case. |
| Input fields | No | The entity field values the test runs the rule against, for example `Properties[user.email]` = `old@cluedin.com`. Same field format as [Rule Inspector](/govern/rules/rule-inspector). |
| Expected output fields | No | The field values you expect after the rule runs, in the same format. |

## Create and run a unit test

**To create a unit test**

1. Open the rule, and go to the **Tests** tab.
2. Select **New test**.
3. Enter a name for the test case.
4. Under **Input fields**, add every field the rule's conditions or actions depend on, with the value to test against.
5. Under **Expected output fields**, add every field you expect to have a specific value after the rule runs, with that expected value.
6. Select **Save**.

A rule can have multiple test cases. Repeat the steps above for each one.

**To run a unit test**

Select **Run** on a test case, or **Run all** to run every test case for the rule.

## Verify the result

Each test case shows a green check (passed) or red cross (failed), and a table of every expected field, its expected value, and the actual value the rule produced. A test passes only when every expected field's actual value matches; a test case with no expected output fields never passes, since there's nothing to confirm.

## What this changes

Nothing. Running a test case uses the same disposable, in-memory entity as [Rule Inspector](/govern/rules/rule-inspector) — it never reads or changes a real record. Creating, editing, and deleting test cases only changes the test cases themselves, not the rule.

## If something goes wrong

- **A test fails even though the rule looks correct.** Check the actual value shown for each failed field — it often points to a missing input field, or a condition that didn't match. Open [Rule Inspector](/govern/rules/rule-inspector) with the same input fields to see the full condition and action trace.
- **"Could not find unit test" or "Could not find rule" when running a test.** The test case or the rule it belongs to was deleted. Create a new test case.
