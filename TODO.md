# To do: documentation for AI assistants

Follow-ups to Agent mode (`_plugins/agent_markdown.rb`, `/llms.txt`, the
Markdown copy of every page, and [Use this documentation with an AI
assistant](docs/01-start-here/090-ai-assistants.md)). Not part of the site
build.

## Search the documentation over MCP

An assistant connected over MCP should be able to search the documentation and
get back the matching sections, instead of fetching `llms.txt` and walking the
pages itself.

- Needs something that runs a server: GitHub Pages only serves files. Options
  to weigh: a small MCP server over `llms-full.txt` (or the `.md` pages) with a
  search index; a hosted docs-to-MCP service that reads `llms.txt`; or a
  documentation search tool added to the CluedIn MCP server itself.
- Return sections, not whole pages: the `.md` pages are already split by
  heading, which is the natural unit.
- Keep it generated from the same build, so it cannot drift from the site.

## Test assistants on realistic tasks

Measure whether the documentation lets an assistant do real work, before and
after changes to it.

- Write a set of tasks with known correct answers, such as "onboard three
  customer files", "configure and validate deduplication on Customer", "add an
  enricher and confirm it ran", "stream golden records to an export target".
- For each, check that the assistant finds the right pages, picks the right
  operation (UI step, REST endpoint or MCP tool), supplies valid inputs, and
  can tell that the task succeeded.
- Run them against the live `llms.txt` and `.md` pages, and repeat after
  restructuring guides, so the effect of each change is measured rather than
  assumed.

## Questions for a product expert

Ten task guides were restructured to the how-to template in CONTRIBUTING.md
("The structure of a how-to"). Where the documentation did not confirm a fact
the template asks for, the section was left out rather than guessed. Answering
these lets the guides be completed.

**Upload a file** (`/ingest/data-sources/file`)
- Is **Group** required when uploading, and is there a default group?
- Can a failed load be retried anywhere other than the Preview tab? Do upload,
  parse and load continue if the user leaves the page after the upload ends?

**Ingestion generally** (file, mapping, processing, validations)
- Which claims does each task need? The docs give claims only for the whole
  Data Sources module.

**Create mapping** (`/ingest/mapping/create-mapping`)
- Are a new business domain, vocabulary and vocabulary keys (status New)
  created when you select **Create Mapping**, or only when the data set is
  processed?
- Are **Business domain** and **Vocabulary** required for auto mapping, as for
  manual mapping?
- Can AI mapping suggestions be edited before the mapping is created? What
  happens if the Azure OpenAI call fails?

**Process data** (`/ingest/processing/process-data`)
- Is **Purge quarantine before processing** selected by default?
- Does re-processing a data set overwrite values changed in CluedIn since the
  last run (manual edits, clean projects)?
- What does **Cancel** do to records already processed in that run?
- Does enabling auto-submission process records already waiting on the
  Preview tab, or only new ones?
- Are processed golden records sent to streams and export targets immediately?

**Validations** (`/ingest/processing/validations`)
- The text says a corrected value is highlighted in green; the screenshot
  shows bold on blue. Which is current?
- What role or ownership is needed to switch a data set to edit mode and add
  validations? Are validations kept when switching back to the original?

**Create a rule** (`/govern/rules/create-rule`)
- Can a rule be saved with no filters, and which records does it then apply to?
- What does the undocumented **Conditions** section of the Add Action pane do,
  and how does it combine with the rule's filters?
- Is a new rule always inactive? Does **Affected Records** count records whose
  value was already correct?
- Does reprocessing through the GraphQL `postProcess` query update the rule's
  status and its Affected records tab?
- `/troubleshooting/rules-not-working` and `/troubleshooting/rules-slow` refer
  to UI the other pages do not describe ("Rules > Execution History", "Entity
  Explorer", "published" rules). Are they current?

**Create a deduplication project** (`/master/deduplication/create-a-deduplication-project`)
- When several normalization rules are selected on one criterion, in what
  order are they applied? Are they chained?
- When a single-value normalization rule emits nothing, is the original value
  still compared?
- How does "cascading matching" across matching rule groups (Best practices)
  relate to rules combining with OR? Should it go into Matching semantics?
- Does creating a project or a rule need any claim besides Deduplication
  Project Management?
- Are there defaults for project type and the Sift4 threshold?

**Manage groups of duplicates** (`/master/deduplication/manage-groups-of-duplicates`)
- What are the options for "Choose the strategy for dealing with stale data"
  when merging, and what does each do?
- After unmerge or **Unmerge All**, are downstream systems fed by streams
  updated? (The rollback article says so, but describes a different UI.)
- How is an unmerge aborted? The status "Abort unmerging" exists; no control
  is documented.
- Which duplicate becomes the base golden record of a merge?

**Add an enricher** (`/govern/enrichment/add-enricher`)
- This page ends with **Save**; the per-enricher pages use **Test Connection**
  then **Add**. Which is current?
- Does inactivating an enricher stop all future enrichment, and does it
  remove enriched data already added?
- How long after triggering enrichment does data appear, and is there a
  completion indicator?

**Create, configure and run an AI agent** (`/govern/ai-agents/create-configure-and-run-an-ai-agent`)
- Which claim or role is needed to create, test, run and schedule AI agent jobs?
- The steps say **Create Data Source** pane, **Vocabulary Keys** and
  **Create**; the screenshot shows **Add data source**, a required **Type**
  (Query), **Fields to include** and **Add**. Which is current, and what other
  data source types exist?
- Can a job be tested or run without an **Endpoint**? Are **Skill** and the
  prompt **Instructions** required?
- Suggested values are described as green; the screenshot shows blue.
- Is there a default schedule interval ("Every 1 days" appears when disabled)?
- Can a running job be cancelled?

**Create a stream** (`/publish/streams/create-a-stream`)
- Are **Target name** and **Streaming mode** required, and what are their
  defaults?
- Do the **Outgoing** and **Incoming** edge descriptions have source and
  target swapped?
- Does the Streams claim alone allow choosing an export target, or is the
  Export Targets claim also needed?

## Images that do not match their text

Found while writing alt text. The alt text describes what each image actually
shows; the image or the text around it needs fixing.

- `docs/02-ingest/connectors/040-using-agents.md`: `agent-simple.png` (cloud vs
  on-premises deployment) sits under "Agent jobs", and `agent-complex.png` (job
  flow) under "Cloud deployment". They look swapped.
- `docs/11-solutions-and-integrations/power-automate/030-post-configuration-guide.md`:
  `sign-in-error-redirect-uri.png` shows the same AADSTS700054 id_token error
  as `sign-in-error-no-id-token.png`, not a redirect URI error.
- `docs/08-deploy-and-operate/monitoring/010-engine-room.md`: the image after
  the paragraph about processing-step metrics shows the "Status of Configured
  Integrations" panel.
- `docs/15-release-notes/010-2026-02.md`, line 65: the auto-increment example
  links `UniqueValues.png`.
- `docs/15-release-notes/index.md`, line 76: "Release plan for 2026-2027"
  shows a September 2025 to September 2026 roadmap.
- `docs/02-ingest/mapping/020-review-mapping.md`, line 128: the text is about
  linking employees to companies; the image shows a DB Schenker relations graph.
- `docs/03-model/010-identifiers.md`: `codes-1.gif` follows a sentence about
  **View Identifiers** but shows a shadow entity diagram.
- `docs/05-govern-and-improve/cleaning/070-how-to-fix-address-data.md`:
  `trigger-external-enrichment.png` only highlights the area near **Edit**.
- `docs/11-solutions-and-integrations/master-data-services/020-azure-relay.md`:
  the diagram labels a barrier "NAV", probably meaning NAT.
