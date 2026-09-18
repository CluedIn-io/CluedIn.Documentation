---
layout: cluedin
nav_order: 7
parent: Deduplication
grand_parent: Management
permalink: /management/deduplication/match-one-of-multiple-fields
title: Match one of multiple fields
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article, you will learn how to identify duplicates when a record contains several values of the same kind and any one of those values can match another record. This approach works with all matching functions, including equality and fuzzy matching.

## Example

Suppose customer records contain a company name and up to three email addresses:

| Record | Company name | Email 1 | Email 2 | Email 3 |
|--|--|--|--|--|
| A | Contoso | alice@example.com | accounts@contoso.com | |
| B | Contoso | info@contoso.com | alice@example.com | |

These records should be identified as duplicates because:

- their company names are the same; and
- one of the email addresses in record A is the same as one of the email addresses in record B.

The shared email address does not occupy the same field in both records. It is stored in **Email 1** in record A and **Email 2** in record B.

A matching criterion compares the selected vocabulary key on both records. For example, a criterion for `customer.email1` compares `customer.email1` on record A with `customer.email1` on record B. It does not compare `customer.email1` with `customer.email2`.

To compare values regardless of their original field, combine them into one helper vocabulary key and split that value during duplicate detection.

## Create a combined vocabulary key

Before generating matches, create a helper vocabulary key that contains all relevant values from each record. For example:

```text
customer.emails
```

During ingestion or processing, populate this vocabulary key by joining the available email addresses with a delimiter. A pipe character (`|`) can be used as the delimiter:

```text
alice@example.com|accounts@contoso.com
```

Exclude empty values when constructing the combined value.

The two example records would contain the following values:

| Record | `customer.companyName` | `customer.emails` |
|--|--|--|
| A | Contoso | `alice@example.com|accounts@contoso.com` |
| B | Contoso | `info@contoso.com|alice@example.com` |

{:.note}
Choose a delimiter that cannot occur within the individual values.

## Configure the matching rule

Create one matching rule with two matching criteria joined by **AND**.

Configure the company name criterion as follows:

| Setting | Value |
|--|--|
| Vocabulary key | `customer.companyName` |
| Matching function | **Equals** |

Configure the email criterion as follows:

| Setting | Value |
|--|--|
| Vocabulary key | `customer.emails` |
| Matching function | **Equals** |
| Normalization rule | **Split text into tokens, using regex pattern** |
| Separator pattern | `\|` |

The separator pattern `\|` represents a literal pipe character in a regular expression.

If you use the regular **Split text** normalization rule instead of the regex version, enter a literal pipe character (`|`) as the separator.

The completed rule represents the following logic:

```text
customer.companyName equals
AND
any value in customer.emails equals any value in customer.emails
```

For more information about configuring matching rules, see [Create a deduplication project](/management/deduplication/create-a-deduplication-project#add-a-matching-rule).

## How the values are compared

For record A, the split normalization produces:

```text
alice@example.com
accounts@contoso.com
```

For record B, it produces:

```text
info@contoso.com
alice@example.com
```

The email criterion is satisfied because both records contain `alice@example.com`. The original position of the email address does not matter.

The company name criterion must also be satisfied because matching criteria within a rule are joined by **AND**. If both criteria match, CluedIn includes the records in the same group of potential duplicates.

## Use other matching functions

This approach is not limited to the **Equals** matching function. Splitting the combined value produces multiple candidates, and the matching function selected for the criterion is applied to those candidates.

You can use the same configuration with any matching function supported by the criterion, including:

- **Email**
- **Contains**
- **Starts with**
- **Ends with**
- **First token equals**
- **Fuzzy match - Sift4**
- **Fuzzy match - phonetic, DoubleMetaphone**

For example, records may contain several alternative organization names:

```text
Contoso Limited|Contoso Ltd|Contoso
```

You can split the value and use **Fuzzy match - Sift4** so that any alternative name from one record can be compared with any alternative name from another record.

Choose a matching function appropriate for the data. For email addresses and identifiers, use **Equals**, **Email**, or another strict function whenever possible. Fuzzy matching is more suitable for names and other descriptive text because it can produce false positives when used with structured identifiers.

For more information about the available functions and normalization rules, see [Deduplication reference](/management/deduplication/deduplication-reference#matching-functions).

## Apply the pattern to other data

The same pattern can be used whenever equivalent values are stored in multiple fields, including:

- phone numbers;
- external identifiers;
- product codes;
- website domains;
- previous or alternative names; and
- addresses from multiple source systems.

Create one combined vocabulary key for the related values, split it into tokens with a normalization rule, and select the matching function that is appropriate for the data.
