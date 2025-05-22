---
layout: cluedin
nav_order: 6
parent: Data catalog
grand_parent: Management
permalink: /management/data-catalog/data-types
title: Data types
---

In this article, you will find reference information about data types that can be used in vocabulary keys. Specifying the data type correctly facilitates the use of filter operations for more precise filter results.

Each data type is associated with a specific storage type that defines how the data is stored:

- **Keyword** – represents the storage of data in text format. Storing data as a keyword doesn't allow you to query properties using numeric and date operators such as _Between_, _Equals_, _Greater or Equal_.

- **Typed** – represents the storage of data in its native form. The **Typed** storage is selected by default for data types that can be typable. The **Typed** storage allows you to query properties using numeric and date operators such as _Between_, _Equals_, _Greater or Equal_.

- **Untyped** – represents the storage of typable data in text format. If you don't want to query properties using numeric and date operators, then you can change the storage from **Typed** to **Untyped**.

The following table provides the description of data types along with the type of storage that applies to each data type.

| Data type | Description | Storage |
|--|--|--|
| Text | A Unicode text string. | Keyword |
| DateTime | A date with a time, in the time zone of your computer. If no time zone is specified, then UTC is assumed when we try to normalize* the date. | Typed |
| Time | A time without a date, in the time zone of your computer | Typed |
| Duration | A span of time. It is used to store and manipulate time intervals, which could be measured in seconds, minutes, hours, days, or other units of time. | Typed |
| Boolean | A _true_ or _false_ value. Data will only be strong-typed if it is stored as the values "true" or "false". For all other values such as "yes", "no", "1", "0" and so on, the data must be normalized using a [rule](/management/rules) or a clean [project](/preparation/clean). | Typed |
| Integer | A whole number without any fractional or decimal part. | Typed |
| Number | Any numeric value, including integers and numbers with decimal parts. | Typed |
| Uri | A Universal Resource Identifier (URI) text string to an image. | Keyword |
| Guid | A Globally Unique Identifier. | Keyword |
| Email | An email address. | Keyword |
| PhoneNumber | A phone number. | Keyword |
| TimeZone | A geographical region's standard time offset from UTC or a specific named time zone, such as those defined by the [IANA Time Zone Database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). | Keyword |
| GeographyCity | A name of a city. | Keyword |
| GeographyState | A name of a state, county, or province. | Keyword |
| GeographyCountry | A name of a country in ISO code. | Keyword |
| GeographyCoordinates | A coordinate represented as a latitude and longitude, or other coordinate system. Can also be used for individual latitude or longitude properties. | Keyword |
| GeographyLocation | A generic location such as "Street 1, Apt 2-B”.  | Keyword |
| Json | An object or object graph represent in JSON format. | Keyword |
| Xml | An object or object graph represent in XML format. | Keyword |
| Html | A page or snippet of HTML. | Keyword |
| IPAddress | An IP Address in either v4 or v6 format. | Keyword |
| Color | A color specification. | Keyword |
| Money | A monetary value. | Typed |
| Currency | Represents currency values. | Keyword |
| PersonName | A name of a person. | Keyword |
| OrganizationName | A name of an organization. | Keyword |
| Identifier | An identifier representing the key of a record, normally as a GUID or Integer. | Keyword |
| [Lookup](/management/data-catalog/lookup-data-type) | A custom list of possible values, which is defined with a glossary. | Keyword |

_*Date normalization occurs when the **Date Time** option is enabled in **Administration** > **Settings** > **Processing Property Data Type Normalization**. In this case, CluedIn analyzes the incoming date format and converts it to ISO 8601 format (YYYY-MM-DDT00:00:00+00:00). If you want to instruct CluedIn how to interpret dates before converting them to ISO 8601 format, [create](/management/rules/create-rule) a rule with the **Normalize Date** [action](/management/rules/rules-reference)._
