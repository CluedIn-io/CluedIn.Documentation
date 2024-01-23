---
layout: cluedin
title: Modelling
parent: Management
nav_order: 020
has_children: false
permalink: /management/modelling
tags: ["management","modelling"]
---

As you will have learnt from our `Eventual Connectivity` pattern, you do not need to do the classic modelling that you will typically do with data integration projects. Saying that, you can have complete control over how your systems are modelled.

![Diagram](../assets/images/management/intro-modelling.png)  

The model that is generated in the Graph database of CluedIn is dictated by the Entity Codes and Edges that you specify in your crawler or mappings. Because of this, you don't have direct access to the databases themselves and you are not going to be creating database models like you are used to - rather the models will be inferred from the database. Although this might seem like an odd approach, effectively what we are achieving here is a data model that is for connecting records. This model will not be normalised in any shape or form - quite the opposite. 

Once the model is formed in the graph, you will be able to use CluedIn's other tooling to project or form this model into all different types of models for downstream consumption. This is made possible as the graph that CluedIn generates is a high-fidelity data model that can downcast itself into all different types of sub-models e.g. relational model. 

When you think of building Master Data Management models, you often think in a modelling-first mindset. The challenge with this approach is that you are possibly setting an end-goal that is too complex to achieve. By having the model inferred you are essentially letting technology do a lot of the mind-bending modelling work on your behalf. Your perfect model will not be formed in CluedIn itself, but something even better - you will have your data in a model that can project itself into a perfect MDM model as well as other ad-hoc models that might come in the future. This flexibility allows you to have an MDM platform that can change with your business and the demands of the MDM itself.

If you are reading this and you are responsible for the modelling of data within CluedIn, it is important to remember that you are not trying to enforce a model onto the data coming into CluedIn. This is quite different to the way that other MDM providers do this, but in the end it yields a much better result. It is quite challenging to accept that you will bring data into your MDM system with a denormalised model, but the thing to remember is that you can put all different types of "views" over your data to make it represented in a way that fits into your perfect MDM model. 

The goal of the process is to get the data in a shape, quality and standard that can be adapted to different modelling needs without the need to redesign schemas and models as new requirements come up. 

For this it is also important to remember that when you are ingesting data into CluedIn, you need to start thinking in the terms of business objects, not rows or records. If you think in rows or records you will not get the true benefit of CluedIn. 