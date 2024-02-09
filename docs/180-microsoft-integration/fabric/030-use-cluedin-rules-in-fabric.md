---
layout: cluedin
title: Use CluedIn rules in Microsoft Fabric
parent: Microsoft Fabric Integration
grand_parent: Microsoft Integration
permalink: /microsoft-integration/fabric/use-cluedin-rules-in-fabric
nav_order: 030
has_children: false
---

CluedIn provides a powerful GraphQL API that can be used to get data and metadata and to execute actions. In this article, you will learn how to read CluedIn rules' metadata in Microsoft Fabric and use it to work with data in OneLake.

**To use CluedIn rule in Microsoft Fabric**

1. Create a notebook in Microsoft Fabric, install dependencies, and get a CluedIn access token.

    ```python
    !pip install cluedin
    !pip install jqqb_evaluator
    
    import cluedin
    from jqqb_evaluator.evaluator import Evaluator
    from copy import deepcopy
    from itertools import repeat
    
    ctx = cluedin.Context.from_dict({
      "domain": "cluedin.demo",
      "org_name": "foobar",
      "user_email": "admin@cluedin.demo",
      "user_password": "yourStrong(!)Password"
    })
    ctx.get_token()
    ```

1. Get all the rules from CluedIn.

    ```python
    query = """
    query getRules($searchName: String, $isActive: Boolean, $pageNumber: Int, $sortBy: String, $sortDirection: String, $scope: String) {
      management {
        id
        rules(
          searchName: $searchName
          isActive: $isActive
          pageNumber: $pageNumber
          sortBy: $sortBy
          sortDirection: $sortDirection
          scope: $scope
        ) {
          total
          data {
            id
            name
            order
            description
            isActive
            createdBy
            modifiedBy
            ownedBy
            createdAt
            modifiedAt
            author {
              id
              username
              __typename
            }
            scope
            isReprocessing
            __typename
          }
          __typename
        }
        __typename
      }
    }
    """
    
    variables = {
      "scope": "DataPart"
    }
    
    rules = cluedin.gql.org_gql(ctx, query, variables)['data']['management']['rules']['data']
    ```

1. If you want to get a particular rule by ID, use the following method.

    ```python
    import requests
    
    def get_rule(ctx rule_id):
      headers = {
        'Authorization': 'Bearer {}'.format(ctx.access_token),
        'Content-Type': 'application/json'
      }
    
      return requests.get(
        f'{api_url}/rules/{rule_id}',
        headers=headers)
    ```

1. Evaluate CluedIn rules' conditions in a notebook on the Microsoft Fabric side. The rules' format is based on [Querybuilder.js](https://querybuilder.js.org/), so with minimal transformations, you can use it together with the [jqqb_evaluator](https://pypi.org/project/jqqb-evaluator/) library to evaluate CluedIn rules' conditions.

    ```python
    # Map a CluedIn rule JSON to Querybuilder syntax
    def rule_json_to_querybuilder(rule_json, property_map):
      result = deepcopy(rule_json)
      result.pop('objectTypeId', None)
      for key in ['field', 'type', 'value']:
        if result[key] == None:
          result.pop(key, None)
      if result['operator'] == '00000000-0000-0000-0000-000000000000':
        result.pop('operator', None)
      else:
        result['operator'] = rule_operator_id_to_querybuilder_string(result['operator'])
      
      if 'value' in result and len(result['value']) == 1:
        result['value'] = result['value'][0]
    
      if 'field' in result and result['field'] in property_map:
        result['field'] = property_map[result['field']]
    
      if 'type' not in result or result['type'] == 'rule':
        result['rules'] = list(map(rule_json_to_querybuilder, result['rules'], repeat(property_map)))
      else:
        result['input'] = 'text'
        result.pop('rules', None)
    
      return result
    
    def rule_operator_id_to_querybuilder_string(rule_operator_id):
      if rule_operator_id == '0bafc522-8011-43ba-978a-babe222ba466':
        return 'equal'
      # TODO: add more cases
      else:
        return None
    ```

1. Load a data frame from Spark.

    ```python
    df = spark.read.format("csv").option("delimiter", "\t").option("header", "true").load(PATH_TO_CSV_IN_ONELAKE)
    ```

1. Filter data with the conditions provided from CluedIn rules.

    ```python
    # the property_map is needed to map CluedIn vocabulary keys to properties of our dataset in OneLake
    property_map = {
      'Properties[IMDb.name.basic.BirthYear]': 'birthYear',
      'Properties[IMDb.name.basic.DeathYear]': 'deathYear',
    }
    
    rule_set = rule_json_to_querybuilder(rule_json['conditions'], property_map)
    
    evaluator = Evaluator(rule_set)
    
    def row_filter(row):
      return evaluator.object_matches_rules(row.asDict())
    
    # rows:            11.369.728 11.99 seconds (48.63 seconds with always-true filter)
    # positive filter: 11.185.109 1.24 minutes
    # negative filter:    184.619 1.22 minutes
    
    df.rdd.filter(row_filter).count()
    ```