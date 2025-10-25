---
layout: cluedin
title: Delete individual data parts
parent: Golden records
grand_parent: Key terms and features
permalink: /golden-records/delete-data-parts-from-golden-records
nav_order: 5
has_children: false
---

In this article, you will learn how to delete specific data parts (also referred to as records) from a golden record. For more information about records, data parts, and golden records, see [Data life cycle](/key-terms-and-features/data-life-cycle).

If you no longer need specific data parts that form a golden record, you can easily delete them. You can delete data parts from a golden record in two places:

- [On the **History** tab](#delete-data-parts-in-history) – use this option if you want to have a detailed and chronological view of all data parts forming a golden record. For more details, see [History](/key-terms-and-features/golden-records/history).

- [On the **Topology** tab](#delete-data-parts-in-topology) – use this option if you want to have a visual representation of how a golden record is formed.

{:.important}
Deleting data parts from a golden record is different from [removing records from a data source](/integration/additional-operations-on-records/remove-records). When you remove records from a data source, all data parts originating from that source are removed from every golden record in which they are used. On the contrary, deleting data parts from a golden record allows you to delete specific data parts originating from almost any source. In this case, the data parts are deleted only from the specific golden record.

Deleting data parts from either the **History** tab or the **Topology** tab produces the same result: the data part is removed from the golden record. However, there are several cases when you cannot delete data parts from a golden record. A data part cannot be deleted from a golden record under the following conditions:

- If it is the only data part that contains the origin code of the golden record.

- If it is a manual merge data part. You can undo the manual merge on the **Topology** tab.

- If it is a deduplication project merge data part. You can undo the deduplication project merge on the **Topology** tab.

- If it is one of two data parts that contribute to the merge data part.

Even though you can delete a data part from an enricher, keep in mind that it may appear again. To prevent this, deactivate the related enricher before deleting a data part.

## Delete data parts in History

On the **History** tab of a golden record, you can find all data parts that form a golden record. If you don't need a specific data part in a golden record, you can delete it.

**To delete data parts on the History tab**

1. Find the data part that you want to delete.

1. On the right side of the row, select the three-dot button (⋮) > **Delete**.

    ![delete-data-part-history-1.png]({{ "/assets/images/golden-records/delete-data-part-history-1.png" | relative_url }})

    Alternatively, select the record ID. In the data part details pane that opens, select **Delete**.

1. Review the data part that will be deleted, and then select **Next**.

1. Confirm that you want to delete the data part by entering _DELETE_. Then, select **Confirm**.

    ![delete-data-part-history-2.gif]({{ "/assets/images/golden-records/delete-data-part-history-2.gif" | relative_url }})

    The data part is removed from the **History** tab. Consequently, all changes that the data part contributed to the golden record are also removed.

## Delete data parts in Topology

On the **Topology** tab of a golden record, you view how the data parts forming a golden record are linked. If you don't need a specific data part in a golden record, you can delete it.

**To delete data parts on the Topology pane**

1. Find and select the data part that you want to delete.

1. In the data part details pane that opens, select **Delete**.

1. Review the data part that will be deleted, and then select **Next**.

1. Confirm that you want to delete the data part by entering _DELETE_. Then, select **Confirm**.

    ![delete-data-part-topology.gif]({{ "/assets/images/golden-records/delete-data-part-topology.gif" | relative_url }})

    The data part is removed from the **Topology** tab. Consequently, all changes that the data part contributed to the golden record are also removed.