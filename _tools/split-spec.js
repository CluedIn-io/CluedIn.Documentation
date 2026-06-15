#!/usr/bin/env node
/*
 * Splits the bundled CluedIn OpenAPI specification (assets/api/swagger.json)
 * into one sub-specification per category, written to
 * assets/api/categories/<slug>.json plus a manifest.json file.
 *
 * Each sub-specification contains:
 *   - only the operations whose tags belong to the category
 *   - the transitive closure of $ref'd schemas (so Swagger UI can render
 *     request and response bodies without unresolved references)
 *   - components.securitySchemes copied unchanged
 *
 * The script is run inside the docker container:
 *   docker exec cluedin-docs node /srv/jekyll/_tools/split-spec.js
 */

const fs = require('fs');
const path = require('path');

// Resolve paths relative to this script so the splitter works both inside
// the docker container (where the script lives at /srv/jekyll/_tools/...)
// and natively from the repo root (`node _tools/split-spec.js`).
const ROOT = path.resolve(__dirname, '..', 'assets', 'api');
const SRC = path.join(ROOT, 'swagger.json');
const OUT_DIR = path.join(ROOT, 'categories');
const OVERLAY_DIR = path.join(ROOT, 'descriptions-overlay');

// Optional overlay: per-route human-written summary, description, and
// per-parameter descriptions. Files live in assets/api/descriptions-overlay/,
// one JSON file per category, with keys "METHOD path" e.g.
//   "GET /api/v1/vocabs/keys": { "summary": "...", "description": "...",
//                                  "parameters": { "page": "..." } }
// Most CluedIn routes ship both /api/foo and /api/v1/foo variants that wrap
// the same controller method; the loader treats them as equivalent so the
// overlay only needs one entry per logical route. Keys starting with "_" are
// treated as comments and ignored.
let overlay = {};
if (fs.existsSync(OVERLAY_DIR) && fs.statSync(OVERLAY_DIR).isDirectory()) {
  const files = fs.readdirSync(OVERLAY_DIR).filter(f => f.endsWith('.json')).sort();
  for (const f of files) {
    try {
      const entries = JSON.parse(fs.readFileSync(path.join(OVERLAY_DIR, f), 'utf8'));
      let added = 0;
      for (const k of Object.keys(entries)) {
        if (k.startsWith('_')) continue;
        overlay[k] = entries[k];
        added++;
      }
      console.log(`Loaded ${added} overlay entries from descriptions-overlay/${f}`);
    } catch (e) {
      console.warn(`Could not parse overlay file ${f}: ${e.message}`);
    }
  }
}

function lookupOverlay(method, p) {
  const m = method.toUpperCase();
  if (overlay[`${m} ${p}`]) return overlay[`${m} ${p}`];
  // Fall back across the /api/ <-> /api/v1/ pair.
  if (p.startsWith('/api/v1/')) {
    const alt = '/api/' + p.substring('/api/v1/'.length);
    if (overlay[`${m} ${alt}`]) return overlay[`${m} ${alt}`];
  } else if (p.startsWith('/api/') && !/^\/api\/v\d+\//.test(p)) {
    const alt = '/api/v1/' + p.substring('/api/'.length);
    if (overlay[`${m} ${alt}`]) return overlay[`${m} ${alt}`];
  }
  return null;
}

function applyOverlay(method, p, op) {
  const o = lookupOverlay(method, p);
  if (!o) return op;
  const merged = Object.assign({}, op);
  if (o.summary) merged.summary = o.summary;
  if (o.description) merged.description = o.description;
  if (o.parameters && Array.isArray(merged.parameters)) {
    merged.parameters = merged.parameters.map(param => {
      if (param && param.name && o.parameters[param.name] && !param.description) {
        return Object.assign({}, param, { description: o.parameters[param.name] });
      }
      return param;
    });
  }
  return merged;
}

// Curated category map (single source of truth shared with prune-spec.js).
// Order in this list controls the order of categories in the manifest.
const CATEGORIES = require('./api-categories.js');

const spec = JSON.parse(fs.readFileSync(SRC, 'utf8'));

const specTagNames = (spec.tags || []).map(t => t.name);
const assigned = new Set(CATEGORIES.flatMap(c => c.tags));
const missing = specTagNames.filter(t => !assigned.has(t));
if (missing.length) {
  // Any tag in swagger.json that is not assigned to a category is treated as
  // excluded and dropped from the rendered reference. Run prune-spec.js to also
  // remove these operations from the published swagger.json.
  console.log('DROPPED unassigned tags (not in any category):', missing);
}

function collectRefs(node, out) {
  if (node == null) return;
  if (Array.isArray(node)) { for (const x of node) collectRefs(x, out); return; }
  if (typeof node !== 'object') return;
  for (const k of Object.keys(node)) {
    if (k === '$ref' && typeof node[k] === 'string') out.add(node[k]);
    else collectRefs(node[k], out);
  }
}

function schemaNameFromRef(ref) {
  const prefix = '#/components/schemas/';
  return ref.startsWith(prefix) ? ref.substring(prefix.length) : null;
}

function buildSchemaClosure(initialRefs, allSchemas) {
  const closure = new Set();
  const queue = [...initialRefs];
  while (queue.length) {
    const ref = queue.shift();
    const name = schemaNameFromRef(ref);
    if (name == null) continue;
    if (closure.has(name)) continue;
    if (!(name in allSchemas)) continue;
    closure.add(name);
    const inner = new Set();
    collectRefs(allSchemas[name], inner);
    for (const r of inner) queue.push(r);
  }
  return closure;
}

fs.mkdirSync(OUT_DIR, { recursive: true });

// Remove any stale category files from a previous run so we don't leave orphans.
for (const f of fs.readdirSync(OUT_DIR)) {
  if (f.endsWith('.json')) fs.unlinkSync(path.join(OUT_DIR, f));
}

const manifest = [];

for (const cat of CATEGORIES) {
  const tagSet = new Set(cat.tags);
  const paths = {};
  let opCount = 0;
  for (const p of Object.keys(spec.paths)) {
    const item = spec.paths[p];
    const kept = {};
    for (const m of Object.keys(item)) {
      const op = item[m];
      if (op && Array.isArray(op.tags) && op.tags.some(t => tagSet.has(t))) {
        kept[m] = applyOverlay(m, p, op);
        opCount++;
      }
    }
    if (Object.keys(kept).length) paths[p] = kept;
  }

  if (opCount === 0) {
    console.log(`SKIP ${cat.slug.padEnd(40)} (no operations)`);
    continue;
  }

  const refs = new Set();
  collectRefs(paths, refs);
  const closure = buildSchemaClosure(refs, (spec.components && spec.components.schemas) || {});
  const schemas = {};
  for (const n of closure) schemas[n] = spec.components.schemas[n];

  const sub = {
    openapi: spec.openapi,
    info: {
      title: `CluedIn REST API — ${cat.title}`,
      description: cat.description,
      version: spec.info.version
    },
    tags: (spec.tags || []).filter(t => tagSet.has(t.name)),
    paths,
    components: Object.assign(
      { schemas },
      spec.components && spec.components.securitySchemes
        ? { securitySchemes: spec.components.securitySchemes }
        : {}
    )
  };

  const outFile = path.join(OUT_DIR, `${cat.slug}.json`);
  fs.writeFileSync(outFile, JSON.stringify(sub));
  const size = fs.statSync(outFile).size;
  console.log(
    `OK   ${cat.slug.padEnd(40)} ops=${String(opCount).padStart(4)}  schemas=${String(closure.size).padStart(4)}  size=${size}B`
  );
  manifest.push({
    slug: cat.slug,
    title: cat.title,
    description: cat.description,
    tags: cat.tags,
    operationCount: opCount,
    schemaCount: closure.size
  });
}

fs.writeFileSync(path.join(OUT_DIR, 'manifest.json'), JSON.stringify(manifest, null, 2));
console.log(`\nWrote ${manifest.length} categories to ${OUT_DIR}`);
