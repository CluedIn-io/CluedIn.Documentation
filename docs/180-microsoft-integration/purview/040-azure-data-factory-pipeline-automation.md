---
layout: cluedin
nav_order: 4
parent: Microsoft Purview Integration
grand_parent: Microsoft Integration
permalink: /microsoft-integration/purview/data-factory-pipeline-automation
title: Data Factory Pipeline Automation
last_modified: 2025-10-09
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

## Overview
In this article, you will learn how to configure pipeline automation to sync data between Microsoft Purview (Unified Data Governance) and CluedIn using either **Azure Data Factory** or **Fabric Data Factory**.

CluedIn can automatically provision and execute pipelines for assets you tag in Purview with a designated glossary term. You can choose your orchestration engine:

- **Azure Data Factory (ADF)** — traditional Azure service.
- **Fabric Data Factory (FDF)** — Data Factory experience within Microsoft Fabric.

## Supported sources and formats

### Quick matrix

| Orchestrator | Azure Data Lake (ADLS) | Azure SQL Database / SQL Server | Snowflake | Fabric Files | Fabric Table |
|---|---|---|---|---|---|
| **Azure Data Factory** | **Supported** (all file formats) | **Supported** | **Supported** | **Supported** (all file formats **except Parquet**) | **Not supported** |
| **Fabric Data Factory** | **Supported** (all file formats) | — | — | **Supported** (all file formats **including Parquet**) | **Supported** |

> Notes
> - “Fabric Files” refers to files stored in Fabric OneLake item folders (Lakehouse, etc.).
> - If you need Parquet in Fabric Files or to automate Fabric Table ingestion, use **Fabric Data Factory**.

## Prerequisites
Before you begin, ensure you have:
- Access to Microsoft Purview and a glossary you can edit.
- A CluedIn tenant with administrator permissions.
- One of the following orchestration environments available to you:
  - An **Azure Data Factory** resource, or
  - A **Fabric** workspace with **Fabric Data Factory** enabled.

## Preparation
This section describes what you need to set up depending on your chosen orchestrator.

### Option A — Use **Azure Data Factory** (existing flow)
Follow these steps to prepare **ADF** and Purview, then configure CluedIn settings.

#### Step 1 — Create/verify Azure resources
1. **Create (or identify) an Azure Data Factory** resource in the correct subscription/resource group.

  ![adf-instance.png]({{ "/assets/images/microsoft-integration/purview/adf-instance.png" | relative_url }})

2. **(Optional)** Create an **Azure Key Vault** to hold secrets.

  ![akv-instance.png]({{ "/assets/images/microsoft-integration/purview/akv-instance.png" | relative_url }})

#### Step 2 — Service principal (shared)
Use the shared steps in **[Service principal (both ADF & Fabric)](#service-principal-both-adf--fabric)** to create the app registration and client secret. No ADF‑specific differences here.

> After creating the service principal, continue with role assignments below.

#### Step 3 — Assign roles and permissions
1. In **Azure Data Factory**, assign the service principal the **Contributor** role (or a least‑privilege custom role that allows pipeline authoring/execution).

    ![adf-assign-contributor-role.png]({{ "/assets/images/microsoft-integration/purview/adf-assign-contributor-role.png" | relative_url }})

1. If using **Key Vault**, grant **Secret Get/List** permissions.

    ![key-vault-create-access-policy-permissions.png]({{ "/assets/images/microsoft-integration/purview/key-vault-create-access-policy-permissions.png" | relative_url }})

1. Grant data‑plane access where needed:
   - **ADLS Gen2**: *Storage Blob Data Reader* (read) and/or *Storage Blob Data Contributor* (write) on the target containers.
   - **Azure SQL / SQL Server**: grant DB-level read and/or write as required.
   - **Snowflake**: map a Snowflake user/role and grant warehouse / DB / schema / table privileges.

#### Step 4 — Prepare Purview
Use the shared steps in **[Purview glossary term (both ADF & Fabric)](#purview-glossary-term-both-adf--fabric)** to create/apply the term. No ADF‑specific differences here.

#### Step 5 — Configure CluedIn (ADF settings)
1. In **CluedIn → Administration → Settings → Purview**:
   - Set **Azure Data Factory Base Url** (resource ID URL of your ADF, e.g., `/subscriptions/.../resourceGroups/.../providers/Microsoft.DataFactory/factories/<name>`).
   - Enter Data Factory **Client ID**, **Client Secret**, and **Tenant ID** (service principal from Step 2).
   - Set **Pipeline Automation Term Pattern** to the glossary term created in Purview (e.g., `CluedIn_Automate`).
   - Enable **Data Factory Pipeline Automation**.
   
    ![adf-cluedin-settings.png]({{ "/assets/images/microsoft-integration/purview/adf-cluedin-settings.png" | relative_url }})

#### Step 6 — Validate in ADF
1. Open **ADF Studio → Author** and confirm CluedIn created the **Pipeline(s)** and **Dataset(s)** for your tagged assets.

    ![adf-pipelines.png]({{ "/assets/images/microsoft-integration/purview/adf-pipelines.png" | relative_url }})

1. Open **Manage → Linked services** and verify connections (e.g., REST to CluedIn, ADLS/SQL/Snowflake as needed).

    ![adf-linked-services.png]({{ "/assets/images/microsoft-integration/purview/adf-linked-services.png" | relative_url }})

1. Open **Monitor → Pipeline runs** to confirm successful execution.

    ![adf-pipeline-runs.png]({{ "/assets/images/microsoft-integration/purview/adf-pipeline-runs.png" | relative_url }})


#### Step 7 — Verify ingestion in CluedIn
1. In the target **Data Source** within CluedIn, confirm a **Dataset** is present for each automated asset and rows are flowing.

    ![sync-data-products-adf-notification.png]({{ "/assets/images/microsoft-integration/purview/sync-data-products-adf-notification.png" | relative_url }})

---

### Option B — Use **Fabric Data Factory** (new)
CluedIn now supports pipeline automation via **Fabric Data Factory**. Use this when you need:
- Parquet files inside Fabric Files (OneLake) to be automated; or
- Fabric Table ingestion automation.

#### Step 1 — Workspace prerequisites
1. Ensure you have a **Fabric workspace** with capacity and permissions to create **Data Factory** items.

    ![fabric-workspace.png]({{ "/assets/images/microsoft-integration/purview/fabric-workspace.png" | relative_url }})

#### Step 2 — Register (or reuse) the service principal
1. Use the same app registration as ADF **or** create a separate one following the [Service principal](#service-principal-both-adf--fabric) section.
2. Ensure the identity has **Contributor** (or equivalent) on the Fabric workspace.

    ![fabric-workspace-access.png]({{ "/assets/images/microsoft-integration/purview/fabric-workspace-access.png" | relative_url }})

#### Step 3 — Prepare Purview
Use the shared steps in **[Purview glossary term (both ADF & Fabric)](#purview-glossary-term-both-adf--fabric)** to create/apply the term. No Fabric‑specific differences here.

#### Step 4 — Configure CluedIn (Fabric settings)
1. In **CluedIn → Administration → Settings → Purview** (or Fabric section):
   - **Fabric Data Factory Base Url**: `https://api.fabric.microsoft.com/<workspaceId>` (replace `<workspaceId>` with your Fabric **Workspace ID**).
   - Enter Data Factory **Tenant ID**, **Client ID**, **Client Secret** for the service principal.
   - Set the **Term Pattern** to your Purview term (e.g., `CluedIn_Automate`).
   - Enable **Data Factory Pipeline Automation**.

    ![adf-cluedin-settings.png]({{ "/assets/images/microsoft-integration/purview/adf-cluedin-settings.png" | relative_url }})

#### Step 5 — Validate in Fabric Data Factory
1. In your Fabric workspace, open **Data Factory** and verify pipelines were created for the tagged assets.

    ![fabric-pipelines.png]({{ "/assets/images/microsoft-integration/purview/fabric-pipelines.png" | relative_url }})

1. Run or monitor pipelines as needed and confirm successful execution.

    ![fabric-pipeline-runs.png]({{ "/assets/images/microsoft-integration/purview/fabric-pipeline-runs.png" | relative_url }})

#### Step 6 — Verify ingestion in CluedIn
1. As with ADF, confirm **Datasets** are present and data is flowing in the target **Data Source**.

> **Supported sources and formats (FDF)**
> - **Azure Data Lake** — all file formats.
> - **Fabric Files** — all file formats, **including Parquet**.
> - **Fabric Table** — supported.

CluedIn now supports pipeline automation via **Fabric Data Factory**. Use this when you need:
- Parquet files inside Fabric Files (OneLake) to be automated; or
- Fabric Table ingestion automation.

#### Supported sources and formats (FDF)
- **Azure Data Lake** — all file formats.
- **Fabric Files** — all file formats, **including Parquet**.
- **Fabric Table** — supported.

#### Preparation in Fabric (high-level)
> The detailed, click-by-click FDF setup can vary by tenant configuration. Use the guide below as a high‑level checklist and insert your screenshots where indicated.

1. **Workspace & capacities**
   - Ensure you have a Fabric workspace with permissions to create Data Factory items.

2. **Credentials & connections**
   - Create/verify connections to OneLake (Fabric Files) and ADLS. Ensure the identity used by FDF can read your sources and reach CluedIn’s ingestion endpoint.

3. **Purview term**
   - As with ADF, maintain a glossary **term** for the assets you want to automate.

4. **Configuration in CluedIn**
   - In **Administration > Settings > Purview** (or Fabric section if available in your tenant):
     - Enable **Data Factory Pipeline Automation**.
     - Provide the required client/application details (Tenant ID, App/Client ID, Secret) and the **Term Pattern** used to target assets.

> If your tenant uses a unified app registration for both ADF and Fabric, document which app is used for each in your environment for auditability.

## Purview glossary term (both ADF & Fabric)
Use a single glossary **term** in Microsoft Purview to mark assets for automation. CluedIn looks for this term to decide which assets to ingest.

### Create and apply the term
1. In the **Microsoft Purview portal**, open **Unified Catalog → Catalog management → Classic types** and create or select your glossary.

    ![sync-data-sources-create-glossary.png]({{ "/assets/images/microsoft-integration/purview/sync-data-sources-create-glossary.png" | relative_url }})

1. Create a **new term** (e.g., `CluedIn_Automate`).  

    ![adf-new-term.png]({{ "/assets/images/microsoft-integration/purview/adf-new-term.png" | relative_url }})

1. Apply the term to each asset you want CluedIn to ingest (e.g., ADLS path, Fabric file/folder, etc.).  

    ![adf-term-with-asset.png]({{ "/assets/images/microsoft-integration/purview/adf-term-with-asset.png" | relative_url }})

> You’ll reference this exact term string in CluedIn settings as the **Term Pattern**.

## Service principal (both ADF & Fabric)
Use a single **service principal** (app registration) for automation, or separate ones per platform if your organization prefers stricter isolation. This identity is used by CluedIn to authenticate with Azure resources and orchestrators.

### Create / configure the service principal
1. **App registration** (Microsoft Entra ID)
   - Register a new application (or choose an existing one dedicated to data movement).

    ![register-app-new-registration.png]({{ "/assets/images/microsoft-integration/purview/register-app-new-registration.png" | relative_url }})

1. **Client secret**
   - Create a client secret; copy the **Value** securely. You’ll store this in CluedIn (and optionally in Key Vault).

    ![register-app-new-client-secret.png]({{ "/assets/images/microsoft-integration/purview/register-app-new-client-secret.png" | relative_url }})

1. **Record identifiers**
   - **Tenant ID**, **Client (Application) ID**, and **Client Secret Value**.

### Required roles & permissions
> Assign the minimum access necessary. If your organization uses PIM, ensure the SP can activate roles when needed.

**For Azure Data Factory (ADF)**
- **Resource role**: *Contributor* on the **ADF** resource (or a custom role with `dataFactory/*` as appropriate).
- **Key Vault** (if used): *Get* and *List* on secrets.
- **Data sources** (as applicable):
  - ADLS Gen2: *Storage Blob Data Reader* (read) and/or *Storage Blob Data Contributor* (write) on the target containers.
  - Azure SQL / SQL Server (via MI/private link): grant database permissions per your policy (e.g., read on source, write on staging).
  - Snowflake: create/assign a Snowflake user/role mapped to this automation and grant warehouse/db/schema/table privileges as needed.

**For Fabric Data Factory (FDF)**
- **Fabric workspace**: *Contributor* (or role that allows creating & running Data Factory pipelines).
- **OneLake / Fabric items**:
  - Lakehouse / Files: grant permissions on the workspace/item folders.
  - **Fabric Table**: ensure the SP can read from/write to the Lakehouse and run pipelines that materialize/ingest tables.
- **External sources** (e.g., ADLS): grant the same storage roles as above when reading from or landing to ADLS.

### Configure in CluedIn
In **Administration → Settings → Purview**:
- Enter Data Factory **Tenant ID**, **Client ID**, **Client Secret** for the service principal.
- Enable the desired automation toggles and set the **Term Pattern** used in Purview.

    ![adf-cluedin-settings.png]({{ "/assets/images/microsoft-integration/purview/adf-cluedin-settings.png" | relative_url }})

### Security tips
- Store secrets in **Azure Key Vault** and reference them where supported.
- Use short‑lived client secrets or certificates with rotation policies.
- Limit the SP’s scope using resource‑level RBAC and data‑plane roles.

## Choosing the right orchestrator
Use this decision guide:

- Choose **Azure Data Factory** if you need to automate:
  - ADLS files (any format), Azure SQL Database/SQL Server, or Snowflake sources; and
  - You **do not** need Parquet in Fabric Files nor Fabric Table.

- Choose **Fabric Data Factory** if you need to automate:
  - ADLS files (any format), **Fabric Files including Parquet**, or **Fabric Table**.

## Troubleshooting & tips
- If no pipelines appear after tagging assets, confirm your **Term Pattern** in CluedIn exactly matches the Purview term.
- For permission errors, double‑check Key Vault policies (ADF) or Fabric connection credentials.
- When switching orchestrators, ensure only one automation path targets the same asset to avoid duplicates.
