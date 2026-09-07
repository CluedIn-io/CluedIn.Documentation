# How `docs/` was restructured

`docs/` is generated, not hand-arranged. Every article in the pre-restructure
tree was assigned exactly one home in the new one, and these scripts performed
the move.

| File | What it is |
|---|---|
| `ia.py` | The information architecture: the top-level sections, and the helpers the routing table uses. |
| `targets_a.py`, `targets_b.py`, `targets_c.py` | The routing table. For every source article, the one section and subsection it belongs to, its content type and its order. |
| `migrate.py` | Reads the routing table, copies each article to its new home, rewrites front matter and internal links, writes the section indexes, and records `redirect_from` so old URLs keep working. |
| `validate.py` | Checks the generated tree before Jekyll builds it. |
| `report.md` | The generated record of the move: every routing decision, every retitle, every repaired link. |
| `redirects.csv` | Old URL to new URL for all 565 pre-restructure URLs. |

## The two rules

1. **One canonical home per subject.** Learning paths, playbooks, solution
   guides and troubleshooting articles link to that home instead of restating
   it.
2. **Every article declares a content type** — `concept`, `how-to`, `tutorial`,
   `reference` or `troubleshooting` — so the four kinds of documentation stay
   distinguishable. `validate.py` fails the build if one is missing.

## Re-running the migration

`migrate.py` reads a pre-restructure `docs/` tree and writes a new one, so it
needs that tree checked out somewhere other than here:

```bash
git worktree add ../docs-old <commit before the restructure>
mkdir -p ../docs-new && cp -r _migration ../docs-new/

CLUEDIN_DOCS_SOURCE=$(pwd)/../docs-old python ../docs-new/_migration/migrate.py
python _migration/validate.py
```

The output lands in `../docs-new/docs`. Copy it over `docs/` to apply it.

Change where an article lives by editing the routing table in `targets_*.py`,
not by moving the file — otherwise the next run puts it back.
