---
layout: cluedin
title: Edge Types
parent: Development
nav_order: 380
has_children: false
permalink: /development/edge-types
tags: ["development","edges"]
---

Edges Types are a way to determine the relationships between data. This is typically in the structure of a Object - Verb - Object. For example, John - works at - Lego. In CluedIn, edges can store properties such as weights and general metadata, but the main idea behind these edges is to describe the relationship of two nodes for processing and querying purposes. 

In CluedIn, there are static Edge Types and Dynamic Edge Types. Static Edge Types are your way to set an Edge Type based off known rules that will not change. All other Edge Types should be Dynamic. 

It is always recommended to leave Edges in crawlers as generic as possible and introduce new processors in the processing server to dynamically resolve generic edge types into specific ones. Imagine you have an edge type of "Works At" that you set statically in your crawlers - you can see that it has a temporal factor to it, in that you have no guarantee that this will always be "Works At". Due to this, you can introduce new processors that would check other values e.g. A Job start and end date, and use this to dynamically change the edge type to "Worked At" if this person was ever to leave. Here is a list of the Edge Types that are in the base installation of CluedIn: 

```csharp
namespace CluedIn.Core.Data
{
    /// <summary>
    /// The entity edge type.
    /// </summary>
    public partial class EntityEdgeType
    {
        /**********************************************************************************************************
         * FIELDS
         **********************************************************************************************************/

        /// <summary>At edge type</summary>
        public static readonly EntityEdgeType At = "/At";

        /// <summary>The created at</summary>
        public static readonly EntityEdgeType CreatedAt = "/CreatedAt";

        /// <summary>The modified at edge type</summary>
        public static readonly EntityEdgeType ModifiedAt = "/ModifiedAt";

        /// <summary>The discovered at edge type</summary>
        public static readonly EntityEdgeType DiscoveredAt = "/DiscoveredAt";

        /// <summary>The author edge type</summary>
        public static readonly EntityEdgeType Author = "/Author";

        /// <summary>The birthday edge type</summary>
        public static readonly EntityEdgeType Birthday = "/Birthday";

        /// <summary>The part of edge type</summary>
        public static readonly EntityEdgeType PartOf = "/PartOf";

        /// <summary>The parent edge type</summary>
        public static readonly EntityEdgeType Parent = "/Parent";

        /// <summary>The located in</summary>
        public static readonly EntityEdgeType LocatedIn = "/LocatedIn";

        /// <summary>The follows</summary>
        public static readonly EntityEdgeType Follows = "/Follows";

        /// <summary>The used by</summary>
        public static readonly EntityEdgeType UsedBy = "/UsedBy";

        /// <summary>The requested by</summary>
        public static readonly EntityEdgeType RequestedBy = "/RequestedBy";

        /// <summary>The mentioned</summary>
        public static readonly EntityEdgeType Mentioned = "/Mentioned";

        /// <summary>The represents.</summary>
        public static readonly EntityEdgeType Represents = "/Represents";

        /// <summary>The action</summary>
        public static readonly ActionEntityEdgeType Action = new ActionEntityEdgeType();

        /**********************************************************************************************************/

        public static readonly EntityEdgeType SimilarTo      = "/SimilarTo";
        public static readonly EntityEdgeType WorksFor       = "/WorksFor";
        public static readonly EntityEdgeType Read           = "/Read";
        public static readonly EntityEdgeType ReadWrite      = "/ReadWrite";
        public static readonly EntityEdgeType InvitedTo      = "/InvitedTo";
        public static readonly EntityEdgeType StartedOn      = "/StartedOn";
        public static readonly EntityEdgeType EndedOn        = "/EndedOn";
        public static readonly EntityEdgeType Received       = "/Received";
        public static readonly EntityEdgeType DueOn          = "/DueOn";
        public static readonly EntityEdgeType WitheldIn      = "/WitheldIn";
        public static readonly EntityEdgeType DeletedBy      = "/DeletedBy";
        public static readonly EntityEdgeType CompletedOn    = "/CompletedOn";
        public static readonly EntityEdgeType ManagedIn      = "/ManagedIn";
        public static readonly EntityEdgeType AttachedTo     = "/AttachedTo";
        public static readonly EntityEdgeType Deployed       = "/Deployed";
        public static readonly EntityEdgeType Has            = "/Has";
        public static readonly EntityEdgeType Involves       = "/Involves";
        public static readonly EntityEdgeType MemberOf       = "/MemberOf";
        public static readonly EntityEdgeType WorkedOn       = "/WorkedOn";
        public static readonly EntityEdgeType WorkedOnBy     = "/WorkedOnBy";
        public static readonly EntityEdgeType Recipient      = "/Recipient";
        public static readonly EntityEdgeType CreatedBy      = "/CreatedBy";
        public static readonly EntityEdgeType Created        = "/Created";
        public static readonly EntityEdgeType For            = "/For";
        public static readonly EntityEdgeType Attended       = "/Attended";
        public static readonly EntityEdgeType Presented      = "/Presented";
        public static readonly EntityEdgeType Owns           = "/Owns";
        public static readonly EntityEdgeType OwnedBy        = "/OwnedBy";
        public static readonly EntityEdgeType Registered     = "/Registered";
        public static readonly EntityEdgeType ManagedBy      = "/ManagedBy";
        public static readonly EntityEdgeType Modified       = "/Modified";
        public static readonly EntityEdgeType ModifiedBy     = "/ModifiedBy";
        public static readonly EntityEdgeType Competitor 	 = "/Competitor";
        public static readonly EntityEdgeType IsType         = "/Is";
        public static readonly EntityEdgeType Investor       = "/Investor";
        public static readonly EntityEdgeType ApprovedBy     = "/ApprovedBy";

        /**********************************************************************************************************
         * INNER TYPES
         **********************************************************************************************************/

        public class ActionEntityEdgeType : HierarichalEntityEdgeType
        {
            public readonly EntityEdgeType ModifiedBy = "/Action/ModifiedBy";
            public readonly EntityEdgeType CreatedBy  = "/Action/CreatedBy";
            public readonly EntityEdgeType RemovedBy  = "/Action/RemovedBy";
            public readonly EntityEdgeType RevertedBy = "/Action/RevertedBy";
            public readonly EntityEdgeType SynchedBy  = "/Action/SynchedBy";

            protected override EntityEdgeType BaseType { get { return "/Action"; } }
        }

        public abstract class HierarichalEntityEdgeType
        {
            /// <summary>Gets the entity type base.</summary>
            /// <value>The entity type base.</value>
            protected abstract EntityEdgeType BaseType { get; }

            /// <summary>Implements the operator ==.</summary>
            /// <param name="type1">The type1.</param>
            /// <param name="type2">The type2.</param>
            /// <returns>The result of the operator.</returns>
            public static bool operator ==(EntityEdgeType type1, HierarichalEntityEdgeType type2) 
            {
                return type1 == (EntityEdgeType)type2;
            }

            /// <summary>Implements the operator !=.</summary>
            /// <param name="type1">The type1.</param>
            /// <param name="type2">The type2.</param>
            /// <returns>The result of the operator.</returns>
            public static bool operator !=(EntityEdgeType type1, HierarichalEntityEdgeType type2) 
            {
                return type1 != (EntityEdgeType)type2;
            }

            /// <summary>Implements the operator ==.</summary>
            /// <param name="type1">The type1.</param>
            /// <param name="type2">The type2.</param>
            /// <returns>The result of the operator.</returns>
            public static bool operator ==(HierarichalEntityEdgeType type1, EntityEdgeType type2) 
            {
                return ((EntityEdgeType)type1) == type2;
            }

            /// <summary>Implements the operator !=.</summary>
            /// <param name="type1">The type1.</param>
            /// <param name="type2">The type2.</param>
            /// <returns>The result of the operator.</returns>
            public static bool operator !=(HierarichalEntityEdgeType type1, EntityEdgeType type2) 
            {
                return ((EntityEdgeType)type1) != type2;
            }

            /// <summary>
            /// Performs an implicit conversion from <see cref="HierarichalEntityType"/> to <see cref="EntityType"/>.
            /// </summary>
            /// <param name="type">The type.</param>
            /// <returns>The result of the conversion.</returns>
            public static implicit operator EntityEdgeType(HierarichalEntityEdgeType type)
            {
                return type.BaseType;
            }

            /// <summary>
            /// Performs an implicit conversion from <see cref="HierarichalEntityEdgeType"/> to <see cref="System.String"/>.
            /// </summary>
            /// <param name="type">The type.</param>
            /// <returns>The result of the conversion.</returns>
            public static implicit operator string(HierarichalEntityEdgeType type)
            {
                return type.BaseType;
            }

            /// <summary>
            /// Returns a <see cref="System.String" /> that represents this instance.
            /// </summary>
            /// <returns>A <see cref="System.String" /> that represents this instance.</returns>
            public override string ToString()
            {
                return ((EntityEdgeType)this).ToString();
            }

            /// <summary>Returns a hash code for this instance.</summary>
            /// <returns>
            /// A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table. 
            /// </returns>
            public override int GetHashCode()
            {
                return ((EntityEdgeType)this).GetHashCode();
            }

            /// <summary>
            /// Determines whether the specified <see cref="System.Object" />, is equal to this instance.
            /// </summary>
            /// <param name="obj">The <see cref="System.Object" /> to compare with this instance.</param>
            /// <returns>
            ///   <c>true</c> if the specified <see cref="System.Object" /> is equal to this instance; otherwise, <c>false</c>.
            /// </returns>
            public override bool Equals(object obj)
            {
                return this.BaseType.Equals(obj);
            }
        }
    }
}
```
