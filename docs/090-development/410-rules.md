---
layout: cluedin
title: Rules in CluedIn
parent: Development
nav_order: 410
permalink: {{ site.baseurl }}/developer/rules
tags: ["development","rules"]
published: false
---

Using the rules engine, CluedIn users can configure areas of the application to operate on specific entities.
The entities can then be modified, or simply returned to provide a filter on querying.

![StreamRules](../assets/images/development/streamrules.png)

## Creating a RuleAction

> The following guidance is for version `3.2.4+`

_RuleActions_ are simple classes that can be included into any extension and deployed into CluedIn.
_RuleActions_ are automatically discovered by CluedIn at start up and do not
need to be directly registered.

To create a _RuleAction_:
1. Create a class that extends `BaseRuleAction`
    + The base class provides the simplest foundation to build upon
1. Override the `Name` and `SupportsPreview` properties
    + `Name` should be user friendly text as it will be displayed in the UI.
    + Set `SupportsPreview` to `true` only if you want to support calling the action in preview mode
1. Optionally add `RuleProperty` members
    + Each property decorated with the `[RuleProperty]` attribute will be displayed in the UI with a field for users to enter data.
1. Implement the `Run` method
    + This is the method called when the action is actually invoked. Here you can apply changes to the entity or use the `context` to access other areas of CluedIn.
    + Return a `RuleActionResult` that contains details of the change that occurred.

> NOTE: Your class **must** have a parameter-less constructor, or no constructors.

```c#
using CluedIn.Core.Data.Parts;
using CluedIn.Core.Processing;
using CluedIn.Core.Rules;
using CluedIn.Core.Rules.Models;

namespace CluedIn.Rules.Actions
{
    public class AddTag : BaseRuleAction
    {
        public override string Name => "Add Tag";

        public override bool SupportsPreview => false;

        [RuleProperty]
        public string Value { get; set; }

        public override RuleActionResult Run(ProcessingContext context, IEntityMetadataPart entityMetadataPart, bool isPreview)
        {
            var parsedValue = ParseTokens(Value, context, entityMetadataPart);

            entityMetadataPart.Tags.Add(new Core.Data.Tag(parsedValue));

            return new RuleActionResult { IsSuccess = true, Messages = new string[] { $"Added Tag {parsedValue}" } };
        }
    }
}
```

CluedIn will then be able to list the _RuleAction_:
![RuleAction](../assets/images/development/actionlist.png)


### Parsing Tokens
> The following guidance is for version `3.2.4+`

Users may supply tokens to fields in a _RuleAction_ to set dynamic values that will be resolved when the action runs.

To ensure rule tokens are resolved, a call should be made to `ParseTokens` within the `Run` method:
```c#
///
var parsedValue = ParseTokens(Value, context, entityMetadataPart);

entityMetadataPart.Tags.Add(new Core.Data.Tag(parsedValue));
///
```
Here, the `RuleProperty` called `Value` may contain tokens - the value is passed to `ParseTokens` with the variable `parsedValue` containing the resulting value.  The `parsedValue` is then adding to the entity as a tag.

### Supporting Preview
To support preview, further changes are required:
1. Set `SupportsPreview` to `true`
1. Implement `IRuleActionPreview` on the class
    + e.g. `public class AddTag : BaseRuleAction, IRuleActionPreview`
1. Implement the `BuildPreviewData` method

`BuildPreviewData` will be invoked _before_ the `Run` method - it is used to
prepare a dummy entity with data that can be modified.
When implementing the method, modify the property so that the `Run` method should succeed. For example, in the `DeleteValue` _RuleAction_ the `BuildPreviewData` method adds a field, so that when `Run` is invoked, the field can be removed
```c#
public void BuildPreviewData(IEntity result)
{
    result.Properties.Add(FieldName, "Old Value");
}
```

## Creating a RuleToken
> The following guidance is for version `3.2.4+`

_RuleTokens_ allow a user to provide a value to a rule action property that will be resolved when the action is invoked. Examples include:
+ Getting a data
+ Getting the value of vocabulary

As with _RuleActions_ they can be implemented with simple classes that can be included in an extension and are automatically resolved when CluedIn starts up.

To create a RuleToken:
1. Create a class that implements `IRuleActionToken`
1. Set the `Key` property
    + This is the text that the user will use in the UI
1. Implement the `Resolve` member
    + The `input` passed to this member will be an optional value that the user specifies

```c#
using CluedIn.Core.Data.Parts;
using CluedIn.Core.Processing;

namespace CluedIn.Rules.Tokens.Implementations
{
    public class VocabularyToken : IRuleActionToken
    {
        public string Key => "Vocabulary";

        public string Resolve(ProcessingContext context, IEntityMetadataPart entityMetadataPart, string input)
        {
            if (entityMetadataPart.Properties == null)
                return input;

            if (entityMetadataPart.Properties.TryGetValue(input, out var value))
                return value;

            return input;
        }
    }
}
```

Users can then specify the token in a field when configuring a _RuleAction_:
![RuleTokens](../assets/images/development/tokens.png)
In this example, the user is setting the `user.fullName` property to the combined value of "`user.firstName user.lastName`"