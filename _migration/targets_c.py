"""Routing table, part 3: Develop & APIs, Solutions & integrations, Learning
paths, Playbooks, Troubleshooting, Release notes, Archive, and the standalone
pages.

The archive takes material the repository itself already marks as retired -
pages inside `outdated/` and `legacy/` folders, and the two whole sections
(`090-development`, `100-user-interface`) in which every single page carries
`published: false`. Nothing is archived on a guess about whether it is still
accurate.
"""

from ia import g

TARGETS = [
    # -----------------------------------------------------------------------
    # Develop & APIs
    # -----------------------------------------------------------------------
    dict(
        section="develop",
        sub=None,
        pages=[
            (
                "docs/050-preparation/enricher/180-build-enricher.md",
                dict(type="how-to", order=30),
            ),
        ],
    ),
    dict(
        section="develop",
        sub="python-sdk",
        title="Python SDK",
        slug="python-sdk",
        nav_order=10,
        default_type="how-to",
        intro=(
            "The Python SDK is the fastest way to script CluedIn: query golden records, push data "
            "in, pull data out, and automate the operations you would otherwise click through."
        ),
        pages=[
            ("docs/210-playbooks/data-engineering/010-python-sdk.md", dict(type="reference")),
            "docs/210-playbooks/data-engineering/020-search.md",
            "docs/210-playbooks/data-engineering/030-automation.md",
            "docs/210-playbooks/data-engineering/040-ingestion.md",
            "docs/210-playbooks/data-engineering/050-export.md",
            ("docs/210-playbooks/data-engineering/060-magic.md", dict(type="reference")),
        ],
    ),
    dict(
        section="develop",
        sub="integrations",
        title="Build integrations",
        slug="integrations",
        nav_order=20,
        default_type="how-to",
        intro=(
            "Writing your own connector so CluedIn can crawl a system it does not support out of "
            "the box.\n\n"
            "Installing and running connectors is covered in [Ingest](/ingest/connectors)."
        ),
        pages=[
            "docs/040-integration/crawlers/080-build-integration.md",
            ("docs/040-integration/crawlers/090-delta-crawls.md", dict(type="concept")),
            ("docs/040-integration/crawlers/030-robust-integrations.md", dict(type="concept")),
            (
                "docs/040-integration/crawlers/140-crawler-validation-framework.md",
                dict(type="reference"),
            ),
        ],
    ),
    dict(
        section="develop",
        sub="api-reference",
        title="API reference",
        slug="api",
        abs_permalink="/api",
        nav_order=40,
        default_type="reference",
        index_from="docs/250-rest-api/020-api-reference.md",
        intro=(
            "The REST API is generated from CluedIn's OpenAPI specification and covers more than "
            "a thousand endpoints, grouped below by the part of the product they act on."
        ),
        pages=[
            (
                "docs/250-rest-api/010-get-started.md",
                dict(
                    title="Get started with the REST API",
                    slug="get-started",
                    type="how-to",
                    order=5,
                ),
            ),
            "docs/250-rest-api/020-api-reference/020-access-control-and-governance.md",
            "docs/250-rest-api/020-api-reference/030-entities.md",
            "docs/250-rest-api/020-api-reference/040-search.md",
            "docs/250-rest-api/020-api-reference/050-vocabularies.md",
            "docs/250-rest-api/020-api-reference/060-glossary.md",
            "docs/250-rest-api/020-api-reference/070-hierarchies.md",
            "docs/250-rest-api/020-api-reference/075-deduplication.md",
            "docs/250-rest-api/020-api-reference/080-rules-and-evaluation.md",
            "docs/250-rest-api/020-api-reference/100-streams-and-export.md",
            "docs/250-rest-api/020-api-reference/110-data-preparation-and-enrichment.md",
            "docs/250-rest-api/020-api-reference/130-ai.md",
            "docs/250-rest-api/020-api-reference/140-administration-and-configuration.md",
            "docs/250-rest-api/020-api-reference/150-organization.md",
        ],
    ),
    # -----------------------------------------------------------------------
    # Solutions & integrations
    # -----------------------------------------------------------------------
    dict(
        section="solutions",
        sub=None,
        pages=[
            ("docs/180-microsoft-integration/050-event-hub.md", dict(type="how-to", order=80)),
            ("docs/180-microsoft-integration/060-open-ai.md", dict(type="how-to", order=85)),
            ("docs/180-microsoft-integration/090-excel-add-in.md", dict(type="how-to", order=90)),
        ],
    ),
    dict(
        section="solutions",
        sub="purview",
        title="Microsoft Purview",
        slug="purview",
        nav_order=10,
        default_type="how-to",
        index_from="docs/180-microsoft-integration/020-purview.md",
        intro=(
            "CluedIn and Purview cover different halves of the same problem: Purview catalogues "
            "and governs metadata, CluedIn masters the data itself. These guides keep the two in "
            "step."
        ),
        pages=[
            (
                "docs/180-microsoft-integration/purview/010-intro.md",
                dict(title="Purview integration features", slug="features", type="concept"),
            ),
            "docs/180-microsoft-integration/purview/010-purview-pre-configuration-guide.md",
            "docs/180-microsoft-integration/purview/020-setup-permissions.md",
            "docs/180-microsoft-integration/purview/020-purview-configuration.guide.md",
            "docs/180-microsoft-integration/purview/030-sync-data-sources.md",
            "docs/180-microsoft-integration/purview/040-azure-data-factory-pipeline-automation.md",
            "docs/180-microsoft-integration/purview/041-data-factory-pipeline-run-schedule.md",
            "docs/180-microsoft-integration/purview/050-sync-manual-data-entry-to-purview.md",
            "docs/180-microsoft-integration/purview/060-sync-processing-rules-to-purview.md",
            "docs/180-microsoft-integration/purview/070-sync-clean-projects-to-purview.md",
            "docs/180-microsoft-integration/purview/080-sync-deduplication-projects-to-purview.md",
            "docs/180-microsoft-integration/purview/090-sync-streams-to-purview.md",
            "docs/180-microsoft-integration/purview/100-sync-purview-glossaries-to-cluedin-glossaries.md",
            "docs/180-microsoft-integration/purview/110-sync-purview-glossaries-to-cluedin-vocabularies.md",
            "docs/180-microsoft-integration/purview/120-sync-data-products.md",
        ],
    ),
    dict(
        section="solutions",
        sub="power-apps",
        title="Power Apps",
        slug="power-apps",
        nav_order=20,
        default_type="how-to",
        index_from="docs/180-microsoft-integration/010-powerapps.md",
        intro=(
            "Surfacing CluedIn golden records inside Power Apps and Dataverse, and pushing changes "
            "made there back into CluedIn."
        ),
        pages=[
            "docs/180-microsoft-integration/powerapps/010-power-apps-pre-configuration-guide.md",
            "docs/180-microsoft-integration/powerapps/010-setup-credentials.md",
            "docs/180-microsoft-integration/powerapps/020-setup-connections.md",
            "docs/180-microsoft-integration/powerapps/020-power-apps-configuration-guide.md",
            (
                "docs/180-microsoft-integration/powerapps/030-features.md",
                dict(title="Power Apps features", slug="features", type="concept"),
            ),
            (
                "docs/180-microsoft-integration/powerapps/040-external-features.md",
                dict(title="Power Apps external features", slug="external-features", type="concept"),
            ),
            "docs/180-microsoft-integration/powerapps/020-features/010-sync-entitytypes-to-dataverse.md",
            "docs/180-microsoft-integration/powerapps/020-features/020-sync-dataverse-to-cluedin.md",
            "docs/180-microsoft-integration/powerapps/020-features/030-create-ingestion-endpoint-workflow.md",
            "docs/180-microsoft-integration/powerapps/020-features/040-create-batch-approval-worrkflow.md",
            (
                "docs/180-microsoft-integration/powerapps/020-features/050-create-streams.md",
                dict(title="Create streams from Power Apps", slug="create-streams"),
            ),
        ],
    ),
    dict(
        section="solutions",
        sub="power-automate",
        title="Power Automate",
        slug="power-automate",
        nav_order=30,
        default_type="how-to",
        index_from="docs/180-microsoft-integration/010-power-automate.md",
        intro="Triggering Power Automate flows from CluedIn, and calling CluedIn from a flow.",
        pages=[
            "docs/180-microsoft-integration/power-automate/010-power-automate-pre-configuration-guide.md",
            "docs/180-microsoft-integration/power-automate/020-power-automate-configuration-guide.md",
            "docs/180-microsoft-integration/power-automate/030-power-automate-post-configuration-guide.md",
            "docs/180-microsoft-integration/power-automate/040-power-automate-private-network.md",
        ],
    ),
    dict(
        section="solutions",
        sub="fabric",
        title="Microsoft Fabric",
        slug="fabric",
        nav_order=40,
        default_type="how-to",
        index_from="docs/180-microsoft-integration/040-fabric.md",
        intro=(
            "Moving data between CluedIn and Fabric in both directions, and running CluedIn rules "
            "against data that lives in Fabric."
        ),
        pages=[
            "docs/180-microsoft-integration/fabric/010-connect-cluedin-to-fabric.md",
            "docs/180-microsoft-integration/fabric/020-connect-fabric-to-cluedin.md",
            "docs/180-microsoft-integration/fabric/030-use-cluedin-rules-in-fabric.md",
            "docs/180-microsoft-integration/fabric/040-use-cluedin-fabric-workload.md",
        ],
    ),
    dict(
        section="solutions",
        sub="azure-data-factory",
        title="Azure Data Factory",
        slug="azure-data-factory",
        nav_order=50,
        default_type="how-to",
        index_from="docs/180-microsoft-integration/070-adf.md",
        intro="Using Data Factory pipelines to move data into and out of CluedIn.",
        pages=[
            "docs/180-microsoft-integration/azure-data-factory/001-adf-with-private-link.md",
            "docs/180-microsoft-integration/azure-data-factory/002-copy-data-activity.md",
            "docs/180-microsoft-integration/azure-data-factory/003-data-flow-activity.md",
        ],
    ),
    dict(
        section="solutions",
        sub="master-data-services",
        title="Master Data Services",
        slug="master-data-services",
        nav_order=60,
        default_type="how-to",
        index_from="docs/180-microsoft-integration/080-mds-configuration.md",
        intro=(
            "Connecting CluedIn to SQL Server Master Data Services, either directly or through "
            "Azure Relay.\n\n"
            "If you are migrating away from MDS rather than integrating with it, see the "
            "[MDS to CluedIn use case](/solutions/use-cases)."
        ),
        pages=[
            "docs/180-microsoft-integration/mds/010-direct-connection.md",
            "docs/180-microsoft-integration/mds/020-azure-relay.md",
        ],
    ),
    dict(
        section="solutions",
        sub="copilot",
        title="Copilot",
        slug="copilot",
        nav_order=70,
        default_type="how-to",
        index_from="docs/180-microsoft-integration/030-copilot.md",
        intro="Asking questions about your golden records in natural language through Copilot.",
        pages=[
            "docs/180-microsoft-integration/copilot/010-get-access-to-copilot.md",
            "docs/180-microsoft-integration/copilot/020-work-with-copilot.md",
        ],
    ),
    dict(
        section="solutions",
        sub="use-cases",
        title="Use cases",
        slug="use-cases",
        nav_order=100,
        default_type="concept",
        index_from="docs/230-usecases/001-usecases-summary.md",
        intro=(
            "End-to-end walkthroughs of a business problem: what the data looks like going in, "
            "what CluedIn does to it, and what comes out the other side."
        ),
        pages=[
            "docs/230-usecases/customer360/001-customer-sources.md",
            "docs/230-usecases/supplier360/001-sources.md",
            "docs/230-usecases/master-data-management-for-product-data/001-product-data.md",
            "docs/230-usecases/centralised-master-data-management/001-centralised-mdm.md",
            "docs/230-usecases/data-quality-management/001-sources.md",
            "docs/230-usecases/reference-data-management/001-customer-sources.md",
            "docs/230-usecases/householding/001-customer-sources.md",
            "docs/230-usecases/customer-onboarding-acceleration/001-customer-sources.md",
            "docs/230-usecases/data-integration-for-analytics/001-customer-sources.md",
            "docs/230-usecases/helping-with-erp-migration/001-customer-sources.md",
            "docs/230-usecases/regulatory-compliance/001-customer-sources.md",
            (
                "docs/230-usecases/mds-to-cluedin/01-mds-to-cluedin-why-and-how.md",
                dict(title="MDS to CluedIn: why and how", slug="mds-to-cluedin-1"),
            ),
            (
                "docs/230-usecases/mds-to-cluedin/02-mds-to-cluedin-adoption-and-mindset.md",
                dict(title="MDS to CluedIn: adoption and mindset", slug="mds-to-cluedin-2"),
            ),
            (
                "docs/230-usecases/mds-to-cluedin/03-mds-to-cluedin-faq-mapping.md",
                dict(title="MDS to CluedIn: FAQ and worked example", slug="mds-to-cluedin-3"),
            ),
        ],
    ),
    # -----------------------------------------------------------------------
    # Learning paths
    # -----------------------------------------------------------------------
    dict(
        section="learning",
        sub="data-steward-course",
        title="Data Steward course",
        slug="data-steward",
        nav_order=10,
        default_type="tutorial",
        index_from="docs/120-learning-paths/010-data-steward-course.md",
        intro=(
            "For the person who reviews, corrects and approves data every day. The course follows "
            "one operating loop: find the records, judge them, fix them, and hand the rest on."
        ),
        pages=g("docs/120-learning-paths/data-steward-course/*.md"),
    ),
    dict(
        section="learning",
        sub="data-architect-course",
        title="Data Architect course",
        slug="data-architect",
        nav_order=20,
        default_type="tutorial",
        index_from="docs/120-learning-paths/020-data-architect-course.md",
        intro=(
            "For the person who decides how CluedIn is set up: the model, the ingestion design, "
            "the matching strategy, and the path from development to production."
        ),
        pages=g(
            "docs/120-learning-paths/data-architect-course/*.md",
            exclude=("docs/120-learning-paths/data-architect-course/120-capstone-architecture-review.md",),
        )
        + [
            (
                "docs/120-learning-paths/data-architect-course/120-capstone-architecture-review.md",
                dict(
                    title="Capstone: architecture review",
                    slug="capstone-architecture-review",
                    order=200,
                ),
            )
        ],
    ),
    dict(
        section="learning",
        sub="fundamentals",
        title="CluedIn fundamentals",
        slug="fundamentals",
        nav_order=30,
        default_type="tutorial",
        index_from="docs/220-training/001-fundamentals.md",
        intro=(
            "The base training course: get data in, build a single view of a customer, and spot "
            "what is wrong with it."
        ),
        pages=g("docs/220-training/fundamentals/*.md"),
    ),
    dict(
        section="learning",
        sub="ai-training",
        title="AI in CluedIn",
        slug="ai",
        nav_order=40,
        default_type="tutorial",
        index_from="docs/220-training/002-ai.md",
        intro=(
            "Where AI fits in CluedIn: agents that do stewardship work, the AI enricher, and "
            "Copilot - each with a demo you can follow."
        ),
        pages=g("docs/220-training/ai/*.md"),
    ),
    dict(
        section="learning",
        sub="role-handbooks",
        title="Role handbooks",
        slug="role-handbooks",
        nav_order=50,
        default_type="tutorial",
        intro=(
            "One condensed handbook per role: what you are responsible for, what you touch in the "
            "product, and the order to learn it in."
        ),
        pages=[
            # The subtitle each handbook carried ("- field guide", "- build & operate
            # handbook") is dropped from the title: it made every entry in this list
            # too long to scan, and says nothing the role name does not.
            (
                "docs/220-training/CluedIn for Data Stewards/010-get-live-in-14-days.md",
                dict(title="CluedIn for Data Stewards"),
            ),
            (
                "docs/220-training/CluedIn for Data Modellers/010-get-live-in-14-days.md",
                dict(title="CluedIn for Data Modellers"),
            ),
            (
                "docs/220-training/CluedIn for Data Engineers/010-get-live-in-14-days.md",
                dict(title="CluedIn for Data Engineers"),
            ),
            (
                "docs/220-training/CluedIn for Data Governance Managers/010-get-live-in-14-days.md",
                dict(title="CluedIn for Data Governance Managers"),
            ),
            (
                "docs/220-training/CluedIn for Administrators/010-get-live-in-14-days.md",
                dict(title="CluedIn for Administrators"),
            ),
            (
                "docs/220-training/CluedIn for Solution Architects/010-get-live-in-14-days.md",
                dict(title="CluedIn for Solution Architects"),
            ),
            (
                "docs/220-training/CluedIn for System Integrators/010-get-live-in-14-days.md",
                dict(title="CluedIn for System Integrators"),
            ),
            (
                "docs/220-training/CluedIn for Developers/010-get-live-in-14-days.md",
                dict(title="CluedIn for Developers"),
            ),
        ],
    ),
    # -----------------------------------------------------------------------
    # Playbooks
    # -----------------------------------------------------------------------
    dict(
        section="playbooks",
        sub=None,
        pages=[
            ("docs/210-playbooks/007-data-transformation-playbook.md", dict(order=60)),
            ("docs/210-playbooks/008-data-export-playbook.md", dict(order=70)),
            ("docs/210-playbooks/110-resources-for-data-steward.md", dict(order=80, type="reference")),
            (
                "docs/220-training/Get Live in 14 Days/010-get-live-in-14-days.md",
                dict(order=90, slug="go-live-in-14-days"),
            ),
            (
                "docs/220-training/Taking the AI Approach to CluedIn/010-get-live-in-14-days.md",
                dict(order=95, slug="implement-cluedin-with-ai"),
            ),
        ],
    ),
    dict(
        section="playbooks",
        sub="project-delivery",
        title="Project delivery",
        slug="project-delivery",
        nav_order=10,
        default_type="concept",
        intro=(
            "How to scope and run a CluedIn project: what to decide before you start, how to "
            "sequence the work, and what has to be true before you go to production."
        ),
        pages=[
            "docs/210-playbooks/001-before-you-start.md",
            "docs/210-playbooks/002-how-to-approach-cluedin-project.md",
            "docs/210-playbooks/003-prepare-for-cluedin-project.md",
            "docs/210-playbooks/004-start-your-cluedin-project.md",
            "docs/210-playbooks/005-start-your-it-journey.md",
            "docs/210-playbooks/009-release-to-production-playbook.md",
            (
                "docs/210-playbooks/130-vendorvsclientRACIexample.md",
                dict(title="Example RACI matrix", slug="raci-example", type="reference"),
            ),
        ],
    ),
    dict(
        section="playbooks",
        sub="data-ingestion",
        title="Data ingestion playbook",
        slug="data-ingestion",
        nav_order=20,
        default_type="concept",
        index_from="docs/210-playbooks/006-data-ingestion-playbook.md",
        intro=(
            "How to decide what to ingest and in what order. For the mechanics of doing it, see "
            "[Ingest](/ingest)."
        ),
        pages=[
            "docs/210-playbooks/data-ingestion/001-data-impact-workshop.md",
            "docs/210-playbooks/data-ingestion/002-pick-the-right-tool.md",
            (
                "docs/210-playbooks/data-ingestion/003-ingest-data.md",
                dict(title="Plan the ingestion", slug="plan-the-ingestion"),
            ),
            (
                "docs/210-playbooks/data-ingestion/004-concept-of-mapping.md",
                dict(title="Plan the mapping", slug="plan-the-mapping"),
            ),
            (
                "docs/210-playbooks/data-ingestion/005-process-data.md",
                dict(title="Plan the processing", slug="plan-the-processing"),
            ),
        ],
    ),
    dict(
        section="playbooks",
        sub="data-engineering",
        title="Data engineering playbook",
        slug="data-engineering",
        nav_order=30,
        default_type="concept",
        index_from="docs/210-playbooks/100-data-engineering-playbook.md",
        intro=(
            "Where CluedIn sits in a wider data architecture, and how far you should extend it "
            "before you should build around it."
        ),
        pages=[
            "docs/210-playbooks/data-engineering/001-cluedin-in-your-data-architecture.md",
            "docs/210-playbooks/data-engineering/002-extending-cluedin-with-ms-integrations.md",
            "docs/210-playbooks/data-engineering/003-customization-in-cluedin.md",
        ],
    ),
    # -----------------------------------------------------------------------
    # Troubleshooting
    # -----------------------------------------------------------------------
    dict(
        section="troubleshooting",
        sub=None,
        default_type="troubleshooting",
        pages=[
            ("docs/200-kb/kb0016-slow-processing-slow-performancemd.md", dict(order=10)),
            ("docs/200-kb/kb0013-my-rules-are-processing-slowly.md", dict(order=20)),
            ("docs/200-kb/kb0014-why-are-my-rules-not-working.md", dict(order=30)),
            ("docs/200-kb/kb0003-elastic-index-rebuild.md", dict(order=40)),
            ("docs/200-kb/kb0017-why-can-I-not-delete-this.md", dict(order=50)),
            ("docs/200-kb/kb0015-the-product-toolkit-is-failing-to-export-or-import.md", dict(order=60)),
        ],
    ),
    # -----------------------------------------------------------------------
    # Release notes
    # -----------------------------------------------------------------------
    dict(
        section="release",
        sub=None,
        default_type="reference",
        index_from="docs/170-release-notes.md",
        pages=[
            ("docs/160-release/006-release-2026-02.md", dict(order=10)),
            ("docs/160-release/005-release-2026-01.md", dict(order=20)),
            ("docs/160-release/004-release-2025-09.md", dict(order=30)),
            ("docs/160-release/002-release-2025-05.md", dict(order=40)),
            ("docs/160-release/001-release-2024-12.md", dict(order=50)),
            ("docs/160-release/003-terminology-changes.md", dict(order=60)),
            ("docs/200-kb/kb0008-platform-versioning.md", dict(order=70)),
        ],
    ),
    # -----------------------------------------------------------------------
    # Archive
    # -----------------------------------------------------------------------
    dict(
        section="archive",
        sub="legacy-development",
        title="Legacy development documentation",
        slug="legacy-development",
        nav_order=10,
        default_type="reference",
        intro=(
            "Developer documentation for earlier versions of the platform. Every page in this set "
            "already carried `published: false` in the source repository, so none of it was on "
            "the live site. It is kept here until it can be rewritten against the current "
            "platform or deleted.\n\n"
            "Current developer material is in [Develop & APIs](/develop)."
        ),
        pages=g("docs/090-development/*.md"),
    ),
    dict(
        section="archive",
        sub="legacy-user-interface",
        title="Legacy user interface documentation",
        slug="legacy-user-interface",
        nav_order=20,
        default_type="reference",
        intro=(
            "Descriptions of the CluedIn interface from before the 2025.05 terminology change, "
            "when golden records were called entities. All of these pages carried "
            "`published: false`, and each has been superseded: golden record pages by "
            "[Master](/master/golden-records), search by [Search](/master/search)."
        ),
        pages=g("docs/100-user-interface/*.md"),
    ),
    dict(
        section="archive",
        sub="unsupported-features",
        title="Unsupported features",
        slug="unsupported-features",
        nav_order=30,
        default_type="reference",
        intro=(
            "Features that were documented but are no longer supported. These pages come from "
            "folders the repository itself named `outdated`."
        ),
        pages=g("docs/070-governance/outdated/*.md")
        + g("docs/050-preparation/outdated/*.md")
        + g("docs/150-consume/outdated/*.md")
        + [
            (
                "docs/080-management/030-modelling.md",
                dict(title="Modelling (superseded)", slug="modelling"),
            )
        ],
    ),
    dict(
        section="archive",
        sub="historical-operations",
        title="Historical operations",
        slug="historical-operations",
        nav_order=40,
        default_type="reference",
        intro=(
            "Operational runbooks kept for installations that have not yet been upgraded, and "
            "superseded drafts. Current runbooks are in "
            "[Backup and restore](/operate/backup-and-restore)."
        ),
        pages=[
            (
                "docs/190-paas-operations/backup-and-restore/legacy/011-disaster-recovery-runbook-legacy.md",
                dict(slug="disaster-recovery-runbook-pre-2025-09"),
            ),
            (
                "docs/190-paas-operations/_002-backup-and-restore.md",
                dict(title="Backup and restore (superseded draft)", slug="backup-and-restore-draft"),
            ),
        ],
    ),
]

# ---------------------------------------------------------------------------
# Standalone pages: kept at the root of the site and excluded from navigation.
# ---------------------------------------------------------------------------

STANDALONE = [
    dict(
        source="docs/240-terms-of-service.md",
        dest="terms-of-service.md",
        permalink="/terms-of-service",
        type="reference",
    ),
    dict(
        source="docs/tag.md",
        dest="tag.md",
        permalink="/tag",
        type=None,
    ),
]

# ---------------------------------------------------------------------------
# Old landing pages that exist only to hold a card grid. Their children are now
# reachable from the generated section index, so the pages themselves are not
# migrated. Listed explicitly so the migration report can account for every
# source file rather than silently dropping some.
# ---------------------------------------------------------------------------

REPLACED_BY_SECTION_INDEX = [
    "docs/010-getting-started.md",
    "docs/020-deployment.md",
    "docs/030-administration.md",
    "docs/030-key-terms-and-features.md",
    "docs/040-integration.md",
    "docs/050-preparation.md",
    "docs/070-governance.md",
    "docs/080-management.md",
    "docs/090-development.md",
    "docs/100-user-interface.md",
    "docs/120-learning-paths/000-learning-paths.md",
    "docs/150-consume.md",
    "docs/180-microsoft-integration.md",
    "docs/190-paas-operations.md",
    "docs/200-kb.md",
    "docs/210-playbooks.md",
    "docs/220-training.md",
    "docs/230-usecases.md",
    "docs/250-rest-api.md",
    "docs/040-integration/180-additional-operations-on-records.md",
]
