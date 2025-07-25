---
layout: cluedin
title: Eventual connectivity
parent: Key terms and features
nav_order: 8
has_children: false
permalink: /key-terms-and-features/eventual-connectivity
tags: ["development","eventual-connectivity"]
---

The eventual connectivity pattern is at the heart of CluedIn. This pattern of integration makes it simple to blend data from many different systems into a unified and connected data set.

**Example**

Let’s explore the concept of eventual connectivity in CluedIn through an example. We have a golden record that mentions an email address. This email address indicates that there might be another data set where the email is also used. So, CluedIn creates a shadow entity, which acts as a placeholder, with the email address. This shadow entity may have several codes, one of which is built using the email address.

At this point, the document golden record is related to the shadow entity. When a new record containing the same email address appears in the system, CluedIn recognizes matching emails, and replaces the shadow entity with a new golden record. In the end, the document record is now related to another golden record, and not to the shadow entity.

![eventual-connectivity-1.gif]({{ "/assets/images/key-terms-and-features/eventual-connectivity-1.gif" | relative_url }})

**Goal of eventual connectivity**

The goal of eventual connectivity is not to model your data into a final form but to provide a flexible model inferred from the source systems. This means that you don't have control over the modelling within CluedIn up-front, but you will have control later in the process. You won't have to conduct long and tedious architecture meetings to discuss how different systems will connect with each other. The eventual connectivity pattern will do the blending of data for you, as long as you can instruct it and guide it using its underlying concepts.

**Underlying concepts**

- Identifiers – universally unique identifiers of a record. Read more about identifiers [here](/key-terms-and-features/entity-codes).

- Edges – a way to instruct CluedIn that there is a reference from one object to another. Edges are the key behind the eventual connectivity pattern. Read more about edge [here](/key-terms-and-features/edges).

- Shadow entities (also known as floating edges) – records that are constructed from edges, with the expectation that the system will eventually find a link between these records.

- Aliases – a way to instruct CluedIn that there is a property that can fuzzily lead to a linkage between golden records.

- Vocabularies – a way to map properties from the source system to a common vocabulary that CluedIn understands. The vocabularies are key to bridge data across systems. For more information, see a video about vocabulary key mapping [here](/management/data-catalog/modeling-approaches).

**Main advantage**

The main advantage of the eventual connectivity pattern is that you can take one system or even one object within a system at a time, determine the codes, aliases, and edges for an object, and then let the pattern manage how everything will blend together. It is also important to remember that with edges, we do not expect you to know where the reference is pointing to. Rather we would ask you to instruct us that a particular field or column should point to another record. This record could be in the current system, or it could be in another system all together.