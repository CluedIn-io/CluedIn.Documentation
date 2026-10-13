---
title: Publish & consume
url: https://documentation.cluedin.net/publish
content_type: landing
---

# Publish & consume

How do I get trusted data out?
  Data engineers and integration developers.

Streams push golden records continuously to an export target; GraphQL and the [REST API](https://documentation.cluedin.net/api.md) pull them on demand. Start with the export target you need, then build the stream that feeds it.

## In this section

- [Streams](https://documentation.cluedin.net/publish/streams.md): A stream is a continuous export: you define which golden records and which properties, point it at an export target, and CluedIn keeps the target up to date as the data changes.
- [Export targets](https://documentation.cluedin.net/publish/export-targets.md): An export target is the destination a stream writes to.
- [GraphQL](https://documentation.cluedin.net/publish/graphql.md): GraphQL is the query interface for reading golden records on demand, as opposed to streams, which push them continuously.
- [Integration patterns](https://documentation.cluedin.net/publish/integration-patterns.md): Worked patterns for getting trusted data out of CluedIn and into the systems that need it, including writing corrected values back to the systems the data came from.
