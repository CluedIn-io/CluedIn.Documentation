---
layout: cluedin
title: Audits
parent: Govern & improve
nav_order: 85
permalink: /govern/audits
content_type: how-to
summary: Run a manual or AI-assisted audit of your golden records, review records as Correct or Not correct, and follow up on what is wrong.
tags: ["governance", "audits", "data quality", "review", "steward inbox", "notifications"]
last_modified: 2026-11-25
---

## On this page
{: .no_toc .text-delta }

- TOC
{:toc}

An **audit** is a structured review of your golden records against a question, for example "is every attribute the contract promises actually populated?". Reviewers (or an AI endpoint) mark each record **Correct** or **Not correct**. The audit then shows how much of your data passes, and gives you a list of findings to follow up.

You can find audits in **Management** > **Audits**.

## Prerequisites

- To view audits, you need at least the **Informed** level on the **Management > Audits** claim. To create, start, stop, edit or delete audits, or to record findings, you need at least **Consultant**. See [roles and permissions](/administer/users-and-roles).
- For an AI-based audit, an AI endpoint must already be configured. See [Prerequisites to using AI agents](/govern/ai-agents/prerequisites-to-using-ai-agents).

## Create an audit

1. On the **Audits** page, select **New audit**.
1. Enter a **Name** and, optionally, a **Description**. You can change both later from the audit's **⋮** menu > **Edit details**.
1. Choose the **Mode**:
    - **Manual**: people review records themselves.
    - **AI-based**: an AI endpoint evaluates every record in scope against a prompt.
1. Under **What should this audit check?**, pick a template. The text below the list explains what the selected template actually inspects. Choose **Ask for something else, in your own words** to write your own check. In an AI-based audit, that text becomes the prompt the AI evaluates every record against.

    ![New audit panel with the "Completeness against the contract" template selected, and its explanation shown below the list]({{ "/assets/images/govern/audits/create-template-description.png" | relative_url }})

1. Optionally, set a **Time frame start** and **Time frame end**:
    - A start date in the past describes a historical window of data.
    - A start date in the future describes when the audit is scheduled to run.
1. Under **Users involved**, add the people who should review records. Each person you add gets a task in their [Steward Inbox](#notifications-and-the-steward-inbox) and a notification.
1. Optionally, enter a **Recurrence interval** to re-run the audit on a schedule, then select **Create**.

## Start, stop, resume and delete

- **Start audit** begins the review. If the audit's start date is still in the future, CluedIn asks you to confirm that you want to start it now rather than at its scheduled date.

    ![Confirmation dialog asking "Start this audit early?" for an audit scheduled to start on 1/15/2027]({{ "/assets/images/govern/audits/future-start-confirm.png" | relative_url }})

- **Stop audit** pauses it. While an audit is stopped, nobody can record findings for it. **Resume audit** makes it active again and keeps every finding recorded so far. When you resume an AI-based audit, its AI run continues from where it stopped.
- **Delete audit**, in the audit's **⋮** menu, permanently deletes the audit and all of its findings. You must stop an active audit before you can delete it.

    ![Confirmation dialog for deleting an audit, stating how many findings will be deleted with it]({{ "/assets/images/govern/audits/delete-confirm.png" | relative_url }})

You can only take part in one active audit at a time. If you start another audit while one you created or are involved in is still active, CluedIn tells you which audit is in the way.

People who aren't involved in any running audit see a notice on the **Audits** page when audits are running in the organization. The notice shows only how many audits are running, not their names or participants.

![Notice on the Audits page: "1 audit is currently running in your organization. You are not involved in it..."]({{ "/assets/images/govern/audits/reviewer-other-active-notice.png" | relative_url }})

### What this changes

Starting, stopping and resuming an audit only change the audit's own status. Deleting an audit removes the audit and its findings permanently, and cannot be undone. No audit action changes your golden records.

## Review records

While an audit you are part of is active, the audit icon in the top bar links to it, and you can record decisions in two places:

- **Search**: an **Audit** column shows each record's latest decision. Select one or more records, then select **Mark correct** or **Mark not correct** in the toolbar. Selecting a checkbox only selects the record. To preview a record, use its preview image.
- **A record's page**: use the ✓ (Correct) and ✕ (Not correct) buttons next to the record's name.

When you mark a record as **Not correct**, you can add a comment explaining what is wrong. The button shows a spinner until the decision is saved, and then the record's badge updates.

![Search results with the Audit column showing Correct and Not correct badges]({{ "/assets/images/govern/audits/search-mark-done.png" | relative_url }})

Two reviewers can record different decisions on the same record. Both decisions are kept.

## Work with findings

The audit's page shows its outcome, progress and activity, and lists every finding in a table:

- Use the **All records**, **Not correct** and **Correct** tabs, the search box, and the **Source**, **Assigned to** and **Resolution** filters to narrow the list.
- Sort by any column with arrows, and drag a column's edge to resize it.
- Select **Show full comment** to read a long comment, such as an AI explanation, in full.
- In **Assigned to**, assign a **Not correct** finding to the person who should fix it. In the **⋮** menu, mark the finding as resolved once it is fixed.
- **Refresh findings** reloads the table, and **Export findings (CSV)** downloads every finding, including its comment.

![Findings table with Source, Assigned to and Resolution filters, a comment with a "Show full comment" link, and an assignee]({{ "/assets/images/govern/audits/findings-table.png" | relative_url }})

### Verify the result

The **Audit outcomes** card shows **Records reviewed**, **Correct**, **Not correct** and **% Correct**, and updates as soon as a decision is saved. **Records reviewed** counts each reviewed record once. **Correct** and **Not correct** count decisions, so a record that two reviewers decided on counts twice.

## Notifications and the Steward Inbox

CluedIn creates a task in a user's **Steward Inbox**, and sends a notification through the steward notification channels:

- When the user is added to someone else's audit (**Audit participation**). The task stays until the audit is stopped.
- When a **Not correct** finding is assigned to the user (**Assigned audit finding**). The task includes the finding's comment and stays until the finding is resolved. If you reassign the finding, the new assignee is notified.

Each task links straight to the audit.

![Steward Inbox showing an "Audit participation" task: You were added to the audit "Supplier provenance review"]({{ "/assets/images/govern/audits/reviewer-inbox.png" | relative_url }})

## Audit coverage in the Trust Center

The Trust Center's **Governance maturity** chart includes **Audit coverage**: the share of golden records that have at least one audit finding.
