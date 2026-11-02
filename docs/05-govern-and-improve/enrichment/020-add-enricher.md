---
layout: cluedin
title: Add an enricher
parent: Enrichment
grand_parent: Govern & improve
nav_order: 20
permalink: /govern/enrichment/add-enricher
content_type: how-to
redirect_from: ["/preparation/enricher/add-enricher"]
source_path: docs/050-preparation/enricher/020-add-enricher.md
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

Add an enricher when you want CluedIn to add information from a third-party source to your golden records. While CluedIn offers a range of predefined enrichers for your use, you also have the option to create custom enrichers tailored to your specific needs. An added enricher is active: it enriches golden records during processing, and you can trigger enrichment for golden records that were processed before you added it.

## Prerequisites

- The **Enrichment** claim to add and edit enrichers, and the **Data Management** claim to trigger enrichment for a golden record. See [Claims](/administer/users-and-roles/claims).
- The details the enricher needs, such as an API key for the external service. The fields depend on the enricher; see its page under [Enricher reference](/govern/enrichment/enricher-reference).
- Golden records that have values in the vocabulary keys the enricher uses as input. If the enricher has no vocabulary key value to search with, it cannot look for additional information. See [Concept of enricher](/govern/enrichment/concept-of-enricher).

## Add and configure an enricher

You can add an enricher both before and after processing the data.

**To add and configure an enricher**

1. On the navigation pane, go to **Preparation** > **Enrich**.

1. Select **Add Enricher**.

1. On the **Choose Enricher** tab, select the needed enricher, and then select **Next**.

1. On the **Configure** tab, enter the authentication details. The list of fields that you need to complete depends on the selected enricher. You can complete the fields now or do it later on the enricher details page.

1. Optional: select **Configure with AI** to have AI suggest the configuration. See [Configure with AI](#configure-with-ai).

1. Select **Save**.

    ![Animation: from Enrich, Add Enricher is selected, an enricher is chosen, its Configure tab is completed, and the details page opens]({{ "/assets/images/preparation/enricher/add-enricher.gif" | relative_url }})

    The enricher details page opens, where you can view and change configuration information and other settings. The enricher is active, which means that the enrichment process will begin immediately after you start [processing](/ingest/processing/process-data). If you have already processed the data before adding an enricher, you can trigger the enrichment for the existing golden records.

On the enricher details page, you can manage the enricher:

- Change the display name of the enricher. 

- Select the source of data coming through the enricher.

- Specify the quality of data coming through the enricher.

- Inactivate the enricher if you no longer need it.

- Manage users who have access to the data coming through the enricher. For more details, see [Data access](/administer/users-and-roles/data-access).

## Configure with AI

Instead of filling in the **Configure** tab yourself, you can have AI suggest the vocabulary keys and, optionally, a filter, a rate limit, or a recurring schedule for the enricher.

![The Configure with AI panel on the Add Enricher dialog's Configure tab, with a Business domain selector, a Prompt field, and a Suggest settings button]({{ "/assets/images/preparation/enricher/configure-with-ai/configure-with-ai-panel.png" | relative_url }})
{: .documentation-screenshot}

**To configure an enricher with AI**

1. On the **Configure** tab, select **Configure with AI**.

1. Select the **Business domain** to enrich. AI reads the vocabulary keys that belong to this business domain to find candidates for the enricher's fields.

1. Optional: enter a **Prompt** with extra context, or ask AI to add a filter, a rate limit, or a recurring schedule. Drag a vocabulary key from the **Vocabulary keys** list into the prompt to reference it directly.

1. Optional: expand **Advanced** to choose a different AI endpoint. By default, suggestions use the organization's default AI endpoint.

1. Select **Suggest settings**.

   AI fills in the fields on the **Configure** tab with its suggestions. Each suggested field is labeled **AI suggested**, with the reason for that suggestion.

   ![The Configure tab after AI suggested settings: a summary banner showing the business domain, prompt and number of settings suggested, with Undo all and Suggest again buttons]({{ "/assets/images/preparation/enricher/configure-with-ai/ai-suggested-summary.png" | relative_url }})
   {: .documentation-screenshot}

1. Review the suggestions before saving the enricher:

   - For a vocabulary key field, AI fills in its best match. If more than one vocabulary key is a plausible match, the field is labeled **Requires manual action** and lists the **Possible keys** to choose from.
   - If your prompt asked for a rate limit or a recurring schedule, review the suggested values under **Rate Limiting** and **Recurring Enrichment** further down the **Configure** tab.

   ![The Website Vocabulary Key field with two AI-suggested possible keys, and Enable Rate Limiting turned on with a reason and a suggested number of calls]({{ "/assets/images/preparation/enricher/configure-with-ai/vocabulary-and-rate-limit-suggestion.png" | relative_url }})
   {: .documentation-screenshot}

   ![The Recurring Enrichment toggle turned on with an AI-suggested reason, and the Schedule Frequency fields below it showing the suggested repeat interval and days]({{ "/assets/images/preparation/enricher/configure-with-ai/schedule-suggestion.png" | relative_url }})
   {: .documentation-screenshot}

1. Optional: change any suggested value yourself, select **Suggest again** to rescan with a different prompt or business domain, or select **Undo all** to discard every AI suggestion and restore the values you had before.

1. Select **Save** on the **Configure** tab to save the enricher with the reviewed configuration.

{:.note}
**Configure with AI** only fills in the fields on the **Configure** tab; it does not save the enricher. Nothing from the AI suggestions is applied until you select **Save**.

## Trigger enrichment 

If you process the data and then add an enricher, the enrichment won't start automatically. To enrich the existing golden records, you can trigger enrichment in one of the following ways:

- Using the GraphQL tool.

- Manually trigger enrichment for each golden record.

**To trigger enrichment using the GraphQL tool**

1. On the navigation pane, go to **Consume** > **GraphQL**.

1. Enter a query to enrich all golden records that belong to a certain business domain. Replace _/Organization_ with the needed name of business domain.

    ```
    {
     search(query: "entityType:/Organization") {
         entries {
             actions {
                 enrich
             }
         }
     }
    }
    ```

1. Execute the query.

    You triggered the enrichment for the golden records belonging to the specified business domain. Now, you can view the enrichment results on the golden record details page.

**To trigger enrichment for each golden record manually**

1. Find and open the needed golden record.

1. In the upper-right corner of the golden record details page, select **More** > **Trigger external enrichment**.

    ![Animation: on the Organization golden record CluedIn, More is opened and Trigger external enrichment is selected]({{ "/assets/images/preparation/enricher/trigger-enrichment.gif" | relative_url }})

    Now, you can view the enrichment results on the golden record details page.

## View enrichment results

The **Properties** tab of the golden record lists new properties added through enrichment. The source of these properties is specified based on the type of enricher through which they were obtained.

![Animation: the Properties tab of the enriched CluedIn golden record, listing new properties with the enricher as their source]({{ "/assets/images/preparation/enricher/enricher-properties.gif" | relative_url }})

According to the [data life cycle](/get-started/core-concepts/data-life-cycle), properties added through enrichment appear in CluedIn as a clue. This clue is then transferred to the data part, which in turn becomes the constituent element of the golden record. The **History** tab of the golden record contains all the data parts that make up that golden record, including the data parts that came from the enricher. For more information, see [History](/master/golden-records/history).

![Animation: the History tab of the enriched CluedIn golden record, showing the data part that came from the enricher]({{ "/assets/images/preparation/enricher/enricher-history.gif" | relative_url }})

## Verify the result

- **After you save the enricher**, its details page opens and the enricher is active. This means that the configuration is saved; it does not mean that any golden record has been enriched yet.
- **After processing or triggering enrichment**, the new properties appear on the golden record's **Properties** tab and the enricher's data part on its **History** tab, as described in [View enrichment results](#view-enrichment-results). Enrichment data goes through the processing pipeline like any other clue, so it appears on the golden record once processing has finished, not at the moment you trigger it.
- If the enricher returns more than one possible match for a golden record, the candidates are not applied. They are stored on the enricher's **Matches** tab for review. See [Multi-match enrichment](/govern/enrichment/multi-match).

## What this changes

- **Adding an enricher saves its configuration and makes it active.** From then on, golden records are enriched when data is [processed](/ingest/processing/process-data). Golden records that were processed before you added the enricher are not enriched until you [trigger enrichment](#trigger-enrichment).
- **Enrichment changes golden records.** Information from the enricher arrives as a clue with the same primary identifier as the golden record. During processing, CluedIn turns it into a data part and merges it into the existing golden record by identifiers, so the golden record gains new properties and a new data part in its history. See [Concept of enricher](/govern/enrichment/concept-of-enricher).
- **Triggering enrichment with GraphQL** acts on every golden record that the search query returns, for example all golden records of a business domain.
- **To remove enriched data**, [delete the enricher's data part](/master/golden-records/delete-data-parts-from-golden-records) from the golden record. A data part from an enricher may appear again, so inactivate the enricher before you delete it.
- **Selecting Suggest settings only fills in the Configure tab.** AI suggestions are not saved, and the enricher is not created, until you select **Save**.

## If something goes wrong

- **Existing golden records are not enriched.** Enrichment does not start automatically for data processed before the enricher was added. [Trigger enrichment](#trigger-enrichment).
- **The enricher finds nothing for a golden record.** Check that the golden record has a value in the vocabulary key the enricher searches with, and that the enricher's authentication details are complete on the enricher details page.
- **Enrichment results wait for review instead of appearing on the golden record.** The enricher returned several candidates. Review them on the **Matches** tab; see [Multi-match enrichment](/govern/enrichment/multi-match).
- **Deleted enrichment data comes back.** Inactivate the enricher, and then delete the data part again.
- **Suggest settings is disabled.** Select a **Business domain** first; AI needs it to find vocabulary key candidates.
- **AI could not suggest a configuration.** This can happen when no AI endpoint is configured, or when the AI request fails. Expand **Advanced** to check or change the AI endpoint, and try **Suggest settings** again. You can still fill in the **Configure** tab yourself.
