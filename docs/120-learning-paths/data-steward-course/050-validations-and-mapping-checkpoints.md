---
layout: cluedin
title: Review source quality with validations and mapping checkpoints
parent: Data Steward course
grand_parent: Learning paths
nav_order: 50
permalink: /learning-paths/data-steward-course/validations-and-mapping-checkpoints
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

Stewards often meet data quality problems after those problems are already visible in golden records. Validations and mapping checkpoints help you catch them earlier, while the data is still close to the source and easier to reason about.

![validations-result.png]({{ "/assets/images/integration/additional-operations/validations-result.png" | relative_url }})

## What this module teaches

By the end of this module, you should be able to:

- explain what validations do
- understand the prerequisites for using validations
- review mapping details with a steward’s eye
- interpret validation results and decide what to do next
- distinguish between “fix the current values” and “change the ingestion design”

## Why validations matter to stewards

Validations do not exist just to color cells red. They help you answer operational questions such as:

- Is the source systematically malformed?
- Which fields are safe to trust?
- How many records are affected?
- Should the issue be corrected in-place before processing further?
- Should this become a repeated quality-control pattern?

A strong steward treats validations as an **early-warning system**.

## Validation prerequisites

Two prerequisites matter:

- the dataset must be **mapped** to standard fields
- the dataset should be in **edit mode**

Why this matters:

- without mapping, CluedIn does not know enough to suggest sensible validations
- without edit mode, you cannot add validations or correct source values directly in the dataset workflow

This is a good example of why stewards need baseline ingestion literacy.

## The three validation modes

### Auto-validation

This is the fastest starting point. CluedIn analyzes fields and suggests validation methods for some of them.

Use it when:

- you are exploring a new dataset
- you want a quick signal of likely field issues
- you want to see where CluedIn itself spots obvious risk

Strength: fast triage  
Weakness: not enough for all business logic

### Manual validation

This lets you choose a validation method field by field.

Use it when:

- you know which field needs checking
- you need a different rule than auto-validation suggested
- you want more deliberate control over the check

Strength: controlled and explicit  
Weakness: requires more stewardship judgment

### Advanced validation

This uses JavaScript logic for more complex conditions.

Use it when:

- field-level checks are not enough
- validity depends on combinations of values
- business logic matters more than simple formatting

Strength: expressive  
Weakness: should usually involve more technical ownership or careful review

## What validation methods are trying to detect

Different methods answer different questions:

- is this value present?
- is this value formatted correctly?
- is this value inside an acceptable range?
- does this value match an approved pattern?
- does this record violate a business rule when multiple fields are considered together?

A steward does not need every method memorized. What matters is knowing which *question* you are trying to answer.

## How to read validation results

When validations run, you see counts of:

- total values
- valid values
- invalid values

A steward should not stop at the red count. Ask:

- Is the field business-critical?
- Is the invalid rate tiny, moderate, or severe?
- Is the issue concentrated in one source pattern?
- Can values be corrected safely now?
- Is this issue likely to recur on future loads?

Validation results tell you not only what is bad, but how urgent the problem is and whether a structural fix is needed.

## Finding invalid values

From the validation results, you can filter directly to invalid records. This is powerful because it turns a field-level quality signal into an actionable queue.

![validations-invalid-values.png]({{ "/assets/images/integration/additional-operations/validations-invalid-values.png" | relative_url }})

Once invalid values are isolated, the steward can decide whether to:

- fix them directly in the dataset
- handle them later in a clean project
- quarantine or hold the source if governance requires it
- escalate the issue to source owners or architects

## Mapping checkpoints a steward should always review

Validations are only half the story. The steward should also review mapping details because quality checks are only as meaningful as the mapped semantics.

### Checkpoint 1: are fields mapped to the right meaning?

If a phone field is mapped as something else, even perfect validation logic will not help the steward in the right way.

### Checkpoint 2: is the display behavior useful?

Ask whether the chosen entity name, description, created date, and modified date help a human steward understand records in search.

### Checkpoint 3: is the identifier safe?

A dangerous identifier can make validation look cleaner than the operational reality because wrongly merged records hide the true scale of source defects.

### Checkpoint 4: are relationships being built from reliable keys?

If relationship fields are unstable, the resulting graph can mislead downstream stewardship.

## When to fix in the dataset vs when to fix later

### Fix now in the dataset when

- the invalid values are obvious and limited
- the corrections are safe
- the issue is close to the source and still easy to reason about
- you want to prevent the bad values from spreading further

### Fix later in a clean project when

- the records are already in operational circulation
- you need broader review tools
- the issue affects a larger golden-record set
- the work is more naturally managed as a steward queue

### Escalate instead of fixing locally when

- the wrong field is mapped
- the identifier logic is unsafe
- the same issue will clearly repeat on every load
- the issue should be normalized upstream or turned into a durable rule

## Red flags in validation work

Escalate quickly if you see patterns like:

- the “best” validation result still hides obviously bad business logic
- the same invalid pattern appears in large volume after each intake
- fields that should be required are routinely empty
- mapped fields with validation issues also drive identifiers, relations, or key downstream exports

## Practice exercise

Pick one dataset and answer:

- Which field would you validate first, and why?
- Would auto-validation be enough?
- If the field shows invalid values, what percentage would cause you to escalate immediately?
- Would you fix current values here, in Clean, or upstream?
- What evidence would you give the architect?

## You are ready for the next module when

You can explain:

- the difference between auto, manual, and advanced validation
- why validations require mapping context
- how to turn a red validation result into a real operational action plan
- when a dataset issue should be fixed locally versus structurally

## What comes next

Now you are ready for one of the steward’s core remediation tools: clean projects. In the next module you will learn how to turn a recurring issue into a controlled and repeatable clean workflow.
