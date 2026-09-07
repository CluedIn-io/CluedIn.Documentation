"""
Information architecture for the restructured CluedIn documentation.

This file is the single source of truth for the new site. It states, for every
article in the old `docs/` tree, exactly one canonical home in the new tree.
`migrate.py` reads it, copies the files, rewrites their front matter and
internal links, and produces a redirect map.

Two rules govern everything below:

  1. A subject gets exactly one canonical home. Learning paths, playbooks,
     solution guides and troubleshooting articles link to that home instead of
     re-explaining the subject.

  2. Every article declares a content type - concept, how-to, tutorial,
     reference or troubleshooting - so the four kinds of documentation stay
     distinguishable.

Structures
----------
SECTIONS  top-level navigation entries: the eight lifecycle areas first, then
          supporting material, then the archive.
TARGETS   every section and subsection that can hold pages, with the ordered
          list of source files that belong to it.

A page entry is either a path string, or a (path, overrides) tuple where
overrides may set `title` (to resolve a duplicate or clarify a legacy name),
`type` (to override the target default content type) or `slug`.
"""

import glob as _glob
import os

def _find_source():
    """Locate the CluedIn documentation checkout these scripts read from.

    Works both when this folder sits inside that repository and when it lives
    in a repository of its own with the source checked out alongside it. Set
    CLUEDIN_DOCS_SOURCE to override.
    """
    here = os.path.dirname(os.path.abspath(__file__))
    candidates = []
    if os.environ.get("CLUEDIN_DOCS_SOURCE"):
        candidates.append(os.environ["CLUEDIN_DOCS_SOURCE"])
    candidates += [
        os.path.join(here, "..", ".."),                            # inside the source repo
        os.path.join(here, "..", "..", "CluedInDocumentation"),    # sibling checkout
        os.path.join(here, "..", "..", "CluedIn.Documentation"),
    ]
    for candidate in candidates:
        candidate = os.path.abspath(candidate)
        if all(
            os.path.exists(os.path.join(candidate, part))
            for part in ("docs", "assets", "_config.yml")
        ):
            return candidate
    return os.path.abspath(candidates[-1])


REPO_ROOT = _find_source()


def g(pattern, exclude=()):
    """Expand a glob against the old docs tree, sorted, files only."""
    out = []
    for p in sorted(_glob.glob(os.path.join(REPO_ROOT, pattern))):
        if not os.path.isfile(p):
            continue
        rel = os.path.relpath(p, REPO_ROOT).replace("\\", "/")
        if rel not in exclude:
            out.append(rel)
    return out


# Slugs corrected on the way across. The old permalink had a typo, so the new
# site takes the spelling the link everywhere else already assumed.
SLUG_FIXES = {
    "docs/220-training/ai/002-ai-agents-fixing-data-quality-issues.md": "fixing-data-quality-issues",
    # Two demo pages whose old permalinks were distinguished only by the folder
    # above them. Flattened into one level, they need distinct slugs.
    "docs/220-training/ai/006-ai-enricher-demo.md": "ai-enricher-demo",
    "docs/220-training/ai/008-copilot-demo.md": "copilot-demo",
}


# ---------------------------------------------------------------------------
# Top-level sections
#
# nav_order 1-9   the data lifecycle, plus develop & APIs
# nav_order 20+   supporting material that is not part of the workflow
# nav_order 30+   archive
# ---------------------------------------------------------------------------

SECTIONS = [
    dict(
        key="start",
        dir="01-start-here",
        title="Get started",
        permalink="/get-started",
        nav_order=1,
        question="What is CluedIn and how do I begin?",
        audience="Anyone opening CluedIn for the first time.",
        intro=(
            "CluedIn takes messy data from many systems and turns it into golden records you "
            "can trust. This section explains what the platform does, defines the terms used "
            "everywhere else in the documentation, and walks you through your first end-to-end "
            "run.\n\n"
            "Once you are oriented, the rest of the documentation follows the data lifecycle: "
            "[Ingest](/ingest) -> [Model](/model) -> [Master](/master) -> "
            "[Govern & improve](/govern) -> [Publish & consume](/publish)."
        ),
    ),
    dict(
        key="ingest",
        dir="02-ingest",
        title="Ingest",
        permalink="/ingest",
        nav_order=2,
        question="How do I get data into CluedIn?",
        audience="Data engineers and anyone connecting a source system.",
        intro=(
            "Everything that brings records into CluedIn lives here: connecting a source, "
            "describing what you want to ingest, mapping source columns onto the model, and "
            "processing the result into golden records.\n\n"
            "The usual order is **Data sources -> Mapping -> Processing**. Use "
            "[Troubleshoot ingestion](/ingest/troubleshooting) when records do not arrive or "
            "land in quarantine."
        ),
    ),
    dict(
        key="model",
        dir="03-model",
        title="Model",
        permalink="/model",
        nav_order=3,
        question="How do I describe my data so CluedIn understands it?",
        audience="Data architects and data modellers.",
        intro=(
            "The model is how CluedIn knows that a row is a customer, that two columns mean the "
            "same thing, and that one record belongs under another. Business domains classify "
            "records, vocabularies describe their properties, identifiers make records findable "
            "across systems, and relationships connect them.\n\n"
            "Get the model right before you master data - entity resolution is only as good as "
            "the identifiers and domains you give it."
        ),
    ),
    dict(
        key="master",
        dir="04-master",
        title="Master",
        permalink="/master",
        nav_order=4,
        question="How do I turn records into trusted golden records?",
        audience="Data stewards and data architects.",
        intro=(
            "Mastering is where many records about the same real-world thing become one golden "
            "record. Deduplication finds the duplicates, merging resolves them, and the golden "
            "record keeps the full history and explanation of how every value was chosen.\n\n"
            "For what a golden record *is*, see [Core concepts](/get-started/core-concepts). "
            "This section covers how to work with them."
        ),
    ),
    dict(
        key="govern",
        dir="05-govern-and-improve",
        title="Govern & improve",
        permalink="/govern",
        nav_order=5,
        question="How do I improve and govern the data?",
        audience="Data stewards and data governance managers.",
        intro=(
            "Once data is mastered, this is how you keep it good: clean projects fix recurring "
            "quality problems, rules apply logic automatically, enrichers fill gaps from "
            "external sources, tags and the glossary classify records, and workflows put "
            "approvals around changes."
        ),
    ),
    dict(
        key="publish",
        dir="06-publish-and-consume",
        title="Publish & consume",
        permalink="/publish",
        nav_order=6,
        question="How do I get trusted data out?",
        audience="Data engineers and integration developers.",
        intro=(
            "Streams push golden records continuously to an export target; GraphQL and the "
            "[REST API](/api) pull them on demand. Start with the export target you need, then "
            "build the stream that feeds it."
        ),
    ),
    dict(
        key="administer",
        dir="07-administer",
        title="Administer",
        permalink="/administer",
        nav_order=7,
        question="How do I manage the product?",
        audience="CluedIn administrators working inside the product.",
        intro=(
            "Everything an administrator does **inside** CluedIn: who can sign in, what they can "
            "see and do, how the interface is configured, and how API access is issued.\n\n"
            "Running the platform itself - deploying, upgrading, backing up - is "
            "[Deploy & operate](/operate)."
        ),
    ),
    dict(
        key="operate",
        dir="08-deploy-and-operate",
        title="Deploy & operate",
        permalink="/operate",
        nav_order=8,
        question="How do I run the platform?",
        audience="Platform and DevOps teams running a CluedIn installation.",
        intro=(
            "Everything a platform team does **to** a CluedIn installation: choosing a "
            "deployment model, installing it, configuring the cluster, upgrading it, backing it "
            "up, watching it, and keeping its cost and security in order.\n\n"
            "Product administration - users, roles, UI configuration - is "
            "[Administer](/administer)."
        ),
    ),
    dict(
        key="develop",
        dir="09-develop",
        title="Develop & APIs",
        permalink="/develop",
        nav_order=9,
        question="How do I automate or extend CluedIn?",
        audience="Developers building on top of CluedIn.",
        intro=(
            "Automate CluedIn from Python, call it over REST, and extend it with custom "
            "integrations and enrichers.\n\n"
            "The [API reference](/api) is generated from the OpenAPI specification and covers "
            "every endpoint."
        ),
    ),
    dict(
        key="solutions",
        dir="11-solutions-and-integrations",
        title="Solutions & integrations",
        permalink="/solutions",
        nav_order=20,
        question="How does CluedIn fit with the rest of my stack?",
        audience="Solution architects and system integrators.",
        intro=(
            "Guides for connecting CluedIn to specific ecosystems, and worked use cases showing "
            "how the platform is applied to a business problem.\n\n"
            "These guides link to the product documentation rather than repeating it."
        ),
    ),
    dict(
        key="learning",
        dir="12-learning-paths",
        title="Learning paths",
        permalink="/learning-paths",
        nav_order=21,
        question="How do I learn CluedIn for my role?",
        audience="New users following a structured course.",
        intro=(
            "Role-based courses that sequence the product documentation into a learning order. "
            "Each module explains the *why*, then links to the canonical article for the *how* - "
            "so there is only ever one explanation of a feature to keep up to date."
        ),
    ),
    dict(
        key="playbooks",
        dir="13-playbooks",
        title="Playbooks",
        permalink="/playbooks",
        nav_order=22,
        question="How do I run a CluedIn project?",
        audience="Project leads, delivery teams and consultants.",
        intro=(
            "Delivery methodology rather than product reference: how to scope a CluedIn project, "
            "sequence the work, and get to production. Playbooks link to the product "
            "documentation for the mechanics."
        ),
    ),
    dict(
        key="troubleshooting",
        dir="14-troubleshooting",
        title="Troubleshooting",
        permalink="/troubleshooting",
        nav_order=23,
        question="Something is not working - what do I check?",
        audience="Anyone hitting a symptom.",
        intro=(
            "Symptom-first articles: what you observe, why it happens, and what to do about it. "
            "Each article names a symptom, not a feature.\n\n"
            "This section replaces the old Knowledge Base. Knowledge Base articles that were "
            "really feature documentation now live with the feature they describe."
        ),
    ),
    dict(
        key="release",
        dir="15-release-notes",
        title="Release notes",
        permalink="/release-notes",
        nav_order=24,
        question="What changed, and what is supported?",
        audience="Everyone.",
        intro="What shipped in each release, and how CluedIn versions and supports the platform.",
    ),
    dict(
        key="archive",
        dir="archive",
        title="Archive",
        permalink="/archive",
        nav_order=30,
        question="Where did the old material go?",
        audience="Maintainers.",
        intro=(
            "Material kept for reference but no longer part of the supported documentation: "
            "features that were withdrawn, developer documentation for older platform versions, "
            "and superseded operational runbooks.\n\n"
            "Nothing here should be linked from the product documentation. Pages keep the "
            "`published: false` flag they already carried, so they do not render on the live "
            "site - they are retained so the history is not lost."
        ),
    ),
]
