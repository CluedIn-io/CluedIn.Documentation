# Instructions for AI assistants

This repository is the CluedIn documentation site (Jekyll, just-the-docs
v0.7.0 as a remote theme). Read this before adding, moving or editing an
article.

## Placing a new article

**Read [CONTRIBUTING.md](CONTRIBUTING.md) first and follow it.** It is the
procedure for deciding where an article goes, and it has exactly one right
answer for any article. Do not place an article by guessing from a similar
file name or a feature name.

In short:

- The docs are organised around the data lifecycle, not the product's feature
  list: Get started, Ingest, Model, Master, Govern & improve, Publish &
  consume, then Administer, Deploy & operate, Develop & APIs. Supporting
  material (solutions, learning paths, playbooks, troubleshooting, release
  notes) comes after them.
- One canonical home per subject. Supporting material links to that home and
  never restates it.
- Every article declares one `content_type`: `concept`, `how-to`, `tutorial`,
  `reference` or `troubleshooting`. An article that needs two is two articles.
- The navigation has at most three levels.
- The numeric file name prefix must equal `nav_order`. The directory name is
  not the URL (`docs/05-govern-and-improve/` serves `/govern`). Each section's
  URL is the `permalink` in its `index.md`.
- `parent` and `grand_parent` are page **titles**, spelled exactly.
- Do not edit `_migration/targets_*.py` or rerun `_migration/migrate.py` to
  add an article. `docs/` is authored directly now.

Use the front matter templates in CONTRIBUTING.md, "Step 5 — File name and
front matter".

## Before you finish

```bash
python _migration/validate.py
```

It must print `errors : 0` and no new warnings. Build the site too if you
changed layouts, includes, styles or front matter:

```bash
bundle exec jekyll build
```

## Site design

- Styles: `_sass/custom/custom.scss`, compiled into both colour schemes. Colours
  come from the scheme files `_sass/color_schemes/clue.scss` (light) and
  `clue-dark.scss` (dark). Don't hard-code colours in components.
- Home page: `index.md`. Its cards and "Popular guides" are front matter lists,
  and every `url` must be a live permalink. "What's new" is built from the
  release notes, so a new release note needs a one-line `summary:`.
- Sidebar group headings and icons: `assets/js/nav-groups.js`. Icons:
  `_includes/icons/cluedin.html`.
- Logo: `assets/images/clued-in-logo.svg` is the mark used on www.cluedin.com.
  Don't replace or redraw it.
