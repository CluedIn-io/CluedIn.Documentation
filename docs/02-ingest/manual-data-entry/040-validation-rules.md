---
layout: cluedin
title: Manual data entry validation rules
parent: Manual data entry
grand_parent: Ingest
nav_order: 40
permalink: /ingest/manual-data-entry/validation-rules
content_type: reference
last_modified: 2026-11-26
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

This article lists the validation rules you can add to a form field of a [manual data entry project](/ingest/manual-data-entry/configure-a-manual-data-entry-project#create-form-fields), and the language of the **Custom expression** rule.

A value is checked against its field's rules while you enter it (in both the Form and Tabular views), and again when the records are published. A record that breaks a rule can't be published until it is corrected. Each rule has a default message; you can replace it with your own.

## Field types and the format they imply

Some form field types imply a rule, so you don't need to add it:

| Form field type | Entered as | Implied rule |
|--|--|--|
| Text Field | One line of text | – |
| Long text | Several lines of text | – |
| Number | A number | Number |
| Date | A date, picked or typed as YYYY-MM-DD | Date |
| Email address | An email address | Email address |
| Web address (URL) | A link starting with `http://` or `https://` | URL |
| Phone number | A phone number | Phone number |
| Image (link) | A link to an image, shown as a preview | URL |
| Pick List, Toggle, Date and time, Time, Lookup | As before | – |

## Rules

Empty values are checked only by **Is Required** and by the rules under [When a value is needed](#when-a-value-is-needed) and [Custom](#custom). The other rules check a value only when there is one.

### When a value is needed

| Rule | Argument | The value… |
|--|--|--|
| Required if another field… | A field, and optionally a value | is required when the other field has that value (or, without a value, any value). |
| Required unless another field has a value | A field | is required when the other field is empty, for example an email address unless there is a phone number. |
| Must be empty if another field… | A field, and optionally a value | must be empty when the other field has that value (or any value). |
| Unique in the session | – | is not used by another record of the session, ignoring case and surrounding spaces. |

### Text

| Rule | Argument | The value… |
|--|--|--|
| Minimum length, Maximum length, Exact length | A number | has at least, at most or exactly that many characters. |
| Matches pattern | A regular expression | matches it. |
| Starts with, Ends with, Contains, Does not contain | Text | starts with, ends with, contains or doesn't contain it (case-sensitive). |
| One of, Not one of | A list, one value per line or separated by commas | is (or isn't) one of the values. |
| Letters only | – | contains letters, spaces, apostrophes and hyphens only. |
| Letters and digits only | – | contains letters and digits only. |
| Uppercase, Lowercase | – | is in uppercase or in lowercase. |
| No spaces | – | contains no spaces. |
| No leading, trailing or double spaces | – | doesn't start or end with a space and has no double spaces. |

### Numbers

| Rule | Argument | The value… |
|--|--|--|
| Number, Whole number | – | is a number, or a whole number. |
| Minimum value, Maximum value | A number | is a number at least or at most that. |
| Greater than zero, Zero or more | – | is a number above zero, or zero or above. |
| Maximum decimal places | A number | is a number with at most that many decimal places. |

### Dates

| Rule | Argument | The value… |
|--|--|--|
| Date | – | is a date, such as 2026-11-26. |
| On or after date, On or before date | A date | is a date on or after, or on or before, it. |
| In the past, In the future | – | is a date before today, or after today. |

### Formats

| Rule | Argument | The value… |
|--|--|--|
| Email address, URL, Phone number | – | is an email address, an `http(s)` link, or a phone number of 7 to 15 digits. |
| Postal code of a country | A country (AU, US, GB, CA, DE, FR, NL, NZ, DK, SE, IN and more) | is a postal code in that country's format. |
| Country code (ISO 3166) | – | is a two-letter country code, such as AU. |
| Currency code (ISO 4217) | – | is a three-letter currency code, such as EUR. |
| IBAN, Card number | – | is an IBAN with a valid checksum, or a card number that passes the Luhn check. |
| GUID / UUID, IP address, JSON | – | is a GUID, an IPv4 or IPv6 address, or valid JSON. |

### Compared with another field

| Rule | Argument | The value… |
|--|--|--|
| Same as field, Different from field | A field | is the same as, or different from, the other field's value. |
| Greater than field, Less than field | A field | is greater or less than the other field's value, comparing numbers as numbers and dates as dates (for example, an end date after a start date). |

### Custom

For anything else, add a **Custom expression** rule: a condition the value must meet. The value is valid when the expression is true. The expression is also checked when the value is empty, so you can use it for conditional requirements.

| In an expression | Means |
|--|--|
| `value` | The field's own value (empty text when it's empty). |
| `field("customer.country")` | Another field of the same record, by its vocabulary key. |
| `'text'`, `"text"`, `42`, `true`, `false`, `null` | Literals. |
| `!`, `&&`, `\|\|` | Not, and, or. |
| `==`, `!=`, `<`, `<=`, `>`, `>=` | Comparisons: as numbers when both sides are numbers, otherwise as text. Dates written as YYYY-MM-DD compare correctly as text. |
| `+`, `-`, `*`, `/`, `%` | Arithmetic; `+` joins text unless both sides are numbers. |
| `condition ? a : b` | `a` when the condition is true, otherwise `b`. |

Functions: `len`, `lower`, `upper`, `trim`, `isEmpty`, `isNumber`, `number`, `text`, `contains`, `startsWith`, `endsWith`, `matches` (a regular expression), `in(value, "a", "b", …)`, `coalesce`, `abs`, `round(n, digits)`, `min`, `max`, `today()`, `isDate`, `year`, and `daysBetween(from, to)`.

Examples:

- A four-digit postal code, but only for Australia: `field("customer.country") != "Australia" || matches(value, "^\\d{4}$")`
- An end date at most 90 days after the start date: `daysBetween(field("contract.start"), value) <= 90`
- A discount only for wholesale customers: `isEmpty(value) || field("customer.type") == "Wholesale"`

The editor checks an expression as you type it and tells you what is wrong. An expression can only read the record's values and call the functions above, so it's safe to run for everyone who enters records.
