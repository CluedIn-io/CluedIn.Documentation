---
layout: cluedin
title: Enrichers, AI agents, and automation design
parent: Data Architect course
grand_parent: Learning paths
nav_order: 80
permalink: /learning-paths/data-architect-course/enrichers-ai-agents-and-automation-design
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

CluedIn can extend records with enrichers and AI-driven jobs, but those automation surfaces need architectural discipline. Otherwise they become another source of opaque changes instead of controlled improvement.

## What you should get from this module

- understand the documented built-in enrichers and AI-agent roles
- choose enrichment and AI patterns deliberately
- design automation with traceability and review in mind

![builtin_agents_sp.png]({{ "/assets/images/management/ai-agents/built-in-ai-agents/builtin_agents_sp.png" | relative_url }})

## Guided walkthrough

Begin with the enricher reference. The important lesson is not to memorize every package. It is to understand the categories of enrichment that CluedIn supports: company registries, maps, web sources, AI services, and custom or REST-based patterns. These enrichers can reshape records significantly by adding new data parts and external context.

Now return to the built-in AI agents page. The platform explicitly documents default roles:
- Data Steward for fixing quality issues and looking for duplicates
- Data Architect for creating rules

That means AI is being positioned as an accelerator for documented operational and architectural tasks, not as a magical replacement for design thinking.

Teach three architecture principles here:

1. **Scope before automation**  
   Always know which population the automation will touch.

2. **Review before trust**  
   Test jobs and inspect outcomes before broad enablement.

3. **Traceability after execution**  
   Make sure downstream teams can understand what changed, why it changed, and how to reverse course if needed.

Also connect enrichment to golden-record behavior. Every enricher or AI-driven correction changes the record's shape over time. The architect should expect those changes to show up in record history, stewardship workflows, and sometimes downstream streams.

## Role lens

Automation should reduce toil, not reduce explainability. The architect is responsible for making automation legible to stewards and safe for consumers.

## Practice assignment

Pick one business domain and propose:

- one suitable enricher category
- one AI-assisted use case
- the scope definition you would use
- how you would test it
- what success and failure would look like operationally

## Exit criteria

- The learner can describe when enrichers and AI are useful in CluedIn.
- The learner can scope and test automation responsibly.
- The learner understands the need for traceability after automated changes.

## Suggested source material

- [Enricher reference](/preparation/enricher/enricher-reference)
- [Built-in AI agents](/management/ai-agents/built-in-ai-agents)
- [Tag monitoring](/governance/tag-monitoring)
