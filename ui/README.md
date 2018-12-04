# UI

Please refer to [CluedIn.UI](https://github.com/CluedIn-io/CluedIn.Widget) repository if you need more information.

## Integration Configuration file

The integration configuration is configure to setup the self-service integration.

You can find it here:

https://github.com/CluedIn-io/CluedIn.Widget/blob/master/core/modules/integration/config/providers.js

Example:

```
'02940843-7b6b-4cfb-9fd2-f498bae89c0d': {
    name: 'Asana',
    icon: `${cdnUrl}asana.png`,
    domain: 'asana.com',
    type: [projectManagmentType],
    about: 'Asana is a web and mobile application designed to help teams improve communication, teamwork and collaboration.',
    authMethods: {
      oauth: {
        oauthCallbackKey: 'asana',
        initial: 'api/asana?authError=none',
        callback: 'api/asana?authError',
      },
    },
    properties: [{
      displayName: 'Workspaces',
      type: 'list',
      isRequired: true,
      name: 'workspaces',
      options: {
        key: 'Id',
        displayName: 'Name',
        stateField: 'State',
        states: ['ACTIVE', 'INACTIVE'],
      },
    }, {
      displayName: 'Projects',
      type: 'list',
      isRequired: true,
      name: 'projects',
      options: {
        key: 'Id',
        displayName: 'Name',
        stateField: 'State',
        states: ['ACTIVE', 'INACTIVE'],
      },
    },
    WEBHOOK_PROPERTY,
    ],
},
```

### Configuration Object

- The key is the providerID
- name is the name that will be display on the UI
- icon is the path that will be display by the UI (if not present, will fallback to first letter)
- type: [] array of enum for the filtering in the UI
- about: short description displayed in the UI
- authMethods, configuration object to tell the UI what form to render for the 1st step when adding an integration
- properties: an array of properties to render for the 2nd step and/or the edit of a configuration.
- Add WEBHOOK_PROPERTY if the configuration supports webhook.

## Entity configuration file

Currently the Entity page is configured based on a configuration object.

You can find it here:

https://github.com/CluedIn-io/CluedIn.Widget/blob/master/core/modules/wms/onPremiseLayout.js

### Reason for an entity object:

### Configuration Object

Here is a sample:

```
{
  _id: '5b4c9733139ec9bfdc5ad5de',
  __v: 0,
  icon: 'Issue',
  displayName: 'Support Ticket',
  entityType: '/Support/Ticket',
  tabs: [],
  guid: '239fa7c0-3844-11e6-bef1-1bafabfeeb7f',
  widgets: [],
  suggestedSearchFilter: [],
  includeSuggestedSearches: false,
  created: '2018-07-22T06:41:27.612Z',
  isDefault: true,
},
```

- _id is depricated
- __v: 0 is depricated
- icon: the name of the icon being used (see [full icon list](http://www.uxilab.eu/components/icons))
- displayName is the value that will be display in various places in the UI (eg: search filter)
- tabs: [] is the configuration of the different tabs of the Entity Page (in addition to 'All Properties' and 'Pending changes')
- guid: is required, ideally a unique GUID
- widgets: [] an array of object to configure the widgets to show
- suggestedSearchFilter: [] an array of object to configure what to show as suggested search
- includeSuggestedSearches: boolean (true|false) 
- created: optional value to set how the config was created.
- isDefault is depricated

Example of a complex configuration:

```
{
    _id: '576a331728ef63601b279dd5',
    __v: 0,
    icon: 'Organization',
    route: 'organization/:id',
    displayNameWithArticle: 'an organization',
    layout: {
      name: 'DefaultTab',
      _id: '5758382fb0b4463d12aff1b4',
    },
    entityType: '/Organization',
    displayName: 'Organization',
    tabs: [
      {
        place: 'main',
        _id: '5758382fb0b4463d12aff1a0',
        children: [
          {
            name: 'info',
            displayName: 'Latest Information',
            layout: {
              name: 'TowColumns',
              _id: '5758382fb0b4463d12aff1ac',
            },
            _id: '5758382fb0b4463d12aff1a7',
            suggestedSearchFilter: [],
            includeSuggestedSearches: true,
          },
        ],
      },
    ],
    guid: 'ccc59130-2d8c-11e6-98af-43f586d4a24c',
    widgets: [
      {
        name: 'entityOrganizationHeader',
        place: 'header',
        _id: '5758382fb0b4463d12aff1b3',
        parameters: '{}',
        onlyAdmin: false,
      },
      {
        place: 'info.profile',
        _id: '5758382fb0b4463d12aff1b1',
        name: 'EntityProperty',
        parameters: '{}',
        onlyAdmin: false,
      },
      {
        place: 'info.profile',
        _id: '5758382fb0b2863d12aff1b1',
        name: 'UpcomingMeetings',
        parameters: '{}',
        onlyAdmin: false,
      },
      {
        name: 'Fact',
        place: 'info.profile',
        _id: '5758273062971f780f4426fc',
        parameters: '{}',
        onlyAdmin: false,
      },
      {
        _id: '5758382fb0b4463d12aff1b2',
        name: 'EntitySourceAndProfile',
        place: 'info.profile',
        parameters: '{}',
        onlyAdmin: false,
      },
      {
        name: 'EntitySocialOverview',
        place: 'info.profile',
        _id: '5758382fb0b4463d12aff1b0',
        parameters: '{}',
        onlyAdmin: false,
      },
      {
        name: 'LastActivity',
        place: 'info.main',
        _id: '5758382fb0b4463d12aff1a4',
        parameters: '{}',
        onlyAdmin: false,
      },
      {
        name: 'LastDocuments',
        place: 'info.main',
        _id: '5758382fb0b4463d12aff1af',
        parameters: '{}',
        onlyAdmin: false,
      },
      {
        name: 'LastIssues',
        place: 'info.main',
        _id: '5758382fb0b4463d12aff1ae',
        parameters: '{}',
        onlyAdmin: false,
      },
      {
        name: 'EntityPersonList',
        place: 'employee.main',
        _id: '5758382fb0b4463d12aff1ad',
        parameters: '{}',
        onlyAdmin: false,
      },
    ],
    suggestedSearchFilter: [],
    includeSuggestedSearches: false,
    created: '2016-06-08T15:22:23.555Z',
    isDefault: true,
}
```

## Entity configuration file