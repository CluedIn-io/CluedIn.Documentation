---
layout: cluedin
title: Work with CluedIn Copilot
parent: Copilot Integration
grand_parent: Microsoft Integration
permalink: {{ site.baseurl }}/microsoft-integration/copilot-integration/work-with-copilot
nav_order: 020
has_children: false
---
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

In this article, you will learn about Copilot skills that are available in CluedIn and find examples of prompts for each skill.

## Copilot overview

CluedIn Copilot is an AI assistant designed to help you with day-to-day data management tasks through conversational prompts in any language.

You can open the Copilot chat from any place in CluedIn by clicking on the message icon in the lower-right corner of the page. The Copilot pane contains all chats marked with color circles. If you want to rename or delete a chat, select **Copilot** next to the search bar.

CluedIn Copilot currently has 40+ specific skills (also called functions). To get a list of all these skills, use prompts similar to the following:

- What functions can you call?

- What are all the functions that I can do?

You'll find a description of each skill in [Copilot skills](#copilot-skills).

![functions.gif](../../assets/images/microsoft-integration/copilot/functions.gif)

To enhance your efficiency in interacting with CluedIn Copilot, you can **chain different skills together**. Instead of creating separate prompts for actions like creating, activating, and reprocessing a rule, you can combine these tasks into a single prompt.

```
Create a rule that tags all records with customer.country set to 'Norway' as 'Nordic', then activate and reprocess the rule.
```

Another example of chaining multiple skills together is using the anomaly detection skill followed by creating rules to mitigate it. Instead of entering two separate prompts, you can simply enter one combined prompt.

```
Find anomalies in training.country vocabulary keys. For each anomaly, create a rule (one per anomaly), which would best mitigate the anomaly. All rules are related only to /TrainingContact entity type.
```

CluedIn Copilot is **multilingual**, so you can activate all skills in any language you want, it doesn’t have to be English.

In most cases, CluedIn Copilot knows your **current location** in the platform. You can write prompts referring to what is currently displayed on the page, such as _this_ data set, _this_ vocabulary key, and so on.

You can combine **general knowledge** with CluedIn skills in one prompt.

```
Can you create a golden record rule that tags Company records where the company.state is not one of the Australian states.
```

Note that CluedIn Copilot does not offer a preview feature for its actions; it directly executes them.

## Copilot skills

This section contains all CluedIn Copilot skills grouped by categories or modules. Each skill contains one or several prompt examples to give you an understanding of how to use its functionality effectively.

{:.important}
Sometimes you may encounter issues with CluedIn Copilot where it does not understand your requests as expected. In such cases, as with any generative AI solution, please start over and create a new chat.

### Data set skills

CluedIn Copilot can analyze a data set to provide general overview, suggest possible mapping options, and create a mapping for the data set.

![dataset.gif](../../assets/images/microsoft-integration/copilot/dataset.gif)

| Copilot function | Description | Prompt example |
|--|--|--|
| DescribeDataSet | Provides general information about a data set: column description, possible validation checks, data quality issues, and so on.<br><br>If you are on the data set page, you can just tell the Copilot to describe _this_ data set. Otherwise, you can refer to the data set by its ID, which you can find in the URL of the page.  | Tell me a bit about this data set.<br><br>Describe this data set.<br><br>Describe the data set with ID 443259BB-1D17-4078-A069-7ECAD418BA19. |
| SuggestDatasetMapping | Provides suggestions on how to map a data set to an existing entity type and vocabulary. The suggested mapping can be used to define how the data set columns should be transformed and linked to the specified vocabulary.<br><br>If you are on the data set page, you can just tell the Copilot to suggest mapping for _this_ data set. Otherwise, you can refer to the data set by its ID, which you can find in the URL of the page. | Can you suggest a mapping from this data set to the Employee vocabulary?<br><br>Can you suggest how to map this data set to the Company vocabulary? |
| CreateDatasetMapping | Create a mapping from a data set to an existing business domain and vocabulary. Note that you'll need to set up the primary identifier to complete the mapping.<br><br>If you are on the data set page, you can just tell the Copilot to create mapping for _this_ data set. Otherwise, you can refer to the data set by its ID, which you can find in the URL of the page. | Can you create a mapping from this data set to the Employee vocabulary? |
| ListDataSets | Provides a list of all available data sets. Note that it is not possible to list data sets by creation date or other properties, you can only get a list of all data sets. | Can you list all data sets? |
| EntitySearchByDataSetColumnSample| Allows you to check if the values you have chosen as an entity code can already be found in the system. This can be helpful when you want to ensure that the chosen entity codes are unique and do not already exist in the system. | Can you check if values in the customerId column already have values in the system? |

### Rule-related skills

CluedIn Copilot can create all [types of rules](/management/rules/rule-types)—data part rules, survivorship rules, and golden records rules—and apply any [rule action](/management/rules/rules-reference).

![rule-tag.gif](../../assets/images/microsoft-integration/copilot/rule-tag.gif)

| Copilot function | Description | Prompt example |
|--|--|--|
| ActivateRule | Activates a rule. For more efficiency in your data management tasks, you can use this skill in one prompt along with creating a rule. | Can you create a rule to transform all values of the contact.country vocabulary key to upper-case, and then activate this rule? |
| CloneRule | Creates a copy of a rule. Once the copy is created, you'll get a link to view and manage the rule. | Can you create a copy of this rule? |
| CreateGoldenRecordRule | Creates a new golden record rule. You can use this skill in one prompt along with activating and reprocessing a rule. Once the copy is created, you'll get a link to view and manage the rule. | Create a golden record rule that tags all Company records where the company.state is not in one of the valid Australian states, and tag it with "Invalid Australian State".<br><br>Can you create a rule that detects if the doctor.npi matches the pattern of a valid NPI number and tag any record that does not with "Invalid NPI Number"? |
| CreateProcessingRule | Creates a new data part rule. You can use this skill in one prompt along with activating and reprocessing a rule. Once the rule is created, you'll get a link to view and manage the rule. | Can you create a rule to transform all values of the contact.country vocabulary key to upper-case? |
| CreateSurvivorshipRule | Creates a new survivorship rule. You can use this skill in one prompt along with activating and reprocessing a rule. Once the rule is created, you'll get a link to view and manage the rule. | Can you create a survivorship rule to define the winning value for organization.countryCode based on the most frequently used value? |
| DeactivateRule | Deactivates a rule. | Can you deactivate all golden record rules? |
| ReprocessRule | Reprocesses a rule to apply the rule's actions to records that match the rule's filter. This skill can be used in one prompt along with creating and activating a rule for more efficient data management tasks. | Create a rule that tags all records with customer.country set to 'Norway' as 'Nordic', then activate and reprocess the rule. |
| SuggestVocabularyKeyRules | Provides suggestions for validation or business rules for a particular vocabulary key. You can review these suggestions and then decide which rules to create.<br><br>If you are on the vocabulary key page, you can just tell the Copilot to suggest rules for _this_ vocabulary key.  | Can you suggest rules for this vocabulary key? |

### Data catalog skills (vocabulary and vocabulary key)

CluedIn Copilot can create vocabularies and vocabulary keys as well detect anomalies in vocabulary key values.

![profiling.gif](../../assets/images/microsoft-integration/copilot/profiling.gif)

| Copilot function | Description | Prompt example |
|--|--|--|
| CreateVocabulary | Creates a new vocabulary with the specified name. Once a new vocabulary is created, you'll get a link to view and manage the vocabulary details.<br><br>If you are on the page of the business domain you want to associate the vocabulary with, you can just tell the Copilot to create the vocabulary for _this_ business domain. If you don't specify the business domain, it will be provided automatically, but you can change it later. | Can you create a new vocabulary called Company for the Company business domain?<br><br>Can you create a new vocabulary called Company for this business domain? |
| CreateVocabularyKey | Creates a new vocabulary key with the specified name. If you previously created a vocabulary in the chat, the new vocabulary keys will be added to that vocabulary.<br><br>You can create individual vocabulary keys one at a time by entering a separate prompt for each vocabulary key. However, if you need to create multiple vocabulary keys, you can instruct Copilot to perform the task in a single prompt. | Can you create 10 vocabulary keys including Name, Age, Gender, JobTitle, ContactNumber, Email, ManagedBy, Salary, Tenure and NickName? |
| ProfileVocabularyKey | Creates profiling for a vocabulary key. | Can you profile this vocabulary key? |
| StandardizeData | Provides suggestions on how to standardize or normalize values within a vocabulary key. You can review the suggestions and then instruct Copilot to create rules or do it on your own. | Can you standardize values of this vocabulary key? |
| DetectAnomaly | Detects anomalies in the top 10000 values of a vocabulary key.<br><br>While viewing a vocabulary key, you can ask CluedIn Copilot to suggest some standardization of the data and it will recommend (but not change) values that are similar and that should be set up as rules. | Can you find any anomalies in this vocabulary key? If so, can you create a golden record rule per anomaly that tags it with "Invalid City“? |
| ListVocabularies | Lists all vocabularies. | Can you list all vocabularies that are currently used in the system? |
| ListVocabularyKeys | Lists vocabulary keys associated with a vocabulary. | Can you list all vocabulary keys associated with the Contact vocabulary? |
| ChangeVocabularyKeyToGlossaryTermLookupKey | Changes a vocabulary key into a lookup value. | Can you change the company.country vocabulary key to a lookup key? |

### Deduplication-related skills

CluedIn Copilot can create deduplication projects and display information about those projects and groups of duplicates. However, it currently cannot create the matching rules.

| Copilot function | Description | Prompt example |
|--|--|--|
| CreateDeduplicationProject | Creates a deduplication project. Once the project is created, you'll get a link to view and configure the project. | Can you create a deduplication project for Customer records?  |
| ExplainDeduplicationGroup | Provides general information about a deduplication group based on the comparison of the fields. You need to provide the group ID, which you can find in the URL of the page. | Explain the group of duplicates with this ID 71926613-deed-4f2e-b300-311359b76869. |
| GenerateResultsDeduplicationProject | Generates results of a deduplication project.<br><br>If you are on the project page, you can just tell the Copilot to generate results of _this_ project. Otherwise, you can refer to the project by its ID, which you can find in the URL of the page. | Can you generate the results of this deduplication project? |
| ListDeduplicationProject | Provides a list of all available deduplication projects, including project ID, project name, ID of the user who created the project, creation date, and whether the project is archived or not. | Can you list all deduplication projects? |

### Stream and export target skills

CluedIn Copilot can create and start streams to share data with other systems. Note that it cannot yet pause or stop streams.

| Copilot function | Description | Prompt example |
|--|--|--|
| CreateStream | Creates a stream. Since stream configuration requires many details, consider asking the Copilot to provide a list of information needed to create a stream. You can then enter the required information step by step.<br><br>Typically, you need to provide the stream name, condition, actions (if necessary), name for the content in the external system, export target ID, streaming mode, edges (if necessary), and properties to export.  |I need to create a stream. What details do you need? |
| CloneStream | Creates a copy of the stream configuration. Note that you'll have to provide the export target configuration in the copied stream.  | Can you create a copy of this stream? |
| StartStream | Starts a stream. | Can you start this stream? |
| ListStreams | Provides a list of all available streams, including stream ID, name, and status. | Can you list all streams? |
| ListExportTargets | Provides a list of all available export targets, including export target ID, type, and whether it is enabled or not. | Can you list all export targets? |

### Clean-related skills

CluedIn Copilot can create clean projects according to your requirements and display information about the existing clean projects. However, it currently cannot generate the results of the clean project.

![clean.gif](../../assets/images/microsoft-integration/copilot/clean.gif)

| Copilot function | Description | Prompt example |
|--|--|--|
| CreateCleanProject | Creates a clean project. You'll get a brief project description, including top 10 records that match the project's filters. You can click the link to go to the clean project and validate if Copilot did the right thing. Then you'll be able to generate the project results on your own. | Can you create a clean project to fix contact.jobTitle values in records of the Contact business domain? |
| ListCleaningProjects | Provides a list of all available clean projects, including project ID and project name. | Can you list all clean projects?<br><br>What clean project are currently available in the platform? |

### Hierarchy skills

CluedIn Copilot can create hierarchies to visualize relations between golden records.

| Copilot function | Description | Prompt example |
|--|--|--|
| CreateHierarchy | Creates a new hierarchy. Before creating the hierarchy, make sure that the records have the appropriate edge type defined.  Once the hierarchy is created, you'll get a link to view the details. | Can you create a hierarchy called Org Chart for all records of the Contact business domain? |
| ListHierarchies | Provides a list of all available hierarchies, including status, number of nodes, creation and modification dates. | Can you list all hierarchies that are available in the system? |

### Glossary skills

CluedIn Copilot can create glossary terms within specific category and display information about the existing glossary categories.

| Copilot function | Description | Prompt example |
|--|--|--|
| CreateGlossaryTermSkill | Creates a glossary term within the specified category. You might be asked to provide the ID of the category, which you can find in the URL of the page. Once the term is created, you'll get a link to view the details. | Can you create a glossary term called North America that would include Customer records whose contact.businessRegion vocabulary key is set to North America? |
| ListGlossaryCategories | Provides a list of all available glossary categories. | Can you list all glossary categories?<br><br>What glossary categories are available in the platform? |  

### Other skills

CluedIn Copilot can search for golden records according to your requirements as well as perform actions related to business domains (create, describe, list).

![search.gif](../../assets/images/microsoft-integration/copilot/search.gif)

| Copilot function | Description | Prompt example |
|--|--|--|
| DataQualityMetrics | Provides current global data quality metrics. | Can you show me the global quality metrics? |
| Search | Finds records according to your input.<br>CluedIn will return the top 10 results in a table and a link to launch into the full search query as well. | Can you find the Person records where the user.country is in the Nordics? |
| ListEntityTypes | Provides a list of all available business domains. Note that business domains that have no associated data will not appear in the list. | Can you list all entity types? |
| CreateEntityType| Creates a new business domain with the specified name. Once a new business domaine is created, you'll get a link to view details. | Can you create a new entity type named Company? |
| DescribeEntity | Provides general information about a golden record: business domain, name, codes, properties, vocabularies, and so on.<br>If you are on the golden record page, you can just tell the Copilot to describe _this_ golden record.  | Can you describe this golden record? |
