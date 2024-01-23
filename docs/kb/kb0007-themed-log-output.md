---
layout: cluedin
title: "Disabling colors in CluedIn log output"
description: "Disabling colors in CluedIn log output"
permalink: /kb/themed-log-output
nav_exclude: true
tags: ["logging", "configuration"]
last_modified: 2022-05-05
is_kb: true
---

CluedIn uses Serilog for logging. By default, logs are formatted with an ANSI color theme.

If you wish to disable this and output just plain text logs, you can do so by adding the following line to your configuration:

```yaml
CLUEDIN_appSettings__Serilog_ThemedLogOutput: "false"
```

