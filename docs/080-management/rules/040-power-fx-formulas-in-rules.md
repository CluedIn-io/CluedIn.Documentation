---
layout: cluedin
nav_order: 4
parent: Rules
grand_parent: Management
permalink: /management/rules/power-fx-formulas
title: Power Fx formulas
last_modified: 2026-09-23
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article, you will learn about Power Fx formulas that you can use in the Rule Builder to set up filters, conditions, and actions in the Rule Builder.

<div class="videoFrame">
<iframe src="https://player.vimeo.com/video/1061960696?h=3ba16f6d8a&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write" title="Power FX formulas in CluedIn"></iframe>
</div>

Power Fx is a general-purpose, low-code, strong-typed, and functional programming language developed by Microsoft. Power Fx enables you to build and customize applications, workflows, and other solutions by writing simple, declarative expressions rather than traditional code. You can work with Power Fx using _Excel-like formulas_, which makes it intuitive both for technical and business users. For more information, see [Microsoft Power Fx overview](https://learn.microsoft.com/en-us/power-platform/power-fx/overview).

In CluedIn, you can use Power Fx formulas in the Rule Builder for querying, equality testing, decision making, type conversion, and string manipulation based on the supported properties of a data part or a golden record.

## Power Fx formulas in rules

You can use Power Fx formulas in the following types of rules:

- Data part rules – formulas are available in filters and actions (conditions and formula action).

- Survivorship rules – formulas are available in filters and actions (conditions). The formula action is not available in survivorship rules.

- Golden record rules – formulas are available in filters and actions (conditions and formula action).

In CluedIn, a Power Fx formula requires a _context_ to work with. It is called an `Entity`, and it represents a data part or a golden record. Essentially, it is a global variable that holds a sandboxed version of a data part or a golden record in CluedIn.

![power-fx-formula-example.png]({{ "/assets/images/management/rules/power-fx-formula-example.png" | relative_url }})

Consider the following example of a formula.

```
Right(Entity.Name, 1) = "t"
```

This formula consists of the following elements:

- `Right` – a built-in function that retrieves the rightmost _x_ characters in a string.

- `Entity` – a context that the formula is working against.

- `Name` – a string property of `Entity`.

- `1` – the number of characters to retrieve from the right end of the string.

- `= "t"` – the equality evaluator that checks if the retrieved character is equal to the letter “t”.

The formula checks if the rightmost character of `Entity.Name` is `t`. If it is, the formula returns `true`, meaning that the rule will be applied to a specific golden record. If the formula returns `false`, the rule will not be applied to a specific golden record.

**Custom functions**

Custom CluedIn functions are designed to help you with querying and setting data for a data part or a golden record. Custom functions include the following:

- `AddTag` – adds a tag to the golden record's tag collection. This function is analogous to the Add Tag rule action.

- `GetVocabularyKeyValue` – gets a value from the golden record's properties if such value exists; otherwise, it returns `Empty` (null).

- `GetVersionBranches` – returns the data parts associated with a golden record. Use this function to inspect source values that contributed to the golden record or compare the current golden record value with values that still exist on its underlying data parts.

- `LoadIncomingRelationships` – returns the entities connected to the supplied entity through incoming relationships. Use this function to traverse from the current record to records that point to it.

- `LoadOutgoingRelationships` – returns the entities connected to the supplied entity through outgoing relationships. Use this function to traverse from the current record to records that it points to.

- `SetEntityProperty` – sets a golden record metadata property (for example, `Created Date`, `Aliases`, `Description`).

- `SetVocabularyKeyValue` – sets or adds a vocabulary key to the golden record's properties.

## Power Fx formula examples

This section contains some examples of Power Fx formulas in rules.

1. Set a value using an IF condition.

    ```
    SetVocabularyKeyValue(Entity, "user.price", If(((GetVocabularyKeyValue(Entity, "user.price") / 5) * 7) + 14 > 50, 355, ((GetVocabularyKeyValue(Entity, "user.price") / 5) * 7) + 14))
    ```

1. Set contract status to “Expiring Soon” if the contract ends within 5 days; otherwise, set it to “Active”.

     ```
    SetVocabularyKeyValue(Entity, "finance.contractStatus", If(DateDiff(Today(), GetVocabularyKeyValue(Entity, "finance.contractEndDate")) < 5, "Expiring Soon", "Active"))
    ```

1. Set salary grade to “Above Target” if the salary is higher than the target salary; otherwise, set it to “Below Target”.

    ```
    SetVocabularyKeyValue(Entity, "finance.salaryGrade", If(Value(GetVocabularyKeyValue(Entity, "finance.salary")) > Value(GetVocabularyKeyValue(Entity, "finance.targetSalary")), "Above Target", "Below Target"))
    ```

1. Set a vocabulary key value to a date using type conversion and formatting it to ISO format.

    ```
    SetVocabularyKeyValue(Entity, "user.startDate", Text(DateValue(GetVocabularyKeyValue(Entity, "user.startDate")), "yyyy-MM-ddTHH:mm:ssZ"))
    ```

1. Set full name to the combination of first name and last name, separated by a space.

    ```
    SetVocabularyKeyValue(Entity, "employee.fullName", GetVocabularyKeyValue(Entity, "employee.firstName") & " " & GetVocabularyKeyValue(Entity, "employee.lastName"))
    ```

1. Add a tag.

    ```
    AddTag(Entity, "ThisIsATag")
    ```

1. Check if the number of rows on a table/collection equals a value.

    ```
    CountRows(Entity.OutgoingEdges) = 1
    ```

1. Set a golden record property to a value.

    ```
    SetEntityProperty(Entity, "Encoding", "utf-8")
    ```

1. Get a golden record by [identifier](/key-terms-and-features/entity-codes) (previously known as entity code). If found, returns a golden record; otherwise, returns an error.

    ```
    LoadEntityByEntityCode("5452407DH")
    ```

1. Check if the lookup vocabulary key is invalid due to lookup code not found in reference data.

    ```
    ("[Invalid (Missing)]" in GetVocabularyKeyValue(Entity,"product.producttype-EntityCode"))
    ```

1. Getting the latest currency exchange rate from another record to product record so that a live price in common currency can be calculated.

    ```
    SetVocabularyKeyValue(Entity,"Product.ExchangeRate", 
     GetVocabularyKeyValue( 
           LoadEntityByEntityCode("/ExchangeRate#CurrencyCode:" &  
                  GetVocabularyKeyValue(Entity,"Product.localCurrencyCode")) 
                 ,"currency.exchangeRate"))
    ```


### Compare a golden record with its data parts

Use `GetVersionBranches(Entity)` to return the data parts associated with the current golden record. This is useful when a rule needs to consider values that exist on the underlying data parts, including values that were not selected as the surviving value on the golden record.

The examples below assume that the rule is running against a golden record.

1. Check whether the current golden record value is greater than every value for the same vocabulary key on its data parts.

    ```powerfx
    Value(GetVocabularyKeyValue(Entity, "company.revenue")) > Max(GetVersionBranches(Entity), Value(GetVocabularyKeyValue(ThisRecord, "company.revenue")))
    ```

    This expression returns `true` when the golden record's `company.revenue` value is greater than the highest `company.revenue` value found on any associated data part.

1. Check whether any data part contains a value greater than the value currently selected on the golden record.

    ```powerfx
    CountRows(
        Filter(
            GetVersionBranches(Entity),
            Value(GetVocabularyKeyValue(ThisRecord, "company.revenue")) > Value(GetVocabularyKeyValue(Entity, "company.revenue"))
        )
    ) > 0
    ```

    This can be useful for identifying cases where survivorship has selected a lower value even though a higher value exists on one of the source data parts.

1. Set a review flag when any data part contains a value greater than the current golden record value.

    ```powerfx
    SetVocabularyKeyValue(
        Entity,
        "company.requiresRevenueReview",
        CountRows(
            Filter(
                GetVersionBranches(Entity),
                Value(GetVocabularyKeyValue(ThisRecord, "company.revenue")) > Value(GetVocabularyKeyValue(Entity, "company.revenue"))
            )
        ) > 0
    )
    ```

1. Store the highest value available across all associated data parts.

    ```powerfx
    SetVocabularyKeyValue(
        Entity,
        "company.maximumSourceRevenue",
        Max(
            GetVersionBranches(Entity),
            Value(GetVocabularyKeyValue(ThisRecord, "company.revenue"))
        )
    )
    ```

    This stores the highest source value separately, allowing the surviving value and the maximum source value to be inspected side by side.


### Traverse relationships between records

Use `LoadIncomingRelationships(Entity)` and `LoadOutgoingRelationships(Entity)` to navigate the relationships between records in CluedIn.

- `LoadIncomingRelationships(Entity)` returns the related entities that have an incoming relationship to the supplied entity.
- `LoadOutgoingRelationships(Entity)` returns the related entities that the supplied entity has an outgoing relationship to.

The returned entities can be used with standard Power Fx functions such as `First`, `Filter`, `CountRows`, `Max`, and `ForAll`. You can also pass a returned entity into another relationship function to traverse multiple hops through the graph.

1. Check whether the current entity has any outgoing relationships.

    ```powerfx
    CountRows(LoadOutgoingRelationships(Entity)) > 0
    ```

1. Check whether the current entity has any incoming relationships.

    ```powerfx
    CountRows(LoadIncomingRelationships(Entity)) > 0
    ```

1. Read a value from the first entity connected through an outgoing relationship.

    ```powerfx
    GetVocabularyKeyValue(
        First(LoadOutgoingRelationships(Entity)),
        "company.name"
    )
    ```

    This can be useful when the current record is related to a parent, owner, supplier, account, or another business entity and you need to inspect a value on that related record.

1. Check whether any outgoing related record has a specific vocabulary key value.

    ```powerfx
    CountRows(
        Filter(
            LoadOutgoingRelationships(Entity),
            GetVocabularyKeyValue(ThisRecord, "company.status") = "Active"
        )
    ) > 0
    ```

    This expression returns `true` when at least one related entity has `company.status` set to `Active`.

1. Compare a value on the current record with values on its outgoing related records.

    ```powerfx
    Value(GetVocabularyKeyValue(Entity, "company.revenue")) >
    Max(
        LoadOutgoingRelationships(Entity),
        Value(GetVocabularyKeyValue(ThisRecord, "company.revenue"))
    )
    ```

    This returns `true` when the current entity's revenue is greater than the revenue of every entity connected through an outgoing relationship.

1. Check a value on an incoming related record.

    ```powerfx
    CountRows(
        Filter(
            LoadIncomingRelationships(Entity),
            GetVocabularyKeyValue(ThisRecord, "customer.riskRating") = "High"
        )
    ) > 0
    ```

    This can be used when records that point to the current entity contain information that should influence a rule on the current record.

1. Traverse two relationship hops.

    ```powerfx
    LoadOutgoingRelationships(
        First(
            LoadOutgoingRelationships(Entity)
        )
    )
    ```

    This first loads the entities connected to the current record through outgoing relationships, selects the first related entity, and then loads that entity's outgoing relationships.

1. Check whether a record two hops away contains a specific value.

    ```powerfx
    CountRows(
        Filter(
            LoadOutgoingRelationships(
                First(LoadOutgoingRelationships(Entity))
            ),
            GetVocabularyKeyValue(ThisRecord, "location.country") = "Australia"
        )
    ) > 0
    ```

    Multi-hop traversal can be useful when a business rule depends on indirectly related records. For example, you might traverse from a contact to an account, and then from the account to its registered locations.

1. Traverse an outgoing relationship followed by an incoming relationship.

    ```powerfx
    LoadIncomingRelationships(
        First(
            LoadOutgoingRelationships(Entity)
        )
    )
    ```

    Combining incoming and outgoing traversal allows rules to navigate the graph in either direction rather than being limited to the relationships directly exposed on the current record.
