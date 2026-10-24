---
layout: cluedin
title: Power Fx formulas
parent: Rules
grand_parent: Govern & improve
nav_order: 50
permalink: /govern/rules/power-fx-formulas
content_type: reference
redirect_from: ["/management/rules/power-fx-formulas"]
source_path: docs/080-management/rules/040-power-fx-formulas-in-rules.md
last_modified: 2026-10-22
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article, you will learn about Power Fx formulas that you can use in the Rule Builder to set up filters, conditions, and actions.

<div class="videoFrame">
<iframe src="https://player.vimeo.com/video/1061960696?h=3ba16f6d8a&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write" title="Power FX formulas in CluedIn"></iframe>
</div>

Power Fx is a general-purpose, low-code, strong-typed, and functional programming language developed by Microsoft. Power Fx enables you to build and customize applications, workflows, and other solutions by writing simple, declarative expressions rather than traditional code. You can work with Power Fx using _Excel-like formulas_, which makes it intuitive both for technical and business users. For more information, see [Microsoft Power Fx overview](https://learn.microsoft.com/en-us/power-platform/power-fx/overview).

In CluedIn, you can use Power Fx formulas in the Rule Builder for querying, equality testing, decision making, type conversion, and string manipulation based on the supported properties of a data part or a golden record.

For the full behaviour of every function - parameters, return values, scopes, errors and Spark limits - see [Power Fx advanced reference](/govern/rules/power-fx-advanced-reference).

## Power Fx formulas in rules

You can use Power Fx formulas in the following types of rules:

- Data part rules – formulas are available in filters and actions (conditions and formula action).

- Survivorship rules – formulas are available in filters and actions (conditions). The formula action is not available in survivorship rules.

- Golden record rules – formulas are available in filters and actions (conditions and formula action).

A condition must return `true` or `false`. A formula action must return the record to apply - see [Combine several changes](#combine-several-changes).

### The context variables

A Power Fx formula works against a _context_: a variable that holds a sandboxed copy of the record the rule is processing. Which variables exist depends on where the formula runs.

| Where the formula runs | Variables | What they hold |
|---|---|---|
| Data part rules | `Entity` | The current data part |
| Golden record rules | `Entity` | The current golden record |
| Survivorship rule filters | `Entity` | The golden record |
| Survivorship action conditions, such as **Latest Matching Condition** | `DataPart`, `GoldenRecord` | The candidate data part, and the golden record, separately |

In a survivorship action condition there is no `Entity` variable. Use `DataPart` for the candidate data part's values:

```powerfx
GetVocabularyKeyValue(DataPart, "customer.status") = "Active"
```

![A rule condition of type Formula that checks whether firstName and lastName concatenated differ from fullName, using GetVocabularyKeyValue on Entity]({{ "/assets/images/management/rules/power-fx-formula-example.png" | relative_url }})

Consider the following example of a formula.

```powerfx
Right(Entity.Name, 1) = "t"
```

This formula consists of the following elements:

- `Right` – a built-in function that retrieves the rightmost _x_ characters in a string.

- `Entity` – a context that the formula is working against.

- `Name` – a string property of `Entity`.

- `1` – the number of characters to retrieve from the right end of the string.

- `= "t"` – the equality evaluator that checks if the retrieved character is equal to the letter “t”.

The formula checks if the rightmost character of `Entity.Name` is `t`. If it is, the formula returns `true`, meaning that the rule will be applied to a specific golden record. If the formula returns `false`, the rule will not be applied to a specific golden record.

### Vocabulary values are text

Vocabulary key values are stored as text. Convert them with `Value`, `DateValue` or `DateTimeValue` before comparing numbers or dates, and convert a number, date or Boolean back to text with `Text` before writing it with `SetVocabularyKeyValue`. A missing value is Power Fx blank - test it with `IsBlank` or supply a default with `Coalesce`.

Vocabulary functions resolve the key you give them through its vocabulary definition, including any destination mapping, so the key must be [registered](/model/vocabularies/vocabulary-keys).

## Custom functions

Custom CluedIn functions are designed to help you with querying and setting data for a data part or a golden record.

| Function | What it does | Available in |
|---|---|---|
| `AddTag(record, tag)` | Adds a tag to the record's tag collection, unless an identical tag is already there. Analogous to the Add Tag rule action. Returns the updated record. | Data part and golden record rules |
| `GetVocabularyKeyValue(record, key)` | Returns the value of a vocabulary key as text, or blank if the record has no value for it. | All rules |
| `VocabularyKeyExists(record, key)` | Returns `true` if the record has a row for the vocabulary key, even an empty one. | All rules |
| `SetVocabularyKeyValue(record, key, text)` | Sets or adds a vocabulary key value. The value is text. Returns the updated record. | Data part and golden record rules |
| `SetEntityProperty(record, property, value)` | Sets a single-valued metadata property, such as `DisplayName`, `Description` or `Encoding`. Returns a new record. Table properties such as `Aliases` and `Tags` cannot be set this way, and some properties are read-only. | Data part and golden record rules |
| `FuzzyMatch(text1, text2)` | Returns a similarity score from 0 to 1. | All rules |
| `LoadEntityByEntityCode(code)` | Loads a golden record by its full entity code. Returns an error if no record has that code. | All rules |
| `LoadIncomingRelationships(record)` | Returns a table of the record's incoming relationships, one row per relationship with `EdgeType` and `EntityCode` (the code of the record at the other end). | Golden record rules |
| `LoadOutgoingRelationships(record)` | Returns a table of the record's outgoing relationships, with the same two fields. | Golden record rules |
| `GetVersionBranches(record)` | Returns the golden record's version history: a table of branches, each with a `Name` and its versions in `Parts`. | Golden record and survivorship rules |

The relationship and history functions return codes and version rows, not ready-to-use records. See [Compare a golden record with its history](#compare-a-golden-record-with-its-history) and [Traverse relationships between records](#traverse-relationships-between-records) for how to read values through them.

## Power Fx formula examples

This section contains some examples of Power Fx formulas in rules.

1. Set a value using an IF condition.

    ```powerfx
    SetVocabularyKeyValue(Entity, "user.price",
        Text(With({price: Value(GetVocabularyKeyValue(Entity, "user.price")) / 5 * 7 + 14},
            If(price > 50, 355, price))))
    ```

    `With` calculates the new price once, and `Text` turns the number back into the text the setter expects.

1. Set contract status to “Expiring Soon” if the contract ends within 5 days; otherwise, set it to “Active”.

    ```powerfx
    SetVocabularyKeyValue(Entity, "finance.contractStatus",
        If(DateDiff(Today(), DateValue(GetVocabularyKeyValue(Entity, "finance.contractEndDate"))) < 5,
            "Expiring Soon", "Active"))
    ```

1. Set salary grade to “Above Target” if the salary is higher than the target salary; otherwise, set it to “Below Target”.

    ```powerfx
    SetVocabularyKeyValue(Entity, "finance.salaryGrade", If(Value(GetVocabularyKeyValue(Entity, "finance.salary")) > Value(GetVocabularyKeyValue(Entity, "finance.targetSalary")), "Above Target", "Below Target"))
    ```

1. Set a vocabulary key value to a date using type conversion and formatting it to ISO format.

    ```powerfx
    SetVocabularyKeyValue(Entity, "user.startDate", Text(DateValue(GetVocabularyKeyValue(Entity, "user.startDate")), "yyyy-MM-ddTHH:mm:ssZ"))
    ```

1. Set full name to the combination of first name and last name, separated by a space.

    ```powerfx
    SetVocabularyKeyValue(Entity, "employee.fullName", GetVocabularyKeyValue(Entity, "employee.firstName") & " " & GetVocabularyKeyValue(Entity, "employee.lastName"))
    ```

1. Add a tag.

    ```powerfx
    AddTag(Entity, "ThisIsATag")
    ```

1. Check if the number of rows on a table/collection equals a value.

    ```powerfx
    CountRows(Entity.OutgoingEdges) = 1
    ```

1. Set a golden record property to a value.

    ```powerfx
    SetEntityProperty(Entity, "Encoding", "utf-8")
    ```

    Property names are case-sensitive and must match the runtime field name exactly.

1. Get a golden record by its [entity code](/model/identifiers). If found, returns a golden record; otherwise, returns an error.

    ```powerfx
    LoadEntityByEntityCode("/Person#CRM:5452407DH")
    ```

    The code must be complete: business domain, origin and value. The value on its own, such as `"5452407DH"`, is not an entity code and fails.

1. Check if the lookup vocabulary key is invalid due to lookup code not found in reference data.

    ```powerfx
    ("[Invalid (Missing)]" in GetVocabularyKeyValue(Entity,"product.producttype-EntityCode"))
    ```

1. Getting the latest currency exchange rate from another record to product record so that a live price in common currency can be calculated.

    ```powerfx
    SetVocabularyKeyValue(Entity,"Product.ExchangeRate",
     GetVocabularyKeyValue(
           LoadEntityByEntityCode("/ExchangeRate#CurrencyCode:" &
                  GetVocabularyKeyValue(Entity,"Product.localCurrencyCode"))
                 ,"currency.exchangeRate"))
    ```

### Combine several changes

A formula action writes back only its **final** result, so it must end with the record to apply. To make several changes, pass the record returned by one function into the next:

```powerfx
AddTag(
    SetVocabularyKeyValue(Entity, "customer.reviewStatus", "Complete"),
    "Reviewed")
```

When an action uses `If`, return a record from every branch. `Entity` leaves the record unchanged:

```powerfx
If(GetVocabularyKeyValue(Entity, "customer.status") = "Active",
    AddTag(Entity, "Active customer"),
    Entity)
```

Do not end a formula with `; Entity` after a setter. `SetEntityProperty` in particular returns a new record, and ending with the original `Entity` discards the change.

### Compare a golden record with its history

Use `GetVersionBranches(Entity)` to inspect the versions behind the current golden record, including values that were not selected as the surviving value. The examples below assume that the rule is running against a golden record.

`GetVersionBranches` returns a table of **branches**, not data parts. Each branch has two fields:

- `Name` – the branch name.
- `Parts` – the versions in that branch, newest first. Each version has `Date`, `ChangeType`, `IsHead` and `InputSource`, plus the data part itself in two forms: `EntityData` as it arrived, and `ProcessedEntityData` after processing.

Vocabulary values live on `EntityData` or `ProcessedEntityData`, so a formula reaches through `Parts` to read them:

```powerfx
GetVocabularyKeyValue(
    First(First(GetVersionBranches(Entity)).Parts).EntityData,
    "company.revenue"
)
```

This reads the original `company.revenue` value from the newest version in the first branch.

Before comparing, decide which versions you mean. These are different comparisons and can give different answers:

| Comparison | Versions considered | Inside each branch, use |
|---|---|---|
| Latest per branch | The newest version in every branch | `First(Parts)` |
| Branch heads | Versions marked as the head of their branch | `Filter(Parts, IsHead)` |
| All versions | Every historical version in every branch | `Parts` |

1. Check whether the current golden record value is greater than the latest value in every branch.

    ```powerfx
    Value(GetVocabularyKeyValue(Entity, "company.revenue")) >
    Max(GetVersionBranches(Entity),
        Value(GetVocabularyKeyValue(First(Parts).EntityData, "company.revenue")))
    ```

    This returns `true` when the golden record's `company.revenue` is higher than the newest `company.revenue` in each branch.

1. Check whether any historical version contains a value greater than the value currently selected on the golden record.

    ```powerfx
    With({current: Value(GetVocabularyKeyValue(Entity, "company.revenue"))},
        CountRows(
            Filter(GetVersionBranches(Entity),
                CountRows(Filter(Parts,
                    Value(GetVocabularyKeyValue(EntityData, "company.revenue")) > current)) > 0)
        ) > 0
    )
    ```

    This considers every version in every branch. To consider only the latest version of each branch, test `First(Parts)` instead of filtering `Parts`. Either way, it can identify cases where survivorship selected a lower value even though a higher value exists in the history.

1. Set a review flag when any branch head contains a value greater than the current golden record value.

    ```powerfx
    With({current: Value(GetVocabularyKeyValue(Entity, "company.revenue"))},
        SetVocabularyKeyValue(Entity, "company.requiresRevenueReview",
            If(CountRows(
                Filter(GetVersionBranches(Entity),
                    CountRows(Filter(Parts, IsHead &&
                        Value(GetVocabularyKeyValue(EntityData, "company.revenue")) > current)) > 0)
            ) > 0, "true", "false"))
    )
    ```

    The setter stores text, so the result is written as `"true"` or `"false"`.

1. Store the highest value across all versions.

    ```powerfx
    SetVocabularyKeyValue(Entity, "company.maximumSourceRevenue",
        Text(Max(GetVersionBranches(Entity),
            Max(Parts, Value(GetVocabularyKeyValue(EntityData, "company.revenue"))))))
    ```

    This stores the highest historical value separately, allowing the surviving value and the maximum source value to be inspected side by side.

Inside a nested `Filter` or `Max` over `Parts`, field names such as `EntityData` and `IsHead` refer to the version row. Use `ProcessedEntityData` instead of `EntityData` to compare processed values. `Max` ignores blank values, and `Value` fails on text that is not a number. An empty table can also mean the history is not available for the record, not only that it has none.

### Traverse relationships between records

Use `LoadIncomingRelationships(Entity)` and `LoadOutgoingRelationships(Entity)` to navigate the relationships between records in CluedIn. Both functions are available in golden record rules.

- `LoadIncomingRelationships(Entity)` returns the relationships that point **to** the current record.
- `LoadOutgoingRelationships(Entity)` returns the relationships that point **from** the current record.

Each row has two text fields:

- `EdgeType` – the type of the relationship.
- `EntityCode` – the entity code of the record at the other end: the source of an incoming relationship, or the target of an outgoing one.

The rows are **not** the related records. To read a value on a related record, load it first with `LoadEntityByEntityCode(EntityCode)`. Each load is a separate read from the data store, so a formula that loads every related record does work for each relationship of each record the rule processes. Keep traversal to what the rule needs.

1. Check whether the current entity has any outgoing relationships.

    ```powerfx
    CountRows(LoadOutgoingRelationships(Entity)) > 0
    ```

1. Check whether the current entity has any incoming relationships.

    ```powerfx
    CountRows(LoadIncomingRelationships(Entity)) > 0
    ```

1. Check whether the current entity has a relationship of a particular type.

    ```powerfx
    CountRows(Filter(LoadOutgoingRelationships(Entity), EdgeType = "/WorksFor")) > 0
    ```

    The value must match the edge type as it is stored in your data. `/WorksFor` is an example.

1. Read a value from the first entity connected through an outgoing relationship.

    ```powerfx
    GetVocabularyKeyValue(
        LoadEntityByEntityCode(
            First(LoadOutgoingRelationships(Entity)).EntityCode
        ),
        "company.name"
    )
    ```

    This can be useful when the current record is related to a parent, owner, supplier, account, or another business entity and you need to inspect a value on that related record. It assumes the record has at least one outgoing relationship; check with `CountRows` first if it may not.

1. Check whether any outgoing related record has a specific vocabulary key value.

    ```powerfx
    CountRows(
        Filter(
            LoadOutgoingRelationships(Entity),
            GetVocabularyKeyValue(LoadEntityByEntityCode(EntityCode), "company.status") = "Active"
        )
    ) > 0
    ```

    This expression returns `true` when at least one related entity has `company.status` set to `Active`.

1. Compare a value on the current record with values on its outgoing related records.

    ```powerfx
    Value(GetVocabularyKeyValue(Entity, "company.revenue")) >
    Max(
        LoadOutgoingRelationships(Entity),
        Value(GetVocabularyKeyValue(LoadEntityByEntityCode(EntityCode), "company.revenue"))
    )
    ```

    This returns `true` when the current entity's revenue is greater than the revenue of every entity connected through an outgoing relationship.

1. Check a value on an incoming related record.

    ```powerfx
    CountRows(
        Filter(
            LoadIncomingRelationships(Entity),
            GetVocabularyKeyValue(LoadEntityByEntityCode(EntityCode), "customer.riskRating") = "High"
        )
    ) > 0
    ```

    This can be used when records that point to the current entity contain information that should influence a rule on the current record.

1. Traverse two relationship hops.

    ```powerfx
    LoadOutgoingRelationships(
        LoadEntityByEntityCode(
            First(LoadOutgoingRelationships(Entity)).EntityCode
        )
    )
    ```

    This loads the current record's outgoing relationships, loads the record at the end of the first one, and then loads that record's outgoing relationships. The result is again a table of `EdgeType` and `EntityCode`.

1. Check whether a record two hops away contains a specific value.

    ```powerfx
    CountRows(
        Filter(
            LoadOutgoingRelationships(
                LoadEntityByEntityCode(First(LoadOutgoingRelationships(Entity)).EntityCode)
            ),
            GetVocabularyKeyValue(LoadEntityByEntityCode(EntityCode), "location.country") = "Australia"
        )
    ) > 0
    ```

    Multi-hop traversal can be useful when a business rule depends on indirectly related records. For example, you might traverse from a contact to an account, and then from the account to its registered locations.

1. Traverse an outgoing relationship followed by an incoming relationship.

    ```powerfx
    LoadIncomingRelationships(
        LoadEntityByEntityCode(
            First(LoadOutgoingRelationships(Entity)).EntityCode
        )
    )
    ```

    Combining incoming and outgoing traversal allows rules to navigate the graph in either direction rather than being limited to the relationships directly exposed on the current record.

`LoadEntityByEntityCode` returns an error when a code does not resolve to a record. To treat that as a non-match instead, wrap the condition in `IfError(..., false)`. Relationship loading is also limited by a timeout. Both are described in [Power Fx advanced reference](/govern/rules/power-fx-advanced-reference#loadincomingrelationships).
