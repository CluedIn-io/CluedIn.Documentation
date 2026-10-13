"""Routing table, part 2: Govern & improve, Publish & consume, Administer,
Deploy & operate.

Administration and operations are deliberately kept apart. Administration is
what an administrator does inside the product; operations is what a platform
team does to the installation. They have different audiences and almost no
overlapping readers.
"""

from ia import g

TARGETS = [
    # -----------------------------------------------------------------------
    # Govern & improve
    # -----------------------------------------------------------------------
    dict(
        section="govern",
        sub=None,
        pages=[
            (
                "docs/010-getting-started/080-glossary.md",
                dict(
                    title="Work with the glossary",
                    slug="work-with-glossary",
                    type="how-to",
                    order=10,
                ),
            ),
            (
                "docs/200-kb/how-to/050-set-retention-on-data.md",
                dict(type="how-to", order=90),
            ),
        ],
    ),
    dict(
        section="govern",
        sub="cleaning",
        title="Cleaning",
        slug="cleaning",
        nav_order=20,
        default_type="how-to",
        index_from="docs/050-preparation/001-clean.md",
        intro=(
            "A clean project takes a set of golden records, shows you what is wrong with them, "
            "and lets you fix it in bulk. Use it for the problems that keep coming back - "
            "inconsistent addresses, mixed date formats, values in the wrong field."
        ),
        pages=[
            "docs/050-preparation/clean/010-create-clean-project.md",
            "docs/050-preparation/clean/020-manage-clean-project.md",
            ("docs/050-preparation/clean/030-clean-reference.md", dict(type="reference")),
            ("docs/050-preparation/clean/040-clean-application-reference.md", dict(type="reference")),
            (
                "docs/050-preparation/clean/050-processing-logic-in-clean-projects.md",
                dict(type="concept"),
            ),
            (
                "docs/010-getting-started/030-manual-data-cleaning.md",
                dict(
                    title="Tutorial: clean data",
                    slug="tutorial-clean-data",
                    type="tutorial",
                ),
            ),
            "docs/200-kb/how-to/010-fix-address-data.md",
            "docs/200-kb/how-to/030-standardize-dates.md",
        ],
    ),
    dict(
        section="govern",
        sub="enrichment",
        title="Enrichment",
        slug="enrichment",
        nav_order=30,
        default_type="reference",
        index_from="docs/050-preparation/002-enricher.md",
        intro=(
            "An enricher fills gaps in your data from an external source - a company register, a "
            "mapping service, a search index. Start with the concept and the reference, then pick "
            "the provider you need.\n\n"
            "Writing your own enricher is developer work - see "
            "[Develop & APIs](/develop/extensions)."
        ),
        pages=[
            ("docs/050-preparation/enricher/010-concept-of-enricher.md", dict(type="concept")),
            ("docs/050-preparation/enricher/020-add-enricher.md", dict(type="how-to")),
            "docs/050-preparation/enricher/030-enricher-reference.md",
            "docs/050-preparation/enricher/040-brreg.md",
            "docs/050-preparation/enricher/050-clearbit.md",
            "docs/050-preparation/enricher/060-companies-house.md",
            "docs/050-preparation/enricher/070-cvr.md",
            "docs/050-preparation/enricher/080-duckduckgo.md",
            "docs/050-preparation/enricher/090-gleif.md",
            "docs/050-preparation/enricher/110-google-maps.md",
            "docs/050-preparation/enricher/210-google-images.md",
            "docs/050-preparation/enricher/120-knowledge-graph.md",
            "docs/050-preparation/enricher/130-libpostal.md",
            "docs/050-preparation/enricher/140-open-corporates.md",
            "docs/050-preparation/enricher/150-permid.md",
            "docs/050-preparation/enricher/160-vatlayer.md",
            "docs/050-preparation/enricher/220-bvd.md",
            (
                "docs/050-preparation/enricher/170-web.md",
                dict(title="Web enricher", slug="web"),
            ),
            (
                "docs/050-preparation/enricher/190-artificial-intelligence.md",
                dict(title="AI enricher", slug="artificial-intelligence"),
            ),
            (
                "docs/050-preparation/enricher/200-rest-api.md",
                dict(title="REST API enricher", slug="rest-api"),
            ),
        ],
    ),
    dict(
        section="govern",
        sub="rules",
        title="Rules",
        slug="rules",
        nav_order=40,
        default_type="how-to",
        index_from="docs/080-management/010-rules.md",
        intro=(
            "Rules apply logic to your data automatically: change a value, add a tag, block a "
            "change. There are three kinds - pre-process rules act during ingestion, data part "
            "rules act on individual source records, and golden record rules act on the merged "
            "result.\n\n"
            "Start with [Rule types](/govern/rules/rule-types) to work out which kind you need."
        ),
        pages=[
            ("docs/080-management/rules/010-rule-types.md", dict(type="reference")),
            "docs/080-management/rules/020-create-rule.md",
            "docs/080-management/rules/030-manage-rules.md",
            ("docs/080-management/rules/040-rules-reference.md", dict(type="reference")),
            ("docs/080-management/rules/040-power-fx-formulas-in-rules.md", dict(type="reference")),
            ("docs/080-management/rules/050-best-practices-for-rules.md", dict(type="concept")),
            (
                "docs/010-getting-started/060-rule-builder.md",
                dict(
                    title="Tutorial: create rules",
                    slug="tutorial-create-rules",
                    type="tutorial",
                ),
            ),
            (
                "docs/200-kb/how-to/090-rules-that-work-across-business-domains.md",
                dict(
                    title="Write rules across business domains",
                    slug="rules-across-business-domains",
                ),
            ),
            ("docs/200-kb/kb0009-cel.md", dict(type="reference")),
        ],
    ),
    dict(
        section="govern",
        sub="tags",
        title="Tags",
        slug="tags",
        nav_order=50,
        default_type="how-to",
        intro=(
            "Tags are labels you attach to golden records and data parts. They do not overwrite "
            "anything - they classify, so that rules, filters, streams and reports can act on the "
            "classification."
        ),
        pages=[
            ("docs/070-governance/010-tag-monitoring.md", dict(type="concept")),
            (
                "docs/200-kb/how-to/060-working-with-tags-with-golden-record-or-data-part-rules.md",
                dict(title="Use tags with rules", slug="use-tags-with-rules"),
            ),
            "docs/200-kb/how-to/020-tag-records-with-data-quality-issues.md",
        ],
    ),
    dict(
        section="govern",
        sub="ai-agents",
        title="AI agents",
        slug="ai-agents",
        nav_order=60,
        default_type="how-to",
        index_from="docs/080-management/070-ai-agents.md",
        intro=(
            "AI agents do stewardship work for you - proposing fixes for quality problems, "
            "suggesting duplicates to merge, drafting rules. Everything an agent does is "
            "reviewable and revertible, so start with the prerequisites and the review workflow "
            "before turning one loose."
        ),
        pages=[
            (
                "docs/080-management/ai-agents/010-prerequisites-to-using-ai-agents.md",
                dict(type="reference"),
            ),
            ("docs/080-management/ai-agents/020-built-in-ai-agents.md", dict(type="reference")),
            "docs/080-management/ai-agents/030-create-configure-and-run-an-ai-agent.md",
            "docs/080-management/ai-agents/040-review-the-results-returned-by-an-ai-agent.md",
            "docs/080-management/ai-agents/050-view-and-revert-changes-made-by-ai-agent.md",
            ("docs/080-management/ai-agents/060-ai-agents-faqs.md", dict(type="reference")),
        ],
    ),
    dict(
        section="govern",
        sub="workflows",
        title="Workflows",
        slug="workflows",
        nav_order=70,
        default_type="how-to",
        index_from="docs/110-workflow.md",
        intro=(
            "A workflow puts an approval step in front of a change, so that edits to golden "
            "records are reviewed before they take effect."
        ),
        pages=[
            ("docs/130-workflow.md/010-concept-of-approvals.md", dict(type="concept")),
            ("docs/130-workflow.md/020-prerequisites.md", dict(type="reference")),
            "docs/130-workflow.md/030-create-and-manage-workflows.md",
            "docs/130-workflow.md/040-manage-approval-requests.md",
        ],
    ),
    # -----------------------------------------------------------------------
    # Publish & consume
    # -----------------------------------------------------------------------
    dict(
        section="publish",
        sub="streams",
        title="Streams",
        slug="streams",
        nav_order=20,
        default_type="how-to",
        index_from="docs/150-consume/002-streams.md",
        intro=(
            "A stream is a continuous export: you define which golden records and which "
            "properties, point it at an [export target](/publish/export-targets), and CluedIn "
            "keeps the target up to date as the data changes."
        ),
        pages=[
            ("docs/150-consume/streams/010-concept-of-a-stream.md", dict(type="concept")),
            "docs/150-consume/streams/010-create-a-stream.md",
            "docs/150-consume/streams/020-manage-streams.md",
            ("docs/150-consume/streams/030-stream-reference.md", dict(type="reference")),
            "docs/150-consume/streams/040-stream-logs.md",
            (
                "docs/010-getting-started/050-data-streaming.md",
                dict(
                    title="Tutorial: stream data",
                    slug="tutorial-stream-data",
                    type="tutorial",
                ),
            ),
        ],
    ),
    dict(
        section="publish",
        sub="export-targets",
        title="Export targets",
        slug="export-targets",
        nav_order=30,
        default_type="reference",
        index_from="docs/150-consume/040-export-targets.md",
        intro=(
            "An export target is the destination a [stream](/publish/streams) writes to. Each "
            "connector below documents its configuration, its data shape, and its limits."
        ),
        pages=[
            "docs/150-consume/export-targets/010-connector-reference.md",
            "docs/150-consume/export-targets/020-adl-connector.md",
            "docs/150-consume/export-targets/030-dedicated-sql-pool.md",
            "docs/150-consume/export-targets/040-azure-event-hub.md",
            "docs/150-consume/export-targets/050-azure-service-bus-connector.md",
            "docs/150-consume/export-targets/065-dataverse-connector-v2.md",
            "docs/150-consume/export-targets/060-dataverse-connector.md",
            "docs/150-consume/export-targets/070-http-connector.md",
            "docs/150-consume/export-targets/080-onelake-connector.md",
            "docs/150-consume/export-targets/081-open-mirroring-connector.md",
            "docs/150-consume/export-targets/090-sql-server-connector.md",
            ("docs/150-consume/export-targets/100-create-service-principal.md", dict(type="how-to")),
            "docs/150-consume/export-targets/130-file-name-patterns.md",
        ],
    ),
    dict(
        section="publish",
        sub="graphql",
        title="GraphQL",
        slug="graphql",
        nav_order=40,
        default_type="how-to",
        index_from="docs/150-consume/010-graphql.md",
        intro=(
            "GraphQL is the query interface for reading golden records on demand, as opposed to "
            "[streams](/publish/streams), which push them continuously."
        ),
        pages=[
            "docs/150-consume/graphql/020-add-graphql-entity-type-resolvers.md",
            "docs/150-consume/graphql/050-graphql-actions.md",
        ],
    ),
    dict(
        section="publish",
        sub="integration-patterns",
        title="Integration patterns",
        slug="integration-patterns",
        nav_order=50,
        default_type="how-to",
        intro=(
            "Worked patterns for getting trusted data out of CluedIn and into the systems that "
            "need it, including writing corrected values back to the systems the data came from."
        ),
        pages=[
            "docs/200-kb/how-to/100-connect-cluedin-to-slack.md",
            "docs/200-kb/how-to/150-writing-data-back-to-operational-systems.md",
            (
                "docs/210-playbooks/120-writing-back-to-datasource.md",
                dict(
                    title="Write back to Event Hub and Dataverse",
                    slug="write-back-event-hub-dataverse",
                ),
            ),
        ],
    ),
    # -----------------------------------------------------------------------
    # Administer
    # -----------------------------------------------------------------------
    dict(
        section="administer",
        sub=None,
        pages=[
            ("docs/030-administration/080-feature-flags.md", dict(type="reference", order=50)),
            ("docs/030-administration/110-api-token.md", dict(type="how-to", order=60)),
        ],
    ),
    dict(
        section="administer",
        sub="users-and-roles",
        title="Users and roles",
        slug="users-and-roles",
        nav_order=20,
        default_type="how-to",
        intro=(
            "Who can sign in, and what they are allowed to do. A user gets roles, a role carries "
            "claims and permissions, and access control decides which data each role can see."
        ),
        pages=[
            "docs/030-administration/010-user-management.md",
            ("docs/030-administration/020-roles.md", dict(type="concept")),
            "docs/030-administration/030-assign-roles.md",
            ("docs/030-administration/040-claims.md", dict(type="concept")),
            "docs/030-administration/050-process-role-requests.md",
            ("docs/030-administration/060-permissions.md", dict(type="reference")),
            ("docs/030-administration/090-user.access.md", dict(type="concept", slug="user-access")),
            "docs/030-administration/user-access/010-data-access.md",
            "docs/030-administration/user-access/020-feature-access.md",
        ],
    ),
    dict(
        section="administer",
        sub="access-control",
        title="Access control",
        slug="access-control",
        nav_order=30,
        default_type="how-to",
        index_from="docs/080-management/050-access.control.md",
        intro=(
            "Access control policies decide which golden records and which properties a role can "
            "see. Use them when different teams share one instance but must not share all of the "
            "data in it."
        ),
        pages=[
            "docs/080-management/access-control/010-create-access-control-policy.md",
            "docs/080-management/access-control/020-manage-access-control-policies.md",
            ("docs/080-management/access-control/030-access-control-reference.md", dict(type="reference")),
        ],
    ),
    dict(
        section="administer",
        sub="ui-configuration",
        title="UI configuration",
        slug="ui-configuration",
        nav_order=40,
        default_type="how-to",
        intro=(
            "What users see when they open CluedIn: the layout of a golden record page, the items "
            "in the navigation menu, and the language the interface uses for your business "
            "domains."
        ),
        pages=[
            ("docs/030-administration/100-user-interface.md", dict(type="concept", slug="user-interface")),
            "docs/030-administration/user-interface/010-entity-page-layout.md",
            "docs/030-administration/user-interface/020-side-navigation-menu.md",
            (
                "docs/080-management/entity-type/010-entity-setup.md",
                dict(title="Business domain page layout", slug="business-domain-page-layout"),
            ),
            (
                "docs/080-management/entity-type/020-entity-type-translation.md",
                dict(title="Business domain translation", slug="business-domain-translation"),
            ),
        ],
    ),
    # -----------------------------------------------------------------------
    # Deploy & operate
    # -----------------------------------------------------------------------
    dict(
        section="operate",
        sub=None,
        pages=[
            ("docs/190-paas-operations/001-architecture.md", dict(type="concept", order=10)),
            ("docs/190-paas-operations/140-queues-in-cluedin.md", dict(type="concept", order=15)),
        ],
    ),
    dict(
        section="operate",
        sub="deployment-options",
        title="Deployment options",
        slug="deployment-options",
        nav_order=20,
        default_type="concept",
        intro=(
            "CluedIn runs as a managed SaaS service, as a private SaaS or PaaS deployment in your "
            "own Azure subscription, or locally for development. Choose the model first - it "
            "determines everything else in this section."
        ),
        pages=[
            "docs/020-deployment/000-saas.md",
            "docs/020-deployment/001-saas-install.md",
            "docs/020-deployment/002-paas-install.md",
            "docs/020-deployment/004-local-install.md",
            ("docs/020-deployment/003-pricing.md", dict(type="reference")),
            ("docs/020-deployment/006-licensing-agent-install.md", dict(type="how-to")),
            (
                "docs/020-deployment/007-licensing-agent-exclusion.md",
                dict(
                    title="Azure Policy exemption for deployment scripts",
                    type="reference",
                ),
            ),
            ("docs/020-deployment/005-delete-cluedin-instance.md", dict(type="how-to")),
        ],
    ),
    dict(
        section="operate",
        sub="azure-deployment",
        title="Azure deployment",
        slug="azure",
        nav_order=30,
        default_type="how-to",
        intro=(
            "Deploying CluedIn into your own Azure subscription: the cluster, the network, the "
            "certificates, the storage, and the Helm release that installs the platform onto them."
        ),
        pages=[
            "docs/020-deployment/azure/010-aks.md",
            "docs/020-deployment/azure/020-dns.md",
            "docs/020-deployment/azure/030-certificate.md",
            "docs/020-deployment/azure/040-disks.md",
            "docs/020-deployment/azure/050-email.md",
            "docs/020-deployment/azure/060-pat.md",
            "docs/020-deployment/azure/070-helm.md",
            "docs/020-deployment/azure/080-cluedin-setup.md",
            ("docs/020-deployment/azure/setup/010-step-by-step-install.md", dict(type="tutorial")),
            "docs/020-deployment/azure/setup/020-full-azure-cli-install.md",
        ],
    ),
    dict(
        section="operate",
        sub="azure-marketplace",
        title="Azure Marketplace",
        slug="azure-marketplace",
        nav_order=40,
        default_type="how-to",
        intro=(
            "Installing CluedIn from the Azure Marketplace, including the decisions to make and "
            "the checks to run before and after the managed application is deployed."
        ),
        pages=[
            ("docs/020-deployment/ama/020-ama-first-step.md", dict(type="concept")),
            ("docs/020-deployment/ama/030-ama-second-step.md", dict(type="reference")),
            "docs/020-deployment/ama/040-ama-third-step.md",
            "docs/020-deployment/ama/050-ama-fourth-step.md",
            ("docs/020-deployment/saas/010-azure-requirements.md", dict(type="reference")),
            "docs/020-deployment/saas/020-saas-installation-guide.md",
        ],
    ),
    dict(
        section="operate",
        sub="local-deployment",
        title="Local deployment",
        slug="local",
        nav_order=50,
        default_type="how-to",
        intro=(
            "Running CluedIn on a single machine for development and evaluation, including how to "
            "add extension packages and how to upgrade it."
        ),
        pages=[
            ("docs/020-deployment/local/010-requirements.md", dict(type="reference")),
            "docs/020-deployment/local/020-local-install-guide.md",
            "docs/020-deployment/local/030-extension-package.md",
            "docs/020-deployment/local/040-local-upgrade.md",
        ],
    ),
    dict(
        section="operate",
        sub="configuration",
        title="Configuration",
        slug="configuration",
        nav_order=60,
        default_type="how-to",
        index_from="docs/190-paas-operations/003-configuration.md",
        intro=(
            "Configuring a deployed installation: how you connect to it, how it authenticates "
            "people, how it reaches the network, and how it stores and secures its data."
        ),
        pages=[
            "docs/190-paas-operations/configuration/010-connect-to-cluedin.md",
            "docs/190-paas-operations/configuration/020-setup-sso.md",
            "docs/190-paas-operations/configuration/030-advanced-network.md",
            "docs/190-paas-operations/configuration/040-configure-email.md",
            "docs/190-paas-operations/configuration/050-configure-logging.md",
            "docs/190-paas-operations/configuration/070-configure-certificates.md",
            "docs/190-paas-operations/configuration/080-configure-dns.md",
            "docs/190-paas-operations/configuration/081-configure-pvc.md",
            "docs/190-paas-operations/configuration/090-configure-alerts.md",
            "docs/190-paas-operations/configuration/100-configure-firewall.md",
            "docs/190-paas-operations/configuration/114-configure-sqlserver.md",
            "docs/190-paas-operations/configuration/115-modify-response-headers.md",
            "docs/190-paas-operations/configuration/116-dedicated-stream-processing-pod.md",
            "docs/190-paas-operations/170-private-endpoint.md",
            "docs/190-paas-operations/008-akv2aks.md",
            (
                "docs/190-paas-operations/007-configuration-migration.md",
                dict(slug="sync-configuration-between-environments"),
            ),
        ],
    ),
    dict(
        section="operate",
        sub="upgrade",
        title="Upgrade",
        slug="upgrade",
        nav_order=70,
        default_type="how-to",
        index_from="docs/190-paas-operations/004-upgrade.md",
        intro=(
            "How to upgrade a CluedIn installation, and what each release requires. Read the "
            "guide first, then the notes for the version you are moving to - some releases have "
            "steps that must be done in order."
        ),
        pages=[
            ("docs/190-paas-operations/upgrade/100-cluedin-upgrade-guide.md", dict(order=10)),
            ("docs/190-paas-operations/upgrade/upgrade-guide/060-required-tools.md", dict(type="reference", order=15)),
            ("docs/190-paas-operations/upgrade/upgrade-guide/010-plan-the-upgrade.md", dict(order=20)),
            ("docs/190-paas-operations/upgrade/upgrade-guide/020-prepare-for-the-upgrade.md", dict(order=30)),
            ("docs/190-paas-operations/upgrade/upgrade-guide/030-perform-for-the-upgrade.md", dict(order=40)),
            ("docs/190-paas-operations/upgrade/upgrade-guide/040-common-upgrade-operations.md", dict(order=50)),
            (
                "docs/190-paas-operations/upgrade/upgrade-guide/050-resolve-common-upgrade-issues.md",
                dict(type="troubleshooting", order=60),
            ),
            ("docs/190-paas-operations/upgrade/111-aks-upgrade.md", dict(order=70)),
            ("docs/190-paas-operations/configuration/110-ama-upgrade.md", dict(order=80)),
        ]
        + [
            (p, dict(type="reference", order=100 + i * 5))
            for i, p in enumerate(g("docs/190-paas-operations/upgrade/2*.md"))
        ],
    ),
    dict(
        section="operate",
        sub="backup-and-restore",
        title="Backup and restore",
        slug="backup-and-restore",
        nav_order=80,
        default_type="how-to",
        index_from="docs/190-paas-operations/002-backup-and-restore.md",
        intro=(
            "Protecting an installation and getting it back. The disaster recovery plan explains "
            "the strategy; the runbooks are the steps to follow when you need them."
        ),
        pages=[
            ("docs/190-paas-operations/010-disaster-recovery-plan.md", dict(type="concept")),
            "docs/190-paas-operations/backup-and-restore/020-backup-runbook.md",
            "docs/190-paas-operations/backup-and-restore/030-copy-snapshots-runbook.md",
            "docs/190-paas-operations/backup-and-restore/040-restore-runbook.md",
            "docs/190-paas-operations/backup-and-restore/010-disaster-recovery-runbook.md",
            "docs/190-paas-operations/backup-and-restore/011-disaster-recovery-runbook-failover-database.md",
            "docs/190-paas-operations/backup-and-restore/050-traffic-manager-runbook.md",
        ],
    ),
    dict(
        section="operate",
        sub="monitoring",
        title="Monitoring",
        slug="monitoring",
        nav_order=90,
        default_type="concept",
        intro=(
            "Watching a running installation: the Engine Room shows what the platform is "
            "processing right now, and Log Analytics holds the detail when you need to go back "
            "through it."
        ),
        pages=[
            "docs/070-engine-room.md",
            "docs/120-engine-room/010-cluedIn-performance-metrics.md",
            ("docs/190-paas-operations/120-log-analytics-workspace.md", dict(type="how-to")),
        ],
    ),
    dict(
        section="operate",
        sub="security",
        title="Security",
        slug="security",
        nav_order=100,
        default_type="reference",
        intro=(
            "The security posture of a CluedIn installation, how to restrict access to individual "
            "components, and CluedIn's response to publicly disclosed vulnerabilities."
        ),
        pages=[
            "docs/190-paas-operations/160-security-inventory.md",
            ("docs/200-kb/kb1003-defender.md", dict(type="how-to")),
            ("docs/200-kb/kb0002-basic-auth-clean.md", dict(type="how-to")),
            ("docs/200-kb/kb0006-sso-auth-clean.md", dict(type="how-to")),
            "docs/200-kb/kb0005-log4j.md",
            (
                "docs/200-kb/kb1004-ingress-nginx.md",
                dict(title="Ingress NGINX vulnerabilities (not impacted)"),
            ),
            "docs/200-kb/kb0001-pid.md",
        ],
    ),
    dict(
        section="operate",
        sub="cost-and-scaling",
        title="Cost and scaling",
        slug="cost-and-scaling",
        nav_order=110,
        default_type="how-to",
        intro=(
            "What drives the cost of a CluedIn installation and what you can safely turn down or "
            "off when you do not need it."
        ),
        pages=[
            "docs/190-paas-operations/005-cost-reduction.md",
            "docs/200-kb/kb0009-cost-efficience.md",
            "docs/200-kb/kb0012-stop-aks-cluster.md",
        ],
    ),
    dict(
        section="operate",
        sub="operations",
        title="Day-to-day operations",
        slug="operations",
        nav_order=120,
        default_type="how-to",
        intro=(
            "The recurring operational tasks: promoting configuration between environments, "
            "resetting an instance, migrating the database, and knowing what CluedIn support "
            "covers."
        ),
        pages=[
            ("docs/190-paas-operations/006-support-scope.md", dict(type="reference")),
            "docs/190-paas-operations/009-env-management.md",
            "docs/190-paas-operations/110-reset-tool.md",
            "docs/190-paas-operations/150-azure-sql-migration.md",
            ("docs/190-paas-operations/130-common-questions.md", dict(type="reference")),
        ],
    ),
]
