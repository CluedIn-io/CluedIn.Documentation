---
category: Manipulation
title: Fuzzy Merging Explained
---

Fuzzy Merging is the process of accepting that certain records will not have a unique way to find each other. This documents the process of how CluedIn makes a decision whether two or more records should merge with each other. 

If an incoming record has not been able to find an existing record in CluedIn with a perfect Entity Code match, then the next thing it will try is to run Fuzzy Merging. 

FuzzyEntityMatching can be disabled at a Global level using the configuration switch of ClueProcessing.FuzzyEntityMatching.Enabled set to either false or true.

We then evaluate if the particular clue that we are going to lookup has processing intructions on it that either ignores or subscribes to the fuzzy matching process. 

Now is your change to introduce custom logic in code to ignore certain records from continuing using the IProcessingFilter "IsFuzzyMatchEntityPrefiltered()" method. 

After this CluedIn will then look at all implementations of the IFuzzyEntityMatcher interface including many that ship with CluedIn out of the box. These IFuzzyEntityMatchers are the pieces of logic that try to determine a group of possible matches of entities. 

After this, CluedIn will choose the entity that has the best possible match. 

Below is an example of how you could extend the Fuzzy merging with your own logic.

```csharp
using System;

using CluedIn.Core;
using CluedIn.Core.Data;
using CluedIn.Core.Data.Parts;

namespace CluedIn.Processing.EntityResolution
{
    /// <summary>A custom fuzzy matcher</summary>
    /// <seealso cref="CluedIn.Processing.EntityResolution.FuzzyEntityMatcherBase" />
    public class CustomFuzzyMatchingMatcher : FuzzyEntityMatcherBase
    {
        /**********************************************************************************************************
         * PROPERTIES
         **********************************************************************************************************/

        /// <summary>
        /// Gets a value indicating whether the matcher should be used in clue to entity matching.
        /// </summary>
        /// <value>
        /// <c>true</c> if the matcher should be used in clue to entity matching; otherwise, <c>false</c>.
        /// </value>
        public override bool UseInClueToEntityMatching
        {
            get
            {
                return false;
            }
        }

        /**********************************************************************************************************
         * METHODS
         **********************************************************************************************************/

        /// <summary>
        /// Checks if the specified entity type can be matched be this instance.
        /// </summary>
        /// <param name="type">The type.</param>
        /// <returns>
        ///   <c>true</c> if the entity matcher can match the specified entity type; otherwise <c>false</c>.
        /// </returns>
        /// <exception cref="System.ArgumentNullException">type</exception>
        public override bool Accepts(EntityType type)
        {
           return true;
        }

        /// <summary>Finds the matches.</summary>
        /// <param name="id">The identifier.</param>
        /// <param name="metadata">The metadata.</param>
        /// <param name="context">The context.</param>
        /// <returns>The matches.</returns>
        public override MatchGrouping FindMatches(Guid id, IEntityMetadata metadata, ExecutionContext context)
        {
 			IEnumerable<string> emailTexts;

            if (!metadata.Properties.TryGetValues(out emailTexts, Vocabularies.CluedInUser.Email, Vocabularies.CluedInUser.EmailAddresses, Vocabularies.CluedInPerson.Email))
                return null;

            emailTexts = emailTexts.SelectMany(e => e.Split(new [] {';', ',', '|'}, StringSplitOptions.RemoveEmptyEntries)).ToList();

            var emails = emailTexts.Where(e => MailAddressUtility.IsValid(e) && !MailAddressUtility.IsNoReplyEmailAddress(context, e)).Select(v => new MailAddress(v));
            var names  = emails.SelectMany(m =>
                {
                    DomainName domainName;

                    if (DomainName.TryParse(m.Host, out domainName))
                        return new[] { m.User, domainName.Domain, m.ToString() };

                    return new[] { m.User, m.ToString() };
                });

            if (!names.Any())
                return null;

            var nicknameModel   = context.ApplicationContext.Container.TryResolve<NicknameModel<string>>("PersonNicknameModel") ?? new NicknameModel<string>();
            var emailProviders  = context.ApplicationContext.Container.TryResolve<BagOfWordsModel<string>>("EmailProviders") ?? new BagOfWordsModel<string>();

            var recordFactory   = new RecordFactory(nicknameModel, emailProviders);
            var hits = FuzzyEntityMatchQueries.FindEmailMatches(context, metadata, names);

            if (hits == null || !hits.Any()) return null;

            return this.BuildMatchGroupings(context, id, metadata, recordFactory, hits);
        }
    }
}
```