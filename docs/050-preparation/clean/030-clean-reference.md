---
layout: default
nav_order: 3
parent: Clean
grand_parent: Preparation
permalink: /preparation/clean/clean-reference
title: Clean reference
tags: ["preparation", "clean"]
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article, you will find reference information to help you understand the statuses of clean projects and the process of working with them.

## Clean project statuses

The following table provides the description of the clean project statuses.

| Status | Description |
|--|--|
| New | The clean project has been created, no results have been generated yet. |
| Generating | CluedIn is generating the results of the clean project. The records that match the filters and selected properties from the configuration are loaded into the clean application. This status also appears when you are regenerating the results to load the latest data to the clean application. |
| Generation aborting | The process of generating or regenerating the results of the clean project is being cancelled. The status will shortly change to **New**. |
| Ready for clean | CluedIn has generated the results of the clean project and you are now ready to perform cleaning activities in the clean application. |
| Ready to process | The clean project contains some changes of values that were made in the clean application. |
| Processing | CluedIn is publishing fixed values to the golden records. |
| Processing aborting| The process of publishing fixed values to the golden records is being cancelled. The status will shortly change to **Ready to process**. |
| Processed | CluedIn has published the fixed values to the golden records. |
| Reverting | CluedIn is reverting the results of the clean project, returning the values in golden records to their state before cleaning. |
| Revert aborting | The process of reverting changes is being cancelled. The status will shortly change to **Ready to process**.  |
| Archived | The clean project is no longer active. Once the project is archived, it cannot be unarchived.  |

## Clean project status workflow

The following diagram shows the clean project workflow along with its statuses and main activities.

![clean-reference-1.png](../../assets/images/preparation/clean/clean-reference-1.png)

**Note:** The **Archived** status is not shown in the diagram, but you can archive the clean project when it is in any status except **Generation aborting**, **Processing aborting**, and **Revert aborting**.