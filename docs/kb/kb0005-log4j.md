---
layout: default
title: CluedIn Security - Log4j2 CVE-2021-44228
permalink: /kb/log4j
nav_exclude: true
tags: ["security"]
last_modified: 2022-01-31
---

On December 9th 2021 a high severity vulnerability was disclosed in the Apache Log4j2 library for all 
versions between 2.0-beta9 and 2.14.1. This library is used by a significant amount of Java based 
applications and services.

At CluedIn, we build .NET and Node.js services that are not impacted by the vulnerability. 
However, we do utilise some third-party services that are Java based.

This announcement details the usage of those services and their exposure to CVE-2021-44228.

## Update: CVE-2021-45046
After the intial wave of fixes an additonal issue was discovered ([CVE-2021-45-46](https://nvd.nist.gov/vuln/detail/CVE-2021-45046#vulnCurrentDescriptionTitle)) which highlighted that in some cases the proposed fixes for CVE-2021-44228 were insufficient.  

In all cases, no actions are required for CluedIn services.  Notably Elasticsearch may have false positives, however [Elastic reccomends](https://discuss.elastic.co/t/apache-log4j2-remote-code-execution-rce-vulnerability-cve-2021-44228-esa-2021-31/291476#update-dec-15-10) the same changes as for the orginal CVE.

Therefore, there are no additonal requirments for fixes with CluedIn.

## Neo4j

All versions of CluedIn use the 3.5.x (currently 3.5.29) version of the community edition of Neo4j or 
an earlier version. 

As identified in the [Neo4j repository](https://github.com/neo4j/neo4j/issues/12796#issuecomment-992289758https://github.com/neo4j/neo4j/issues/12796), versions prior to 4.2 used a custom logging framework and are 
not affected by the vulnerability.

Additionally – Neo4j is not exposed to the public internet so user crafted requests that could expose 
the vulnerability cannot be targeted to the service.

### Actions Required

No action is required for the current nor any previous version of CluedIn.

## Elasticsearch

CluedIn 3.1.0-3.2.5 uses the 7.8.0 version of Elasticsearch. As identified by [Elastic](https://discuss.elastic.co/t/apache-log4j2-remote-code-execution-rce-vulnerability-cve-2021-44228-esa-2021-31/291476), Elasticsearch 
version 7.8+ running on JDK9+ are not susceptible.

CluedIn 3.0.0 uses 7.6.2 and will require setting a JVM option to prevent exposure.

Additionally – Elasticsearch is not exposed to the public internet so user crafted requests that could 
expose the vulnerability cannot be targeted to the service.

### Actions Required

CluedIn Version 3.0.0

• In your `values.yml` set the following

```yaml
elasticsearch:
 esJavaOpts: “-Dlog4j2.formatMsgNoLookups=true”
```

• Perform a `helm upgrade` with the new `values.yml`

No action is required for version 3.1+ of CluedIn.

## OpenRefine

CluedIn 3.2.2-3.2.5 uses the 3.4.1 version of OpenRefine. OpenRefine uses version 1.x of Log4j
which does not contain the features which enable exposure to the vulnerability.

All earlier versions of CluedIn use the 3.1 version of OpenRefine. Again, version 1.x of Log4j is used, 
which does not contain the features which enable exposure to the vulnerability.

### Actions Required

No action is required.

## Related links

* [https://www.randori.com/blog/cve-2021-44228/](https://www.randori.com/blog/cve-2021-44228/)
* [https://github.com/mubix/CVE-2021-44228-Log4Shell-Hashes](https://github.com/mubix/CVE-2021-44228-Log4Shell-Hashes)
* [https://msrc-blog.microsoft.com/2021/12/11/microsofts-response-to-cve-2021-44228-apache-log4j2/](https://msrc-blog.microsoft.com/2021/12/11/microsofts-response-to-cve-2021-44228-apache-log4j2/)
* [https://www.synopsys.com/blogs/software-security/zero-day-exploit-log4j-analysis/](https://www.synopsys.com/blogs/software-security/zero-day-exploit-log4j-analysis/)
* [https://blog.sonatype.com/a-new-0-day-log4j-vulnerability-discovered-in-the-wild](https://blog.sonatype.com/a-new-0-day-log4j-vulnerability-discovered-in-the-wild)
* [https://securelist.com/cve-2021-44228-vulnerability-in-apache-log4j-library/105210/](https://securelist.com/cve-2021-44228-vulnerability-in-apache-log4j-library/105210/)
* [https://nvd.nist.gov/vuln/detail/CVE-2021-44228](https://nvd.nist.gov/vuln/detail/CVE-2021-44228)
* [https://blog.cloudflare.com/inside-the-log4j2-vulnerability-cve-2021-44228/](https://blog.cloudflare.com/inside-the-log4j2-vulnerability-cve-2021-44228/)
* [https://github.com/neo4j-graphql/neo4j-graphql-java/issues/260](https://github.com/neo4j-graphql/neo4j-graphql-java/issues/260)
* [https://github.com/neo4j/neo4j/issues/12796](https://github.com/neo4j/neo4j/issues/12796)
* [https://www.elastic.co/blog/detecting-log4j2-with-elastic-security](https://www.elastic.co/blog/detecting-log4j2-with-elastic-security)
* [https://discuss.elastic.co/t/apache-log4j2-remote-code-execution-rce-vulnerability-cve-2021-44228-esa-2021-31/291476](https://discuss.elastic.co/t/apache-log4j2-remote-code-execution-rce-vulnerability-cve-2021-44228-esa-2021-31/291476)
* [https://blog.cloudflare.com/cve-2021-44228-log4j-rce-0-day-mitigation/](https://blog.cloudflare.com/cve-2021-44228-log4j-rce-0-day-mitigation/)