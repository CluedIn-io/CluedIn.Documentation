# Where a new article goes

The documentation is organised around **the path data takes through CluedIn**,
not around the product's feature list. A reader who does not yet know what a
feature is called can still find its page, because they know which stage of
their own work they are in.

That only holds if new articles are placed the same way. This page is the
procedure for placing one. It takes about a minute, and the answer is
deterministic — there is exactly one right home for any given article.

- [The two rules](#the-two-rules)
- [Step 1 — Product documentation, or supporting material?](#step-1--product-documentation-or-supporting-material)
- [Step 2 — Which section?](#step-2--which-section)
- [Step 3 — Which subsection?](#step-3--which-subsection)
- [Step 4 — Which content type?](#step-4--which-content-type)
- [Step 5 — File name and front matter](#step-5--file-name-and-front-matter)
- [Moving or renaming an article](#moving-or-renaming-an-article)
- [Check it before you push](#check-it-before-you-push)
- [Section reference](#section-reference)

---

## The two rules

Everything below follows from these.

**1. One canonical home per subject.** A subject is explained in exactly one
place. Learning paths, playbooks, solution guides and troubleshooting articles
*link to* that place; they never restate it. If you are writing a playbook and
find yourself explaining how deduplication works, that explanation belongs in
`/master/deduplication`, and the playbook links to it.

**2. Every article declares a content type** — `concept`, `how-to`, `tutorial`,
`reference` or `troubleshooting`. `validate.py` rejects an article without one.
An article that would need two content types is two articles.

---

## Step 1 — Product documentation, or supporting material?

Ask: **does this article explain a part of CluedIn itself?**

**Yes** — it is product documentation. It belongs in one of the nine sections
that make up the primary navigation (`01`–`09`), and it is the canonical home
for its subject. Go to [Step 2](#step-2--which-section).

**No** — it is supporting material. Pick by what the article *is*:

| The article… | Section |
|---|---|
| teaches a role over a sequence of modules, in a deliberate order | **Learning paths** (`12`) |
| is delivery methodology — how to scope, sequence and land a project | **Playbooks** (`13`) |
| connects CluedIn to a specific external ecosystem (Purview, Fabric, Power Apps, Data Factory), or walks through a business use case end to end | **Solutions & integrations** (`11`) |
| starts from a symptom the reader has already observed | **Troubleshooting** (`14`) |
| says what shipped, or what is supported | **Release notes** (`15`) |
| documents something withdrawn, superseded, or for an old platform version | **Archive** (`archive`, with `published: false`) |

Supporting material is allowed to be opinionated, sequenced and
audience-specific. It is not allowed to be the only place a feature is
explained. If the canonical page you want to link to does not exist yet, write
it in the product section first, then link to it.

> **The test.** Delete every sentence in your draft that explains how a feature
> works, and replace each with a link. If what remains is still a useful
> article, it is supporting material. If nothing is left, it was product
> documentation all along.

---

## Step 2 — Which section?

Product documentation goes to the lifecycle stage the reader is *in* when they
need the article — not the stage the feature is technically implemented in.

| Section | Put it here when the article is about… |
|---|---|
| **Get started** (`/get-started`) | orienting a new reader: what the platform is, the vocabulary the rest of the documentation assumes, the first end-to-end run |
| **Ingest** (`/ingest`) | getting records *in*: connecting a source, describing what to ingest, mapping columns onto the model, processing the result |
| **Model** (`/model`) | describing what data *means*: business domains, vocabularies, identifiers, relationships, hierarchies, the data catalog |
| **Master** (`/master`) | turning many records into one: deduplication, merging, and working with the golden records that result |
| **Govern & improve** (`/govern`) | keeping data good: clean projects, rules, enrichers, tags, the glossary, approval workflows, AI agents |
| **Publish & consume** (`/publish`) | getting trusted data *out* through product features: streams, export targets, GraphQL |
| **Administer** (`/administer`) | managing the product **from inside it**: users, roles, permissions, access control, UI configuration, API tokens |
| **Deploy & operate** (`/operate`) | running the installation **from outside it**: deployment, cluster configuration, upgrade, backup, monitoring, cost, security posture |
| **Develop & APIs** (`/develop`) | writing code against CluedIn: the Python SDK, the REST API, custom connectors and enrichers |

### The four boundaries people get wrong

**Administer vs Deploy & operate.** Administer is what you do *inside* the
product through its interface. Deploy & operate is what you do *to* the
installation. "Add a user" is Administer; "add a node" is Deploy & operate.
Authentication is the awkward one: *which identity provider the cluster is wired
to* is Deploy & operate, and *which role a signed-in person has* is Administer.

**Model vs Master.** Model describes what data means before you resolve it;
Master resolves it. Vocabularies, business domains and identifiers are Model —
they are the inputs entity resolution consumes. Deduplication, merging and
golden record history are Master.

**Model vs Govern & improve.** Model is structure; Govern is the quality and
classification applied on top of it. A *vocabulary key* is Model. A *tag* or a
*glossary term* is Govern, because it classifies records rather than describing
their shape.

**Publish & consume vs Develop & APIs.** If the reader configures a product
feature to move data out — a stream, an export target, a GraphQL query — it is
Publish & consume. If they write code that calls CluedIn, it is Develop & APIs.

### Symptoms

Symptom-first articles go to **Troubleshooting** (`/troubleshooting`), with one
exception: symptoms about records not arriving, or arriving wrong, already have
a home at `/ingest/troubleshooting` (quarantine, logs, processing throughput).
Put ingestion symptoms there and everything else in the top-level section.

A troubleshooting article names a **symptom**, not a feature. "Records are stuck
in quarantine" is a troubleshooting title. "Quarantine" is not — that is a
concept page under Ingest.

---

## Step 3 — Which subsection?

Look at the [section reference](#section-reference) below, or at the section's
index page, and use an existing subsection if one covers the subject. Most
articles land in one that already exists.

A section can also hold articles directly, without a subsection — `/master` has
`search` and `filters` as direct children alongside its two subsections. Use
that when the article belongs to the section as a whole rather than to one
subject within it.

**Create a new subsection only when all three are true:**

1. You have at least three articles on the subject, or will have within the
   change you are making. One article is not a section.
2. No existing subsection covers it without stretching.
3. It answers a distinct question a reader would ask.

Creating one means adding a directory with an `index.md` — see
[the index template](#a-subsection-index) below.

**Three navigation levels, never four.** Section → subsection → article. The
theme cannot render a fourth level, and `validate.py` rejects one if you create
it. If you need more depth, the subsection is doing too much and should
be split into two sibling subsections.

---

## Step 4 — Which content type?

| Type | Use when | The test |
|---|---|---|
| `concept` | explaining how something works, or why it exists | The reader finishes understanding something, not having done something. |
| `how-to` | steps to accomplish one task | The reader arrives already knowing what they want; you give them the shortest path to it. |
| `tutorial` | guided end-to-end learning | The reader is learning, so you choose the example, and it works start to finish. |
| `reference` | facts, options, parameters, APIs | The reader looks one thing up and leaves. Nothing is sequential. |
| `troubleshooting` | symptom, cause, and fix | Titled by what the reader observed, not by the feature involved. |
| `landing` | a section or subsection index | Only on `index.md`. Never on an article. |

The distinction that matters most is **how-to vs tutorial**. A how-to assumes
competence and covers the reader's real data; a tutorial assumes none and uses
data you supply. Do not write a how-to that opens with three paragraphs of
background — that is a concept page and a how-to, and they should be two
articles that link to each other.

---

## Step 5 — File name and front matter

### Path and file name

```
docs/<NN-section>/<subsection>/<NNN>-<slug>.md
```

- The numeric prefix orders the page and **must equal its `nav_order`**. Number
  in tens (`010`, `020`, `030`) so a later article can be inserted without
  renumbering the directory.
- `<slug>` is the last segment of the page's URL: lowercase, hyphenated, no
  numbers.
- The directory name is not the URL. `05-govern-and-improve` serves `/govern`;
  `08-deploy-and-operate/azure-deployment` serves `/operate/azure`. The
  `permalink` in the front matter is what decides the URL — the
  [section reference](#section-reference) lists each one.

### An article

```yaml
---
layout: cluedin
title: Property rules
parent: Mapping           # exact title of the containing index page
grand_parent: Ingest      # omit when the article is a direct child of a section
nav_order: 30             # equals the file's numeric prefix
permalink: /ingest/mapping/property-rules
content_type: how-to
---
```

| Key | |
|---|---|
| `layout` | Always `cluedin`. |
| `title` | Must be unique among its siblings — `validate.py` rejects duplicates. |
| `parent`, `grand_parent` | The **titles** of the containing index pages, spelled exactly (`Govern & improve`, not `Govern`). A mismatch makes just-the-docs silently drop the page from the navigation, which is why this is checked. |
| `nav_order` | Position among siblings. Equals the file's numeric prefix. |
| `permalink` | The URL: section permalink + subsection slug + page slug, with no numeric prefixes. |
| `content_type` | One of the five in [Step 4](#step-4--which-content-type). |
| `redirect_from` | Only when a URL that used to serve this content no longer does — see [Moving or renaming](#moving-or-renaming-an-article). |
| `tags`, `last_modified` | Optional. |
| `source_path` | **Do not add.** It records where the restructure took a page from, and is meaningless on a new article. |

### A subsection index

```yaml
---
layout: cluedin
title: Mapping
parent: Ingest
nav_order: 30
has_children: true
permalink: /ingest/mapping
content_type: landing
summary: Mapping decides which source column becomes which vocabulary key, which value identifies the record, and what business domain it belongs to.
---
```

Then one or two paragraphs saying what the subsection covers and in what order
to read it. The `summary` is what a reader sees next to this subsection in its
parent's index, so write it as a sentence about the subject, not about the page
("A data source is where records come from", not "This section covers data
sources").

### Do not hand-maintain the index

The list of pages in a section is **generated**. `_includes/children.html` reads
the child pages and renders them with their content-type badges, sorted by
`nav_order`. Setting the front matter correctly is the whole job — an article
cannot be added to a section and then be missing from its index.

Never add a card grid or a hand-written link list to an `index.md`. If a page
appears in the wrong order, fix its `nav_order`; if it does not appear at all,
its `parent` does not match the index page's `title`.

---

## Moving or renaming an article

Every URL the site has ever served still has to work. When a page's `permalink`
changes, add the old one to `redirect_from`:

```yaml
permalink: /govern/rules/rule-types
redirect_from: ["/management/rules/rule-types"]
```

The `jekyll-redirect-from` plugin builds a redirect stub at each old URL. Keep
appending to the list rather than replacing it — a page that has moved twice
needs both of its old URLs.

Renaming a page's `title` also changes what its children must declare as
`parent`. Update them in the same commit; `validate.py` will tell you if you
miss one.

---

## Check it before you push

```bash
python _migration/validate.py
```

It must print `errors : 0`. It catches, before Jekyll gets a chance to build a
quietly broken site:

- an article with no content type, or an unrecognised one
- two articles with the same title under the same parent
- two articles claiming the same URL
- a `parent` or `grand_parent` that matches no page — the failure just-the-docs
  handles by silently dropping the page from the navigation
- a fourth navigation level, including a stray `great_grand_parent`
- **a page the sidebar cannot reach**, because its parent chain does not climb
  all the way to a top-level section. Such a page is still built and still
  served, so nothing looks broken — it is simply impossible to find unless you
  already know the URL
- an internal link pointing at a URL no page serves

The five warnings it currently prints are links that were already broken before
the restructure; they are recorded in `_migration/report.md`. Do not add to them.

It also prints a `nav_exclude` count. Those are pages deliberately kept out of
the sidebar — reachable only by a direct link — and there are currently four.
Setting `nav_exclude: true` on a new article means accepting that no reader will
find it by browsing, so do it only when the page exists to be linked to from
somewhere specific.

Then build the site and look at the page:

```bash
bundle exec jekyll build
```

### A note on `_migration/`

`docs/` was generated once, from the routing table in `_migration/targets_*.py`,
when the documentation was restructured around the lifecycle. That move is
finished — **`docs/` is now authored directly**, and adding an article means
adding a file, not editing the routing table.

What stays useful from that folder is `validate.py`, which is the ongoing check
described above, and `report.md` / `redirects.csv`, which are the record of
where every pre-restructure article went.

---

## Section reference

The directory, the URL, and the subsections each section currently has. Where a
subsection's URL is not simply its directory name, the URL is given in
parentheses.

| Section | Directory | URL | Subsections |
|---|---|---|---|
| Get started | `01-start-here` | `/get-started` | core-concepts |
| Ingest | `02-ingest` | `/ingest` | connectors, data-sources, manual-data-entry, mapping, patterns, processing, troubleshooting |
| Model | `03-model` | `/model` | business-domains, data-catalog, hierarchies, relationships, vocabularies |
| Master | `04-master` | `/master` | deduplication, golden-records |
| Govern & improve | `05-govern-and-improve` | `/govern` | ai-agents, cleaning, enrichment, rules, tags, workflows |
| Publish & consume | `06-publish-and-consume` | `/publish` | export-targets, graphql, integration-patterns, streams |
| Administer | `07-administer` | `/administer` | access-control, ui-configuration, users-and-roles |
| Deploy & operate | `08-deploy-and-operate` | `/operate` | azure-deployment (`/operate/azure`), azure-marketplace, backup-and-restore, configuration, cost-and-scaling, deployment-options, local-deployment (`/operate/local`), monitoring, operations, security, upgrade |
| Develop & APIs | `09-develop` | `/develop` | api-reference (`/api`), integrations, python-sdk |
| Solutions & integrations | `11-solutions-and-integrations` | `/solutions` | azure-data-factory, copilot, fabric, master-data-services, power-apps, power-automate, purview, use-cases |
| Learning paths | `12-learning-paths` | `/learning-paths` | ai-training (`/learning-paths/ai`), data-architect-course (`/learning-paths/data-architect`), data-steward-course (`/learning-paths/data-steward`), fundamentals, role-handbooks |
| Playbooks | `13-playbooks` | `/playbooks` | data-engineering, data-ingestion, project-delivery |
| Troubleshooting | `14-troubleshooting` | `/troubleshooting` | — |
| Release notes | `15-release-notes` | `/release-notes` | — |
| Archive | `archive` | `/archive` | historical-operations, legacy-development, legacy-user-interface, unsupported-features |

Sections `01`–`09` are the primary navigation. Anything with a `nav_order` of 20
or above renders below a separator as supporting material — the
`nav_secondary_from` setting in `_config.yml`.
