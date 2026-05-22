---
layout: cluedin
title: Best Practices for Matching and Merging
parent: Knowledge base
permalink: /kb/best-practices-for-matching-and-merging
nav_order: 2
---


# Best Practices for Matching and Merging in CluedIn

Matching and merging is a core capability of CluedIn. It allows you to identify duplicate records across systems and consolidate them into a single golden record. A well-designed matching strategy ensures that the platform can reliably detect duplicates while maintaining high confidence in automated merges.

This article outlines the available approaches to matching in CluedIn and provides practical best practices for designing an effective matching strategy.

---

# Approaches to Matching and Merging

CluedIn provides three primary approaches to identifying duplicates. These approaches can be used independently or together depending on the complexity and quality of your data.

## 1. Matching Rules (Deterministic and Probabilistic)

The most common approach to matching in CluedIn is through **Matching Rules**.

Matching rules allow you to define how records should be compared in order to determine if they represent the same entity. CluedIn supports both:

- **Deterministic matching** – exact or strict comparisons  
- **Probabilistic matching** – similarity or fuzzy comparisons  

You can create **multiple matching rule groups**, and CluedIn supports **cascading matching**.

This means:

1. The first rule group attempts to find matches.
2. If no match is found, CluedIn automatically attempts the next rule group.
3. This continues through all configured groups until a match is found or all groups have been evaluated.

This cascading approach allows you to start with highly confident rules and gradually fall back to broader matching logic.

### Using Normalizers

Matching rules can also use **Normalizers**, which allow you to influence how values are compared without modifying the underlying data.

Examples include:

- Ignoring casing differences
- Standardizing whitespace
- Normalizing formatting differences

For example:


John.Smith@Company.com

john.smith@company.com


With appropriate normalization, these values can be matched without requiring changes to the original data.

Normalizers allow you to improve matching accuracy while keeping your source data intact.

---

## 2. Matching Using Identifiers or Keys

Another approach is matching using **identifiers or keys**.

This is the **simplest and most deterministic** form of matching.

In this approach:

- Records are matched based on a shared **unique identifier**
- The identifier is typically sourced from upstream systems
- Configuration is managed in the **CluedIn mapping screens**

Examples of identifiers include:

- CRM IDs  
- Customer numbers  
- External system keys  
- Source system record IDs  

When reliable identifiers exist, this method can produce extremely accurate matching with minimal configuration.

However, many real-world datasets do not always contain consistent identifiers, which is why rule-based or AI-driven matching may also be required.

---

## 3. AI Agents and the Find Duplicates Skill

CluedIn also supports **AI-powered matching** through **AI Agents** using the **Find Duplicates** skill.

This approach allows you to analyse large volumes of data without relying on traditional matching rules.

AI Agents use a **rule-less matching approach**, meaning they evaluate records based on semantic similarity rather than predefined rules.

This can identify potential duplicates that traditional rule-based methods would struggle to detect.

For example:

| Value A | Value B |
|--------|--------|
| NASA | Space Company |

Although these values are **semantically related**, a traditional rule-based approach based on string similarity would likely not detect them as related.

AI Agents can identify these kinds of relationships because they analyze meaning rather than just string distance.

It is important to understand that this approach **does not replace rule-based matching**. Instead, it complements it by identifying matches that rules may miss.

---

# Best Practice: Clean Data Before Matching

One of the most effective but sometimes counterintuitive strategies when designing matching rules is:

> **Clean your data to fit your matching rules rather than creating increasingly complex rules to fit messy data.**

Many teams initially attempt to solve data quality issues by building large numbers of matching rules. However, this often leads to:

- Complex rule configurations
- Higher maintenance overhead
- Increased risk of incorrect matches

Instead, a better approach is to **standardize and clean the data first**, and then apply simpler matching rules.

CluedIn provides **CluedIn Clean** to support this process.

Examples of data cleaning include:

- Standardizing phone number formats
- Normalizing company names
- Removing inconsistent casing
- Aligning address structures
- Removing punctuation or formatting inconsistencies

### Benefits of Cleaning Data First

Cleaning your data before matching provides several advantages.

#### 1. Improved Data Quality

The most obvious benefit is that your data becomes more consistent and easier to use across the platform.

#### 2. Simpler Matching Rules

Once data is normalized, you can often use **deterministic matching rules** rather than fuzzy comparisons.

For example, instead of fuzzy matching:


Company Name ~ Company Name


You may be able to use deterministic matching:


Normalized Company Name = Normalized Company Name


#### 3. Increased Automation

Deterministic rules are typically more reliable and easier to automate. This can reduce manual review and improve overall trust in the matching process.

---

# Best Practice: Use AI Matching to Find Additional Candidates

AI-based matching works particularly well as a **secondary layer of duplicate detection**.

Because AI Agents analyze **semantic relationships**, they can identify connections between records that would not normally be detected through rule-based matching.

This is especially useful for:

- Inconsistent naming conventions  
- Indirect entity relationships  
- Organizations with multiple naming variations  
- Industry or semantic similarities  

For example:

| Record A | Record B |
|---------|---------|
| NASA | Space Company |

Although these values have little string similarity, they clearly represent related concepts. AI-based matching can detect these types of relationships.

This approach is particularly useful for:

- **Discovering hidden duplicates**
- **Generating candidate matches for review**
- **Augmenting rule-based matching strategies**

Rather than replacing rules, AI Agents provide an additional technique that can surface **unique matches that are otherwise difficult to find**.

---

# Summary

CluedIn supports three complementary approaches to matching and merging:

| Approach | Description |
|--------|-------------|
| Matching Rules | Deterministic and probabilistic rules with cascading logic |
| Identifier Matching | Matching based on unique system identifiers |
| AI Agents | Semantic matching using the Find Duplicates skill |

To maximize matching accuracy:

1. **Clean and standardize data before creating complex rules**
2. **Use deterministic rules wherever possible**
3. **Leverage identifiers when available**
4. **Use AI Agents to uncover additional matches that rules cannot detect**

Combining these approaches allows organizations to build a robust and scalable matching str
