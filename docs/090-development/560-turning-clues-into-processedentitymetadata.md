---
layout: default
title: Turning Clues into ProcessedEntityMetadata
parent: Development
nav_order: 560
permalink: /developer/processedentitymetadata
tags: ["development", "clues"]
---

An Entity contains a property called a ProcessedEntityMetadata. This stores the preferred values for properties from all the clues into a unified set of properties. What dictates these values will vary, but it essentially comes down to:

 - The values that are the latest instance of a property.
 - The values that have the highest data metric scores.
 - A combination of the highest data metrics and the source "trust" score that is set on the integration. 