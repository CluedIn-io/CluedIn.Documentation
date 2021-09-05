---
layout: default
title: Validate Server Health
parent: Development
nav_order: 150
has_children: false
permalink: /development/validate-server-health
tags: ["development","health-check"]
---

There might be times when you would like to Validate that CluedIn can operate propely once it has been booted. An example of this would be to validate that all Vocabularies are created properly. 

Essentially, the application will not boot if it does not pass all the validation and integrity checks.

Other examples could include:

 - Not booting if integrations do not pass the Validation Framework checks.
 - Not booting if all databases don't connect properly.
 - Not booting if disk space is not available.

Here is an example of adding your own types of Integrity checks when CluedIn boots:

```csharp
using System;
using System.Collections.Generic;
using System.Linq;

using Castle.Windsor;

using CluedIn.Core.Data.Vocabularies;
using CluedIn.Core.Logging;

namespace Custom.Core.IntegrityChecks
{
    /// <summary>The vocabulary checks</summary>
    public class VocabularyChecks : IIntegrityCheck
    {
        public void Verify(IWindsorContainer container, ILogger log)
        {
            var allVocabularies                 = (container.ResolveAll<IVocabulary>() ?? new IVocabulary[0]).ToList();
            var vocabularies                    = allVocabularies.Where(d => d.Keys.Any()).ToList();
            var invalidPropertiesVocabularies   = this.GetInvalidVocabularyProperties(allVocabularies).ToList();

            this.VerifyDuplicateKeysDoesNotExists(allVocabularies, log);

            if (invalidPropertiesVocabularies.Any())
            {
                this.VerifyNullPropertiesDoesNotExists(invalidPropertiesVocabularies, log);
                this.VerifyKeyPropertiesWithNoVocabularyAssignedDoesNotExist(invalidPropertiesVocabularies, log);
                this.VerifyKeyPropertiesThatDoesNotMatchContainingVocabularyDoesNotExist(invalidPropertiesVocabularies, log);
            }

            this.VerifyEmptyVocabulariesDoesNotExist(allVocabularies, log);
            this.VerifyEmptyVocabularyGroupsDoesNotExist(allVocabularies, log);
            this.VerifyVocabulariesWithNoGroupingsDoesNotExists(allVocabularies, log);
            this.VerifyKeyPrefixIsPopulated(allVocabularies, log);

            log.Info(() => "Loaded {0} vocabularies with total {1} keys".FormatWith(vocabularies.Count(), vocabularies.Sum(v => v.Keys.Count())));
        }

        public bool VerifyDuplicateKeysDoesNotExists(IEnumerable<IVocabulary> allVocabularies, ILogger log, bool debugBreak = true)
        {
            var vocabularies  = allVocabularies.Where(d => d.Keys.Any()).ToList();
            var duplicateKeys = vocabularies.SelectMany(v => v.Keys).GroupBy(k => k.ToString()).Where(g => g.Count() > 1).ToList();

            // Validate that no duplicate vocabulary keys exists
            if (duplicateKeys.Any())
            {
                duplicateKeys.ForEach(g => log.Error(() => "Multiple vocabulary keys exists of type: \"{0}\"; Count: {1}; Vocabularies: {2}".FormatWith(g.Key, g.Count(), string.Join(", ", g.Select(k => k.Vocabulary.VocabularyName + " (" + k.Vocabulary.GetType().Name + ")").Distinct()))));

                if (debugBreak)
                    System.Diagnostics.Debugger.Break();
                else
                    return true;

                throw new ApplicationException("Multiple vocabulary keys exists");
            }

            return false;
        }

        public bool VerifyEmptyVocabulariesDoesNotExist(IEnumerable<IVocabulary> allVocabularies, ILogger log, bool debugBreak = true)
        {
            var emptyVocabularies = allVocabularies.Where(d => !d.Keys.Any() && !(d is DynamicVocabulary)).ToList();

            if (emptyVocabularies.Any())
            {
                log.Warn(() => "Found {0} vocabularies with no keys; Vocabularies: {1}".FormatWith(emptyVocabularies.Count, string.Join(", ", emptyVocabularies.Select(v => v.VocabularyName))));
                return true;
            }

            return false;
        }

        public bool VerifyEmptyVocabularyGroupsDoesNotExist(IEnumerable<IVocabulary> allVocabularies, ILogger log, bool debugBreak = true)
        {
            var emptyVocabularyGroups = allVocabularies.OfType<SimpleVocabulary>().SelectMany(v => v.Groups).Where(g => !g.Keys.Any()).ToList();

            if (emptyVocabularyGroups.Any())
            {
                log.Warn(() => "Found {0} vocabulary key groups with no keys; Vocabularies: {1}".FormatWith(emptyVocabularyGroups.Count, string.Join(", ", emptyVocabularyGroups.Select(v => v.Name + " (" + v.Vocabulary.VocabularyName + ")"))));
                return true;
            }

            return false;
        }

        public bool VerifyVocabulariesWithNoGroupingsDoesNotExists(IEnumerable<IVocabulary> allVocabularies, ILogger log, bool debugBreak = true)
        {
            var noGroupingVocabularies = allVocabularies.Where(d => d.Grouping == null).ToList();

            if (noGroupingVocabularies.Any())
            {
                log.Warn(() => "Found {0} vocabularies with no grouping; Vocabularies: {1}".FormatWith(noGroupingVocabularies.Count, string.Join(", ", noGroupingVocabularies.Select(v => v.VocabularyName))));
                return true;
            }

            return false;
        }

        public bool VerifyKeyPrefixIsPopulated(IEnumerable<IVocabulary> allVocabularies, ILogger log, bool debugBreak = true)
        {
            var noKeyPrefixVocabularies = allVocabularies.Where(d => d.KeyPrefix == null).ToList();

            if (noKeyPrefixVocabularies.Any())
            {
                log.Warn(() => "Found {0} vocabularies with no key prefix; Vocabularies: {1}".FormatWith(noKeyPrefixVocabularies.Count, string.Join(", ", noKeyPrefixVocabularies.Select(v => v.VocabularyName ?? v.GetType().Name))));
                return true;
            }

            return false;
        }

        public bool VerifyNullPropertiesDoesNotExists(IEnumerable<(IVocabulary vocabulary, string propertyName, VocabularyKey vocabularyKey)> invalidPropertiesVocabularies, ILogger log, bool debugBreak = true)
        {
            var nullProperties = invalidPropertiesVocabularies.Where(t => t.vocabularyKey == null).ToList();

            if (nullProperties.Any())
            {
                return this.DoFail(
                        log,
                        () => "Found {0} vocabulary properties with null value; Vocabulary Properties: {1}".FormatWith(nullProperties.Count, string.Join(", ", nullProperties.Select(v => v.propertyName + " (" + v.vocabulary.VocabularyName + ")"))),
                        "Vocabulary properties with null value exists",
                        debugBreak
                    );
            }

            return false;
        }

        public bool VerifyKeyPropertiesWithNoVocabularyAssignedDoesNotExist(IEnumerable<(IVocabulary vocabulary, string propertyName, VocabularyKey vocabularyKey)> invalidPropertiesVocabularies, ILogger log, bool debugBreak = true)
        {
            var noVocabularyProperties = invalidPropertiesVocabularies.Where(t => t.vocabularyKey != null && t.vocabularyKey.Vocabulary == null).ToList();

            if (noVocabularyProperties.Any())
            {
                return this.DoFail(
                    log,
                    () => "Found {0} vocabulary keys with no associated vocabulary; Vocabulary Properties: {1}".FormatWith(noVocabularyProperties.Count, string.Join(", ", noVocabularyProperties.Select(v => v.propertyName + " (" + (v.vocabulary.VocabularyName ?? v.vocabulary.GetType().Name) + ")"))),
                    "Vocabulary keys with no associated vocabulary exists",
                    debugBreak
                );
            }

            return false;
        }

        public bool VerifyKeyPropertiesThatDoesNotMatchContainingVocabularyDoesNotExist(IEnumerable<(IVocabulary vocabulary, string propertyName, VocabularyKey vocabularyKey)> invalidPropertiesVocabularies, ILogger log, bool debugBreak = true)
        {
            var vocabulariesDoesNotMatchProperties  = invalidPropertiesVocabularies.Where(t => t.vocabularyKey != null && t.vocabularyKey.Vocabulary != null && t.vocabularyKey.Vocabulary != t.vocabulary).ToList();

            if (vocabulariesDoesNotMatchProperties.Any())
            {
                return this.DoFail(
                    log,
                    () => "Found {0} vocabulary keys where the vocabulary doesn't match; Vocabulary Properties: {1}".FormatWith(vocabulariesDoesNotMatchProperties.Count, string.Join(", ", vocabulariesDoesNotMatchProperties.Select(v => v.propertyName + " (" + v.vocabulary.VocabularyName + ")"))),
                    "Vocabulary keys where the vocabulary doesn't match exists",
                    debugBreak
                );
            }

            return false;
        }

        
        

        private bool DoFail(ILogger log, Func<string> logMessage, string exceptionMessage, bool debugBreak)
        {
            log.Warn(logMessage);

            if (debugBreak)
                System.Diagnostics.Debugger.Break();
            else
                return true;

            throw new ApplicationException(exceptionMessage);
        }

        public IEnumerable<(IVocabulary vocabulary, string propertyName, VocabularyKey vocabularyKey)> GetInvalidVocabularyProperties(IEnumerable<IVocabulary> allVocabularies)
        {
            return GetVocabularyProperties(allVocabularies)
                       .OrderBy(t => t.vocabulary.VocabularyName)
                       .ThenBy(t => t.propertyName)
                       .Where(t => t.vocabularyKey == null || t.vocabularyKey.Vocabulary == null || t.vocabularyKey.Vocabulary != t.vocabulary);
        }

        private static IEnumerable<(IVocabulary vocabulary, string propertyName, VocabularyKey vocabularyKey)> GetVocabularyProperties(IEnumerable<IVocabulary> vocabularies)
        {
            foreach (var vocabulary in vocabularies)
            {
                var properties = vocabulary.GetType().GetProperties();

                foreach (var property in properties)
                {
                    if (!property.CanRead || !typeof(VocabularyKey).IsAssignableFrom(property.PropertyType))
                        continue;

                    if (property.Name == "CompositeKey")
                        continue;

                    var propertyValue = property.GetValue(vocabulary) as VocabularyKey;

                    yield return (vocabulary, property.Name, propertyValue);
                }
            }
        }
    }
}
```