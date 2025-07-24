---
layout: cluedin
title: Supported and unsupported characters
parent: Knowledge base
permalink: {{ site.baseurl }}/kb/supported-characters
nav_order: 13
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article, you'll find reference information about supported and unsupported characters in clues and entities.

{:.important}
If your data contains unsupported characters, remove them before submitting data to CluedIn.

## Supported characters

All valid Unicode characters are supported. Exceptions include Unicode surrogate blocks, `0xFFFE`, and `0xFFFF`.

```
 Characters:      0x9, 0xA, 0xD,
 Character Range: 0x20-0xD7FF
 Character Range: 0xE000-0xFFFD
 Character Range: 0x10000-0x10FFFF
```

Unicode control characters or undefined Unicode characters should not be used but are supported. These are within the following character ranges.

```
 0x7F-0x84
 0x86-0x9F
 0xFDD0-0xFDEF
 0x1FFFE-0x1FFFF
 0x2FFFE-0x2FFFF
 0x3FFFE-0x3FFFF
 0x4FFFE-0x4FFFF
 0x5FFFE-0x5FFFF
 0x6FFFE-0x6FFFF
 0x7FFFE-0x7FFFF
 0x8FFFE-0x8FFFF
 0x9FFFE-0x9FFFF
 0xAFFFE-0xAFFFF
 0xBFFFE-0xBFFFF
 0xCFFFE-0xCFFFF
 0xDFFFE-0xDFFFF
 0xEFFFE-0xEFFFF
 0xFFFFE-0xFFFFF
 0x10FFFE-0x10FFFF
```

## Unsupported characters

ASCI control characters are not supported. Exceptions include `0x9`, `0xA`, and `0xD`, which are valid characters.

- Character range `0x-0x1F` is not supported.
- Character `0x7F` is technically supported but should not be used.
- Unicode surrogate blocks are not supported.
- `0xFFFE` and `0xFFFF` are not supported.