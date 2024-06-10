---
layout: cluedin
title: Dynamic Vocabularies
parent: Development
nav_order: 300
has_children: false
permalink: /development/dynamic-vocabularies
tags: ["development","vocabularies"]
published: false
---

There are many times where you will get data that cannot be statically mapped in code or via a mapping in a user interface. In CluedIn these will map to dynamic vocabularies. Dynamic vocabularies are a way to tell CluedIn that a particular value has no Vocabulary mapping. Essentially, CluedIn will start to inspect the values in these properties to infer the types and details of the static Vocabularies. This is not necessarily a bad thing and even in the static mapping cases, CluedIn will analyse the values anyway as to determine if a Vocabulary mapping was done incorrectly. This is important for anomaly detection and outlier detection of values. 

You can set a Dynamic Vocabulary by adding the "-custom" flag at the end of your Vocabulary Key. This will instruct the CluedIn Processing Server that it will need to do extra analysis on the values to help determine things that can statically be set with normal Vocabularies such as Data Types. Be aware that every time you use the "-custom" flag, that you will incur more than normal processing on the server. 

If you use the `DynamicVocabulary` class for your `Vocabulary` then it will handle all of the "-custom" flag for you.