#!/usr/bin/env node
/*
 * Prunes the bundled CluedIn OpenAPI specification (assets/api/swagger.json)
 * in place so it contains ONLY the operations whose tags are assigned to a
 * documentation category in _tools/api-categories.js. Every other tag is an
 * "Exclude" verdict in the REST API audit and is removed from:
 *   - paths      (operations whose every tag is excluded)
 *   - tags       (the top-level tag list)
 *   - components.schemas (anything no longer referenced; closure recomputed)
 *
 * securitySchemes and all other top-level fields are preserved unchanged.
 * The operation is idempotent: re-running on an already-pruned spec is a no-op.
 *
 * Run this BEFORE split-spec.js whenever the category/inclusion list changes:
 *   node _tools/prune-spec.js && node _tools/split-spec.js
 */

const fs = require('fs');
const path = require('path');

const CATEGORIES = require('./api-categories.js');
const ROOT = path.resolve(__dirname, '..', 'assets', 'api');
const SRC = path.join(ROOT, 'swagger.json');
const OVERLAY_DIR = path.join(ROOT, 'descriptions-overlay');

const keep = new Set(CATEGORIES.flatMap(c => c.tags));
const spec = JSON.parse(fs.readFileSync(SRC, 'utf8'));

// 1. Keep only operations that carry at least one kept tag.
const beforeOps = Object.values(spec.paths).reduce((n, item) => n + Object.keys(item).length, 0);
const newPaths = {};
let keptOps = 0;
const droppedTags = new Set();
for (const p of Object.keys(spec.paths)) {
  const item = spec.paths[p];
  const kept = {};
  for (const m of Object.keys(item)) {
    const op = item[m];
    const tags = (op && Array.isArray(op.tags)) ? op.tags : [];
    if (tags.some(t => keep.has(t))) {
      kept[m] = op;
      keptOps++;
    } else {
      tags.forEach(t => { if (!keep.has(t)) droppedTags.add(t); });
    }
  }
  if (Object.keys(kept).length) newPaths[p] = kept;
}
spec.paths = newPaths;

// 2. Recompute the schema closure reachable from the kept paths (plus any
//    non-schema component buckets, which may $ref schemas too).
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

const allSchemas = (spec.components && spec.components.schemas) || {};
const seedRefs = new Set();
collectRefs(spec.paths, seedRefs);
for (const bucket of Object.keys(spec.components || {})) {
  if (bucket === 'schemas') continue;
  collectRefs(spec.components[bucket], seedRefs);
}

const closure = new Set();
const queue = [...seedRefs];
while (queue.length) {
  const name = schemaNameFromRef(queue.shift());
  if (name == null || closure.has(name) || !(name in allSchemas)) continue;
  closure.add(name);
  const inner = new Set();
  collectRefs(allSchemas[name], inner);
  for (const r of inner) queue.push(r);
}

const beforeSchemas = Object.keys(allSchemas).length;
const prunedSchemas = {};
for (const n of Object.keys(allSchemas)) {
  if (closure.has(n)) prunedSchemas[n] = allSchemas[n];
}
spec.components.schemas = prunedSchemas;

// 3. Prune the top-level tag list.
const beforeTags = (spec.tags || []).length;
if (Array.isArray(spec.tags)) spec.tags = spec.tags.filter(t => keep.has(t.name));

fs.writeFileSync(SRC, JSON.stringify(spec));

// 4. Prune the human-written description overlays so they don't keep entries for
//    endpoints that no longer exist in the spec. The split-spec overlay loader
//    treats the /api/ and /api/v1/ forms of a route as equivalent, so an entry
//    survives if either form is still present. Keys starting with "_" are
//    comments and are always kept.
const keptOpKeys = new Set();
for (const p of Object.keys(spec.paths)) {
  for (const m of Object.keys(spec.paths[p])) keptOpKeys.add(`${m.toUpperCase()} ${p}`);
}
function overlayKeyStillExists(key) {
  const sp = key.indexOf(' ');
  if (sp < 0) return true;
  const m = key.substring(0, sp).toUpperCase();
  const p = key.substring(sp + 1);
  if (keptOpKeys.has(`${m} ${p}`)) return true;
  if (p.startsWith('/api/v1/') && keptOpKeys.has(`${m} /api/${p.substring('/api/v1/'.length)}`)) return true;
  if (p.startsWith('/api/') && !/^\/api\/v\d+\//.test(p) && keptOpKeys.has(`${m} /api/v1/${p.substring('/api/'.length)}`)) return true;
  return false;
}
let overlayRemoved = 0;
if (fs.existsSync(OVERLAY_DIR) && fs.statSync(OVERLAY_DIR).isDirectory()) {
  for (const f of fs.readdirSync(OVERLAY_DIR).filter(n => n.endsWith('.json'))) {
    const file = path.join(OVERLAY_DIR, f);
    const entries = JSON.parse(fs.readFileSync(file, 'utf8'));
    const out = {};
    let removed = 0;
    for (const k of Object.keys(entries)) {
      if (k.startsWith('_') || overlayKeyStillExists(k)) out[k] = entries[k];
      else removed++;
    }
    if (removed) {
      fs.writeFileSync(file, JSON.stringify(out, null, 2) + '\n');
      overlayRemoved += removed;
      console.log(`  overlay ${f}: removed ${removed} dead entr${removed === 1 ? 'y' : 'ies'}`);
    }
  }
}

console.log(`Pruned swagger.json`);
console.log(`  operations: ${beforeOps} -> ${keptOps}`);
console.log(`  tags:       ${beforeTags} -> ${(spec.tags || []).length}`);
console.log(`  schemas:    ${beforeSchemas} -> ${Object.keys(prunedSchemas).length}`);
if (droppedTags.size) {
  console.log(`  removed tags (${droppedTags.size}): ${[...droppedTags].sort().join(', ')}`);
}
