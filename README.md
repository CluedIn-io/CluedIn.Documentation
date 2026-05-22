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
