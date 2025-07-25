---
layout: cluedin
title: Manage approval requests
parent: Workflow
permalink: workflow/manage-approval-requests
nav_order: 4
has_children: false
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

{:.important}
To use the **Workflow** module in CluedIn, you need to configure [Power Automate integration](/microsoft-integration/power-automate).

In this article, you will learn how to view, approve, and reject approval requests sent from the Power Automate widget in CluedIn.

## View pending approval requests

If you're an approver in the approval flow or if you made some changes in CluedIn that require approval from somebody else, you can find your pending requests in CluedIn. 

**To view pending approval requests**

1. On the navigation pane, go to **Workflow** > **Approvals**.

1. To view the approval requests that are assigned to you, go to the **Received** tab. Here, you can also approve or reject a request right away.

    ![view-approvals-1.png]({{ "/assets/images/workflow/view-approvals-1.png" | relative_url }})| relative_url }})

1. To view the approval requests that were sent out on your behalf, go to the **Sent** tab. Here, you can view the status of each request, indicating whether they have been approved, rejected, or still pending.

    ![approvals-sent.png]({{ "/assets/images/workflow/approvals-sent.png" | relative_url }})| relative_url }})

## Approve or reject an approval request

When a specific activity in CluedIn requires your approval, you receive an email in Outlook or a message in the Approvals app in Teams. You can then approve or reject a request from the email, Teams, or the Power Automate widget in CluedIn (**Workflow** > **Approvals**).

**To approve or reject a request from email**

1. Open the email and review the request details.

1. Make an approval decision by selecting **Approve** or **Reject**. Optionally, you can add a comment before sending your approval decision.

    ![email.png]({{ "/assets/images/workflow/email.png" | relative_url }})| relative_url }})

**To approve or reject a request from the Approvals app in Teams**

1. Open the request and review its details.

1. Make an approval decision by selecting **Approve** or **Reject**. Optionally, you can add a comment before sending your approval decision.

    ![teams.png]({{ "/assets/images/workflow/teams.png" | relative_url }})| relative_url }})

If you approved the request, the action that required your approval is automatically performed in CluedIn. Regardless of the approval decision, the user who performed the action receives a notification in CluedIn.