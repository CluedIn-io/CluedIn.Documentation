---
layout: default
title: What is CluedIn
parent: Getting Started
permalink: /getting-started/what-is-cluedin
nav_order: 10
tags: ["getting-started"]
---
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

To understand the value of [CluedIn](https://www.cluedin.net), it is essential to talk about why the platform exists in the first place. We can all agree that, nowadays, all enterprise companies have many processes and projects which are _fueled_ by data. This data is typically not in a ready-to-use state, and hence it has to flow through some processes to make it ready for consumption. Whether the use-case is running advanced analytics, machine learning, business intelligence, anti-money laundering, obtaining a single view of your customer, or for data privacy - it turns out that all of these use-cases end up requiring very similar data preparation processes and attention. These standard processes are what CluedIn encapsulates into the platform. 

## Data management pillars

![Diagram](../assets/images/getting-started/pillars.png)

Data projects all start with data *discovery*. First, there is always a need to know where your data is and what systems it lies. After this, there is typically a stage of data *integration*, where you need to bring multiple data sources together into a unified or connected set of data. During this phase, you need to make sure that you are not putting too much pressure on the source systems, but at the same time would like the data available to the business as soon as possible. Choosing an integration style or pattern can be complex, but you have many choices - whether that is streaming, batch, CDC, or others.

After this integration has been done, the next step is to *normalize*, *standardize*, *harmonize*, and *clean* the data so that machines can process it in a uniform, consistent and high-fidelity manner. While this is occurring, you need to ensure you have control over the data by providing there is a clear owner responsible for its maintenance. This leads to the need for full traceability and audit trail of where this data is coming from, what is happening to it in this process of preparation, and where it is being used. With privacy being a mandated concern, you also need to make sure you have control over personal data and how it is used within the business. Finally, this data needs to be easily and readily available for the business to consume to fuel its operational needs. 

Whether your use case is Machine Learning or Business Intelligence, you will need to apply these same core pillars of data management detailed above. Of course, you might have extra steps in each use case, but these pillars above are at least the common pillars for any use-case involving data. CluedIn is this foundation layer that encapsulates everything we mentioned above into a coherent, consistent end-to-end data fabric of source to target data processing. 

What you get in the end can be described well in this demonstration video.

<iframe width="640" height="360" frameborder="0" allowfullscreen src="https://player.vimeo.com/video/331758206?controls=1"></iframe>

## Why did we create CluedIn? 

CluedIn exists because our team saw project after project failing because large enterprises were buying platforms that tackled each part of the journey - but failed in stitching these different pillars together into a platform. So CluedIn was born with the stitching, meaning that our different pillars were designed to work well with each other - in fact, they complement each other. 

Our documentation will help you understand more about the different components of CluedIn and how it all fits together. It will give you the insights you need to work with and extend the platform with your own needs. CluedIn is designed to be extended, and hence we offer easy and intuitive ways to inject your functionality or make our data available to other services to do what they do best. 

At a high level, you can conceptualize CluedIn as a streaming platform. We handle the constant flow of data and are designed to work in environments where systems don't stand still, and data is never static. 

CluedIn is an application that runs in Docker containers and uses Kubernetes as the way to host and orchestrate the different pieces of the application. Because of this, CluedIn is designed to work well in elastic environments and can automatically scale to the sizes and infrastructure you need to handle your data workloads. CluedIn runs large customers with 100's TB's of data and smaller customers with just a few TB's. So whether you have TB's or PB's of data to process - CluedIn can and will process your workloads.

It is essential to mention that CluedIn is a persistence layer. Unlike Data Virtualization, CluedIn ingests parts of your source data into its platform. Therefore, you have full control over what parts of your source data are ingested. The goal of CluedIn is to create the highest fidelity version of the data you will have in your business. It is not only the data itself but the structure of the data as well. With CluedIn having the highest fidelity version of your data, it means that any business request for data, in any format, in any modeling can be served out of the CluedIn Data Fabric. It will allow you to project data out exactly how the target systems would like as we contain the highest fidelity version of it. 

![Diagram](../assets/images/getting-started/high-fidelity.png)

We hope you enjoy and get value out of your CluedIn solution. 
