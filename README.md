# CluedIn Documentation

Jekyll-based documentation site for CluedIn.

## Prerequisites

- [Docker](https://www.docker.com/) and [VS Code](https://code.visualstudio.com/) with the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

## Getting started

1. Open the repository in VS Code.
2. When prompted, click **Reopen in Container** (or run **Dev Containers: Reopen in Container** from the command palette).
3. The container will build and install all Ruby gem dependencies automatically.

## Running the development server

### Via VS Code task (recommended)

Press `Ctrl+Shift+B` (or run **Tasks: Run Build Task**) to start the Jekyll development server. The site will be available at `http://localhost:4000`.

The task uses incremental builds and live reload, so the browser will refresh automatically when files change.

### Via terminal

```bash
bundle exec jekyll serve --host 0.0.0.0 --livereload --watch --incremental --destination /tmp/_site --force_polling
```

### Via Make

```bash
make serve
```

### Via standalone Docker

If you don't want to use the Dev Containers workflow, the included PowerShell script runs the same Jekyll server in a `ruby:3.3-bookworm` container without VS Code:

```powershell
pwsh ./run-jekyll-docker.ps1
```

The first run takes ~5–8 minutes (apt + `bundle install` inside the container); subsequent starts are much faster. The container is named `cluedin-docs`; stop it with `docker stop cluedin-docs`. The script passes `--force_polling` to Jekyll so livereload detects edits through the Windows Docker bind mount.

## Building the site

To do a one-off build without starting the server:

```bash
bundle exec jekyll build
```

The output is written to `_site/` by default (or `/tmp/_site` when using the VS Code task).

## Installing/updating dependencies

```bash
bundle install      # install gems from Gemfile.lock
bundle update       # update gems to latest allowed versions
```

## REST API reference

The REST API documentation under `docs/250-rest-api/` renders a categorized reference from a bundled OpenAPI specification. The structure is:

- **Source spec:** `assets/api/swagger.json` — point-in-time export of the live API's OpenAPI 3.0 spec.
- **Hand-written descriptions:** `assets/api/descriptions-overlay/<category>.json` — summary, description, and parameter notes per route. Merged onto the spec at split time so the original `swagger.json` stays untouched.
- **Per-category sub-specs:** `assets/api/categories/<category>.json` — derived artifacts served to the Swagger UI viewer. One file per category (System & health, Entities, etc.) keeps each page fast.
- **Splitter:** `_tools/split-spec.js` — regenerates the sub-specs from `swagger.json` + overlays.
- **Viewer:** `assets/api/viewer.html` — renders a sub-spec with Swagger UI. A connection bar at the top requests a bearer token via the resource-owner password grant (`POST <base>/auth/connect/token`, `client_id` = org name) and attaches it to every "Try it out" request, rewriting each request's origin to the connected environment. The base URL and token live in `sessionStorage` so they are shared across category iframes/tabs. Calls are subject to the target environment's CORS policy.

### Refreshing the reference

After updating `swagger.json` (download a fresh copy from `https://<organization>.<domain>/api/swagger/v1/swagger.json`) or any overlay file, regenerate the per-category sub-specs and commit them:

```bash
# inside the docker container (if running):
docker exec cluedin-docs node /srv/jekyll/_tools/split-spec.js

# or natively, from the repo root:
node _tools/split-spec.js
```

The splitter rewrites every file under `assets/api/categories/`. The reference picks up the new specs on the next site build.

## Build performance

Expect each build to take **~60 seconds**, even with `--incremental` and even when only a single file has changed.

The root cause is `jekyll-remote-theme`. Jekyll's incremental build mode only skips re-rendering a page if none of its dependencies have changed. Because the remote theme's layout files (`_layouts/default.html`, `_includes/head.html`, `_includes/css/activation.scss.liquid`, etc.) are dependencies of every page, any change — including to the remote theme cache itself — causes all 416 pages to be re-rendered.

The top render hotspots (from `--profile`) are all remote theme files:

| Template | Pages rendered | Time (s) |
|---|---|---|
| `_layouts/default.html` | 416 | 26.7 |
| `_includes/head.html` | 416 | 18.5 |
| `_includes/css/activation.scss.liquid` | 416 | 17.6 |

There is no simple workaround without changing the theme strategy (e.g. switching from `jekyll-remote-theme` to a locally vendored copy of the theme).
