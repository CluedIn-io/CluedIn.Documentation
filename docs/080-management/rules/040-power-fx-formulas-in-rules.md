---
layout: cluedin
nav_order: 4
parent: Rules
grand_parent: Management
permalink: /management/rules/power-fx-formulas
title: Power Fx formulas
last_modified: 2025-07-17
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