---
layout: cluedin
nav_order: 11
parent: Enricher
grand_parent: Preparation
permalink: /preparation/enricher/google-maps
title: Google Maps
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

This article outlines how to configure the Google Maps enricher. The purpose of this enricher is to provide address-related information. More details can be found in [Properties from Google Maps enricher](#properties-from-google-maps-enricher).

The Google Maps enricher supports the following endpoints:

- `https://maps.googleapis.com/maps/api/place/textsearch/json?query={organizationName}{organizationAddress}{organizationCity}{organizationZip}{organizationState}{organizationCountry}` – if organization name, address, city, zip, state, and country are provided.

- `https://maps.googleapis.com/maps/api/place/textsearch/json?query={organizationName}` – if organization name is provided.

- `https://maps.googleapis.com/maps/api/place/textsearch/json?query={organizationAddress}` – if organization address is provided.

- `https://maps.googleapis.com/maps/api/place/textsearch/json?query={location}` – if one of the addresses other than organization address is provided.

- `https://maps.googleapis.com/maps/api/place/textsearch/json?query={location}&location={latitude}{longitude}` – if one of the addresses other than organization address and latitude and longitude are provided.

- `https://maps.googleapis.com/maps/api/place/textsearch/json?query=location={latitude}{longitude}` – if latitude and longitude are provided.

- `https://maps.googleapis.com/maps/api/place/details/json?placeid={id}` – the ID is taken from the previous text search API (the result of `https://maps.googleapis.com/maps/api/place/textsearch/json`).

## Add Google Maps enricher

To use the Google Maps enricher, you must provide the API key. To get the API key, follow the instructions [here](https://cloud.google.com/docs/authentication/api-keys#create).

To enrich golden records using the Google Maps enricher, ensure they have a specific property (for example, Enrich) set to _True_. Golden records without this property or with a value other than _True_ will be skipped during enrichment.

The Google Maps enricher can use a variety of attributes for searching the Google Maps Platform:

- For Organization:

    - A combination of **Organization Name**, **Address**, **Zip**, **State**, **City**, **Country**

    - A combination of **Organization Name** and **Address**.

    - **Organization Name**

    - **Organization Address**

- For Location: **Location Address**

- For Person:

    - **Person Address** and **Person Address City**

    - **Person Address**

- For User: **User Address**

When you're configuring the Google Maps enricher for a specific business domain, make sure you fill in the relevant fields for that business domain.

**To add the Google Maps enricher**

1. On the navigation pane, go to **Preparation** > **Enrich**. Then, select **Add Enricher**.

1. On the **Choose Enricher** tab, select **Google Maps**, and then select **Next**.

    ![google-maps-enricher-1.png](../../assets/images/preparation/enricher/google-maps-enricher-1.png)

1. On the **Configure** tab, provide the following details:

    - **API Key** – enter the API key for retrieving information from the Google Maps Platform.

    - **Accepted Business Domain** – enter the business domain to define which golden records will be enriched.

    - **Vocabulary Key used to control whether it should be enriched** – enter the vocabulary key that indicates if the golden record should be enriched. If the value is true, then the golden record will be enriched. Otherwise, the golden record will not be enriched.

    - **Organization Name Vocab Key** – enter the vocabulary key that contains company names that will be used for searching the Google Maps Platform.

    - **Organization Address Vocab Key** – enter the vocabulary key that contains company addresses that will be used for searching the Google Maps Platform.

    - **Organization City Vocab Key** – enter the vocabulary key that contains cities that will be used for searching the Google Maps Platform.

    - **Organization Zip** – enter the vocabulary key that contains company ZIP Codes that will be used for searching the Google Maps Platform.

    - **Organization State Vocab Key** – enter the vocabulary key that contains states that will be used for searching the Google Maps Platform.

    - **Organization Country Vocab Key** – enter the vocabulary key that contains countries that will be used for searching the Google Maps Platform.

    - **Location Address Vocab Key** – enter the vocabulary key that contains location addresses that will be used for searching the Google Maps Platform.

    - **User Address Vocab Key** – enter the vocabulary key that contains user addresses that will be used for searching the Google Maps Platform.

    - **Person Address Vocab Key** – enter the vocabulary key that contains person addresses that will be used for searching the Google Maps Platform.

    - **Person Address City Vocab Key** – enter the vocabulary key that contains person cities that will be used for searching the Google Maps Platform.

    - **Latitude Vocab Key** – this field is not currently used for searching the Google Maps Platform.

    - **Longitude Vocab Key** – this field is not currently used for searching the Google Maps Platform.

        ![google-maps-enricher-2.png](../../assets/images/preparation/enricher/google-maps-enricher-2.png)

1. Select **Add**.

    The Google Maps enricher is added and has an active status. This means that it will enrich golden records based on the configuration details during processing or when you trigger external enrichment.

After the Google Maps enricher is added, you can modify its details:

- **Settings** – add a user-friendly display name, select the description for data coming from the enricher, and define the source quality for determining the winning values.

    ![google-maps-enricher-3.png](../../assets/images/preparation/enricher/google-maps-enricher-3.png)

- **Authentication** – modify the details you provided while configuring the enricher.

## Properties from Google Maps enricher

You can find the properties added to golden records from the Google Maps enricher on the **Properties** page.

![google-maps-enricher-4.png](../../assets/images/preparation/enricher/google-maps-enricher-4.png)

For a more detailed information about the changes made to a golden record by the Google Maps enricher, check the corresponding data part on the **History** page.

![google-maps-enricher-5.png](../../assets/images/preparation/enricher/google-maps-enricher-5.png)

The following table lists the properties that can be added to golden records by the Google Maps enricher.

| Display name | Vocabulary key |
|--|--|
| Address Components | googleMaps.Organization.AddressComponents |
| Administrative Area Level 1 | googleMaps.Organization.AdministrativeAreaLevel1 |
| Administrative Area Level 2 | googleMaps.Organization.AdministrativeAreaLevel2 |
| Adr Address | googleMaps.Organization.AdrAddress |
| Business Status | googleMaps.Organization.BusinessStatus |
| City Name | googleMaps.Organization.CityName |
| Country Code | googleMaps.Organization.CountryCode |
| Formatted Address | googleMaps.Organization.FormattedAddress |
| Formatted PhoneNumber | googleMaps.Organization.FormattedPhoneNumber |
| Icon | googleMaps.Organization.Icon |
| Id | googleMaps.Organization.Id |
| International Phone Number | googleMaps.Organization.InternationalPhoneNumber |
| Latitude | googleMaps.Organization.Latitude |
| Longitude | googleMaps.Organization.Longitude |
| Name | googleMaps.Organization.Name |
| Neighborhood | googleMaps.Organization.Neighborhood |
| Opening Hours | googleMaps.Organization.OpeningHours |
| Place Id | googleMaps.Organization.PlaceId |
| Plus Code | googleMaps.Organization.PlusCode |
| Postal Code | googleMaps.Organization.PostalCode |
| Rating | googleMaps.Organization.Rating |
| Reference | googleMaps.Organization.Reference |
| Reviews | googleMaps.Organization.Reviews |
| Scope | googleMaps.Organization.Scope |
| Street Number | googleMaps.Organization.StreetNumber |
| Sub Premise | googleMaps.Organization.SubPremise |
| Types | googleMaps.Organization.Types |
| Url | googleMaps.Organization.Url |
| User Ratings Total | googleMaps.Organization.UserRatingsTotal |
| Utc Offset | googleMaps.Organization.UtcOffset |
| Vicinity | googleMaps.Organization.Vicinity |
| Website | googleMaps.Organization.Website |
| AdministrativeArea | googleMaps.Location.AdministrativeArea |
| Code Country | googleMaps.Location.CodeCountry |
| Code Postal | googleMaps.Location.CodePostal |
| Components Address | googleMaps.Location.componentsAddress |
| Formatted Address | googleMaps.Location.formattedAddress |
| Geometry | googleMaps.Location.Geometry |
| Latitude | googleMaps.Location.Latitude |
| Longitude | googleMaps.Location.Longitude |
| Name | googleMaps.Location.Name |
| Name City | googleMaps.Location.NameCity |
| Name Street | googleMaps.Location.NameStreet |
| Number Street | googleMaps.Location.NumberStreet |