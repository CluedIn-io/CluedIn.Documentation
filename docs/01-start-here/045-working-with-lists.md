---
layout: cluedin
title: Working with lists
parent: Get started
nav_order: 45
permalink: /get-started/working-with-lists
content_type: concept
tags: ["getting-started"]
---

## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

CluedIn shows most of its data — data sources, deduplication projects, audit logs, workflows, and more — as a list or table. Most of these lists share the same toolbar, so once you know how one works, you know how most of them work.

![A list's toolbar, showing a search box, a refresh button, and an Export CSV button, above sortable column headers]({{ "/assets/images/getting-started/working-with-lists/list-toolbar.png" | relative_url }})

## Refreshing a list

Select the refresh icon in the toolbar to reload a list's data from the server without reloading the browser page. Your current sort, filter, and page stay as they are — only the underlying data updates.

## Sorting and filtering

Where a column supports it, select its header to sort the list by that column; select again to reverse the sort direction. Most lists also have a search box in the toolbar that filters the list as you type.

## Selecting across pages

On lists that support bulk actions, selecting the checkbox in the header selects every row on the current page. If the list spans more than one page, a banner offers to extend the selection to every row that matches your current filter — not just the page you're looking at. Changing a filter while an across-page selection is active clears it, since the selection no longer matches what's on screen.

## Exporting to CSV

Select **Export CSV** to download the list as a spreadsheet. Where a list spans more than one page, you're offered two choices:

- **Export all results** downloads every row matching your current filter, not just the current page. This is the default choice for most lists.
- **Export current page** downloads only the rows currently on screen.

The downloaded file name includes the scope you chose (`all` or `page`) and the date, so repeated exports don't overwrite each other.

Not every list has every one of these capabilities — a few lists have no bulk actions to select across pages, and a few have no more than one page of data to export "all" of. Where a capability doesn't apply, its control simply isn't shown.
