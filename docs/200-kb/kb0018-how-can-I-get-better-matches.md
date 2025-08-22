---
layout: cluedin
title: How can I get better matches of duplicate records in CluedIn
parent: Knowledge base
permalink: /kb/better-matches
tags: ["Deduplication", "Matching"]
nav_order: 18
---

# How to Get Better Matches in Deduplication Projects

Deduplication Projects in CluedIn help identify and merge duplicate records across your data sources. Good results depend not only on the rules you configure, but also on the **quality and consistency of the data being matched**. This article provides practical advice for improving match quality.

---

## Key Principles

### 1. Prioritize Deterministic Matching Rules
It’s tempting to design complex rules to cover every possible variation in your data. However, this often increases false positives and makes matching less predictable.  

- **Instead of chasing perfection**, create rules that are as deterministic and strict as possible (e.g., “Exact match on Tax ID” or “Exact match on Email Address”).  
- Use **high-confidence identifiers** first: IDs, email, phone numbers, domains.  
- Apply fuzzy matching sparingly, only where no strong identifier exists.  

---

### 2. Use CluedIn Clean to Improve Input Data
Matching accuracy is only as good as the **quality of your input data**. Use **CluedIn Clean** to standardize and normalize data before running matching:  

- Clean addresses into a structured, comparable format.  
- Convert phone numbers to **E.164** international format.  
- Normalize company names (remove “Ltd”, “Inc”, punctuation).  
- Standardize casing, diacritics, and whitespace.  

> By cleaning first, you make it easier for deterministic rules to succeed, rather than relying on fuzzy matching to compensate for poor data quality.

---

### 3. Apply Normalisers to Ignore Irrelevant Differences
Normalisers allow you to **exclude certain aspects of data from the matching process** so that records aren’t incorrectly treated as different:  

- **Case Normalisation**: Treat `CLUEdin`, `CluedIn`, and `cluedin` as identical.  
- **Whitespace Normalisation**: Ignore leading/trailing or multiple spaces.  
- **Punctuation Normalisation**: Strip characters like commas, periods, or dashes where not significant.  
- **Custom Normalisers**: Define rules to remove common “noise” (e.g., `Ltd`, `Inc`, `GmbH`).  

---

## Recommended Approach

1. **Start simple and strict**  
   - Build rules around unique, high-confidence identifiers.  
   - Ensure those identifiers are cleaned and normalised first.  

2. **Add cleaning steps in CluedIn Clean**  
   - Focus on the data elements used in matching.  
   - Validate that cleaned values align with your rules.  

3. **Use fuzzy matching only as a fallback**  
   - Apply it after deterministic rules to catch edge cases.  
   - Always review candidates in stewardship before merging.  

---

## Example

- **Before Cleaning**  
  - `Acme Inc.` vs. `ACME, Incorporated`  
  - Phone: `0044 7700 900123` vs. `+44 7700 900123`  

- **After CluedIn Clean & Normalisation**  
  - `Acme` vs. `Acme`  
  - Phone: `+447700900123` vs. `+447700900123`  

**Result**: Deterministic matching rules (Exact Name + Exact Phone) succeed with confidence, no need for fuzzy fallback.

---

## Summary

To get the best matches in Deduplication Projects:  
- **Keep rules deterministic** and simple.  
- **Clean data with CluedIn Clean** so it conforms to your matching rules.  
- **Use normalisers** to remove irrelevant differences like case, whitespace, and punctuation.  
- **Reserve fuzzy matching** for edge cases where no strong identifiers exist.  

This approach ensures higher accuracy, fewer false positives, and faster stewardship.



