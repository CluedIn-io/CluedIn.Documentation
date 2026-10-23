---
title: Power Fx advanced reference
url: https://documentation.cluedin.net/govern/rules/power-fx-advanced-reference
content_type: reference
section: Govern & improve > Rules
---

# Power Fx advanced reference

> reference: Facts, options, APIs.

This is the complete reference for Power Fx in CluedIn rules: how a formula is evaluated, which
context variables each rule scope supplies, the shape of the records those variables hold, and every
CluedIn custom function with its parameters, return value, side effects and failure behaviour. It is
written to be precise enough that a person - or an AI assistant such as Claude or ChatGPT - can write
a correct formula from it without trial and error.

For an introduction with simple examples, start with [Power Fx formulas](https://documentation.cluedin.net/govern/rules/power-fx-formulas.md).
Read this page when a formula needs to compose several actions, read related records or version
history, handle missing or malformed data deliberately, or run on Spark.

> **Note:** This reference describes the rule engine implementation as reviewed in October 2026 (Power Fx
packages 1.8.1). What is available in a given installation depends on its release and configuration.
Validate formula binding, scope variables, vocabulary mappings, error handling and the final record in
the target environment before promoting a rule.

## Rules for writing CluedIn Power Fx formulas

These rules summarise the rest of the page. Each one prevents a mistake that evaluates without an
error but silently does the wrong thing.

1. **A condition must return a Boolean.** Any other result type is logged and treated as `false`.
   Do not wrap a comparison in `If(..., true, false)`.
2. **An action must end with the record to apply.** The engine writes the *final value* of the
   formula back to the current record. A scalar, a table, or the original `Entity` after a setter call
   discards the change.
3. **Chain setters by nesting, not with `;`.** Pass the record returned by one setter into the next:
   `AddTag(SetVocabularyKeyValue(Entity, "k", "v"), "t")`. Nesting is always correct; a `;` sequence
   such as `SetEntityProperty(...); Entity` silently loses the change.
4. **Every branch of an action `If` returns a record.** Use `Entity` as the "do nothing" branch.
5. **Use the variable names of the scope.** `Entity` in data part, golden record and survivorship
   rules; `GoldenRecord` and `DataPart` in survivorship action conditions - `Entity` does not exist
   there.
6. **Read vocabulary values with `GetVocabularyKeyValue`, not with dot paths.**
   `Entity.Properties.customer.status` is invalid; `Properties` is a table of `Key`/`Value` rows.
7. **Vocabulary values are text.** Convert with `Value`, `DateValue` or `DateTimeValue` before numeric
   or date comparison, and format with `Text(...)` before writing a number or date back.
8. **A missing value is `Blank()`.** Test with `IsBlank`, default with `Coalesce`.
9. **Use current field names:** `BusinessDomain` (not `EntityType`), `PrimaryIdentifier` (not
   `OriginEntityCode`), `Identifiers` (not `Codes`).
10. **Field names passed to `SetEntityProperty` are exact and case-sensitive,** and some fields are
    read-only. A blocked write returns the original record without an error.
11. **Use vocabulary setters for properties, `SetEntityProperty` for top-level metadata.**
12. **Entity codes are full serialized codes** such as `/Person#Somewhere:customer-123` - entity type,
    origin and value - not a bare business identifier or a GUID.
13. **Lookups cost data store reads.** Bind a loaded record or relationship table once with `With`.
14. **Setters on a loaded record do not save it.** Only the current record is written back.
15. **Use only the ten CluedIn functions listed on this page** plus standard Power Fx functions.
    There are no CluedIn functions for HTTP calls, SQL, creating or deleting entities, editing edges,
    or removing tags.
16. **On Spark, the function set is smaller** and key or property names must be string literals.

## How formulas are evaluated

Power Fx is Microsoft's strongly typed, Excel-style formula language. The host decides which functions
and objects a formula can use. In CluedIn, formulas can use the standard Power Fx function library, the
context variables described below, and the CluedIn custom functions. Power Apps controls, connectors
and data sources are not available. See the
[Microsoft Power Fx overview](https://learn.microsoft.com/en-us/power-platform/power-fx/overview) for
the language itself.

The engine enables the `PowerFxV1` feature set, `Set`, mutation functions, JSON functions and regular
expression functions. Examples on this page use comma argument separators and dot decimals.

### Conditions return a Boolean

A condition - in a rule filter or a survivorship action condition - decides whether a record matches.
A `true` result matches. A successful evaluation that returns anything other than a Boolean is logged
and treated as `false`. An evaluation *error* is different: it is raised as an exception and logged in
the rule's execution log, not quietly turned into `false`.

```powerfx
Right(Entity.DisplayName, 1) = "t"
```

```powerfx
GetVocabularyKeyValue(Entity, "user.firstName") & " " &
GetVocabularyKeyValue(Entity, "user.lastName") =
GetVocabularyKeyValue(Entity, "user.fullName")
```

`&` joins text and `=` compares values, so the second formula is already a Boolean.

### Actions return the record to apply

A formula action evaluates the formula and maps its **final result** back onto the current record's
metadata, provided that result is a record. A scalar or table result gives the engine nothing to write
back.

```powerfx
SetVocabularyKeyValue(Entity, "user.fullName",
    GetVocabularyKeyValue(Entity, "user.firstName") & " " &
    GetVocabularyKeyValue(Entity, "user.lastName"))
```

The setter returns the record with its updated `Properties` table, and because it is the final value
of the formula, that record is applied. This matters most with `SetEntityProperty`, which builds and
returns a *new* record rather than changing the record it was given. See
[Carry the returned record forward](#carry-the-returned-record-forward).

### Blank values and explicit conversions

A missing vocabulary value is `Blank()`. Vocabulary values are always text, so convert them before
comparing numbers or dates. A failed conversion is an evaluation error, not `false`.

```powerfx
If(IsBlank(GetVocabularyKeyValue(Entity, "customer.age")),
    false,
    Value(GetVocabularyKeyValue(Entity, "customer.age")) >= 18)
```

This handles a missing age, but non-numeric text such as `"unknown"` still fails in `Value`. When
malformed data should count as a non-match, catch the error explicitly:

```powerfx
IfError(Value(GetVocabularyKeyValue(Entity, "customer.age")) >= 18, false)
```

`IfError` catches Power Fx error values, such as a failed conversion or the `NotFound` error from
`LoadEntityByEntityCode`. It does not catch .NET exceptions thrown by a function, which are listed per
function below.

## Rule scopes and context variables

The scope of a rule decides which variables the formula receives and which custom functions are
registered. A function being registered in a scope and a particular record supporting it are separate
questions: a function can be available yet return an empty result for a record that lacks the
metadata it needs.

| Scope | Variables | What they hold |
|---|---|---|
| Data part | `Entity` | The current data part |
| Entity (golden record) | `Entity` | The current golden record |
| Survivorship | `Entity` | The golden record context supplied for survivorship |
| Survivorship action condition | `GoldenRecord`, `DataPart` | The golden record and the candidate data part, separately |

In a survivorship action condition, `Entity` does not exist:

```powerfx
GetVocabularyKeyValue(DataPart, "customer.status") = "Active"
```

For how these scopes map onto the rule types in the UI, see [Rule types](https://documentation.cluedin.net/govern/rules/rule-types.md).

### Function availability by scope

| Function | Data part | Entity | Survivorship | Survivorship action condition |
|---|---|---|---|---|
| `GetVocabularyKeyValue` | Yes | Yes | Yes | Yes |
| `VocabularyKeyExists` | Yes | Yes | Yes | Yes |
| `FuzzyMatch` | Yes | Yes | Yes | Yes |
| `LoadEntityByEntityCode` | Yes | Yes | Yes | Yes |
| `GetVersionBranches` | No | Yes | Yes | Yes |
| `SetVocabularyKeyValue` | Yes | Yes | No | No |
| `SetEntityProperty` | Yes | Yes | No | No |
| `AddTag` | Yes | Yes | No | No |
| `LoadIncomingRelationships` | No | Yes | No | No |
| `LoadOutgoingRelationships` | No | Yes | No | No |

"Yes" means the function is registered in that scope. Setters and `AddTag` belong in actions; the
engine does not enforce a separate read-only function list for conditions, so do not rely on a
registration error to keep a setter out of a filter.

`GetVersionBranches(GoldenRecord)` is meaningful in a survivorship action condition;
`GetVersionBranches(DataPart)` returns an empty table because a data part is not a golden record. The
relationship loaders need both Entity scope and a record backed by a real CluedIn entity.

The Spark engine registers fewer functions - see [Spark execution](#spark-execution-has-a-smaller-function-set).

## The record schema

CluedIn converts its native metadata into Power Fx records and tables. The field names below are the
names a formula uses at runtime.

| Field | Power Fx type | Meaning |
|---|---|---|
| `DisplayName`, `Name` | Text or blank | Presentation name and underlying name |
| `BusinessDomain` | Text | The business domain (entity type), for example `/Person` |
| `PrimaryIdentifier` | Text | The origin entity code, serialized |
| `Description`, `Revision` | Text or blank | Description and revision metadata |
| `CreatedDate`, `ModifiedDate`, `DiscoveryDate` | Text or blank | Dates as **text** in round-trip (`O`) format |
| `Properties` | Table of `Key`, `Value` (text) | Vocabulary key values |
| `Tags`, `Aliases` | Single-column text tables | Each row has a `Value` field |
| `Identifiers` | Table | `Code`, `Key`, `Origin`, `Type`, `Value` text fields |
| `Uri` | Text or blank | Serialized URI |
| `DocumentMimeType`, `DocumentFileName`, `Encoding` | Text or blank | Document metadata |
| `DocumentSize` | Number or blank | Document size |
| `ProviderDefinitionId` | GUID or blank | Provider definition identifier |
| `OutgoingEdges`, `IncomingEdges` | Tables | Relationship edges carried on the record - see below |
| `_metadataId` | GUID | Internal identity used by the runtime; do not set it |

Golden records additionally expose `IsShadowEntity`, `IsExternalData` and `IsDeleted` (Boolean,
possibly blank), `ProviderDefinitionIds` (single-column GUID table), and `Providers` and
`VocabulariesUsed` (single-column text tables).

When the result is written back, `BusinessDomain` maps to the native `EntityType`,
`PrimaryIdentifier` to `OriginEntityCode`, and `Identifiers` to `Codes`. Formulas must use the
runtime names; `Entity.EntityType`, `Entity.OriginEntityCode` and `Entity.Codes` do not exist.

```powerfx
First(Entity.Tags).Value = "Reviewed"
```

```powerfx
CountRows(Entity.Identifiers) > 1
```

```powerfx
DateTimeValue(Entity.ModifiedDate) > DateTimeValue("2025-01-01")
```

Guard empty tables before using `First`, and handle blank or invalid date text where it can occur.

> **Warning:** The formula editor's IntelliSense uses a separate sample schema. It describes dates as date-time values
and omits `IncomingEdges`, while at runtime dates are text and both edge tables exist. When the editor
and the runtime disagree, the runtime schema on this page is the one that applies.

### Properties are rows, not fields

`Entity.Properties` is a table whose rows have `Key` and `Value` text fields. A vocabulary key name
containing dots is a string stored in `Key`, not a nested path.

```powerfx
LookUp(Entity.Properties, Key = "customer.status", Value)
```

This reads the literally stored key. `GetVocabularyKeyValue` first resolves the vocabulary definition
and its destination mapping, so it can intentionally read a *different* stored key. Use the custom
function whenever you want CluedIn's vocabulary semantics - which is almost always.

### Edge rows on the record

`Entity.OutgoingEdges` and `Entity.IncomingEdges` rows have these text fields:

| Field | Meaning |
|---|---|
| `EdgeType` | Serialized edge type |
| `ToReferenceCode`, `ToReferenceName`, `ToReferenceEntityId` | Destination entity code, name and ID |
| `FromReferenceCode`, `FromReferenceName`, `FromReferenceEntityId` | Source entity code, name and ID |

### Loaded relationships have a different shape

`LoadIncomingRelationships` and `LoadOutgoingRelationships` query the primary data store and return
rows with only two text fields, `EdgeType` and `EntityCode`, where `EntityCode` identifies the entity
on the other end. They do not return the seven-column edge rows above, and they do not return the
related records themselves.

| Source | `EntityCode` / codes identify | Fields |
|---|---|---|
| `LoadIncomingRelationships(Entity)` | The source of each incoming edge | `EdgeType`, `EntityCode` |
| `LoadOutgoingRelationships(Entity)` | The destination of each outgoing edge | `EdgeType`, `EntityCode` |
| `Entity.OutgoingEdges` | Both ends, in separate fields | Seven edge fields |

Loading can find relationships that are not carried on the record, at the cost of a data store read.
A `Filter` applied to the loaded table runs after loading; it does not narrow the query.

## Custom function quick reference

CluedIn adds ten function names. All parameters are required. `SetEntityProperty` has five overloads,
one per value type; every other function has one signature.

| Function | Signature | Returns | Scopes |
|---|---|---|---|
| [`GetVocabularyKeyValue`](#getvocabularykeyvalue) | `(record, keyText)` | Text or blank | All |
| [`VocabularyKeyExists`](#vocabularykeyexists) | `(record, keyText)` | Boolean | All |
| [`SetVocabularyKeyValue`](#setvocabularykeyvalue) | `(record, keyText, valueText)` | Updated record | Data part, Entity |
| [`SetEntityProperty`](#setentityproperty) | `(record, propertyText, value)` | Rebuilt record, or error | Data part, Entity |
| [`AddTag`](#addtag) | `(record, tagText)` | Updated record | Data part, Entity |
| [`FuzzyMatch`](#fuzzymatch) | `(leftText, rightText)` | Number from 0 to 1 | All |
| [`LoadEntityByEntityCode`](#loadentitybyentitycode) | `(entityCodeText)` | Golden record, or error | All |
| [`LoadIncomingRelationships`](#loadincomingrelationships) | `(record)` | Table of `EdgeType`, `EntityCode` | Entity |
| [`LoadOutgoingRelationships`](#loadoutgoingrelationships) | `(record)` | Table of `EdgeType`, `EntityCode` | Entity |
| [`GetVersionBranches`](#getversionbranches) | `(record)` | Table of branches | Entity, Survivorship, Survivorship action condition |

**Record arguments.** Pass the scope's context variables, or records returned by CluedIn functions.
A record you build yourself with `{ ... }` is accepted by the type checker but is not equivalent: the
functions expect CluedIn's internal table wrappers and, for history and relationships, a registered
runtime identity.

**"Updated record"** is the runtime value. It is not a success flag, not a saved database object, and
not a promise that every field will persist. Only the final record of an action is written back, and
only to the current record.

**Vocabulary mappings.** The vocabulary readers and the vocabulary setter resolve a key through the
organization's vocabulary definitions, including its destination mapping, on every call. Register the
vocabulary key - and any mapping - before relying on these functions. See
[Vocabulary keys](https://documentation.cluedin.net/model/vocabularies/vocabulary-keys.md).

## GetVocabularyKeyValue

Reads a vocabulary value from a record, after resolving the vocabulary definition and its destination
mapping.

```powerfx
GetVocabularyKeyValue(record, keyText)
```

| Parameter | Type | Description |
|---|---|---|
| `record` | Record | A CluedIn context record, or a record returned by a CluedIn function |
| `keyText` | Text | The full vocabulary key name, such as `customer.status` |

**Returns** the matching value as text. Returns blank when the vocabulary key is not defined, when the
mapped key has no row, or when `Properties` is not a CluedIn properties table. A blank result does not
say which of these happened.

**Effect** none; reads the vocabulary definitions and the record.

```powerfx
GetVocabularyKeyValue(Entity, "customer.status") = "Active"
```

```powerfx
Coalesce(GetVocabularyKeyValue(Entity, "customer.region"), "Unknown")
```

The second formula is a value, not a condition; use it inside a comparison or a setter.

**Failure behaviour.** The function expects at most one matching row. If `Properties` contains
duplicate rows for the key, it throws instead of returning the first. Failures of the vocabulary
service are not converted to blank.

## VocabularyKeyExists

Tests whether the record has a row for a registered vocabulary key, after destination mapping. It tests
*presence*, not whether the value is useful.

```powerfx
VocabularyKeyExists(record, keyText)
```

| Parameter | Type | Description |
|---|---|---|
| `record` | Record | A CluedIn record containing `Properties` |
| `keyText` | Text | The full registered vocabulary key name |

**Returns** `true` when the mapped key has at least one row; otherwise `false`. An undefined vocabulary
key returns `false`, even if a row with that raw key exists.

**Effect** none.

```powerfx
VocabularyKeyExists(Entity, "customer.email")
```

A row with an empty value still counts as present. To require a populated value:

```powerfx
VocabularyKeyExists(Entity, "customer.email") &&
    !IsBlank(GetVocabularyKeyValue(Entity, "customer.email"))
```

With duplicate rows, `VocabularyKeyExists` returns `true` while `GetVocabularyKeyValue` throws. Not
available on Spark.

## SetVocabularyKeyValue

Updates the value of a vocabulary key in the record's `Properties`, or appends it if absent.

```powerfx
SetVocabularyKeyValue(record, keyText, valueText)
```

| Parameter | Type | Description |
|---|---|---|
| `record` | Record | The CluedIn record to update - normally `Entity` |
| `keyText` | Text | The full vocabulary key name |
| `valueText` | Text | The text to store; format numbers and dates explicitly with `Text` |

**Returns** the record with the updated `Properties`. If `Properties` is not a CluedIn properties table,
returns the record unchanged.

**Effect** updates the existing row for the mapped key, or appends a new row.

```powerfx
SetVocabularyKeyValue(Entity, "customer.status", "Active")
```

```powerfx
SetVocabularyKeyValue(Entity, "customer.reviewDate",
    Text(DateValue("2026-10-22"), "yyyy-mm-dd"))
```

```powerfx
SetVocabularyKeyValue(Entity, "finance.salaryGrade",
    If(Value(GetVocabularyKeyValue(Entity, "finance.salary")) >
       Value(GetVocabularyKeyValue(Entity, "finance.targetSalary")),
       "Above Target", "Below Target"))
```

The value is always stored as text; the setter does not change the vocabulary key's data type.

**Undefined keys.** If the key has no vocabulary definition, the setter appends a row using the raw
`keyText` - it does not create the definition. The readers will still return blank and `false` for that
key. Repeating the write can append duplicate rows rather than updating the first one. Register the key
before treating this function as a reliable upsert.

The setter does not delete rows, does not treat blank as "delete", and does not save any other record.

## SetEntityProperty

Sets a top-level metadata field and returns a **rebuilt** record. Use it for fields such as
`DisplayName`, `Description` or `BusinessDomain`. Use `SetVocabularyKeyValue` for vocabulary values.

```powerfx
SetEntityProperty(record, propertyText, value)
```

| Parameter | Type | Description |
|---|---|---|
| `record` | Record | The CluedIn record - normally `Entity` |
| `propertyText` | Text | The exact, case-sensitive runtime field name from [the record schema](#the-record-schema) |
| `value` | Text, Number, Boolean, DateTime or GUID | The new value; the overload is chosen by its type |

**Returns** a rebuilt record on success; the **original record** if the field is read-only (with a
warning in the log, but no error); a `NotFound` error of severity `Severe` if the field does not exist.
A record that cannot be converted throws.

```powerfx
SetEntityProperty(Entity, "DisplayName", "Ben")
```

```powerfx
SetEntityProperty(Entity, "BusinessDomain", "/Person")
```

```powerfx
SetEntityProperty(Entity, "DocumentSize", 1024)
```

**Match the field's type.** Five overloads do not mean every field accepts five types. Date fields are
text at runtime, so set them with formatted text; a value of the wrong type can become blank or be
ignored when the record is written back.

```powerfx
SetEntityProperty(Entity, "ModifiedDate", Text(DateValue("2026-10-22"), "yyyy-mm-dd"))
```

### Read-only fields

A write to any of these fields is blocked: the function logs a warning and returns the original record.
A successful evaluation is therefore not proof that the field changed.

| Blocked runtime field | Native property |
|---|---|
| `ProviderDefinitionId` | `ProviderDefinitionId` |
| `Properties` | `Properties` |
| `OutgoingEdges` | `OutgoingEdges` |
| `Identifiers` | `Codes` |
| `PrimaryIdentifier` | `OriginEntityCode` |
| `DiscoveryDate` | `DiscoveryDate` |
| `IsShadowEntity` | `IsShadowEntity` |
| `IsExternalData` | `IsExternalData` |
| `IsDeleted` | `IsDeleted` |

The list is not a complete persistence policy. Edges are never written back, and `VocabulariesUsed` is
skipped, so a field missing from this table is not guaranteed to be writable.

**Table fields cannot be set.** `SetEntityProperty` has no table overload, so it cannot replace
`Aliases`, `Tags`, `Identifiers`, `Properties` or the edge tables. Use `AddTag` for tags, the
vocabulary setter for properties, and the **Add Alias** and **Remove Alias** rule actions for aliases.

### Carry the returned record forward

Because `SetEntityProperty` returns a new record, the next function must receive that record and the
formula must end with it.

```powerfx
AddTag(
    SetEntityProperty(Entity, "DisplayName", "Reviewed customer"),
    "Reviewed")
```

Do **not** write:

```powerfx
SetEntityProperty(Entity, "DisplayName", "Reviewed customer");
Entity
```

The formula finishes with the original `Entity`, so the change to `DisplayName` is discarded.

## AddTag

Adds one tag to the record, skipping it if an identical tag already exists.

```powerfx
AddTag(record, tagText)
```

| Parameter | Type | Description |
|---|---|---|
| `record` | Record | A CluedIn record with a `Tags` field |
| `tagText` | Text | The tag to add |

**Returns** the record with the updated `Tags` table.

```powerfx
AddTag(Entity, "Reviewed")
```

```powerfx
If(GetVocabularyKeyValue(Entity, "customer.status") = "Active",
    AddTag(Entity, "Active customer"),
    Entity)
```

**Comparison.** Duplicate detection is exact and case-sensitive, with no trimming: `Reviewed` and
`reviewed` are different tags. Empty text is not rejected. Normalise the input with `Trim` or
`Proper` if your tag taxonomy needs it.

**Failure behaviour.** Throws if the record has no `Tags` field or cannot be converted. There is no
`RemoveTag` function. On Spark, a missing `Tags` field is silently ignored instead.

## FuzzyMatch

Returns a similarity score between two strings, from `0` (no similarity) to `1` (identical), based on
the Sift4 edit distance. It compares two values; it does not find or merge records.

```powerfx
FuzzyMatch(leftText, rightText)
```

| Parameter | Type | Description |
|---|---|---|
| `leftText` | Text | The first string |
| `rightText` | Text | The second string |

**Returns** a Number. Identical strings return `1`. Otherwise the score is
`Max(0, 1 - distance / Max(Len(leftText), Len(rightText)))`, where `distance` is the Sift4 distance
with a maximum offset of 2.

**Effect** local calculation only.

```powerfx
FuzzyMatch(
    Lower(Trim(GetVocabularyKeyValue(Entity, "customer.legalName"))),
    Lower(Trim(GetVocabularyKeyValue(Entity, "customer.tradingName")))
) >= 0.85
```

The `0.85` threshold is illustrative; tune it against records you know should and should not match.

**Edge cases.** The function does no case or whitespace normalisation - do it yourself, as above. Two
empty strings return `1`; one empty string returns `0`. Not available on Spark.

## LoadEntityByEntityCode

Loads a golden record from the primary data store by its entity code.

```powerfx
LoadEntityByEntityCode(entityCodeText)
```

| Parameter | Type | Description |
|---|---|---|
| `entityCodeText` | Text | A full serialized entity code: `/<BusinessDomain>#<Origin>:<Value>` |

**Returns** the full golden record, with every field in [the record schema](#the-record-schema). If no
entity has that code, returns a `NotFound` error of severity `Moderate`.

**Effect** one read from the primary data store per call. The loaded record is registered with the
runtime, so it can be passed to `GetVocabularyKeyValue` and `GetVersionBranches`.

```powerfx
LoadEntityByEntityCode("/Person#Somewhere:customer-123").DisplayName
```

```powerfx
With(
    {customer: LoadEntityByEntityCode("/Person#Somewhere:customer-123")},
    GetVocabularyKeyValue(customer, "customer.status") = "Active"
)
```

A code is built from the business domain, origin and value. A business identifier on its own, or a
database GUID, is not an entity code. Codes can be assembled from vocabulary values:

```powerfx
SetVocabularyKeyValue(Entity, "product.exchangeRate",
    GetVocabularyKeyValue(
        LoadEntityByEntityCode("/ExchangeRate#CurrencyCode:" &
            GetVocabularyKeyValue(Entity, "product.localCurrencyCode")),
        "currency.exchangeRate"))
```

See [Identifiers](https://documentation.cluedin.net/model/identifiers.md) for how entity codes are formed.

**Missing entities.** To treat a missing entity as a non-match rather than an error:

```powerfx
IfError(
    GetVocabularyKeyValue(
        LoadEntityByEntityCode("/Person#Somewhere:customer-123"),
        "customer.status") = "Active",
    false)
```

**Failure behaviour.** A malformed code and data store failures are thrown, not returned as
`NotFound`, and `IfError` does not catch them.

**No cross-record saves.** Setters applied to a loaded record change only the value in the formula. The
action writes its final record back to the *current* record, never to the loaded one. Read from loaded
records; write to `Entity`.

## LoadIncomingRelationships

Loads the relationships that point *to* the record. The record is the destination; each returned
`EntityCode` is the source.

```powerfx
LoadIncomingRelationships(record)
```

| Parameter | Type | Description |
|---|---|---|
| `record` | Record | A record backed by a real CluedIn entity - normally `Entity` in Entity scope |

**Returns** a table of `EdgeType` (text) and `EntityCode` (text, the source entity's code). Returns an
empty table when there are no relationships, or when the record is not backed by a real entity.

**Scope** Entity only.

```powerfx
CountRows(LoadIncomingRelationships(Entity)) > 0
```

```powerfx
CountRows(Filter(LoadIncomingRelationships(Entity), EdgeType = "/WorksFor")) > 0
```

The `EdgeType` value must match the serialized edge type stored in your data. A table on its own is not
a valid condition; reduce it to a Boolean with `CountRows`, `IsEmpty` or similar.

**Cost and timeout.** All rows are loaded before the table is returned; there is no paging, row limit
or edge-type filter on the query. Loading is limited by
`Rules.PowerFx.LoadRelationsTimeoutInMilliseconds` (default 10000 ms). When the limit is detected the
function returns a `Timeout` error of severity `Moderate`. The limit is checked while edges are read,
so it is not a hard guarantee against a data store call that hangs. Other data store failures are
thrown.

## LoadOutgoingRelationships

Loads the relationships that point *from* the record. The record is the source; each returned
`EntityCode` is the destination.

```powerfx
LoadOutgoingRelationships(record)
```

Parameters, return shape, scope, timeout and failure behaviour are the same as
[`LoadIncomingRelationships`](#loadincomingrelationships), with `EntityCode` taken from the destination.

```powerfx
With(
    {relationships: LoadOutgoingRelationships(Entity)},
    CountRows(Filter(relationships, EdgeType = "/WorksFor")) > 0 &&
    CountRows(relationships) < 50
)
```

`With` loads the table once for several checks within the formula. It does not cache between records
or rule runs.

To read a related record, pass the code on:

```powerfx
With(
    {employer: First(Filter(LoadOutgoingRelationships(Entity), EdgeType = "/WorksFor"))},
    !IsBlank(employer) &&
    GetVocabularyKeyValue(LoadEntityByEntityCode(employer.EntityCode), "organization.country") = "DK"
)
```

Each `LoadEntityByEntityCode` adds another data store read. The returned rows are neither ordered nor
deduplicated. See [Golden record relations](https://documentation.cluedin.net/master/golden-records/golden-record-relations.md).

## GetVersionBranches

Returns the version history branches already held for a golden record, with each branch's versions as
a nested table. It does not query the data store for history.

```powerfx
GetVersionBranches(record)
```

| Parameter | Type | Description |
|---|---|---|
| `record` | Record | A golden record: `Entity` in Entity or survivorship scope, `GoldenRecord` in a survivorship action condition, or a record from `LoadEntityByEntityCode` |

**Scopes** Entity, Survivorship and Survivorship action condition.

**Returns** a table of branches:

| Branch field | Type | Meaning |
|---|---|---|
| `Name` | Text | The branch name |
| `Parts` | Table | The branch's versions, **newest first** |

Each row of `Parts`:

| Part field | Type | Meaning |
|---|---|---|
| `Date` | Text | Version date in round-trip (`O`) format |
| `Branch` | Text | Branch name, or empty text |
| `ChangeType` | Text | Serialized change type |
| `IsHead` | Boolean | Whether this is the head version of the branch |
| `InputSource` | Text | The data part's input source, or empty text |
| `EntityData` | Record | The original data part, in the record schema |
| `ProcessedEntityData` | Record | The processed data part, in the record schema |

`EntityData` and `ProcessedEntityData` can be passed to `GetVocabularyKeyValue`. They are data parts,
so passing them to `GetVersionBranches` returns an empty table.

**Empty results.** The table is empty when the record is not a golden record, is not backed by a real
entity, or has no branches. An empty table does not on its own mean "no history". Branches are not
sorted; only `Parts` is ordered.

```powerfx
First(First(GetVersionBranches(Entity)).Parts).EntityData.Name
```

In real rules, pick a branch by name and guard against empty tables:

```powerfx
With(
    {crm: LookUp(GetVersionBranches(Entity), Name = "crm")},
    !IsBlank(crm) && !IsEmpty(crm.Parts) &&
    GetVocabularyKeyValue(First(crm.Parts).EntityData, "customer.status") = "Active"
)
```

The branch name `crm` is illustrative. See [History](https://documentation.cluedin.net/master/golden-records/history.md) for how branches
relate to sources.

### Choose which versions to compare

A branch row is not a data part, so `GetVocabularyKeyValue(ThisRecord, ...)` over the branch table
reads nothing. Decide which versions a rule means, and reach into `Parts` accordingly. These are three
different comparisons and can give different answers.

| Comparison | Versions considered | Expression over each branch |
|---|---|---|
| Latest per branch | The newest version in every branch | `First(Parts)` |
| Branch heads | Versions marked as the head of their branch | `Filter(Parts, IsHead)` |
| All versions | Every historical version in every branch | `Parts` |

```powerfx
// Latest per branch: the highest revenue among each branch's newest version
Max(GetVersionBranches(Entity),
    Value(GetVocabularyKeyValue(First(Parts).EntityData, "company.revenue")))
```

```powerfx
// Branch heads
Max(GetVersionBranches(Entity),
    Max(Filter(Parts, IsHead), Value(GetVocabularyKeyValue(EntityData, "company.revenue"))))
```

```powerfx
// All versions
Max(GetVersionBranches(Entity),
    Max(Parts, Value(GetVocabularyKeyValue(EntityData, "company.revenue"))))
```

Inside the inner `Max` or `Filter`, field names such as `EntityData` and `IsHead` refer to the part
row. Use `ProcessedEntityData` instead of `EntityData` to compare the values after processing rather
than as they arrived. `Max` ignores blank values, and `Value` fails on non-numeric text.

## Patterns

### Compare the latest value across branches

Does the newest version in every branch agree on a value?

```powerfx
With(
    {branches: GetVersionBranches(Entity)},
    CountRows(branches) > 1 &&
    CountRows(
        Distinct(
            ForAll(branches,
                GetVocabularyKeyValue(First(Parts).EntityData, "customer.status")),
            Value
        )
    ) = 1
)
```

Use `ProcessedEntityData` instead of `EntityData` to compare processed versions. Blank values also
collapse into one distinct value, so add a non-blank check if agreement must be on a populated value.

### Apply several changes in one action

```powerfx
AddTag(
    SetVocabularyKeyValue(
        SetEntityProperty(Entity, "DisplayName", "Reviewed customer"),
        "customer.reviewStatus", "Complete"),
    "Reviewed")
```

Read it inside out: each call receives the previous call's record, and the outermost call returns the
record that is applied. The changes are not one transaction - validate the final record.

### Update the current record based on a related one

```powerfx
With(
    {related: LoadEntityByEntityCode("/Person#Somewhere:customer-123")},
    If(GetVocabularyKeyValue(related, "customer.status") = "Active",
        AddTag(Entity, "Related active customer"),
        Entity)
)
```

The loaded record is only read; the action returns `Entity` in both branches. Wrap the lookup in
`IfError` if the related entity may not exist.

### Normalise a value only when it is present

```powerfx
If(IsBlank(GetVocabularyKeyValue(Entity, "customer.email")),
    Entity,
    SetVocabularyKeyValue(Entity, "customer.email",
        Lower(Trim(GetVocabularyKeyValue(Entity, "customer.email")))))
```

### Flag a pattern with a regular expression

```powerfx
If(IsMatch(GetVocabularyKeyValue(Entity, "customer.email"), "^[^@\s]+@[^@\s]+\.[^@\s]+$"),
    Entity,
    AddTag(Entity, "Invalid email"))
```

Regular expressions are limited by `Rules.PowerFx.RegExTimeoutInMilliseconds`.

## Common mistakes

| Wrong | Why | Correct |
|---|---|---|
| `Entity.Properties.customer.status` | `Properties` is a table, not a nested record | `GetVocabularyKeyValue(Entity, "customer.status")` |
| `Entity.EntityType`, `Entity.OriginEntityCode`, `Entity.Codes` | Older names | `Entity.BusinessDomain`, `Entity.PrimaryIdentifier`, `Entity.Identifiers` |
| `SetEntityProperty(Entity, "DisplayName", "X"); Entity` | Ends with the unchanged record | `SetEntityProperty(Entity, "DisplayName", "X")` |
| `SetEntityProperty(Entity, "DisplayName", "X"); AddTag(Entity, "t")` | `AddTag` starts from the original record, so the new display name is lost | `AddTag(SetEntityProperty(Entity, "DisplayName", "X"), "t")` |
| `If(cond, AddTag(Entity, "t"))` | The false branch returns blank, not a record | `If(cond, AddTag(Entity, "t"), Entity)` |
| `If(x > 5, true, false)` | Redundant | `x > 5` |
| `GetVocabularyKeyValue(Entity, "order.total") > 100` | Compares text with a number | `Value(GetVocabularyKeyValue(Entity, "order.total")) > 100` |
| `SetVocabularyKeyValue(Entity, "order.total", 100)` | The value parameter is text | `SetVocabularyKeyValue(Entity, "order.total", Text(100))` |
| `SetEntityProperty(Entity, "displayname", "X")` | Field names are case-sensitive | `SetEntityProperty(Entity, "DisplayName", "X")` |
| `SetEntityProperty(Entity, "IsDeleted", true)` | Read-only; silently ignored | Not settable from a formula |
| `SetEntityProperty(Entity, "Aliases", ...)` | `Aliases` is a table; there is no table overload | The **Add Alias** rule action |
| `GetVocabularyKeyValue(ThisRecord, "k")` over `GetVersionBranches(Entity)` | A branch row has only `Name` and `Parts` | `GetVocabularyKeyValue(First(Parts).EntityData, "k")` |
| `GetVocabularyKeyValue(First(LoadOutgoingRelationships(Entity)), "k")` | A relationship row has only `EdgeType` and `EntityCode` | `GetVocabularyKeyValue(LoadEntityByEntityCode(First(LoadOutgoingRelationships(Entity)).EntityCode), "k")` |
| `GetVocabularyKeyValue(Entity, "customer.status")` in a survivorship action condition | `Entity` does not exist in that scope | `GetVocabularyKeyValue(DataPart, "customer.status")` |
| `LoadEntityByEntityCode("5452407DH")` | Not a full entity code | `LoadEntityByEntityCode("/Customer#Erp:5452407DH")` |
| `SetVocabularyKeyValue(LoadEntityByEntityCode(code), "k", "v")` | The loaded record is never saved | Write to `Entity`; update the other record with its own rule |
| `LoadIncomingRelationships(Entity)` in a data part rule | Entity scope only | Use it in a golden record rule |

## Errors and operational behaviour

The engine distinguishes three outcomes. Diagnose them separately in the rule's execution log.

- **A Power Fx error value** at the top level - from a failed conversion, `NotFound` or `Timeout` - is
  raised as a Power Fx error.
- **Any other exception** during evaluation is raised as an evaluation exception.
- **A successful non-Boolean condition result** is logged and treated as `false`.

| Situation | Behaviour |
|---|---|
| Vocabulary key not defined, read | `GetVocabularyKeyValue` returns blank; `VocabularyKeyExists` returns `false` |
| Vocabulary key has no row | Blank / `false` |
| `Properties` is not a CluedIn properties table | Readers return blank / `false`; the setter returns the record unchanged |
| Duplicate rows for a key | `GetVocabularyKeyValue` throws; `VocabularyKeyExists` returns `true` |
| `SetEntityProperty` on a field that does not exist | `NotFound` error, severity `Severe` |
| `SetEntityProperty` on a read-only field | Warning logged; original record returned |
| `LoadEntityByEntityCode` finds nothing | `NotFound` error, severity `Moderate` |
| Relationship loading exceeds its timeout | `Timeout` error, severity `Moderate` |
| History or relationships on a record without runtime identity | Empty table |
| A value cannot be converted when written back | Logged and skipped; the field keeps its old value |

### Write-back is not a transaction

After evaluation, the final record is mapped onto the current record field by field. Conversion
failures are logged and skipped; there is no all-or-nothing validation or rollback. A formula that
evaluates successfully can still leave a field unchanged - check the result, especially for dates,
numbers, URIs and Booleans.

### Keep data store work visible

`LoadEntityByEntityCode` and the relationship loaders read the data store inside formula evaluation,
for every record the rule processes. The vocabulary functions also resolve definitions on every call.
Bind repeated results with `With`, and keep lookups to what the business rule needs. There is no single
global evaluation deadline; regular expressions, relationship loading and the editor's evaluation
endpoint each have their own limit.

## Configuration

| Setting | Default | Effect |
|---|---|---|
| `Rules.PowerFx.RegExTimeoutInMilliseconds` | 1000 ms | Timeout for regular expression functions |
| `Rules.PowerFx.MaxExpressionLength` | 10000 characters | Maximum formula length; `0` disables the limit. Applies to formulas parsed without explicit parser options, such as conditions |
| `Rules.PowerFx.LoadRelationsTimeoutInMilliseconds` | 10000 ms | Timeout checked by the relationship loaders |

## Formula editor endpoints

The Rule Builder's formula editor uses these endpoints. Each takes a `scope` query parameter, which
defaults to `Entity`.

| Method and route | Purpose |
|---|---|
| `GET /api/powerfx/context` | Returns a sample context for the scope |
| `POST /api/powerfx/lsp` | Language server requests (IntelliSense, diagnostics); the body is forwarded as-is |
| `POST /api/powerfx/eval` | Evaluates an expression against a supplied context |

The `context` field of an evaluation request is a JSON **string**, not a nested object:

```json
{
  "context": "{\"Entity\":{\"DisplayName\":\"Test\"}}",
  "expression": "Right(Entity.DisplayName, 1) = \"t\""
}
```

The endpoint parses, checks and evaluates with a two-second limit, and returns the result, tokens and
parse information. Errors are returned as content with HTTP 200. The endpoint does not set up the rule
runtime or registered records, so the vocabulary, lookup, relationship and history functions cannot
be validated with it. Test those through a real rule run.

## Spark execution has a smaller function set

Rules executed on Spark use a separate compatibility checker and row evaluator. A function available
in Entity scope is not automatically available on Spark.

| Function | Spark actions | Spark conditions |
|---|---|---|
| `GetVocabularyKeyValue` | Yes | Yes |
| `SetVocabularyKeyValue` | Yes | No |
| `SetEntityProperty` (all overloads) | Yes | No |
| `AddTag` | Yes | No |
| `VocabularyKeyExists` | No | No |
| `FuzzyMatch` | No | No |
| `LoadEntityByEntityCode` | No | No |
| `LoadIncomingRelationships` | No | No |
| `LoadOutgoingRelationships` | No | No |
| `GetVersionBranches` | No | No |

Additional Spark requirements:

- The key or property name passed to `GetVocabularyKeyValue`, `SetVocabularyKeyValue` and
  `SetEntityProperty` must be a **string literal**. `"customer." & "status"` is rejected, because
  mappings and columns are resolved before the rows are distributed.
- A condition must compile to a Boolean.
- The checker binds against a record containing only `Properties` and `Tags`; the row evaluator also
  carries `Name` and `EntityType`. Other fields are not available.

Behaviour also differs from the standard engine:

| Situation | Standard engine | Spark |
|---|---|---|
| Vocabulary key with no mapping | `GetVocabularyKeyValue` returns blank | Falls back to the raw key |
| `SetEntityProperty` on a missing field | `NotFound` error | Returns the original record |
| `AddTag` on a record without `Tags` | Throws | No-op |

## Extending the function library

Custom functions are .NET classes derived from `ExpressionRuleEngineReflectionFunctionBase`. At
startup, CluedIn scans its assemblies for non-abstract subclasses and registers them; when a formula
engine is created for a scope, every function whose `IsCompatibleWithScope` accepts that scope is added
to it.

| Responsibility | What to implement |
|---|---|
| Name and signature | Pass the formula name, return type and parameter types to the base constructor |
| Invocation | An `Execute` method, as expected by Power Fx `ReflectionFunction` |
| Runtime services | The base class sets `ConfigType` to `ExpressionRuleEngineRuntimeConfig`, which gives access to the execution context. Set it to `null` if the function needs none, as `FuzzyMatch` does |
| Scope | `IsCompatibleWithScope` for the rule scopes the function supports |
| Data | Return records and tables with stable field names, and register runtime metadata if other functions must recognise the records |
| Errors | Return explicit Power Fx errors, or document exceptions and empty results |

A separate `CluedIn.PowerFx.CustomFunctions` package contains a second implementation of
`LoadEntityByEntityCode` that returns an empty record, not `NotFound`, for a missing entity. It is the
same formula name, not an additional function. Do not install both without checking which is
registered; the behaviour documented on this page is the core engine's.

## Corrections to older descriptions

Earlier material - including the beta-era overview of Power Fx expression rules, and content that AI
assistants may have learned from - describes Power Fx in CluedIn differently. Where they conflict, this
page is current.

| Older description | Current behaviour |
|---|---|
| Four custom functions | Ten function names, including fuzzy matching, entity lookup, relationship loading, key existence and version branches |
| Power Fx SDK 1.2 | Power Fx 1.8.1 |
| A single `Entity` context | Scope-specific; `GoldenRecord` and `DataPart` in survivorship action conditions |
| `EntityType`, `OriginEntityCode`, `Codes` | `BusinessDomain`, `PrimaryIdentifier`, `Identifiers` |
| Formulas cannot read other records | `LoadEntityByEntityCode` and the relationship loaders read the data store |
| A missing value is empty or null | `GetVocabularyKeyValue` returns `Blank()`; `VocabularyKeyExists` tests presence |
| Planned functions for HTTP, queries, entity creation and so on | Not implemented; the ten functions on this page are the complete CluedIn set |

## Related articles

- [Power Fx formulas](https://documentation.cluedin.net/govern/rules/power-fx-formulas.md) - introduction and examples
- [Rule types](https://documentation.cluedin.net/govern/rules/rule-types.md) - which rules use which scope
- [Creating a rule](https://documentation.cluedin.net/govern/rules/create-rule.md) - where formulas go in the Rule Builder, and how to read the execution log
- [Vocabulary keys](https://documentation.cluedin.net/model/vocabularies/vocabulary-keys.md) - the keys formulas read and write
- [Identifiers](https://documentation.cluedin.net/model/identifiers.md) - how entity codes are formed
- [History](https://documentation.cluedin.net/master/golden-records/history.md) - the branches `GetVersionBranches` returns

Up: [Rules](https://documentation.cluedin.net/govern/rules.md)
