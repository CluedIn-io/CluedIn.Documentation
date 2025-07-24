---
layout: cluedin
title: Data Marts
parent: Consume
nav_order: 30
permalink: consume/data-marts
tags: ["consume"]
published: false
---

Data Marts allow you to prepare certain data sets for future consumption. Unlike a Stream, a Data Mart is not necessarily yet data that is being made available to any consumers, but at the same time you might find that a Data Mart is consumed multiple times. 

The idea behind a Data Mart in CluedIn is to logically group a certain collection of data in which you can apply operations directly to just that data and nothing else. Examples include:

 - Being able to have Data Quality Metrics on a particular subset of data. 
 - Being able to Clean a paritcular subset of data. 
 - Being able to expose what the data in a Data Mart is being used for (Showcasing)

Data Marts can be created in a way that they can be static snaphots of data, or live and dynamic sets of data. There are times when you might want to setup temporal based Data Marts e.g. 2019 Customers. There are other times when you will want the Data Marts to be more "live" and when underlying data changes or is added, you want the Data Mart to relfect this e.g. Customers. 