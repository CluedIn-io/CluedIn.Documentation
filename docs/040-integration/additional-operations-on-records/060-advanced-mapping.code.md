---
layout: default
nav_order: 3
parent: Additional operations
grand_parent: Integration
permalink: /integration/additional-operations-on-records/advanced-mapping-code
title: Advanced mapping code
tags: ["integration", "property rules"]
last_modified: 2024-01-15
---

In this article, you will learn about the possibility of introducing changes to your [clues](/key-terms-and-features/clue-reference) using JavaScript glue code. You can perform similar actions as with [property](/integration/additional-operations-on-records/property-rules) and [pre-process](/integration/additional-operations-on-records/preprocess-rules) rules but you gain greater flexibility to set up complex conditions.

The advanced mapping code is applied to the clues after property and pre-process rules.

![advanced-mapping-code.png](../../assets/images/integration/additional-operations/advanced-mapping-code.png)

**Prerequisites**

To access advanced mapping, go to **Administration** > **Feature Flags**, and then turn on the **Advanced Mapping** feature.

## Write advanced mapping code

Sometimes, the conditions in property and pre-process rules might appear cumbersome when you need to execute complex logic on your records. In such cases, you can use the advanced mapping capabilities that allow you to modify clues by executing the code. From a security perspective, advanced mapping runs on a virtual machine that does not have access to your network.

The advanced mapping code can be executed on the following levels:

- **Code mapping before sending clues** – default level that allows you to modify clues using built-in [methods](#available-methods). Our article focuses on this level because it is the most commonly used.

- **Code mapping before creating clues** – additional level that only allows you to modify record values using the following code:
    
    ```
    value['customer.companyName'] = 'Star';

    [value]
    ```

    Where `'customer.companyName'` is the name of the property, `'Star'` is the value that will be set to the property in each record, and `[value]` is an element that indicates that the code is executed for each record.  
     
**Example**

Suppose you have ingested the revenue data, and you want to add tags to facilitate the retrieval of golden records in CluedIn. You want to add a tag  "Golden" to those records where the revenue is greater than or equal to 1000000; and another tag "Silver" to those records where the revenue is greater than or equal to 500000 . You can achieve that by writing the advanced mapping code similar to the following example.

```
if (getVocabularyKeyValue('customer.revenue') >= 1000000) {
    addTag('Golden');
} else if (getVocabularyKeyValue('customer.revenue') >= 500000) {
    addTag('Silver');
}
[value]
```

**Note:** `[value]` is an important element that indicates that the code is executed for each clue.

**To modify clues by writing the advanced mapping code**

1. On the navigation pane, go to **Integrations** > **Data Sources**. Then, find and open the data set.

1. Go to the **Map** tab, and then select **Advanced**.

1. In the upper-right corner, make sure that **Code mapping before sending clues** is selected.

1. Select **Run** to load all clues that were created from the data set.

    The clues appear on the right side of the page. If you have created property or pre-processed rules, note that they have already been applied to the clues.

1. On the right side of the page, write the code to modify the clues as needed. You can write any JavaScript code.

    To check if the code is applied as intended, select **Run**.

1. If you are satisfied with the result, select **Save**.

    Your changes to the clues are saved. The advanced mapping code is executed right before you send the data into processing pipeline.

## Available methods

This is a reference section that lists all available methods that you can use to write the advanced mapping code. Please refer to [CluedIn Expression Language (C.E.L.)](/kb/cel) for all string and math methods. This section is focused on built-in CluedIn-specific methods.

**getVocabularyKeyValue**

Retrieves the clues that have a specific vocabulary key in order to apply further actions on the values or clues. In the following example, the code retrieves specific values of `'customer.industry'` and adds a tag "Golden Oil & Gas" to those clues where `'customer.revenue'` is greater than 750000. 

```
if (
    (getVocabularyKeyValue('customer.industry') === 'Natural Gas Distribution' || 
     getVocabularyKeyValue('customer.industry') === 'Oil & Gas Production') &&
     getVocabularyKeyValue('customer.revenue') > 750000
) {
    addTag('Golden Oil & Gas');
}
    
[value]
```

**setVocabularyKeyValue**

Changes the vocabulary key values. In the following example, the code retrieves the current value of `'customer.industry'` using `getVocabularyKeyValue`, converts it to lowercase using `toLowerCase()`, and then sets the updated lowercase value using `setVocabularyKeyValue`.


```
setVocabularyKeyValue('customer.industry', getVocabularyKeyValue('customer.industry').toLowerCase());

[value]
```
 
**getEntityProperty**

Retrieves the clues that have a specific entity property in order to apply further actions on the values or clues. In the following example, the code takes the `'name'` property from the clue, converts it to uppercase using `toUpperCase()`, and then sets the result as the value of the `'description'` property for the clue.

```
const name = getEntityProperty('name');
setEntityProperty('description', name.toUpperCase());

[value]
```

**setEntityProperty**

Adds or changes the value of the entity property, such as name, description, entityType, date created, and so on. In the following example, the code checks if the `'customer.industry'` vocabulary key is set to `'Precious Metals'`, and if it is, the code sets the `'description'` property of the clue to the specified string.

```
if (getVocabularyKeyValue('customer.industry') === 'Precious Metals') {
    setEntityProperty('description', 'This record comes from corporate CRM');
}

[value]
```

**removeVocabularyKey**

Removes vocabulary key from the clues. In the following example, the code removes the `'customer.revenue'` vocabulary key from all clues.

```
removeVocabularyKey('customer.revenue')

[value]
```

**quarantine**

Send the clues that do not meet certain conditions to quarantine. In the following example, the code checks if the value of `'customer.revenue'` is absent or equal to 0. If it is, the code send such clues to quarantine.

```
const customerRevenue = getVocabularyKeyValue('customer.revenue');

if (customerRevenue === undefined || customerRevenue === null || customerRevenue === 0) {
    quarantine();
}

[value]
```

**addAlias**

Adds aliases to the clues. In the following example, the code adds an alias taken from the `'customer.company'` vocabulary key to each clue.

```
addAlias(getVocabularyKeyValue('customer.company'));

[value]
```

**addTag**

Adds tags to the clues. In the following example, the code checks if the value of `'customer.industry'` is equal to "Oil & Gas". If the condition is true, a tag "Oil & Gas" is added to the corresponding clues. 


```
if (getVocabularyKeyValue('customer.industry') === 'Oil & Gas') {
    addTag('Oil & Gas');
}

[value]
```

**addCode**

Adds a code to the clue. Since the code usually consists of entity type, origin, and a specific value, the resulting code would be `"/Customer#doccontactcsv:thisismycode"`.

```
addCode("thisismycode")

[value]
``` 

**removeTags**

Removes all tags from the clue.

```
removeTags()

[value]
```

**removeCodes**

Removes all codes from the **Codes** section of the clue.

```
removeCodes()

[value]
```

**removeAliases**

Removes all aliases from the clue.

```
removeAliases()

[value]
```