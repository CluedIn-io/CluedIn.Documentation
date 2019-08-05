---
category: Data Cleaning
---

# Research GQL Frankenstein projects

We have started a GQL api but never finished it.

This project is about defining a GQL for CluedIn which would scale and could evolve independently of the main repository.


## Main Repo GQL Schema

The current schema is pretty small.

Moreover, for Golden, the latest / upcoming is not needed.

Also the entitySchema should probably be called Catalog.


```
me: Identity

entity(id: Guid!): IEntity

latest(
  entityType: EntityType
  entityTypes: [EntityType]
  contextId: Guid
  contextIds: [Guid]
  cursor: PagingCursor
  pageSize: Int
): PagedDataResult_EntityInterface

upcoming(
  entityType: EntityType
  entityTypes: [EntityType]
  contextId: Guid
  contextIds: [Guid]
  cursor: PagingCursor
  pageSize: Int
): PagedDataResult_EntityInterface

search(
  query: String
  filter: String
  filters: [FilterQuery]
  contextId: Guid
  contextIds: [Guid]
  cursor: PagingCursor
  pageSize: Int
  sort: SortMethod
  sortDirection: SortDirection
  rankingSettings: RankingSettings
  includeExternalData: Boolean
  includeUnstructuredData: Boolean
): PagedSearchResult_EntityInterface

entitySchema: EntityPropertySchemaScalar

```

### Code repo

https://github.com/CluedIn-io/CluedIn/tree/1c82c67cb27cd2ed361ad2e713adbe53f3f21b12/Code/Core.GraphQL


## Needed Schema

Full GQL Schema for matching production.

Please note, we are introduce schema module to ease the separation and matching the same sections as the UI / Documentation...

**NOTE: GDPR Schema as been ignored for now as it is critical and hard to test, so we will update it later**

**Query**

```
  Administration {
    organization: Organization //usage should be resolver
    user(id: String): User
    users: [User]
    token: Token
    potentialUsers(): [PotentialUser]
    invitations(): [UserInvitation]
  }
  Integration {
    connectors(): [Connector]
    connector(id: ID!): Connector //permission + owners is a nested resolvers
  }
  Manipulation {
    catalog: EntityPropertySchemaScalar
  }
  Entity {
    entity(id: Guid!): IEntity //history should be a resolver of Entity
    search(
      query: String
      filter: String
      filters: [FilterQuery]
      contextId: Guid
      contextIds: [Guid]
      cursor: PagingCursor
      pageSize: Int
      sort: SortMethod
      sortDirection: SortDirection
      rankingSettings: RankingSettings
      includeExternalData: Boolean
      includeUnstructuredData: Boolean
    ): PagedSearchResult_EntityInterface
  }
  Marketplace {
    connectors(
      q: String
      staffPick: Boolean
      new: Boolean
      categories: [String]
    ): [Connector]
    connector(
      id: String!
    ): Connector
    connectorPair(
      id: String!
      extraId: String!
    ): [Connector]
    connectorCategories: [ConnectorCategory]
    enrichers(
      q: String
      staffPick: Boolean
      new: Boolean
      categories: [String]
    ): [Enricher]
    enricher(
      id: String!
    ): Enricher
  }
  Manipulation {
    duplicates: [DuplicateEntry]
  }
  Governance {
    dataBreaches(): [DataBreach]
    dataBreach(id: ID!): DataBreach
    retention(id: ID!): Retention
    retentions(): [Retention]
  }
```

**Mutation**

```
  Administration {
    activateUser(id: ID!): User
    deActivateUser(id: ID!): User
    saveOrganization(organizationInput: OrganizationInput!): Organization
    generateToken: Token
    revokeToken(id: ID!): Token
    inviteUser(id: ID!): UserInvitation
    removeInviteUser(id: ID!): UserInvitation
    promoteUser(id: ID!, roleName: string): UserRole
    demoteUser(id: ID!, roleName: string): UserRole
    promoteUserToRole(id: ID!, roleName: string): UserRole
    demoteUserToRole(id: ID!, roleName: string): UserRole
  }
  Integration {
    inviteUserToAddConnector(id: ID!): ConnectorUserInvitation
    addActiveConnector(connectorInput): Connector
    enableProvider(connectorInput): Connector
    saveConnector(connectorInput): Connector
    addTrelloToken(token: string!): Connector
    addUserToConnector(id: ID!, userId: ID!): ConnectorPermission
    removeUserToConnector(id:ID!, userId: ID!): ConnectorPermission
    addUsersToConnector(id: ID!, userIds: [ID]): [ConnectorPermission]
    removeUsersToConnector(id:ID!, userIds: [ID]): [ConnectorPermission]
    playConnector(id: ID!): Connector
    pauseConnector(id: ID!): Connector
    rejectConnector(id: ID!): Connector
    approveConnector(id: ID!): Connector
    processConnector(id: ID!): Connector
    addProductOwnerToConnector(id:ID!, userId: ID!): ConnectorOwner
    removeProductOwnerToConnector(id:ID!, userId: ID!): ConnectorOwner
    addProductOwnersToConnector(id:ID!, userIds: [ID]): [ConnectorOwner]
    removeProductOwnersToConnector(id:ID!, userIds: [ID]): [ConnectorOwner]
  }
  Entity {
    anonymiseProperty(propertyTransformationInput): TransformationInput
    deAnonymiseProperty(propertyTransformationInput): TransformationInput
    externalSearch(id: ID!): Entity
    markEntitySensitive: (id: ID!): Entity
    markEntityUnSensitive: (id: ID!): Entity
    updateEntityProperty:(propertyTransformationInput): TransformationInput
    reProcessEntity: (id: ID!): Entity
    merge(id:ID!, targetIds: [ID], mergeDelta: MergeDelta): Entity
  }
  Governance {
    createDataBreach(DataBreachInput): DataBreach
    deleteDataBreach(id: ID!): DataBreach
    deleteDataBreaches(ids: [ID]): [DataBreach]
    createRetention(retentionInput: RetentionInput): Retention
    deleteRetention(id: ID!): Retention
    deleteRetention(ids: [ID]): [Retention]
  }
```

## GDPR

Query:

```
  Governance: {
    sar(id:ID!): Sar
    sars(): Sars
    gdprConfiguration(): GdprConfiguration

  }
```

Mutation:

```
  Governance: {
    crateSar(sarInput: SarInput): Sar
    saveSar(sarInput: SarInput): Sar
    createSarReport(SarReportInput): SarReport
    updateSarReport(SarReportInput): SarReport
    sendGdprReport(id: ID!, email: string!): Sar
    updateGdprConfiguration(gdprConfiguration: GdprConfiguration): GdprConfiguration
  }
```


Other code to migrate:

//Need to ask Denis if he know all of this is

```

export const removeAllData = id =>
  apiRequest('POST', `/api/v1/remove/gdpr?id=${id}`);

export const minimizeUserData = id =>
  apiRequest('POST', `api/v1/gdpr/minimize?id=${id}&isQueued=true`).then(getBody);

export const subscribeForUserData = ({ guid, id: sarId }) =>
  apiRequest('POST', `api/v1/gdpr/subscribe?guid=${guid}&sarId=${sarId}`);

export const unSubscribeForUserData = ({ guid, id: sarId }) =>
  apiRequest('POST', `api/v1/gdpr/unsubscribe?guid=${guid}&sarId=${sarId}`);

export const unMinimizeUserData = id =>
  apiRequest('POST', `api/v1/gdpr/unminimize?id=${id}`).then(getBody);

export const addFromProcessing = id =>
  apiRequest('POST', `api/v1/gdpr/unprocessing?id=${id}`).then(getBody);

export const getConsentReport = () =>
  apiRequest('GET', 'api/gdpr/consent').then(getBody);

export const getIdentifiersReport = () =>
  apiRequest('GET', 'api/gdpr/indentifying').then(getBody);

export const getEncryptedReport = () =>
  apiRequest('GET', 'api/gdpr/encrypted').then(getBody);

export const getLocationReport = () =>
  apiRequest('GET', 'api/gdpr/location').then(getBody);

export const getEntityTypesReport = () =>
  apiRequest('GET', 'api/gdpr/entitytypes').then(getBody);

export const escalate = (sarId, entityIdToEscalateTo, reason) => {
  const args = `?sarId=${sarId}&identityId=${entityIdToEscalateTo}&reason=${reason}`;

  return apiRequest('POST', `api/gdprescalate/${args}`)
    // it seems empty response means all good (200 OK)
    .then(getBody);
};

export const getExtendReportTransforms = () => (
  apiRequest('GET', 'api/gdpr/transforms')
    .then(getBody)
);

export const postExtendReportData = (sarId, transformId, file) =>
  apiRequest(
    'POST',
    `api/gdpr/clue?sarId=${sarId}&transformId=${transformId}`,
    file
  );

export const batchImportFromFile = file => (
  apiRequestForSARBatch(
    'POST',
    'api/gdpr/report/batch',
    file,
  )
    .then(getBody)
    .then(res => JSON.parse(res))// because json string
    .then((resp) => {
      if (!resp || (resp && resp.length === 0)) {
        const err = new Error('batchImportDataFailure: Empty response from the server. \n No data could be found in the file');
        console.error(err);
        throw err;
      }
      return resp;
    })// because can upload png
);

```