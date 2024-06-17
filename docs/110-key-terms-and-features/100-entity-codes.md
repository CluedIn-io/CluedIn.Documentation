---
layout: cluedin
title: Entity codes
parent: Key terms and features
nav_order: 10
has_children: false
permalink: /key-terms-and-features/entity-codes
tags: ["development","entities","entity-codes"]
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

A code is a way to instruct CluedIn to know what a completely unique reference to a clue is. If two clues have identical codes, they will be merged during processing.

**Example**

Let’s explore the concept of codes in CluedIn through an example. We have a golden record—John Smith—that originates from the HR system. One of the codes for this golden record is created using the ID. Now, a new record from the CRM system appears in CluedIn, and one of its codes matches the code of the golden record from the HR system. As a result, the new CRM record is merged with the existing HR record, integrating any new properties from the CRM record into the existing golden record.

![codes-merge-1.gif](../../assets/images/key-terms-and-features/codes-merge-1.gif)

To find all the codes that uniquely represent a golden record in the system, go to the golden record page, and select **View Codes**.

![codes-1.gif](../../assets/images/key-terms-and-features/codes-1.gif)

The codes are divided into two sections:

- [Origin code](#entity-origin-code) – also referred to as the entity origin code. This is the primary unique identifier of a golden record in CluedIn.

- [Codes](#codes) – also referred to as entity codes. This section contains all codes associated with a golden record.

For more information, see the **Codes** section in our [Review mapping](/integration/review-mapping#codes) article.

## Entity origin code

An entity origin code is a primary unique identifier of a record in CluedIn. The required details for producing the entity origin code are established when the mapping for a data set is created. To find these details, go to the **Map** tab of the data set and select **Edit mapping**. On the **Map entity** tab, you'll find the **Entity Origin** section, which contains the required details for producing the entity origin code.

![codes-2.png](../../assets/images/key-terms-and-features/codes-2.png)

The entity origin code is made up from the entity type (1), [origin](/key-terms-and-features/origin) (2), and the value from the column that was selected for producing the entity origin code (3). This combination allows achieving absolute uniqueness across any data source that you interact with. 

![codes-3.png](../../assets/images/key-terms-and-features/codes-3.png)

## Entity codes

An entity code is an additional identifier that uniquely represents a record in CluedIn. The required details for producing the entity codes are established when the mapping for a data set is created. To find these details, go to the **Map** tab of the data set and select **Edit mapping**. On the **Map entity** tab, you'll find the **Codes** section, which contains the required details for producing the entity codes.

![codes-4.png](../../assets/images/key-terms-and-features/codes-4.png)

If a data set contains additional columns that can serve as unique identifiers besides the ones used for producing the entity origin code, then these columns can also be used to produce entity codes. For example, if the entity origin code is produced using the ID, then the entity code could be produced using the email. The entity codes are made up from the entity type, [origin](/key-terms-and-features/origin), and the value from the column that was selected for producing the entity codes.

In the **Entity Codes** section, you can instruct CluedIn to produce additional codes:

- **Provider name codes** – codes that are built form the entity type, provider name (for example, File Data Source), and the value from the column that was selected for producing the entity origin code.

- **Strict edge codes** – codes that are built from the entity type, data source group ID/data source ID/data set ID, and the value from the column that was selected for producing the entity origin code.

## FAQ

**How to make sure that the codes will blend across different data sources?**

Since a code will only merge with another code if they are identical, how can you merge records across different systems if the origin is different? One of the ways to achieve it is through the GUID.

If a record has an adentifier that is a GUID/UUID, you can set the origin as CluedIn because no matter the system, the identifier should be unique. However, this is not applicable if you are using deterministic GUIDS. If you're wondering whether you use deterministic GUIDs, conducting preliminary analysis on the data can help. Check if many GUIDs overlap in a certain sequence, such as the first chunk of the GUID being replicated many times. This is a strong indicator that you are using deterministic GUIDs. Random GUIDs are so unique that the chance of them being the same is close to impossible.

You could even determine that the entity type can be generic as well. You will have to craft these special entity codes in your clues (for example, something like `/Generic#CluedIn:<GUID>`). You will need to make sure your edges support the same mechanism. In doing this, you are instructing CluedIn that no matter the entity type, no matter the origin of the data, this record can be uniquely identified by just the GUID.

**What if a record doesn't have a unique reference to construct a code?** 

Often you will find that you need to merge or link records across systems that don't have IDs but rather require fuzzy merging to be able to link records. In this case, we often suggest creating a composite code constructed from a combination of column or property values that guarantee uniqueness. For example, if you have a Transaction record, you might find that a combination of the Transaction Date, Product, Location, and Store will guarantee uniqueness. It is best to calculate a "Hash" of these values combined, which means that we can calculate a code from this.

**What if an identifier is not ready for producing a code?**

Sometimes identifiers for codes are not ready to be made into a unique entity origin code. For example, your data might include default or fallback values when a real value is not present. Imagine you have an EmployeeId column, and when a value is missing, placeholders like "NONE", "", or "N/A" are used. These are not valid identifiers for the EmployeeId. However, the important aspect is that you cannot handle all permutations of these placeholders upfront. Therefore, you should create codes with the intention that these values are unique. You can fix and clean up such values later.