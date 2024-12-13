---
layout: cluedin
nav_order: 1
parent: Roles
grand_parent: Administration
permalink: /administration/roles/claims
title: Claims
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article, you'll find detailed explanation of each claim used in CluedIn. Claims, together with access levels, define user access to the features in CluedIn. The purpose of this article is to help you understand what actions on the platform a particular claim is related to.

## Integration

This section focuses on getting data into CluedIn from various sources: files, endpoints, databases, enrichers, integrations, and manual data entry projects.

**Available Integrations**

This claim governs access to all built-in integrations for connecting and pushing the data to CluedIn. It covers only one action—viewing available integrations.

**Configured Integrations**

This claim governs access to the actions for configuring an integration to push the data into CluedIn. It covers the following actions:

- Adding and editing an integration.
- Inviting a user to add an integration.
- Managing [permissions](/administration/user-access/data-access) to the data from an integration: adding or removing users or roles.
- Undoing a merge on the Topology tab of a golden record.

**Data Source Groups**

This claim governs access to the actions for importing your data into CluedIn, managing the resulting data sources, and processing data. To perform all actions within this claim, you should also have at least Informed access to several other claims: Configured Integrations, Annotation, Data Catalog, and Export Targets. Learn more about getting your data into CluedIn in [Data sources](/integration/data sources).

{:.important}
This claim does not govern access to data from data sources. To get access to data, you need to have appropriate source control and access control permissions.

This claim covers the following actions:

- Viewing data source groups.
- Viewing data sources and data source details. Access to the Data tab is granted based on data access permissions.
- Viewing data sets and data set details, except the Mapping tab (governed by the management.annotation claim). Additionally, access to the Data and Quarantine tabs is granted based on data access permissions.
- Editing and deleting a data source group.
- Editing a data source: changing name and logo.
- Managing a data set: archiving or removing.
- Editing the quality of a data source.
- Importing data from a [file](/integration/file), an [endpoint](/integration/endpoint), and a [database](/integration/database).
- Adding, editing, and removing [pre-process rules](/integration/additional-operations-on-records/preprocess-rules).
- [Processing](/integration/process-data) data to create new golden records or enhance existing ones.
- Managing processing logs: configuring retention period and purging logs.
- Managing [data set logs](/integration/additional-operations-on-records/logs): configuring retention period and purging logs.
- Managing permissions to data from the data source: adding or removing users or roles.

**Enrichment**

This claim governs access to enrichers, which improve the quality and completeness of your golden records with the help of third-party sources. Learn more about enhancing your golden records with external information in [Enricher](/preparation/enricher).

This claim covers the following actions:

- Viewing enrichers.
- Adding and editing enrichers.
- Managing permissions to data from the enricher: adding or removing users or roles.
- Managing the owners of the enricher: adding or removing users or roles.

**Manual Data Entry Input**

This claim governs access to the actions for creating new records directly in CluedIn and adding or editing golden record properties. It covers the following actions:

- Creating a new record in a manual data entry project.
- Editing the quality of a manual data entry project.
- Managing logs of a manual data entry project: configuring retention period and purging logs.
- Editing golden record property on the golden record details page.
- Adding new golden record property on the golden record details page.
- Viewing audit log for a golden record property.

**Manual Data Entry Project Management**

This claim governs access to the actions for setting up a manual data entry project. To perform all actions within this claim, you should also have at least Informed access to several other claims: Configured Integrations, Annotation, Data Catalog, Entity Types, and Export Targets.

This claim covers the following actions:

- Viewing a manual data entry project.
- Creating and editing a manual data entry project and form fields.
- Creating and editing form fields.

## Governance

This section focuses on data quality metrics, sensitive data identification, global data metrics, as well as global data model.

**Global Data Model**

This claim governs access to global data model that allows you to explore connections between entity types in the platform. It covers only one action—viewing global data model.

**Metrics**

This claim governs access to data quality metrics dashboards and global data metrics dashboards. It covers only one action—viewing respective dashboards.

**Personal Identifiers**

This claim governs access to metrics related to sensitive data. It covers only one action—viewing sensitive data metrics.

## Preparation

This section focuses on access to clean projects and cleaning activities.

**Clean**

This claim governs access to the actions for cleaning your golden records: creating a clean project, performing cleaning activities in the clean application, and sending cleaned golden records back to CluedIn. Learn more about data cleaning in [Clean](/preparation/clean).

{:.important}
This claim bypasses source control and access control permissions because access to data is essential to work in the clean project.

This claim covers the following actions:

- Viewing a clean project.
- Creating and editing a clean project.
- Generating and regenerating the results for a clean project.
- Performing clean activities in the clean application.
- Exporting records from the clean application.
- Processing cleaned records.
- Generating and viewing data part rules based on cleaning activities.
- Reverting changes to golden records as a result of cleaning activities.
- Managing owners of the clean project: adding or removing users and roles.
- Creating a clean project from search.

## Engine Room

This section focuses on various tools for monitoring what is happening inside CluedIn through real-time charts and summaries.

**Configuration Groups**

This claim governs access to configuration groups that contain environment variables, feature flag settings, and other settings that are being used by your CluedIn instance. It covers only one action—viewing configuration groups.

**Processing**

This claim governs access to the processing pipeline, where you can monitor high-level metrics of all the processing that happens in CluedIn such as ingestion, processing, and streaming activities. It covers only one action—viewing processing pipeline.

**Statistics**

This claim governs access to real-time charts showing global CPU and memory stats on the nodes that run your CluedIn instance. It covers only one action—viewing respective charts and dashboards.

## Management

This section focuses on various possibilities for managing your golden records: applying business rules, identifying and merging duplicates, managing your data catalog, and more.

**Entity Types**

This claim governs access to entity types (also known as business domains) that describe the semantic meaning of golden records. Learn more about entity types in a dedicated [article](/management/entity-type).

This claim covers the following actions:

- Viewing an entity type.
- Creating and editing an entity type.

**Access Control**

This claim governs access to the feature that allows you to set up fine-grained control over access to specific golden records and vocabulary keys.

This claim covers the following actions:

- Viewing access control policies.
- Creating and editing an access control policy.
- Managing owners of the access control policy: adding or removing users and roles.

**Annotation**

This claim governs access to the mapping in data sets and manual data entry projects. Lean more about data set mapping in [Create mapping](/integration/create-mapping) and [Review mapping details](/integration/review-mapping).

This claim covers the following actions:

- Viewing data set mapping details.
- Creating and editing data set mapping.
- Viewing mapping details in the manual data entry project.
- Editing mapping in the manual data entry project.

**Data Catalog**

This claim governs access to vocabularies and vocabulary keys. Learn more in [Data catalog](/management/data-catalog).

This claim covers the following actions:

- Viewing vocabularies and vocabulary keys.
- Creating and editing a vocabulary and a vocabulary key.
- Removing a vocabulary if it does not have vocabulary keys.
- Removing a vocabulary key if it is not used anywhere in the system or if it has been remapped to another vocabulary key.
- Managing owners of the vocabulary: adding or removing users and roles.
- Viewing changes in audit log of a vocabulary or vocabulary key.

**Deduplication Project Management**

This claim governs access to configuring a deduplication project and setting up matching rules. Learn more about deduplication project management in [Deduplication](/management/deduplication).

{:.important}
This claim bypasses source control and access control permissions because access to data is essential to work in the deduplication project.

This claim covers the following actions:

- Viewing a deduplication project.
- Creating and editing a deduplication project.
- Archiving a deduplication project.
- Generating or discarding matches in a deduplication project.
- Viewing groups of duplicates that were identified in a deduplication project.
- Managing owners of the deduplication project: adding or removing users and roles.
- Viewing changes in audit log of a deduplication project.

**Deduplication Review**

This claim governs access to reviewing and processing groups of duplicates that were identified in a deduplication project. Learn more about working in a deduplication project in [Manage groups of duplicates](/management/deduplication/manage-groups-of-duplicates).

{:.important}
This claim bypasses source control and access control permissions because access to data is essential to work in the deduplication project.

This claim covers the following actions:

- Processing groups of duplicates: selecting appropriate values among conflicting values, approving or rejecting a group for merge.
- Revoking approval from a group of duplicates if you decide not to merge it.
- Merging a group of duplicates to produce a consolidated golden record.
- Unmerging a golden record that was merged in the deduplication project.
- Viewing merged golden records produced in deduplication project.

**Glossary**

This claim governs access to glossary that contains groups of golden records, called terms, that meet specific criteria. It covers the following actions:

- Viewing terms by categories.
- Creating a category that acts as a folder for terms.
- Changing the name of a category.
- Creating a term within a category.
- Editing a term to define conditions for including golden records in the term and to change term configuration.
- Managing term status by activating or deactivating it as needed.
- Removing a term if you no longer need it.
- Endorsing a term to indicate to other users that it is reliable for their use.
- Viewing golden records that match conditions from term configuration.
- Managing owners of the term: adding or removing users and roles.
- View changes in term audit log.

**Hierarchy Builder**

This claim governs access to the actions for organizing, visualizing, and managing hierarchy relations between golden records within and across different business domains. It covers the following actions:

- Viewing all hierarchies and opening any hierarchy to view relations between its elements.
- Creating a hierarchy either by dragging elements onto the canvas or by leveraging relations between golden records.
- Editing hierarchy configuration: changing hierarchy properties, replacing nodes, deleting nodes or subtrees.
- Deleting a hierarchy if you no longer need it.
- Loading golden records connected by various types of relations so that these relations are automatically visualized in the hierarchy.
- Publishing the hierarchy to make the hierarchy relations available on the Relations and Hierarchies tab of golden records.
- Managing hierarchy owners: adding or removing users and roles.

**Rule Builder**

This claim governs access to the actions for managing all types of business rules that help you modify golden records in an organized and controlled manner. Learn more in [Rules](/management/rules).

{:.important}
This claim is applicable to all types of rules: data part rules, survivorship rules, and golden record rules. If you can create a data part rule, it means you can do the same with survivorship and golden record rules.

This claim covers the following actions:

- Viewing all rules and opening any specific rule to view its configuration.
- Creating a rule, specifying the golden records to which the rule will be applied, and choosing the action to be performed by the rule.
- Editing rule configuration: name, description, filters, and actions.
- Managing rule status by activating or deactivating it as needed.
- Removing a rule if you no longer need it.
- Reprocessing a rule to apply the rule's action to golden records associated with the rule.
- Managing rule owners: adding or removing users and roles.
- Viewing changes in the rule audit log.
- Editing rule processing order to prioritize the execution of specific rules over others.

## Workflow

This section focuses on access to automated workflows and approvals.

**Workflow Approvals**

This claim governs access to approval requests sent from the Power Automate widget in CluedIn. It covers the following actions:

- Viewing approval requests.
- Approving or rejecting an approval request.

**Workflow Builder**

This claim governs access to the actions for creating workflows in the Power Automate widget in CluedIn for automating specific approvals and processes. It covers the following actions:

- Viewing all workflows and opening any workflow to view its details.
- Creating a workflow for automating the approval process for a specific action in CluedIn.
- Editing a workflow.
- Managing workflow status by activating or deactivating it as needed.

## Consume

This section focuses on access to tools for configuring connection with external systems and exporting golden records from CluedIn to those systems.

**Export Targets**

This claim governs access to the actions for configuring external destinations where golden records from CluedIn can be sent. Learn more in [Export targets](/consume/export-targets).

This claim covers the following actions:

- Viewing all export targets and their configuration details.
- Adding and configuring an export target.
- Managing export target status by activating or deactivating it.
- Testing if CluedIn can connect to the export target.
- Managing permissions to of the export target: adding or removing users or roles.
- Managing export target owners: adding or removing users or roles.

**Graph QL**

This claim governs access to the GraphQL tool, where you can execute queries directly in the UI. It is useful when you need to query data in CluedIn and verify if your GQL syntax is correct. This claim covers only one action—executing queries in GraphQL.

**Streams**

This claim governs access to various actions for exporting golden records from CluedIn to the export target. Learn more in [Streams](/consume/streams).

This claim covers the following actions:

- Viewing all streams and their configuration details.
- Creating a stream.
- Editing a stream.
- Deleting a stream.
- Starting, pausing, and stopping the stream.
- Creating stream export target configuration: selecting a connector, specifying connector properties, and selecting golden record properties and relations for export.
- Editing stream export target configuration.
- Managing stream owners: adding or removing users or roles.
- Viewing changes in stream audit log.

## Admin

This section focuses on various administrative tasks in CluedIn.

**Data Management**

This claim governs access to various actions for managing golden records.

{:.important}
This claim bypasses source control and access control permissions because access to data is essential to work with golden records.  

This claim covers the following actions:

- Deleting a golden record.
- Triggering enrichment for a golden record.
- Reprocessing a golden record.
- Adding or deleting an edge to represent relations between golden records.
- Deleting a data part that contributes to a golden record on the History and topology tabs of the golden record.

**Roles**

This claim governs access to the roles in CluedIn, which in turn grant permissions to users to perform specific actions in the platform. Learn more about roles in a dedicated [article](/administration/roles).

This claim covers the following actions:

- Viewing a role, including its claims and access levels as well as users who have this role.
- Adding a new role and selecting the needed access level for each claim.
- Editing a role.
- Adding user to a role.

**Token Management**

This claim governs access to various actions for customizing your CluedIn instance. It covers the following actions:

- Viewing API tokens.
- Creating an API token.
- Revoking an API token.
- Viewing organization settings.
- Editing organization settings and saving changes.
- Viewing [feature flags](/administration/feature-flags), as well as turning them on or off as needed.
- Viewing theme configuration.
- Changing theme configuration.
- Viewing [entity page layouts](/administration/entity-page-layout) and their details.
- Editing an entity page layout.
- Adding or removing an entity page layout.

**Users**

This claim governs access to actions for managing users in CluedIn. Learn more about user management in a [dedicated article](/administration/user-management).

This claim covers the following actions:

- Viewing users who have been added to CluedIn, as well as user settings and roles.
- Inviting a user to CluedIn.
- Deactivating a user to prevent them from signing in to CluedIn.
- Viewing user invitations.
- Removing user invitation.
- Resending user invitation.