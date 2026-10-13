---
title: Crawler validation framework
url: https://documentation.cluedin.net/develop/integrations/crawler-validation-framework
content_type: reference
section: Develop & APIs > Build integrations
---

# Crawler validation framework

> reference: Facts, options, APIs.

When [building](https://documentation.cluedin.net/develop/integrations/build-integration.md) new integrations for CluedIn, it’s important to follow the recommended practices. The crawler validation framework helps developers ensure that each [clue](https://documentation.cluedin.net/get-started/core-concepts/clue-reference.md) they produce is ready for processing at the highest quality level.

- The framework runs only in Debug/Developer mode and is disabled in production.

- The framework acts as a guide by warning developers when key properties might be missing—for example, a `Uri` or `Name`. While it’s normal in some cases not to have these properties, they are easy to overlook, which is why the framework highlights them.

- In situations where you know a property cannot be produced, you can suppress the validators at the Clue Producer level.

Up: [Build integrations](https://documentation.cluedin.net/develop/integrations.md)
