---
layout: cluedin
title: Dun & Bradstreet
parent: REST API enricher samples
grand_parent: Govern & improve
nav_order: 30
permalink: /govern/rest-api-enricher-samples/dun-and-bradstreet
content_type: reference
summary: "Looks up a company by DUNS number in Dun & Bradstreet's Direct+ API. V2 script; needs a D&B API key and secret."
---

This script looks up a company by its DUNS number in the Dun & Bradstreet Direct+ API. It adds the company's primary name, operating status, corporate linkage (parent, headquarters, domestic ultimate and global ultimate DUNS numbers), industry codes, and other company details. It gets an access token with your D&B key and secret, and caches the token.

**Enricher version:** V2  
**API key:** your D&B Direct+ key and secret, entered in the script in place of `{key}` and `{secret}`

CluedIn also has a built-in [Dun and Bradstreet enricher](/govern/enrichment/dnb).

To set up the enricher, see [Add REST API enricher](/govern/enrichment/rest-api#add-rest-api-enricher), then use the settings and script on this page.

## Vocabulary key and properties

```
companies.dunsnumber
```

## Process script

```javascript
// REST API Enricher V2 - DnB Search by DUNS - Process Response Script

function populateIndustryCodes(results, parsedContent) {
  const selectedTypes = ["19295", "37788"];

  const industryCodeValues =
    parsedContent?.organization?.industryCodes?.filter(
      (x) => x?.typeDnBCode > 0 && selectedTypes.includes(String(x.typeDnBCode))
    ) ?? [];

  if (industryCodeValues.length === 0) return;

  let industryCodesIndex = 0;
  for (const industryCode of industryCodeValues) {
    results[`Industry_${industryCodesIndex}_Description`] =
      industryCode.description;
    results[`Industry_${industryCodesIndex}_TypeDescription`] =
      industryCode.typeDescription;
    results[`Industry_${industryCodesIndex}_TypeDnBCode`] =
      industryCode.typeDnBCode;
    results[`Industry_${industryCodesIndex}_Priority`] = industryCode.priority;
    results[`Industry_${industryCodesIndex}_Code`] = industryCode.code;

    industryCodesIndex++;
  }
}

function populateOrganizationInfo(results, parsedContent) {
  const org = parsedContent?.organization;

  // DUNS Control Status
  if (org?.dunsControlStatus) {
    const status = org.dunsControlStatus;

    results.DunsControlStatusFullReportDate = status.fullReportDate;
    results.DunsControlStatusLastUpdateDate = status.lastUpdateDate;
    results.DunsControlStatusOperatingStatusDescription =
      status.operatingStatus?.description;
    results.DunsControlStatusOperatingStatusDnbCode =
      status.operatingStatus?.dnbCode;
    results.DunsControlStatusIsMarketable = status.isMarketable;
    results.DunsControlStatusIsMailUndeliverable = status.isMailUndeliverable;
    results.DunsControlStatusIsTelephoneDisconnected =
      status.isTelephoneDisconnected;
    results.DunsControlStatusIsDelisted = status.isDelisted;

    if (status?.operatingStatus) {
      results.OperatingStatusCode = status.operatingStatus?.dnbCode;
      results.OperatingStatusDescription = status.operatingStatus?.description;
    }
  }

  // DUNS Numbers
  results.Duns = org?.duns;
  results.DomesticUltimateDuns = org?.corporateLinkage?.domesticUltimate?.duns;
  results.GlobalUltimateDuns = org?.corporateLinkage?.globalUltimate?.duns;
  results.ParentDuns = org?.corporateLinkage?.parent?.duns;
  results.HeadQuarterDuns = org?.corporateLinkage?.headQuarter?.duns;

  // Business Information
  results.PrimaryBusinessName = org?.primaryName;
  results.BusinessEntityTypeDnbCode = org?.businessEntityType?.dnbCode;
  results.BusinessEntityTypeDescription = org?.businessEntityType?.description;

  // Trade Style Names
  const tradeStyleNames =
    org?.tradeStyleNames
      ?.map((t) => t?.name)
      ?.filter((n) => n && n.length > 0) ?? [];

  if (tradeStyleNames.length > 0) {
    results.TradeStyleNames = tradeStyleNames.join(" | ");
  }

  // Website
  const website = org?.websiteAddress?.[0];
  if (website) {
    results.WebsiteUrl = website.url;
  }

  // Telephone
  const telephone = org?.telephone?.[0];
  if (telephone?.isdCode && telephone?.telephoneNumber) {
    results.Telephone = `+${telephone.isdCode} ${telephone.telephoneNumber}`;
  }

  // Fax
  const fax = org?.fax?.[0];
  if (fax?.isdCode && fax?.faxNumber) {
    results.Fax = `+${fax.isdCode} ${fax.faxNumber}`;
  }

  // Stock Exchange
  const primaryStockExchange = org?.stockExchanges?.find(
    (x) => x?.isPrimary === true
  );

  if (primaryStockExchange) {
    results.StockExchangeTickerName = primaryStockExchange.tickerName;
    results.StockExchangeName = primaryStockExchange.exchangeName?.description;
    results.StockExchangeCountryCode =
      primaryStockExchange.exchangeCountry?.isoAlpha2Code;
  }

  // Registration Numbers
  const selectedRegistrationNumberTypes = ["2541"];

  if (selectedRegistrationNumberTypes.length > 0) {
    const registrationNumbers =
      org?.registrationNumbers?.filter(
        (x) =>
          x?.typeDnBCode > 0 &&
          selectedRegistrationNumberTypes.includes(String(x.typeDnBCode))
      ) ?? [];

    let index = 0;
    for (const reg of registrationNumbers) {
      results[`RegistrationNumbers_${index}_RegistrationNumber`] =
        reg.registrationNumber;
      results[`RegistrationNumbers_${index}_TypeDescription`] =
        reg.typeDescription;
      results[`RegistrationNumbers_${index}_TypeDnBCode`] = reg.typeDnBCode;
      results[
        `RegistrationNumbers_${index}_RegistrationNumberClassDescription`
      ] = reg.registrationNumberClass?.description;
      results[`RegistrationNumbers_${index}_RegistrationNumberClassDnbCode`] =
        reg.registrationNumberClass?.dnbCode;

      index++;
    }
  }

  // Corporate Linkage - Family Tree Roles Played
  let familyIndex = 0;
  for (const role of org?.corporateLinkage?.familytreeRolesPlayed ?? []) {
    results[
      `CorporateLinkageFamilyTreeRolesPlayedVocabulary_${familyIndex}_Description`
    ] = role.description;
    results[
      `CorporateLinkageFamilyTreeRolesPlayedVocabulary_${familyIndex}_DnbCode`
    ] = role.dnbCode;
    familyIndex++;
  }

  results.HierarchyLevel = org?.corporateLinkage?.hierarchyLevel;
  results.GlobalUltimateFamilyTreeMembersCount =
    org?.corporateLinkage?.globalUltimateFamilyTreeMembersCount;

  // Number of Employees
  results.NumberOfEmployees = org?.numberOfEmployees?.[0]?.value;
  results.GlobalUltimateNumberOfEmployees =
    org?.corporateLinkage?.globalUltimate?.numberOfEmployees?.[0]?.value;
  results.DomesticUltimateNumberOfEmployees =
    org?.corporateLinkage?.domesticUltimate?.numberOfEmployees?.[0]?.value;

  // Yearly Revenue
  const orgFinancial = org?.financials?.[0];
  const orgRevenue = orgFinancial?.yearlyRevenue?.[0];

  results.YearlyRevenue =
    orgRevenue && orgRevenue.currency
      ? `${orgRevenue.value} ${orgRevenue.currency}`
      : null;

  const globalUltimateFinancial = org?.globalUltimate?.financials?.[0];
  const globalUltimateRevenue = globalUltimateFinancial?.yearlyRevenue?.[0];

  results.GlobalUltimateYearlyRevenue =
    globalUltimateRevenue && globalUltimateRevenue.currency
      ? `${globalUltimateRevenue.value} ${globalUltimateRevenue.currency}`
      : null;

  const domesticUltimateFinancial = org?.domesticUltimate?.financials?.[0];
  const domesticUltimateRevenue = domesticUltimateFinancial?.yearlyRevenue?.[0];

  results.DomesticUltimateYearlyRevenue =
    domesticUltimateRevenue && domesticUltimateRevenue.currency
      ? `${domesticUltimateRevenue.value} ${domesticUltimateRevenue.currency}`
      : null;
}

function populatePrimaryAddresses(results, parsedContent) {
  const org = parsedContent?.organization;

  const domesticUltimateDuns = org?.corporateLinkage?.domesticUltimate?.duns;
  const globalUltimateDuns = org?.corporateLinkage?.globalUltimate?.duns;
  const parentDuns = org?.corporateLinkage?.parent?.duns;
  const headQuarterDuns = org?.corporateLinkage?.headQuarter?.duns;
  const duns = org?.duns;

  // Domestic Ultimate
  if (
    org?.corporateLinkage?.domesticUltimate?.primaryAddress &&
    domesticUltimateDuns &&
    domesticUltimateDuns !== duns
  ) {
    const addr = org.corporateLinkage.domesticUltimate.primaryAddress;

    results.DomesticUltimatePrimaryAddressCountry = addr.addressCountry?.name;
    results.DomesticUltimateISO2CountryCode =
      addr.addressCountry?.isoAlpha2Code;
    results.DomesticUltimatePrimaryAddressCountyName = addr.addressCounty?.name;
    results.DomesticUltimatePrimaryAddressLocality = addr.addressLocality?.name;
    results.DomesticUltimatePrimaryAddressPostalCode = addr.postalCode;
    results.DomesticUltimatePrimaryAddressRegionName = addr.addressRegion?.name;
    results.DomesticUltimatePrimaryAddressRegionAbbreviatedName =
      addr.addressRegion?.abbreviatedName;
    results.DomesticUltimatePrimaryAddressStreetLine1 =
      addr.streetAddress?.line1;
    results.DomesticUltimatePrimaryAddressStreetLine2 =
      addr.streetAddress?.line2;
  }

  // Global Ultimate
  if (
    org?.corporateLinkage?.globalUltimate?.primaryAddress &&
    globalUltimateDuns &&
    globalUltimateDuns !== duns
  ) {
    const addr = org.corporateLinkage.globalUltimate.primaryAddress;

    results.GlobalUltimatePrimaryAddressCountry = addr.addressCountry?.name;
    results.GlobalUltimateISO2CountryCode = addr.addressCountry?.isoAlpha2Code;
    results.GlobalUltimatePrimaryAddressCountyName = addr.addressCounty?.name;
    results.GlobalUltimatePrimaryAddressLocality = addr.addressLocality?.name;
    results.GlobalUltimatePrimaryAddressPostalCode = addr.postalCode;
    results.GlobalUltimatePrimaryAddressRegionName = addr.addressRegion?.name;
    results.GlobalUltimatePrimaryAddressRegionAbbreviatedName =
      addr.addressRegion?.abbreviatedName;
    results.GlobalUltimatePrimaryAddressStreetLine1 = addr.streetAddress?.line1;
    results.GlobalUltimatePrimaryAddressStreetLine2 = addr.streetAddress?.line2;
  }

  // Parent
  if (
    org?.corporateLinkage?.parent?.primaryAddress &&
    parentDuns &&
    parentDuns !== duns
  ) {
    const addr = org.corporateLinkage.parent.primaryAddress;

    results.ParentPrimaryAddressCountry = addr.addressCountry?.name;
    results.ParentISO2CountryCode = addr.addressCountry?.isoAlpha2Code;
    results.ParentPrimaryAddressCountyName = addr.addressCounty?.name;
    results.ParentPrimaryAddressLocality = addr.addressLocality?.name;
    results.ParentPrimaryAddressPostalCode = addr.postalCode;
    results.ParentPrimaryAddressRegionName = addr.addressRegion?.name;
    results.ParentPrimaryAddressRegionAbbreviatedName =
      addr.addressRegion?.abbreviatedName;
    results.ParentPrimaryAddressStreetLine1 = addr.streetAddress?.line1;
    results.ParentPrimaryAddressStreetLine2 = addr.streetAddress?.line2;
  }

  // HeadQuarter
  if (
    org?.corporateLinkage?.headQuarter?.primaryAddress &&
    headQuarterDuns &&
    headQuarterDuns !== duns
  ) {
    const addr = org.corporateLinkage.headQuarter.primaryAddress;

    results.HeadQuarterPrimaryAddressCountry = addr.addressCountry?.name;
    results.HeadQuarterISO2CountryCode = addr.addressCountry?.isoAlpha2Code;
    results.HeadQuarterPrimaryAddressCountyName = addr.addressCounty?.name;
    results.HeadQuarterPrimaryAddressLocality = addr.addressLocality?.name;
    results.HeadQuarterPrimaryAddressPostalCode = addr.postalCode;
    results.HeadQuarterPrimaryAddressRegionName = addr.addressRegion?.name;
    results.HeadQuarterPrimaryAddressRegionAbbreviatedName =
      addr.addressRegion?.abbreviatedName;
    results.HeadQuarterPrimaryAddressStreetLine1 = addr.streetAddress?.line1;
    results.HeadQuarterPrimaryAddressStreetLine2 = addr.streetAddress?.line2;
  }

  // Self
  if (!org?.primaryAddress) return;

  const primary = org.primaryAddress;

  results.PrimaryAddressCountry = primary.addressCountry?.name;
  results.ISO2CountryCode = primary.addressCountry?.isoAlpha2Code;
  results.PrimaryAddressCountyName = primary.addressCounty?.name;
  results.PrimaryAddressLocality = primary.addressLocality?.name;
  results.PrimaryAddressPostalCode = primary.postalCode;
  results.PrimaryAddressRegionName = primary.addressRegion?.name;
  results.PrimaryAddressRegionAbbreviatedName =
    primary.addressRegion?.abbreviatedName;
  results.PrimaryAddressStreetLine1 = primary.streetAddress?.line1;
  results.PrimaryAddressStreetLine2 = primary.streetAddress?.line2;
}

function searchByDuns(token) {
  // Get DUNS Number from vocabularies passed in Vocabulary and Properties control, please change the key as needed
  const dunsNumber = vocabularies.find(
    (x) => x.Key === "companies.dunsnumber"
  )?.Value;
  const dnbResponse = http.send({
    url: `https://plus.dnb.com/v1/data/duns/${dunsNumber}?blockIDs=companyfinancials_L1_v3,hierarchyconnections_L1_v1,companyinfo_L3_v1,companyinfo_identifiers_v1,esginsight_L3_v1`,
    method: "GET",
    headers: [{ Key: "Authorization", Value: `Bearer ${token}` }],
  });

  let parsedContent = JSON.parse(dnbResponse.Content);
  let results = {};

  const confidenceScore =
    parsedContent?.matchCandidates?.[0]?.matchQualityInformation
      ?.confidenceCode;
  populatePrimaryAddresses(results, parsedContent);
  populateOrganizationInfo(results, parsedContent);
  populateIndustryCodes(results, parsedContent);

  return JSON.stringify([
    { Data: results, Score: confidenceScore ? confidenceScore * 10 : 100 },
  ]);
}

try {
  const authCacheKey = "dnb_auth_token";
  const cachedAuthToken = cache.Get(authCacheKey);

  const key = "{key}";
  const secret = "{secret}";

  const credentials = `${key}:${secret}`;

  const base64 = stringEncoder.toBase64(credentials);

  const token = cache.GetOrSetFactory(
    "dnb_auth_token",
    () => {
      const tokenResponse = http.Send({
        url: `https://plus.dnb.com/v2/token`,
        method: "POST",
        headers: [
          { Key: "Content-Type", Value: "application/json" },
          { Key: "Authorization", Value: `Basic ${base64}` },
        ],
        body: { grant_type: "client_credentials" },
      });

      return JSON.parse(tokenResponse.Content).access_token;
    },
    3000000
  );

  log(JSON.stringify(token));

  response = searchByDuns(token);
} catch (error) {
  const errorDetails = {
    name: error?.name,
    message: error?.message,
    stack: error?.stack,
  };
  log("Authentication failed :" + JSON.stringify(errorDetails));
}
```
