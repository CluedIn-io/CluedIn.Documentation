---
layout: cluedin
title: Use this documentation with an AI assistant
parent: Get started
nav_order: 90
permalink: /get-started/ai-assistants
content_type: how-to
tags: ["ai", "llms.txt", "mcp"]
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

Point an AI assistant such as Claude, ChatGPT, Microsoft Copilot or Cursor at this documentation so it answers CluedIn questions from the current pages instead of from memory, and reads them in a form that costs it far fewer tokens than the web pages.

{:.important}
This page is about **your own AI assistant** reading the documentation. It is not about CluedIn's [AI agents](/govern/ai-agents), the product feature that works on your golden records inside CluedIn.

## Prerequisites

- An AI assistant that can fetch web pages, either built in or through a fetch tool connected over MCP (Model Context Protocol).

## Point the assistant at the documentation

Give the assistant this address, and tell it to start there:

```text
https://documentation.cluedin.net/llms.txt
```

`llms.txt` is an index written for AI assistants. It explains how the documentation is organised and which kind of page answers which kind of question, then lists every section and subsection with a one-line summary. From there the assistant fetches only the pages it needs.

For example, start a conversation with:

```text
Use https://documentation.cluedin.net/llms.txt to answer my questions about CluedIn.
Fetch the .md version of each page you read.
```

## Give the assistant a single page

Every page is also published as Markdown, at its address with `.md` added:

| Page | Markdown for the assistant |
|---|---|
| `https://documentation.cluedin.net/govern/enrichment/add-enricher` | `https://documentation.cluedin.net/govern/enrichment/add-enricher.md` |

The Markdown has the page's text, tables, code and notes, without the site navigation. A section page ends with a list of the pages in it.

To copy a page into a conversation instead, select **Agent mode** in the top bar. The page is replaced by its Markdown, with buttons to copy it, copy its address, or open it. Select **Agent mode** again to return to the normal page.

## Load the whole documentation

To put all the product documentation into a tool that indexes documents, such as a project's knowledge files or a search index, use:

```text
https://documentation.cluedin.net/llms-full.txt
```

It is large — the whole product documentation in one file — so give it to a tool that indexes it, rather than pasting it into a single conversation.

## Let the assistant work in your CluedIn instance

The documentation tells an assistant how CluedIn works. To let it act in your own CluedIn instance, connect the assistant to the CluedIn MCP server as described in [Connecting CluedIn MCP to Claude, ChatGPT and Microsoft Copilot](/govern/ai-agents/ai-agents-faqs#connecting-cluedin-mcp-to-claude-chatgpt-and-microsoft-copilot).

For the REST API, the [API reference](/api) links the OpenAPI document for each category; the complete specification is `https://documentation.cluedin.net/assets/api/swagger.json`.

## Verify the result

Ask the assistant a question that only the current documentation answers, and ask it which pages it read. It should name `.md` addresses on `documentation.cluedin.net`. If it answers without naming any, it answered from memory: repeat the instruction to start from `llms.txt`.

## If something goes wrong

| What you see | What to do |
|---|---|
| The assistant says it cannot open web pages. | Turn on its web access, or connect a fetch tool over MCP, then try again. Without one, select **Agent mode** on a page and paste the copied Markdown into the conversation. |
| The assistant uses old terms such as *entity* or *entity type*. | Point it at the [terminology](/get-started/terminology) page. `llms.txt` also lists the renamed terms. |
| The assistant confuses its own work with CluedIn's AI agents. | Tell it that "AI agents" in this documentation is a CluedIn feature, described under [AI agents](/govern/ai-agents). |
