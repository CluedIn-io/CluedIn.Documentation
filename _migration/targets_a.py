"""Routing table, part 1: Get started, Ingest, Model, Master.

Each entry places a set of source articles under exactly one home. `sub=None`
means the pages become direct children of the section itself.

`new_pages` are articles that do not exist in the old tree and are written by
the migration: orientation pages, and the quickstart that now links to the
tutorials rather than duplicating them.
"""

TARGETS = [
    # -----------------------------------------------------------------------
    # Get started
    # -----------------------------------------------------------------------
    dict(
        section="start",
        sub=None,
        pages=[
            ("docs/009-quick-feature-tour.md", dict(type="tutorial", order=20)),
            ("docs/010-get-cluedin.md", dict(type="how-to", order=60)),
            ("docs/020-getting-access.md", dict(type="how-to", order=70)),
            (
                "docs/200-kb/kb0010-faq.md",
                dict(type="reference", order=80, slug="faq"),
            ),
        ],
        new_pages=[
            dict(
                slug="what-is-cluedin",
                title="What is CluedIn?",
                order=10,
                type="concept",
                body=(
                    "CluedIn is a master data management platform. It ingests records from every "
                    "system you connect to it, works out which of those records describe the same "
                    "real-world thing, and produces one **golden record** per thing - with the "
                    "full history of where each value came from.\n\n"
                    "## What the platform does\n\n"
                    "| Stage | What happens | Where it is documented |\n"
                    "|---|---|---|\n"
                    "| Ingest | Records arrive from files, databases, endpoints and connectors, "
                    "and are mapped onto your model. | [Ingest](/ingest) |\n"
                    "| Model | Business domains, vocabularies and identifiers describe what the "
                    "data means. | [Model](/model) |\n"
                    "| Master | Duplicates are found and merged into golden records. | "
                    "[Master](/master) |\n"
                    "| Govern & improve | Clean projects, rules, enrichers and tags raise and hold "
                    "data quality. | [Govern & improve](/govern) |\n"
                    "| Publish & consume | Streams, export targets, GraphQL and REST deliver the "
                    "trusted data onward. | [Publish & consume](/publish) |\n\n"
                    "The two supporting areas are [Administer](/administer) - managing the product "
                    "- and [Deploy & operate](/operate) - running the installation.\n\n"
                    "## What makes it different\n\n"
                    "CluedIn does not require you to agree on a schema before you load data. "
                    "Records are ingested as they are, described with vocabularies, and connected "
                    "through identifiers as evidence arrives. That property is called "
                    "[eventual connectivity](/get-started/core-concepts/eventual-connectivity), "
                    "and it is the idea most worth understanding before anything else.\n\n"
                    "## Next\n\n"
                    "- New to the product: [Quickstart](/get-started/quickstart)\n"
                    "- Want the vocabulary first: [Core concepts](/get-started/core-concepts) and "
                    "[Terminology](/get-started/terminology)\n"
                    "- Learning for a specific role: [Learning paths](/learning-paths)\n"
                ),
            ),
            dict(
                slug="quickstart",
                title="Quickstart",
                order=40,
                type="tutorial",
                body=(
                    "This is the shortest complete path through CluedIn: get data in, make it "
                    "good, and send it somewhere. Each step is a tutorial that lives with the "
                    "feature it teaches, so what you learn here is the same article you will come "
                    "back to later.\n\n"
                    "Work through them in order - each one assumes the previous one is done.\n\n"
                    "| # | Step | What you end up with |\n"
                    "|---|---|---|\n"
                    "| 1 | [Ingest data](/ingest/tutorial-ingest-data) | A data source loaded, "
                    "mapped and processed into golden records |\n"
                    "| 2 | [Clean data](/govern/cleaning/tutorial-clean-data) | Obvious quality "
                    "problems fixed in a clean project |\n"
                    "| 3 | [Deduplicate data](/master/deduplication/tutorial-deduplicate-data) | "
                    "Duplicate records merged into single golden records |\n"
                    "| 4 | [Stream data](/publish/streams/tutorial-stream-data) | Golden records "
                    "flowing to an export target |\n"
                    "| 5 | [Create rules](/govern/rules/tutorial-create-rules) | Logic applied "
                    "automatically as data changes |\n"
                    "| 6 | [Create hierarchies](/model/hierarchies/tutorial-create-hierarchies) | "
                    "Records organised into a parent/child structure |\n"
                    "| 7 | [Work with the glossary](/govern/work-with-glossary) | Terms that "
                    "describe groups of golden records |\n"
                    "| 8 | [Add relations between records](/model/relationships/tutorial-add-relations) "
                    "| Records connected to each other |\n\n"
                    "**Before you start.** You need access to a CluedIn instance. If you do not "
                    "have one yet, see [How to get CluedIn](/get-started/get-cluedin) and "
                    "[Getting access](/get-started/getting-access).\n"
                ),
            ),
            dict(
                slug="terminology",
                title="Terminology",
                order=50,
                type="reference",
                body=(
                    "Each term below has exactly one home in the documentation. If you are "
                    "looking for the definition, start here; if you are looking for how to work "
                    "with the thing, follow the link.\n\n"
                    "| Term | What it means | Canonical home |\n"
                    "|---|---|---|\n"
                    "| Golden record | The single trusted record for one real-world thing, built "
                    "from all the data parts that describe it. | "
                    "[Core concepts](/get-started/core-concepts/golden-records) - working with "
                    "them: [Master](/master/golden-records) |\n"
                    "| Data part | One system's version of a record at one point in time. Golden "
                    "records are assembled from data parts. | "
                    "[Data life cycle](/get-started/core-concepts/data-life-cycle) |\n"
                    "| Clue | The unit of data CluedIn ingests - a record plus its metadata and "
                    "identifiers. | [Clue reference](/get-started/core-concepts/clue-reference) |\n"
                    "| Business domain | The classification of a record, such as Customer or "
                    "Product. Formerly called *entity type*. | "
                    "[Model](/model/business-domains) |\n"
                    "| Vocabulary | The set of properties that describe records in a business "
                    "domain. Formerly called *schema*. | [Model](/model/vocabularies) |\n"
                    "| Vocabulary key | One property within a vocabulary. | "
                    "[Model](/model/vocabularies/vocabulary-keys) |\n"
                    "| Identifier | A value that identifies a record across systems and lets "
                    "CluedIn connect records. Formerly called *entity code*. | "
                    "[Model](/model/identifiers) |\n"
                    "| Edge / relationship | A connection between two records. | "
                    "[Model](/model/relationships) |\n"
                    "| Origin | The system a data part came from. | "
                    "[Core concepts](/get-started/core-concepts/origin) |\n"
                    "| Eventual connectivity | Records connecting up as evidence arrives, rather "
                    "than requiring an agreed schema up front. | "
                    "[Core concepts](/get-started/core-concepts/eventual-connectivity) |\n"
                    "| Data source | A file, database, endpoint or connector that feeds records "
                    "into CluedIn. | [Ingest](/ingest/data-sources) |\n"
                    "| Mapping | The definition of which source column becomes which vocabulary "
                    "key. | [Ingest](/ingest/mapping) |\n"
                    "| Clean project | A workspace for fixing recurring data quality problems. | "
                    "[Govern & improve](/govern/cleaning) |\n"
                    "| Deduplication project | A workspace for finding and merging duplicate "
                    "records. | [Master](/master/deduplication) |\n"
                    "| Rule | Logic applied automatically to data parts or golden records. | "
                    "[Govern & improve](/govern/rules) |\n"
                    "| Enricher | A service that adds data from an external source. | "
                    "[Govern & improve](/govern/enrichment) |\n"
                    "| Glossary term | A named group of golden records that meet a condition. | "
                    "[Govern & improve](/govern/work-with-glossary) |\n"
                    "| Stream | A continuous export of golden records to an export target. | "
                    "[Publish & consume](/publish/streams) |\n"
                    "| Export target | The destination a stream writes to. | "
                    "[Publish & consume](/publish/export-targets) |\n\n"
                    "Several of these names changed in the 2025.05 release. See "
                    "[Terminology changes](/release-notes/terminology-changes) for the full "
                    "before-and-after list.\n"
                ),
            ),
        ],
    ),
    dict(
        section="start",
        sub="core-concepts",
        title="Core concepts",
        slug="core-concepts",
        nav_order=30,
        default_type="concept",
        intro=(
            "Short explanations of the ideas the rest of the documentation assumes you know. "
            "These pages explain **what** something is; the lifecycle sections explain **how** to "
            "work with it."
        ),
        pages=[
            "docs/110-key-terms-and-features/010-data-life-cycle.md",
            "docs/110-key-terms-and-features/050-golden-records.md",
            "docs/110-key-terms-and-features/080-eventual-connectivity.md",
            "docs/110-key-terms-and-features/120-origin.md",
            "docs/110-key-terms-and-features/020-clue-reference.md",
            "docs/110-key-terms-and-features/070-connectors.md",
            "docs/110-key-terms-and-features/060-billable-records.md",
        ],
    ),
    # -----------------------------------------------------------------------
    # Ingest
    # -----------------------------------------------------------------------
    dict(
        section="ingest",
        sub=None,
        pages=[
            (
                "docs/010-getting-started/020-data-ingestion.md",
                dict(
                    title="Tutorial: ingest data",
                    slug="tutorial-ingest-data",
                    type="tutorial",
                    order=10,
                ),
            ),
        ],
    ),
    dict(
        section="ingest",
        sub="data-sources",
        title="Data sources",
        slug="data-sources",
        nav_order=20,
        default_type="how-to",
        index_from="docs/040-integration/190-data-sources.md",
        intro=(
            "A data source is where records come from. CluedIn reads from files you upload, "
            "databases it connects to, endpoints that push data in, and "
            "[connectors](/ingest/connectors) that crawl an external system.\n\n"
            "Whichever you choose, the next step is the same: [map](/ingest/mapping) the source "
            "onto your model, then [process](/ingest/processing) it."
        ),
        pages=[
            ("docs/040-integration/data-sources/130-define-data-to-ingest.md", dict(type="concept")),
            "docs/040-integration/data-sources/140-file.md",
            "docs/040-integration/data-sources/150-endpoint.md",
            "docs/040-integration/data-sources/160-database.md",
        ],
    ),
    dict(
        section="ingest",
        sub="mapping",
        title="Mapping",
        slug="mapping",
        nav_order=30,
        default_type="how-to",
        intro=(
            "Mapping decides which source column becomes which vocabulary key, which value "
            "identifies the record, and what business domain it belongs to. It is the point where "
            "raw data meets your [model](/model).\n\n"
            "Property rules and pre-process rules shape values *during* mapping, before the record "
            "becomes a data part."
        ),
        pages=[
            "docs/040-integration/data-sources/170-create-mapping.md",
            "docs/040-integration/data-sources/180-review-mapping.md",
            "docs/040-integration/additional-operations-on-records/010-property-rules.md",
            "docs/040-integration/additional-operations-on-records/020-preprocess-rules.md",
            (
                "docs/040-integration/additional-operations-on-records/030-advanced-mapping.code.md",
                dict(type="reference"),
            ),
        ],
    ),
    dict(
        section="ingest",
        sub="processing",
        title="Processing",
        slug="processing",
        nav_order=40,
        default_type="how-to",
        intro=(
            "Processing turns mapped records into data parts and golden records. Preview and "
            "validations let you check what will happen before you commit; approval puts a gate "
            "in front of it."
        ),
        pages=[
            "docs/040-integration/data-sources/190-process-data.md",
            "docs/040-integration/additional-operations-on-records/080-preview.md",
            "docs/040-integration/additional-operations-on-records/090-validations.md",
            "docs/040-integration/additional-operations-on-records/050-approval.md",
            "docs/040-integration/additional-operations-on-records/100-remove-records.md",
        ],
    ),
    dict(
        section="ingest",
        sub="troubleshooting",
        title="Troubleshoot ingestion",
        slug="troubleshooting",
        nav_order=50,
        default_type="how-to",
        intro=(
            "When records do not arrive, or arrive wrong, these are the three places to look: the "
            "quarantine holds records that failed validation, the logs say what the source did, "
            "and monitoring shows whether processing is keeping up."
        ),
        pages=[
            "docs/040-integration/additional-operations-on-records/040-quarantine.md",
            "docs/040-integration/additional-operations-on-records/060-logs.md",
            "docs/040-integration/additional-operations-on-records/070-monitoring.md",
        ],
    ),
    dict(
        section="ingest",
        sub="manual-data-entry",
        title="Manual data entry",
        slug="manual-data-entry",
        nav_order=60,
        default_type="how-to",
        index_from="docs/040-integration/210-manual-data-entry.md",
        intro=(
            "Some data has no source system - it lives in someone's head or a spreadsheet. A "
            "manual data entry project lets people add and maintain those records inside CluedIn "
            "with the same mapping and processing as any other source."
        ),
        pages=[
            "docs/040-integration/manual-data-entry/010-configure-a-manual-data-entry-project.md",
            "docs/040-integration/manual-data-entry/020-add-records-in-a-manual-data-entry-project.md",
            "docs/040-integration/manual-data-entry/030-manage-a-manual-data-entry-project.md",
        ],
    ),
    dict(
        section="ingest",
        sub="connectors",
        title="Connectors",
        slug="connectors",
        nav_order=70,
        default_type="concept",
        index_from="docs/040-integration/200-crawlers.md",
        intro=(
            "A connector crawls an external system and turns what it finds into clues. Use these "
            "pages to understand what crawling does and to install a connector.\n\n"
            "Building your own connector is developer work - see "
            "[Develop & APIs](/develop/integrations)."
        ),
        pages=[
            (
                "docs/040-integration/crawlers/010-introduction.md",
                dict(slug="about-integrations"),
            ),
            "docs/040-integration/crawlers/020-crawling.md",
            ("docs/040-integration/crawlers/100-install-integration.md", dict(type="how-to")),
            ("docs/040-integration/crawlers/130-using-agents.md", dict(type="how-to")),
        ],
    ),
    dict(
        section="ingest",
        sub="patterns",
        title="Ingestion patterns",
        slug="patterns",
        nav_order=80,
        default_type="how-to",
        intro=(
            "Worked patterns for feeding CluedIn from common parts of a modern data stack, and "
            "for the case where you have many systems rather than a few."
        ),
        pages=[
            "docs/200-kb/how-to/110-connect-fivetran-to-cluedin.md",
            "docs/200-kb/how-to/120-connect-dbt-to-cluedin.md",
            "docs/200-kb/how-to/130-connect-snowflake-to-cluedin.md",
            "docs/200-kb/how-to/140-connecting-a-large-amount-of-systems.md",
        ],
    ),
    # -----------------------------------------------------------------------
    # Model
    # -----------------------------------------------------------------------
    dict(
        section="model",
        sub=None,
        pages=[
            (
                "docs/110-key-terms-and-features/100-entity-codes.md",
                dict(type="concept", order=10, slug="identifiers"),
            ),
        ],
    ),
    dict(
        section="model",
        sub="business-domains",
        title="Business domains",
        slug="business-domains",
        nav_order=20,
        default_type="how-to",
        intro=(
            "A business domain says what kind of thing a record is - Customer, Product, "
            "Organization. It drives how records are searched, displayed, resolved and exported.\n\n"
            "Business domains were called *entity types* before the 2025.05 release."
        ),
        pages=[
            (
                "docs/110-key-terms-and-features/090-entity-type.md",
                dict(
                    title="Business domains explained",
                    slug="business-domains-explained",
                    type="concept",
                ),
            ),
            (
                "docs/080-management/040-entity-type.md",
                dict(title="Manage business domains", slug="manage-business-domains"),
            ),
        ],
    ),
    dict(
        section="model",
        sub="vocabularies",
        title="Vocabularies",
        slug="vocabularies",
        nav_order=30,
        default_type="how-to",
        intro=(
            "A vocabulary is the set of properties that describe records from a source or a "
            "business domain, and a vocabulary key is one of those properties. Mapping connects "
            "source columns to vocabulary keys, so the vocabulary is what makes data from "
            "different systems comparable."
        ),
        pages=[
            (
                "docs/110-key-terms-and-features/110-vocabularies.md",
                dict(
                    title="Vocabularies explained",
                    slug="vocabularies-explained",
                    type="concept",
                ),
            ),
            (
                "docs/080-management/data-catalog/020-vocabulary.md",
                dict(title="Create and manage vocabularies", slug="manage-vocabularies"),
            ),
            ("docs/080-management/data-catalog/030-vocabulary-keys.md", dict(type="concept")),
            "docs/080-management/data-catalog/040-manage-vocabulary-keys.md",
        ],
    ),
    dict(
        section="model",
        sub="data-catalog",
        title="Data catalog",
        slug="data-catalog",
        nav_order=40,
        default_type="reference",
        index_from="docs/080-management/030-data-catalog.md",
        intro=(
            "The data catalog is where every vocabulary, key and data type in your instance can "
            "be found and inspected. Start here when you need to know what already exists before "
            "adding to the model."
        ),
        pages=[
            ("docs/080-management/data-catalog/010-modeling-approaches.md", dict(type="concept")),
            ("docs/080-management/data-catalog/040-search-data-catalog.md", dict(type="how-to")),
            "docs/080-management/data-catalog/050-data-types.md",
            "docs/080-management/data-catalog/060-lookup-data-type.md",
            (
                "docs/200-kb/how-to/080-match-lookup-or-reference-data-automatically.md",
                dict(
                    title="Match reference and lookup data automatically",
                    slug="match-reference-data",
                    type="how-to",
                ),
            ),
            "docs/200-kb/kb1002-supported-characters.md",
        ],
    ),
    dict(
        section="model",
        sub="relationships",
        title="Relationships",
        slug="relationships",
        nav_order=50,
        default_type="concept",
        intro=(
            "Relationships - edges - connect one record to another: an employee to an "
            "organization, an order to a customer. They are part of the model, and they are what "
            "makes the graph in CluedIn navigable.\n\n"
            "For relationships as they appear on a golden record, see "
            "[Golden record relations](/master/golden-records/golden-record-relations)."
        ),
        pages=[
            (
                "docs/110-key-terms-and-features/130-edges.md",
                dict(title="Relationships (edges)", slug="edges"),
            ),
            (
                "docs/010-getting-started/090-relations.md",
                dict(
                    title="Tutorial: add relations between records",
                    slug="tutorial-add-relations",
                    type="tutorial",
                ),
            ),
        ],
    ),
    dict(
        section="model",
        sub="hierarchies",
        title="Hierarchies",
        slug="hierarchies",
        nav_order=60,
        default_type="how-to",
        index_from="docs/080-management/060-hierarchy-builder.md",
        intro=(
            "A hierarchy arranges golden records into a parent/child structure - a company and "
            "its subsidiaries, a product and its variants. The hierarchy builder is where you "
            "create and maintain them."
        ),
        pages=[
            ("docs/080-management/hierarchy-builder/010-concept-of-hierarchy.md", dict(type="concept")),
            "docs/080-management/hierarchy-builder/020-create-a-hierarchy.md",
            "docs/080-management/hierarchy-builder/030-work-in-a-hierarchy-project.md",
            "docs/080-management/hierarchy-builder/040-manage-hierarchies.md",
            (
                "docs/010-getting-started/070-hierarchy-builder.md",
                dict(
                    title="Tutorial: create hierarchies",
                    slug="tutorial-create-hierarchies",
                    type="tutorial",
                ),
            ),
            "docs/200-kb/how-to/040-build-org-hierarchy.md",
        ],
    ),
    # -----------------------------------------------------------------------
    # Master
    # -----------------------------------------------------------------------
    dict(
        section="master",
        sub=None,
        pages=[
            ("docs/110-key-terms-and-features/030-search.md", dict(type="how-to", order=80)),
            ("docs/110-key-terms-and-features/040-filters.md", dict(type="how-to", order=90)),
        ],
    ),
    dict(
        section="master",
        sub="golden-records",
        title="Golden records",
        slug="golden-records",
        nav_order=20,
        default_type="how-to",
        intro=(
            "How to work with golden records once they exist: see what they are connected to, "
            "read their history, understand why a value was chosen, and remove records or "
            "individual data parts.\n\n"
            "For what a golden record is, see "
            "[Core concepts](/get-started/core-concepts/golden-records)."
        ),
        pages=[
            "docs/110-key-terms-and-features/golden-records/010-golden-record-relations.md",
            ("docs/110-key-terms-and-features/golden-records/020-history.md", dict(type="concept")),
            ("docs/110-key-terms-and-features/golden-records/030-explain-log.md", dict(type="concept")),
            "docs/110-key-terms-and-features/golden-records/040-delete-golden-record.md",
            "docs/110-key-terms-and-features/golden-records/050-delete-individual-data-parts.md",
            "docs/200-kb/how-to/070-undo-or-rollback-changes.md",
        ],
    ),
    dict(
        section="master",
        sub="deduplication",
        title="Deduplication",
        slug="deduplication",
        nav_order=30,
        default_type="how-to",
        index_from="docs/080-management/020-deduplication.md",
        intro=(
            "Deduplication is how CluedIn finds records that describe the same thing and merges "
            "them. A deduplication project defines the matching logic, groups the candidates, and "
            "hands the ambiguous ones to a steward to decide."
        ),
        pages=[
            ("docs/080-management/deduplication/010-concept-of-deduplication.md", dict(type="concept")),
            ("docs/080-management/deduplication/020-deduplication-in-practice.md", dict(type="concept")),
            "docs/080-management/deduplication/030-create-deduplication-project.md",
            "docs/080-management/deduplication/040-manage-a-deduplication-project.md",
            "docs/080-management/deduplication/050-manage-groups-of-duplicates.md",
            ("docs/080-management/deduplication/060-deduplication-reference.md", dict(type="reference")),
            (
                "docs/010-getting-started/040-deduplication.md",
                dict(
                    title="Tutorial: deduplicate data",
                    slug="tutorial-deduplicate-data",
                    type="tutorial",
                ),
            ),
            ("docs/200-kb/how-to/160-best-practices-for-matching-and-merging.md", dict(type="concept")),
            "docs/200-kb/kb0018-how-can-I-get-better-matches.md",
        ],
    ),
]
