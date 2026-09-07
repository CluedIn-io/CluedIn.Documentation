"""
Build the restructured documentation site from the old `docs/` tree.

Reads the routing table in ia.py / targets_*.py and, for every article:

  * copies it to its one canonical home under site-next/docs/
  * rewrites the front matter (parent, grand_parent, nav_order, permalink,
    content_type) while preserving every other key the page already had
  * rewrites internal links so they point at the new permalinks
  * records `redirect_from` so the old URL keeps working

It also writes the section and subsection index pages, the home page, and a
migration report listing every routing decision, retitle and unresolved link.

The old `docs/` tree is never modified; the new tree is written to
`<parent of _migration>/docs`. See _migration/README.md for how to point it
at a checkout of the pre-restructure tree:

    CLUEDIN_DOCS_SOURCE=../docs-old python _migration/migrate.py
"""

import io
import os
import re
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import ia  # noqa: E402
import targets_a  # noqa: E402
import targets_b  # noqa: E402
import targets_c  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = ia.REPO_ROOT
SITE = os.path.abspath(os.path.join(HERE, ".."))
DOCS_OUT = os.path.join(SITE, "docs")

# Prefix applied to every link the migration writes. Empty when the site is
# served from the root of a domain, which is the normal case. Set it with
# `--baseurl /next` when the site is published under a path, so that hard-coded
# links match where the pages actually land. Page permalinks are NOT prefixed:
# Jekyll writes them relative to the destination and `baseurl` in _config.yml
# handles the rest.
BASEURL = ""

SECTION_BY_KEY = {s["key"]: s for s in ia.SECTIONS}
ALL_TARGETS = targets_a.TARGETS + targets_b.TARGETS + targets_c.TARGETS

# Front matter keys this migration owns. Everything else on a page - tags,
# published, last_modified, headerIcon, nav_exclude, sitemap - is carried over
# untouched, so no page silently changes visibility or metadata.
CONTROLLED = {
    "layout",
    "title",
    "parent",
    "grand_parent",
    "nav_order",
    "permalink",
    "has_children",
    "content_type",
    "redirect_from",
    "source_path",
    "summary",
    "list_children",
}

# Old top-level URLs that no longer exist as pages. Links to them are rewritten
# to the section that absorbed them, and the section index claims the URL as a
# redirect so external links keep working.
SECTION_REDIRECTS = {
    "/getting-started": "/get-started/quickstart",
    "/get-cluedin": "/get-started/get-cluedin",
    "/key-terms-and-features": "/get-started/core-concepts",
    "/integration": "/ingest",
    "/preparation": "/govern",
    "/governance": "/govern",
    "/management": "/govern",
    "/consume": "/publish",
    "/administration": "/administer",
    "/deployment": "/operate",
    "/paas-operations": "/operate",
    "/development": "/develop",
    "/user-interface": "/archive/legacy-user-interface",
    "/microsoft-integration": "/solutions",
    "/usecases": "/solutions/use-cases",
    "/usecases-summary": "/solutions/use-cases",
    "/kb": "/troubleshooting",
    "/training": "/learning-paths",
    "/rest-api": "/api",
    "/workflow": "/govern/workflows",
    "/integration/additional-operations-on-records": "/ingest",
}

# Images that sat next to a page inside docs/ instead of under assets/. Jekyll
# published them at their source path, so the pages' `./media/...` links never
# resolved on the old site either. The restructure moves the files under
# assets/ and points the links at the URL that now serves them.
MEDIA_MOVES = {
    "/microsoft-integration/purview/media/": "/assets/images/microsoft-integration/purview/media/",
}

# Links that were already broken in the old site and whose intended target is
# unambiguous - a typo in the permalink, or a page that was renamed without its
# inbound links being updated. Repaired here so the new site does not inherit
# them. Anything genuinely ambiguous is left alone and listed in the report.
ALIASES = {
    "/training/ai/ai-agents/fixing-data-quality-issues": "/training/ai/ai-agents/fixing-data-quality-issuese",
    "/preparation/enricher/azure-openai": "/preparation/enricher/artificial-intelligence",
    "/microsoft-integration/purview/adf-pipeline-automation": "/microsoft-integration/purview/data-factory-pipeline-automation",
    "/deployment/saas-cluedin": "/deployment/cluedin-saas",
    "/integration/additional-operations-on-records/source-record-validation": "/integration/additional-operations-on-records/validations",
}


# ---------------------------------------------------------------------------
# Front matter
# ---------------------------------------------------------------------------


def read_page(path):
    """Return (ordered list of front matter lines, body) for a markdown file."""
    text = io.open(os.path.join(REPO, path), encoding="utf-8-sig").read()
    if not text.startswith("---"):
        return [], text
    parts = re.split(r"^---[ \t]*$", text, maxsplit=2, flags=re.M)
    if len(parts) < 3:
        return [], text
    return parts[1].strip("\n").split("\n"), parts[2].lstrip("\n")


def front_matter_value(lines, key):
    for line in lines:
        m = re.match(r"^" + re.escape(key) + r":\s*(.*)$", line)
        if m:
            return m.group(1).strip()
    return None


def keep_uncontrolled(lines):
    """Drop the keys this migration owns, keeping everything else verbatim."""
    out, skipping = [], False
    for line in lines:
        m = re.match(r"^([A-Za-z_][\w-]*):", line)
        if m:
            skipping = m.group(1) in CONTROLLED
            if skipping:
                continue
            out.append(line)
        else:
            if not skipping and line.strip():
                out.append(line)
    return out


def yaml_str(value):
    """Quote a scalar when YAML would otherwise misread it."""
    text = str(value)
    if text == "":
        return '""'
    if re.search(r'^[\s>|&*!%@`\-?{}\[\],#"\']|:\s|:$|\s#|^(true|false|null|yes|no|on|off)$', text, re.I):
        return '"' + text.replace("\\", "\\\\").replace('"', '\\"') + '"'
    return text


def render_page(fm, extra_lines, body):
    lines = ["---"]
    for key, value in fm.items():
        if value is None:
            continue
        if isinstance(value, list):
            lines.append(
                "%s: [%s]"
                % (key, ", ".join('"%s"' % str(v).replace('"', '\\"') for v in value))
            )
        elif isinstance(value, bool):
            lines.append("%s: %s" % (key, "true" if value else "false"))
        else:
            lines.append("%s: %s" % (key, yaml_str(value)))
    lines.extend(extra_lines)
    lines.append("---")
    return "\n".join(lines) + "\n\n" + body.lstrip("\n")


# ---------------------------------------------------------------------------
# Body transforms
# ---------------------------------------------------------------------------

CARD_LINE = re.compile(r'[ \t]*<div class="card-line">.*?</div>\s*</div>\s*', re.S)


def strip_card_grids(body):
    """Remove card navigation grids from a landing page.

    Card grids are pure navigation: the generated "In this section" list and
    the sidebar already cover them, and they are the main reason the old
    landing pages had to be hand-maintained.
    """
    previous = None
    while previous != body:
        previous = body
        body = re.sub(
            r'[ \t]*<div class="card-line">(?:(?!<div class="card-line">).)*?\n[ \t]*</div>\s*\n',
            "",
            body,
            flags=re.S,
        )
    return body


# Absolute links, and the relative ones a page writes to its neighbours
# (`./aks`, `../assets/images/x.png`). Both have to be rewritten: a relative
# link is resolved against the URL of the page that holds it, and the
# restructure changes that URL.
LINK_RE = re.compile(r'(\]\(|href=")((?:/|\.{1,2}/)[^)"\s]*)')


def summarise(intro):
    """First sentence of a section intro, as plain text for the parent's index."""
    text = " ".join(intro.split("\n\n")[0].split())
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = text.replace("**", "")
    match = re.search(r"^(.+?[.!?])(\s|$)", text)
    return match.group(1) if match else text


def absolutise(page_url, relative):
    """Resolve a relative link against the URL of the page that contains it.

    Pages are served at `/a/b` (Jekyll writes `/a/b.html`), so the base for a
    relative link is `/a/`, the same way a browser resolves it.
    """
    parts = [segment for segment in page_url.rstrip("/").split("/")[:-1] if segment]
    for segment in relative.split("/"):
        if segment in (".", ""):
            continue
        if segment == "..":
            if parts:
                parts.pop()
        else:
            parts.append(segment)
    return "/" + "/".join(parts)


def rewrite_links(
    body, url_map, unresolved, source, valid_new=frozenset(), repaired=None, page_url=None
):
    def replace(match):
        prefix, url = match.group(1), match.group(2)
        if "{{" in url or "{%" in url:
            # A Liquid expression, not a link. `docs/tag.md` builds hrefs this
            # way; rewriting it would corrupt the template.
            return match.group(0)
        anchor = ""
        if "#" in url:
            url, anchor = url.split("#", 1)
            anchor = "#" + anchor
        if url.startswith("."):
            # A relative link only means anything next to the page it came
            # from. Turn it into the absolute URL it pointed at on the old
            # site, then route it like any other link.
            if not page_url:
                unresolved.append((source, url))
                return match.group(0)
            url = absolutise(page_url, url)
        key = url.rstrip("/").lower() or "/"
        if key in ALIASES:
            key = ALIASES[key]
            if repaired is not None and key in url_map:
                repaired.append((source, url, url_map[key]))
        if key in url_map:
            return prefix + BASEURL + url_map[key] + anchor
        # Already a new-site URL (the pages written for this site link forward).
        if key in valid_new:
            return prefix + BASEURL + url + anchor
        if url.startswith("/assets/") or url.startswith("/static/") or key == "/":
            return prefix + BASEURL + url + anchor
        for was, now in MEDIA_MOVES.items():
            if key.startswith(was):
                moved = now + url[len(was):]
                if repaired is not None:
                    repaired.append((source, url, moved))
                return prefix + BASEURL + moved + anchor
        unresolved.append((source, url))
        return match.group(0)

    return LINK_RE.sub(replace, body)


# ---------------------------------------------------------------------------
# Plan
# ---------------------------------------------------------------------------


def normalise_pages(entries):
    for entry in entries:
        if isinstance(entry, tuple):
            yield entry[0], dict(entry[1])
        else:
            yield entry, {}


def slug_from(path, fm_lines, override):
    if override:
        return override
    if path in ia.SLUG_FIXES:
        return ia.SLUG_FIXES[path]
    permalink = front_matter_value(fm_lines, "permalink")
    if permalink:
        return permalink.strip("/").split("/")[-1]
    base = os.path.basename(path)[:-3]
    return re.sub(r"^\d+-", "", base).lower().replace(".", "-")


def build_plan():
    """Return (pages, sections, subsections, notes)."""
    pages = []          # every article that gets written
    subsections = []    # subsection index pages
    notes = {"retitled": [], "duplicate_sources": [], "index_from": []}
    seen_sources = {}

    def claim(source, where):
        if source in seen_sources:
            notes["duplicate_sources"].append((source, seen_sources[source], where))
        seen_sources[source] = where

    for target in ALL_TARGETS:
        section = SECTION_BY_KEY[target["section"]]
        sub = target.get("sub")
        default_type = target.get("default_type", "how-to")

        if sub:
            base_permalink = target.get("abs_permalink") or (
                section["permalink"] + "/" + target["slug"]
            )
            out_dir = os.path.join(section["dir"], sub)
            parent_title = target["title"]
            grand_parent = section["title"]
            sub_record = dict(
                title=target["title"],
                permalink=base_permalink,
                dir=out_dir,
                section=section,
                nav_order=target["nav_order"],
                intro=target.get("intro", ""),
                index_from=target.get("index_from"),
                children=[],
            )
            subsections.append(sub_record)
            if target.get("index_from"):
                claim(target["index_from"], base_permalink)
                notes["index_from"].append((target["index_from"], base_permalink))
        else:
            base_permalink = section["permalink"]
            out_dir = section["dir"]
            parent_title = section["title"]
            grand_parent = None
            sub_record = None
            if target.get("index_from"):
                claim(target["index_from"], base_permalink)
                notes["index_from"].append((target["index_from"], base_permalink))
                section["index_from"] = target["index_from"]

        auto_order = 0
        for source, over in normalise_pages(target.get("pages", [])):
            full = os.path.join(REPO, source)
            if not os.path.isfile(full):
                raise SystemExit("missing source file: " + source)
            fm_lines, body = read_page(source)
            auto_order += 10
            order = over.get("order", auto_order)
            slug = slug_from(source, fm_lines, over.get("slug"))
            original_title = front_matter_value(fm_lines, "title") or ""
            title = over.get("title") or original_title.strip('"')
            if not title:
                raise SystemExit("no title for " + source)
            if over.get("title") and over["title"] != original_title:
                notes["retitled"].append((source, original_title, over["title"]))

            record = dict(
                source=source,
                dest=os.path.join(out_dir, "%03d-%s.md" % (order, slug)),
                permalink=base_permalink + "/" + slug,
                old_permalink=front_matter_value(fm_lines, "permalink"),
                title=title,
                parent=parent_title,
                grand_parent=grand_parent,
                nav_order=order,
                content_type=over.get("type", default_type),
                fm_lines=fm_lines,
                body=body,
            )
            claim(source, record["permalink"])
            pages.append(record)
            if sub_record is not None:
                sub_record["children"].append(record)

        for new in target.get("new_pages", []):
            record = dict(
                source=None,
                dest=os.path.join(out_dir, "%03d-%s.md" % (new["order"], new["slug"])),
                permalink=base_permalink + "/" + new["slug"],
                old_permalink=None,
                title=new["title"],
                parent=parent_title,
                grand_parent=grand_parent,
                nav_order=new["order"],
                content_type=new["type"],
                fm_lines=[],
                body=new["body"],
            )
            pages.append(record)
            if sub_record is not None:
                sub_record["children"].append(record)

    for entry in targets_c.STANDALONE:
        fm_lines, body = read_page(entry["source"])
        claim(entry["source"], entry["permalink"])
        pages.append(
            dict(
                source=entry["source"],
                dest=entry["dest"],
                permalink=entry["permalink"],
                old_permalink=front_matter_value(fm_lines, "permalink"),
                title=(front_matter_value(fm_lines, "title") or "").strip('"'),
                parent=None,
                grand_parent=None,
                nav_order=None,
                content_type=entry["type"],
                fm_lines=fm_lines,
                body=body,
                nav_exclude=True,
            )
        )

    for source in targets_c.REPLACED_BY_SECTION_INDEX:
        claim(source, "(replaced by generated section index)")

    return pages, subsections, notes, seen_sources


# ---------------------------------------------------------------------------
# Write
# ---------------------------------------------------------------------------


def build_url_map(pages, subsections):
    url_map = {}

    def add(old, new):
        if not old:
            return
        url_map.setdefault(old.rstrip("/").lower() or "/", new)

    for page in pages:
        add(page["old_permalink"], page["permalink"])
    for sub in subsections:
        if sub["index_from"]:
            fm_lines, _ = read_page(sub["index_from"])
            add(front_matter_value(fm_lines, "permalink"), sub["permalink"])
    for section in ia.SECTIONS:
        if section.get("index_from"):
            fm_lines, _ = read_page(section["index_from"])
            add(front_matter_value(fm_lines, "permalink"), section["permalink"])
    for old, new in SECTION_REDIRECTS.items():
        add(old, new)
    return url_map


def redirects_for(new_permalink, page_old, url_map):
    """Old URLs that should redirect to this page."""
    out = []
    if page_old and page_old.rstrip("/") != new_permalink:
        out.append(page_old.rstrip("/"))
    for old, new in SECTION_REDIRECTS.items():
        if new == new_permalink and old not in out:
            out.append(old)
    return out


def write(path, text):
    full = os.path.join(DOCS_OUT if not os.path.isabs(path) else "", path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    io.open(full, "w", encoding="utf-8", newline="\n").write(text)


def parse_args(argv):
    global BASEURL
    rest = []
    index = 0
    while index < len(argv):
        arg = argv[index]
        if arg.startswith("--baseurl="):
            BASEURL = arg.split("=", 1)[1].rstrip("/")
        elif arg == "--baseurl":
            index += 1
            BASEURL = argv[index].rstrip("/")
        else:
            rest.append(arg)
        index += 1
    if BASEURL and not BASEURL.startswith("/"):
        BASEURL = "/" + BASEURL
    return rest


def main():
    parse_args(sys.argv[1:])
    pages, subsections, notes, claimed = build_plan()
    url_map = build_url_map(pages, subsections)
    valid_new = {p["permalink"].lower() for p in pages}
    valid_new |= {s["permalink"].lower() for s in subsections}
    valid_new |= {s["permalink"].lower() for s in ia.SECTIONS}
    unresolved = []
    repaired = []

    if os.path.isdir(DOCS_OUT):
        shutil.rmtree(DOCS_OUT)
    os.makedirs(DOCS_OUT)

    # --- articles ---------------------------------------------------------
    for page in pages:
        fm = {"layout": "cluedin", "title": page["title"]}
        if page["parent"]:
            fm["parent"] = page["parent"]
        if page["grand_parent"]:
            fm["grand_parent"] = page["grand_parent"]
        if page["nav_order"] is not None:
            fm["nav_order"] = page["nav_order"]
        fm["permalink"] = page["permalink"]
        if page["content_type"]:
            fm["content_type"] = page["content_type"]
        redirects = redirects_for(page["permalink"], page["old_permalink"], url_map)
        if redirects:
            fm["redirect_from"] = redirects
        if page["source"]:
            fm["source_path"] = page["source"]
        if page.get("nav_exclude"):
            fm["nav_exclude"] = True

        body = rewrite_links(
            page["body"],
            url_map,
            unresolved,
            page["source"] or page["dest"],
            valid_new,
            repaired,
            page_url=page["old_permalink"],
        )
        write(page["dest"], render_page(fm, keep_uncontrolled(page["fm_lines"]), body))

    # --- subsection indexes ----------------------------------------------
    for sub in subsections:
        child_urls = {c["permalink"] for c in sub["children"]}
        extra_lines, source_path = [], None
        if sub["index_from"]:
            fm_lines, body = read_page(sub["index_from"])
            body = strip_card_grids(body)
            old_permalink = front_matter_value(fm_lines, "permalink")
            body = rewrite_links(
                body,
                url_map,
                unresolved,
                sub["index_from"],
                valid_new,
                repaired,
                page_url=old_permalink,
            )
            extra_lines = keep_uncontrolled(fm_lines)
            source_path = sub["index_from"]
            listed = sum(1 for url in child_urls if "(" + url in body or '"' + url in body)
            list_children = listed < 2
        else:
            body = sub["intro"] + "\n"
            old_permalink = None
            list_children = True

        fm = {
            "layout": "cluedin",
            "title": sub["title"],
            "parent": sub["section"]["title"],
            "nav_order": sub["nav_order"],
            "has_children": True,
            "permalink": sub["permalink"],
            "content_type": "landing",
        }
        if sub["intro"]:
            fm["summary"] = summarise(sub["intro"])
        if not list_children:
            fm["list_children"] = False
        redirects = redirects_for(sub["permalink"], old_permalink, url_map)
        if redirects:
            fm["redirect_from"] = redirects
        if source_path:
            fm["source_path"] = source_path
        write(os.path.join(sub["dir"], "index.md"), render_page(fm, extra_lines, body))

    # --- section indexes --------------------------------------------------
    for section in ia.SECTIONS:
        body = (
            '<div class="audience">\n'
            '  <p class="audience-question">%s</p>\n'
            '  <p class="audience-who">%s</p>\n'
            "</div>\n\n%s\n"
            % (section["question"], section["audience"], section["intro"])
        )
        body = rewrite_links(body, url_map, unresolved, section["dir"], valid_new, repaired)

        # A section whose old landing page carried real content - the release
        # notes page held the version tables, the roadmap and the release
        # process - keeps that content below the orientation blurb. Without
        # this, the prose would be dropped on the floor.
        extra_lines, source_path, old_permalink = [], None, None
        if section.get("index_from"):
            fm_lines, kept = read_page(section["index_from"])
            old_permalink = front_matter_value(fm_lines, "permalink")
            kept = strip_card_grids(kept)
            kept = rewrite_links(
                kept,
                url_map,
                unresolved,
                section["index_from"],
                valid_new,
                repaired,
                page_url=old_permalink,
            )
            if kept.strip():
                body = body.rstrip("\n") + "\n\n" + kept.lstrip("\n")
            extra_lines = keep_uncontrolled(fm_lines)
            source_path = section["index_from"]

        fm = {
            "layout": "cluedin",
            "title": section["title"],
            "nav_order": section["nav_order"],
            "has_children": True,
            "permalink": section["permalink"],
            "content_type": "landing",
        }
        redirects = redirects_for(section["permalink"], old_permalink, url_map)
        if redirects:
            fm["redirect_from"] = redirects
        if source_path:
            fm["source_path"] = source_path
        write(os.path.join(section["dir"], "index.md"), render_page(fm, extra_lines, body))

    # --- reports ----------------------------------------------------------
    all_sources = sorted(
        os.path.relpath(os.path.join(root, name), REPO).replace("\\", "/")
        for root, _dirs, files in os.walk(os.path.join(REPO, "docs"))
        for name in files
        if name.endswith(".md")
    )
    unclaimed = [s for s in all_sources if s not in claimed]

    notes["repaired"] = repaired
    write_report(pages, subsections, notes, unresolved, unclaimed, all_sources, url_map)

    if BASEURL:
        print("baseurl            : %s" % BASEURL)
    print("pages written      : %d" % len(pages))
    print("subsection indexes : %d" % len(subsections))
    print("section indexes    : %d" % len(ia.SECTIONS))
    print("source files       : %d" % len(all_sources))
    print("unrouted sources   : %d" % len(unclaimed))
    print("duplicate routes   : %d" % len(notes["duplicate_sources"]))
    print("links repaired     : %d" % len(set(repaired)))
    print("unresolved links   : %d" % len(set(unresolved)))
    for source in unclaimed:
        print("  UNROUTED " + source)
    for row in notes["duplicate_sources"]:
        print("  DUPLICATE %s -> %s and %s" % row)


def write_report(pages, subsections, notes, unresolved, unclaimed, all_sources, url_map):
    lines = [
        "# Migration report",
        "",
        "Generated by `_migration/migrate.py`. Every number below is derived from the",
        "routing table, not written by hand.",
        "",
        "| | Count |",
        "|---|---|",
        "| Source articles in `docs/` | %d |" % len(all_sources),
        "| Articles migrated | %d |" % len([p for p in pages if p["source"]]),
        "| Articles newly written | %d |" % len([p for p in pages if not p["source"]]),
        "| Section index pages | %d |" % len(ia.SECTIONS),
        "| Subsection index pages | %d |" % len(subsections),
        "| Old landing pages replaced by a generated index | %d |"
        % len(targets_c.REPLACED_BY_SECTION_INDEX),
        "| Source articles not routed | %d |" % len(unclaimed),
        "| Internal links that could not be resolved | %d |" % len(unresolved),
        "",
        "## Content types",
        "",
        "| Type | Articles |",
        "|---|---|",
    ]
    counts = {}
    for page in pages:
        counts[page["content_type"] or "(none)"] = counts.get(page["content_type"] or "(none)", 0) + 1
    for key in sorted(counts, key=str):
        lines.append("| %s | %d |" % (key, counts[key]))

    lines += ["", "## Articles retitled", "", "| Source | Was | Now |", "|---|---|---|"]
    for source, was, now in notes["retitled"]:
        lines.append("| `%s` | %s | %s |" % (source, was, now))

    lines += [
        "",
        "## Old landing pages reused as a section index",
        "",
        "The page keeps its prose; its card grid is removed because the generated",
        '"In this section" list replaces it.',
        "",
        "| Source | Now |",
        "|---|---|",
    ]
    for source, permalink in notes["index_from"]:
        lines.append("| `%s` | `%s` |" % (source, permalink))

    lines += [
        "",
        "## Old landing pages dropped",
        "",
        "These held nothing but a card grid pointing at their children, which the",
        "generated section index now does automatically.",
        "",
    ]
    for source in targets_c.REPLACED_BY_SECTION_INDEX:
        lines.append("- `%s`" % source)

    if notes.get("repaired"):
        lines += [
            "",
            "## Pre-existing broken links repaired",
            "",
            "These links were broken in the old site - a typo in a permalink, or a page",
            "renamed without its inbound links being updated.",
            "",
            "| In | Was | Now |",
            "|---|---|---|",
        ]
        for source, was, now in sorted(set(notes["repaired"])):
            lines.append("| `%s` | `%s` | `%s` |" % (source, was, now))

    if unclaimed:
        lines += ["", "## Source articles not routed", ""]
        lines += ["- `%s`" % s for s in unclaimed]

    if unresolved:
        lines += [
            "",
            "## Unresolved internal links",
            "",
            "Links whose target does not exist in the old site either - they were already",
            "broken before the migration.",
            "",
            "| In | Link |",
            "|---|---|",
        ]
        for source, url in sorted(set(unresolved)):
            lines.append("| `%s` | `%s` |" % (source, url))

    lines += ["", "## Full routing table", "", "| New URL | Type | Source |", "|---|---|---|"]
    for page in sorted(pages, key=lambda p: p["permalink"]):
        lines.append(
            "| `%s` | %s | %s |"
            % (
                page["permalink"],
                page["content_type"],
                "`%s`" % page["source"] if page["source"] else "*written for this site*",
            )
        )

    io.open(os.path.join(HERE, "report.md"), "w", encoding="utf-8", newline="\n").write(
        "\n".join(lines) + "\n"
    )

    with io.open(os.path.join(HERE, "redirects.csv"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write("old_url,new_url\n")
        for old, new in sorted(url_map.items()):
            fh.write("%s,%s\n" % (old, new))


if __name__ == "__main__":
    main()
