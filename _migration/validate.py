"""
Check the generated site before it is built.

Jekyll will happily build a site whose navigation is broken - just-the-docs
silently drops a page whose `parent` does not resolve. These checks catch that,
plus the failure modes the restructure is specifically meant to prevent:

  * a page with no content type
  * two pages with the same title under the same parent
  * two pages claiming the same URL
  * navigation nested more than three levels deep, which the theme cannot render
  * a page the sidebar cannot reach, because its parent chain does not climb to
    a top-level section
  * an internal link pointing at a URL no page serves

Exit code is non-zero if anything fails, so this can gate a build.

    python _migration/validate.py
"""

import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.abspath(os.path.join(HERE, ".."))
DOCS = os.path.join(SITE, "docs")

VALID_TYPES = {"concept", "how-to", "tutorial", "reference", "troubleshooting", "landing"}
LINK_RE = re.compile(r'(?:\]\(|href=")(/[^)"\s]*)')


def site_baseurl():
    """The baseurl from _config.yml.

    Links in the content carry it (migrate.py writes them that way) but
    permalinks do not, because Jekyll adds it when the site is served. Strip it
    before comparing the two.
    """
    config = os.path.join(SITE, "_config.yml")
    if not os.path.isfile(config):
        return ""
    for line in io.open(config, encoding="utf-8"):
        match = re.match(r'^baseurl:\s*"?([^"\n]*)"?', line)
        if match:
            return match.group(1).strip().rstrip("/")
    return ""


def read_front_matter(path):
    text = io.open(path, encoding="utf-8-sig").read()
    if not text.startswith("---"):
        return {}, text
    parts = re.split(r"^---[ \t]*$", text, maxsplit=2, flags=re.M)
    if len(parts) < 3:
        return {}, text
    fm = {}
    for line in parts[1].split("\n"):
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if m:
            fm[m.group(1)] = m.group(2).strip().strip('"')
    return fm, parts[2]


def main():
    pages = []
    for root, dirs, files in os.walk(SITE):
        dirs[:] = [d for d in dirs if d not in ("assets", ".git", "_site", "vendor", "node_modules")]
        if os.path.basename(root).startswith("_") or "\\static" in root or "/static" in root:
            continue
        for name in files:
            if not name.endswith(".md"):
                continue
            path = os.path.join(root, name)
            fm, body = read_front_matter(path)
            if not fm:
                # No front matter means Jekyll does not treat it as a page
                # (README.md, and anything in the config's `exclude` list).
                continue
            pages.append((os.path.relpath(path, SITE).replace("\\", "/"), fm, body))

    errors, warnings = [], []

    urls = {}
    titles = {}
    parents = set()
    for rel, fm, _body in pages:
        permalink = fm.get("permalink")
        if not permalink:
            errors.append("%s: no permalink" % rel)
            continue
        key = permalink.rstrip("/") or "/"
        if key in urls:
            errors.append("%s: permalink %s already used by %s" % (rel, permalink, urls[key]))
        urls[key] = rel

        if fm.get("has_children") == "true":
            parents.add(fm.get("title"))

        if permalink != "/" and fm.get("nav_exclude") != "true":
            content_type = fm.get("content_type")
            if not content_type:
                errors.append("%s: no content_type" % rel)
            elif content_type not in VALID_TYPES:
                errors.append("%s: unknown content_type %r" % (rel, content_type))

        sibling_key = (fm.get("grand_parent"), fm.get("parent"), fm.get("title"))
        if fm.get("parent"):
            if sibling_key in titles:
                errors.append(
                    "%s: title %r duplicated under %r (also %s)"
                    % (rel, fm.get("title"), fm.get("parent"), titles[sibling_key])
                )
            titles[sibling_key] = rel

    # navigation resolves, and is never more than three levels deep
    all_titles = {fm.get("title") for _rel, fm, _b in pages}
    for rel, fm, _body in pages:
        for key in ("parent", "grand_parent"):
            value = fm.get(key)
            if value and value not in all_titles:
                errors.append("%s: %s %r does not match any page title" % (rel, key, value))
            if value and value not in parents and value in all_titles:
                errors.append("%s: %s %r is not a page with has_children" % (rel, key, value))
        if fm.get("grand_parent") and fm.get("has_children") == "true":
            errors.append("%s: fourth navigation level (theme supports three)" % rel)
        if fm.get("great_grand_parent"):
            errors.append(
                "%s: great_grand_parent declares a fourth navigation level. The "
                "theme renders three, so the key has no effect and is stale" % rel
            )

    # every published page is reachable from the sidebar
    #
    # just-the-docs walks parent -> grand_parent -> top level by title. A page
    # whose chain does not climb all the way is built and served, but nothing
    # links to it, so the only way to find it is to already know its URL.
    top_level = {
        fm.get("title")
        for _rel, fm, _b in pages
        if not fm.get("parent") and fm.get("published") != "false"
    }
    children_of = {}
    for _rel, fm, _b in pages:
        if fm.get("parent"):
            children_of.setdefault(fm.get("title"), set()).add(fm.get("parent"))

    unreachable, hidden = [], []
    for rel, fm, _body in pages:
        if fm.get("published") == "false":
            continue                       # deliberately off the live site
        if fm.get("nav_exclude") == "true":
            hidden.append(rel)
            continue
        parent, grand_parent = fm.get("parent"), fm.get("grand_parent")
        if not parent:
            continue                       # a top-level section
        if grand_parent:
            if grand_parent not in top_level:
                unreachable.append((rel, "grand_parent %r is not a top-level section" % grand_parent))
            elif grand_parent not in children_of.get(parent, set()):
                unreachable.append((rel, "no page titled %r sits under %r" % (parent, grand_parent)))
        elif parent not in top_level:
            unreachable.append((rel, "parent %r is not top level, and no grand_parent is declared" % parent))
    for rel, why in unreachable:
        errors.append("%s: not reachable from the sidebar - %s" % (rel, why))

    # every internal link resolves to a page or an asset
    prefix = site_baseurl()
    for rel, fm, body in pages:
        for url in LINK_RE.findall(body):
            target = url.split("#")[0].rstrip("/") or "/"
            if prefix and target.startswith(prefix + "/"):
                target = target[len(prefix):]
            elif prefix and target == prefix:
                target = "/"
            if target.startswith(("/assets/", "/static/")):
                continue
            if target not in urls:
                warnings.append("%s: link to %s serves no page" % (rel, url))

    print("pages checked : %d" % len(pages))
    print("nav_exclude   : %d (built and linkable, but not in the sidebar)" % len(hidden))
    print("errors        : %d" % len(errors))
    print("warnings      : %d" % len(warnings))
    for message in errors:
        print("  ERROR   " + message)
    for message in sorted(set(warnings)):
        print("  WARNING " + message)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
