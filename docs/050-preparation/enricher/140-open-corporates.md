---
layout: cluedin
nav_order: 14
parent: Enricher
grand_parent: Preparation
permalink: preparation/enricher/open-corporates
title: OpenCorporates
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

This article outlines how to configure the [OpenCorporates](https://opencorporates.com/) enricher. The purpose of this enricher is to provide a wide range of information about companies from around the world (for example, creation date, status, officers, and so on). More details can be found in [Properties from OpenCorporates enricher](#properties-from-opencorporates-enricher).

The Open Corporates enricher supports the following endpoints:

- `https://api.opencorporates.com/v0.4/companies/search?q={nameLookup}`, where `{nameLookup}` is the name of company – this endpoint is called when no company codes can be found in golden record's organization.codes.cvr, organization.codes.brreg, organization.codes.companyHouse, or organization.codes.cik

- `https://api.opencorporates.com/v0.4companies/{jurisdictionCodeLookup.Jurisdiction}/{jurisdictionCodeLookup.Value}?format=json` – this endpoint is called when there are company codes, so the jurisdiction of golden record will be retrieved and used in the API.

## Add OpenCorporates enricher

To use the OpenCorporates enricher, you must provide the API token. To get the API token, follow the instructions on the [OpenCorporates website](https://opencorporates.com/plug-in-our-data/). The OpenCorportes enricher uses the company name to retrieve information from the OpenCorporates website.

**To add the OpenCorporates enricher**

1. On the navigation pane, go to **Preparation** > **Enrich**. Then, select **Add Enricher**.

1. On the **Choose Enricher** tab, select **OpenCorporates**, and then select **Next**.

    ![open-corporates-enricher-1.png]({{ "/assets/images/preparation/enricher/open-corporates-enricher-1.png" | relative_url }})

1. On the **Configure** tab, provide the following details:

    - **API Key** – enter the API token for retrieving information from the OpenCorporates website.

    - **Accepted Business Domain** – enter the business domain to define which golden records will be enriched.

    - **Lookup Vocabulary Key** – enter the vocabulary key that contains the names of companies that you want to enrich.

        ![open-corporates-enricher-2.png]({{ "/assets/images/preparation/enricher/open-corporates-enricher-2.png" | relative_url }})

1. Select **Test Connection** to make sure the enricher is properly configured, and then select **Add**.

    The OpenCorporates enricher is added and has an active status. This means that it will enrich golden records based on the configuration details during processing or when you trigger external enrichment.

After the OpenCorporates enricher is added, you can modify its details:

- **Settings** – add a user-friendly display name, select the description for data coming from the enricher, and define the source quality for determining the winning values.

- **Authentication** – modify the details you provided to configure the enricher.

## Properties from OpenCorporates enricher

You can find the properties added to golden records from the OpenCorporates enricher on the **Properties** page.

![open-corporates-enricher-4.png]({{ "/assets/images/preparation/enricher/open-corporates-enricher-4.png" | relative_url }})

For a more detailed information about the changes made to a golden record by the OpenCorporates enricher, check the corresponding data part on the **History** page.

![open-corporates-enricher-5.png]({{ "/assets/images/preparation/enricher/open-corporates-enricher-5.png" | relative_url }})

The following table lists the properties that can be added to golden records by the OpenCorporates enricher.

| Display name | Vocabulary key |
|--|--|
| Agent Name | openCorporates.organization.agentName |
| Agent Address | openCorporates.organization.agentAddress |
| Alternative Names | openCorporates.organization.alternativeNames |
| Branch | openCorporates.organization.branch |
| Branch Status | openCorporates.organization.branchStatus |
| Company Number | openCorporates.organization.companyNumber, mapped to organization.codes.companyNumber |
| Company Type | openCorporates.organization.companyType, mapped to organization.type |
| Controlling Entity | openCorporates.organization.controllingEntity |
| Corporate Groupings | openCorporates.organization.corporateGroupings |
| Created At | openCorporates.organization.createdAt, mapped to date.createdDate |
| Current Status | openCorporates.organization.currentStatus |
| Data | openCorporates.organization.data |
| Dissolution Date | openCorporates.organization.dissolutionDate, mapped to organization.dissolutionDate |
| Filings | openCorporates.organization.filings |
| Incorporation Date | openCorporates.organization.incorporationDate, mapped to organization.foundingDate |
| Identifiers | openCorporates.organization.identifiers |
| Industry Codes | openCorporates.organization.industryCodes |
| Native Company Number | openCorporates.organization.nativeCompanyNumber |
| Registry Url | openCorporates.organization.registryUrl |
| Jurisdiction Code | openCorporates.organization.jurisdictionCode, mapped to organization.jurisdictionCode |
| Address Country Code | openCorporates.organization.addressCountryCode, mapped to organization.address.countryCode |
| In Active | openCorporates.organization.inActive |
| Home Company | openCorporates.organization.homeCompany |
| Open Corporates Url | openCorporates.organization.openCorporatesUrl |
| Officers Name | openCorporates.organization.officersName |
| Officers | openCorporates.organization.officers |
| Number Of Employees | openCorporates.organization.numberOfEmployees, mapped to organization.employeeCount |
| Source Publisher | openCorporates.organization.sourcePublisher |
| Source Url | openCorporates.organization.sourceUrl |
| Previous Names | openCorporates.organization.previousNames |
| Registered Address | openCorporates.organization.registeredAddress, mapped to organization.address |
| Updated At | openCorporates.organization.updatedAt, mapped to date.modifiedDate |
| Trademark Registration | openCorporates.organization.trademarkRegistration |
| Website | openCorporates.organization.website, mapped to organization.website |
| Telephone Number | openCorporates.organization.telephoneNumber, mapped to organization.phoneNumber |
| Official Register Entry | openCorporates.organization.officialRegisterEntry |
| Date | openCorporates.filing.date, mapped to date.createdDate |
| Filing Code | openCorporates.filing.filingCode |
| Filing Type | openCorporates.filing.filingType |
| Open Corporates Url | openCorporates.filing.openCorporatesUrl |
| Score | openCorporates.filing.score |
| Uid | openCorporates.filing.uid |