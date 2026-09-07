---
layout: cluedin
title: Crawler validation framework
parent: Build integrations
grand_parent: Develop & APIs
nav_order: 40
permalink: /develop/integrations/crawler-validation-framework
content_type: reference
redirect_from: ["/crawling/crawler-validation-framework"]
source_path: docs/040-integration/crawlers/140-crawler-validation-framework.md
tags: ["crawling","agents"]
---

When [building](/develop/integrations/build-integration) new integrations for CluedIn, it’s important to follow the recommended practices. The crawler validation framework helps developers ensure that each [clue](/get-started/core-concepts/clue-reference) they produce is ready for processing at the highest quality level.

- The framework runs only in Debug/Developer mode and is disabled in production.

- The framework acts as a guide by warning developers when key properties might be missing—for example, a `Uri` or `Name`. While it’s normal in some cases not to have these properties, they are easy to overlook, which is why the framework highlights them.

- In situations where you know a property cannot be produced, you can suppress the validators at the Clue Producer level.