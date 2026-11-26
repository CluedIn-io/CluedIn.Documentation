---
layout: cluedin
title: Responsibilities
parent: Users and roles
grand_parent: Administer
nav_order: 105
permalink: /administer/users-and-roles/responsibilities
content_type: how-to
tags: ["administration", "roles", "raci"]
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

Responsibilities say who does, approves, is asked about, or is told about the work on a CluedIn feature, and on which data. They decide where Steward Inbox tasks go. Set them up when you want deduplication matches, clean projects, failing rules or streams to reach the right people without adding everyone as an owner.

A responsibility doesn't give anyone access. What a role can open and change is set by its [access levels](/administer/users-and-roles/roles#supported-access-levels), and what a user or role can do with one item is set on the item's [Access tab](/administer/users-and-roles/feature-access#item-access).

## Prerequisites

- To add, edit or delete responsibilities: the **Roles** claim at **Edit** access or higher. See [Roles](/administer/users-and-roles/roles).
- The role or person you want to assign must already exist. See [Roles](/administer/users-and-roles/roles) and [User management](/administer/users-and-roles/user-management).
- To describe a responsibility in your own words, your organization needs an AI endpoint. See [Configure a model endpoint](/govern/ai-agents/prerequisites-to-using-ai-agents#configure-a-model-endpoint).

## How responsibilities work

Each responsibility has an assignee, a RACI letter, a feature, and what it applies to.

| RACI letter | Meaning |
|--|--|
| **Responsible** | Does the work. Tasks are routed to them. |
| **Accountable** | Approves the work. Only one role or person should be Accountable for the same work. |
| **Consulted** | Is asked for input. |
| **Informed** | Is told when the work is done. |

The assignee is a role or one person:

- **A role**: everyone in the role sees the task. The first person to pick it up takes it, and the others see who has it.
- **A person**: tasks go to that person's inbox and wait there until they pick them up. Nothing is reassigned automatically.

A responsibility applies to one of the following:

- **Everything** in the feature.
- **Specific business domains**. With exactly one business domain, you can narrow it down to some records with a condition, using the same builder as rules.
- **Specific data sources**.
- **Specific projects** of the feature, such as specific rules, clean projects or streams. This option appears only when exactly one feature that has projects is selected.

Saving creates one responsibility per feature and per business domain, data source or project. The lists show them grouped into one row, with the values as tags.

### Which responsibility wins

When several responsibilities match the same task, the most specific one wins, in this order:

1. A project or data source.
1. A business domain with a condition.
1. A business domain.
1. Everything in the feature.

If two equally specific responsibilities match, both assignees get the task, and the list shows an overlap warning.

## Add a responsibility for one role

1. Go to **Administration** > **Roles**, and then select the role.

1. Go to the **Responsibilities** tab, and then select **Add responsibility**.

    ![The Responsibilities tab of the DataSteward role, listing its responsibilities with the RACI letter, feature and scope of each, and warnings under some rows]({{ "/assets/images/administration/responsibilities/role-responsibilities-tab.png" | relative_url }})

1. Fill in the form, as described in [Fill in the responsibility form](#fill-in-the-responsibility-form). The role is already set as the assignee.

1. Select **Add**.

## Add a responsibility from the list of all responsibilities

1. Go to **Administration** > **Roles**, and then go to the **All responsibilities** tab.

    The list is grouped by feature. Select a feature in the toolbar to show only that feature, or select **Export CSV** to download the list. To see only the rows that need attention, set **Status** to **Needs attention**, or select **Show only these** in the issues banner.

    ![The All responsibilities tab: a banner saying how many issues need attention, and responsibilities grouped by feature, each row showing who it is assigned to, the RACI letter and the scope]({{ "/assets/images/administration/responsibilities/all-responsibilities-tab.png" | relative_url }})

1. Select **Add responsibility** in the toolbar, or **Add responsibility** on a feature's header to start with that feature selected.

1. Fill in the form, as described in [Fill in the responsibility form](#fill-in-the-responsibility-form).

1. Select **Add**.

## Fill in the responsibility form

![The Add responsibility panel, with the "Describe it in your own words" box at the top, then Assign to, Features, Applies to and RACI]({{ "/assets/images/administration/responsibilities/add-responsibility-form.png" | relative_url }})

1. Optional: under **Describe it in your own words**, write what should happen, for example "Make Sarah responsible for Customer Party when matches are detected", and then select **Fill in the form**.

    The AI fills in the fields below and shows what it understood, phrase by phrase. If it couldn't tell something, such as who should do the work, it says so; pick that field yourself. The AI never saves anything. Check the fields before you select **Add**.

1. In **Assign to**, select a role. To assign one person, type their name.

1. In **Features**, select one or more features.

1. In **Applies to**, select what the responsibility covers, and then select the business domains, data sources or projects.

1. Optional: with exactly one business domain selected, select **Add condition** under **Narrow down (optional)** to cover only the records that match the condition.

1. In **RACI**, select the letter.

The summary at the bottom of the form says, in one sentence, what saving will add. Options that would only repeat an existing responsibility are disabled and marked **Already assigned**.

When the new responsibility needs a decision, the form asks in place:

- **[Role] needs more access**: the role doesn't have the access level this RACI letter needs on the feature. **Also give [role] [level] access to [feature]** is ticked by default, and saving then changes the role's access together with the responsibility. For a person, it's their role that gets the access, so it applies to everyone in that role. If you untick it, the responsibility is still added, but the work waits until someone gives the access.
- **[Name] is already Accountable for this**: only one role or person can approve the same work. Choose **Replace [name] with [assignee]**, which removes the previous Accountable when you add, or **Keep [name]**, which adds nothing.

To start again, select **Clear** next to **Fill in the form**, or **Clear and start over** under what the AI understood. Both empty the prompt and the form, and keep the role when you opened the form from a role page.

## Edit, reassign or delete a responsibility

Select a row to open its details, and then:

- Select **Edit** to change the business domains, data sources or projects of the row.
- For a person, select **Edit or reassign**, and then pick another person or a role in **Assign to**. Their tasks move with the responsibility. Organization admins can reassign any responsibility; the role or person that is Accountable for the same work can reassign it too.
- Select **Delete** to remove the whole row, with all its tags. Work stops being routed to that assignee.

## Verify the result

- The new row appears on the role's **Responsibilities** tab and on the **All responsibilities** tab, in the group of its feature.
- The next time the Steward Inbox is opened or refreshed, tasks for the covered work appear for the assignee. Tasks routed to a role show **Routed to** the role, with **Pick up** for anyone in it. After someone picks a task up, the others see who has it, and the person who has it can select **Hand back**.

## What this changes

Responsibilities only decide where tasks go. They don't change what anyone can open or edit, and they don't change any data. Tasks are worked out from the responsibilities each time the inbox is loaded, so a change applies to existing tasks straight away. Deleting or reassigning a responsibility can be undone by adding it again.

Today, responsibilities route these Steward Inbox tasks: duplicate matches waiting for review, clean projects waiting to be processed, rules that need attention, and streams that need attention. Tasks for items you own still reach you as before.

## If something goes wrong

The list rows and the issues panel show these warnings; the form handles not enough access and a second Accountable as decisions (see [Fill in the responsibility form](#fill-in-the-responsibility-form)), shows overlaps as small notes, and warns about a deactivated person. On the **All responsibilities** tab, select **View issues** to see them all, with an action to fix each one.

![The issues panel, listing each issue with a short explanation and a fix action such as Add Accountable, Change access or Review]({{ "/assets/images/administration/responsibilities/issues-panel.png" | relative_url }})

| Warning | What it means | What to do |
|--|--|--|
| **Two Accountable** | More than one role or person is Accountable for the same feature and scope. | Keep one Accountable assignee. |
| **Overlap** | Two assignees are Responsible for the same feature and scope, so both receive the tasks. | Narrow one of them down, or delete one. |
| **Already exists** | The same responsibility exists. When you add several at once, existing ones are skipped and the form says how many. | Nothing; the existing one stays. |
| **Not enough access** | Responsible and Accountable need at least **Edit** access to the feature, and Consulted and Informed need at least **View**, in the assignee's role. For a person, their roles are checked. | Select **Change access** to open the role and raise its access level. |
| **No Accountable** | Nobody approves the work for a feature and scope. | Select **Add Accountable**. |
| **Deactivated user** | The assigned person is deactivated in user management. | An admin should reassign their responsibilities. |

If **Fill in the form** says that no AI endpoint is configured, ask an admin to add one, or fill in the form yourself.
