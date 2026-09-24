---
layout: cluedin
title: Configuration import and export
parent: Administration
permalink: /administration/configuration-import-export
nav_order: 115
tags: ["administration", "configuration", "deployment", "import", "export"]
last_modified: 2026-09-24
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

The **Configuration Import / Export** feature lets you move CluedIn configuration between environments directly from the user interface.

It is designed for scenarios where you configure CluedIn in one environment—for example, **Development**—and then want to promote that configuration to **Test** and **Production** without having to run PowerShell scripts.

A typical promotion flow is:

```text
Development  ->  Export configuration  ->  Configuration package
                                              |
                                              v
Test         <-  Import configuration  <------
                                              |
                                              v
Production   <-  Import approved configuration
```

This makes it easier for administrators and implementation teams to keep environments aligned while still maintaining separate Development, Test, and Production instances.

{:.important}
Configuration Import / Export moves **CluedIn configuration** between environments. It is not used to copy the mastered data stored in an environment and it does not deploy or upgrade the CluedIn application or its infrastructure.

## When to use Configuration Import / Export

Use the UI-based Configuration Import / Export experience when you want to:

- Promote configuration from Development to Test or Production.
- Reproduce an approved configuration in another CluedIn environment.
- Move configuration without installing or running PowerShell tooling.
- Perform occasional or administrator-driven environment synchronization.
- Create a configuration package that can be reviewed and then imported into another environment.

For example, you might configure business domains, mappings, rules, streams, or other supported CluedIn configuration in Development, validate it, and then export the configuration for import into Test.

After testing is complete, the approved configuration can then be promoted to Production.

## Open Configuration Import / Export

To open the feature:

1. On the navigation pane, go to **Administration**.

1. Select **Configuration Import / Export**.

The page contains separate areas for:

- **Exports** – create and manage configuration packages produced from the current environment.
- **Imports** – import a configuration package into the current environment.

## Export configuration

Use an export to capture configuration from the current CluedIn environment.

For example, if Development contains the latest approved configuration, create the export from Development before moving it into Test.

**To export configuration**

1. Go to **Administration** > **Configuration Import / Export**.

1. Select **Exports**.

1. Select **Start export**.

1. Configure the export and select the CluedIn configuration that you want to include.

1. Start the export.

CluedIn creates a configuration package that can be transferred to another environment.

The export history on the page lets you keep track of configuration exports that have been created.

{:.note}
The configuration options available for export can vary depending on the CluedIn version and features enabled in the environment.

## Import configuration

Use an import to apply a previously exported configuration package to another CluedIn environment.

For example, after exporting configuration from Development:

1. Open the Test environment.

1. Go to **Administration** > **Configuration Import / Export**.

1. Select **Imports**.

1. Start a new import.

1. Provide the configuration package exported from Development.

1. Review the configuration to be imported.

1. Run the import.

After validating the configuration in Test, you can repeat the process to promote the approved package to Production.

## Recommended Development, Test, and Production flow

A common process is:

1. **Configure in Development** – create and modify CluedIn configuration in the Development environment.

1. **Export from Development** – create a configuration package after the changes are ready for testing.

1. **Import into Test** – import the package into the Test environment.

1. **Validate in Test** – confirm that the imported configuration behaves as expected with the Test environment and its data.

1. **Promote the approved configuration** – use the approved configuration package to import the same configuration into Production.

This approach helps avoid manually recreating the same configuration in every environment.

It also reduces configuration drift because Test and Production can be based on the same configuration that was prepared in Development.

## Configuration Import / Export vs Product Deployment Toolkit

The UI-based Configuration Import / Export feature **does not replace the CluedIn Product Deployment Toolkit**.

Both approaches are intended to help move CluedIn configuration between environments, but they are optimized for different operating models.

| Approach | Best suited for |
|--|--|
| **Configuration Import / Export in the CluedIn UI** | Administrator-driven or occasional configuration promotion where users want to export and import configuration without running scripts. |
| **CluedIn Product Deployment Toolkit** | Automated configuration promotion, CI/CD pipelines, source-controlled releases, repeatable deployments, and integration with DevOps processes. |

### Use the UI when

The UI is a good choice when:

- An administrator wants to promote configuration manually.
- Configuration deployments happen occasionally.
- You do not need configuration deployment to be triggered automatically by a pipeline.
- You want a simpler experience without PowerShell.

### Use the Product Deployment Toolkit when

The Product Deployment Toolkit remains the preferred option when:

- Configuration promotion is part of a **CI/CD process**.
- Configuration must be stored and versioned in Git.
- Pull requests or other approval gates are part of the release process.
- Test and Production deployments should be automated.
- You need repeatable scripted deployments.
- Your organization treats CluedIn configuration as code.

For an example of using the Product Deployment Toolkit with GitHub Actions, see [CI/CD for CluedIn configuration with GitHub Actions](/administration/configuration-cicd).

## Choose the approach that fits your release process

The UI and Product Deployment Toolkit can coexist.

For example, a smaller implementation team might use Configuration Import / Export to manually move approved changes between environments, while an enterprise DevOps team might use the Product Deployment Toolkit to promote configuration automatically through Development, Test, and Production.

The important distinction is the **deployment mechanism**, not the configuration-management goal:

- The **UI** provides an interactive way to export and import configuration.
- The **Product Deployment Toolkit** provides a scriptable way to automate the same type of environment promotion as part of CI/CD.
