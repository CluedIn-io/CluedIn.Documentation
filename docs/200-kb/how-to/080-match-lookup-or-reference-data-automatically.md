---
layout: cluedin
title: How to match reference data or lookup data automatically
parent: Knowledge base
permalink: /kb/how-to-match-reference-data
nav_order: 2
---

# How to Automatically Match Lookup or Reference Data to a Known List of Values

Many business processes rely on **lookup tables** or **reference data** (e.g., country codes, product categories, departments, payment terms). In practice, data sources often contain values that don’t exactly match your standard lists. CluedIn provides tools to automatically align these values to your **canonical reference set**.

---

## Why Match Reference Data?

- **Consistency**: Ensure all systems use the same codes and descriptions.  
- **Analytics**: Prevent fragmented reporting (e.g., `UK`, `U.K.`, `United Kingdom`).  
- **Interoperability**: Map local or legacy codes to global standards (e.g., currency codes, ISO country codes).  
- **Data Quality**: Reduce manual stewardship by automating corrections.  

---

## Approaches in CluedIn

### 1. Deterministic Matching
If the incoming values are clean and predictable:  
- Use **Data Part Rules** to map exact matches (`UK` → `GB`).  
- Apply **Normalisers** to ignore casing, whitespace, or punctuation (`us` = `US`).  

This works best when the variety of input formats is limited.

---

### 2. Fuzzy & AI-Powered Matching with **Find Closest Match**
For more complex or inconsistent input values, use the **Find Closest Match** Rule Action.  

- **What it does**:  
  - Compares the incoming value against your known list of canonical values.  
  - Uses **fuzzy string similarity** and **semantic AI** to suggest the **closest aligned match**.  
  - Automatically replaces or tags the value with the matched canonical reference.  

- **Example**:  
  - Input: `U.K.`, `Britain`, `Great Britan`  
  - Canonical List: `United Kingdom`, `Germany`, `France`  
  - **Find Closest Match Result**: → `United Kingdom`  

- **Advantages**:  
  - Handles typos, spelling variations, abbreviations, and synonyms.  
  - Reduces manual stewardship workload.  
  - Consistently maps new variations as they appear.  

---

## Step-by-Step: Using **Find Closest Match**

1. **Prepare your reference list**  
   - Define your canonical values in a Vocabulary or controlled lookup table.  

2. **Create or edit a Rule**  
   - Go to **Governance → Rules**.  
   - Add a new **Data Part Rule** or edit an existing one.  

3. **Add the Find Closest Match Action**  
   - Choose **Find Closest Match** as the action.  
   - Select the attribute (e.g., `Country`, `Currency`, `Category`).  
   - Point it to your canonical list of values.  

4. **Configure thresholds (optional)**  
   - Adjust similarity thresholds to control how strict/loose matches are.  
   - Lower thresholds = more automated matches (but higher false positives).  
   - Higher thresholds = more accuracy, but some unmatched values may require stewardship.  

5. **Test & Validate**  
   - Run the rule on sample data.  
   - Verify results and adjust thresholds if needed.  

6. **Operationalize**  
   - Apply the rule to incoming data streams.  
   - Review unmatched or low-confidence cases in Stewardship.  

---

## Best Practices

- **Start strict, then relax**: Begin with higher thresholds to build trust. Lower gradually if too many values remain unmatched.  
- **Combine with cleaning**: Standardize casing, whitespace, and punctuation before running **Find Closest Match**.  
- **Audit results**: Periodically review mappings to catch drift (new slang, abbreviations, or vendor codes).  
- **Log & tag**: Keep the original raw value stored for lineage and auditing.  

---

## Example Use Cases

- Mapping **country names** from free-text CRM fields to ISO 3166-1 codes.  
- Aligning **product categories** from multiple e-commerce sites to a master taxonomy.  
- Standardizing **department names** from HR systems (`HR`, `Human Res`, `People Ops`).  
- Normalizing **payment terms** (`Net30`, `30 Days`, `Thirty-day terms`).  

---

## Summary

When working with lookup or reference data in CluedIn:

- Use **deterministic rules** for exact, clean matches.  
- Apply **normalisers** to ignore irrelevant differences (case, punctuation).  
- Leverage the **Find Closest Match** Rule Action to automatically map inconsistent, fuzzy, or semantically similar values to your canonical list.  

This hybrid approach ensures **maximum automation** with **minimum risk**, reducing manual stewardship and improving data consistency across your ecosystem.

