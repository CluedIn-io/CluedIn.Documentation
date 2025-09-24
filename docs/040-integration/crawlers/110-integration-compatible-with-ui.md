---
layout: cluedin
title: Integration and CluedIn UI
parent: Crawlers
grand_parent: Ingestion
nav_order: 110
has_children: false
permalink: /integration/integration-compatible-with-ui
tags: ["integration","ui"]
---
## On this page
{: .no_toc .text-delta }
1. TOC
{:toc}

To allow users to add and manage an integration from the interface, you must include specific information in your provider. If this information is missing, the provider will still work, but the user experience will be negatively affected.

## IExtendedProviderMetadata interface

To provide information to CluedIn.UI, implement the `IExtendedProviderMetadata` interface. The sections below explain the purpose of each property in this interface.

Example:

- [HelloWorldProvider.cs](https://github.com/CluedIn-io/CluedIn.Crawling.HelloWorld/blob/master/src/HelloWorld.Provider/HelloWorldProvider.cs)


Code:

```csharp
    public interface IExtendedProviderMetadata
    {
        string Icon { get; }            // see notes below

        string Domain { get; }          // The Url to your application

        string About { get; }           // A sentence describing the purpose of your application

        string AuthMethods { get; }     // A serialised JSON array of Authentication Methods supports (TODO Obtain list of )

        string Properties { get; }      // TODO find out how this is used by UI

        string ServiceType { get; }     // IE CRMType etc (TODO get full list)

        string Aliases { get; }         // TODO find out how used in the UI

        Guide Guide { get; set; }       // Instructions on how to configure your Provider in the UI

        string Details { get; set; }    // Details of how this provider will interact with your application

        string Category { get; set; }   // The category your provider fall under to allow filtering in the UI

        string Type { get; set; }       // Available options [cloud, on-premise]
    }
```

## Icon

The icon is used by CluedIn.UI to quickly show to all users what the provider is. The ideal image size is 128x128px.

To make your icon discoverable:

1. Add it as an Embedded Resource via the Build Action property in your Provider project. For details, see [Build Actions](https://docs.microsoft.com/en-us/visualstudio/ide/build-actions?view=vs-2019).

1. Our convention is to place the image file under a `Resources` folder.

1. Reference the icon in the `Icon` property using `.` notation (dot), not `\`.

Example folder structure:

```
- Provider.HellowWorld.csproj
    \Resources
        \cluedin.png
```

This would be referenced as `Resources.cluedin.png`.

The following example shows how the Provider Icon is used in the application:

![Diagram]({{ "/assets/images/integration/provider-icons.png" | relative_url }})

## Domain

This property represents the URL of your application:

- Leave it empty if the integration does not have a website.

- CluedIn.UI uses this value to redirect users to the integration’s website when more information is needed.

For example, for a Slack integration, you would set the `Domain` property to `https://slack.com/`.


## About

This property represents the description of the integration.

For example, for a Zendesk integration, you could use the following: `Zendesk makes better experiences for agents, admins, and customers. As employees, we encourage each other to grow and innovate.`

## AuthMethods

The authentication methods property is a JSON object that tells CluedIn.UI how the user should authenticate with the integration.

### Oauth

CluedIn provides a mechanism to handle integrations that require an OAuth flow. However, you must still provide a redirect URL so the UI knows where to send the user during authentication.

Example:

```
"authMethods": {
  "oauth": {
    "oauthCallbackKey": "office365azureactivedirectory",
    "initial": "api/office365azureactivedirectory?authError=none",
    "callback": "api/office365azureactivedirectory?authError",
  },
},
```

{:.important}
In future versions, CluedIn will aim to remove the need for these values by introducing generic controllers. However, due to certain exceptions encountered with some OAuth mechanisms, these values are still required for now.

### Credentials

Credentials are generally used for systems that require basic authentication. These credentials allow the integration to pull data from the source system.

Example:

```
"credentials": [{
  "displayName": "User Name",
  "type": "input",
  "isRequired": true,
  "name": "username",
}, {
  "displayName": "Password",
  "name": "password",
  "type": "password",
  "isRequired": true,
}],
```

### API token

Some integrations require an API token to be included with the request.

Example:

```
"token": [{
  "displayName": "Api Token",
  "type": "input",
  "isRequired": true,
  "name": "apiToken",
}],
```

### Custom

If your integration requires a custom field, you can add it to the `credentials` object as an extra field.

```
"credentials": [{
    "type": "subdomain",
    "name": "websiteName",
    "displayName": "Website Name",
    "protocol": "https://",
    "domain": "zendesk.com",
    "isRequired": true,
  }, {
    "type": "input",
    "name": "username",
    "displayName": "Username",
    "isRequired": true,
  }, {
    "type": "password",
    "name": "password",
    "displayName": "Password",
    "isRequired": true,
}],
```

### Properties

The properties let you define more precisely what to crawl from an integration.

- If you want the integration to fetch all data, leave the properties empty.

- If you want to limit the scope, you can require the user adding the integration to select a specific project, folder, or another type of segmentation supported by the integration.

Example – List of projects:

```
[{
  "displayName": "Projects to include",
  "type": "list",
  "isRequired": true,
  "name": "projects",
  "options": {
    "key": "Id",
    "displayName": "Name",
    "stateField": "State",
    "states": ["ACTIVE", "INACTIVE"],
  }
}]
```

- `displayName` – The label displayed in the UI when the integration is rendered.
- `type` – The type of data returned, either `list` or `tree`.
- `isRequired` – Indicates whether the user must provide this information.
- `name` – The name of the field to configure (taken from `HelperConfiguration`).
- `options` – The value that should be set for each value selected by the user.

Example – Tree of folders:

```
[{
  "displayName": "Folders to include",
  "name": "folders",
  "type": "tree",
  "isRequired": true,
}]
```

{:.important}
Contact us if you need more options.

### Type

A list of types for the integration. This is especially useful when you have many integrations installed.

Possible values include:

- `Cloudfile`

- `Support`

- `CRM`

- `Social`

- `Code`

- `Task`

- `Communication`

Example:

```
type: ["Task", "Support"]
```

In the UI:

![Diagram]({{ "/assets/images/integration/integration-categories.png" | relative_url }})
