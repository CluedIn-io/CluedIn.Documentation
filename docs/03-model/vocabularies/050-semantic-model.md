---
layout: cluedin
title: Semantic model
parent: Vocabularies
grand_parent: Model
nav_order: 50
permalink: /model/vocabularies/semantic-model
content_type: how-to
---

## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

The **Semantic model** shows how vocabulary keys map into one another, and lets you map keys at scale: drag from one key onto another, review every change, and save them all at once. In this article, you will learn how to read the Semantic model and how to map, change and remove vocabulary key mappings with it.

For what a vocabulary key mapping does to your data, see [Map one vocabulary key to another](/model/vocabularies/manage-vocabulary-keys#map-one-vocabulary-key-to-another).

## Prerequisites

- To view the Semantic model, you need access to the data catalog.
- To save mapping changes straight away, you need to be an owner of the vocabulary of each changed key, or have accountable access to the data catalog. Otherwise, your changes are sent to the vocabulary's owners for approval.

## Where to find the Semantic model

The same Semantic model appears on three pages. Each page shows the keys that matter there, and offers only the actions that make sense there.

| Page | Path | What it shows |
|---|---|---|
| Vocabulary | **Management** > **Data catalog** > **All Vocabulary** > a vocabulary > **Semantic model** | This vocabulary and every vocabulary downstream of it. Full editing. |
| Vocabulary key | A vocabulary key > **Semantic model** | This key, every key that maps into it and every key it maps into. Only this key's mappings can be changed. |
| Golden record | A golden record > **Semantic model** | The keys that have a value on this record, with the record's values, and the keys they map into. |

On a golden record's **Properties** tab, a property whose key is part of a mapping has an information icon next to it. Select the icon to open that key's **Semantic model** tab and see where the value comes from and where it goes.

![Properties tab of a golden record with the information icon next to a mapped property and its tooltip]({{ "/assets/images/management/data-catalog/semantic-model-properties-link.png" | relative_url }})

## Read the Semantic model

![Semantic model tab of a vocabulary with the Filters panel, three layer columns, and lines between vocabulary keys]({{ "/assets/images/management/data-catalog/semantic-model-vocabulary.png" | relative_url }})

- **Layers** – vocabularies are laid out in columns from left to right: Layer 1, Layer 2 and so on, up to 10. A vocabulary sits one layer to the right of the highest layer of any vocabulary that maps into it. On a vocabulary page, Layer 1 holds only that vocabulary and is locked.

- **Vocabulary cards** – each vocabulary is one card with its business domain icon, name, key prefix and number of keys. Each key in the card shows its name, key, data type and, on a golden record, the record's value.

- **Lines** – a line goes from a key to the key it maps into. A dashed orange line is a change that is not saved yet. A **Type** badge means the two keys have different data types. A **Copy** badge means the value is kept in both keys instead of moving.

- **Filters** – narrow the board by business domain, vocabulary, data type, mapping and usage, or search by key name, key or vocabulary. Keys that don't match are dimmed, not hidden. Turn off **Show layer columns** to hide the column backgrounds.

Select a key to open **Key details**: how many records have a value for it, what it maps to and from, where it is used, and sample values.

![Key details panel of a vocabulary key showing records with a value, its mapping, where it is used, and sample values]({{ "/assets/images/management/data-catalog/semantic-model-key-details.png" | relative_url }})

On a vocabulary key page, the Semantic model is that key's lineage: where its value comes from and where it goes.

![Semantic model tab of a vocabulary key showing the key highlighted as This key, the key that maps into it, and the key it maps into]({{ "/assets/images/management/data-catalog/semantic-model-vocabulary-key.png" | relative_url }})

On a golden record, each key shows the record's value. Mapping changes made here still apply to every record that uses those keys.

![Semantic model tab of a golden record with each key showing this record's value]({{ "/assets/images/management/data-catalog/semantic-model-golden-record.png" | relative_url }})

## Map a vocabulary key

**To map a vocabulary key to another**

1. Drag the blue dot on the right of the key onto the key you want to map it to.

    While you drag, every key is marked: a teal outline for the same data type, an amber outline for a different data type, and greyed out when the key can't be a target. A hint above the board counts each kind and says when the drop would replace an existing mapping.

    ![Dragging a key's blue dot, with possible targets outlined in teal or amber and the rest greyed out]({{ "/assets/images/management/data-catalog/semantic-model-drag.png" | relative_url }})

1. Drop the dot on the key. The new mapping appears as a dashed orange line, and the bar at the bottom of the board shows how many changes are pending.

A key maps to one key only, so mapping an already mapped key replaces its mapping. Mappings go one way, left to right. You can't map a key into:

- another key of the same vocabulary;
- the vocabulary you are viewing, on its own page;
- a key whose chain leads back to the key you are dragging (a loop);
- a key that would push the chain past 10 layers;
- the key it already maps to.

Different data types are allowed. The line gets a **Type** badge and the **Mapping** panel shows a warning, so check the sample values before saving.

On a vocabulary key page, you can only map that key, or map another key into it. To change other mappings in its chain, open the Semantic model of their vocabulary.

### Change or remove a mapping

Select a line to open the **Mapping** panel. It shows the source and target keys and the mapping's status: **Saved**, **Not saved yet** or **Reprocessing**.

![Mapping panel showing the source and target keys, the copy switch, and Remove mapping]({{ "/assets/images/management/data-catalog/semantic-model-mapping-panel.png" | relative_url }})

- To keep the value in the source key as well as the target key, turn on **Keep the value in [source key] too (copy)**. By default, the value moves.

- To remove the mapping, select **Remove mapping**, or hover over the line and select the delete icon in the middle of it.

On a vocabulary page, you can also use the menu of a vocabulary or of a layer column, or select several vocabularies with their checkboxes, to remove their mappings or remove them from the model. **Delete layer** removes every vocabulary in that layer from the model, together with their mappings. Removing a vocabulary from the model only removes it from the board; its mappings are removed as pending changes.

Every change shows a message with an **Undo** action. You can also undo and redo with the toolbar buttons, or with Ctrl+Z and Ctrl+Shift+Z.

### Add vocabulary keys

To bring other keys onto the board, select **Add vocabulary keys** and pick the keys. A vocabulary new to the board lands in a new layer on the right. You can drag a vocabulary by its header into another layer, from Layer 2 onwards, but never to the left of a vocabulary that maps into it. Adding keys is not a change that needs saving.

### Suggest AI mappings

Select **Suggest AI mappings** to get suggested mappings for the keys that are not mapped yet. By default, the suggestions go into the vocabularies this one already maps into; use **Suggest mappings into** to choose others. Suggestions show on the board as dashed purple lines. Accept or dismiss them one by one, or select several and accept or dismiss them together. An accepted suggestion becomes a pending change like any other.

![AI mapping suggestions panel with the Suggest mappings into selection]({{ "/assets/images/management/data-catalog/semantic-model-ai-suggestions.png" | relative_url }})

## Save your changes

Nothing is saved until you save it, and you save all pending changes at once.

1. In the bar at the bottom of the board, select **Save changes**.

1. Review the changes, any data type warnings, and how many records will be reprocessed. Then, select **Save and reprocess**.

    ![Save changes dialog listing an added mapping, a data type warning, and the number of records to reprocess]({{ "/assets/images/management/data-catalog/semantic-model-save.png" | relative_url }})

The bar shows the reprocessing progress while the board stays usable, and the affected lines are animated until it's done. When reprocessing finishes, the board refreshes and a message says how many records were reprocessed.

![Reprocessing bar at the bottom of the board with a progress bar and record count]({{ "/assets/images/management/data-catalog/semantic-model-reprocessing.png" | relative_url }})

If you are not an owner of the vocabulary, your changes are sent to its owners for approval instead. To drop every pending change, select **Discard**; you can undo that too.

## Verify the result

- When saving finishes, the lines you changed are solid again and the **Mapping** panel shows **Saved**. While records are being reprocessed, it shows **Reprocessing**.
- The message at the end of reprocessing tells you the work has finished, not just that it was accepted.
- Saved mapping changes appear in the vocabulary's **Audit log** tab, with who made each change and when.

## What this changes

- Saving a mapping change updates the source key's mapping and reprocesses the records that use the keys involved, so values move (or, with copy, are copied) into the target key on every golden record, not only the one you are looking at.
- The copy setting is stored as a **Copy Value** rule on the source key.
- Adding keys, moving vocabularies between layers, reordering keys and removing vocabularies from the model only change the board. They are not saved.
- A saved mapping change can be reversed by removing or changing the mapping and saving again, which reprocesses the records again.
