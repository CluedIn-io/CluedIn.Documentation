---
title: Multi-match enrichment
url: https://documentation.cluedin.net/govern/enrichment/multi-match
content_type: how-to
section: Govern & improve > Enrichment
---

# Multi-match enrichment

> how-to: Steps to accomplish one task.

This article explains how to review and process multiple enrichment candidates for the same golden record.

## About multi-match enrichment

Some enrichers can return more than one possible match for a golden record. Instead of immediately applying a candidate, CluedIn stores the candidates as matches for review. Multi-match enrichment lets you compare those candidates with the enriched record and decide which matches to approve, reject, or revoke.

> **Note:** If an enricher returns only one match for a golden record, that match does not appear on the **Matches** tab. Instead, the enriched data appears directly on the **Preview** tab.

## Review matches

1. On the navigation pane, go to **Preparation** > **Enrich**.

1. Open the required enricher and select the **Matches** tab.

1. In the **Enriched records** list, select the record whose candidates you want to review.

   The matches table displays the candidates for the selected enriched record.

   ![Matches tab of a Companies House enricher: Enriched records list with statuses on the left, and the matches table with Compare links, Status and Comparison score for the selected record](https://documentation.cluedin.net/assets/images/preparation/enricher/multi-match/multi-match-table.png)

1. Review the values returned by each candidate. Use **Compare** to open the comparison view, where you can inspect the source and candidate values side by side.

   ![Comparison view for ABF Grain Products Ltd: candidate cards with scores at the top, and source and match values side by side for Identifier, Name and Address](https://documentation.cluedin.net/assets/images/preparation/enricher/multi-match/multi-match-comparison-view.png)

1. Select one or more candidates and choose **Approve**, **Reject**, or **Revoke**.

   - **Approve** accepts the selected match or matches.
   - **Reject** marks the selected match or matches as unsuitable.
   - **Revoke** removes a previous approval or rejection and returns the match to review.

   Rejecting or revoking a candidate also removes that candidate's data from the **Preview** tab.

> **Note:** Only enrichers with **Allow Select Multiple Matches** enabled in their settings allow multiple candidates for the same golden record to be selected.

## Enriched record statuses

The status shown in the **Enriched records** list summarizes the statuses of all candidates for that record.

| Status            | Description                                                                                              |
| ----------------- | -------------------------------------------------------------------------------------------------------- |
| **Needs review**  | The enriched record has candidates that still require a manual decision.                                 |
| **Auto-selected** | At least one candidate was auto-selected. You can still review and change the decisions.                 |
| **Approved**      | All reviewed candidates were approved.                                                                   |
| **Rejected**      | All reviewed candidates were rejected.                                                                   |
| **Reviewed**      | The enriched record has a mixture of decisions, or both reviewed and pending candidates.                 |
| **Conflicted**    | The enriched record has conflicting selected candidates. Review the candidates and resolve the conflict. |

## Match statuses

Each candidate in the matches table has its own status.

| Status            | Description                                                                                                                                       |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| **New**           | The candidate has not yet been reviewed.                                                                                                          |
| **Auto-selected** | CluedIn selected the candidate automatically. You can still review and change the decision.                                                       |
| **Approved**      | The candidate was approved.                                                                                                                       |
| **Rejected**      | The candidate was rejected and is not auto-selected again, even if it matches an auto-select condition.                                           |
| **Conflicted**    | More than one candidate was selected where the enricher does not allow multiple selected matches. Review the candidates and resolve the conflict. |

## Filter enriched records

Use the filter above the **Enriched records** list to find records by their aggregate status.

1. Select the filter icon next to the **Search enriched record** field.

1. Under **Group status**, select one or more statuses to show only the matching enriched records.

   The number next to each status shows how many enriched record groups have that status. **Needs review** excludes enriched records with auto-selected candidates; use **Auto-selected** to view those records.

1. Select **Reset** to clear the status filters and show all enriched records again.

![Animation: filtering the Enriched records list by status, such as Needs review or Auto-selected, and then selecting Reset to show all records](https://documentation.cluedin.net/assets/images/preparation/enricher/multi-match/multi-match-enriched-records-filter.gif)

## Compare candidates

The **Comparison** column opens the comparison view for a candidate. The comparison view shows the source values and candidate values that CluedIn used to evaluate the match.

When AI comparison is enabled for the enricher, the matches table also shows a **Comparison score**. This score is an AI-generated indication of how closely the candidate matches the enriched record. Use it as review guidance, not as the only basis for an approval decision.

![Animation: selecting Compare in the matches table to open the comparison view for a candidate, with its Comparison score](https://documentation.cluedin.net/assets/images/preparation/enricher/multi-match/multi-match-comparison.gif)

## Process all matches

To process matches for all enriched records, select the More menu next to Enriched records. If you apply a filter, the action affects only the enriched records that match that filter.

![Animation: opening the More menu next to Enriched records and processing all matches, after which the records and candidates show Rejected](https://documentation.cluedin.net/assets/images/preparation/enricher/multi-match/multi-match-bulk-process.gif)

## Process all matches for an enriched record

To process all candidates for one enriched record, select the **More** menu next to that record in the **Enriched records** list. These actions apply only to the candidates for that enriched record. They do not affect candidates that belong to another enriched record.

![Animation: opening the More menu next to one enriched record and processing all of its candidates at once](https://documentation.cluedin.net/assets/images/preparation/enricher/multi-match/multi-match-process-by-record.gif)

## Configure multi-match settings

To configure multi-match behavior, open the enricher and select the settings icon on the **Matches** tab.

| Setting                            | Description                                                                                                                                                                                                                                                                          |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Allow Select Multiple Matches**  | Allows users to select more than one candidate for the same golden record. Leave this disabled when only one candidate can be approved.                                                                                                                                              |
| **Auto-select Matches**            | Enables rule-based automatic selection of the best matching candidate.                                                                                                                                                                                                               |
| **Auto-select Matches Conditions** | Defines the rules a candidate must satisfy before CluedIn automatically selects it. This setting is available when **Auto-select Matches** is enabled. For details, see [Configure Auto-select Matches Conditions](#configure-auto-select-matches-conditions).                       |
| **Auto-select Matches using AI**   | Uses an AI model to evaluate the available candidates and select the most likely match. AI evaluation also provides the comparison content and score shown in the matches table. For details, see [Configure Auto-select Matches using AI](#configure-auto-select-matches-using-ai). |
| **Endpoint**                       | Selects the AI endpoint that evaluates the candidates. This setting is available when **Auto-select Matches using AI** is enabled.                                                                                                                                                   |
| **Prompt**                         | Provides instructions for the AI evaluation, including the important fields and selection criteria. This setting is available when **Auto-select Matches using AI** is enabled.                                                                                                      |

Auto-selected candidates can still be reviewed and changed in the **Matches** tab. Configure the rules or prompt carefully and use the comparison view to validate the results before relying on automatic selections.

## Configure Auto-select Matches Conditions

Use **Auto-select Matches Conditions** to define the rules a candidate must meet before CluedIn selects it automatically.

1. In **Matches Settings**, enable **Auto-select Matches**.

1. Under **Auto-select Matches Conditions**, add the conditions that identify a suitable candidate.

1. Save the settings.

CluedIn evaluates the conditions for the available candidates and automatically selects the best matching candidate when the conditions are met. Review auto-selected candidates in the **Matches** tab and adjust the decision when needed.

![Matches Settings with Auto-select Matches turned on and three or conditions on companyNumber and companies2.regNumber; Auto-select Matches using AI is off](https://documentation.cluedin.net/assets/images/preparation/enricher/multi-match/multi-match-auto-select-condition-settings.png)

### Example Auto-select Conditions

- Auto-select when the Matches `companyNumber` column equals `00079590`.

![Auto-select condition: Match Column companyNumber Equals the literal value 00079590](https://documentation.cluedin.net/assets/images/preparation/enricher/multi-match/multi-match-auto-select-condition-3.png)

- Auto-select when the Matches `companyNumber` column equals the golden record's `companies2.regNumber` value.

![Auto-select condition: Match Column companyNumber Equals the golden record vocabulary key companies2.regNumber](https://documentation.cluedin.net/assets/images/preparation/enricher/multi-match/multi-match-auto-select-condition-2.png)

- Auto-select when the golden record's `companies2.regNumber` value equals the Matches `companyNumber` column.

![Auto-select condition: Vocabulary companies2.regNumber Equals the value {column:companyNumber}](https://documentation.cluedin.net/assets/images/preparation/enricher/multi-match/multi-match-auto-select-condition-1.png)

## Configure Auto-select Matches using AI

Use **Auto-select Matches using AI** when an AI model should evaluate the available candidates and select the most likely match.

1. In **Matches Settings**, enable **Auto-select Matches using AI**.

1. Select the AI **Endpoint** to use for the evaluation. To reduce repeat AI requests and associated costs, choose an endpoint with a longer cache duration when you expect to evaluate the same records more than once.

1. Enter a **Prompt** that describes how the AI should compare the source record and candidates. Include the fields that matter most and any selection criteria.

1. Save the settings.

AI evaluation produces comparison content and a comparison score for the candidate. Use the score as review guidance and verify the result in the comparison view before relying on an automatic selection.

![Matches Settings with Auto-select Matches using AI turned on, the CluedIn-Mini Balanced endpoint selected, and a prompt setting matching priority and field mappings](https://documentation.cluedin.net/assets/images/preparation/enricher/multi-match/multi-match-auto-select-ai-settings.png)

### Example AI Prompt for Companies House

This prompt tells the AI how to map golden record properties to Matches columns when comparing a source record with a candidate.

```text
The matching priority is:
1. CompanyNumber
2. CompanyName
3. Address

Field name mappings between Source and Matches:
- {Vocabulary:companies2.regNumber}: companyNumber
- {Vocabulary:companies2.debtorName}: companyName
- Address group:
  - Source: {Vocabulary:companies2.addr1}, {Vocabulary:companies2.addr2}, {Vocabulary:companies2.addr3}, {Vocabulary:companies2.addr4}, {Vocabulary:companies2.postcode}
  - Candidate: address+registeredOfficeAddressLine1,address+registeredOfficeAddressLine2,address+registeredOfficeLocality,address+registeredOfficePostalCode
```

## Recommended review workflow

1. Enable the enricher and trigger the enrichment.

1. Review the **Matches** tab and enable **Auto-select Matches** if needed.

1. When available, review the comparison score and the properties used for comparison to confirm that the evaluation is appropriate.

1. Approve the appropriate candidate or candidates, and reject unsuitable candidates.

1. Use **Revoke** when a previous decision needs to be reconsidered.

Up: [Enrichment](https://documentation.cluedin.net/govern/enrichment.md)
