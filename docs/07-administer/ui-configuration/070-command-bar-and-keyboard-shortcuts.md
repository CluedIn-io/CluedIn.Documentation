---
layout: cluedin
title: Command bar and keyboard shortcuts
parent: UI configuration
grand_parent: Administer
nav_order: 70
permalink: /administer/ui-configuration/command-bar-and-keyboard-shortcuts
content_type: how-to
tags: ["administration", "user interface"]
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

On this page you can learn how to open and use the command bar, and which keyboard shortcuts CluedIn supports.

# Open the command bar

The command bar is an overlay you can open from anywhere in CluedIn to jump to a page, run a quick action, or find your way to rules and AI agents, without using the menus.

**To open the command bar**

- Press **Ctrl+K** (Windows/Linux) or **⌘K** (Mac).

Press the same combination again, or **Esc**, to close it.

![The command bar open over the Administration area of CluedIn, listing matching pages such as Administration / API Tokens and Administration / Artificial Intelligence]({{ "/assets/images/administration/command-bar/command-bar-open.png" | relative_url }})

# Use the command bar

**To find and go to a page**

1. Open the command bar.
1. Start typing the name of a page, module, or area, such as `rule` or `deduplication`.
1. Select a result to go there. The command bar closes automatically.

Results that you've used recently are shown above otherwise similar matches, so the pages and actions you work with most are usually at the top.

**To run an action**

Some results run an action directly instead of taking you to a page — for example, **Copy link to this page**. Selecting one runs it immediately and shows a confirmation message.

# Keyboard shortcuts reference

Besides the command bar itself, CluedIn supports the following keyboard shortcuts.

| Shortcut | What it does | Where it works |
|---|---|---|
| **Ctrl+K** / **⌘K** | Opens the command bar. | Anywhere in CluedIn. |
| **Esc** | Closes the command bar. | While the command bar is open. |
| **A** | Approves the current duplicate match. Same as selecting **Approve**. | On a duplicate group's conflict-resolution step, in a [deduplication project]({{ "/master/deduplication/manage-groups-of-duplicates" | relative_url }}). |
| **R** | Rejects the current duplicate match. Same as selecting **Reject**. | On a duplicate group's conflict-resolution step, in a [deduplication project]({{ "/master/deduplication/manage-groups-of-duplicates" | relative_url }}). |
| **Ctrl+S** / **⌘S** | Saves your pending changes. Same as selecting **Save**. | On an entity's **Properties** tab, while in edit mode. |

{: .note }
The **A** and **R** shortcuts only act while the corresponding button would otherwise be available — for example, **A** has no effect once a group is already approved. Both go through the same confirmation dialog as clicking the button with your mouse.

**To see this list inside CluedIn**

1. Open the command bar (**Ctrl+K** / **⌘K**).
1. Select **Keyboard shortcuts**.

    ![The command bar's Keyboard shortcuts view, listing each shortcut next to its key combination]({{ "/assets/images/administration/command-bar/keyboard-shortcuts-help.png" | relative_url }})

1. Select **Back to search** to return to the command bar, or press **Esc** to close it.
